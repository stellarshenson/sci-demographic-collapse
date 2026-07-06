# Reports - Figures & Tables

Executed figures and tables from the SOTA campaign (Notebooks 3-8). Each figure is generated in place by its
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

**Recalibration (Notebook 7, E12)**
- `nb7_e12h40_collapse.png` - ELBO posterior collapse: median overshoot, large gap, near-zero latent usage
- `nb7_e12_loss_landscape.png` - Wasserstein loss basin + Adam descent; ELBO collapses τ→0 while WAE keeps it finite
- `nb7_e12h41_closure.png` - the Wasserstein median tracks the recent dip the ELBO smooths away
- `nb7_e12h42_tournament.png` - method tournament (ELBO vs MMD vs exact-Wasserstein) on gap, MAPE, population residual
- `nb7_e12h43_coverage.png` - hierarchical drift-pooling restores held-out TFR coverage to 100%
- `nb7_e12h44_crisis.png` - the recalibration preserves all four crisis footprints

**Contrarian audit (Notebook 8, E13)**
- `nb8_contrarian_scorecard.png` - 25-cell survive/qualify grid (12 findings survived, 13 qualified)
- `nb8_qualified_findings.png` - the strongest qualifications (USA quantum falls, migration-led change, migration stabilizes Korea)

**Reversal interventions (Notebook 9, E14)**
- `nb9_e14_seldon_manifold.png` - the bistable recovery/collapse basin with regions placed and interventions as moves across the separatrix
- `nb9_e14_drivers.png` - drivers of the 2100 decline (quantum deficit dominant) and the stylized keystone (childlessness ρ)
- `nb9_e14_interventions.png` - single-intervention effects and the road to reversal (USA reverses, Korea bends)

## Tables

- `nb4_parameter_table.csv` - ELBO posterior parameters (means ± CI) and free energy F at the optimum, per region (superseded by nb7)
- `nb4_predictions.csv` - ELBO prediction vs observed (2023) with residuals (superseded by nb7)
- `nb7_parameter_table.csv` - recalibrated Wasserstein parameters (level, drift, τ, σ, MI-usage), per region
- `nb7_predictions.csv` - recalibrated prediction vs observed (2023): ELBO vs Wasserstein residuals, TFR and population
- `nb5_crisis_costs.csv` - demographic cost per crisis (forgone births / excess deaths)
- `nb6_projection_table.csv` - 2100 population, baseline and change from 2023
- `nb9_intervention_catalogue.csv` - the 14 reversal interventions (type, lever, ΔTFR, literature grounding)
- `nb9_reversal_table.csv` - each intervention's 2100 population effect per region

## Verdict records

- `nb3_round1_verdicts.json`, `nb4_round23_verdicts.json`, `nb5_crisis_verdicts.json`, `nb6_intervention_verdicts.json`, `nb7_recalibration_verdicts.json`, `nb8_contrarian_verdicts.json`, `nb9_reversal_verdicts.json`
