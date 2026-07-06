<!-- @import /home/lab/workspace/.claude/CLAUDE.md -->

# Project-Specific Configuration

This file imports workspace-level configuration from `/home/lab/workspace/.claude/CLAUDE.md`.
All workspace rules apply. Project-specific rules below strengthen or extend them.

The workspace `/home/lab/workspace/.claude/` directory contains additional instruction files
(MERMAID.md, NOTEBOOK.md, DATASCIENCE.md, GIT.md, and others) referenced by CLAUDE.md.
Consult workspace CLAUDE.md and the .claude directory to discover all applicable standards.

## Mandatory Bans (Reinforced)

The following workspace rules are STRICTLY ENFORCED for this project:

- **No automatic git tags** - only create tags when user explicitly requests
- **No automatic version changes** - only modify version in package.json/pyproject.toml/etc. when user explicitly requests
- **No automatic publishing** - never run `make publish`, `npm publish`, `twine upload`, or similar without explicit user request
- **No manual package installs if Makefile exists** - use `make install` or equivalent Makefile targets, not direct `pip install`/`uv install`/`npm install`
- **No automatic git commits or pushes** - only when user explicitly requests

## Project Context

Data science learning project simulating population dynamics to state and test hypotheses about
demographic collapse - sustained sub-replacement fertility driving long-run population decline and
ageing. Central question: whether low fertility alone predicts collapse, or whether age structure and
population momentum govern the timing and depth of the decline. Comparative scope across countries and
regions. Exploratory, not a production forecasting system.

**Technology stack**:
- Python 3.13, `uv` environment manager (env name `sci-demographic-collapse`)
- `ruff` for linting and formatting (line length 99, isort enabled)
- `pytest` for testing
- Jupyter kernel support enabled
- Core deps: `loguru`, `tqdm`, `typer`, `python-dotenv`
- Module: `sci_demographic_collapse` under `src/`
- Scaffolded from `copier-data-science` v1.3.9; `.copier-answers.yml` is Copier-managed (never edit manually)

**Domain terminology**:
- Total fertility rate (TFR), replacement level (~2.1 births/woman)
- Age structure, population momentum, cohort projection
- Fertility, mortality, migration as projection drivers

**Environment / secrets**:
- `.env` is encryption-enabled (`make .env` / `make .env.enc` to decrypt / encrypt)

## Journal Rules (Project-Specific)

- **APPEND ONLY**: New journal entries MUST be appended at the end of the file, never inserted between existing entries
- Entries maintain strict chronological order by position - the last entry in the file is always the most recent work
- Never reorder, move, or insert entries out of sequence
- The Stellars **journal plugin** is the canonical tool for this file: create via `/journal:create`, append via `/journal:update`, archive via `/journal:archive`. The `journal:journal` skill auto-triggers on any mention of "journal" and runs `journal-tools check` after every write
- Direct edits to `JOURNAL.md` are a last resort - prefer the plugin so modus secundis format, continuous numbering and append-only order are enforced automatically

## Strengthened Rules

Rules from the workspace configuration that are especially load-bearing for this data science project:

- **Experiment / analysis work lives IN the notebook, never scratch scripts** - simulations, sweeps, and hypothesis tests are built as notebook cells and executed in place (`jupyter nbconvert --to notebook --execute --inplace`); no `/tmp/*.py` prototype-then-port. The notebook is the single source of record: code, outputs, figures, and conclusions together
- **Notebook structure** - follow the `notebook-standards` skill: standard section order, grouped imports, centralized configuration cell, markdown header before each major section, rich progress bars in a separate cell
- **Hypothesis-driven documentation** - use the `datascience:hypothesis` skill to maintain an append-only experiments log and a SOTA design doc when recording rounds and concluding on drivers of collapse
- **Data hygiene** - keep `data/raw/` immutable; use `data/interim/` for transforms and `data/processed/` for final datasets
- **Makefile is the entry point** - use `make install` / `make test` / `make lint` / `make format`, never manual `uv`/`pip` invocations
- **Rich output** - follow the `rich-output` / `datascience` skills for console and notebook formatting
