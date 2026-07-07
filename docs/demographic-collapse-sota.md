# Demographic Collapse - SOTA Model

**Canonical SOTA Document**

The distilled, calibrated design that survived the E1-E13 experiment campaign - an age-structured
cohort-component model of national populations, driven by observed UN WPP 2024 schedules, calibrated by
free-energy minimization with an information-preserving Wasserstein objective, backtested out-of-sample,
stress-tested against past crises, used to size interventions to 2100, put through a 25-hypothesis
contrarian audit of its own findings, and used to catalogue and model the full menu of reversal interventions.
The full evidence trail is in
[the experiments log](experiments/demographic-collapse-experiments.md); the executable record is Notebooks
3-9 and the reusable core module `src/sci_demographic_collapse/coremodel.py`.

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

That driver is calibrated on a local-linear-trend state-space model of the quantum by minimizing a free
energy - a reconstruction term plus a divergence that keeps the latent trend close to its prior. The first
attempt used the variational free energy F = −ELBO (Pyro SVI), and it failed in an instructive way: its
posterior median over-predicted the recent period TFR by +0.2 to +0.3 at 2023. The cause is **posterior
collapse** - the ELBO applies a Kullback-Leibler penalty to *every* latent innovation, so the optimiser
drives the innovation scale τ toward zero and the trend flattens into a line that cannot bend to the recent
decline (E12-H40: mean gap 0.198, τ → 0.004, near-zero latent usage).

The fix keeps the reconstruction term but replaces the per-point KL with a penalty on the **aggregate**
posterior only - a Wasserstein Auto-Encoder / InfoVAE(α = 1) objective. Because it constrains the pooled
latent distribution rather than each point, it preserves the mutual information between latent and data, and
the latent is free to track the observed series. A three-way tournament (ELBO vs RBF-MMD vs exact
one-dimensional Wasserstein-2) picks the exact optimal-transport penalty: it closes the in-sample 2023 gap to
≈ 0.018 with mutual-information usage restored to 0.96 and a 2023 population residual of 0.69%, beating both
MMD and the ELBO (E12-H41/H42). This aggregate-divergence free energy is the minimum-free-energy state the
project set out to reach - now without the collapse. The recalibrated per-region parameter table (level,
drift, innovation scale τ, noise σ) is exported to `reports/nb7_parameter_table.csv`.

## What the model reproduces

