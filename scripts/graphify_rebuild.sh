#!/usr/bin/env bash
# Local graphify rebuild harness - part of the project, NOT part of the make-build package.
# Rebuilds the knowledge graph for the whole project scope (code + record docs)
# into a temporary out dir. Reuses graphify's semantic cache, so unchanged files
# cost nothing; uncached docs need an LLM backend (gemini key or claude CLI).
#
#   scripts/graphify_rebuild.sh [OUT_DIR]
#
# OUT_DIR defaults to /tmp/graphify-sci-demographic-collapse (temporary artefact).
set -euo pipefail

PROJECT=/home/lab/workspace/learning/projects/sci-demographic-collapse
OUT=${1:-/tmp/graphify-sci-demographic-collapse}
mkdir -p "$OUT/graphify-out"
cd "$OUT"

# resolve the graphify interpreter (pipx/uv-tool install)
PY=$(uv tool run graphifyy python -c "import sys; print(sys.executable)" 2>/dev/null || true)
if [ -z "$PY" ]; then PY=$(head -1 "$(which graphify)" | tr -d '#!'); fi
"$PY" -c "import graphify" || { echo "graphify not importable via $PY"; exit 1; }
echo -n "$PY" > graphify-out/.graphify_python
echo "$PROJECT" > graphify-out/.graphify_root

# 1. detect + scope: src/tests code, record docs (no papers/images/digests/@archive)
"$PY" - "$PROJECT" <<'EOF'
import json, sys
from pathlib import Path
from graphify.detect import detect
root = sys.argv[1]
r = detect(Path(root))
def keep_code(f): return "/src/" in f or "/tests/" in f
def keep_doc(f):
    if "/references/papers" in f or "/@archive" in f or "/.ipynb_checkpoints" in f: return False
    return f.endswith(".md") and ("/docs/" in f or f == root + "/README.md"
                                  or "/reports/" in f or "/logs/" in f)
files = {"code": [f for f in r["files"]["code"] if keep_code(f)],
         "document": [f for f in r["files"]["document"] if keep_doc(f)],
         "paper": [], "image": [], "video": []}
words = sum(len(open(f, errors="ignore").read().split()) for v in files.values() for f in v)
r.update(files=files, total_files=sum(map(len, files.values())), total_words=words)
Path("graphify-out/.graphify_detect.json").write_text(json.dumps(r))
print(f"scoped: {r['total_files']} files, {words} words")
EOF

# 2. AST extraction (deterministic, free)
"$PY" - <<'EOF'
import json
from pathlib import Path
from graphify.extract import collect_files, extract
detect = json.loads(Path("graphify-out/.graphify_detect.json").read_text())
code = []
for f in detect["files"]["code"]:
    code.extend(collect_files(Path(f)) if Path(f).is_dir() else [Path(f)])
result = extract(code, cache_root=Path(".")) if code else {"nodes": [], "edges": [], "input_tokens": 0, "output_tokens": 0}
Path("graphify-out/.graphify_ast.json").write_text(json.dumps(result))
print(f"AST: {len(result['nodes'])} nodes, {len(result['edges'])} edges")
EOF

# 3. semantic extraction: cache first, LLM backend for the uncached remainder
BACKEND=""
if [ -n "${GEMINI_API_KEY:-}${GOOGLE_API_KEY:-}" ]; then BACKEND="gemini";
elif command -v claude >/dev/null 2>&1; then BACKEND="claude-cli"; fi
"$PY" - "$BACKEND" <<'EOF'
import json, sys
from pathlib import Path
from graphify.cache import check_semantic_cache, save_semantic_cache
backend = sys.argv[1]
detect = json.loads(Path("graphify-out/.graphify_detect.json").read_text())
all_files = [f for v in detect["files"].values() for f in v]
c_nodes, c_edges, c_hyper, uncached = check_semantic_cache(all_files)
print(f"semantic cache: {len(all_files) - len(uncached)} hit, {len(uncached)} uncached")
n_nodes, n_edges, n_hyper = [], [], []
if uncached and backend:
    from graphify.llm import extract_corpus_parallel
    new = extract_corpus_parallel(uncached, backend=backend)
    n_nodes, n_edges = new.get("nodes", []), new.get("edges", [])
    n_hyper = new.get("hyperedges", [])
    save_semantic_cache(n_nodes, n_edges, n_hyper)
elif uncached:
    print(f"WARNING: no LLM backend - {len(uncached)} files get AST-only coverage")
Path("graphify-out/.graphify_semantic.json").write_text(json.dumps(
    {"nodes": c_nodes + n_nodes, "edges": c_edges + n_edges,
     "hyperedges": c_hyper + n_hyper, "input_tokens": 0, "output_tokens": 0}))
print(f"semantic: {len(c_nodes) + len(n_nodes)} nodes, {len(c_edges) + len(n_edges)} edges")
EOF

# 4. merge, build, cluster, report, exports
"$PY" - <<'EOF'
import json
from pathlib import Path
from graphify.build import build_from_json
from graphify.cluster import cluster, score_all
from graphify.analyze import god_nodes, surprising_connections, suggest_questions
from graphify.report import generate
from graphify.export import to_json
ast = json.loads(Path("graphify-out/.graphify_ast.json").read_text())
sem = json.loads(Path("graphify-out/.graphify_semantic.json").read_text())
seen = {n["id"] for n in ast["nodes"]}
nodes = ast["nodes"] + [n for n in sem["nodes"] if n["id"] not in seen]
merged = {"nodes": nodes, "edges": ast["edges"] + sem["edges"],
          "hyperedges": sem.get("hyperedges", []), "input_tokens": 0, "output_tokens": 0}
Path("graphify-out/.graphify_extract.json").write_text(json.dumps(merged))
detection = json.loads(Path("graphify-out/.graphify_detect.json").read_text())
G = build_from_json(merged)
communities = cluster(G)
labels = {cid: "Community " + str(cid) for cid in communities}
questions = suggest_questions(G, communities, labels)
report = generate(G, communities, score_all(G, communities), labels, god_nodes(G),
                  surprising_connections(G, communities), detection,
                  {"input": 0, "output": 0}, ".", suggested_questions=questions)
Path("graphify-out/GRAPH_REPORT.md").write_text(report)
to_json(G, communities, "graphify-out/graph.json")
print(f"graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges, {len(communities)} communities")
EOF
graphify export html || true
echo "outputs in $OUT/graphify-out/ (graph.json, GRAPH_REPORT.md, graph.html)"
