# Logs

Progress logs for background and long-running jobs.

- `torch-install.log` - `make install` run that adds the GPU (torch) stack
- `nb-execute.log` - end-to-end execution of `notebooks/01-kj-demographic-collapse.ipynb`
- `ingest-worldbank.log` - World Bank Open Data ingestion (15 indicators x 4 regions) into `data/raw/worldbank/`
- `ingest-secondary.log` - Eurostat age-at-first-birth + OWID marriage-rate ingestion into `data/raw/`
- `nb2-execute.log` - end-to-end execution of `notebooks/02-kj-demographic-calibration.ipynb`
