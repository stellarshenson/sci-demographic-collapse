# Demographic Collapse - Calibration & Event Stress-Test Experiments

**Canonical Experiments Document**

Experiments log for calibrating the nine-state demographic-collapse model (from Notebook 1, stylized) to real data for the USA (primary), EU, South Korea, and China (conditional), and stress-testing it against known past and current events. Batches E1-E5 pre-register 20 hypotheses; execution vehicle is `notebooks/02-kj-demographic-calibration.ipynb` (to be built once data is ingested). All hypotheses are observational (calibration + stress-test) - interventions are parked, not tested.

- **Branch / artefacts** - Notebook 1 (structural, uncalibrated) `notebooks/01-kj-demographic-collapse.ipynb`; E1-E5 execution `notebooks/02-kj-demographic-calibration.ipynb`; design (on convergence) `docs/demographic-collapse-sota.md`
- **Data** - `data/raw/` open-source ingests + `data/raw/PROVENANCE.md` manifest (source, URL, retrieval date, license)
- **Status** - PRE-REGISTRATION; all Results / Verdicts below are `pending` until the notebook runs

## Problem overview

Fit a coupled nine-state ODE model of population dynamics to observed national demographic series and test whether it reproduces history and reacts correctly to known events.

- **Regions** - USA (richest open data, all event tests), EU (Eurostat aggregate + representative members), South Korea (ultra-low-fertility reference, TFR ≈ 0.72), China (UN WPP / NBS, excluded if not reliably obtainable)
- **Panel (per region)** - total fertility rate (TFR), mean age at first birth, crude marriage rate, total population; the four series a hypothesis must reproduce
- **Horizon** - 1960 → present where data allows; event windows sized to each shock
- **States (model)** - n, μ_b, σ²_b, ρ, C, τ, E, Ψ, D (population fraction, fertility-trait mean/variance, childlessness, coupling, onset age, economy, cultural pressure, union duration)
- **Core difficulty** - separating overlapping drivers (recession vs education vs technology) acting on the same series; the model-comparison test (E4-H17) is the honest route
- **Known omission** - the model has no migration term; USA/EU totals are migration-driven, so population-series residuals are expected until migration is added (E5-H20)
- **Not tested** - causal identification of any single intervention; even calibrated, the log is descriptive - interventions stay parked

## Executive summary

Pre-registration only - no results yet. Twenty hypotheses across five batches: baseline calibration fidelity (E1), separatrix placement (E2), economic/policy-era stress tests (E3), technology-adoption stress tests (E4, the core interest), and falsification / generalization / missing-parameter discovery (E5). Every calibrated hypothesis must beat the naive baseline on the four-series panel.

### Research at a glance (verdicts pending)

| id | claim (what is under test) | lever | predicted | verdict |
|---|---|---|---|---|
| E1-H1 | Gompertz-Makeham reproduces USA life-expectancy path | mortality fit | e0 MAPE ≤ 3%, COVID dip caught | pending |
| E1-H2 | skew-normal ASFR reproduces first-birth-age rise | fertility-timing fit | age MAE ≤ 1.0 yr | pending |
| E1-H3 | endogenous momentum alone reproduces the baby bust | run forward, no shocks | TFR to ~1.8 by mid-70s | pending |
| E1-H4 | couple-gate reproduces marriage-rate & marital-fertility shift | coupling+duration fit | marriage-rate MAPE ≤ 12% | pending |
| E2-H5 | USA (2020) sits in the recovery basin | classify calibrated state | recovery side, not collapsed | pending |
| E2-H6 | EU sits closer to the ridge than USA | classify EU vs USA | EU nearer separatrix | pending |
| E2-H7 | KR/China ultra-low sit at/past the ridge | classify KR/China | at or past separatrix | pending |
| E2-H8 | calibrated separatrix ≈ low-fertility-trap TFR 1.5 | read ridge TFR | ridge TFR 1.5 ± 0.2 | pending |
| E3-H9 | 2008 recession reproduces the USA TFR drop | scarcity forcing 2008 | TFR 2.12→1.93 ± 0.1 | pending |
| E3-H10 | COVID-19 reproduces 2020 dip + 2021 rebound | mortality+scarcity 2020 | dip then partial rebound | pending |
| E3-H11 | contraceptive diffusion reproduces 1960s decline | birth-gate 1960s | decline timing matched | pending |
| E3-H12 | education/LFP reproduces onset-age rise | τ forcing | age rise sign+slope | pending |
| E3-H13 | housing cost reproduces negative housing↔fertility | scarcity cross-section | negative slope, p<0.05 | pending |
| E4-H14 | social-media adoption reproduces post-2007 coupling decline | Ψ/C_expect forcing | acceleration matched | pending |
| E4-H15 | smartphone saturation reproduces dating/socializing drop | coupling suppression | drop sign+magnitude | pending |
| E4-H16 | dating apps reproduce meet-online shift + <30 decline | optionality + D forcing | HCMST curve matched | pending |
| E4-H17 | tech forcing beats economics-only on post-2007 fit | add tech term | ≥25% RMSE reduction | pending |
| E5-H18 | CSD early-warning present before inflections | variance/AR1 test | Kendall tau>0 pre-crash | pending |
| E5-H19 | USA-fit params predict EU out-of-sample | transfer + EU events | EU TFR ± 0.2 | pending |
| E5-H20 | residuals identify migration as missing parameter | residual analysis | migration cuts pop residual ≥30% | pending |

