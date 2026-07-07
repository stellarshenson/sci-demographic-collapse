"""Structural + syntax validation for every notebook.

Full end-to-end execution of the notebooks needs a CUDA GPU and the UN WPP dataset (under
``data/raw/``, deliberately not committed), so it cannot run on a stock GitHub runner. What
CI *can* guarantee, and this does for every notebook, is that it is a valid ``nbformat``
document and that every code cell compiles (no syntax errors) - so a broken or corrupted
notebook fails the build. Full execution is a local / self-hosted-GPU-runner step:

    jupyter nbconvert --to notebook --execute --inplace \
        --ExecutePreprocessor.kernel_name=sci-demographic-collapse notebooks/<nb>.ipynb
"""
import ast
from pathlib import Path

import nbformat
import pytest

NB_DIR = Path(__file__).resolve().parent.parent / "notebooks"
NOTEBOOKS = sorted(NB_DIR.glob("*.ipynb"))


def _strip_magics(source: str) -> str:
    """Drop IPython line/cell magics and shell escapes so the cell is plain-python parseable."""
    keep = []
    for line in source.splitlines():
        stripped = line.lstrip()
        if stripped.startswith(("%", "!", "?")):
            continue
        keep.append(line)
    return "\n".join(keep)


def test_notebooks_present():
    assert NOTEBOOKS, "no notebooks found under notebooks/"


@pytest.mark.parametrize("nb_path", NOTEBOOKS, ids=lambda p: p.name)
def test_notebook_valid_and_code_compiles(nb_path):
    nb = nbformat.read(nb_path, as_version=4)
    nbformat.validate(nb)
    for i, cell in enumerate(nb.cells):
        if cell.cell_type != "code":
            continue
        code = _strip_magics(cell.source)
        if not code.strip():
            continue
        try:
            ast.parse(code)
        except SyntaxError as exc:  # pragma: no cover - failure path
            pytest.fail(f"{nb_path.name} code cell {i} has a syntax error: {exc}")
