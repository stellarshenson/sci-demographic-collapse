# Reports - Figures & Tables

Executed figures and tables from the SOTA campaign (Notebooks 3-6). Each figure is generated in place by its
notebook and exported here; the tables are machine-readable CSVs. Full narrative in
[`docs/demographic-collapse-sota.md`](../docs/demographic-collapse-sota.md); evidence trail in
[`docs/experiments/demographic-collapse-experiments.md`](../docs/experiments/demographic-collapse-experiments.md).

## Figures (`figures/`)

**Age-structured core (Notebook 3, E6-E7)**
- `nb3_e6h21_fidelity.png` - one-step operator fidelity (births 0.17%, deaths 0.00%) and the closed-run migration gap
- `nb3_e6h22_momentum.png` - USA population momentum spent (1.09 → 0.98); momentum by region
- `nb3_e6h23_eigenstructure.png` - Leslie transition graph, eigenspectrum, and λ ordered by TFR
- `nb3_e7h24_migration.png` - Rogers-Castro migration schedule and the total-population closure
- `nb3_e7h25_decomposition.png` - natural change vs net migration, USA/Italy/Korea

**Calibration (Notebook 4, E8-E9)**
- `nb4_e8_tempo_quantum.png` - period TFR vs tempo-adjusted quantum; recoverable vs structural shortfall
- `nb4_e8h28_asfr.png` - skew-normal reconstruction of the ASFR schedule
- `nb4_e9h29_calibration.png` - ELBO convergence and the calibrated TFR credible band
- `nb4_e9h30_backtest.png` - held-out backtest (train ≤ 2015); population predictable, TFR regime-dependent

**Crisis battery (Notebook 5, E10)**
- `nb5_e10h32_recession.png` - 2008 recession: TFR fall and forgone births
- `nb5_e10h33_covid.png` - COVID: life-expectancy shock (excess deaths) and the tempo fertility dip
- `nb5_e10h34h35_korea_germany.png` - Korea 1997 permanent step; German reunification aggregate dip
- `nb5_e10h36_synthesis.png` - crisis cost ranking (mortality vs fertility shocks)

**Interventions (Notebook 6, E11)**
- `nb6_e11h37_baseline.png` - baseline projection to 2100 (current fertility persists)
- `nb6_e11h38_interventions.png` - interventions bend the far tail; momentum locks the near term
- `nb6_e11h39_leverage.png` - Korea leverage: only a structural, early lift stabilizes

## Tables

- `nb4_parameter_table.csv` - posterior parameters (means ± CI) and free energy F at the optimum, per region
- `nb4_predictions.csv` - prediction vs observed (2023) with TFR and population residuals
- `nb5_crisis_costs.csv` - demographic cost per crisis (forgone births / excess deaths)
- `nb6_projection_table.csv` - 2100 population, baseline and change from 2023

## Verdict records

- `nb3_round1_verdicts.json`, `nb4_round23_verdicts.json`, `nb5_crisis_verdicts.json`, `nb6_intervention_verdicts.json`