## Methodology and metrics

Each hypothesis fits or forces the calibrated model, then compares its four-series panel against the observed series and against the naive baseline.

- **Panel metrics** - TFR MAPE, mean-age-at-first-birth MAE (years), marriage-rate MAPE, population MAPE; each series carries the naive baseline reading beside it
- **Event-response metric** - for a shock test, the reproduced dip/drop magnitude and timing vs observed, within a pre-registered tolerance
- **Model comparison (E4-H17)** - out-of-sample RMSE reduction from adding the tech forcing, plus an information-criterion check (AIC/BIC) so the extra term must earn its degrees of freedom
- **Verdict labels** - Ships / Kept / Promoted / Dropped / Refuted / Refuted (null) / Killed-at-gate, each with the number that justifies it

### Naive baseline (mandatory)

- **Definition** - frozen-rate cohort-component projection: hold the region's start-year age-specific fertility and mortality constant, no events, no behavioural dynamics; project the panel forward
- **Role** - the floor every hypothesis must beat; a calibrated model that does not lower panel error vs this frozen-rate projection has earned nothing
- **Readout** - each result reported as a delta (e.g. `TFR MAPE 6% vs baseline 22%`)

## Setup

- **Data** - `data/raw/` (immutable) + `data/raw/PROVENANCE.md`; sources per hypothesis in the Experiment `source:` lines
- **Pipeline** - ingest → fit distribution families (Gompertz-Makeham mortality, skew-normal ASFR, Gamma/skew-normal onset, logit-normal fractions) → calibrate coupled-ODE parameters to the panel (least-squares / Bayesian) → encode event forcings as time-varying exogenous inputs → score vs baseline
- **Compute** - torch on GPU (RTX PRO 4000 Blackwell, UUID-pinned) for batched integration and parameter sweeps; scipy/sklearn for fits; polars for the panels
- **Execution vehicle** - `notebooks/02-kj-demographic-calibration.ipynb` (to be built)
- **Reproducibility** - fixed seed; provenance manifest records every source, URL, retrieval date, license
- **Source papers** - digests to be written into `docs/references/<slug>.md` on ingestion (Lutz-Skirbekk-Testa low-fertility trap; Comolli recession-fertility; Rosenfeld HCMST; Twenge iGen; Dettling-Kearney housing-fertility) and linked from each Experiment `source:`

## E1 - Baseline calibration & fidelity (USA)

Four fits establishing the calibrated model reproduces known USA history before any event is injected.

### E1-H1 Mortality calibration
- **Hypothesis** - because the Gompertz-Makeham law fits adult human mortality, fitting it to USA period life tables will reproduce e0 1960→2019 within MAPE ≤ 3% and catch the 2020-21 COVID dip
- **Lever** - mortality hazard m(age), fit to USA period life tables
- **Mechanism** - fit Makeham background + Gompertz exponential to age-specific death rates per decade; drive the model mortality from the fitted schedule
- **Prediction** - e0 MAPE ≤ 3%; the fitted schedule places e0 ≈ 70 (1960) → ≈ 78-79 (2019) with a 2020-21 dip
- **Acceptance bar** - e0 MAPE ≤ 3% and beats the frozen-rate baseline
- **Experiment** - source: CDC/NCHS period life tables, Human Mortality Database (HMD), SSA<br>data: `data/raw/usa/life-tables`<br>method: Gompertz-Makeham least-squares per decade
- **Result** - pending
- **Verdict** - pending

