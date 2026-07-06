# sci-demographic-collapse

Simulation and hypothesis testing of demographic collapse around the world.

> **Note**: Generated with copier-data-science template v1.2+
> For template documentation, visit [copier-data-science](https://github.com/stellarshenson/copier-data-science)

## Purpose

This project simulates population dynamics and uses those simulations to state and test hypotheses about demographic collapse - the sustained shrinking and rapid ageing of a population driven by fertility falling below the replacement level. The aim is to understand how, when, and why collapse unfolds differently across the world, and what separates a country that merely stops growing from one that enters accelerating decline.

The central question is whether a low fertility rate alone predicts collapse, or whether the current **age structure** - the population's built-in momentum - governs the timing and depth of the decline. A young population can keep growing for decades after fertility drops below replacement, then fall sharply once that momentum is spent; an already-aged population collapses much sooner from the same fertility gap.

- **Phenomenon** - sustained sub-replacement fertility (total fertility rate below ~2.1 births per woman) → long-run population decline and ageing
- **Simulation** - project age-structured populations forward in time under assumptions about fertility, mortality, and migration
- **Hypotheses** - identify the drivers of collapse timing and severity: population momentum, age structure, the pace of fertility change, and migration
- **Comparative scope** - contrast trajectories across countries and regions worldwide, from ultra-low-fertility to high-fertility regimes
- **Nature** - a learning and exploratory project, not a production forecasting system

Modelling approach, data sources, and the specific countries or regions covered are intentionally left open at this stage and will be decided as the work develops.

## Quick Start

```bash
make install
```

## Makefile Targets

- `make install` - Create environment and install package
- `make test` - Run tests
- `make lint` / `make format` - Check / fix code style
- `make build` - Build distributable wheel
- `make clean` - Remove compiled files and caches
- `make .env` / `make .env.enc` - Decrypt / encrypt environment secrets
- `make help` - Show all available targets

## Best Practices

- **Notebooks**: Name with number prefix, initials, description - `01-jqp-data-exploration.ipynb`
- **Data**: Keep `raw/` immutable, use `interim/` for transforms, `processed/` for final datasets
- **Source code**: Refactor reusable notebook code into `src/sci_demographic_collapse/` modules
- **Models**: Store trained models in `models/` with clear naming

## Project Organization

```
├── Makefile           <- Makefile with convenience commands
├── README.md          <- The top-level README for developers
├── data
│   ├── external       <- Data from third party sources
│   ├── interim        <- Intermediate data that has been transformed
│   ├── processed      <- The final, canonical data sets for modeling
│   └── raw            <- The original, immutable data dump
│
├── models             <- Trained and serialized models
├── notebooks          <- Jupyter notebooks
├── pyproject.toml     <- Project configuration and dependencies
├── references         <- Data dictionaries, manuals, explanatory materials
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures
├── tests              <- Test files
└── src
    └── sci_demographic_collapse   <- Source code for this project
        ├── __init__.py
        ├── config.py      <- Configuration variables
        ├── dataset.py     <- Data download/generation scripts
        ├── features.py    <- Feature engineering code
        ├── modeling
        │   ├── predict.py <- Model inference
        │   └── train.py   <- Model training
        └── plots.py       <- Visualization code
```
