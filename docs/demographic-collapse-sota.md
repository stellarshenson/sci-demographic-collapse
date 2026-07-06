# Demographic Collapse - SOTA Model

**Canonical SOTA Document**

The distilled, calibrated design that survived the E1-E11 experiment campaign - an age-structured
cohort-component model of national populations, driven by observed UN WPP 2024 schedules, calibrated by
variational free-energy minimization, backtested out-of-sample, stress-tested against past crises, and used
to size interventions to 2100. The full evidence trail is in
[the experiments log](experiments/demographic-collapse-experiments.md); the executable record is Notebooks
3-6 and the reusable core module `src/sci_demographic_collapse/coremodel.py`.

## Overview

The project began as a stylized nine-state ODE (Notebook 1) and a scalar calibration (Notebook 2). Those
established the qualitative picture - a bistable "Seldon manifold" whose ridge lands on the literature's
TFR-1.5 low-fertility trap - but the scalar state could not carry an age pyramid, so population momentum had
to be reframed rather than reproduced. The SOTA model fixes that: the state is the population as a vector of
single-year age buckets, and everything that matters - fertility, mortality, migration - is a function of
age. On that footing the model reproduces the demographic accounting exactly, separates recoverable
postponement from real fertility loss, states its own uncertainty, predicts unseen years, reproduces four
historical crises, and projects the consequences of policy - the requirements of a model one can trust.

## The model

The state is two age vectors, female and male, `Nᶠ, Nᵐ ∈ ℝ¹⁰¹` over single years 0-100+ (thousands). One
year is a linear operator - the **Leslie map** - a weighted directed graph with a Markov aging backbone and a
fertility renewal edge:

- **Aging** - `N′ₐ = Nₐ₋₁ · Sₐ` for ages 1-99, with the open interval at 100+ accumulating; `Sₐ` is the
  life-table survival-into-age ratio (`Sₐ = L(a)/L(a-1)`, `S₀ = L₀/l₀` for birth → age 0)
- **Births** - `B = Σₐ fₐ · Nᶠₐ` over ages 15-49, with `fₐ` the per-woman age-specific fertility rate;
  newborns enter age 0 split by the sex ratio at birth and the birth-survival `S₀`
- **Deaths** - the closed-population identity `D = (ΣN + B) − ΣN′`
- **Migration** - net migrants added by a Rogers-Castro age schedule (a labour-force peak plus a childhood
  echo), scaled to the annual net-migration total

The eigenstructure of the Leslie operator carries the long-run fate directly: the dominant eigenvalue λ₁ is
the intrinsic growth rate (r = ln λ₁) and its eigenvector the stable age pyramid. Across the study regions λ₁
orders monotonically by fertility - all below 1 (every region is sub-replacement), USA highest (0.992), Korea
lowest (0.970, r = −3.1%/yr). Momentum - the growth built into a non-stationary pyramid - is the Keyfitz ratio
computed from that eigenvector, and it is finite and depleting: the USA has spent its positive momentum,
sliding from 1.09 in 1990 to 0.98 in 2023, while Japan and Korea sit deep in negative momentum.

**Fidelity** - driven by observed schedules, the one-step operator reproduces annual births to 0.17% and
deaths to 0.00% (E6-H21). A closed run (no migration) undershoots the observed total by exactly the migration
contribution; adding Rogers-Castro migration closes the USA total to 0.06% MAPE and beats an age-uniform
allocation at the labour ages (E7-H24).

## Calibration - tempo, quantum, and free energy

A falling period TFR mixes two things the model must tell apart. The **Bongaarts-Feeney** decomposition
`adjTFR = TFR/(1 − r)`, with `r` the rate of rise of the mean age at childbearing, splits the observed rate
into recoverable **tempo** (births postponed to later ages) and structural **quantum** (completed fertility).
The result reframes the collapse question region by region: the USA's low period TFR is largely tempo - its
quantum sits near or above replacement - whereas Korea's is a genuine quantum deficit (E8-H26/H27). A
two-parameter skew-normal located at the mean age and scaled to the quantum reconstructs the single-year ASFR
to within 3% of its peak (E8-H28), giving the calibration a low-dimensional, interpretable fertility driver.

That driver is calibrated by **variational inference** - Pyro SVI on a local-linear-trend state-space model
of the quantum - which minimizes the variational free energy F = −ELBO. The converged posterior is the
minimum-free-energy state the project set out to reach; it comes with credible bands, and the stochastic
trend is chosen deliberately so forecast uncertainty grows with horizon rather than pretending to false
confidence. In-sample the SVI converges, beats the frozen-rate baseline, and its 95% band covers the observed
series (E9-H29). The posterior parameter table (per-region level, drift, volatility, noise, and F at the
optimum) is exported to `reports/nb4_parameter_table.csv`.

## What the model reproduces

**Backtest (E9-H30)** - trained on 1990-2015 and asked to predict 2016-2023, the model's **population**
forecast holds everywhere (MAPE ≤ 3%: USA 1.16%, Korea 2.58%, Italy 0.26%). Period-TFR point-forecast
coverage, by contrast, is regime-dependent: Korea's monotone collapse is forecastable (88%), but the USA and
Italy underwent post-2015 regime changes no prior data anticipates. This split is the project's sharpest
lesson - **population is predictable, period TFR is not**, because momentum and age structure, not this year's
fertility rate, govern the medium term.

