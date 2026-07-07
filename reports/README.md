# Reports - Figures & Tables

Executed figures and tables from the SOTA campaign (Notebooks 3-10). Each figure is generated in place by its
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

**Intervention story - the coupling keystone (Notebook 10, E15)**
- `nb10_act1_stakes.png` - baseline population to 2100 indexed to 100 (the stakes)
- `nb10_act2_decomposition.png` - extensive (childlessness) vs intensive (parity) deficit per region
- `nb10_act3_strength.png` - literature strength × margin map, and single-lever effect on the model
- `nb10_act4_manifold.png` - the Seldon manifold: keystone levers cross the separatrix, cash stalls
- `nb10_act5_keystone.png` - coupling & security levers with evidence-tier uncertainty bands
- `nb10_widermenu.png` - fourteen more levers colored by honest verdict (SUPPORTED / PARTIAL / REFUTED)
- `nb10_coupling_depth.png` - ten coupling-specific legislative + psychological levers (measured vs predicted, colored by verdict)
- `nb10_deep_drivers.png` - thirteen specific interventions on the career-first / arms-race / overwork life-script (measured / extrapolated / predicted, colored by verdict)
- `nb10_interactions.png` - the coupled-system interaction: the same keystone push flips the fate near the ridge, does nothing deep in the basin
- `nb10_act6_controversial_targeted.png` - contraception decision-architecture spectrum; age-targeted vs uniform cash
- `nb10_act7_verdict.png` - baseline vs the best well-aimed effort per region (who reverses, who bends)

**Incentives, arms races & defection (Notebook 11, E16)**
- `nb11_arms_race_defusal.png` - the admission-return slope (convex rank-skim vs flat lottery-band, 100% deflation) and net-after-defection for the five arms-race levers (a ban backfires, un-buyable levers do not)
- `nb11_wealth_compression.png` - the wealth/inheritance levers: gross shrinks to net as the rich defect, and the side-effect cost stacked against the net
- `nb11_western_experiments.png` - the four Western natural experiments: Israel composition vs secular default, Hungary tempo vs quantum, housing by tenure, student-debt delay
- `nb11_defection_screen.png` - the central result: every lever re-ranked by net-after-elite-defection (bans/propaganda/wealth-cap go negative, lottery/inequality/penalty rise)
- `nb11_side_effect_frontier.png` - the effect vs side-effect frontier (efficient vs dominated levers) and the manifold bundle crossing
- `nb11_manifold_bundles.png` - the same bundle amplifies near the ridge and stalls deep in the basin (robust crosses the separatrix, fragile does not)

**Swept design spans (Notebook 12, E17)**
- `nb12_coupling_economics.png` - coupling as a financial channel: the premium decomposition (~25% money), single-parent precarity by parity, and the solo-support sweep with its cohabitation cliff (interior optimum)
- `nb12_duration_fidelity.png` - the union-duration reward sweep (de-risk vs lock-in, interior-low) and the fidelity axis where the net sign-flips as coerciveness rises while S-W welfare harm explodes (the exit is the valve)
- `nb12_policy_geometry.png` - five delivery axes: universality (corner), benefit-form (interior=in-kind), permanence (corner), scale (corner=national), who-pays (sign-flip, employer-mandate goes negative)
- `nb12_surrogacy.png` - the surrogate-carrier market: a tiny demand gain post-displacement against the steep psychological/commodification and stratified-reproduction cost (the class is dominated)
- `nb12_optimum_taxonomy.png` - the optima classified (interior / corner / sign-flip) - no universal "turn it to 11"
- `nb12_manifold_bundles.png` - the robust valve-paired bundle crosses the Seldon separatrix where the coercive/dominated bundle stalls

**Hybrids and undercurrents (Notebook 13, E18)**
- `nb13_hybrids.png` - the eight hybrid blend curves (pure-A to pure-B) with the super-additive premium marked where complementary channels stack
- `nb13_financial.png` - financial/institutional undercurrents: the pension-fertility externality, UBI vs child-conditional, the precarity formation-brake
- `nb13_biological.png` - biological undercurrents: the egg-freezing option-value trap (sign-flip) and the fecundity floor (capped, minority driver)
- `nb13_cultural.png` - cultural/marriage-market undercurrents: hypergamy squeeze, one-child hysteresis, the grandmother effect, climate birth-strike, migrant convergence, urban density, status reversal
- `nb13_synthesis.png` - verdicts grouped by undercurrent channel, and the hybrid super-additive premium ranked