### E1-H2 Fertility-timing calibration
- **Hypothesis** - because developed-country ASFR is right-skewed, a skew-normal fit will reproduce the USA mean-age-at-first-birth rise with MAE ≤ 1.0 yr
- **Lever** - age-specific fertility curve shape (skew-normal), fit to NCHS natality
- **Mechanism** - fit skew-normal ASFR per year; map its shift to the model onset τ and window W(τ)
- **Prediction** - mean age at first birth ≈ 21.4 (1970) → ≈ 27.3 (2021), MAE ≤ 1.0 yr (targets to confirm against ingested NCHS)
- **Acceptance bar** - first-birth-age MAE ≤ 1.0 yr and beats baseline
- **Experiment** - source: NCHS natality (final natality files)<br>data: `data/raw/usa/natality`<br>method: skew-normal MLE per year
- **Result** - pending
- **Verdict** - pending

### E1-H3 Endogenous momentum
- **Hypothesis** - because age structure carries built-in momentum, the model seeded at the USA 1960 baby-boom state and run forward with NO shocks will reproduce the baby-bust TFR fall to ~1.7-1.8 by the mid-1970s
- **Lever** - initial condition (1960 USA age structure), events off
- **Mechanism** - seed the calibrated model at the 1960 state, integrate with constant behavioural parameters; observe whether momentum alone bends TFR down
- **Prediction** - TFR falls from ~3.6 (1960) toward ~1.8 by ~1976 from momentum + endogenous coupling dynamics, without external forcing
- **Acceptance bar** - reproduces the direction and reaches TFR ≤ 2.1 within ±3 yr of the observed crossing; quantify the momentum-vs-events share
- **Experiment** - source: World Bank / NCHS TFR series<br>data: `data/raw/usa/tfr`<br>method: forward integration from the 1960 seed
- **Result** - pending
- **Verdict** - pending

### E1-H4 Couple gate
- **Hypothesis** - because births flow from unions in the model, fitting coupling C and duration D to USA marriage data will reproduce the marriage-rate decline and the marital→nonmarital fertility shift 1970-2020 within marriage-rate MAPE ≤ 12%
- **Lever** - coupling formation/dissolution and duration parameters, fit to marriage/union series
- **Mechanism** - calibrate α, δ_C, δ_div, D₀ to observed marriage rate and mean union duration; check the induced marital-fertility split
- **Prediction** - marriage rate falls ~10.6→~6 per 1000 (1970-2020); nonmarital share rises to ~40%
- **Acceptance bar** - marriage-rate MAPE ≤ 12% and the nonmarital-share direction matched, beating baseline
- **Experiment** - source: US Census / ACS marriage & household, NCHS nonmarital natality<br>data: `data/raw/usa/marriage`<br>method: least-squares on C, D dynamics
- **Result** - pending
- **Verdict** - pending

## E2 - Separatrix placement (USA, EU, KR, China?)

Where each calibrated region sits relative to the recovery/collapse divide.

### E2-H5 USA on the recovery side
- **Hypothesis** - because the USA is below replacement but not collapsing, the calibrated USA (2020) state must fall on the recovery side of the separatrix; the model is falsified if it places the USA in the collapse basin
- **Lever** - region calibration (USA 2020), basin classification
- **Mechanism** - integrate the calibrated USA state to the attractor, classify recovery vs extinction
- **Prediction** - USA lands in the recovery basin
- **Acceptance bar** - Refuted if the calibrated USA state flows to extinction
- **Experiment** - source: calibrated USA panel (E1)<br>method: basin classification of the calibrated state
- **Result** - pending
- **Verdict** - pending

### E2-H6 EU nearer the ridge
- **Hypothesis** - because EU TFR (~1.5) is below the USA, the calibrated EU state sits closer to the separatrix than the USA
- **Lever** - region calibration (EU)
- **Mechanism** - calibrate EU panel, measure distance-to-separatrix vs USA
- **Prediction** - EU distance-to-ridge < USA distance-to-ridge
- **Acceptance bar** - EU strictly nearer the ridge than USA
- **Experiment** - source: Eurostat fertility, marriage, population<br>data: `data/raw/eu`<br>method: calibrate + measure basin distance
- **Result** - pending
- **Verdict** - pending