**Crisis battery (E10)** - four historical crises are reproduced and their demographic cost measured by
counterfactual:

- **COVID-19** is a *mortality* shock - modelled excess deaths of 985k over 2020-21, matching the real ≈1M -
  with a fertility dip that was mostly recoverable tempo and rebounded by 2022
- **The 2008 recession** hit the USA as *postponement* first: the 2007-2013 fall was only ~4% quantum
  (tempo), but it never recovered and cost ≈2.8M births cumulatively
- **Korea's 1997 IMF crisis** is a *permanent quantum step* (92% quantum, no recovery through 2005, ≈3.15M
  forgone)
- **German reunification** shows the East German fertility collapse in the national aggregate (≈0.72M forgone)

The tempo-quantum lens is what makes the distinction crisp - a recoverable postponement told apart from a
permanent loss - the same axis that decides whether an intervention can work.

## Interventions and the forward outlook

Held at current fertility, the ultra-low societies roughly halve by 2100 - Korea −63% (51.8M → 19M), Japan
−52%, Italy −39% - while the USA is buffered near flat (+6%) by migration (E11-H37). The collapse is not a
distant risk; it is locked into today's age structure. Interventions can bend the far tail: a phased fertility
lift (attention-economy regulation plus relationship-skills training, +0.30 TFR from 2025) raises the 2100
population materially (USA +73M, Korea +4.6M), but the first two to three decades barely move - momentum is
the reason policy must act early (E11-H38). And the tempo-quantum split decides the leverage: the USA's
recoverable-postponement shortfall returns it to growth with a modest lift, whereas Korea's structural
quantum deficit needs a near-replacement lift, started now rather than in twenty years, merely to stabilize
(E11-H39). The analysis is descriptive - it sizes a lever, it does not claim any policy achieves it.

## Numbers - parameters and predictions

- **Parameter + calibration table** - `reports/nb4_parameter_table.csv` (posterior means and credible
  intervals, F at the optimum, per region)
- **Prediction vs observed (2023) with residuals** - `reports/nb4_predictions.csv`. Population residuals are
  0.1-1.9%; period-TFR point residuals carry a ~+0.2 smoothing bias because the posterior median does not
  chase the recent dip (the credible band covers, and the quantum decomposition carries the interpretable
  signal)
- **Crisis costs** - `reports/nb5_crisis_costs.csv` (forgone births / excess deaths per crisis)
- **Forward projections** - `reports/nb6_projection_table.csv` (2100 population, baseline and interventions)

## The story it tells

- **Momentum governs timing and depth** - the answer to the project's central question. Low fertility sets the
  destination; the age pyramid sets when and how steeply a population gets there. It is why the USA and Korea,
  both sub-replacement, are on utterly different trajectories, and why the near-term is unmovable
- **Tempo is not quantum** - a large part of the developed-world "fertility crisis" is postponement, and how
  much of it is recoverable versus permanent is measurable and differs sharply by country
- **Population is trustworthy, period TFR is not** - the model earns confidence exactly where age structure
  dominates and admits its limits where behaviour surprises
- **The Seldon manifold survived** - the bistable ridge found in stylized equations landed, uncalibrated, on
  the empirical TFR-1.5 low-fertility trap, and the calibrated model places every region correctly along it

## Honest limitations

- **Period-TFR point forecasts** carry a smoothing bias and cannot anticipate regime changes; trust the
  population trajectory and the credible bands, not a single TFR number
- **Migration assumptions** drive the buffered cases - Germany's +12% to 2100 rests on the elevated
  2019-2023 net migration (the 2022 Ukraine surge inflates the recent mean); the migration *age shape* is a
  canonical Rogers-Castro schedule, not a fitted one
- **National aggregate only** - sub-national divergence (East/West Germany after 1990) is not resolved
- **Behavioural sub-questions unresolved** - the technology-and-formation hypotheses stay on a lagging
  marriage proxy (a measurement gap, not a settled negative); a house-price series was never ingested
- **Descriptive, not causal** - the model sizes mechanisms and levers; it licenses no claim that a given
  policy achieves a given lever

## Reproducibility

- **Notebooks** - `03-kj-demographic-sota` (age-structured core, E6-E7), `04-kj-demographic-calibration-bayes`
  (tempo-quantum + Bayesian, E8-E9), `05-kj-demographic-crises` (crisis battery, E10),
  `06-kj-demographic-interventions` (forward projections, E11); all execute end-to-end on the pinned GPU
- **Core module** - `src/sci_demographic_collapse/coremodel.py` (Leslie map, momentum, eigenstructure,
  Rogers-Castro, counterfactual overrides), imported by Notebooks 4-6
- **Data** - `data/raw/unwpp/` (UN WPP 2024, CC BY 3.0 IGO) plus the World Bank / Eurostat / OWID behavioural
  panel; provenance in `data/raw/README.md`, `data/raw/unwpp/README.md`, and the per-source manifests
- **Figures** - sixteen executed figures in `reports/figures/`; tables in `reports/*.csv`