**Dynamical simulation - the model as judge (Notebook 14, E19)**
- `nb14_baseline.png` - baseline validation: the coupled model's TFR and coupling C to 2125, Korea alone crossing into the collapse basin (no intervention)
- `nb14_signals.png` - the three archetypal signals: tempo bumps-and-reverts, quantum needs coupling, coupling escapes the trap; the same quantum lever works in Germany but is gated in Korea
- `nb14_classes_position.png` - dynamical class of all ~88 interventions by region, and the same-lever Korea-vs-Germany position-dependence
- `nb14_interaction_timing.png` - a keystone bundle vs a cash bundle, started early vs a generation late: momentum makes timing decisive

**Seldon harbingers (Notebook 15, E20)**
- `nb15_harbingers.png` - every lever ranked by fertility improvement per composite cost, and the cost-vs-improvement scatter (cheap + high = harbinger)
- `nb15_ablation_core.png` - the full recovery bundle ablated to its lean cost-efficient core (dTFR kept, cost shed); coupling non-ablatable
- `nb15_timing_pareto_position.png` - the harbinger is cheaper earlier (timing), the cost-vs-improvement Pareto knee, and the same near-free lever by position (bends vs recovers)

**Structural levers + the education optimisation (Notebook 16, E22)**
- `nb16_structural_levers.png` - the five structural levers on Korea (trajectories) and their improvement-per-cost value ranking; marriageable-men is the only one that bends
- `nb16_cost_position.png` - fertility improvement by region and the composite-cost-vs-improvement scatter
- `nb16_policy_dose.png` - the sustained male-earnings gain Korea must manufacture to hold / bend / recover, in fracking-boom-equivalents
- `nb16_income_vs_degrees.png` - the education paradox: raising male income vs male degrees (the degree route's arms-race drag)
- `nb16_male_attainment_interaction.png` - income vs degrees vs both (the super-additive interaction)
- `nb16_composites_ablation.png` - the contrarian income bundle (income + kin + equity-at-home) beats degrees+cash, and its ablated core

## Tables

- `nb4_parameter_table.csv` - ELBO posterior parameters (means ± CI) and free energy F at the optimum, per region (superseded by nb7)
- `nb4_predictions.csv` - ELBO prediction vs observed (2023) with residuals (superseded by nb7)
- `nb7_parameter_table.csv` - recalibrated Wasserstein parameters (level, drift, τ, σ, MI-usage), per region
- `nb7_predictions.csv` - recalibrated prediction vs observed (2023): ELBO vs Wasserstein residuals, TFR and population
- `nb5_crisis_costs.csv` - demographic cost per crisis (forgone births / excess deaths)
- `nb6_projection_table.csv` - 2100 population, baseline and change from 2023
- `nb9_intervention_catalogue.csv` - the 14 reversal interventions (type, lever, ΔTFR, literature grounding)
- `nb9_reversal_table.csv` - each intervention's 2100 population effect per region
- `nb10_strength_table.csv` - E15 literature-graded strength catalogue (ΔTFR, margin, durability, evidence tier, per-effect citation)
- `nb10_decomposition.csv` - extensive vs intensive deficit per region (childlessness gap vs parity gap)
- `nb10_verdict_table.csv` - E15 baseline vs max keystone+migration 2100 outcome per region (reversal flag)
- `nb10_e15_verdicts.json` - all 27 E15 verdicts (H51-H77) with evidence
- `nb11_defection_table.csv` - E16 lever catalogue with named incentive, gross/δ/backfire/net, side-effect cost, margin, tier, verdict
- `nb11_frontier_table.csv` - E16 net-after-defection vs side-effect cost per lever (the frontier)
- `nb11_e16_verdicts.json` - all 25 E16 verdicts (H101-H125) with evidence
- `nb12_span_table.csv` - E17 swept-span catalogue: named incentive, optimum type + location, net, side-cost, δ, verdict
- `nb12_e17_verdicts.json` - all 18 E17 verdicts (H126-H143) with evidence
- `nb13_lever_table.csv` - E18 hybrid + creative-lever catalogue: undercurrent, optimum type + location, net, verdict
- `nb13_e18_verdicts.json` - all 20 E18 verdicts (H144-H163) with evidence
- `nb14_dynamical_table.csv` - E19 dynamical re-judgement: each intervention's channel, Korea/Germany 2125 TFR + population gain, and dynamical class
- `nb14_e19_verdicts.json` - full E19 dynamical results for all 88 interventions across Korea/Germany/France
- `nb15_harbinger_table.csv` - E20 lever ranking: composite cost, Korea dTFR, improvement-per-cost efficiency, Seldon fate
- `nb15_e20_verdicts.json` - the six E20 Seldon-harbinger verdicts (H164-H169) with evidence

## Verdict records

- `nb3_round1_verdicts.json`, `nb4_round23_verdicts.json`, `nb5_crisis_verdicts.json`, `nb6_intervention_verdicts.json`, `nb7_recalibration_verdicts.json`, `nb8_contrarian_verdicts.json`, `nb9_reversal_verdicts.json`