### E2-H7 Ultra-low at/past the ridge
- **Hypothesis** - because South Korea (TFR ~0.72) and China (~1.0-1.2) are ultra-low, their calibrated states sit at or past the separatrix
- **Lever** - region calibration (KR; China if data)
- **Mechanism** - calibrate KR/China panels, classify basin
- **Prediction** - KR at or past the ridge; China at or near it (if data reliable)
- **Acceptance bar** - KR at/past the ridge; China reported only if UN WPP data is defensible, else excluded
- **Experiment** - source: Statistics Korea, UN World Population Prospects, NBS (conditional)<br>data: `data/raw/kr`, `data/raw/china`<br>method: calibrate + classify
- **Result** - pending
- **Verdict** - pending

### E2-H8 Separatrix ≈ low-fertility trap
- **Hypothesis** - because the demographic literature identifies a low-fertility trap near TFR 1.5, the calibrated model's separatrix should sit at ridge-TFR 1.5 ± 0.2
- **Lever** - read the separatrix TFR on the calibrated system
- **Mechanism** - locate the calibrated separatrix, read the TFR along it, compare to the Lutz-Skirbekk-Testa threshold
- **Prediction** - ridge TFR ≈ 1.5
- **Acceptance bar** - ridge TFR within 1.5 ± 0.2
- **Experiment** - source: Lutz, Skirbekk & Testa (2006) low-fertility trap - digest `docs/references/low-fertility-trap.md`<br>method: calibrated separatrix TFR readout
- **Result** - pending
- **Verdict** - pending

## E3 - Economic & policy-era stress tests (USA, EU)

Inject known events at their known dates and check the reproduced response.

### E3-H9 Great Recession 2008
- **Hypothesis** - because economic scarcity suppresses coupling and raises onset, injecting the 2008 recession as a scarcity shock reproduces the USA TFR fall 2.12 (2007) → 1.93 (2013) with no rebound, within ±0.1 TFR
- **Lever** - economy/scarcity forcing at 2008 (E drop)
- **Mechanism** - drive E down on the observed 2008-2013 GDP/unemployment path; read TFR response
- **Prediction** - TFR 2.12→~1.93, no recovery through 2019
- **Acceptance bar** - reproduces the drop within ±0.1 TFR and the no-rebound shape, beating baseline
- **Experiment** - source: NCHS TFR, BEA/BLS GDP+unemployment; Comolli (2017) digest `docs/references/comolli-recession-fertility.md`<br>data: `data/raw/usa/tfr`, `data/raw/usa/macro`<br>method: exogenous E forcing
- **Result** - pending
- **Verdict** - pending

### E3-H10 COVID-19 2020
- **Hypothesis** - because COVID hit both mortality and short-run fertility, injecting it at 2020 reproduces the 2020 birth dip and the 2021 partial rebound
- **Lever** - mortality spike + transient scarcity at 2020
- **Mechanism** - apply the observed 2020-21 excess mortality and a short scarcity pulse; read births
- **Prediction** - a 2020 dip then a 2021 partial rebound in births
- **Acceptance bar** - reproduces dip-then-rebound sign and approximate magnitude
- **Experiment** - source: NCHS provisional natality + mortality 2020-2022<br>data: `data/raw/usa/covid`<br>method: dated mortality + scarcity pulse
- **Result** - pending
- **Verdict** - pending

### E3-H11 Contraceptive diffusion 1960s
- **Hypothesis** - because the Pill decoupled coupling from birth, its 1960s diffusion reproduces the timing/steepness of the initial fertility decline
- **Lever** - birth-gate control (Pill diffusion curve) in the 1960s
- **Mechanism** - modulate the coupling→birth gate on the Pill adoption curve; read TFR onset of decline
- **Prediction** - decline onset ~1961-1965 matching the adoption curve
- **Acceptance bar** - decline timing within ±3 yr of observed, beating baseline
- **Experiment** - source: historical Pill-adoption series, NCHS TFR<br>data: `data/raw/usa/contraception`<br>method: gate modulation on adoption curve
- **Result** - pending
- **Verdict** - pending

### E3-H12 Education / labor-force onset delay
- **Hypothesis** - because schooling and work postpone parenthood, rising female tertiary education and LFP as an onset driver reproduce the first-birth-age rise
- **Lever** - onset τ forcing from education/LFP series
- **Mechanism** - drive τ on the female-education/LFP path; read mean age at first birth
- **Prediction** - first-birth age rises with education/LFP, sign and slope matched
- **Acceptance bar** - reproduces the rise sign and slope within tolerance, beating baseline
- **Experiment** - source: BLS LFP, NCES tertiary attainment, Census<br>data: `data/raw/usa/education-lfp`<br>method: τ forcing
- **Result** - pending
- **Verdict** - pending

