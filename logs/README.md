# Logs

Progress logs for background and long-running jobs.

- `torch-install.log` - `make install` run that adds the GPU (torch) stack
- `nb-execute.log` - end-to-end execution of `notebooks/01-kj-demographic-collapse.ipynb`
- `ingest-worldbank.log` - World Bank Open Data ingestion (15 indicators x 4 regions) into `data/raw/worldbank/`
- `ingest-secondary.log` - Eurostat age-at-first-birth + OWID marriage-rate ingestion into `data/raw/`
- `nb2-execute.log` - end-to-end execution of `notebooks/02-kj-demographic-calibration.ipynb`
- `unwpp-ingest.log` - UN WPP 2024 bulk-CSV streaming ingestion into `data/raw/unwpp/`
- `make-install-pyro.log` - `make install` adding the Bayesian stack (pyro-ppl, arviz)
- `nb3-execute.log` - execution of `notebooks/03-kj-demographic-sota.ipynb` (age-structured core, E6-E7)
- `nb4-execute.log` - execution of `notebooks/04-kj-demographic-calibration-bayes.ipynb` (tempo-quantum + Bayesian, E8-E9)
- `nb5-execute.log` - execution of `notebooks/05-kj-demographic-crises.ipynb` (crisis battery, E10)
- `nb6-execute.log` - execution of `notebooks/06-kj-demographic-interventions.ipynb` (interventions, E11)