**Backtest (E9-H30, E12-H43)** - trained on 1990-2015 and asked to predict 2016-2023, the model's
**population** forecast holds everywhere (MAPE ≤ 1%). Period-TFR *point* forecasts still cannot anticipate a
post-2015 regime change - an intrinsic limit of any period-rate forecast - but the recalibration handles it
honestly: pooling the drift across regions (the mechanism behind the UN's bayesTFR) widens the forecast band
so the held-out TFR is covered 100% rather than confidently missed (up from 50% without pooling). The lesson
stands in a sharper form - **population is point-predictable, period TFR is only interval-predictable** -
because momentum and age structure, not this year's fertility rate, govern the medium term.

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

A fuller reversal analysis (E14) catalogues fourteen plausible interventions - state policy (childcare,
allowances, leave, housing, assisted reproduction, migration) and cultural change (gender equity, union
formation, norms) - and projects each on the calibrated core, with three images: the Seldon manifold, the
drivers, and the interventions. Three findings sharpen the outlook. On the stylized manifold every lever is a
directed move - cost, childcare and gender-equity policies lower childlessness while formation policies raise
coupling, both pushing a region leftward across the separatrix toward recovery (E14-H50). The drivers rank
cleanly - the quantum deficit dominates the 2100 decline (Korea 28M of a 32M loss), migration is a strong
second (14M), and recoverable tempo is least (3M), so the heaviest levers are the ones that raise completed
fertility (E14-H49). And reversal is a property of position, not effort: a serious state-and-culture bundle
plus migration returns the tempo-recoverable USA to growth (+129%, E14-H47), but the same maximal effort only
bends ultra-low Korea from a 63% collapse to a 10% decline by 2100 (E14-H48), because its reproductive base is
already hollowed out. No single policy is a cure (E14-H46); only an early, broad bundle moves the trajectory,
and where a region sits on the manifold decides whether it reverses the trend or merely softens it.

The final round (E15) grounds every intervention's strength in the (quasi-)experimental literature and repairs
two gaps in the E14 catalogue. First, it splits fertility into its extensive (childlessness) and intensive
(parity) margins and shows that for Germany, Italy and Japan the deficit is extensive - nearly three in ten
women never have a child - so the missing births are missing mothers, the coupling keystone, not missing third
children (Korea alone is a quantum-collapse special case). Second, it re-grades the strengths against the
evidence and the record: childcare and gender equity are the strongest durable levers, while cash is weak and
temporary - Korea's USD 270B over two decades is the proof - and the difference between a keystone bundle and
an equal-sized cash bundle is durability, not magnitude. Fifty hypotheses, each riding on an already-proven
finding and bounded to a real-world ceiling, return an honest mix of 37 SUPPORTED, 10 PARTIAL and 3 REFUTED:
rolling back gender equality backfires and a paternity father-quota moves norms but not births, while cutting
extreme working hours and building family-size housing emerge as underused levers beside the keystone. A
coupling-in-depth chapter tests ten legislative and psychological levers (France's PACS and de-escalating
Korea's gender war are measured and effective; restricting divorce backfires; state matchmaking makes marriages
without moving a birth rate), and a deeper-drivers chapter targets the binding constraint the obvious levers
miss - the career-first / education-arms-race / overwork life-script (Poland deployed free nurseries and a
93-billion-euro cash program and still fell to ~1.1). Every lever carries an interactions-and-side-effects
reading: the coupled ODE amplifies a keystone push near the ridge and damps it deep in the basin, and cash,
divorce restriction and gender-neutral career policies carry documented countervailing effects. A decision-
maker's star-ranking with mechanism-of-effect chains is regenerated on demand via the `/write-interventions`
command, and the source library lives in `references/papers/` (37 PDFs + 60 digests) with composed proxy
blueprints for un-tested levers in `references/proxies/`. The controversial contraception lever is measured, not endorsed - powerful by raw magnitude but
coercive, non-durable and blind to the keystone. A society escapes the Seldon manifold by attacking the
coupling keystone early, broadly and durably while it still sits near the ridge (E15).

A further round (E16) sharpens the intervention analysis on a principle the earlier rounds left implicit:
gross effect sizes lie, because interventions are evaded. It adds a defection parameter to every lever - the
net a society gets is the gross times the compliant share, plus a backfire term that can invert the sign when
the rich defect. Twenty-five hypotheses (H101-H125, 15 SUPPORTED, 6 PARTIAL, 4 REFUTED) name the exact
incentive each lever moves and isolate its key signal statistically before sizing it. The lesson is a
re-ranking: an outright tutoring ban backfires (Korea 1980 - the rich bought covert tutoring and inequality
widened), while a lottery-band that makes the admission prize un-buyable, or a multi-dimensional test rewarding
un-coachable traits, deflate the arms race at its source and cannot be defected from. The defection screen
drops bans, propaganda, wealth caps and exhortation below zero and lifts inequality compression, lottery
bucketing, universal motherhood-penalty removal and structural defaults to the top - what a state can enforce,
not what sounds strong, is what bends the curve. The Western natural experiments anchor the Western half:
Israel's near-universal default plus universal IVF holds even secular fertility near replacement without
coercion, Hungary's 5-6% of GDP buys mostly tempo, and housing's real lever is supply for young renters, not a
price subsidy to owners. Stacked against their side effects, the coercive levers are dominated; the efficient
frontier is structural and un-buyable (E16).

The last round (E17) sweeps each lever along its design axis rather than testing a single point, and the
finding is geometry over magnitude: how a lever is delivered decides its fate more than how large it is.
Eighteen hypotheses (H126-H143, 12 SUPPORTED, 3 PARTIAL, 3 REFUTED) resolve the delivery axes - universal
beats a means-test cliff, in-kind beats eroding cash, credible permanence beats a policy believed temporary,
national beats a local bonus that only relocates births, and state funding beats an employer mandate that
triggers hiring discrimination against young women. The sharpest mechanism is the outside option as the valve:
rewarding union duration works only as de-risking the stressors that dissolve unions, never as lock-in, because
the credible right to exit is what de-escalates coercion (no-fault divorce cut female suicide up to ~20% and
domestic violence ~30%) - raise the cost of leaving and you remove the incentive it was meant to strengthen. A
quarter of the coupling premium is affordability, so pairing is an economic lever; and the controversial
extremes (a conditioned surrogate-carrier class, a porn ban, an adultery penalty) either sign-flip or drown in
side-cost. The optima are diverse - interior sweet-spots, hard corners and sign-flips coexist - so there is no
lever a designer simply turns to maximum (E17).

A final round (E18) hybridises the proven winners and reaches for creative levers each tied to a named
undercurrent. Twenty hypotheses (H144-H163, 10 SUPPORTED, 8 PARTIAL, 2 REFUTED) show that stacking
*complementary* winners is super-additive - compress the skill premium and make admission un-buyable, de-risk
dissolution and teach the skills and spread them as a peer norm, equalise the second shift across leave and
hours - while stacking two levers on the same channel only saturates, so the design rule is one lever per
channel. The deep undercurrents prove mostly slow, contested, or one-time: the pension-fertility externality is
real (a public pension at 10% of GDP correlates with 0.7-1.6 fewer children) but its corrective has thin causal
support; the biological channel is a hard wall yet a minority driver, and subsidised egg-freezing backfires by
licensing postponement; migration and the grandmother effect are a bridge or an endowment, not a durable lever;
and one-child-policy hysteresis is the sharpest warning that permission is not a lever - lifting the policy left
Chinese fertility falling, because the norms and costs it created outlast it (E18).

## Numbers - parameters and predictions

- **Parameter + calibration table** - `reports/nb7_parameter_table.csv` (recalibrated per-region level,
  drift, innovation scale τ, noise σ, and mutual-information usage); the superseded ELBO run is in
  `reports/nb4_parameter_table.csv`
- **Prediction vs observed (2023) with residuals** - `reports/nb7_predictions.csv`. The Wasserstein
  recalibration collapses the period-TFR residual from the ELBO's +0.18/+0.26 to +0.005/+0.042, and the 2023
  population residual is ≤ 1.6% (USA, Italy, Europe below 0.6%)
- **Crisis costs** - `reports/nb5_crisis_costs.csv` (forgone births / excess deaths per crisis)
- **Forward projections** - `reports/nb6_projection_table.csv` (2100 population, baseline and interventions)

## The story it tells

- **Momentum governs timing and depth** - the answer to the project's central question. Low fertility sets the
  destination; the age pyramid sets when and how steeply a population gets there. It is why the USA and Korea,
  both sub-replacement, are on utterly different trajectories, and why the near-term is unmovable
- **Tempo is not quantum** - a large part of the developed-world "fertility crisis" is postponement, and how
  much of it is recoverable versus permanent is measurable and differs sharply by country
- **Population is point-predictable, period TFR is interval-predictable** - the model earns point confidence
  where age structure dominates and, after the Wasserstein recalibration, states honest intervals where
  behaviour surprises
- **The Seldon manifold survived** - the bistable ridge found in stylized equations landed, uncalibrated, on
  the empirical TFR-1.5 low-fertility trap, and the calibrated model places every region correctly along it

## Honest limitations

- **Period-TFR point forecasts** cannot anticipate regime changes - an intrinsic limit of any period-rate
  forecast; the recalibration removed the in-sample smoothing bias (gap ≈ +0.2 → ≈ +0.02) and made the
  forecast band honest (held-out coverage 100%), so trust the population trajectory and the credible band, not
  a single TFR number
- **Migration assumptions** drive the buffered cases - Germany's +12% to 2100 rests on the elevated
  2019-2023 net migration (the 2022 Ukraine surge inflates the recent mean); the migration *age shape* is a
  canonical Rogers-Castro schedule, not a fitted one
- **National aggregate only** - sub-national divergence (East/West Germany after 1990) is not resolved
- **Behavioural sub-questions unresolved** - the technology-and-formation hypotheses stay on a lagging
  marriage proxy (a measurement gap, not a settled negative); a house-price series was never ingested
- **The USA tempo story is real but partial** - a 25-hypothesis contrarian audit (E13) showed the USA
  tempo-adjusted quantum has itself fallen since 2010, so its shortfall is not purely recoverable
  postponement, and its recent population change was migration-led, not momentum-led; the tempo-recoverability
  claim holds only in part
- **A calibration richer than the data per region** - the audit also flagged that the per-region latent trend
  has more degrees of freedom than data points, so the trustworthy, near-parameter-free evidence is the
  operator fidelity and the held-out backtest, not the in-sample fit
- **Descriptive, not causal** - the model sizes mechanisms and levers; it licenses no claim that a given
  policy achieves a given lever

## Reproducibility

- **Notebooks** - `03-kj-demographic-sota` (age-structured core, E6-E7), `04-kj-demographic-calibration-bayes`
  (tempo-quantum + Bayesian, E8-E9), `05-kj-demographic-crises` (crisis battery, E10),
  `06-kj-demographic-interventions` (forward projections, E11), `07-kj-demographic-recalibration`
  (Wasserstein recalibration closing the prediction gap, E12), `08-kj-demographic-contrarian` (25-hypothesis
  contrarian audit, E13), `09-kj-demographic-reversal` (reversal-intervention catalogue + Seldon manifold /
  drivers / interventions images, E14), `10-kj-demographic-intervention-story` (the coupling keystone +
  literature-grounded intervention strengths on one extensible interface, 50 hypotheses, E15),
  `11-kj-incentives-arms-races-defection` (named-incentive mechanisms with a defection parameter and
  side-effect cost, 25 hypotheses, E16), `12-kj-swept-design-spans` (swept design axes - each hypothesis a
  response curve locating its optimum type; coupling economics, the outside-option valve, policy geometry,
  surrogacy, 18 hypotheses, E17), `13-kj-hybrids-and-undercurrents` (hybrids of the proven winners + creative
  levers each anchored to a named undercurrent - financial/biological/cultural/psychological, 20 hypotheses,
  E18), `14-kj-dynamical-intervention-simulation` (a recalibrated emergent behavioural model - channels = the
  observable parameters C/ρ/P̄/τ/S - coupled to Leslie with dependency feedback, making the model the judge:
  all 88 catalogue interventions integrated four generations and classified by their dynamics, E19); all
  execute end-to-end on the pinned GPU
- **Core module** - `src/sci_demographic_collapse/coremodel.py` (Leslie map, momentum, eigenstructure,
  Rogers-Castro, counterfactual overrides), imported by Notebooks 4-13
- **Data** - `data/raw/unwpp/` (UN WPP 2024, CC BY 3.0 IGO) plus the World Bank / Eurostat / OWID behavioural
  panel; provenance in `data/raw/README.md`, `data/raw/unwpp/README.md`, and the per-source manifests
- **Figures** - forty-four executed figures in `reports/figures/` (including the recalibration loss
  landscape, gap closure, tournament, coverage, crisis-fidelity, contrarian-scorecard, the Seldon-manifold /
  drivers / interventions panels, the E15 intervention-story set: margin decomposition, strength × margin
  map, keystone levers, the wider-menu verdict grid, the coupling-in-depth grid, the deeper-drivers grid, the
  coupled-system interaction panel, the contraception spectrum, and the reversal verdict; and the E16
  defection set: the arms-race defusal panel, the wealth-compression stack, the Western natural experiments,
  the defection screen, the side-effect frontier, and the manifold bundle crossing; and the E17 swept-span
  set: coupling economics, duration-and-fidelity, policy geometry, surrogacy, the optimum-type taxonomy, and
  the robust-vs-fragile bundle; and the E18 hybrids-and-undercurrents set: the hybrid blends, the
  financial/biological/cultural undercurrent panels, and the channel taxonomy); tables in `reports/*.csv`