### E3-H13 Housing cost / precarity
- **Hypothesis** - because scarcity delays childbearing, rising housing cost reproduces a negative housing↔fertility relationship in the cross-section
- **Lever** - scarcity from housing-cost series
- **Mechanism** - map housing cost to the scarcity term; test the induced housing↔fertility slope
- **Prediction** - negative slope, significant
- **Acceptance bar** - negative slope, p < 0.05, consistent with Dettling-Kearney
- **Experiment** - source: FHFA/Zillow house prices, county fertility; Dettling & Kearney (2014) digest `docs/references/dettling-kearney-housing.md`<br>data: `data/raw/usa/housing`<br>method: scarcity mapping + regression
- **Result** - pending
- **Verdict** - pending

## E4 - Technology-adoption stress tests (USA)

The core interest - does the technology stack, entered as optionality/coupling pressure, reproduce the post-2007 coupling decline?

### E4-H14 Social-media adoption
- **Hypothesis** - because social media inflates expectations and attention competition, Facebook onset (2004) plus the social-media adoption curve entered as rising cultural pressure Ψ / expectation C_expect reproduces the post-2007 acceleration of coupling decline and marriage-age rise
- **Lever** - Ψ / C_expect forcing on the social-media adoption curve
- **Mechanism** - drive Ψ and C_expect up on Pew adoption % / Facebook MAU; read coupling and marriage-age response post-2007
- **Prediction** - a post-2007 acceleration in coupling decline and marriage-age rise tracking adoption
- **Acceptance bar** - reproduces the post-2007 acceleration, improving fit vs the no-tech baseline
- **Experiment** - source: Pew social-media fact sheet, Facebook 10-K MAU, ACS marriage<br>data: `data/raw/usa/tech/social-media`<br>method: Ψ/C_expect forcing on adoption curve
- **Result** - pending
- **Verdict** - pending

### E4-H15 Smartphone saturation
- **Hypothesis** - because always-on devices displaced in-person socializing, smartphone saturation (iPhone 2007 → >80% ~2018) entered as coupling suppression reproduces the documented drop in adolescent/young-adult dating and in-person socializing
- **Lever** - coupling-formation suppression on the smartphone-penetration curve
- **Mechanism** - suppress coupling formation α on the penetration curve; read youth dating/socializing proxies
- **Prediction** - a drop in young-adult dating/socializing tracking penetration
- **Acceptance bar** - reproduces the drop sign and approximate magnitude
- **Experiment** - source: Pew mobile, Monitoring the Future, YRBS; Twenge iGen digest `docs/references/twenge-igen.md`<br>data: `data/raw/usa/tech/smartphone`<br>method: α suppression on penetration
- **Result** - pending
- **Verdict** - pending

### E4-H16 Dating-app diffusion
- **Hypothesis** - because dating apps manufacture an infinite-options frame, their diffusion (Tinder 2012, Bumble 2014) entered as optionality pressure (raising the expectation gap, shortening union duration D) reproduces the "online is the #1 way couples meet" shift and the decline in <30 relationship formation
- **Lever** - optionality pressure (C_expect up, D down) on the dating-app adoption curve
- **Mechanism** - raise C_expect and shorten D on the adoption curve; read how-couples-meet and <30 partnering
- **Prediction** - online-meeting share rises to #1 by ~2013-2017; <30 partnering declines
- **Acceptance bar** - reproduces the HCMST meet-online curve and the <30 decline direction
- **Experiment** - source: Rosenfeld HCMST digest `docs/references/rosenfeld-hcmst.md`, Pew online dating 2013/2019/2023<br>data: `data/raw/usa/tech/dating-apps`<br>method: C_expect + D forcing
- **Result** - pending
- **Verdict** - pending

### E4-H17 Tech forcing earns its place
- **Hypothesis** - because economics alone underexplains the post-2007 coupling decline, adding the combined tech forcing (social + smartphone + apps) reduces post-2007 out-of-sample RMSE by ≥25% vs an economics-only model while surviving an information-criterion penalty
- **Lever** - add the tech forcing term to the economics-only calibrated model
- **Mechanism** - fit economics-only, then economics+tech; compare out-of-sample RMSE and AIC/BIC
- **Prediction** - tech term reduces post-2007 RMSE ≥ 25% and lowers AIC/BIC
- **Acceptance bar** - ≥ 25% out-of-sample RMSE reduction AND improved information criterion; Refuted if the term does not earn its degrees of freedom
- **Experiment** - source: the calibrated baseline (E3) + tech series (E4-H14/15/16)<br>method: nested model comparison, out-of-sample split
- **Result** - pending
- **Verdict** - pending

## E5 - Falsification, generalization, missing parameters

### E5-H18 Critical-slowing-down early warning
- **Hypothesis** - because a system nearing a fold recovers ever more slowly, rising variance and lag-1 autocorrelation should precede known USA fertility/marriage inflection points - or be absent (a clean falsification)
- **Lever** - CSD statistics on the observed series (measurement only)
- **Mechanism** - rolling variance and lag-1 autocorrelation on detrended fertility/marriage series before inflections; Kendall tau on the trend
- **Prediction** - Kendall tau > 0 (rising) in the pre-inflection window
- **Acceptance bar** - tau > 0 with significance in ≥ 1 pre-inflection window, else reported as absent (falsified)
- **Experiment** - source: NCHS fertility/marriage time series<br>data: `data/raw/usa`<br>method: rolling variance + AR1 + Kendall tau (measurement only, no fit)
- **Result** - pending
- **Verdict** - pending

### E5-H19 Out-of-sample transfer
- **Hypothesis** - because the mechanisms are meant to be general, parameters fit to the USA applied to the EU with EU event timings predict EU TFR within ±0.2; failures flag region-specific parameters
- **Lever** - transfer USA parameters to EU, swap event timings
- **Mechanism** - hold USA behavioural parameters, apply EU events/economics, predict EU TFR
- **Prediction** - EU TFR predicted within ±0.2 where mechanisms generalize
- **Acceptance bar** - EU TFR within ±0.2, or the deviations localize to named region-specific parameters
- **Experiment** - source: Eurostat, EU event chronology<br>data: `data/raw/eu`<br>method: parameter transfer + EU forcing
- **Result** - pending
- **Verdict** - pending

### E5-H20 Missing-parameter discovery (migration)
- **Hypothesis** - because the model has no migration term, calibrated population residuals will be systematic (sign-consistent, autocorrelated) and adding a migration inflow will cut the population-series residual by ≥ 30%
- **Lever** - residual analysis, then add a migration term
- **Mechanism** - fit without migration, inspect population residual structure; add net migration from data; re-fit
- **Prediction** - structured residual pre-migration; ≥ 30% residual reduction post-migration
- **Acceptance bar** - migration cuts population-series residual ≥ 30% and whitens its autocorrelation
- **Experiment** - source: Census net migration, Eurostat migration, UN WPP<br>data: `data/raw/usa/migration`, `data/raw/eu/migration`<br>method: residual analysis + migration term addition
- **Result** - pending
- **Verdict** - pending

## Interventions parking lot (recorded, NOT planned)

Candidate interventions for a later, separate round - **no hypotheses planned until the model is calibrated** (an uncalibrated model cannot size an intervention). Recorded here so the ideas are not lost.

- **INT-1 Dating-app / attention-economy regulation** - mechanism: dating apps use variable-ratio (slot-machine) reinforcement, engineered for time-on-app → inflates optionality/expectation pressure (Ψ, C_expect) and shortens union duration D, attacking the coupling keystone; precedent: states regulate the addictive mechanism, not the category (gambling licensing / age-gating / safeguards; loot-box bans in Belgium & the Netherlands target the mechanic, not the game); candidate lever: reduce Ψ / C_expect, lengthen D; status PARKED
- **INT-2 Adolescent relationship-skills training** - mechanism: communication and conflict-resolution skills taught in early adolescence → more durable unions (raises D, lowers δ_div) and plausibly better formation, strengthening the keystone via stability; precedent: school-based social-emotional-learning and relationship-education programs (PREP; "Love Notes" / "Relationship Smarts"); candidate lever: lengthen D, reduce δ_div; status PARKED

## Lessons learned

- pending (populated after E1-E5 run)

## Conclusions

- pending

## Next steps

- Ingest `data/raw/` from the approved open sources + write `PROVENANCE.md` and the paper digests
- Build and execute `notebooks/02-kj-demographic-calibration.ipynb` batch by batch, recording verdicts here
- On convergence, distil the calibrated design into `docs/demographic-collapse-sota.md`
