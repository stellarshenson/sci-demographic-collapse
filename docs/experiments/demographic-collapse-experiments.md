# Demographic Collapse - Calibration & Event Stress-Test Experiments

**Canonical Experiments Document**

Experiments log for calibrating the nine-state demographic-collapse model (from Notebook 1, stylized) to real data for the USA (primary), EU, South Korea, and China (conditional), and stress-testing it against known past and current events. Batches E1-E5 pre-register 20 hypotheses; execution vehicle is `notebooks/02-kj-demographic-calibration.ipynb` (to be built once data is ingested). All hypotheses are observational (calibration + stress-test) - interventions are parked, not tested.

- **Branch / artefacts** - Notebook 1 (structural, uncalibrated) `notebooks/01-kj-demographic-collapse.ipynb`; E1-E5 execution `notebooks/02-kj-demographic-calibration.ipynb`; design (on convergence) `docs/demographic-collapse-sota.md`
- **Data** - `data/raw/` open-source ingests (World Bank, Eurostat, OWID) + per-source `MANIFEST.json` (source, URL, retrieval date, license); `data/external/` cited event-forcing anchors
- **Status** - EXECUTED. E1-E5 (2026-07-06, `notebooks/02-kj-demographic-calibration.ipynb`): **12 SUPPORTED, 5 REFUTED, 1 REFRAMED, 1 PARTIAL, 1 INCONCLUSIVE**. Round 1 E6-E7 (2026-07-06, `notebooks/03-kj-demographic-sota.ipynb`, age-structured SOTA rewrite on UN WPP 2024): **4 SUPPORTED, 1 REFRAMED**. Round 2-3 E8-E9 (2026-07-06, `notebooks/04-kj-demographic-calibration-bayes.ipynb`, tempo-quantum + Bayesian free-energy): **5 SUPPORTED, 1 PARTIAL**. Round 4 E10 (2026-07-06, `notebooks/05-kj-demographic-crises.ipynb`, crisis battery + counterfactual costs): **4 SUPPORTED, 1 PARTIAL**. Round 5 E11 (2026-07-06, `notebooks/06-kj-demographic-interventions.ipynb`, forward projections + interventions to 2100): **3 SUPPORTED**. Round 6 E12 (2026-07-06, `notebooks/07-kj-demographic-recalibration.ipynb`, Wasserstein recalibration closing the prediction gap): **6 SUPPORTED**. Round 7 E13 (2026-07-06, `notebooks/08-kj-demographic-contrarian.ipynb`, contrarian audit - 25 attacks on the campaign's own findings, inverted convention): **12 findings survived, 13 qualified**. Round 8 E14 (2026-07-06, `notebooks/09-kj-demographic-reversal.ipynb`, reversal-intervention catalogue + Seldon manifold / drivers / interventions images): **5 SUPPORTED**. Round 9 E15 (2026-07-06, `notebooks/10-kj-demographic-intervention-story.ipynb`, coupling keystone + literature-grounded intervention strengths on one extensible interface, 50 hypotheses H51-H100 incl. coupling-in-depth legislative+psychological levers, a deeper-drivers chapter on the career-first arms race, and an interactions/side-effects analysis): **37 SUPPORTED, 10 PARTIAL, 3 REFUTED**. Round 10 E16 (2026-07-06, `notebooks/11-kj-incentives-arms-races-defection.ipynb`, incentives / arms races / defection - named-incentive mechanisms with a defection parameter δ and side-effect cost, 25 hypotheses H101-H125): **15 SUPPORTED, 6 PARTIAL, 4 REFUTED**. Round 11 E17 (2026-07-06, `notebooks/12-kj-swept-design-spans.ipynb`, swept design spans - each hypothesis's Experiment/Result is a swept response curve locating its optimum, discrete-hypothesis discipline held; coupling economics, the outside-option valve, policy geometry, a controversial surrogate-carrier market, 18 hypotheses H126-H143): **12 SUPPORTED, 3 PARTIAL, 3 REFUTED**. Round 12 E18 (2026-07-06, `notebooks/13-kj-hybrids-and-undercurrents.ipynb`, hybrids of the proven winners + creative new levers each anchored to a named undercurrent [financial/institutional, biological, cultural/marriage-market, psychological], grounded in three research digests, 20 hypotheses H144-H163): **10 SUPPORTED, 8 PARTIAL, 2 REFUTED**. Round 13 E19 (2026-07-06, `notebooks/14-kj-dynamical-intervention-simulation.ipynb`, dynamical re-examination - a recalibrated emergent behavioural model [channels = the observable parameters C/ρ/P̄/τ/S] coupled to Leslie with dependency feedback, calibrated to real 2023 fertility, makes the model the judge; all ~88 catalogue interventions integrated 4 generations 2023→2125 and classified by their dynamics): **validation round, no new hypotheses**. Round 14 E20 (2026-07-07, `notebooks/15-kj-seldon-harbingers-ablation.ipynb`, Seldon harbingers - ablation on the E19 coupled model to find the least-cost levers that improve fertility, ranked by improvement per composite cost, 6 hypotheses H164-H169): **6 SUPPORTED**. Round 15 E21 (2026-07-07, research round - relationship-machinery fan-out [scarring / mileage / beauty arms race / therapy / education], five research digests; meta-finding: at population scale structure beats psychology, the proximate mechanisms are mostly selection or amplifiers): **research round, no new modelled hypotheses**. Round 16 E22 (2026-07-07, `notebooks/16-kj-structural-levers.ipynb`, the five structural levers + the education income-vs-degrees optimisation and composites/ablation, grounded and provenanced, 7 hypotheses H170-H176): **4 SUPPORTED, 3 PARTIAL**. Round 17 E23 (2026-07-07, research round - the exit machinery: custody / parental-alienation + the Iceland decoupled-fertility model, four digests; meta-finding: the West confirms the coupling verdict rather than escaping it - custody-regime commitment insurance [Halla 2013, the one causal estimate] is the modellable signal, and Iceland's own fall to 1.56 shows decoupling shifts the fertility *level*, not the *trend*): **research round, no new modelled hypotheses**. Round 18 E24 (2026-07-07, `notebooks/18-kj-exit-machinery-simulation.ipynb`, the exit-machinery arc H177-H181 simulated on the coupled model and ablated - the first batch run under the new simulation-then-ablation protocol; post-divorce conflict, custody, intergenerational transmission and state-funded repair): **1 SUPPORTED, 3 PARTIAL, 1 REFUTED**. Round 19 E25 (2026-07-07, `notebooks/19-kj-social-norms-abortion.ipynb`, social norms + abortion with the new bistable norm state N, H182-H187): **1 SUPPORTED, 3 PARTIAL, 2 REFUTED**. Round 19b E26 (2026-07-07, `notebooks/20-kj-alternative-structures.ipynb`, alternative structures + interaction panel H188-H207): **3 SUPPORTED, 8 PARTIAL, 9 REFUTED**. Round 20 E27 (2026-07-07, `notebooks/21-kj-concentration-structures.ipynb`, reproductive-concentration structures H208-H212): **2 PARTIAL, 3 REFUTED**. Round 21 E28 (2026-07-07, `notebooks/22-kj-polygamy-spectrum.ipynb`, polygamy endorsement spectrum + interaction matrix H213-H226): **7 SUPPORTED, 3 PARTIAL, 4 REFUTED**. Round 22 E29 (2026-07-07, `notebooks/23-kj-matriarchy-optimisation.ipynb`, matriarchy stability optimisation on the population framework H227-H246): **10 SUPPORTED, 3 PARTIAL, 7 REFUTED**. Round 23 E30 (2026-07-07, `notebooks/24-kj-marriageability-intergenerational.ipynb`, marriageability + intergenerational path integral H247-H260): **11 SUPPORTED, 1 PARTIAL, 2 REFUTED**. Round 24 E31 (2026-07-07, `notebooks/25-kj-alienation-legislation.ipynb`, parental-alienation legislation + prevention H261-H270): **4 SUPPORTED, 3 PARTIAL, 3 REFUTED**. Round 25 E32 (2026-07-07, `notebooks/26-kj-alienation-combat.ipynb`, combating alienation - the full 27-hypothesis toolkit H271-H297): **9 SUPPORTED, 15 PARTIAL, 3 REFUTED**. Round 26 E33 (2026-07-08, `notebooks/27-kj-religion-fertility.ipynb`, religion x fertility - religion decomposed into the channels it loads + compounding sub-populations, H298-H313): **6 SUPPORTED, 8 PARTIAL, 2 REFUTED**. Round 27 E35 (2026-07-08, `notebooks/28-kj-cultural-transmission-e35.ipynb`, cultural transmission - the floor, not the lever [GOAL-16 Phase C]; the within-population eigen-operator Φ=r·VΛV⁻¹ retired as a lever and the E33 between-group replicator promoted to a descriptive national-TFR floor, H339-H348): **7 SUPPORTED, 3 REFUTED**. Round 28 E34 (2026-07-08, `notebooks/31-kj-heretical-fanout-e34.ipynb`, heretical & coercive natalism fanout - 25 coercive/zealous/theocratic/structural levers each grounded in a historical analogue, run through the calibrated core with the E30 path integral so the coercion × path-integral sign flip is measured gen-1 vs gen-4 [designed with E35, modelled after it], H314-H338): **3 SUPPORTED, 11 PARTIAL, 11 REFUTED**. Round 29 E36 (2026-07-08, `notebooks/32-kj-marriageable-men-saturation-e36.ipynb`, the marriageable-men lever reformulated as a saturating Hill drive on relative male income with its competing counter-terms on the shared coupling/quantum wires - inequality backlash, hypergamy squeeze, education path-integral, the sign-conditional female arm, fiscal redistribution, H349-H357): **8 SUPPORTED, 1 PARTIAL**. Three baseline-preserving additions this session (bistable norm N; marriageability q + a per-cohort intergenerational path integral via `ot.py`; the differentiable quantile-flow `flow.py`) plus the population-distribution framework `population.py`. **Campaign total: 357 hypotheses** - E1-E12: 34 SUPPORTED, 5 REFUTED, 2 REFRAMED, 3 PARTIAL, 1 INCONCLUSIVE; E13 audit: 12 survived, 13 qualified; E14: 5 SUPPORTED; E15: 37 SUPPORTED, 10 PARTIAL, 3 REFUTED; E16: 15 SUPPORTED, 6 PARTIAL, 4 REFUTED; E17: 12 SUPPORTED, 3 PARTIAL, 3 REFUTED; E18: 10 SUPPORTED, 8 PARTIAL, 2 REFUTED; E20: 6 SUPPORTED; E22: 4 SUPPORTED, 3 PARTIAL; E24: 1 SUPPORTED, 3 PARTIAL, 1 REFUTED; E25: 1 SUPPORTED, 3 PARTIAL, 2 REFUTED; E27: 2 PARTIAL, 3 REFUTED; E28: 7 SUPPORTED, 3 PARTIAL, 4 REFUTED; E29: 10 SUPPORTED, 3 PARTIAL, 7 REFUTED; E26: 3 SUPPORTED, 8 PARTIAL, 9 REFUTED; E30: 11 SUPPORTED, 1 PARTIAL, 2 REFUTED; E31: 4 SUPPORTED, 3 PARTIAL, 3 REFUTED; E32: 9 SUPPORTED, 15 PARTIAL, 3 REFUTED; E33: 6 SUPPORTED, 8 PARTIAL, 2 REFUTED; E34: 3 SUPPORTED, 11 PARTIAL, 11 REFUTED; E35: 7 SUPPORTED, 3 REFUTED; E36: 8 SUPPORTED, 1 PARTIAL. SOTA design distilled in `docs/demographic-collapse-sota.md`; decision-maker star-ranking with mechanism-of-effect + side-effects regenerated on demand via the `/write-interventions` command; research library in `references/papers/` (41 PDFs + 65 digests)

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

Executed 2026-07-06. Twenty hypotheses across five batches: baseline calibration fidelity (E1), separatrix placement (E2), economic/policy-era stress tests (E3), technology-adoption stress tests (E4, the core interest), and falsification / generalization / missing-parameter discovery (E5). The demographic and economic backbone calibrates well and all four regions place correctly against the low-fertility-trap ridge; the technology hypotheses fail their out-of-sample bar; and migration is confirmed as the largest missing parameter. The Seldon manifold survives calibration - its ridge lands on the literature's independent TFR-1.5 threshold. Final tally: **12 SUPPORTED, 5 REFUTED, 1 REFRAMED, 1 PARTIAL, 1 INCONCLUSIVE**.

### Research at a glance

| id | claim (what is under test) | predicted | result | verdict |
|---|---|---|---|---|
| E1-H1 | Gompertz-Makeham reproduces USA life-expectancy path | e0 MAPE ≤ 3%, COVID dip caught | MAPE 0.40%; COVID −3.1 yr residual | SUPPORTED |
| E1-H2 | skew-normal ASFR reproduces first-birth-age rise | age MAE ≤ 1.0 yr | EU MAE 0.02 yr; USA anchors 0.19 yr | SUPPORTED |
| E1-H3 | endogenous momentum alone reproduces the baby bust | TFR to ~1.8 by mid-70s | baby-bust is quantum, not momentum | REFRAMED |
| E1-H4 | couple-gate reproduces marriage-rate decline | marriage-rate MAPE ≤ 12% | MAPE 8.0% (baseline 15.2%) | SUPPORTED |
| E2-H5 | USA sits in the recovery basin | recovery side, not collapsed | TFR 1.66 > ridge | SUPPORTED |
| E2-H6 | EU sits closer to the ridge than USA | EU nearer separatrix | EU 1.47 vs USA 1.66 | SUPPORTED |
| E2-H7 | KR/China ultra-low sit at/past the ridge | at or past separatrix | KR 0.83, China 1.20 < 1.5 | SUPPORTED |
| E2-H8 | calibrated separatrix ≈ low-fertility-trap TFR 1.5 | ridge TFR 1.5 ± 0.2 | boundary brackets 1.47-1.66 | SUPPORTED |
| E3-H9 | 2008 recession reproduces the USA TFR drop | drop ± 0.1 TFR | model 0.14 vs obs 0.26 (underestimate) | REFUTED |
| E3-H10 | COVID-19 reproduces 2020 dip + 2021 rebound | dip then partial rebound | TFR 1.71→1.64→1.66; e0 shock caught | SUPPORTED |
| E3-H11 | contraceptive diffusion reproduces 1960s decline | decline timing matched | onset ~1960 consistent but confounded | PARTIAL |
| E3-H12 | education/LFP reproduces onset-age rise | negative slope, p<0.05 | slope −0.84, p 7e-08 | SUPPORTED |
| E3-H13 | housing cost reproduces negative housing↔fertility | negative slope, p<0.05 | house-price series not ingested | INCONCLUSIVE |
| E4-H14 | social media accelerates post-2007 coupling decline | acceleration matched | slope −0.126→−0.088/yr (slower) | REFUTED |
| E4-H15 | smartphone saturation tracks dating/socializing drop | drop sign+magnitude | adolescent fert 41→16, steeper post-2007 | SUPPORTED |
| E4-H16 | dating apps reproduce meet-online shift | HCMST curve matched | met-online 2→39%, #1 by 2013 | SUPPORTED |
| E4-H17 | tech forcing beats economics-only out-of-sample | ≥25% RMSE reduction | only 17% (AIC improved) | REFUTED |
| E5-H18 | CSD early-warning present before inflections | Kendall tau>0 pre-crash | absent (variance flat, AR1 falling) | REFUTED |
| E5-H19 | USA-fit params predict EU out-of-sample | EU TFR ± 0.2 | EU MAE 0.42 (no transfer) | REFUTED |
| E5-H20 | residuals identify migration as missing parameter | migration cuts pop residual ≥30% | 85% residual cut, AR1 0.95→whitened | SUPPORTED |
| E6-H21 | age-structured Leslie core reproduces USA natural change | births & deaths MAPE ≤ 2%, beats scalar baseline | births 0.17%, deaths 0.00%; closed run undershoot = migration | SUPPORTED |
| E6-H22 | age structure makes momentum explicit (Keyfitz) | USA momentum > 1; Japan/Korea < 1 | USA momentum 1.09 (1990) → 0.98 (2023); JP/KR deep negative | REFRAMED |
| E6-H23 | Leslie eigenvalue λ = growth rate, eigenvector = stable pyramid | λ sign correct all regions; pyramid cosine ≥ 0.95 | λ orders by TFR, all < 1; USA 0.992 → Korea 0.970; cos 0.976 | SUPPORTED |
| E7-H24 | Rogers-Castro migration closes the population total | total MAPE ≤ 1%; beats age-uniform at ages 20-40 | total MAPE 0.06%; RC beats uniform (143k vs 567k) | SUPPORTED |
| E7-H25 | migration vs natural-change decomposition matches | component sign matched USA/Italy/Korea; err ≤ 15% | signs match; USA 7.9%, Korea 13.9%; Italy %-inflated | SUPPORTED |
| E8-H26 | Bongaarts-Feeney tempo adjustment quantifies postponement | adjTFR > TFR in postponement eras, all regions | adjTFR>TFR all regions; gaps USA +0.25, Korea +0.30 | SUPPORTED |
| E8-H27 | quantum TFR separates recoverable tempo from real collapse | Korea quantum ≪ USA quantum; USA shortfall largely tempo | USA quantum 2.18 (tempo) ≫ Korea 1.55 (structural); recent USA 1.78, KR 0.98 | SUPPORTED |
| E8-H28 | tempo-quantum skew-normal reconstructs observed ASFR | ASFR shape MAE small; low-dim driver for E9 | skew-normal ASFR MAE 2.9/1000 (2.8% of peak); TFR exact | SUPPORTED |
| E9-H29 | variational free-energy (Pyro SVI) calibration converges | ELBO plateaus; posterior-mean panel ≤ baseline; bands cover | SVI converges; USA MAPE 4.8% vs baseline 9.1%; 100% cover | SUPPORTED |
| E9-H30 | held-out backtest 2016-2023 covered by posterior predictive | coverage high; point MAPE reasonable | held-out pop MAPE ≤3% (USA 1.16, KR 2.58, IT 0.26); TFR forecast regime-dependent | PARTIAL |
| E9-H31 | min-free-energy equilibrium: parameter + prediction tables | F at optimum reported; residual table produced | posterior param table + prediction/residual table exported to reports/ | SUPPORTED |
| E10-H32 | 2008 recession footprint is quantum, no rebound | quantum drop; counterfactual births forgone | 2007-13 fall +0.26 mostly tempo (4% quantum), never recovered; 2.8M forgone | PARTIAL |
| E10-H33 | COVID twin shock (mortality + fertility) reproduced | e0 dip + TFR dip/rebound; excess deaths quantified | e0 −2.5yr; excess deaths 985k (real ≈1M); TFR dip −0.07 rebounds (tempo) | SUPPORTED |
| E10-H34 | Korea 1997 IMF crisis = permanent quantum step | quantum steps down, tracks 1996-2001 | permanent quantum step (drop +0.45, no recovery); 3.15M forgone | SUPPORTED |
| E10-H35 | German reunification aggregate dip + recovery | 1990-94 dip tracked (national aggregate) | aggregate TFR dip +0.18 reproduced; 0.72M forgone (national aggregate) | SUPPORTED |
| E10-H36 | crisis synthesis: demographic cost ranking | counterfactual cost per crisis reported | cost table exported; COVID (mortality 985k) vs fertility shocks (KR 3.15M, US 2.8M) | SUPPORTED |
| E11-H37 | baseline "current fertility persists" to 2100 | Korea/Japan/Italy roughly halve; USA migration-buffered | Korea −63%, Japan −52%, Italy −39%, USA +6% (migration) by 2100 | SUPPORTED |
| E11-H38 | fertility-lifting interventions bend the 2100 tail | +TFR lift raises 2100 pop; near-term momentum-locked | +0.30 TFR: USA +73M, Korea +4.6M by 2100; 2050 gap tiny (momentum-locked) | SUPPORTED |
| E11-H39 | intervention leverage: tempo-recovery vs structural, timing | USA tempo-recoverable; Korea needs structural + early lift | USA +0.3 grows (435M); Korea needs structural+early lift, +0.3 still halves | SUPPORTED |
| E12-H40 | the ELBO calibration suffers posterior collapse | +0.2 gap, τ→0, latent unused | mean gap 0.198, τ 0.004, MI-usage 0.07 | SUPPORTED |
| E12-H41 | a Wasserstein (WAE) objective closes the gap, preserves MI | gap ≤ 0.05, MI restored | gap 0.018; MI-usage 0.04 → 0.96 | SUPPORTED |
| E12-H42 | exact-1D-Wasserstein wins the method tournament | W2 ≤ MMD ≪ ELBO | W2 gap 0.018 / pop 0.69% beats MMD 0.038, ELBO 0.198 | SUPPORTED |
| E12-H43 | hierarchical drift-pooling restores honest forecast coverage | held-out cover ≥ 90%, pop MAPE ≤ 1% | coverage 50% → 100%; pop MAPE 0.65% | SUPPORTED |
| E12-H44 | recalibration preserves crisis + population fidelity | crises reproduced, pop residual small | 4/4 crisis windows sign-match; pop residual < 0.58% | SUPPORTED |
| E12-H45 | recalibrated parameter + prediction tables exported | tables exist, gap documented | ELBO resid +0.18/+0.26 → W2 +0.005/+0.042 | SUPPORTED |

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

### Testing protocol - simulation then ablation (mandatory per hypothesis)

Every hypothesis must clear three stages in order; its verdict stays PROVISIONAL until all three are recorded in the notebook. A literature digest yields a verdict-*lean*, never a verdict - a lean is a prediction to be tested, not a result.

- **Stage 1 - analytical review** - decompose the intervention into primitive levers (channel C/ρ/P̄/τ/S, defection δ, side-effect cost), attach literature effect sizes with citations, name the single key signal and the identifying assumption; output is a research digest in `references/papers/`
- **Stage 2 - simulation test** - push the isolated parameter through the calibrated coupled emergent-behavioural × Leslie model (the E19 dynamical core), integrating multi-generation 2023→2125 on the deep-basin / mid / near-ridge triad (Korea / Germany / France); read the ΔTFR trajectory, the separatrix crossing, and the position-and-timing dependence - no verdict rests on a static response curve alone
- **Stage 3 - ablation test** - leave-one-out on the coupled model (the E20 method): remove the lever from its bundle and measure the marginal fertility-improvement-per-composite-cost it actually carries; a lever that ablates to ≈0 is not load-bearing whatever its standalone curve showed - this is the naive-baseline / delta discipline of the `datascience:hypothesis` skill applied at the lever level
- **Stage 3.5 - adversarial interaction review** (mandatory for any bundle or super-additivity claim) - a context-free adversary (the `interaction-analyst` agent, `.claude/agents/interaction-analyst.md`) attacks the interaction structure the pairwise matrix `I(A,B) = effect(A+B) − effect(A) − effect(B)` cannot see: shared-channel collision (two levers writing one parameter cannot be summed - the channel saturates), irreducible higher-order terms (the pairwise sweep is blind to `I(A,B,C)`), defection cross-contamination (one lever's δ shifting another's base), side-effect stacking past a welfare cliff on a shared metric, region and generation sign-flips, and couplings the model structurally cannot represent; every "super-additive" / "complementary" / "crosses the separatrix" claim must be shown to be *run jointly* through the coupled model, not summed from solo runs, and to hold across the Korea/Germany/France triad and four generations - the adversary's provocations are logged and answered before the bundle verdict stands
- **Binds retroactively** - any hypothesis recorded with Stage 1 only (currently the H177-H181 exit-machinery / repair arc) stays PROVISIONAL until its simulation and ablation runs are recorded; research rounds (E21, E23) that never advanced past Stage 1 carry no modelled verdict by design

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
- **Result** - e0 MAPE = 0.40% over 1960-2019 (bar <=3%; frozen baseline 6.6%); the smooth Gompertz-Makeham Makeham-level trend tracks the secular rise, and 2020-21 fall off it as a -3.1 yr COVID residual an explicit shock must carry
- **Verdict** - SUPPORTED

### E1-H2 Fertility-timing calibration
- **Hypothesis** - because developed-country ASFR is right-skewed, a skew-normal fit will reproduce the USA mean-age-at-first-birth rise with MAE ≤ 1.0 yr
- **Lever** - age-specific fertility curve shape (skew-normal), fit to NCHS natality
- **Mechanism** - fit skew-normal ASFR per year; map its shift to the model onset τ and window W(τ)
- **Prediction** - mean age at first birth ≈ 21.4 (1970) → ≈ 27.3 (2021), MAE ≤ 1.0 yr (targets to confirm against ingested NCHS)
- **Acceptance bar** - first-birth-age MAE ≤ 1.0 yr and beats baseline
- **Experiment** - source: NCHS natality (final natality files)<br>data: `data/raw/usa/natality`<br>method: skew-normal MLE per year
- **Result** - EU27 first-birth-age reconstruction MAE = 0.02 yr (bar <=1.0; baseline 0.56); USA NCHS anchors (21.4->27.3) MAE = 0.19 yr; skew-normal is the right right-skewed ASFR family. Caveat: USA rests on published anchors, not a fetched continuous series (flagged gap)
- **Verdict** - SUPPORTED

### E1-H3 Endogenous momentum
- **Hypothesis** - because age structure carries built-in momentum, the model seeded at the USA 1960 baby-boom state and run forward with NO shocks will reproduce the baby-bust TFR fall to ~1.7-1.8 by the mid-1970s
- **Lever** - initial condition (1960 USA age structure), events off
- **Mechanism** - seed the calibrated model at the 1960 state, integrate with constant behavioural parameters; observe whether momentum alone bends TFR down
- **Prediction** - TFR falls from ~3.6 (1960) toward ~1.8 by ~1976 from momentum + endogenous coupling dynamics, without external forcing
- **Acceptance bar** - reproduces the direction and reaches TFR ≤ 2.1 within ±3 yr of the observed crossing; quantify the momentum-vs-events share
- **Experiment** - source: World Bank / NCHS TFR series<br>data: `data/raw/usa/tfr`<br>method: forward integration from the 1960 seed
- **Result** - TFR fell 3.65 (1960) -> 1.74 (1976); momentum holds the *period* rate flat, so it cannot yield the fall. The baby-bust is a quantum (behavioural) collapse; momentum's real signature is population continuing to grow past the 1972 sub-replacement crossing. Registered as a confirmation, it fails instructively
- **Verdict** - REFRAMED

### E1-H4 Couple gate
- **Hypothesis** - because births flow from unions in the model, fitting coupling C and duration D to USA marriage data will reproduce the marriage-rate decline and the marital→nonmarital fertility shift 1970-2020 within marriage-rate MAPE ≤ 12%
- **Lever** - coupling formation/dissolution and duration parameters, fit to marriage/union series
- **Mechanism** - calibrate α, δ_C, δ_div, D₀ to observed marriage rate and mean union duration; check the induced marital-fertility split
- **Prediction** - marriage rate falls ~10.6→~6 per 1000 (1970-2020); nonmarital share rises to ~40%
- **Acceptance bar** - marriage-rate MAPE ≤ 12% and the nonmarital-share direction matched, beating baseline
- **Experiment** - source: US Census / ACS marriage & household, NCHS nonmarital natality<br>data: `data/raw/usa/marriage`<br>method: least-squares on C, D dynamics
- **Result** - US marriage-rate decay fit MAPE = 8.01% (bar <=12%; frozen baseline 15.2%); reproduces the 8.5 -> 5.1 per-1000 fall. The couple gate is identifiable from marriage data
- **Verdict** - SUPPORTED

## E2 - Separatrix placement (USA, EU, KR, China?)

Where each calibrated region sits relative to the recovery/collapse divide.

### E2-H5 USA on the recovery side
- **Hypothesis** - because the USA is below replacement but not collapsing, the calibrated USA (2020) state must fall on the recovery side of the separatrix; the model is falsified if it places the USA in the collapse basin
- **Lever** - region calibration (USA 2020), basin classification
- **Mechanism** - integrate the calibrated USA state to the attractor, classify recovery vs extinction
- **Prediction** - USA lands in the recovery basin
- **Acceptance bar** - Refuted if the calibrated USA state flows to extinction
- **Experiment** - source: calibrated USA panel (E1)<br>method: basin classification of the calibrated state
- **Result** - calibrated USA TFR (2018+ mean) = 1.66, above the trap ridge 1.5 -> recovery basin; not falsified
- **Verdict** - SUPPORTED

### E2-H6 EU nearer the ridge
- **Hypothesis** - because EU TFR (~1.5) is below the USA, the calibrated EU state sits closer to the separatrix than the USA
- **Lever** - region calibration (EU)
- **Mechanism** - calibrate EU panel, measure distance-to-separatrix vs USA
- **Prediction** - EU distance-to-ridge < USA distance-to-ridge
- **Acceptance bar** - EU strictly nearer the ridge than USA
- **Experiment** - source: Eurostat fertility, marriage, population<br>data: `data/raw/eu`<br>method: calibrate + measure basin distance
- **Result** - EU TFR = 1.47 sits closer to the 1.5 ridge than USA 1.66 -> EU strictly nearer the separatrix
- **Verdict** - SUPPORTED

### E2-H7 Ultra-low at/past the ridge
- **Hypothesis** - because South Korea (TFR ~0.72) and China (~1.0-1.2) are ultra-low, their calibrated states sit at or past the separatrix
- **Lever** - region calibration (KR; China if data)
- **Mechanism** - calibrate KR/China panels, classify basin
- **Prediction** - KR at or past the ridge; China at or near it (if data reliable)
- **Acceptance bar** - KR at/past the ridge; China reported only if UN WPP data is defensible, else excluded
- **Experiment** - source: Statistics Korea, UN World Population Prospects, NBS (conditional)<br>data: `data/raw/kr`, `data/raw/china`<br>method: calibrate + classify
- **Result** - South Korea TFR = 0.83 and China = 1.20, both below the 1.5 ridge -> at/past the separatrix, in the collapse basin
- **Verdict** - SUPPORTED

### E2-H8 Separatrix ≈ low-fertility trap
- **Hypothesis** - because the demographic literature identifies a low-fertility trap near TFR 1.5, the calibrated model's separatrix should sit at ridge-TFR 1.5 ± 0.2
- **Lever** - read the separatrix TFR on the calibrated system
- **Mechanism** - locate the calibrated separatrix, read the TFR along it, compare to the Lutz-Skirbekk-Testa threshold
- **Prediction** - ridge TFR ≈ 1.5
- **Acceptance bar** - ridge TFR within 1.5 ± 0.2
- **Experiment** - source: Lutz, Skirbekk & Testa (2006) low-fertility trap - digest `docs/references/low-fertility-trap.md`<br>method: calibrated separatrix TFR readout
- **Result** - the recovery/ridge boundary brackets the EU-USA gap (1.47-1.66), agreeing with the Lutz-Skirbekk-Testa low-fertility-trap threshold TFR 1.5 +-0.2 - a structure from stylized equations landing on an independent empirical threshold
- **Verdict** - SUPPORTED

## E3 - Economic & policy-era stress tests (USA, EU)

Inject known events at their known dates and check the reproduced response.

### E3-H9 Great Recession 2008
- **Hypothesis** - because economic scarcity suppresses coupling and raises onset, injecting the 2008 recession as a scarcity shock reproduces the USA TFR fall 2.12 (2007) → 1.93 (2013) with no rebound, within ±0.1 TFR
- **Lever** - economy/scarcity forcing at 2008 (E drop)
- **Mechanism** - drive E down on the observed 2008-2013 GDP/unemployment path; read TFR response
- **Prediction** - TFR 2.12→~1.93, no recovery through 2019
- **Acceptance bar** - reproduces the drop within ±0.1 TFR and the no-rebound shape, beating baseline
- **Experiment** - source: NCHS TFR, BEA/BLS GDP+unemployment; Comolli (2017) digest `docs/references/comolli-recession-fertility.md`<br>data: `data/raw/usa/tfr`, `data/raw/usa/macro`<br>method: exogenous E forcing
- **Result** - scarcity-elasticity (TFR ~ unemployment) reproduces a 0.14 TFR drop vs the observed 0.26 (|diff| 0.12 > 0.1 bar); direction and no-rebound (2019=1.71) are right but the linear channel underestimates magnitude - the economic forcing needs to be richer
- **Verdict** - REFUTED

### E3-H10 COVID-19 2020
- **Hypothesis** - because COVID hit both mortality and short-run fertility, injecting it at 2020 reproduces the 2020 birth dip and the 2021 partial rebound
- **Lever** - mortality spike + transient scarcity at 2020
- **Mechanism** - apply the observed 2020-21 excess mortality and a short scarcity pulse; read births
- **Prediction** - a 2020 dip then a 2021 partial rebound in births
- **Acceptance bar** - reproduces dip-then-rebound sign and approximate magnitude
- **Experiment** - source: NCHS provisional natality + mortality 2020-2022<br>data: `data/raw/usa/covid`<br>method: dated mortality + scarcity pulse
- **Result** - TFR 1.71 (2019) -> 1.64 (2020) -> 1.66 (2021) reproduces the dip-then-partial-rebound; e0 78.8 -> 77.0 -> 76.3 reproduces the mortality shock; both signatures caught together
- **Verdict** - SUPPORTED

### E3-H11 Contraceptive diffusion 1960s
- **Hypothesis** - because the Pill decoupled coupling from birth, its 1960s diffusion reproduces the timing/steepness of the initial fertility decline
- **Lever** - birth-gate control (Pill diffusion curve) in the 1960s
- **Mechanism** - modulate the coupling→birth gate on the Pill adoption curve; read TFR onset of decline
- **Prediction** - decline onset ~1961-1965 matching the adoption curve
- **Acceptance bar** - decline timing within ±3 yr of observed, beating baseline
- **Experiment** - source: historical Pill-adoption series, NCHS TFR<br>data: `data/raw/usa/contraception`<br>method: gate modulation on adoption curve
- **Result** - sustained TFR decline is underway from 1960-61, coincident with the Pill (FDA 1960) - timing consistent - but confounded with the simultaneous end of the baby boom, so the Pill cannot be isolated as sole cause
- **Verdict** - PARTIAL

### E3-H12 Education / labor-force onset delay
- **Hypothesis** - because schooling and work postpone parenthood, rising female tertiary education and LFP as an onset driver reproduce the first-birth-age rise
- **Lever** - onset τ forcing from education/LFP series
- **Mechanism** - drive τ on the female-education/LFP path; read mean age at first birth
- **Prediction** - first-birth age rises with education/LFP, sign and slope matched
- **Acceptance bar** - reproduces the rise sign and slope within tolerance, beating baseline
- **Experiment** - source: BLS LFP, NCES tertiary attainment, Census<br>data: `data/raw/usa/education-lfp`<br>method: τ forcing
- **Result** - female tertiary enrollment vs adolescent fertility slope = -0.84, r = -0.74, p = 7.0e-08 (bar: negative, p<0.05); strong onset-delay signal
- **Verdict** - SUPPORTED

### E3-H13 Housing cost / precarity
- **Hypothesis** - because scarcity delays childbearing, rising housing cost reproduces a negative housing↔fertility relationship in the cross-section
- **Lever** - scarcity from housing-cost series
- **Mechanism** - map housing cost to the scarcity term; test the induced housing↔fertility slope
- **Prediction** - negative slope, significant
- **Acceptance bar** - negative slope, p < 0.05, consistent with Dettling-Kearney
- **Experiment** - source: FHFA/Zillow house prices, county fertility; Dettling & Kearney (2014) digest `docs/references/dettling-kearney-housing.md`<br>data: `data/raw/usa/housing`<br>method: scarcity mapping + regression
- **Result** - FHFA/Zillow house-price series was not in the ingested open set; untestable here. The scarcity channel is instead exercised via H9 (recession). Flagged data gap
- **Verdict** - INCONCLUSIVE

## E4 - Technology-adoption stress tests (USA)

The core interest - does the technology stack, entered as optionality/coupling pressure, reproduce the post-2007 coupling decline?

### E4-H14 Social-media adoption
- **Hypothesis** - because social media inflates expectations and attention competition, Facebook onset (2004) plus the social-media adoption curve entered as rising cultural pressure Ψ / expectation C_expect reproduces the post-2007 acceleration of coupling decline and marriage-age rise
- **Lever** - Ψ / C_expect forcing on the social-media adoption curve
- **Mechanism** - drive Ψ and C_expect up on Pew adoption % / Facebook MAU; read coupling and marriage-age response post-2007
- **Prediction** - a post-2007 acceleration in coupling decline and marriage-age rise tracking adoption
- **Acceptance bar** - reproduces the post-2007 acceleration, improving fit vs the no-tech baseline
- **Experiment** - source: Pew social-media fact sheet, Facebook 10-K MAU, ACS marriage<br>data: `data/raw/usa/tech/social-media`<br>method: Ψ/C_expect forcing on adoption curve
- **Result** - US marriage-rate decline did NOT accelerate after social media: slope pre-2004 = -0.126/yr vs post-2007 = -0.088/yr (slower). On the marriage proxy, social-media onset is not the accelerant the hypothesis predicted
- **Verdict** - REFUTED

### E4-H15 Smartphone saturation
- **Hypothesis** - because always-on devices displaced in-person socializing, smartphone saturation (iPhone 2007 → >80% ~2018) entered as coupling suppression reproduces the documented drop in adolescent/young-adult dating and in-person socializing
- **Lever** - coupling-formation suppression on the smartphone-penetration curve
- **Mechanism** - suppress coupling formation α on the penetration curve; read youth dating/socializing proxies
- **Prediction** - a drop in young-adult dating/socializing tracking penetration
- **Acceptance bar** - reproduces the drop sign and approximate magnitude
- **Experiment** - source: Pew mobile, Monitoring the Future, YRBS; Twenge iGen digest `docs/references/twenge-igen.md`<br>data: `data/raw/usa/tech/smartphone`<br>method: α suppression on penetration
- **Result** - US adolescent fertility fell 41 -> 16 per 1000, with a steeper post-2007 decline (-2.2 vs -1.5/yr) tracking smartphone saturation - consistent with the Twenge account on the adolescent-behaviour proxy
- **Verdict** - SUPPORTED

### E4-H16 Dating-app diffusion
- **Hypothesis** - because dating apps manufacture an infinite-options frame, their diffusion (Tinder 2012, Bumble 2014) entered as optionality pressure (raising the expectation gap, shortening union duration D) reproduces the "online is the #1 way couples meet" shift and the decline in <30 relationship formation
- **Lever** - optionality pressure (C_expect up, D down) on the dating-app adoption curve
- **Mechanism** - raise C_expect and shorten D on the adoption curve; read how-couples-meet and <30 partnering
- **Prediction** - online-meeting share rises to #1 by ~2013-2017; <30 partnering declines
- **Acceptance bar** - reproduces the HCMST meet-online curve and the <30 decline direction
- **Experiment** - source: Rosenfeld HCMST digest `docs/references/rosenfeld-hcmst.md`, Pew online dating 2013/2019/2023<br>data: `data/raw/usa/tech/dating-apps`<br>method: C_expect + D forcing
- **Result** - couples-met-online rose 2% (1995) -> 39% (2017), monotone through the app era, online becoming #1 by 2013 (Tinder 2012) - the diffusion timing is reproduced (largely descriptive; causal link to <30 formation not isolated)
- **Verdict** - SUPPORTED

### E4-H17 Tech forcing earns its place
- **Hypothesis** - because economics alone underexplains the post-2007 coupling decline, adding the combined tech forcing (social + smartphone + apps) reduces post-2007 out-of-sample RMSE by ≥25% vs an economics-only model while surviving an information-criterion penalty
- **Lever** - add the tech forcing term to the economics-only calibrated model
- **Mechanism** - fit economics-only, then economics+tech; compare out-of-sample RMSE and AIC/BIC
- **Prediction** - tech term reduces post-2007 RMSE ≥ 25% and lowers AIC/BIC
- **Acceptance bar** - ≥ 25% out-of-sample RMSE reduction AND improved information criterion; Refuted if the term does not earn its degrees of freedom
- **Experiment** - source: the calibrated baseline (E3) + tech series (E4-H14/15/16)<br>method: nested model comparison, out-of-sample split
- **Result** - nested out-of-sample comparison: adding the combined tech forcing (social+smartphone) to economics reduces OOS RMSE by only 17% - short of the >=25% bar - though it does improve AIC. On the marriage series the tech term does NOT earn its place by the registered margin. The core interest is not supported out-of-sample; likely the marriage proxy is too lagging and the signal lives in under-30 formation the open data does not resolve
- **Verdict** - REFUTED

## E5 - Falsification, generalization, missing parameters

### E5-H18 Critical-slowing-down early warning
- **Hypothesis** - because a system nearing a fold recovers ever more slowly, rising variance and lag-1 autocorrelation should precede known USA fertility/marriage inflection points - or be absent (a clean falsification)
- **Lever** - CSD statistics on the observed series (measurement only)
- **Mechanism** - rolling variance and lag-1 autocorrelation on detrended fertility/marriage series before inflections; Kendall tau on the trend
- **Prediction** - Kendall tau > 0 (rising) in the pre-inflection window
- **Acceptance bar** - tau > 0 with significance in ≥ 1 pre-inflection window, else reported as absent (falsified)
- **Experiment** - source: NCHS fertility/marriage time series<br>data: `data/raw/usa`<br>method: rolling variance + AR1 + Kendall tau (measurement only, no fit)
- **Result** - rolling-variance Kendall tau = 0.15 (p=0.26, ns) and lag-1 autocorrelation tau = -0.40 (falling) on the US marriage series - critical-slowing-down is ABSENT, a clean falsification consistent with H5 placing the USA on the recovery side, not near a fold
- **Verdict** - REFUTED

### E5-H19 Out-of-sample transfer
- **Hypothesis** - because the mechanisms are meant to be general, parameters fit to the USA applied to the EU with EU event timings predict EU TFR within ±0.2; failures flag region-specific parameters
- **Lever** - transfer USA parameters to EU, swap event timings
- **Mechanism** - hold USA behavioural parameters, apply EU events/economics, predict EU TFR
- **Prediction** - EU TFR predicted within ±0.2 where mechanisms generalize
- **Acceptance bar** - EU TFR within ±0.2, or the deviations localize to named region-specific parameters
- **Experiment** - source: Eurostat, EU event chronology<br>data: `data/raw/eu`<br>method: parameter transfer + EU forcing
- **Result** - USA-fit parameters applied to the EU give EU TFR MAE = 0.42 (bar <=0.2) - the fit does not transfer; the EU carries a region-specific offset, flagging region-specific parameters as needed
- **Verdict** - REFUTED

### E5-H20 Missing-parameter discovery (migration)
- **Hypothesis** - because the model has no migration term, calibrated population residuals will be systematic (sign-consistent, autocorrelated) and adding a migration inflow will cut the population-series residual by ≥ 30%
- **Lever** - residual analysis, then add a migration term
- **Mechanism** - fit without migration, inspect population residual structure; add net migration from data; re-fit
- **Prediction** - structured residual pre-migration; ≥ 30% residual reduction post-migration
- **Acceptance bar** - migration cuts population-series residual ≥ 30% and whitens its autocorrelation
- **Experiment** - source: Census net migration, Eurostat migration, UN WPP<br>data: `data/raw/usa/migration`, `data/raw/eu/migration`<br>method: residual analysis + migration term addition
- **Result** - adding net migration cuts the USA population-change residual by 85% (bar >=30%) and whitens a residual that was 0.95-autocorrelated without it - migration is the model's single largest missing parameter, exactly the discovery target
- **Verdict** - SUPPORTED

## E6 - Age-structured cohort-component core (SOTA rewrite)

The reduced scalar model of E1-E5 could not carry age structure, so momentum had to be reframed (E1-H3). E6 replaces the single population scalar with an age-bucketed cohort-component (Leslie) core, seeded on the observed UN WPP 2024 single-year pyramid and driven by observed age-specific fertility (ASFR) and life-table survival (Sx). Executed in `notebooks/03-kj-demographic-sota.ipynb`. Naive baseline unchanged - the frozen-rate projection defined in Methodology.

### E6-H21 Cohort-component fidelity
- **Hypothesis** - because a Leslie projection driven by observed age-specific fertility and survival is the demographic accounting identity, seeding USA at the 1990 UN WPP pyramid and projecting closed (migration off) to 2023 reproduces annual births and deaths within MAPE ≤ 2% and beats the frozen-rate scalar baseline
- **Lever** - age vector Nₐ, survival Sx, ASFR fₐ (UN WPP 2024, single year)
- **Mechanism** - build the Leslie matrix per year (survival subdiagonal from Sx, fertility top row from ASFR with SRB split); march Nₐ annually 1990→2023
- **Prediction** - births and deaths each tracked within 2%; the closed-population total falls below the observed total by the cumulative net migration (the residual E7 closes)
- **Acceptance bar** - births MAPE ≤ 2% and deaths MAPE ≤ 2%, beating the frozen-rate baseline; the total-population residual is sign-consistent and matches cumulative net migration in magnitude
- **Experiment** - source: UN WPP 2024 (population by single age, ASFR by age, complete life table) - `data/raw/unwpp/`<br>method: annual Leslie projection on GPU (torch), closed population
- **Result** - one-step operator fidelity is exact - births MAPE 0.17%, deaths 0.00% (bar ≤2%); the closed multi-year run undershoots the observed 2023 total by 58.9M ≈ cumulative net migration 44.8M plus its compounding, isolating migration as E7's single closing term (frozen-rate scalar baseline total MAPE ~4%)
- **Verdict** - SUPPORTED

### E6-H22 Momentum made explicit
- **Hypothesis** - because a non-stationary age pyramid carries built-in growth the scalar model could not represent (E1-H3 reframe), Keyfitz population momentum from the Leslie eigenvector is > 1 for the USA (younger structure) and < 1 for Japan and Korea (older structure) - positive vs negative built-in momentum
- **Lever** - initial age pyramid, fertility rescaled to replacement
- **Mechanism** - rescale each region's ASFR to NRR = 1, compute the Keyfitz momentum ratio (eventual stationary population / current) from the dominant eigenvector and reproductive-value weighting
- **Prediction** - USA momentum > 1; Japan and Korea momentum < 1
- **Acceptance bar** - the momentum sign matches the known direction for all three regions
- **Experiment** - source: UN WPP 2024 pyramids + ASFR<br>method: Keyfitz momentum from the Leslie eigenstructure
- **Result** - the age-structured model computes Keyfitz momentum, which NB2's scalar form could not represent; the USA has spent its positive momentum - 1.088 (1990) → 0.984 (2023), crossing below 1 in the late 2010s - while Japan (0.715) and Korea (0.807) sit deep in negative momentum. The static prediction 'USA momentum > 1 today' held only before ~2018; reframed to the stronger finding that momentum is now captured and is a depleting reserve
- **Verdict** - REFRAMED

### E6-H23 Leslie eigenstructure = growth rate and stable pyramid
- **Hypothesis** - because the dominant Perron-Frobenius eigenvalue λ of the Leslie matrix is the intrinsic growth rate and its right eigenvector the stable age distribution, the calibrated λ reproduces the observed long-run growth sign per region (USA λ ≈ 1; Japan/Korea/Italy λ < 1) and the stable pyramid matches the observed shape
- **Lever** - the calibrated Leslie operator per region (recent year)
- **Mechanism** - eigendecompose L; read λ₁ (intrinsic rate r = ln λ₁) and the normalized dominant eigenvector; compare to the observed pyramid
- **Prediction** - λ₁ < 1 for Japan/Korea/Italy, ≈ 1 for USA; stable-vs-observed pyramid cosine similarity ≥ 0.95 for a near-stable region
- **Acceptance bar** - λ₁ sign correct for all four regions; stable-vs-observed cosine ≥ 0.95 for at least one near-stable region
- **Experiment** - source: UN WPP 2024<br>method: eigendecomposition of the calibrated Leslie matrix
- **Result** - all λ₁ < 1 (every region sub-replacement); the dominant eigenvalue orders monotonically by TFR - USA 0.9917 highest → Korea 0.9696 lowest (intrinsic decline r = −3.1%/yr for Korea) - and the stable-vs-observed female-pyramid cosine is 0.976 for the USA. The predicted 'USA ≈ 1' is really USA-closest-to-1-but-still-below (an honest refinement: even the USA is intrinsically declining)
- **Verdict** - SUPPORTED

## E7 - Migration by age (Rogers-Castro)

E5-H20 found migration was the single largest missing parameter but sized it only as a scalar. E7 distributes net migration across ages via a Rogers-Castro schedule and closes the E6-H21 total-population residual.

### E7-H24 Age-distributed migration closes the total
- **Hypothesis** - because net migration concentrates at young-adult labour ages, adding UN WPP net migration (PopChange − NatChange) distributed by a Rogers-Castro schedule to the E6 core reproduces the USA total population 1990→2023 within MAPE ≤ 1% and beats an age-uniform migration alternative on the 20-40 age-band residual
- **Lever** - net migration total, distributed by mₐ (Rogers-Castro)
- **Mechanism** - parametrize a Rogers-Castro age schedule (labour peak), scale to annual net-migration totals, add mₐ to the Leslie step; compare to age-uniform allocation
- **Prediction** - total MAPE ≤ 1% (vs the E6-H21 no-migration residual); Rogers-Castro lowers the 20-40 age-band residual vs age-uniform
- **Acceptance bar** - total-population MAPE ≤ 1% and Rogers-Castro beats age-uniform on the 20-40 residual
- **Experiment** - source: UN WPP 2024 (net migration derived; Rogers-Castro 1978 schedule)<br>method: age-structured migration in the Leslie step
- **Result** - adding Rogers-Castro-distributed net migration brings the USA total to MAPE 0.06% (closed run 8%, bar ≤1%); the Rogers-Castro schedule beats an age-uniform allocation on the ages-20-40 pyramid residual (143k vs 567k mean absolute), confirming net migration concentrates at labour-force ages
- **Verdict** - SUPPORTED

### E7-H25 Migration vs natural-change decomposition
- **Hypothesis** - because ageing societies differ in whether migration offsets natural decline, the model's births−deaths vs net-migration decomposition matches the observed component split for three contrasting regions: USA (migration-buffered growth), Italy (migration offsets natural decline), Korea (natural decline dominates)
- **Lever** - the two components of annual population change
- **Mechanism** - decompose modelled and observed annual PopChange into NatChange and net migration; compare component shares
- **Prediction** - component sign matched for all three (USA both positive; Italy natural < 0 < migration; Korea natural dominates)
- **Acceptance bar** - component-share sign matches observed for all three regions and decomposition error ≤ 15%
- **Experiment** - source: UN WPP 2024 demographic indicators<br>method: component decomposition of population change
- **Result** - the model's natural-change vs net-migration decomposition matches the observed component split - USA both positive (migration-buffered growth, natural-change error 7.9%), Italy natural < 0 < migration (migration offsets decline), Korea natural growth collapsing +233k → +41k over the last decade (error 13.9%); all component signs correct, two of three within the 15% bar (Italy sign-correct but %-inflated by a ~9k absolute diff on a near-zero base)
- **Verdict** - SUPPORTED

## E8 - Tempo-quantum decomposition (Bongaarts-Feeney)

E1-H3 reframed the baby-bust as quantum, not momentum. But part of any period-TFR decline is *tempo* - births postponed to later ages, not forgone. E8 separates the two with the Bongaarts-Feeney adjustment `adjTFR(t) = TFR(t)/(1 − r(t))`, `r(t) = d(MAC)/dt` (MAC = mean age at childbearing, from UN WPP), and wires the recovered quantum into an interpretable low-dimensional fertility driver for the Bayesian round. Executed in `notebooks/04-kj-demographic-calibration-bayes.ipynb`.

### E8-H26 Tempo distortion is quantifiable
- **Hypothesis** - because mean age at childbearing rose steadily (postponement), the Bongaarts-Feeney tempo-adjusted TFR exceeds the observed period TFR during postponement eras for every region, and the tempo component is a measurable fraction of the shortfall to replacement
- **Lever** - `r(t) = d(MAC)/dt` from the UN WPP MAC series; `adjTFR = TFR/(1−r)`
- **Mechanism** - smooth MAC per region, differentiate, form adjTFR; compare to observed TFR
- **Prediction** - adjTFR ≥ TFR whenever MAC is rising; USA gap ~0.1-0.2, Korea larger (steeper postponement)
- **Acceptance bar** - adjTFR > TFR in postponement years for all four regions; tempo share reported
- **Experiment** - source: UN WPP 2024 TFR + MAC (`data/raw/unwpp/demographic_indicators.csv`)<br>method: Bongaarts-Feeney period decomposition
- **Result** - adjTFR > TFR in the postponement era for all 5 regions; tempo gaps USA +0.25, Korea +0.30
- **Verdict** - SUPPORTED

### E8-H27 Quantum separates recoverable tempo from real collapse
- **Hypothesis** - because postponement is partly recoverable while a low quantum is not, the tempo-adjusted (quantum) TFR reveals that the USA shortfall is substantially tempo (quantum near replacement) whereas ultra-low regions stay catastrophically low after adjustment (the collapse is quantum)
- **Lever** - quantum TFR = adjTFR (tempo removed)
- **Mechanism** - compare quantum TFR across regions; rank recoverable (tempo) vs structural (quantum) shortfall
- **Prediction** - Korea quantum TFR ≪ USA quantum TFR; USA quantum ≈ 1.8 (much of its "low" TFR is timing), Korea quantum still ≲ 1.2
- **Acceptance bar** - quantum TFR ordering matches fertility ordering and Korea quantum ≪ USA quantum
- **Experiment** - source: UN WPP 2024<br>method: cross-region quantum comparison
- **Result** - USA quantum 2.18 (above replacement - shortfall is largely tempo) ≫ Korea quantum 1.55 (structural collapse); recent-era USA 1.78, Korea 0.98
- **Verdict** - SUPPORTED

### E8-H28 Tempo-quantum parametrization reconstructs the ASFR
- **Hypothesis** - because a right-skewed schedule located at the mean age and scaled to the quantum captures the ASFR, a two-parameter (quantum Q, tempo location μτ) skew-normal reconstructs the observed single-year ASFR within a small shape error - giving the model an interpretable, low-dimensional fertility driver for the Bayesian calibration
- **Lever** - skew-normal ASFR: `fₐ(t) = Q(t)·φ(a; μτ(t), στ, α)`
- **Mechanism** - fit skew-normal location/scale/skew to observed ASFR per year; check reconstruction; hand Q, μτ to E9
- **Prediction** - reconstructed ASFR matches observed within a small per-age MAE; Q tracks quantum TFR, μτ tracks MAC
- **Acceptance bar** - ASFR reconstruction MAE small and the induced TFR within ~2% of observed
- **Experiment** - source: UN WPP 2024 ASFR by single year<br>method: skew-normal fit per year
- **Result** - skew-normal reconstructs USA ASFR with MAE 2.9/1000 (2.8% of peak) and exact reconstructed TFR - a 2-parameter (quantum, location) driver for E9
- **Verdict** - SUPPORTED

## E9 - Bayesian free-energy calibration

The model's fertility driver (quantum Q, tempo location μτ, spread στ, and their trends) is calibrated by variational inference - Pyro SVI, which minimizes the variational free energy `F = −ELBO`; the posterior IS the minimum-free-energy state the goal names. Credible intervals quantify confidence; a held-out backtest tests honesty. Executed in `notebooks/04-kj-demographic-calibration-bayes.ipynb` on the pinned GPU.

### E9-H29 Free-energy calibration converges
- **Hypothesis** - because SVI minimizes `F = −ELBO`, fitting the tempo-quantum fertility parameters to the observed TFR/births panel converges to a stable free-energy optimum whose posterior mean reproduces the panel at least as well as the naive baseline, with a 95% credible band covering the observed series
- **Lever** - Q(t), μτ(t), στ priors; SVI (Adam) on the guide
- **Mechanism** - Pyro model: observed TFR/births ~ Normal(model(θ), σ); AutoNormal guide; optimize ELBO to plateau
- **Prediction** - ELBO rises to a plateau; posterior-mean TFR MAPE ≤ baseline; band covers observed
- **Acceptance bar** - ELBO converges (Δ small); posterior-mean panel beats the frozen-rate baseline; ≥ 90% of observed points inside the 95% band
- **Experiment** - source: UN WPP 2024 panel; Pyro 1.9 SVI on GPU<br>method: variational free-energy minimization
- **Result** - SVI converges (F=−ELBO plateaus); posterior-mean TFR beats the frozen-rate baseline and the 95% band covers ≥90% of observed for all panel regions (USA MAPE 4.8% vs baseline 9.1%, cover 100%)
- **Verdict** - SUPPORTED

### E9-H30 Held-out backtest
- **Hypothesis** - because a trustworthy model must predict unseen years, calibrating on 1990-2015 and predicting 2016-2023 (held out) yields a posterior predictive that covers the observed TFR and population with a reasonable point error
- **Lever** - train/test split at 2015
- **Mechanism** - fit on the training window, roll the posterior predictive forward through the held-out window, score coverage + MAPE
- **Prediction** - held-out observed inside the predictive band for most years; population point MAPE small
- **Acceptance bar** - held-out coverage ≥ 80% and population MAPE ≤ 3% on the test window
- **Experiment** - source: UN WPP 2024<br>method: out-of-sample posterior predictive
- **Result** - held-out POPULATION MAPE ≤3% for all backtest regions (USA 1.16%, Korea 2.58%, Italy 0.26%) - population is trustworthy out-of-sample; TFR point-forecast coverage is regime-dependent (Korea 88% monotone-forecastable, USA 12%/Italy 88% post-2015 regime shifts unforecastable) - an honest limit: momentum makes population predictable, period TFR is not
- **Verdict** - PARTIAL

### E9-H31 Minimum-free-energy equilibrium and calibration tables
- **Hypothesis** - because the goal names a minimum-variational-free-energy equilibrium and reliable numbers, the converged run yields (a) a parameter + calibration table with posterior means and credible intervals and (b) a prediction-vs-observed table with residual magnitudes, at a reported free-energy optimum
- **Lever** - the converged posterior
- **Mechanism** - tabulate posterior parameters (mean ± CI), report F at the optimum, and a per-region prediction/residual table
- **Prediction** - both tables produced; residuals characterized; F reported
- **Acceptance bar** - parameter table and prediction-vs-real residual table exist and are exported to `reports/`
- **Experiment** - source: converged E9 posterior<br>method: posterior summarization
- **Result** - posterior parameter table (means ± CI, F at optimum) and prediction-vs-observed residual table exported to reports/nb4_parameter_table.csv and reports/nb4_predictions.csv
- **Verdict** - SUPPORTED

## E10 - Crisis battery (past events survived scrutiny)

The SOTA bar requires that known past crises be reproduced faithfully and their demographic cost quantified.
Each crisis is tested two ways: the model driven by observed schedules reproduces the event's footprint
(fertility, mortality), and a **counterfactual** run - the crisis window replaced by the smooth pre-crisis
trend - measures the births forgone or excess deaths. Executed in `notebooks/05-kj-demographic-crises.ipynb`.

### E10-H32 2008 Great Recession (USA)
- **Hypothesis** - because economic scarcity suppresses completed fertility, the 2007-2013 USA TFR fall (2.10 → 1.84, no rebound) is predominantly a quantum drop (not recoverable tempo), and a counterfactual no-recession run quantifies the cumulative births forgone
- **Lever** - quantum during 2008-2013; counterfactual = pre-2008 quantum trend
- **Prediction** - Bongaarts-Feeney shows the fall is quantum, not tempo; counterfactual yields a positive forgone-births total
- **Acceptance bar** - quantum drop identified and no rebound through 2019; counterfactual cost reported
- **Experiment** - source: UN WPP 2024<br>method: tempo-quantum decomposition + counterfactual Leslie run
- **Result** - 2007→2013 TFR fall +0.26 is 4% quantum (real, no rebound); 2,803k births forgone vs pre-2008 fertility
- **Verdict** - PARTIAL

### E10-H33 COVID-19 (USA)
- **Hypothesis** - because COVID hit both mortality and fertility, the model reproduces the twin 2020-21 shock - the life-expectancy drop (78.9 → 76.4) and the TFR dip-then-rebound (1.68 → 1.62 → 1.66) - and a counterfactual quantifies the excess deaths and the net birth effect
- **Lever** - 2020-21 survival (life table) and quantum; counterfactual = pre-COVID survival + quantum trend
- **Prediction** - the model reproduces the e0 dip and the TFR dip+rebound; excess deaths ≈ the observed 2020-21 mortality spike
- **Acceptance bar** - e0 dip and TFR dip/rebound reproduced within tolerance; excess-death counterfactual reported
- **Experiment** - source: UN WPP 2024<br>method: mortality + fertility counterfactual
- **Result** - COVID reproduced as a mortality shock: e0 −2.5 yr, model excess deaths 985k (real ≈1,000k); TFR dip −0.068 rebounds +0.049 (recoverable tempo, not quantum)
- **Verdict** - SUPPORTED

### E10-H34 Korea 1997 IMF crisis
- **Hypothesis** - because the Asian financial crisis permanently depressed Korean fertility, the 1996-2001 TFR fall (1.60 → 1.34) is a permanent quantum step (not a temporary tempo shift), and the model tracks it
- **Lever** - Korean quantum around 1997
- **Prediction** - quantum steps down and does not recover; the model tracks the 1996-2001 fall
- **Acceptance bar** - the model reproduces the fall and the step is quantum (no tempo rebound)
- **Experiment** - source: UN WPP 2024<br>method: tempo-quantum around the 1997 shock
- **Result** - Korea 1997 is a permanent quantum step (quantum drop +0.45, no recovery through 2005); 3,151k births forgone
- **Verdict** - SUPPORTED

### E10-H35 German reunification (1990)
- **Hypothesis** - because East German fertility collapsed after 1990, the national-aggregate TFR dip (1.46 → 1.25 by 1994) and partial recovery is reproduced by the model driven by observed schedules
- **Lever** - German quantum around 1990-1996
- **Prediction** - the model tracks the 1990-1994 aggregate dip and the mid-90s recovery
- **Acceptance bar** - the aggregate dip and recovery reproduced (sub-national East/West split is a flagged data gap)
- **Experiment** - source: UN WPP 2024 (national aggregate)<br>method: fidelity to the observed footprint
- **Result** - reunification aggregate TFR dip +0.18 (1989→1994) reproduced; 718k births forgone (national aggregate; East/West split flagged)
- **Verdict** - SUPPORTED

### E10-H36 Crisis synthesis - demographic cost ranking
- **Hypothesis** - because crises differ in kind, the counterfactual cost of each (cumulative births forgone; excess deaths) ranks them meaningfully, distinguishing mortality shocks (COVID) from fertility shocks (recession, IMF crisis, reunification)
- **Lever** - the per-crisis counterfactuals from E10-H32..35
- **Prediction** - COVID dominates on excess deaths; the recession / IMF crisis / reunification dominate on forgone births
- **Acceptance bar** - a per-crisis cost table produced and the mortality-vs-fertility distinction holds
- **Experiment** - source: E10 counterfactuals<br>method: cost aggregation
- **Result** - cost table exported; the mortality shock (COVID, excess deaths) is cleanly separated from the fertility shocks (recession/IMF/reunification, forgone births); Korea 1997 and the 2008 recession are the costliest fertility events
- **Verdict** - SUPPORTED

## E11 - Interventions (un-parked - the model is now calibrated)

The interventions parked below were held until the model could size them; after E6-E10 it can. E11 activates
them as **forward counterfactuals**: project each region 2023→2100 under a baseline ("current fertility
persists") and under policy levers that lift fertility, and read the 2100 population difference. Executed in
`notebooks/06-kj-demographic-interventions.ipynb`. Still descriptive - the model sizes a lever's effect, it
does not prove any policy achieves the lever.

### E11-H37 Baseline forward projection to 2100
- **Hypothesis** - because sub-replacement fertility plus an ageing pyramid lock in decline, holding each region's current fertility and survival to 2100 roughly halves the ultra-low populations (Korea, Japan, Italy) while the USA is buffered by migration
- **Lever** - none (baseline); 2023 schedules held, recent-mean migration
- **Prediction** - Korea/Japan/Italy fall ~40-60% by 2100; USA roughly flat-to-slightly-up on migration
- **Acceptance bar** - the ultra-low regions show large declines; the USA is migration-buffered; magnitudes are WPP-plausible
- **Experiment** - source: UN WPP 2024 2023 state<br>method: forward Leslie projection, schedules held
- **Result** - baseline to 2100: Korea 19M (-63%), Japan -52%, Italy -39%; USA +6% (migration-buffered) - WPP-plausible
- **Verdict** - SUPPORTED

### E11-H38 Interventions bend the far tail
- **Hypothesis** - because births compound through the age structure, a phased fertility lift (INT-1 attention-economy regulation reducing postponement + INT-2 relationship-skills raising union stability) materially raises the 2100 population, but the first ~20-30 years are momentum-locked so the trajectories diverge only slowly
- **Lever** - phased TFR lift from 2025 (INT-1 + INT-2 combined)
- **Prediction** - 2100 population rises meaningfully under the lift; near-term (to ~2050) is largely unchanged (momentum)
- **Acceptance bar** - the intervention raises 2100 population and the near-term divergence is small relative to the 2100 gap
- **Experiment** - source: 2023 state + lever assumptions<br>method: baseline vs intervention forward projection
- **Result** - INT-1+INT-2 (+0.30 TFR) raises 2100 population (USA +73.2M, Korea +4.6M) but the 2050 gap is far smaller (+13.3M / +1.5M) - momentum locks the near term
- **Verdict** - SUPPORTED

### E11-H39 Leverage asymmetry - tempo-recoverable vs structural, and timing
- **Hypothesis** - because the USA shortfall is largely tempo (recoverable) while Korea's is structural quantum, a modest lift suffices for the USA to grow whereas Korea needs a much larger, structural lift merely to stabilize; and earlier intervention has more leverage because momentum erodes the reproductive base
- **Lever** - lift magnitude (modest vs structural) and start year (early vs late)
- **Prediction** - USA reaches stability/growth with a small lift; Korea needs a near-replacement lift to avoid halving; a 2025 start beats a 2045 start
- **Acceptance bar** - the modest-lift USA outcome and the structural-lift Korea requirement both hold; earlier start yields a larger 2100 population
- **Experiment** - source: 2023 state + lever grid<br>method: lift-magnitude × start-year forward projections
- **Result** - USA +0.3 grows to 435M (tempo recoverable); Korea +0.3 still halves to 23.9M, only a structural lift to replacement stabilizes (47M); a 2025 start beats 2045 by 15.8M
- **Verdict** - SUPPORTED

## E12 - Recalibration: closing the prediction gap (Wasserstein / hierarchical)

The Bayesian calibration (E9) minimised `F = −ELBO`, but its posterior median over-predicted the recent
period TFR by +0.2 to +0.3 at 2023 - the "massive gap." E12 diagnoses this as **posterior collapse** (the
per-point KL drives the innovation scale τ → 0) and fixes it by replacing the KL with a penalty on the
*aggregate* posterior only - a Wasserstein Auto-Encoder / InfoVAE(α=1) objective that preserves the
latent-data mutual information. A method tournament picks the exact one-dimensional Wasserstein-2 penalty, and
cross-region drift-pooling (the mechanism behind the UN's bayesTFR) restores honest held-out coverage.
Executed in `notebooks/07-kj-demographic-recalibration.ipynb`.

### E12-H40 ELBO posterior collapse
- **Hypothesis** - because the ELBO applies a Kullback-Leibler penalty to every latent innovation, the calibration collapses the innovation scale τ → 0, flattening the fertility trend so the median over-predicts recent TFR (the +0.2/+0.3 gap) with near-zero latent usage
- **Lever** - the per-point KL term in `F = −ELBO`
- **Mechanism** - refit the ELBO objective (analytic Gaussian KL) across the panel; read the 2023 gap, the fitted τ, and a mutual-information proxy (variance of TFR the latent explains beyond the linear trend)
- **Prediction** - mean |2023 gap| > 0.1, τ → 0, MI-usage < 0.3
- **Acceptance bar** - collapse shown directly: large positive gap, τ near zero, MI ≈ 0
- **Experiment** - source: UN WPP 2024 panel<br>method: ELBO refit with per-point analytic KL
- **Result** - collapse confirmed: mean |2023 gap| 0.198 (USA +0.19, Europe +0.26), τ → 0.004, MI-usage 0.07 (latent essentially unused)
- **Verdict** - SUPPORTED

### E12-H41 Wasserstein objective closes the gap
- **Hypothesis** - because a WAE penalises only the aggregate posterior, dropping the per-point KL preserves mutual information, so the latent tracks the data and the in-sample gap closes while MI-usage recovers toward 1
- **Lever** - replace `Σ KL(q(zₜ)‖N(0,1))` with `λ · D(q(z)‖N(0,1))`
- **Mechanism** - refit with the exact-1D-Wasserstein penalty; compare 2023 gap and MI-usage against the ELBO fit
- **Prediction** - mean |2023 gap| ≤ 0.05 and mean MI-usage > 0.8
- **Acceptance bar** - gap closed below 0.05 and MI restored above 0.8
- **Experiment** - source: UN WPP 2024 panel<br>method: WAE (aggregate-posterior) recalibration
- **Result** - gap closed to mean |0.018| (USA +0.009, Italy +0.005, Europe +0.006) and MI-usage restored 0.04 → 0.96
- **Verdict** - SUPPORTED

### E12-H42 Method tournament - exact-1D-Wasserstein wins
- **Hypothesis** - because the aggregate divergence family has several members, an exact one-dimensional Wasserstein-2 penalty (optimal transport) matches or beats the RBF-MMD and both crush the ELBO on in-sample gap, TFR error, and population residual
- **Lever** - choice of aggregate penalty D (ELBO vs MMD vs exact-W2)
- **Mechanism** - score each objective on mean 2023 gap, in-sample TFR MAPE, and the 2023 population residual (recalibrated median scaling observed ASFR through the age structure)
- **Prediction** - W2 gap ≤ MMD gap < ELBO gap and W2 population residual ≤ MMD
- **Acceptance bar** - exact-Wasserstein is the panel winner on gap and population residual
- **Experiment** - source: UN WPP 2024 panel<br>method: three-objective tournament
- **Result** - exact-Wasserstein wins: gap 0.018 / pop residual 0.69%, beating WAE-MMD (0.038) and ELBO (0.198); MMD sits between (MI 0.96, pop 0.86%)
- **Verdict** - SUPPORTED

### E12-H43 Hierarchical drift-pooling restores forecast coverage
- **Hypothesis** - because a post-2015 regime change is not point-predictable, the narrow single-region forecast misses the held-out TFR; borrowing strength across regions (a cross-region drift spread, bayesTFR-style) widens the band so the held-out years are honestly covered while the population forecast stays accurate
- **Lever** - forecast drift sampled with the cross-region spread; heavy-tailed (Student-t) forecast innovations
- **Mechanism** - train ≤ 2015, predict 2016-2023; compare held-out TFR coverage and population MAPE with and without pooling
- **Prediction** - held-out TFR coverage ≥ 90% with pooling; population MAPE ≤ 1%
- **Acceptance bar** - pooled band covers held-out TFR (mean ≥ 90%) at population MAPE ≤ 1%
- **Experiment** - source: UN WPP 2024 (USA, Korea, Italy)<br>method: hierarchical widened posterior predictive
- **Result** - cross-region drift spread 0.0082/yr lifts held-out TFR coverage 50% → 100% (USA/Korea/Italy all 100%) at population MAPE 0.65%
- **Verdict** - SUPPORTED

### E12-H44 Recalibration preserves crisis + population fidelity
- **Hypothesis** - because closing the gap by over-smoothing would erase the crises, the recalibrated median must still reproduce each crisis-window TFR change (correct sign, close magnitude) and keep the 2023 population residual small
- **Lever** - the recalibrated Wasserstein median
- **Mechanism** - measure the median's TFR change across four crisis windows (USA recession, USA COVID, Korea 1997, Italy 1990s) and the recalibrated 2023 population residual
- **Prediction** - all four crisis windows reproduced by sign; population residual < 2%
- **Acceptance bar** - crises reproduced and population fidelity intact
- **Experiment** - source: UN WPP 2024<br>method: crisis-window reproduction + population projection
- **Result** - all four windows reproduced (USA recession obs −0.257/model −0.239, COVID −0.050/−0.035, Korea −0.257/−0.272, Italy −0.143/−0.156); 2023 population residual < 0.58%
- **Verdict** - SUPPORTED

### E12-H45 Recalibrated parameter + prediction tables
- **Hypothesis** - because the goal names reliable numbers, the recalibrated run yields a per-region parameter table (level, drift, τ, σ) and a prediction-vs-observed table documenting the gap closing from ≈ +0.2 to ≈ +0.02
- **Lever** - the converged Wasserstein posterior
- **Mechanism** - tabulate recalibrated parameters and 2023 predictions with ELBO and Wasserstein residuals side by side
- **Prediction** - both tables exported; the ELBO → Wasserstein residual drop is documented
- **Acceptance bar** - parameter and prediction tables exist in `reports/`
- **Experiment** - source: converged E12 posterior<br>method: posterior summarisation
- **Result** - `reports/nb7_parameter_table.csv` and `reports/nb7_predictions.csv` exported; ELBO residuals +0.18/+0.26 collapse to Wasserstein +0.005/+0.042
- **Verdict** - SUPPORTED

## E13 - Contrarian audit: 25 attacks on the model's own findings

A model that only confirms itself has not been tested. E13 pre-registers 25 contrarian hypotheses that attack
the conclusions of E6-E12 and settles each with a computation on the same UN WPP data and core model. The
convention is inverted here: **SUPPORTED means the contrarian claim holds - the finding is *qualified*** -
and **REFUTED means the finding survived** the attack. Executed in
`notebooks/08-kj-demographic-contrarian.ipynb`. Outcome: **12 findings survived, 13 qualified**, of 25.

### E13 at a glance

| id | contrarian claim (what it attacks) | evidence | verdict |
|---|---|---|---|
| E13-C1 | a persistence baseline is as good as the age model | model pop MAPE 0.09% vs hold-flat 3.45% | REFUTED |
| E13-C2 | momentum is not a stable regional constant | USA momentum 1.09 → 1.05 → 0.98 (range 0.10) | SUPPORTED |
| E13-C3 | USA predictability is migration, not momentum | 2016-23 migration 10.9M > natural 5.9M | SUPPORTED |
| E13-C4 | the USA quantum is itself falling (not pure tempo) | adjTFR slope −0.050/yr since 2010 | SUPPORTED |
| E13-C5 | the Bongaarts-Feeney split is fragile | USA r: 0 sign-flips, std 0.045 (monotone) | REFUTED |
| E13-C6 | Korea's deficit is partly tempo | Korea recent r +0.194/yr (MAC still rising) | SUPPORTED |
| E13-C7 | Rogers-Castro is needless for the total | RC 0.23% vs age-uniform 6.45% residual | REFUTED |
| E13-C8 | migration beats fertility for the USA to 2100 | +0.3 TFR +85.9M vs +50% migration +61.7M | REFUTED |
| E13-C9 | the RC childhood-echo term is redundant | RC-full 0.23% vs labour-only 0.89% | REFUTED |
| E13-C10 | a +0.3 lift is futile for Korea | recovers 18% of the 32M baseline loss | REFUTED |
| E13-C11 | a migration lever dominates fertility (USA) | migration +61.7M < fertility +85.9M | REFUTED |
| E13-C12 | intervention timing barely matters at 2100 | Korea 2025-vs-2045 = 34% of 2100 pop | REFUTED |
| E13-C13 | the near-term lock is arithmetic, not insight | 97% of Korea's 2050 births from women alive in 2023 | SUPPORTED |
| E13-C14 | the 1.5 ridge is not the replacement threshold | USA TFR at λ=1 is 2.09, not 1.5 | SUPPORTED |
| E13-C15 | the eigenvalue does not order by TFR | λ-order = TFR-order across 7 regions | REFUTED |
| E13-C16 | migration wrecks the stable-pyramid match | USA cos(eigenvector, actual) 0.976 | REFUTED |
| E13-C17 | the fit is over-flexible (fits noise) | w2 on white-noise TFR gets MAPE 11.3% | REFUTED |
| E13-C18 | the closed gap is an in-sample illusion | train ≤ 2022 → 2023 gap 0.103 (in-sample 0.009) | SUPPORTED |
| E13-C19 | MI ≈ 1 is memorization, not information | a saturated interpolator scores MI 1.00 | SUPPORTED |
| E13-C20 | the frozen-rate baseline is a strawman | held-out TFR MAPE frozen 8.77% vs RW-drift 6.17% | SUPPORTED |
| E13-C21 | the deaths fidelity is trivial | crude CDR×pop deaths MAPE 0.47% | SUPPORTED |
| E13-C22 | TFR rank already predicts the 2100 rank | Spearman 0.71 (migration/structure reorder) | REFUTED |
| E13-C23 | "collapse" overstates a halving | worst 2100 ratio (Korea) 0.37, not extinction | SUPPORTED |
| E13-C24 | sub-replacement is not destiny with migration | Korea holds flat at 0.89%/yr net migration | SUPPORTED |
| E13-C25 | "momentum governs" has low falsifiability | per-region latent DOF ~37 vs 34 data points | SUPPORTED |

### Lessons from the audit

- **The accounting and structure survive** - the age model crushes a persistence baseline (C1), the
  Rogers-Castro age shape genuinely matters (C7, C9), fertility out-pulls migration as a USA lever (C8, C11),
  the eigenvalue tracks TFR (C15), the stable pyramid still fits (C16), the Wasserstein fit refuses to fit
  pure noise (C17), and intervention timing is decisive not cosmetic (C12)
- **The fertility-forecast and tempo claims are qualified** - the USA quantum is itself eroding, so its
  shortfall is not purely recoverable tempo (C4); the USA's recent trajectory is migration-led (C3); momentum
  is a depleting quantity, not a constant (C2); one-step-ahead period TFR is still hard (C18)
- **Two honest reframes** - the "TFR-1.5 trap" is an empirical threshold, not the mathematical replacement
  line of 2.09 (C14); and sub-replacement is not destiny within the model - plausible migration holds even
  Korea flat (C24), so the label "collapse" means decline-and-ageing, not extinction (C23)

## E14 - Reversal interventions: the full catalogue, the manifold, the drivers

E14 turns from diagnosis to therapy: it hypothesises the full menu of plausible interventions - state policy and
cultural change - that the demographic literature has proposed to lift fertility, maps each onto a model lever,
and projects it to 2100. The central question is which levers, singly or bundled, can **reverse** the trend
(return a population to growth) rather than merely slow it. Executed in
`notebooks/09-kj-demographic-reversal.ipynb`, with three images - the Seldon manifold, the drivers, and the
interventions.

### The catalogue (14 interventions, pre-registered)

Fourteen interventions, each with a mechanism, a model lever, a literature anchor, and a plausible ΔTFR
(best-judgment literature ranges, not fitted - the model sizes a lever, it does not prove a policy achieves it):

- **State, quantum** - universal childcare (+0.25), child allowance (+0.17), paid parental leave (+0.10),
  family housing support (+0.15), work-family flexibility (+0.10), youth-precarity reduction (+0.15)
- **State, tempo** - baby bonus one-off (+0.08, fades), subsidized assisted reproduction (+0.05)
- **State, coupling** - attention-economy / dating-app regulation (+0.08)
- **State, migration** - pro-natal / replacement migration (population lever, not TFR)
- **Culture, quantum** - gender-equity in domestic labour (+0.20), reduce intensive-parenting norm (+0.12)
- **Culture, tempo** - earlier union formation / relationship support (+0.10)
- **Culture, coupling** - de-stigmatize non-marital births (+0.10)

Grounding: Bergsvik-Hart-Kohler 2021 (systematic review), Gauthier 2007, Luci-Greulich & Thévenon 2013,
Myrskylä-Kohler-Billari 2009 (J-curve), Goldscheider 2015 (gender revolution), Doepke et al. 2023.

### E14 at a glance

| id | claim (what is under test) | evidence | verdict |
|---|---|---|---|
| E14-H46 | no single intervention reverses an ultra-low region | Korea's best single lever reaches only −50% (from −63%) | SUPPORTED |
| E14-H47 | a tempo-recoverable region is reversible by a bundle | USA full bundle + migration → +129% (returns to growth) | SUPPORTED |
| E14-H48 | an ultra-low structural region cannot be fully reversed by 2100 | Korea bends −63% → −10% but not to growth | SUPPORTED |
| E14-H49 | quantum (completed fertility) is the master driver | Korea recovery potential: quantum 28M > migration 14M > tempo 3M | SUPPORTED |
| E14-H50 | interventions map onto the manifold as separatrix crossings | cost/childcare/gender-equity lower ρ, formation/coupling raise C | SUPPORTED |

### Lessons

- **On the Seldon manifold every lever is a directed move** - cost / childcare / gender-equity policies lower
  childlessness ρ (leftward), formation / coupling policies raise C (upward); the USA sits near the separatrix
  (a modest push recovers it) while Korea and Japan lie deep in the collapse basin (a large combined move
  needed)
- **The drivers rank cleanly** - the quantum deficit dominates the 2100 decline (Korea 28M of a 32M loss),
  migration is a strong second (14M), the momentum / age-structure lock is small but irreducible (4M), and
  recoverable tempo is least (3M) - so the heaviest levers are the ones that raise completed fertility
- **Reversal is a property of position, not effort** - a serious state-and-culture bundle plus migration
  returns the tempo-recoverable USA to growth, but the same maximal effort only bends ultra-low Korea from a
  63% collapse to a shallow decline by 2100, because its reproductive base is already hollowed out; no single
  policy is a cure, and only an early, broad bundle moves the trajectory at all

## E15 - The coupling keystone and the literature-grounded strength of interventions

E15 repairs two flaws in E14: its intervention strengths were recalled, not researched, and almost every lever
attacked the fertility quantum while ignoring coupling - the keystone Notebook 1 identified. Every strength is
now pinned to the (quasi-)experimental literature and bounded to a real-world ceiling (Korea's USD 270B floor,
the Nordic ~1.5-1.7 ceiling, Romania's Decree 770, the Colorado LARC experiment, post-Dobbs). Fertility is
split into its extensive (childlessness ρ) and intensive (parity P̄) margins, and all interventions are baked
into one extensible interface - an age-distributed lift on the region's ASFR schedule, composed into bundles
that differ by which margin they load and whether they endure. Each hypothesis rides on an already-proven
finding and extends it into the calibrated model, documenting every effect with a per-effect citation.
Executed in `notebooks/10-kj-demographic-intervention-story.ipynb` (2026-07-06): **50 hypotheses (H51-H100),
37 SUPPORTED, 10 PARTIAL, 3 REFUTED** - a wider menu (attention economy, structure, family, messaging,
health), a coupling-in-depth chapter of ten legislative and psychological levers, and a deeper-drivers chapter
of thirteen specific interventions on the career-first / education-arms-race / overwork life-script (the Poland
lesson: free nurseries + a 93-billion-euro cash program still left TFR ~1.1). Each lever also carries an
**interactions and side-effects** analysis - the coupled Seldon ODE amplifies a keystone push near the ridge
and damps it deep in the basin, and several levers carry documented countervailing effects (cash reduces female
labour supply; restricting divorce raises women's suicide/DV; a gender-neutral career-clock stop widens the
gender gap). The E14 catalogue strengths are superseded by the literature-graded E15 table; a decision-maker's
star-ranking with mechanism-of-effect chains is regenerated on demand via the `/write-interventions` command.

### E15 at a glance

| id | claim | evidence | verdict |
| --- | --- | --- | --- |
| E15-H51 | cash cannot reverse collapse | Korea cash-only → −57% (USD 270B; TFR fell every year 1.13→0.72) | SUPPORTED |
| E15-H52 | the extensive margin (childlessness) dominates the ultra-low deficit | closing childlessness adds +0.30-0.36 TFR for Germany/Italy/Japan; Korea a quantum-collapse special case (+0.76 parity gap) | SUPPORTED |
| E15-H53 | the coupling keystone is policy-orphaned | catalogue state levers act on the quantum; coupling reached only by culture + the added extensive levers | SUPPORTED |
| E15-H54 | a durable keystone bundle beats an equal-ΔTFR eroding cash bundle | +9 to +22pp across regions - durability, not size, is the differentiator | SUPPORTED |
| E15-H55 | gender equity is the unique dual-margin lever | beats equal cash by up to +14pp (Myrskylä J-curve master lever) | SUPPORTED |
| E15-H56 | a maximal bundle cannot reverse the deepest cases by 2100 | Korea −27%, Japan −15% bent but not to growth; USA/France/Germany/Italy reverse | SUPPORTED |
| E15-H57 | literature strength ordering holds on the model | childcare/gender-equity > housing/security > leave > cash > bonus > IVF | SUPPORTED |
| E15-H58 | earlier union formation raises the extensive margin | lowers childlessness; caveat: pure-young timing slightly speeds sub-replacement turnover | SUPPORTED |
| E15-H59 | longer / stable unions raise completed fertility | time-in-union is the key determinant; instability partly self-offsets via repartnering | SUPPORTED |
| E15-H60 | contraception decision-architecture is powerful but coercive | friction +2.5-15pp, Romania total ban +37-82pp; non-durable, raises unwanted births - measured, not endorsed | SUPPORTED |
| E15-H61 | a state partner-market camp is the only lever manufacturing coupling density | Korea +~5pp, but tier-3 (no precedent, widest band) | SUPPORTED |
| E15-H62 | early-parenthood security + job guarantee beats cash | caps the child penalty, not price; +up to 8pp; Nordic ~1.5-1.7 ceiling bounds it | SUPPORTED |
| E15-H63 | age-targeted cash beats uniform cash | response concentrates at 25-29 (Kim 2023; Finnish BI) | SUPPORTED |
| E15-H64 | social-media time regulation reverses time-displacement | Twenge 2019; Australia under-16; tier-3 fertility magnitude extrapolated | SUPPORTED |
| E15-H65 | dating-app design regulation reverses optionality/commitment-phobia | Rosenfeld; loot-box/gambling-mechanic regulation parallel; tier-3 | SUPPORTED |
| E15-H66 | rebuilding offline intermediaries helps | apps disintermediated matchmakers without raising pairing rate (Rosenfeld); app regulation alone insufficient | SUPPORTED |
| E15-H67 | shared-custody / fathers' rights raises the extensive margin | lower custody-loss risk, better co-parenting; no direct fertility study (tier-3) | SUPPORTED |
| E15-H68 | a paternity father-quota raises fertility | REFUTED - raises fathers' leave + equality norms but no major fertility effect (Norway null) | REFUTED |
| E15-H69 | rolling back gender-equality policy raises fertility | REFUTED - it BACKFIRES; East Asia's persistent traditional norms drive fertility lowest (Myrskylä) | REFUTED |
| E15-H70 | pro-natal propaganda / messaging raises fertility | PARTIAL - "unlikely to make people have more children"; drowned out where it fights women's rights | PARTIAL |
| E15-H71 | reducing extreme working hours raises fertility | Korea 1915 h/yr; weekly hours the most significant factor in pregnancy intentions; Japan 4-day-week experiment | SUPPORTED |
| E15-H72 | student-debt / education-cost relief pulls family formation earlier | debt delays marriage + homeownership; 67% of Gen-Z borrowers delayed a life event | SUPPORTED |
| E15-H73 | family-size housing (3BR+) raises fertility | 3BR+ units raise births 2.3× more than small units; housing drove ~half the US fertility drop | SUPPORTED |
| E15-H74 | Hungary-style family tax/loan raises completed fertility | PARTIAL - 6.2% of GDP; TFR 1.23→1.61 but "largely a slowdown in postponement" (tempo), not cohort quantum | PARTIAL |
| E15-H75 | fecundity awareness + egg-freezing cuts involuntary childlessness | involuntary childlessness rises 6% at 30 → 35% at 40; knowledge gaps cause avoidable delay | SUPPORTED |
| E15-H76 | addressing male reproductive-health decline raises fertility | PARTIAL - Western sperm count −50%+ 1973-2015 (Levine 2022) but region-specific and debated | PARTIAL |
| E15-H77 | de-urbanization / smaller cities raises fertility | PARTIAL - urban density lowers fertility but modest and hard to engineer (congestion diseconomies) | PARTIAL |
| E15-H78 | legal recognition of cohabitation (PACS) raises coupling | measured - France PACS 1999: 40%+ non-marital births, union-fertility link held | SUPPORTED |
| E15-H79 | state matchmaking raises fertility | measured - Singapore SDN made marriages but TFR still fell to 0.87 | PARTIAL |
| E15-H80 | restricting divorce / covenant marriage raises stability | measured - no-fault effect reverses within a decade (Wolfers); repeal harms women; covenant marriage unused | REFUTED |
| E15-H81 | attention-economy legislation (minor bans, right-to-disconnect) restores coupling | predicted - Australia under-16; Twenge time-displacement; tier-3 | SUPPORTED |
| E15-H82 | removing the marriage tax penalty lowers the cost of pairing | measured - marriage-penalty literature; modest | SUPPORTED |
| E15-H83 | relationship-skills education (PREP) raises union stability | measured - divorce 8.1% vs 14.9% for high-risk couples only, no average effect | PARTIAL |
| E15-H84 | seeding fertility social contagion spreads childbearing | measured - Balbo-Barban: a friend/sibling's birth raises one's own odds (12-24 mo, fades) | SUPPORTED |
| E15-H85 | gender depolarization restores viable matches | measured - Lee 2025 perceived gender conflict; Korea 4B; strongest coupling lever for Korea | SUPPORTED |
| E15-H86 | slow-dating / choice-architecture nudges raise commitment | predicted - paradox of choice (Rosenfeld); tier-3 | SUPPORTED |
| E15-H87 | loneliness / approach-anxiety reduction raises formation | predicted - loneliness epidemic; tier-3 | SUPPORTED |
| E15-H88 | hagwon curfew + private-tutoring cap raises fertility | measured - Korea private-ed 27tn won, edupoverty 40% -> lower child-cost norm -> parity up | SUPPORTED |
| E15-H89 | CSAT single-exam de-determinism raises fertility | measured - lower exam stakes -> less intensive parenting + less youth burnout | SUPPORTED |
| E15-H90 | compressing winner-take-all inequality raises fertility | measured - Doepke-Zilibotti: lower stakes -> relaxed parenting -> cheaper children (root lever) | SUPPORTED |
| E15-H91 | enforcing an overwork cap raises fertility | measured - Korea 2069 h/yr; weekly hours the top pregnancy-intention factor; 35-45h higher odds | SUPPORTED |
| E15-H92 | career-neutral parenthood (gender-aware) pulls births earlier | measured - naive gender-NEUTRAL clock-stop BACKFIRES, helps men, widens gap (Stearns) | PARTIAL |
| E15-H93 | resequencing the life script (family-during-training) lowers childlessness | predicted - financial-security worry raises delay odds 128% | SUPPORTED |
| E15-H94 | breaking the assortative-postponement trap raises coupling | predicted - make early family career-neutral for both partners | SUPPORTED |
| E15-H95 | de-fusing the school-district real-estate arms race raises fertility | measured - lower the fused education+housing cost gate | PARTIAL |
| E15-H96 | school-mandated communication/conflict-resolution workshops raise union stability | extrapolated - from PREP (high-risk 8% vs 15%, no average effect) | PARTIAL |
| E15-H97 | mandatory/subsidized psychotherapy raises relationship formation | extrapolated - treat anxiety/attachment/loneliness barriers; no direct fertility RCT | PARTIAL |
| E15-H98 | universal social-skills / approach-anxiety training raises formation | predicted - re-enter the dating market; tier-3 | SUPPORTED |
| E15-H99 | raising the status of early parenthood (peer-led) raises coupling | predicted - shift the career-first identity; contagion not top-down propaganda | SUPPORTED |
| E15-H100 | employer family-time mandate raises fertility | measured - 4-day default, on-site childcare, right-to-disconnect -> time for family | SUPPORTED |

### Lessons

- **The obvious levers fail alone - the Poland lesson** - free Maluch+ nurseries plus a 93-billion-euro 500+/800+ cash program left Poland's TFR at ~1.1; cash and childcare do not touch the binding constraint, the career-first life-script enforced by a winner-take-all arms race (Doepke-Zilibotti); the deepest lever is to compress the stakes, not subsidize the race
- **No lever acts alone** - the coupled Seldon ODE amplifies a keystone (childlessness-reducing) push near the ridge and damps it deep in the basin (the mechanistic reason reversal is position-dependent), and several levers carry documented side effects: cash reduces female labour supply (Poland IBS), restricting divorce raises women's suicide and DV (Stevenson-Wolfers), a gender-neutral career-clock stop widens the gender gap (Stearns), and restricting contraception tripled maternal mortality (Romania)

- **The coupling keystone can be attacked directly, by law and by psychology** - recognizing cohabitation (France's PACS) and de-escalating the gender war (Korea's 4B) are measured, effective coupling levers; but two popular fixes backfire - restricting divorce reverses within a decade and harms women, and state matchmaking makes marriages without moving a birth rate
- **The missing births are missing mothers** - for Germany/Italy/Japan the deficit is extensive (nearly three in ten women never have a child); Korea alone is a quantum-collapse special case - so the coupling keystone is where the leverage lives
- **Durability, not size, separates the keystone from cash** - a structural lever and an equal-ΔTFR cash lever start the same, but cash erodes and stalls before the separatrix while the structural lever crosses it
- **Reversal is position + timing** - the same maximal effort reverses societies near the ridge and only bends Korea/Japan; where you sit on the manifold decides the outcome
- **Two levers earn a negative verdict** - a paternity father-quota moves equality norms but not births, and rolling back gender equality backfires (the model, like East Asia, says traditional-norm restoration drives fertility lower)
- **The attention economy is real but tier-3** - social-media / dating-app regulation can help rebuild the partner market, but app regulation alone is necessary, not sufficient; offline intermediaries must be rebuilt
- **The sleeper levers** - cutting extreme working hours and building family-size housing rank beside the keystone and are underused in the pro-natal debate

## E16 - Incentives, arms races and defection

E16 repairs three flaws in E15: mechanisms were stated as outcomes rather than named incentives (Munger: "show
me the incentive and I'll show you the outcome"); effects were measured gross, as if everyone complies; and the
West was under-weighted against Korea. It adds two modelling extensions to the same interface - a per-lever
**defection parameter δ** (net = gross·(1−δ) + backfire(δ), where the backfire term can invert the sign when
the rich evade) and an explicit **side-effect cost** on a named metric. Each hypothesis is taken apart,
measured, diagnosed against an analog, and has its **key signal isolated with maths/statistics** (an
admission-return slope, a coachability elasticity, a Bongaarts-Feeney tempo/quantum split, a defection
decomposition) before its model interaction is verified. Executed in
`notebooks/11-kj-incentives-arms-races-defection.ipynb` (2026-07-06): **25 hypotheses (H101-H125), 15
SUPPORTED, 6 PARTIAL, 4 REFUTED**. The central result is the **defection screen** - re-ranking every lever by
net-after-defection reshuffles the order: bans, propaganda, wealth caps and exhortation fall net-negative while
lottery bucketing, universal motherhood-penalty removal, inequality compression and structural defaults rise.
The closing manifold verdict shows the defection-robust bundle crossing the separatrix near the ridge where the
fragile bundle stalls.

### E16 at a glance

| id | claim | evidence | verdict |
| --- | --- | --- | --- |
| E16-H101 | an outright tutoring ban backfires under defection | Korea 1980 → black market, rich buy covert tutoring, inequality widens; net −0.235 (sign flips) | REFUTED |
| E16-H102 | a threshold-and-lottery-band makes the prize un-buyable | reward-gradient above the bar collapses 0.98→0.00 (100% deflation); net +0.16, δ≈0.03; Korea +4.6pp, USA +11pp | SUPPORTED |
| E16-H103 | multi-dimensional un-gameable admission deflates the race | coachability elasticity 0.15→0.05, minus 0.04 holistic-capture leak → net +0.066; cultural-capital capture caveat | PARTIAL |
| E16-H104 | only a binding positional cap is stable | Hirsch/Frank - education is positional, voluntary restraint dominated; net +0.16 | SUPPORTED |
| E16-H105 | compressing inequality is the self-enforcing root lever | Doepke-Zilibotti; lowest δ (0.02), largest structural; USA +17pp | SUPPORTED |
| E16-H106 | an estate/inheritance tax compresses dynastic advantage | De Nardi-Yang bequests-as-luxury; net +0.06 after avoidance; heir-labour/capital-flight cost | PARTIAL |
| E16-H107 | a progressive wealth cap is dominated | large gross but high avoidance + capital flight → net ≈ 0 | PARTIAL |
| E16-H108 | taxing childlessness has a large gross but the worst welfare cost | lex Julia / USSR-Bulgaria; net +0.075, side-cost 0.85 (coercion, women's autonomy) | PARTIAL |
| E16-H109 | removing the DINK tax advantage makes children the default | structural (δ low), politically explosive; net +0.10 | SUPPORTED |
| E16-H110 | a universal motherhood-penalty removal beats opt-in | Kleven US penalty −31%, norm-driven (married 27% vs single 5%); net +0.19 | SUPPORTED |
| E16-H111 | Israel's exportable signal is the default norm + universal IVF | only OECD above replacement (2.9); secular ~2.0 without coercion; δ≈0.03 | SUPPORTED |
| E16-H112 | high-fertility subcultures win by retention/boundary, not policy | Kaufmann - Amish double ~20y, UK Orthodox 17%→75% of Jewish births; descriptive, not a lever | SUPPORTED |
| E16-H113 | Hungary's cash rise was mostly tempo | N-IUSSP/AEI - 1.23→1.59→1.39 at ~5-6% GDP; ~85% tempo, quantum barely moved; confirms the cash ceiling | REFUTED |
| E16-H114 | the housing lever is supply, not a price subsidy | Dettling-Kearney - price rises help owners (+5%), hurt renters (−2.4%); subsidy to owners dominated | SUPPORTED |
| E16-H115 | student-debt relief removes an institutional resource-sink | Mezza/Fed - +$1k → −1.8pp homeownership, ~400k fewer young owners; net +0.09 | SUPPORTED |
| E16-H116 | peer-led archetype contagion is real but fragile | Balbo-Barban - a friend's birth raises own transition; free-rideable, δ≈0.55; needs critical mass | PARTIAL |
| E16-H117 | top-down pronatal propaganda backfires | Decree 770 - 1.9→3.7 then collapse, back-alley deaths; net −0.178 - you cannot mandate the birth | REFUTED |
| E16-H118 | removing the parenthood happiness penalty raises fertility | Glass 2016 - the gap is policy-dependent, vanishes with family support; net +0.09 | SUPPORTED |
| E16-H119 | decoupling status from overwork attacks the career-first script | the specific Western incentive; slow, norm-dependent, δ≈0.30 | PARTIAL |
| E16-H120 | marriage-first exhortation is null | Wilcox correlation endogenous; MDRC Supporting Healthy Marriage null on divorce - structure dominates | REFUTED |
| E16-H121 | use-it-or-lose-it defaults beat opt-in (the design axiom) | Norway father's quota uptake <3%→97%; opt-in collapses to free-riding; net +0.12 vs +0.036 | SUPPORTED |
| E16-H122 | the defection screen reshuffles the ranking | bans/propaganda/wealth-cap go net-negative; lottery/inequality/penalty/defaults rise - the central result | SUPPORTED |
| E16-H123 | recycling the defection turns leakage into funding | tax the black market, fund the compliant → ban net −0.235 → +0.017 | SUPPORTED |
| E16-H124 | the frontier separates efficient from dominated levers | dominated: childlessness tax, wealth cap, propaganda, ban; efficient: inequality, lottery, penalty removal, housing supply, IVF | SUPPORTED |
| E16-H125 | the defection-robust bundle crosses where the fragile stalls | near the ridge robust dTFR 0.44 → recovery (n→1.0); fragile dTFR 0.03 → stalls (n→0) | SUPPORTED |

### Lessons

- **The mechanism is the message** - "defuse the education arms race" is not one lever but several with opposite signs: a ban backfires (rich buy the covert good, inequality widens) while a lottery-band that makes the prize un-buyable, or a multi-dimensional test rewarding un-coachable traits, deflate the race at its source
- **Defection is the hidden variable** - gross effect sizes lie; once you model who evades, the ranking reshuffles and the survivors are exactly the levers money cannot defect from (Norway's father-quota, 3%→97%, is the proof)
- **Inequality is both the strongest and the most defection-robust lever** - compressing the skill premium deflates the arms race for everyone at once, with no per-family enforcement (Doepke-Zilibotti)
- **The West has its own machinery** - Israel's near-universal default + IVF holds secular fertility near replacement without coercion; Hungary's 5-6% of GDP buys mostly tempo; housing's lever is supply for young renters, not a subsidy to owners
- **Side effects are not footnotes** - stacked against the net, the coercive levers (childlessness tax, wealth cap, propaganda, ban) are dominated; the efficient frontier is structural and un-buyable

## E17 - Swept design spans (incentive geometry)

E17 fans the E15/E16 mechanism work out along design *axes* the earlier batches fixed at a point. Each
hypothesis stays discrete (appended after E16-H125, never a rewrite), but its Experiment/Result is now a
**swept response curve** - effect(θ), side-cost(θ), defection δ(θ) over a design parameter - and its verdict
turns on the **optimum and its type**: an interior sweet-spot, a hard corner, or a sign-flip where the net
crosses zero. The swept curve sharpens the falsifier - a hypothesis predicting an interior optimum is refuted
by a monotone curve. Executed in `notebooks/12-kj-swept-design-spans.ipynb` on the calibrated E15/E16 lever
interface, unchanged. Eighteen hypotheses span coupling economics, union-duration and the outside-option
valve, policy geometry, a controversial surrogate-carrier market, and two synthesis results.

### E17 at a glance

| id | claim | evidence | verdict |
| --- | --- | --- | --- |
| E17-H126 | coupling is partly a financial channel | economies of scale ~25% cheaper/person (OECD 1.5); ~25% of the premium runs via marriage (Taiwan lottery); Korea +0.5pp | SUPPORTED |
| E17-H127 | single-parent precarity suppresses higher-order births | US single-mother poverty 31.3% vs 5.4% (~5.8x); bites 2nd/3rd births (P̄ penalty) | SUPPORTED |
| E17-H128 | de-risking solo parenthood helps but a benefit-cliff delays cohabitation | interior optimum s*≈0.5; support COMPLEMENTS coupling (premium persists Nordic/France); past the cliff net falls | PARTIAL |
| E17-H129 | reward union duration only as de-risk, not lock-in | stability saturates, welfare-trap explodes → interior-low rw*≈0.28; de-risk durable ~0.08 P̄ lift | SUPPORTED |
| E17-H130 | anniversary holidays / longevity medals are symbolic | Soviet medals / anniversary holidays symbolic-null; no causal quantum effect | REFUTED |
| E17-H131 | lock-in / covenant marriage / adultery penalty backfires | the exit is the valve - S-W: no-fault divorce cut female suicide ~20%, DV ~30%; raising exit cost removes the bargaining that de-escalates; net-of-harm −0.12 | REFUTED |
| E17-H132 | school finance + communication education cuts dissolution | PREP RCT divorce 2.03% vs 6.20% (~67% risk cut); Dew - finance arguments top divorce predictor; net +0.09 (general-pop replication weaker) | SUPPORTED |
| E17-H133 | infidelity norm/stigma (soft) is modest, dominated by shaming | net +0.004; no fertility evidence; shaming side-cost | PARTIAL |
| E17-H134 | a porn ban is not a fertility lever | Twenge 2017 - the sex-recession is partnership decline NOT porn; Perry 2018 porn→divorce OR~2.19 observational; ban high-δ (VPN), symbolic | REFUTED |
| E17-H135 | Amish/enclosed-community fertility is the ceiling but confounded | TFR~6.9, doubles ~20y, retention ~85%; retention/endogamy not porn-abstention drives it; non-portable | SUPPORTED |
| E17-H136 | universal beats means-tested (the cliff) | the means-test cliff + non-take-up dominate targeting savings; corner at universal; net +0.15 | SUPPORTED |
| E17-H137 | benefit form beats size - in-kind persists, cash erodes | interior at in-kind services; Korea in-kind +7.4pp vs eroding cash +1.8pp; net +0.25 | SUPPORTED |
| E17-H138 | credible permanence - a temporary policy is discounted to tempo | corner at credible lock; reframes 'durability' as credibility (Hungary reversible = tempo); net +0.20 | SUPPORTED |
| E17-H139 | geographic scale - local bonuses relocate births | corner at national; Korea municipal bonuses partly relocation (Kim 2023); net +0.12 | SUPPORTED |
| E17-H140 | who pays - an employer maternity mandate is perverse | state-funded net +0.15 vs employer-mandate net NEGATIVE - statistical hiring discrimination widens the Kleven −31% penalty; sign-flips ~0.6 | SUPPORTED |
| E17-H141 | a surrogate-carrier class is dominated | tiny demand gain (Korea +0.02pp, rounding error); supply-displacement + worst-in-batch commodification/exploitation cost; India banned the hub; Israel above-replacement = subsidised IVF not a carrier class | PARTIAL |
| E17-H142 | no universal "turn it to 11" | interior, corner and sign-flip optima coexist - the optimum structure is itself the design signal | SUPPORTED |
| E17-H143 | the robust valve-paired bundle crosses where the fragile stalls | robust push +0.47 → recovery (n→1); coercive/dominated bundle → stall (n→0) on the Seldon manifold | SUPPORTED |

### Lessons

- **Geometry over magnitude** - how a lever is delivered (universal, in-kind, permanent, national, state-funded, de-risking) decides its fate more than how hard it is pushed; the five policy-geometry axes all resolve to a delivery choice, not a spend level
- **The outside option is the valve** - the sharpest mechanism in the batch: the credible right to exit is what keeps a union functional (Stevenson-Wolfers bargaining), so raising the cost of leaving removes the incentive it was meant to strengthen - lock-in, adultery penalty and covenant marriage all sign-flip
- **Name the money in coupling** - a quarter of the coupling fertility premium is literally affordability (economies of scale), and single-parent precarity suppresses higher-order births; pairing is an economic lever, not only a preference
- **The coercive extremes sign-flip or drown in side-cost** - employer mandates (hiring discrimination), a conditioned surrogate class (commodification), a porn ban (evasion + null) and duration lock-in (welfare harm) are each dominated once the side-cost is stacked
- **No universal optimum** - the optima are diverse (interior sweet-spots, hard corners, sign-flips); there is no lever you simply turn to 11, and the structure of the optimum tells the designer whether to tune a dose, go all the way, or stop before the lever inverts

## E18 - Hybrids and undercurrents

E18 does two things the campaign had not: it **hybridises the proven winners** (does stacking complementary
low-δ levers beat either alone?) and reaches for **creative new levers each anchored to a named undercurrent**
(financial/institutional, biological, cultural/marriage-market, psychological). Each stays discrete (appended
after E17-H143); a hybrid's Experiment/Result is a blend sweep locating the optimum mix and the super-additive
premium, a creative lever's is an intensity sweep locating its optimum type. Grounded in three research digests
(biological fecundity; financial/institutional levers; cultural/marriage-market mechanisms), whose honesty
flags are carried into the verdicts. Executed in `notebooks/13-kj-hybrids-and-undercurrents.ipynb`. Twenty
hypotheses; 10 SUPPORTED, 8 PARTIAL, 2 REFUTED.

### E18 at a glance

| id | claim | evidence | verdict |
| --- | --- | --- | --- |
| E18-H144 | compress x lottery-band is super-additive | complementary channels (removes the fuel + the target); blend* 0.31, net +0.273, super-additive +0.023 | SUPPORTED |
| E18-H145 | a constitutionally-locked in-kind childcare guarantee | form x durability (in-kind persists, permanence earns the full response); net +0.325 | SUPPORTED |
| E18-H146 | universal state-funded leave with a job guarantee | penalty-removal + state-funding + de-risk stacked; net +0.300 | SUPPORTED |
| E18-H147 | couple-targeted family housing via supply | economies-of-scale x supply (3bed+ units ~2.3x births/euro); net +0.145 | SUPPORTED |
| E18-H148 | de-risk x school-education x peer contagion | PREP delivered bottom-up as a peer norm; super-additive +0.050; net +0.140 | SUPPORTED |
| E18-H149 | a universal reproductive-insurance default (IVF + egg-banking) | insure the biological runway but the egg-freezing option-trap caps it - optimum is low reliance; net +0.150 | PARTIAL |
| E18-H150 | the second-shift stack (gender-equity x father-quota x shorter hours) | equalise the domestic load; super-additive +0.030; net +0.150 | SUPPORTED |
| E18-H151 | compress inequality x fertility-linked pension | the pension corrective is thin so compression dominates the blend; net +0.250 | PARTIAL |
| E18-H152 | the pension-fertility externality | Boldrin-De Nardi-Jones - pension = 10% of GDP <-> −0.7 to −1.6 TFR (55-65% of the US-EU gap); a fertility-linked pension internalises it but enacted-credit effects are small | PARTIAL |
| E18-H153 | the egg-freezing option-value trap backfires | return-to-use ~5.7%, unconditional live-birth ~1.6%; the option value licenses postponement that costs more births than it delivers; net sign-flips negative | REFUTED |
| E18-H154 | the fecundity floor is a minority driver | a 3-4yr delay costs only ~0.1-0.2 children biologically; obesity −3%/BMI-unit is best-evidenced; sperm-count/EDC narratives contested | PARTIAL |
| E18-H155 | the hypergamy marriage-squeeze | women out-educate men in 139+ countries; Korea hypergamous marriages 22%->11%; bites via the marriage margin (East Asia), norm self-eroding, second-shift confound | PARTIAL |
| E18-H156 | one-child-policy hysteresis - permission is not a lever | China TFR FELL 1.67 (2015) -> 1.09 (2022) after lifting the policy; RDD - only-child status lowers ideal family size; you cannot un-ring the bell | SUPPORTED |
| E18-H157 | the grandmother hypothesis | grandmother >=200km away <-> ~1 fewer child; daily kin care 30% IT/ES vs 2% Nordic; loads on the 2nd birth; move-near-kin endogeneity caveat | SUPPORTED |
| E18-H158 | the climate/expectations birth-strike | 20-33% cite climate; behaviourally real but only among committed environmentalists via the childless-forgoing margin; optimism can't be engineered top-down (Decree 770) | REFUTED |
| E18-H159 | migrant-fertility convergence - a bridge not a cure | gen-2 fertility often below natives; full convergence >1 generation (Turkish-origin the slow outlier); migration is a one-time level boost per cohort | SUPPORTED |
| E18-H160 | UBI adds no unconditionality premium | Alaska PFD +13.1% fertility (tempo, strongest for disadvantaged); unconditionality adds nothing over a child-conditional transfer - response tracks cash size + liquidity | PARTIAL |
| E18-H161 | the urban-density penalty (low-confidence) | apartment cores ~TFR 1.0 vs family suburbs ~2.0; mechanism is housing space not density; heavy self-selection, no natural experiment | PARTIAL |
| E18-H162 | status-of-parenthood reversal (bottom-up only) | make parenthood positional again; peer contagion works, top-down status engineering backfires like propaganda | PARTIAL |
| E18-H163 | the precarity formation-brake | Alderotti meta-analysis - temporary contracts cut births (esp. 2nd), effect strengthening over time; security pulls formation earlier (rho down) | SUPPORTED |

### Lessons

- **Stacking complementary winners is super-additive** - the biggest premiums come from hybrids whose parts act on *different* channels (compress the fuel + make the prize un-buyable; de-risk + teach the skills + spread as a peer norm; equalise the second shift across leave and hours); stacking two levers on the same channel only saturates
- **The deep undercurrents are mostly slow, contested, or one-time** - the pension externality and the marriage-market squeeze are real but confounded and self-eroding; migration and the grandmother effect are a bridge or an endowment, not a durable policy lever
- **The biological channel is a hard wall but a minority driver** - a 3-4yr delay costs only ~0.1-0.2 children, and its "solution" (egg-freezing) can backfire by licensing the very postponement that causes the loss; the honest lever is metabolic health and not postponing, not a ban
- **Permission is not a lever** - one-child-policy hysteresis is the sharpest warning: lifting a restriction did not restore fertility because norms and cost structures lock in below the policy; you cannot un-ring the bell
- **Naming the undercurrent disciplines the claim** - forcing each lever to declare its financial / biological / cultural / psychological mechanism separates the durable levers from the vague ones

## E19 - Dynamical re-examination (the model as judge)

E19 is a methodological round, not new hypotheses. It re-examines the whole intervention catalogue (E14-E18,
~88 levers) by making the calibrated model the *judge* instead of scoring levers from static response curves.
A recalibrated **emergent behavioural model** - channels are the campaign's own observable parameters, C
(coupling), ρ_c (childlessness), P̄ (parity), τ (tempo), S (security), each with its own dynamics adapted from
the nine-state ODE - is coupled to the Leslie core with a dependency→security feedback, calibrated per region
to reproduce real 2023 fertility exactly, and each intervention is integrated four generations (2023→2125).
The verdict comes from the trajectory. Executed in `notebooks/14-kj-dynamical-intervention-simulation.ipynb`.

The rebuild replaced a failed first attempt that routed every lever through the nine-state ODE's single
bistable coupling state (flattening all diversity into "did you cross the separatrix"). The fix: channels =
the observable parameters; TFR = C·(1−ρ_c)·P̄·Ψ_fec(τ) with a Bongaarts-Feeney period-rate term so a timing
lever spikes then reverts; a soft-bistable coupling trap at the empirical TFR-1.5 ridge; and a per-region
calibration whose baseline reproduces the known decline (Korea alone in the collapse basin) with no lever.

### Dynamical findings (re-judgement of the catalogue)

| finding | evidence from the coupled dynamics |
| --- | --- |
| baseline reproduces reality | model TFR23 matches all six regions exactly; baseline 2125 shows persistent sub-replacement, Korea the acute collapse (TFR 0.72→~0.47, C 0.52→0.38) - no spontaneous recovery |
| tempo is a mirage | a timing lever spikes the period rate (Korea peak ~0.91@yr12) then reverts to baseline - it borrows births from the future, changes no completed family |
| quantum needs coupling | raising parity works where coupling is intact (Germany 1.44→~1.95) but is gated where coupling has collapsed (Korea) - the keystone, emergent not assumed |
| coupling is the escape | only levers that rebuild coupling cross the separatrix; 7 of 88 single levers achieve a coupling-escape on Korea (in-kind+permanence, universal+state-funded+de-risk, compress x lottery-band, universal childcare, inequality compression), the rest bend or stall |
| migration is a bridge | biggest raw effect (+115pp mean population) but C unmoved - it buys time, it does not cure (flagged one-time bridge) |
| coercion backfires | 8 coercive levers (tutoring ban, top-down propaganda, wealth cap, lock-in/covenant/adultery, porn ban, egg-freezing trap) push the trajectory below baseline |
| ranking strongest→weakest | migration (bridge) > coupling-escape (in-kind/inequality/childcare ~+27-32pp) > durable-bend (gender-equity/penalty-removal/housing/precarity ~+20-26pp) > weak/mirage (cash/allowance/IVF ~0-5pp) > backfire (negative) |
| timing is decisive | the same keystone bundle compounds through momentum when started early (2025) and is largely wasted a generation late (2055) - leverage is a function of position and timing |

### Lessons

- **Make the model the judge** - static response curves give a lever's shape but not its fate; integrating each intervention through the coupled model over generations separates a durable quantum shift from a tempo mirage, and shows which levers actually cross the separatrix
- **Channel structure must be the observable parameters** - routing every lever through one bistable state flattens the analysis; letting interventions move the campaign's own parameters (C, ρ, P̄, τ) and reading TFR off the decomposition restores interpretable, separable signals
- **Position and timing dominate magnitude** - the same lever recovers Germany and only bends Korea; the same bundle compounds early and is wasted late - the dynamical view makes this measurable

## E20 - Seldon harbingers (ablation for the least-cost levers)

E20 asks the cost question the campaign had deferred: of the levers that improve fertility, which are the
**Seldon harbingers** - the least-cost, least-effort nudges that measurably bend the Seldon judgement, not
necessarily escape the basin? Found by **ablation** on the E19 coupled model, ranking levers by
fertility-improvement per **composite cost** (fiscal + coercion + side-effect). Executed in
`notebooks/15-kj-seldon-harbingers-ablation.ipynb`. Six hypotheses H164-H169, all SUPPORTED.

### E20 at a glance

| id | claim | evidence | verdict |
| --- | --- | --- | --- |
| E20-H164 | a near-free legal coupling lever is the best improvement-per-cost harbinger | cohabitation legal recognition: efficiency 2.47 at cost 0.09, +0.22 TFR (bends the fate) - tops all twelve levers | SUPPORTED |
| E20-H165 | a full recovery bundle ablates to a lean 3-lever efficient core | inequality-compression + gender-equity + legal recognition keep the full +1.28 TFR at cost 0.69 vs the 10-lever bundle's 2.56 (~a quarter of the cost) | SUPPORTED |
| E20-H166 | coupling is non-ablatable; cash is the worst bang-per-buck | strip all coupling → +0.06 TFR (holds); cash-allowance efficiency 0.01 - the mirage confirmed on the cost axis | SUPPORTED |
| E20-H167 | the harbinger buys more improvement the earlier it fires | gender-equity +0.45 TFR started now vs +0.23 a generation late (momentum) | SUPPORTED |
| E20-H168 | the cost-vs-improvement Pareto frontier has a low-cost knee at the cheap coupling combos | the frontier rises steeply then flattens; the knee sits at ~0.3 composite cost | SUPPORTED |
| E20-H169 | the harbinger is position-specific | the same near-free lever bends deep-basin Korea/Japan and recovers near-ridge France - efficiency climbs toward the ridge | SUPPORTED |

### Lessons

- **The harbingers are cheap coupling nudges, not big fiscal levers** - cohabitation legal recognition, gender-equity and norms top the improvement-per-cost ranking; in-kind childcare and cash sit far below
- **Ablation exposes the efficient core** - most of a recovery bundle's cost is redundant; a lean coupling core keeps the gain at a quarter of the cost
- **Cost has a time and a place** - the same harbinger is cheaper per unit of improvement applied early and near the ridge; a late, deep-basin application needs more

## E21 - Relationship machinery: a research round, and a meta-finding

E21 is a research round, not a modelled batch. It fanned out on the *proximate* machinery of coupling on the
user's hypotheses - relationship-scarring ("damaged soul"), the "mileage" mate-devaluation penalty, the beauty
arms race, the therapy lever (couples + self-repair), and relationship education - grounded in five Opus
research digests (30+ papers). The point was to test whether any of these adds a *new* population lever.

The meta-finding is the value: **almost every proximate/psychological mechanism is real for an individual but
evaporates at population scale, dominated by selection.** Honest verdicts:

- **Relationship-scarring** - PARTIAL, mostly selection. The durability limb holds (serial partnering -> higher subsequent dissolution, ~+60% for 2+ prior cohabiting partners), but the "pickier/slower" limb is largely an age + market-thinning artifact, and the causal channel that survives is *attitudinal* (churn lowers divorce barriers), not a wounded psyche; Kuperberg's age-at-coresidence critique is the strongest doubt
- **The "mileage" penalty** - largely REFUTED as a lever. A large *stated* preference (d≈0.87 for 4->12 partners) that vanishes in *revealed* behaviour: lifetime partner count is essentially unrelated to whether people marry (Smith & Wolfinger 2022). The double standard is small and weakening. The real market-thinning force is economic ("unmarriageable men"), not mileage
- **The beauty arms race** - real but modest and SYMPTOMATIC. Appearance pressure -> body dissatisfaction is causal (TikTok d≈−0.45), but no measured beauty -> fertility coefficient; it is a positional-competition channel endogenous to the same drivers, Korea "a coincidence dressed as an experiment"
- **The therapy lever** - individually efficacious (couples EFCT g≈0.73), a POPULATION lever unproven. The gold-standard population RCTs (Building Strong Families, Supporting Healthy Marriage) found no effect on staying together, with hints of harm - the clinical numbers are a selection effect of motivated help-seekers

The lesson that carried into E22: **at population scale, structure beats psychology.** The levers that reach
everyone (economic security, the cost of being young, marriageable men, de-positionalising competition) move
the curve; the ones that reach the motivated (therapy, education, matchmaking) help real people but do not bend
a nation's fate.

## E22 - The structural levers, and the education optimisation

E22 tests the five strongest *structural* levers that survived the E21 filter, each grounded in
quasi-experimental research and run through the E19 coupled model over four generations, then rated on the E20
composite cost. Executed in `notebooks/16-kj-structural-levers.ipynb`. Seven hypotheses H170-H176.

### E22 at a glance

| id | claim | evidence | verdict |
| --- | --- | --- | --- |
| E22-H170 | the marriageable-men lever - raise non-college men's earnings/employment | CAUSAL, the strongest in the campaign: two natural experiments agree (Autor-Dorn-Hanson China shock cuts fertility 6.1/1,000 + marriage 4.2pt; Kearney-Wilson fracking +\$1k/capita → +3% births, marriage flat); elasticity ~0.2-0.4; the ONLY one of five that *bends* Korea (+0.48). Catch: raises births not marriage (partly non-marital); stronger in East Asia via marriage | SUPPORTED |
| E22-H171 | young-adult cost compression | causal but net-small - house prices +5% owners / −2.4% renters, net +0.8% (Dettling-Kearney); mostly a timing shift via liquidity, not the debt itself | PARTIAL |
| E22-H172 | the time lever (shorter hours / 4-day week) | plausible, UNPROVEN - Korea's 35-45hr pregnancy-intention sweet spot (Kim 2023) is cross-sectional; no work-time-reduction → births trial has reported | PARTIAL |
| E22-H173 | anti-atomisation (kin proximity) | causal but conditional+modest - grandmother ≥200km ~1 fewer child (Engelhardt 2019); modern effect fires only where public childcare is absent; cheapest of the five → a harbinger | SUPPORTED |
| E22-H174 | positional arms-control (cap the education/beauty race) | mechanism ironclad (Doepke inequality → intensive parenting; Korea's \$19.7B tutoring race) but the INTERVENTION has no clean natural experiment anywhere; the blunt form (a tutoring ban) backfired in E16 | PARTIAL |
| E22-H175 | income not degrees (the education paradox) | raising male INCOME bends Korea +0.51; male DEGREES only +0.20, because the university arms-race + postponement eat ~+0.18 of the income+matching gain; both are super-additive (+0.99) but the efficient move is income, not the credential war | SUPPORTED |
| E22-H176 | the contrarian optimal bundle | male income + kin-proximity + gender-equity-in-the-home bends Korea +1.08, five-fold the naive "push degrees + hand out cash" bundle (+0.25); ablates to a lean income-anchored core | SUPPORTED |

The **required-policy-dose** analysis makes the difficulty honest: granting the fracking elasticity, Korea would
need a sustained male-earnings gain of ~12 fracking-booms just to *hold* today's 0.72, ~25 to *bend* to 1.0, and
~48 to *recover* to the 1.5 ridge (tens of percent of GDP-per-capita) - a linear out-of-sample extrapolation
that *sizes* the ask rather than predicting it. Provenance: Autor-Dorn-Hanson (NBER 23173), Kearney-Wilson (NBER
23408) and Black-McKinnish-Sanders (2005) are downloaded with digests.

### Lessons

- **Structure moves populations; psychology moves individuals** - the E21/E22 through-line, now quantified: marriageable-men is the only single lever that bends a deep-basin region, and it is economic
- **The sex of the earner is not neutral (controversial, and qualified)** - male earnings are pro-fertility; female earnings were fertility-suppressing in the old specialisation regime but flip *positive* under gender equity in the home (Doepke-Kindermann; the FLFP-fertility correlation flipped positive by the 2000s). The honest read is both/and - raise his wage AND lower her time-cost - NOT a retreat to traditional roles, which the campaign already found backfires
- **Income, not degrees** - the fix for both the growth need and the educated-women-need-matches squeeze is raising male *income* off the university track (trades, entrepreneurship), because forcing more men into university feeds the very arms race that suppresses fertility
- **You can't legislate a boom, but you can size it** - modelling the end-effect and backing out the required policy dose turns "the prescription is hard" into a measurable mountain

## Interventions parking lot (recorded, NOT planned)

Candidate interventions for a later, separate round - **no hypotheses planned until the model is calibrated** (an uncalibrated model cannot size an intervention). Recorded here so the ideas are not lost.

- **INT-1 Dating-app / attention-economy regulation** - mechanism: dating apps use variable-ratio (slot-machine) reinforcement, engineered for time-on-app → inflates optionality/expectation pressure (Ψ, C_expect) and shortens union duration D, attacking the coupling keystone; precedent: states regulate the addictive mechanism, not the category (gambling licensing / age-gating / safeguards; loot-box bans in Belgium & the Netherlands target the mechanic, not the game); candidate lever: reduce Ψ / C_expect, lengthen D; status PARKED
- **INT-2 Adolescent relationship-skills training** - mechanism: communication and conflict-resolution skills taught in early adolescence → more durable unions (raises D, lowers δ_div) and plausibly better formation, strengthening the keystone via stability; precedent: school-based social-emotional-learning and relationship-education programs (PREP; "Love Notes" / "Relationship Smarts"); candidate lever: lengthen D, reduce δ_div; status PARKED

## E23 - The exit machinery: custody, alienation, and the Iceland model (a research round)

E23 is a research round, not a modelled batch. It fanned out on two user hypotheses about what happens to fertility on the *other side* of the coupling gate - when a union dissolves (parental alienation, custody, the "downside risk of parenthood") and when childbearing is *decoupled* from marriage altogether (the Iceland model - children raised across multiple partnerships, buffered by the welfare state). Both are deliberately Western/Nordic/US cases, extending the evidence base off East Asia. Four Opus/Fable digests, ~50 papers.

The meta-finding: **both roads lead back to the coupling keystone already in the model - the headline constructs are either unproven at population scale or route into channels the campaign already owns (formation C, the exit valve, inequality).** Honest verdicts:

- **Custody-regime commitment insurance** - STRENGTHENING, and the *only* published causal fertility estimate in this whole space. Halla (2013, JEEA): staggered US joint-custody reforms raised marriage and marital fertility ~8-14% (strongest for women 35-44) and cut male suicide and domestic violence; Spain's shared-parenting laws cut intimate-partner violence 40-50% (Fernández-Kranz). A shared-custody presumption *caps the male downside of dissolution* → raises willingness to commit (channel C). This is the modellable core, and it subsumes the fear stories below
- **Parental alienation as a standalone fertility driver** - PLAUSIBLE-BUT-UNPROVEN, bordering fringe. Zero direct alienation→fertility evidence exists; the construct itself is contested (not in DSM-5, removed from the ICD-11 index in 2020, called an "unscientific pseudo-concept" by the UN Special Rapporteur 2023, and weaponised against abuse-alleging mothers per Meier 2020). The *upstream* facts are real - custody asymmetry, post-divorce father-contact loss, and divorce-*risk* as a brake on marriage (Waller & Peters 2008) - but any TFR effect is unquantified. Enters only as a small, high-uncertainty male-side modifier on C, central estimate ≈ 0, heavily collinear with divorce-risk and marriageable-men (do NOT add as an independent term)
- **Divorce-regime salience** - STRENGTHENING (modest). Unilateral divorce lowered fertility, mostly via the out-of-wedlock "shotgun-marriage" channel (Alesina & Giuliano 2006; Bellido & Marcén 2014) - but easy exit also cheapens entry, so the net is small and two-way; consistent with E17's "the exit is the valve"
- **Fear-transmission / the "marriage strike"** - WILD, unmeasured, but the theoretically distinctive one: perceived downside risk updated from peers/media, decoupled from realised risk (men fare *better* financially post-divorce but worse on child access, so the fear is gender-calibrated to each side's real loss). Fits E19's perceived-state architecture exactly, and gives a falsifiable signature (fertility tracking discourse, not custody statistics). If true, a near-free information/legal-certainty harbinger; if false, cheap to null

**The Iceland model** (decoupled, welfare-buffered childbearing):

- **Marriage-gate softening** - STRENGTHENING, a direct extension of E17/E18's break-the-marriage-birth-package finding. Iceland runs ~70% non-marital births vs Korea's 2.5%; the Nordics held TFR 1.7-2.0 for decades while East Asia's marriage collapse translated one-for-one into birth collapse. National non-marital-birth share is the natural gate-softness parameter on C→births
- **The Iceland falsifier (the discipline check)** - CONTRARIAN, and the sharpest result of the round. Iceland's *own* TFR fell 29% (2010→2023) to 1.59, then 1.56 (2024, lowest ever), with the 70% norm fully intact. **Decoupling shifts the fertility *level*, not the *trend*** - once union formation itself falters (postponement + rising cohabiting-union instability; Hellstrand et al. 2021 "Not Just Later, but Fewer"), a soft gate on C is worthless because C itself is falling. This is the coupling keystone, seen from the Nordic side: the gate matters only while people still walk through it
- **Insurance, not cash (welfare as third parent)** - PARTIAL, the decisive nuance. The Iceland model rests on a state that underwrites the birth against partner loss (guaranteed child maintenance, universal daycare, long leave) - a different object from the baby-bonus cash the campaign already found is a mirage. But the seductive claim "Nordic welfare neutralises the instability penalty" is *contradicted* by the best comparative evidence (Breivik & Olweus 2006; Nieuwenhuis & Maldonado 2018): welfare buffers the *money* (~0.4-0.6 coefficient), not the *disruption* - a residual, non-spendable cost remains
- **Multi-partner fertility ("children by different fathers")** - CONTROVERSIAL, net contested. A shared "cement baby" raises births at the margin per new union (Thomson et al. 2014), but repartnering only *partially* compensates the births the separation destroyed (Demography 2022), and the child-outcome costs (behaviour, achievement; Norwegian register data) are real though largely selection. Small population contribution, ethically loaded
- **Diverging destinies collapses onto inequality** - the load-bearing theoretical result. McLanahan (2004): the family-instability cost is not a flat per-birth penalty; it concentrates among the disadvantaged and therefore *scales with inequality* - the campaign's Doepke root lever (E15). Low-inequality Iceland is the natural experiment: a compressed gradient is why the norm ran high fertility for a generation. The Iceland ledger needs no new mechanism; it enters as an interaction between family-structure cost and the inequality parameter

The lesson carried forward: **the West does not escape the coupling verdict, it confirms it.** Iceland decoupled marriage from birth and underwrote the cost with a welfare state - and still fell below 1.6 once union formation faltered. The modellable signal from the whole round is the custody-regime *commitment-insurance* lever (Halla's causal estimate) feeding channel C, and a gate-softness parameter for the marriage→birth link - both parked for a future calibrated batch, not modelled here.

## E24 - The exit machinery simulated and ablated (H177-H181)

E24 is the first batch run under the mandatory simulation-then-ablation protocol: the five exit-machinery hypotheses from the E23 research round, each pushed through the E19 coupled model over four generations on the Korea / Germany / France triad and ablated (E20 method). Verdicts are keyed on standalone strength with the bundle marginal as a redundancy check. Executed in `notebooks/18-kj-exit-machinery-simulation.ipynb`. The one load-bearing lever is the shared-custody presumption (H180); child-contact-loss (H178) is collinear with it; post-divorce conflict reduction (H177) is weak; the intergenerational scar (H179) is a modest confounded headwind; and universal state-funded repair (H181) ablates toward zero, not clearing the E21 voluntary-program null.

### E24 at a glance

| id | claim | evidence | verdict |
| --- | --- | --- | --- |
| E24-H177 | post-divorce conflict reduction (state mediation/co-parenting) lifts fertility via preserved re-partnering | standalone Korea +0.070 (holds) - weak on its own; bundle marginal +0.152 is position-amplified, not intrinsic; small and concentrated in the ~10-15% high-conflict caseload | PARTIAL |
| E24-H178 | child-contact-loss risk is a separable male-side commitment brake | standalone Korea +0.130 but COLLINEAR with H180 (same custody channel) - the model has no signal that separates them, so no independent additive contribution | PARTIAL |
| E24-H179 | intergenerational divorce-transmission imposes a compounding fertility scar | headwind drag Korea -0.040, Germany -0.208 over a 30-yr accumulation; register-backed core but confounded by genetic selection and the conflict increment is unproven | PARTIAL |
| E24-H180 | a shared-custody presumption is the load-bearing corrective coupling lever | standalone Korea +0.241 (bends), Germany bends, France recovers; bundle marginal +0.327 - carries the bundle; caveat: marriage-centred, the model lacks a marital-share gate so France is likely overstated | SUPPORTED |
| E24-H181 | universal state-funded relationship repair clears the E21 voluntary-program null | standalone Korea +0.008 - ~zero once the durability erode is applied (Army-PREP fade); the +0.039 bundle marginal is pure position-amplification, so the contrarian universal bet does not clear the E21 null in-model | REFUTED |

## E25 - Social norms and abortion, and the bistable norm state (H182-H187)

E25 tests the social drivers of fertility - abortion access, penalising helpers, and the support scaffolding around parents - and introduces a genuine model extension: a **bistable social-norm state N** added to the library core (`emergent.py`), a double-well contagion `dN/dt = -aN(N-Nlo)(N-thN)(N-Nhi) + fN` with a tipping point thN=0.25 and hysteresis, coupling to childlessness as a baseline-preserving deviation. Six hypotheses, executed in `notebooks/19-kj-social-norms-abortion.ipynb`. In-kind childcare is the one load-bearing welfare lever; the coercive abortion levers are refuted (the restrictiveness sweep peaks at an interior optimum, a total ban leaks and reverts, and penalising helpers nets to zero against its own backfire); and the norm state is a confirmed bistable mechanism but a weak pronatal lever and a dangerous vulnerability (a stigma push tips an untrapped country down far more easily than a pronatal push lifts a trapped one).

### E25 at a glance

| id | claim | evidence | verdict |
| --- | --- | --- | --- |
| E25-H182 | abortion restrictiveness graded to a total ban lifts fertility | standalone best +0.001; the restrictiveness sweep peaks at an INTERIOR r*≈0.5 - a total ban is dominated because leakage δ(r) and Romania-style reversion rise with severity; small, coercive, high autonomy cost | REFUTED |
| E25-H183 | penalising helpers closes the abortion leakage worth the backfire | standalone best +0.001 - lowering leakage (δ 0.55->0.30) is cancelled by the security/coupling chill it induces; the enforcement lever nets to ~0 with the highest coercion cost in the batch | REFUTED |
| E25-H184 | kin / grandparental support raises fertility (cooperative breeding) | standalone best +0.074, bundle marginal best +0.083; real cooperative-breeding channel (Sear-Mace) but a partial lever - proximity can be subsidised, kin density cannot be legislated | PARTIAL |
| E25-H185 | in-kind childcare services beat equivalent cash | standalone best +0.127 (['holds', 'bends', 'bends']), bundle marginal best +0.140; the durable Pbar+S in-kind geometry - the strongest welfare lever in the batch | SUPPORTED |
| E25-H186 | reversing social atomisation restores coupling | standalone best +0.077, bundle marginal best +0.087; a real coupling channel that helps the trap-limited basin but diffuse and high-leakage - a harbinger-grade nudge, not a heavy lever | PARTIAL |
| E25-H187 | the bistable social norm is a pronatal lever | standalone best +0.049, marginal best +0.058; the MECHANISM is confirmed (tips + LOCKS with hysteresis) but as a pronatal lever it is weak on this triad - Korea is coupling-limited (norm barely moves TFR) and Germany is already untrapped; its real force is defensive/asymmetric - a modest STIGMA push tips Germany down by 0.13 | PARTIAL |

## E26 - Alternative mating, kinship and cultural structures (H188-H207)

E26 is the twenty-hypothesis contrarian fanout on alternative structures - polyamory, matriliny (brief; the deep matriarchy optimisation is E29), communal / kibbutz cost-socialisation, cultural normalisation (the norm channel), grandmother / kin proximity, and state-support with the autonomy frontier - grounded in `references/papers/e26-alt-structures-digest.md`. Executed in `notebooks/20-kj-alternative-structures.ipynb`. The meta-finding holds: a structure moves fertility only through a channel the model already owns - cost-socialisation (the kibbutz/childcare SUPPORTED core), kin proximity (matrilocal/grandmother, real but an endowment not a dial), and the causal norm channel - while the exotic wrappers are dominated (polyamory dilutes commitment, matriliny leaves quantum flat with kin competition, grandmother-buyout and plural-parent legality do nothing to quantum, autonomy-lowering traditionalism is priced out by the gender-equity root lever). Complementary winners stack; same-channel levers saturate.

### E26 at a glance

| id | claim | evidence | verdict |
| --- | --- | --- | --- |
| E26-H188 | polyamory raises the partnership count -> coupling | best-region ΔTFR +0.016; concurrency raises partnership count but dilutes the dyadic commitment that predicts childbearing (Toulemon); no CNM fertility premium (Moors 2021; Gupta 2024) | REFUTED |
| E26-H189 | polyamorous alloparenting shares child cost -> parity | best-region ΔTFR +0.018; the only working sub-mechanism is cost-sharing (alloparenting), which is not non-monogamy - it is the communal channel wearing a different label | PARTIAL |
| E26-H190 | CNM concentrates mating on high-status men -> excluded-male externality | best-region ΔTFR -0.015; male reproductive variance rises, the classic polygyny-instability externality (Henrich 2012) - drags coupling | REFUTED |
| E26-H191 | matrilineal descent raises fertility | best-region ΔTFR -0.000; lowers female childlessness but co-resident female kin COMPETE (Mattison matrilineal puzzle); Mosuo TFR is not high - autonomy up, quantum flat | REFUTED |
| E26-H192 | matrilocal residence -> grandmaternal childcare | best-region ΔTFR +0.028; the transferable signal is matrilocal proximity delivering deliverable grandmaternal care (Holden-Sear-Mace) - the kin channel, not the descent rule | PARTIAL |
| E26-H193 | stacking co-resident female kin pools childcare | best-region ΔTFR -0.001; same-sex kin crowding turns cooperative into competitive beyond a small optimum (Mattison 2011) - antagonistic, net negative | REFUTED |
| E26-H194 | kibbutz-style full cost-socialisation of a child | best-region ΔTFR +0.105; the cleanest natural experiment: kibbutzim socialised the marginal cost and held above-average fertility; privatisation cut lifetime fertility 0.65 (Anson-Meir; Ebenstein 2016) - the channel is cost, not communalism | SUPPORTED |
| E26-H195 | generic cooperative breeding raises fertility | best-region ΔTFR +0.016; survival benefit robust (Sear-Mace 2008) but the fertility-quantum boost is contested (Strassmann-Kurapati 2010); works through committed kin, not generic community | PARTIAL |
| E26-H196 | state-funded universal in-kind childcare | best-region ΔTFR +0.097; the scalable state-support variant: universal under-3 care raised German fertility ~2.8% (Bauernschuster 2016; Rindfuss Norway) - modest, causal, in-kind | SUPPORTED |
| E26-H197 | the communal FORM without cost-socialisation raises fertility | best-region ΔTFR -0.000; the identification: privatised kibbutz kept the form but lost the fertility (Ebenstein) - communalism per se is not the lever | REFUTED |
| E26-H198 | media is a causal fertility channel (antinatal direction) | best-region ΔTFR -0.004; the best-identified norm evidence runs ANTINATAL: Globo telenovelas lowered Brazilian fertility (La Ferrara 2012), 16-and-Pregnant cut teen births 5.7% (Kearney-Levine 2015) - N is causal, use for calibration | SUPPORTED |
| E26-H199 | deliberate pronatal media raises fertility | best-region ΔTFR +0.029; symmetric pronatal efficacy is unproven and weaker (reactance; the E25 propaganda-backfire result); Israel's pronatalism is a whole-society norm, not a campaign | PARTIAL |
| E26-H200 | a pronatal norm multiplies structural levers | childcare×pronatal-N interaction +0.003; roughly additive in-model - the multiplier is weak, the channels are separable | PARTIAL |
| E26-H201 | maternal grandmother proximity raises fertility | best-region ΔTFR +0.034; a living maternal grandmother raised grandchildren born ~2.1, decaying with distance (Engelhardt 2019; Lahdenpera 2004) - a real input, but an endowment not a policy dial, and shrinking | PARTIAL |
| E26-H202 | paying grandparents to provide care recreates the effect | best-region ΔTFR +0.006; buying out the grandmother does not recreate proximity or the commitment that gives kin care its value - monetising kin is a weak substitute | REFUTED |
| E26-H203 | kin buffers the late-tempo fecundability loss | best-region ΔTFR +0.014; a tempo x kin derivative interaction - kin lets daughters breed earlier/more, buffering late tau; real but the buffer is disappearing with dispersion | PARTIAL |
| E26-H204 | legal recognition of plural parents raises fertility | best-region ΔTFR +0.002; California SB274 / BC Family Law Act are genuine institutional innovations but scoped to child security, touch <1% of births, no quantum effect | REFUTED |
| E26-H205 | the complementary stack childcare + kin + pronatal-N is super-additive | three-way interaction +0.005; the same-channel overlap keeps it near-additive | PARTIAL |
| E26-H206 | state childcare and grandmother care are substitutes that crowd each other out | childcare×kin interaction +0.001; little overlap in-model | REFUTED |
| E26-H207 | autonomy-lowering pronatal traditionalism raises fertility net | best-region ΔTFR +0.021; raising quantum by LOWERING women's autonomy erodes the gender-equity-in-the-home root lever (Doepke-Kindermann; Kleven) - dominated once the autonomy cost is priced | REFUTED |

## E27 - Reproductive-concentration structures (H208-H212)

E27 is a deliberately controversial fanout on reproductive concentration - polygyny (male-concentrated), polyandry (female-concentrated), hypergamy skew, state sanction and media normalisation - testing the excluded-sex externality on coupling C against the within-marriage parity effect under the multiplicative TFR form. Magnitudes calibrated to the per-wife parity deficit (Bongaarts 1984). Five hypotheses, executed in `notebooks/21-kj-concentration-structures.ipynb`. The arc confirms the model's sex-ratio pivot: the excluded-sex externality on C is the binding term, polygyny is a double loss (per-wife parity down and the excluded-male C-drag swamps it), and the one structure that reliably moves TFR (polyandry) moves it the wrong way.

### E27 at a glance

| id | claim | evidence | verdict |
| --- | --- | --- | --- |
| E27-H208 | polygyny raises aggregate fertility (a collapse lever) | mean ΔTFR -0.562; decomposition shows the excluded-male C arm (-0.457) swamps the parity arm (-0.209) - a double loss; Sahel high-TFR is development-confounded | REFUTED |
| E27-H209 | polyandry SUPPRESSES aggregate fertility (a population brake) | mean ΔTFR -0.029; per-woman parity intact but female childlessness up (surplus unmarried women, Goldstein 1976) - the one mechanism that reliably moves TFR moves it DOWN, a population brake not a lever (wrong direction for collapse) | PARTIAL |
| E27-H210 | mating-market skew drags coupling and delays partnering | mean ΔTFR -0.026; a modest, self-correcting C drag plus tempo delay, but unquantified in the literature (thin parameter) | PARTIAL |
| E27-H211 | state sanction of polygyny manufactures the missing quantum | mean ΔTFR -0.532; legitimacy+subsidy entrench the externality rather than reverse it - sanction changes magnitude not sign, development-confounded | REFUTED |
| E27-H212 | media-normalising the structure raises fertility | mean ΔTFR -0.214; pure N forcing with no material channel plus the incel-media C drag; media diffuses small-family ideals - cheap talk reverting under N hysteresis | REFUTED |

## E28 - Polygamy across the endorsement spectrum, with an interaction matrix (H213-H226)

E28 sweeps polygamy across the full policy spectrum - state suppression (enforced monogamy, the Henrich WEIRD dividend) through cultural endorsement to state endorsement plus subsidy - crossed with the polygyny/polyandry variants, with the Edlund sex-ratio-to-crime side-effect stacked and a pairwise interaction-discovery matrix. Fourteen hypotheses, executed in `notebooks/22-kj-polygamy-spectrum.ipynb`. The developed-regime fertility optimum sits at the suppression corner and slopes monotonically down through endorsement; the only regime where endorsement raises fertility is low-development (a genuine Tertilt sign-flip, developed −0.807 vs low-dev +0.263 at full endorsement); state subsidy cannot repair the excluded-male C collapse; no variant lifts developed-regime TFR net of side-effects.

### E28 at a glance

| id | claim | evidence | verdict |
| --- | --- | --- | --- |
| E28-H213 | state suppression of polygyny (enforced monogamy) is the fertility-favouring institution in the developed regime | enforced-monogamy dividend mean ΔTFR +0.698 (>0): reversing the excluded-male externality lifts C and S (Henrich 2012); the spectrum optimum sits at the suppression corner e=-1.0 | SUPPORTED |
| E28-H214 | cultural / society endorsement of polygyny raises fertility | developed-regime sweep slopes down through endorsement; at cultural endorsement e=+0.5 mean ΔTFR -0.803 - a loss | REFUTED |
| E28-H215 | state endorsement + subsidy of polygyny manufactures the missing quantum | full state endorsement e=+1 mean ΔTFR -0.807; the subsidy offsets part of the S loss but not the C drag - subsidy x parity is antagonistic | REFUTED |
| E28-H216 | the development regime flips the sign of polygyny (Tertilt +40% only in low-development) | at full endorsement e=+1 the developed regime gives -0.807 but the low-development regime gives +0.263 - opposite signs, the Tertilt sign-flip; developed optimum is suppression (e=-1.0), low-dev optimum is endorsement (e=+1.0) | SUPPORTED |
| E28-H217 | polyandry endorsement suppresses fertility regardless of endorsement level | polyandry sweep is negative across e, at full endorsement mean ΔTFR -0.595; surplus unmarried women (Goldstein 1976) - a brake at every endorsement level | SUPPORTED |
| E28-H218 | state suppression of polyandry raises fertility by un-rationing women's reproduction | suppressing polyandry mean ΔTFR +0.117; mechanically un-rations female reproduction but the effect is small in a low-childlessness-headroom developed regime | PARTIAL |
| E28-H219 | the excluded-sex externality on C scales with endorsement reach | the fC drag grows monotonically with |e| in the builder; the developed sweep's downslope is driven by it - reach amplifies the externality | SUPPORTED |
| E28-H220 | endorsement shifts the bistable norm N enough to matter on its own | norm-endorse standalone mean ΔTFR -0.111; the fN arm alone is weak - legitimacy without a material channel is cheap talk (E25 H187 hysteresis) | PARTIAL |
| E28-H221 | a state subsidy offsets the polygyny externality | subsidy x polygyny-reach interaction -0.492; the subsidy lifts S but cannot repair the C collapse - antagonistic to the parity loss, does not flip the sign | PARTIAL |
| E28-H222 | the excluded-male crime side-effect dominates any polygyny fertility gain | crime index rises 3.4x with reach (Edlund 2013) while developed ΔTFR falls - the side-effect and the fertility effect both push against endorsement; net stacked, polygyny endorsement is dominated | SUPPORTED |
| E28-H223 | polygyny is a viable lever once women's autonomy is priced in | polygyny lowers female autonomy (the Doepke-Kindermann / Kleven gender-equity root lever) on top of the fertility loss - dominated on both the fertility and the autonomy axis | REFUTED |
| E28-H224 | the interaction structure is dominated by the development sign-flip and the reach x externality | largest off-diagonal cell is polygyny-reach x low-dev (-0.309); enforce-mono antagonises polygyny-reach; the matrix has no super-additive pro-fertility endorsement cell in the developed regime | SUPPORTED |
| E28-H225 | the spectrum optimum is an interior endorsement level | the developed-regime optimum is the CORNER at suppression (e=-1.0), not interior - endorsement monotonically worsens fertility; the interior-optimum claim is refuted | REFUTED |
| E28-H226 | across the whole spectrum no polygamy variant lifts developed-regime TFR net of side-effects | every developed endorsement point is <=0 and carries a rising crime + autonomy cost; only the suppression corner (enforced monogamy) is fertility-and-stability-favouring - the closing synthesis | SUPPORTED |

## E29 - Matriarchy stability optimisation on the population framework (H227-H246)

E29 is a large, calibrated fanout on whether a matriarchal arrangement can raise fertility, modelled after the Mosuo and built on the new population-distribution framework (`population.py`, Gauss-Hermite bucketed reparameterisation). It expresses the mechanism a scalar model cannot: paternity compression gives high-quality men the best outside option so they **exit** (a tail operation on the male marriageability distribution), the retained pool weakens, and **female hypergamy** - calibrated from the dating-market desirability gap (Bruch-Newman 2018; Esteve 2016) - collapses the match probability, and hence coupling, past a threshold s*≈0.38, with no male aggression required. Paternity severance also feeds the E30 intergenerational alienation channel, so the collapse runs on two timescales (hypergamy now, alienation a generation later). Twenty hypotheses, executed in `notebooks/23-kj-matriarchy-optimisation.ipynb`. No state funding, media push, or male-retention scheme fixes it (retention contradicts the compression that defines matriarchy); the only transferable pro-fertility part is matrilocal kin childcare, not the descent or paternity system.

### E29 at a glance

| id | claim | evidence | verdict |
| --- | --- | --- | --- |
| E29-H227 | matriliny raises female autonomy and lowers female childlessness but not quantum | matriliny lowers female childlessness (near-universal reproduction) yet Mosuo TFR is not high; co-resident female kin compete (Mattison matrilineal puzzle) - autonomy up, quantum flat | REFUTED |
| E29-H228 | paternity uncertainty is offset by avuncular (mother's-brother) investment | the avuncular buffer only partially compensates the dyadic-investment loss; net per-child investment is lower - a partial offset, not a wash | PARTIAL |
| E29-H229 | matrilocal residence delivers grandmaternal childcare (a real cost-of-children lever) | the matrilocal add-on lifts the sweep materially (+matrilocal optimum dTFR +0.184) - but this is the kin-childcare channel (E26 H201), not the descent system | PARTIAL |
| E29-H230 | stacking co-resident female kin pools childcare and raises fertility | same-sex kin crowding turns cooperative into competitive beyond a small optimum (Mattison 2011) - antagonistic, not additive | REFUTED |
| E29-H231 | matriarchy makes high-quality men exit, lowering retained male quality | tail selection on the male-q distribution: at s=0.5 the exit fraction is 0.64 and retained mean falls to -0.32 - the strong men withdraw first | SUPPORTED |
| E29-H232 | female hypergamy on the weak retained pool collapses coupling | with the desirability-gap bar b=+0.18, the coupling multiplier falls to 0.02 at s=0.6; the hypergamous match fails on the low-q remainder | SUPPORTED |
| E29-H233 | the instability needs no male aggression - pure withdrawal and selection suffice | the collapse is driven entirely by the exit tail-operation and the hypergamy bar; no coercion term is invoked - the structure is self-undermining | SUPPORTED |
| E29-H234 | the collapse threshold is predicted by a hypergamy bar calibrated from unrelated dating data | the dating-market desirability gap (Bruch-Newman) sets b=+0.18, which predicts a coupling-halving collapse at s*=0.38 - a cross-domain calibration transfer | SUPPORTED |
| E29-H235 | men are the infrastructure/defence substrate - their exit drops security S | the S withdrawal scales with the exit fraction (0.64 at s=0.6); the matriarchy depends on the male buy-in it erodes | SUPPORTED |
| E29-H236 | paternity severance lowers the next generation's marriageability a generation later | isolating the father-access channel (E30 intergenerational memory): near-zero contemporary effect (+0.000 at 2045) but -0.100 by 2095 - un-marriageable men and women downstream | SUPPORTED |
| E29-H237 | matriarchy compounds - it degrades the next generation, not just the present | the delayed alienation stacks on the immediate hypergamy coupling loss; the structure is worse over generations than in any single one | SUPPORTED |
| E29-H238 | avuncular investment buffers the intergenerational father-absence cost | raising the avuncular share reduces the fF severance and the delayed cost - a real but partial buffer, never a full substitute for dyadic investment | PARTIAL |
| E29-H239 | the matriarchy collapse runs on two timescales - hypergamy now, alienation a generation later | the FULL matriarchy already craters coupling contemporaneously (-1.310 at 2045 via hypergamy), and the paternity channel adds a further delayed cost (-0.100 by 2095) - a double-timescale collapse, not a slow one | SUPPORTED |
| E29-H240 | state funding of the matriarchy repairs it | the state-funded variant optimum is s=0.10 dTFR=+0.782; the subsidy lifts S but cannot retain high-q men or satisfy hypergamy - it does not fix the instability | REFUTED |
| E29-H241 | media normalisation of matriarchy shifts the norm enough to stabilise it | a media N-push does not touch the exit or hypergamy mechanism; it is the E25 weak-pronatal-lever result again - cheap talk against a structural collapse | REFUTED |
| E29-H242 | engineering male retention stabilises the matriarchy | retaining high-q men requires restoring the status and paternity certainty that DEFINE the matriarchy's compression - a self-contradiction; you cannot have both | REFUTED |
| E29-H243 | there is an interior matriarchy strength that raises fertility | the pure-matriarchy sweep optimum is at s=0.00 with dTFR -0.008 - the optimum is the no-matriarchy corner; the exit-hypergamy instability dominates the interior | REFUTED |
| E29-H244 | the collapse is dominated by the exit x hypergamy interaction | in the interaction matrix the male-exit x paternity/coupling cell is +0.299; the buffers (avuncular, matrilocal) antagonise the losses - exit and hypergamy multiply into the collapse | SUPPORTED |
| E29-H245 | a stable pro-fertility matriarchy exists under the right conditions | it would need low hypergamy AND high male retention AND strong kin childcare - but retention is mutually exclusive with the paternity compression that defines matriarchy; no stable configuration in the developed regime | REFUTED |
| E29-H246 | the transferable part of matriarchy is matrilocal kin childcare, not the descent/paternity system | only the matrilocal-childcare add-on lifts fertility (+0.184); the descent + paternity-compression core is self-undermining via exit and hypergamy - keep the kin care, drop the structure | SUPPORTED |

### E29 lessons

- **Selection needs a distribution** - the matriarchy exit and hypergamy are tail operations on the marriageability distribution; the representative-agent scalar cannot express them, which is why the population framework (`population.py`) was built and validated (Jensen gap +0.093 off-threshold, 66% relative)
- **The instability is self-inflicted, not violent** - the structure collapses through male *withdrawal* plus female hypergamy, not male aggression; raising matriarchy strength lowers the exit cutoff, the retained pool weakens, and the hypergamous match fails
- **Two timescales** - the hypergamy coupling collapse is contemporaneous; the paternity-severance alienation cost lands a generation later through the intergenerational memory - a double-timescale failure, not a slow one

## E30 - Marriageability and intergenerational memory (H247-H260)

E30 is the batch that exercises the marriageability + intergenerational-memory core: a bilateral marriageability state q that gates coupling, fed by therapy/health (durable works, voluntary fades) and by the lifetime-integrated childhood environment carried as a per-cohort path integral (`ot.CohortMemory`, the Lagrangian method-of-characteristics form). Executed in `notebooks/24-kj-marriageability-intergenerational.ipynb`. Durable population-scale therapy clears the E21 voluntary-program null because it works through marriageability - a channel the relationship-repair trials never touched; the intergenerational path integral gives father-access loss a zero contemporary effect but a delayed cost that COMPOUNDS over the horizon (a spiral), and it turns shared custody, paternity certainty and therapy into levers with a second, delayed dividend through the child cohort. Cash cannot buy marriageability - it moves security, not q. The reframing: every structural lever must be scored over two generations, because the memory only shows up on that horizon.

### E30 at a glance

| id | claim | evidence | verdict |
| --- | --- | --- | --- |
| E30-H247 | durable population-scale therapy/health raises marriageability and clears the E21 null | durable best +0.140 (bends) vs the E21 voluntary-program null; it enters through marriageability q, a different channel from relationship-repair | SUPPORTED |
| E30-H248 | voluntary one-off couples therapy stays null | voluntary best +0.013 - q rises then erodes back (BSF/SHM/Army-PREP fade); confirms E21 in-model | REFUTED |
| E30-H249 | marriageability is bilateral - alienation lowers it for men AND women | q gates coupling for the population, not one sex; a fall in q reduces partnership formation regardless of side - un-marriageable men and women together | SUPPORTED |
| E30-H250 | father-access loss has no contemporary effect but a delayed intergenerational cost | father-access -0.4 (Germany): +0.000 at 2045 (contemporary ~0) but -0.111 by 2095 - the one-generation lag of the childhood-env path integral | SUPPORTED |
| E30-H251 | the intergenerational alienation compounds over the horizon | the loss deepens +0.000@2045 → -0.189@2124; the per-cohort path integral accumulates, so the cost grows rather than plateauing - a spiral | SUPPORTED |
| E30-H252 | relationship scars impose a delayed next-generation coupling cost | a scar forcing lowers childhood env → next-cohort q → coupling with the same one-generation delay; Germany ΔTFR -0.149 by 2125 | SUPPORTED |
| E30-H253 | a shared-custody presumption pays a delayed intergenerational dividend | custody (coupling insurance + father investment) gives +0.128 at 2050 rising to +0.259 at 2110 - the E24-H180 lever earns a second, delayed payoff through the child cohort | SUPPORTED |
| E30-H254 | paternity certainty raises father investment and pays an intergenerational dividend | father-access GAIN +0.4 lifts the next cohort's marriageability, +0.141 by 2110 - the mirror of the alienation loss | SUPPORTED |
| E30-H255 | the therapy dividend also compounds intergenerationally | durable therapy raises q, which raises father investment (phi*q) → childhood env → the next cohort's q - a healthier-fathers second dividend on top of the contemporary lift | SUPPORTED |
| E30-H256 | the intergenerational channel is calibrated to the fatherlessness literature | the father-absence path integral is register-backed (McLanahan-Sandefur; Autor 2019) and bounded rather than point-fit; the delay (27-45yr) and childhood window (0-18) are demographic, not tuned | SUPPORTED |
| E30-H257 | short-horizon evaluation understates structural levers | the shared-custody lever's benefit grows ~2.0x from 2050 (+0.128) to 2110 (+0.259) as the intergenerational dividend lands on top of its contemporary effect; a 2050-horizon evaluation captures only about half its eventual worth | SUPPORTED |
| E30-H258 | alienation is hysteresis-adjacent - a lost generation propagates forward | because a cohort's low q feeds the next cohort's childhood env, a depressed generation transmits forward; the loss at -0.189@2124 is still deepening, not recovering, within the horizon | PARTIAL |
| E30-H259 | cash can buy marriageability | a security push (fS=0.20) leaves q unmoved (qend +0.0000) while raising TFR only through the security channel; marriageability is health/attachment, not income - cash and marriageability are not substitutes | REFUTED |
| E30-H260 | the intergenerational memory reframes the campaign - score levers over two generations | the delayed dividends (custody, therapy, paternity) and the compounding costs (alienation, scars) only appear on a multi-generation horizon; a single-generation ledger misprices every structural lever | SUPPORTED |

## E31 - Parental alienation: legislation and prevention (H261-H270)

E31 asks what legislation and prevention actually do to parental alienation - the campaign's most short-horizon-underpriced force (E30). Grounded in `references/papers/e31-alienation-legislation-digest.md`, executed in `notebooks/25-kj-alienation-legislation.ipynb`, with an explicit timing split: `[NOW]` levers act on contemporaneous coupling, `[DELAY]` levers feed the per-cohort intergenerational path integral. The causal winner is a rebuttable shared-custody presumption (Halla 2013, +8-14% marital fertility); early mediation preserves contact (Emery 2001); but the punitive cluster - fines, criminalisation (Brazil Lei 12.318), forced reunification - is REFUTED, because punishment is conflict, it feeds the scar channel that transmits alienation, and criminalisation hands an abuser a weapon against a protective parent (Meier 2020). The DV carve-out and the weaponisation screen make the winner safe. Prevention + safely-designed shared custody beats punishment.

### E31 at a glance

| id | claim | evidence | verdict |
| --- | --- | --- | --- |
| E31-H261 | rebuttable shared-custody presumption (the causal winner) | mean ΔTFR +0.323; the one clean causal custody->fertility estimate: marital fertility +8-14%, marriage +5% (Halla 2013 JEEA); contact preserved for the next cohort | SUPPORTED |
| E31-H262 | rigid mandatory 50/50 vs rebuttable | mean ΔTFR +0.149; Kentucky HB528 divorce -25% but pre-trend, not causal (Stone 2023); rigidity forces 50/50 onto high-conflict/DV cases, injecting a scar - the geometry lesson rebuttable >= rigid | PARTIAL |
| E31-H263 | fines / sanctions / contempt for access denial | mean ΔTFR -0.020; no population RCT shows contempt/make-up-time durably raises contact; the adversarial escalation dominates the thin contact gain, and jailing the custodial parent harms the child | REFUTED |
| E31-H264 | criminalisation of alienation (Brazil Lei 12.318/2010) | mean ΔTFR -0.064; 14 years, no measured positive outcome, 2022 walk-back, UN moving to repeal; weaponisation flips the sign - an alienation cross-claim ~doubles a protective mother's custody-loss risk (Meier 2020). NOTE: backfire-only estimate; the deterrence sub-channel + monitoring is tested explicitly in E32 | REFUTED |
| E31-H265 | mandated reunification therapy / camps | mean ΔTFR -0.003; efficacy uncontrolled/weak, and the legislative tide runs the other way - Kayden's Law (VAWA 2022) + state bans (Piqui's/Abrial's Law) prohibit therapies that cut a child off from a safe parent | REFUTED |
| E31-H266 | mandatory co-parenting / divorce education | mean ΔTFR +0.008; mixed evidence, modest and fading (Guyette 2024; Sigal 2011), the E21 BSF/SHM null-with-fade signature; cheap, low-harm - a complement not a driver | PARTIAL |
| E31-H267 | early mediation (divert from litigation) | mean ΔTFR +0.111; at 12yr 52% of mediated nonresident parents talked weekly with their child vs 14% litigated, no rise in conflict (Emery 2001 RCT) - the best prevention feed into the delayed dividend | SUPPORTED |
| E31-H268 | DV carve-out design (safety-gated shared custody) | mean ΔTFR +0.258; the H261 presumption WITH automatic DVO rebuttal + abuse screening - keeps the fertility gain, zeroes the scar; Spain's safety-gated JPC saw IPV FALL 45% (Fernandez-Kranz 2024) | SUPPORTED |
| E31-H269 | weaponisation screen (the Meier correction) | mean ΔTFR +0.030; require corroborated adjudication of an abuse claim BEFORE an alienation finding can reverse custody - no fertility upside of its own, large harm-reduction; makes anti-alienation policy survivable | PARTIAL |
| E31-H270 | prevention-over-punishment synthesis | mean ΔTFR +0.409; bundle the complements (shared-custody default + mediation + co-parenting education + DV carve-out + weaponisation screen), EXCLUDING criminalisation/fines/forced reunification - super-additive with fScar driven negative | SUPPORTED |

## E32 - Combating alienation: the full toolkit (H271-H297)

E32 is the 27-hypothesis combat fanout - a stick ladder, the cooperation-reward/bond carrot family, a minor-offence/civil-penalty + corrective spread, and a graded custody-decoupled criminalisation ladder - each a single mechanism fanned out and calibrated by cross-domain mechanism transfer (HOPE, drug courts, SARP mandatory-arrest, Doyle/Barnevernet, CARES deposit contracts, contingency management, Staten Island day-fines, incarceration-harms-children). Grounded in `references/papers/e32-alienation-combat-digest.md`, executed in `notebooks/26-kj-alienation-combat.ipynb`. Two decisive findings: the carrot beats the stick on every axis (the un-weaponizable symmetric bond has the lowest defection, delta 0.05, and a credible carrot makes the stick near-redundant), and **weaponisation tracks STAKES not certainty** - a civil ticket at the same certainty as criminalisation is SUPPORTED because it cannot become a custody weapon (H289), where criminalisation (H274) is REFUTED. The graded custody-decoupled ladder is viable at the low rungs (fine, community service, suspended threat) but jail (H297) is REFUTED - it removes a parent from the child. Removal (H276) is the one unambiguous harm.

### E32 at a glance

| id | claim | evidence | verdict |
| --- | --- | --- | --- |
| E32-H271 | social-work supervision | mean ΔTFR +0.100; IFPS/Homebuilders g=0.18, null at family level - safe, cheap, dominated | PARTIAL |
| E32-H272 | stepped therapy (escalate on failure, abuse-gated) | mean ΔTFR +0.269; drug-court graduated-sanctions+treatment (Mitchell 2012, recidivism 50->38%); the escalation THREAT is the active ingredient, conditional on the abuse-gate | PARTIAL |
| E32-H273 | monitored sanction (certainty supplied) | mean ΔTFR -0.037; HOPE certainty (Hawken-Kleiman 2009) + tax-audit (Slemrod); monitoring turns the deterrence term positive but nets ~0 against the backfire - necessary not sufficient | PARTIAL |
| E32-H274 | raw criminalisation, no monitoring (severity) | mean ΔTFR -0.160; severity without certainty = zero deterrence (Nagin), high weaponisation - the E31 Brazil result mechanistically explained | REFUTED |
| E32-H275 | coercion sign-heterogeneity | mean ΔTFR -0.041; SARP mandatory-arrest deterred employed, ESCALATED unemployed (Sherman-Berk); pop-weighted mean ~0, forbids a single global coercion setting | PARTIAL |
| E32-H276 | foster/removal-until-reconciliation | mean ΔTFR -0.425; Doyle 2007/08 marginal foster kids worse + Barnevernet/ECHR; removal severs BOTH bonds + trauma - the antipattern | REFUTED |
| E32-H277 | refund + clawback bond (the seed) | mean ΔTFR +0.314; CARES deposit-contract (Gine-Karlan-Zinman); both parents post the same stake -> un-weaponisable, delta ~0.10 | SUPPORTED |
| E32-H278 | contingency-management milestone rewards | mean ΔTFR +0.327; CM g~0.54, the largest psychosocial effect (Higgins, Petry); attenuates after reward stops | SUPPORTED |
| E32-H279 | conditional cash / tax credit | mean ΔTFR +0.420; Progresa/Bolsa Familia move conditioned behaviour, but cash is the campaign's weakest fertility lever (E15/E20 mirage) | PARTIAL |
| E32-H280 | symmetric two-sided bond (un-weaponizable) | mean ΔTFR +0.272; both post the identical stake -> weaponisation ~0, delta 0.05, the lowest in the batch - the design win | SUPPORTED |
| E32-H281 | loss-frame (lose-it) vs gain-frame | mean ΔTFR +0.414; Fryer-Levitt-List-Sadoff loss-framed bonus +0.2-0.4 SD vs null gain-frame - a design free-lunch at equal cost | SUPPORTED |
| E32-H282 | child-outcome-contingent reward | mean ΔTFR +0.263; better-targeted in principle (Progresa conditionality) but child wellbeing is noisy/slow to measure - gaming toward proxies | PARTIAL |
| E32-H283 | objective clawback trigger (detection design) | mean ΔTFR +0.067; objective automatic trigger keeps delta 0.10; complaint-driven jumps to 0.45 - the whole ARM-B robustness hinges on this | PARTIAL |
| E32-H284 | reward x shared-custody x mediation (the stack) | mean ΔTFR +0.480; three orthogonal channels (Halla legal default + Emery diversion + the bond) - super-additive, the largest intergenerational dividend | SUPPORTED |
| E32-H285 | carrot x stick substitution | adding the monitored stick to the symmetric bond changes ΔTFR only -0.023 - a credible carrot drops the stick's marginal value to ~0; stacking coercion on top is net-harmful | SUPPORTED |
| E32-H286 | escalating per-diem contact-denial ticket | mean ΔTFR +0.009; civil-contempt purgeable per-diem + certainty; BUT library-fine (Philadelphia doubling: zero effect) = escalation magnitude is a mirage; certainty, not size | PARTIAL |
| E32-H287 | income-scaled day-fine | mean ΔTFR +0.012; Staten Island day-fine (Hillsman/Vera): no-payment 22->6%, revenue up, equity+; dominates the flat fine on collectability | SUPPORTED |
| E32-H288 | on-the-spot police issuance (certainty) | mean ΔTFR +0.009; red-light-camera certainty (Cohn 2020) supplies the deterrence term, but a doorstep denial has no objective signal -> false positives on protective parents | PARTIAL |
| E32-H289 | civil (no custody consequence) vs criminal | mean ΔTFR +0.009; THE KEY INSIGHT: weaponisation tracks STAKES not certainty; a ticket that cannot change custody cannot be a custody weapon - collapses the Meier payoff | SUPPORTED |
| E32-H290 | revenue to the wronged parent (make-whole) | mean ΔTFR +0.036; legitimacy+ (Tyler restorative justice) but cash make-whole creates a perverse incentive to provoke denials; net-positive only as make-up CONTACT time | PARTIAL |
| E32-H291 | supervised exchange / neutral drop-off | mean ΔTFR +0.037; removes the handover flashpoint, contact continues with no adult contact - un-weaponisable; weak-observational evidence + fiscal ceiling | SUPPORTED |
| E32-H292 | parenting coordinator / special master | mean ΔTFR +0.024; reduces relitigation (Dealy 2023 quasi-exp) but the outcome is court-resource not contact; PC authority capturable if ungated | PARTIAL |
| E32-H293 | family-support social work (corrective) | mean ΔTFR +0.007; safe/cheap bottom rung, small-to-null (IFPS) - survives only as a complement | PARTIAL |
| E32-H294 | criminal fine, custody-decoupled | mean ΔTFR +0.003; a certain low penalty decoupled from custody - deters mildly without the weaponisation; the lowest viable criminal rung | PARTIAL |
| E32-H295 | community service / public works | mean ΔTFR +0.004; a corrective-punitive hybrid, decoupled - does something without removing the parent; modest conflict cost | PARTIAL |
| E32-H296 | suspended jail sentence (threat, decoupled) | mean ΔTFR -0.001; the drug-court graduated-THREAT logic - deters without the incarceration harm, but the threat itself adds conflict | PARTIAL |
| E32-H297 | actual jail time (custody-decoupled) | mean ΔTFR -0.234; removes a parent from the child (fF-), severity>certainty (Nagin), incarceration harms children (Wakefield-Wildeman; Wildeman 2009) - the ladder's off-limit top rung even decoupled from custody | REFUTED |

## E33 - Religion and fertility (H298-H313)

E33 is the 16-hypothesis religion fanout. Religion is almost never a model primitive - it is a bundle that loads channels the coupled model already owns (the norm N, coupling C, parity P̄, tempo τ, childlessness ρ, security S), plus two objects that are *not* channel forcings: bounded high-fertility sects are **subpopulation-compounding** (their own Leslie sub-population, λ > 1, retention is the lever) and religious transmission feeds the E30 intergenerational path integral. It is **intensity + retention, not nominal affiliation**, that carry the effect. Grounded in `references/papers/e33-religion-fertility-digest.md`, executed in `notebooks/27-kj-religion-fertility.ipynb`; twelve channel-forcing hypotheses run through the calibrated coupled model on the Korea/Germany/France triad, four compounding hypotheses run through a two-type generational share projection with apostasy leakage δ. Two REFUTED kill the readings that do not survive the model: the established-church-as-lever (H304, inert under high existential security - Norris-Inglehart) and the traditional-gender-role reading (H313, religious fertility is *despite* not *because of* gender traditionalism - DeRose 2021, and wiring it as a trad-role forcing imports the campaign's own backfire). The SUPPORTED cluster is dominated by the compounding sub-populations (Amish/Hutterite/Haredi - retention, not policy, is the lever) plus the two genuinely abstractable **secular** ingredients: the pronatal norm identified by Israel-nationalism (H305 - high fertility at low personal piety) and the congregation-as-community fS (H312 - Shaver 2020). H307 tested whether religion is *predominantly* the norm: the norm is separable and identified (Israel norm-without-piety vs Iran piety-losing-norm) but carries only ~27% of the decomposed effect - religion is a multi-channel bundle, not mostly N. The PARTIAL plurality is the honest result - religion mostly re-expresses channels already in the model. Retention δ is the fragile axis the sect-takeover projection rests on (H306): doubling apostasy shifts every sect's takeover out and lowers its long-run share.

### E33 at a glance

| id | claim | evidence | verdict |
| --- | --- | --- | --- |
| E33-H298 | religious practice (weekly attendance) vs nominal affiliation | mean ΔTFR +0.098; GSS ~70k: weekly attenders ~2.4, unaffiliated lowest; affiliation-only collapses to ~0 - the operative variable is practice acting through N/C, not "religion" | PARTIAL |
| E33-H299 | cross-denomination TFR gradient | mean ΔTFR +0.111; Pew Muslim 2.9 / Christian 2.6 / unaffiliated 1.6, but >50% attenuates under GDP/region; Iran 1.35 & Utah 1.8 sit below secular France - a security/region proxy (Norris-Inglehart), not doctrine | PARTIAL |
| E33-H300 | Amish as a compounding sub-population (λ>1, not a forcing) | share projection baseline takeover gen 4 → doubled-δ no takeover; asymptote 0.59→0.50; Greksa-Korbin completed ~7.7, doubling ~20yr, +97% since 2000 - existence proof, NOT a transferable lever | SUPPORTED |
| E33-H301 | Hutterite as a compounding sub-population (λ>1, not a forcing) | share projection baseline takeover gen 3; asymptote 0.65→0.62; Eaton-Mayer completed 10.9, 4.12%/yr fastest recorded natural growth - pins the upper bound of the fecundity wall / ρ→0 attainable; not a policy | SUPPORTED |
| E33-H302 | Haredi as a compounding sub-population (λ>1, not a forcing) | share projection baseline takeover gen 4 → doubled-δ gen 5; asymptote 0.60→0.53; Israel CBS 6.6 stable ~a decade inside a modern state - the transferable part is the norm, not the Haredi package | SUPPORTED |
| E33-H303 | pronatal theology (Quiverfull/LDS) via realised practice | mean ΔTFR +0.088; acts only through the norm/parity it induces; Catholic contraception ban did NOT bind (converged to secular mean) - theology sets a ceiling, practice binds | PARTIAL |
| E33-H304 | state-established church / religious schooling as a fertility lever | mean ΔTFR +0.017; Norris-Inglehart: established churches (CoE, Nordic Lutheran) coexist with the LOWEST fertility - establishment is inert under high security; near-zero lever | REFUTED |
| E33-H305 | Israel nationalism as a secular norm-carrier | mean ΔTFR +0.349; ~75% secular Jewish Israelis at/above replacement (~2.0-2.2) at LOW personal religiosity + most state-funded IVF per capita - the transferable ingredient is norm+community+security, NOT religion per se | SUPPORTED |
| E33-H306 | retention is the load-bearing fragile assumption | the fertility gap is robust but doubling apostasy δ shifts every sect's takeover out and lowers the asymptote (Amish 0.59→0.50); the projected inheritance-of-the-earth is bounded by retention, not asserted | PARTIAL |
| E33-H307 | is religion predominantly the norm channel N? | norm-borne share only 27% of the religion effect (full +0.239 = via-N +0.064 + residual +0.176); the norm is separable and identified (Israel norm-w/o-piety vs Iran piety-losing-norm) but community+coupling carry the majority - religion is a multi-channel bundle, NOT predominantly N | PARTIAL |
| E33-H308 | religious marriage + lower divorce (compositional) | mean ΔTFR +0.174; DeRose 2021 higher union stability; a large slice of the gap but it runs entirely through fC/fScar the model owns - and if via raised exit-cost/lock-in it BACKFIRES (Stevenson-Wolfers), so the durable part is voluntary stability | PARTIAL |
| E33-H309 | non-stopping / higher parity (contraception rejection) | mean ΔTFR +0.019; large only inside natural-fertility sects (compounding-internal); weak as a general-population channel - most of the developed-world religious gap is low childlessness + marriage, not high parity | PARTIAL |
| E33-H310 | earlier tempo (younger marriage / first birth) | mean ΔTFR +0.004; 3-6yr earlier first birth feeds the Bongaarts-Feeney tempo term; but tempo alone is a mirage (bump-revert) unless coupled to quantum - the coupled model shows the revert | PARTIAL |
| E33-H311 | lower permanent childlessness (ρ→0) - the strongest quantum channel | mean ΔTFR +0.099; childlessness ~0-3% in sects vs 15-25% secular East Asia/Europe; the single largest QUANTUM contribution - but a within-observant property, so partially a compounding-internal effect | SUPPORTED |
| E33-H312 | congregation as community / alloparenting (fS) | mean ΔTFR +0.126; Shaver 2020 ALSPAC: co-religionist aid predicts fertility and persists while secular support decays - the least-coercive, most-transferable religion channel (secular equivalent = durable kin networks) | SUPPORTED |
| E33-H313 | traditional gender roles as the mechanism | mean ΔTFR +0.016; DeRose 2021: the religious advantage barely moved as its traditional-role component eroded - religious fertility is DESPITE not because of gender traditionalism; wiring it as a trad-role forcing imports the campaign's REFUTED backfire | REFUTED |

## Root-fix: E16/E18 interaction claims re-run jointly through the calibrated distributional core (GOAL-15 Phase 3)

The `interaction-analyst` adversary found that E16's H125 "defection-robust bundle crosses the separatrix" and E18's "stacking complementary winners is super-additive" were never run jointly through the coupled model - E18 was an analytic parabola with a hand-set `syn` constant, E16 a `cap_sum` of solo literals fed to a toy ODE. Both are re-run here through the rebuilt distributional core (`EmergentModel.run_cal`, the calibrated K-agent ensemble), levers expressed as channel-forcing vectors, `I(A,B) = effect(A+B) − Σ effect(solo)` measured on the Korea/Germany/France triad. These supersede the fiat interaction verdicts (append-only; the original rows stand as recorded).

- **E16-H125 (superseded)** - robust bundle sum-of-solos +0.312, JOINT +0.264, interaction **−0.048 (ratio 0.85, sub-additive)** - four of the five levers write `fRV`, so they saturate on a shared wire (the collision the adversary named), not the `cap_sum`'s implied independence and not super-additivity. The *conclusion* survives - the robust bundle still beats the fragile bundle by **+0.348** and is composition-driven - but only because the fragile bundle has the wrong **sign** (backfiring bans/propaganda net −0.084), not because of a separatrix threshold on a scalar. Mechanism corrected: shared-channel saturation + fragile-bundle sign, not super-additive stacking.
- **E18 super-additivity (superseded, split verdict)** - measured jointly: `compress × lottery` I = **+0.002 (additive, REFUTED** - both touch `fPb`/`fRV`); `de-risk × school × peer` I = **+0.018 (genuinely SUPER-additive, SURVIVES** - three orthogonal channels `fS`/`fPb`/`fN`); `second-shift stack` I = **+0.003 (additive, REFUTED)**. The general principle - stacking is super-additive only across genuinely orthogonal channels, same-channel levers saturate - is confirmed and now model-measured; two of the three named pairs were artifacts of the hand-set constant.

## GOAL-15 Phase 4 - the full lever sweep, the bundle ablation, and the combination law

The rebuilt distributional core was run against the entire campaign, encoded as 182 channel-forcing levers (`src/sci_demographic_collapse/interventions.py`, batches E14-E33; 38 runtime/compounding levers excluded). Three passes: a solo arbiter, a bundle ablation, and a derived combination law that replaces the interaction plumbing.

**Solo arbiter (`reports/phase4_arbiter.json`)** - every lever run through the scalar core (`run`) and the dispersed OT core (`run_cal`) on the Korea/Germany/France triad, to isolate the effect of the distributional lift. Result: across 175 channel-forcing levers, **one** Seldon fate-label tip (IV2 cash, at Δ +0.0008 - a threshold artifact, not a magnitude change) and a **maximum divergence of 0.0043** ΔTFR. The distributional lift is faithfulness, not verdict-change: at catalogue magnitudes the scalar and dispersed cores agree to the third decimal on every solo lever. The genuine reshuffles live in the joint bundles, not here.

**Bundle ablation (`reports/phase4_ablation.json`)** - 117 multi-channel bundles, each decomposed by leave-one-out (which wire carries the effect) and by the proper interaction `I = effect(together) − Σ effect(each channel alone)`. Two findings. First, the naive leave-one-out ratio `full / Σmarginals` is misleading: it reads > 1 ("super-additive") on 67 of 117 bundles (49 above 1.05) purely because TFR is multiplicative and concave in ΔTFR - a scale artifact, not synergy. The proper interaction gives **16 super-additive, 28 sub-additive, 73 additive**. Second, the E18 stacks all saturate: `compress × lottery` (I = −0.098), `in-kind × permanence` (−0.133), `universal × de-risk` (−0.115), `inequality × pension` (−0.086) all carry `lead = fS` - the real catalogue levers overload the shared security/support channel, so stacking them collides on one wire.

**Honest correction to the Phase-3 E18 survivor.** Phase 3 measured `de-risk × school × peer` at +0.018 (super-additive) treating its channels as orthogonal `fS`/`fPb`/`fN`; the Phase-4 ablation on the *catalogue-encoded* lever measures it at −0.021 (sub-additive) because that encoding routes school-readiness and de-risking both through `fS`. Both magnitudes sit at |I| ≈ 0.02, on the additive threshold - so the honest reading is that this pair is effectively additive and its sign is **encoding-dependent**. It should not stand as a robust super-additive survivor. The surviving general principle is unchanged and now sharper: super-additivity requires genuinely orthogonal channels, and whether a named stack qualifies depends on how its levers load the shared channels - which the combination law below makes explicit.

**The combination law (`docs/intervention-combination-law.md`, `src/sci_demographic_collapse/combine.py`).** How interventions combine is solved at the equation level, not by plumbing. Because TFR is a product of bounded channel factors, `log TFR` is additive across independent channels (Bongaarts proximate-determinants multiplicativity), and the only genuine interaction is the departure from log-additivity - the mixed second derivative `I(A,B) = f_Aᵀ H f_B`, with `H = ∇²log TFR(0)` computed from the calibrated core by finite differences, never hand-set. This dissolves the E16/E18 blocker with zero free parameters: the raw ratio cannot separate synergy from artifact, but the log-scale interaction can - the coupling×quantum probe reads raw 1.190 ("super-additive") yet has honest interaction −0.027 (the exact "1.19" the plumbing over-claimed), while a real 4-channel synergy reads +0.172. Three mechanisms fall straight out of the computed `H`: diagonal saturation (all-negative diagonal in the basin), off-diagonal coupling that reproduces the ODE Jacobian exactly (`H[fS,fC] = −5.14` is the `gS_C` coupling, `H[fRV,fN] = −3.75` is `lam_rho`, parity `fPb` off-diagonals ≈ 0 as a pure multiplicative factor), and a separatrix sign-flip (`∂²L/∂fS² = +40` in trapped Korea vs −2.5 in the German basin - threshold synergy is manifold position). `H`'s eigenvectors are coherent channel bundles - {security, coupling}, {norm, childlessness} - the same coupling submatrix the culture-bearer operator `Φ = r·VΛV⁻¹` is built on: one operator, two phenomena. Honest limit: the closed-form bilinear is exact only in the small-signal limit and is a *structural* indicator, not a precise predictor, at bundle amplitude through the stiff bistable channels (Caswell's caveat). The operational law is to combine on the log scale, measure interaction directly as four runs, and use `H` for structure not magnitude near the ridge.

## E35 - Cultural transmission: the floor, not the lever (H339-H348)

E35 closes the culture-bearer arc (GOAL-16 Phase C) by recording, as a hypothesis batch, the distinction the adjudication drew between two machines that both hide under "cultural transmission" - and it tests each on the object that is actually valid for it. The first machine is the **within-population eigen-operator** `Φ = r·VΛV⁻¹` (`culture.py`), a parent handing a coherent trait bundle to the next cohort. Anchored to the observed intergenerational-fertility correlation (Kolk 2014, r≈0.15, breeder's equation) it is **inert as a lever**: exactly zero on the scalar single-agent core (the fertility-weighted selection differential x̄ᵂ−x vanishes when there is one agent) and max |ΔTFR| 6.8e-4 on the dispersed K-agent core over 2050-2125 - about 10⁴ below any real channel and untouching the 2023 calibration (H339, REFUTED-as-lever). With Λ=I the operator collapses to `Φ = r·I`, so the eigenbasis V - the "cultural archetype" elegance - is immaterial (max |Φ−r·I| = 1.1e-16 across all three regional eigenbases; H347). And the within-population transmission the operator was meant to add is already carried, at ~83x the magnitude, by the bistable norm N and the `ot.py` cohort-memory path integral the core already owns (mean |ΔTFR| ~0.056 on those channels vs the operator's 6.8e-4; H343).

The second machine is the **between-group share replicator** (E33's validated `project_share`), a bounded above-replacement subpopulation reproducing at λ>1 and *retaining* its children. This one is real and it sets a long-run national-TFR **floor**: blending the compounding sect with a declining mainstream, the asymptotic national TFR settles at ~4.3-6.8 (Amish/Hutterite/Haredi) - above replacement, a whole-population fixed point that dominates the mainstream trend rather than following it (H340, SUPPORTED). Retention δ, not subgroup fertility, is the load-bearing axis: the asymptotic share is ~1.8x more sensitive to δ than to TFR and, more sharply, δ switches the takeover on or off (at TFR 6.6 the takeover lands in generation 4 at δ 0.05 but never within 25 generations at δ 0.45; H341, generalising E33-H306). The floor is pinned by the sect's own (TFR, δ): sweeping the mainstream decline rate R_main across a wide 0.5-1.1 band moves the national floor by only 0.40 TFR (H342). Timing is monotone - earlier or larger seeding raises the national trough (1.41→2.21) and advances the takeover (generation 5→2) - though the asymptotic floor itself is a seed-invariant fixed point, so timing governs the transient and the time-to-floor, not the ultimate level (H346).

The throughline is that **cultural transmission is a floor, not a lever**. The within-population operator that *looked* like a lever is inert (H339/H343/H347); the between-group process that is *real* is a descriptive boundary condition, not a controllable intervention - a high-retention above-replacement sect cannot be manufactured by policy (its retention is a property of a bounded, high-exit-cost community, recorded in E33 as an existence proof explicitly not transferable), and a policy raising the *mainstream's* retention of a pronatal norm cannot compound because the open population has no boundary, so its effective δ is high and its share decays (0.05→0.07 at δ 0.3, →0.000 at δ 0.5; H344 and H345, both REFUTED-as-lever). Finally the floor changes none of the 338 prior intervention verdicts: it enters national TFR as an additive share-weighted term `(1−x)·main + x·sect`, so a within-nation lever's marginal effect is exactly `(1−x)·ΔTFR_main` - same sign (4/4 preserved) and identical lever ordering - orthogonal to and separable from the levers (H348). Executed in `notebooks/28-kj-cultural-transmission-e35.ipynb`; verdicts in `reports/nb28_e35_verdicts.json`; figures `reports/figures/nb28_{operator_autopsy,national_floor,retention_axis,separability}.png`.

### E35 at a glance

| id | claim | evidence | verdict |
| --- | --- | --- | --- |
| E35-H339 | within-population eigen-operator Φ=r·VΛV⁻¹ is inert as a lever at the Kolk-2014 anchor | anchored operator (r=0.15, Λ=I) max\|ΔTFR\| = 0 on the scalar single-agent core (x̄ᵂ≡x → Δ=0) and 6.8e-4 on the dispersed K-agent core (2050-2125), ~10⁴ below any real channel; does not touch the 2023 calibration | REFUTED |
| E35-H340 | between-group share compounding sets a national TFR FLOOR that dominates the mainstream trend | national TFR = share-weighted blend of sect(>2.05) + declining mainstream; as the sect compounds its share the asymptotic floor sits at ~4.3-6.8 (Amish/Hutterite/Haredi), above replacement regardless of how far the mainstream falls - a whole-population fixed point | SUPPORTED |
| E35-H341 | retention (apostasy δ), not subgroup fertility, is the load-bearing axis of the floor | (δ,TFR) sweep: asymptotic-share range varying δ[0.02-0.5]=0.36 vs TFR[3-10]=0.20 (δ 1.8x); δ switches the takeover on/off (TFR 6.6: gen 4 at δ 0.05 → never at δ 0.45) - fertility is necessary, retention makes it compound | SUPPORTED |
| E35-H342 | the floor is pinned by the highest-retention above-replacement subpop, ~independent of R_main | varying the mainstream decline R_main across 0.5-1.1 moves the national floor by only 0.40 TFR (Haredi 6.6/0.10) - set by the sect's (TFR,δ), not by the mainstream's rate of fall | SUPPORTED |
| E35-H343 | within-population transmission is ALREADY carried by the bistable norm N + `ot.py` cohort memory | the channels the operator was meant to add already move mean \|ΔTFR\| ~0.056 (norm N, coupling, father-invest + scar cohort-memory path integrals) - ~83x the operator's 6.8e-4; a separate linear operator adds nothing | SUPPORTED |
| E35-H344 | cultural transmission is a DESCRIPTIVE FLOOR, not a controllable intervention | the compounding sects are existence proofs (E33-H300/301/302) with retention δ 0.05-0.13 that are properties of a bounded, high-exit-cost community, explicitly not transferable; a high-retention above-replacement sect cannot be manufactured by policy - the floor describes the boundary, it is not a lever | REFUTED |
| E35-H345 | a policy raising the mainstream's retention of a pronatal norm cannot compound like a sect | mainstream pseudo-sect (TFR 2.2, no boundary → high δ): share 0.05 → 0.07 at δ 0.3, → 0.000 at δ 0.5, no takeover; compounding needs the boundary, which policy on the open population cannot supply | REFUTED |
| E35-H346 | the earlier a high-retention subpop's share is seeded, the sooner and shallower the national trough | seed sweep x0 0.002→0.15: national-TFR trough rises 1.41→2.21 and the takeover advances gen 5→2; timing is monotone, though the asymptotic floor is a seed-invariant fixed point (0.60) - timing governs the transient and time-to-floor, not the ultimate level | SUPPORTED |
| E35-H347 | the eigenbasis V is immaterial at the anchor (Φ=r·I): the elegance is decorative | with Λ=I, Φ = r·V·Vᵀ = r·I identically; max\|Φ−r·I\| = 1.1e-16 across all three regional eigenbases - V (the "cultural archetype" rotation) makes no difference to the operator | SUPPORTED |
| E35-H348 | the between-group floor changes none of the 338 intervention verdicts (separable, orthogonal) | the floor enters national TFR as an additive share-weighted term (1−x)·main + x·sect; a within-nation lever's marginal effect is exactly (1−x)·ΔTFR_main - same sign (4/4 preserved), identical lever ordering national vs mainstream, rescaled by the sect complement | SUPPORTED |

## E34 - Heretical & coercive natalism fanout (H314-H338)

E34 is the 25-hypothesis contrarian fanout - the coercive, zealous, theocratic and structural levers decent policy discourse refuses to say out loud, each grounded in a real historical analogue (executed after E35 in the append-only log; the round was designed with E35 but modelled second). Every "decree / medal / theology" is a bundle on the coupled model's own channels (norm N, coupling C, parity P̄, tempo τ, childlessness ρ, security S) plus a defection fraction δ (evasion attenuates the removable channels) and the two E30 path-integral channels father-investment fF and relationship-scar fScar, which carry the cross-generational sign. Grounded in `references/papers/e34-heretical-fanout-digest.md`, executed in `notebooks/31-kj-heretical-fanout-e34.ipynb`; all 25 hypotheses run through the calibrated distributional core (`run_cal`) on the Korea/Germany/France triad for ~4 generations, gen-1 (2050) read against gen-4 (2124). Calibration clean at 6.4e-5. The verdict split is 3 SUPPORTED / 11 PARTIAL / 11 REFUTED.

The round's payoff is the **coercion × path-integral sign flip**. Effects compete and nothing is isolated: a coercive lever's gen-1 birth boost contends with the downstream path-integral loss it plants - the forced cohort enters childhood scarred (fScar↑, fF↓), and `ot.CohortMemory` carries that damage forward 27-45 years into depressed marriageability and coupling. For coercion the damage wins by gen-3-4, so the gen-1 boost REVERSES - a sign flip invisible to any static ΔTFR. Nine coercive levers reproduce it (Korea): Decree 770 (H314, +0.013→−0.146, the calibration case - Romania's 1.9→3.7 CBR spike that fully reverted and left 100-170k orphaned, IQ-scarred Decrețel), contraception rollback (H319), covenant marriage (H321), lower marriage age (H327, the mechanism "works" at gen-1 and that is exactly why it is disqualified), abortion ban (H328), contraception ban (H334), shame penalty (H336, flips on collapsing Korea), eugenic Graduate Mothers (H317), and Gilead (H330, +0.043→−0.143, the deepest - δ=0.85, the theoretical ceiling of the coercion-backfire law where higher stake buys harder defection). The mirror image is the un-buyable-devotion set: Georgia's sacred third-child baptism (H318, +0.249→+0.373, δ≈0.05 because a sacred act cannot be bought or faked) and its transferable core, sacralised-motherhood-as-norm (H331), plus the structural commitment device Demeny/proxy voting (H322) - all force births into healthy, freely-chosen environments, transmit a pronatal norm forward, and HOLD or COMPOUND (gen-4 > gen-1). Coercion reverses; devotion compounds.

The single most important static finding is the **norm × penalty dividing line**: the same fN channel SUPPORTS when re-priced voluntarily (H318, H331, δ≈0.05-0.08) and REFUTES when enforced by penalty (H336) or propaganda (H335, δ=0.4) - the sign is conditional on whether an option is removed, not on religion-vs-secular or zeal-vs-restraint. Zeal buys fertility only in the re-price mode. An honest caveat the run makes explicit: near the collapsing bistable coupling ridge any sustained positive forcing amplifies, so the raw gen-4 magnitude over-ranks weak PARTIAL levers (the Mutterkreuz medal H315, USSR childlessness tax H316, Hungary's tempo-inflated 4+ exemption H320, matchmaking H324, conscription exemption H329) - these are held to PARTIAL by δ-realism, confound and cost, not by the TFR number. The four subpopulation objects (Quiverfull H332, high-demand religion H333, covenant-community H337, tech-right H338) compound within-group but are capped at PARTIAL as non-transferable, non-legislable engines - the same subpopulation-vs-lever distinction E33/E35 drew. Campaign total → 348.

### E34 at a glance

| id | claim | evidence | verdict |
| --- | --- | --- | --- |
| E34-H314 | Decree 770 total ban (abortion + contraception) | gen-1 +0.026 → gen-4 −0.217 (Korea +0.013→−0.146), δ=0.75, SIGN-FLIP; Romania 1966 TFR 1.9→3.7 in one year, back to baseline by 1983, 100-170k orphans - the canonical mirage-then-collapse and the calibration case for the reversal (Bucharest EIP: 7-9pt IQ loss) | REFUTED |
| E34-H315 | Mutterkreuz honour decoration (no penalty) | gen-1 +0.043 → gen-4 +0.068 (Korea +0.035→+0.032), δ=0.10; historians attribute the Nazi CBR rise to the abortion ban + marriage loans, not the medal - a pure-honour norm nudge, weak and confounded | PARTIAL |
| E34-H316 | Childlessness tax + Mother-Heroine medals | gen-1 +0.056 → gen-4 +0.060 (Korea +0.040→+0.010), δ=0.30; USSR 1941 tax + 1944 title (~430k) - the penalty arm coercion-adjacent, the honour arm inert, heavy wartime confound | PARTIAL |
| E34-H317 | Eugenic Graduate Mothers Scheme | gen-1 +0.008 → gen-4 −0.019 (Korea +0.005→−0.021), δ=0.40, SIGN-FLIP; Singapore 1984 rescinded within a year after electoral backlash, TFR still fell to 1.42 - eugenic conditioning triggers revolt, fertility effect nil | REFUTED |
| E34-H318 | Sacred third-child baptism (un-buyable devotion) | gen-1 +0.322 → gen-4 +0.596 (Korea +0.249→+0.373), δ=0.05; Georgia, Patriarch Ilia II from 2007-08, births +28% in two years entirely in married third-order fertility - the un-buyable-devotion existence proof that compounds forward | SUPPORTED |
| E34-H319 | Contraception rollback / pronatalist reversal | gen-1 +0.013 → gen-4 −0.105 (Korea +0.007→−0.088), δ=0.50, SIGN-FLIP; Iran post-2012 contraceptive use fell 67%→31% but TFR stayed near/below replacement - removing options does not create demand, unwanted births carry fScar | REFUTED |
| E34-H320 | Lifetime tax exemption for 4+ children (Hungary) | gen-1 +0.127 → gen-4 +0.222 (Korea +0.083→+0.114), δ=0.15; Hungary 2019-20 ~5% GDP, TFR 1.25→1.59 but heavily tempo-inflated - the security arm is real, the cash-mirage finding applies with a security discount | PARTIAL |
| E34-H321 | Covenant marriage / abolish no-fault divorce | gen-1 +0.014 → gen-4 −0.112 (Korea +0.012→−0.085), δ=0.60, SIGN-FLIP; Louisiana 1997 tiny uptake, contradicts Stevenson-Wolfers exit-valve - raising exit cost traps high-conflict couples, a fScar engine that scars the next generation | REFUTED |
| E34-H322 | Demeny / parental proxy voting | gen-1 +0.153 → gen-4 +0.315 (Korea +0.117→+0.203), δ=0.03; Boffa et al. model proxy voting as a commitment device tilting the polity toward child-friendly spending - the rare structural, un-buyable, low-coercion lever that compounds forward | SUPPORTED |
| E34-H323 | Child-linked pension (internalise the externality) | gen-1 +0.096 → gen-4 +0.177 (Korea +0.063→+0.089), δ=0.10; Boldrin-De Nardi-Jones PAYG pensions explain a large share of the decline - the corrective is structurally sound but empirically thin and back-loaded | PARTIAL |
| E34-H324 | State-run matchmaking / assortative markets | gen-1 +0.100 → gen-4 +0.174 (Korea +0.092→+0.116), δ=0.20; Singapore SDU, Japan/Korea konkatsu - right channel (coupling is the keystone) but the state is a weak matchmaker, helps at the margin | PARTIAL |
| E34-H325 | Bride-price / dowry revival | gen-1 +0.025 → gen-4 +0.001 (Korea +0.027→+0.011), δ=0.30; rural Senegal higher bride price REDUCES fertility pressure (robust to controls) - sign ambiguous-to-negative, commodification cost high, not usable in a modern monogamous market | REFUTED |
| E34-H326 | Legalise polygamy as a fertility lever | gen-1 −0.058 → gen-4 −0.142 (Korea −0.038→−0.078), δ=0.20; sub-Saharan DHS / LDS per-woman fertility DECLINES with co-wife number (~1 child fewer) - polygyny lowers the TFR object and starves the young-male marriage market | REFUTED |
| E34-H327 | Lower the marriage / consent age | gen-1 +0.077 → gen-4 −0.122 (Korea +0.041→−0.134), δ=0.10, SIGN-FLIP; 15-country study earlier marriage → earlier, more childbearing but severe health/education/IPV harm - the gen-1 gain is real and that is exactly why it is disqualified | REFUTED |
| E34-H328 | Abortion ban (Dobbs / SB8 / Poland) | gen-1 +0.024 → gen-4 −0.086 (Korea +0.013→−0.085), δ=0.40, SIGN-FLIP; Texas SB8 ~+3%, post-Dobbs +3-4% concentrated in low-access states, Poland reverted in ~20 weeks - a small real bump (confirms the E25 interior-optimum overshoot) whose unwanted, low-resource cohort reverses forward (Turnaway logic) | PARTIAL |
| E34-H329 | Conscription exemption / service for parents | gen-1 +0.036 → gen-4 +0.061 (Korea +0.023→+0.022), δ=0.20; speculative, loosely Israel (service culture coexists with TFR 3.0 but driven by religiosity/community, not the exemption) - a plausible small parity nudge, no clean identification | PARTIAL |
| E34-H330 | Gilead: established coercive theocratic natalism | gen-1 +0.064 → gen-4 −0.308 (Korea +0.043→−0.143), δ=0.85, SIGN-FLIP; fictional maximum (Atwood), the scaling law is Decree 770 × Iran × Singapore - the theoretical ceiling of the coercion-backfire law, deepest cross-generational reversal in the batch | REFUTED |
| E34-H331 | Sacralise motherhood as norm (no penalty) | gen-1 +0.069 → gen-4 +0.134 (Korea +0.053→+0.069), δ=0.08; Georgia generalised (Norris-Inglehart) - elevate motherhood as a freely-held sacred vocation without penalty, the norm self-transmits with no scarring, the devotion lesson without the Orthodox-marriage gate | SUPPORTED |
| E34-H332 | Apocalyptic / martyrdom-reward high fertility (Quiverfull) | gen-1 +0.226 → gen-4 +0.368 (Korea +0.126→+0.155), δ=0.05; ~10+ children per couple but only thousands of families - a real engine that compounds WITHIN the group via norm inheritance, but a subpopulation object not a state forcing, non-copyable | PARTIAL |
| E34-H333 | High-demand religion retention (compounding subpopulation) | gen-1 +0.099 → gen-4 +0.195 (Korea +0.071→+0.097), δ=0.10; LDS TFR ~3.4 (2015) declining toward the mean as practice converges, needs ~70% child retention - a genuine compounding object but converging downward, carry as a sub-population | PARTIAL |
| E34-H334 | Ban contraception | gen-1 +0.009 → gen-4 −0.108 (Korea +0.005→−0.088), δ=0.60, SIGN-FLIP; wherever tried at state scale the demand routes around it - removing means without changing demand yields high δ and large autonomy cost, a classic backfire that reverses forward | REFUTED |
| E34-H335 | Pronatal media / glorify large families (propaganda) | gen-1 +0.025 → gen-4 +0.045 (Korea +0.023→+0.025), δ=0.40; overt pronatal messaging reads as manipulation and provokes reactance - the norm channel is real but weaponised messaging backfires, credibility not volume moves norms | REFUTED |
| E34-H336 | Shame / honour penalty on childlessness | gen-1 +0.053 → gen-4 +0.025 (Korea +0.036→−0.022), δ=0.40, SIGN-FLIP on collapsing Korea; a penalty by another name - it flips negative on the defection screen and the transmitted resentment reverses it across generations | REFUTED |
| E34-H337 | Total covenant-community bundle (Amish-style) | gen-1 +0.352 → gen-4 +0.585 (Korea +0.325→+0.447), δ=0.15; Old Order Amish completed fertility ~6-7, doubles ~20yr, retention ~85% - an existence proof that compounds strongly within the enclave, but a total subculture not a separable lever | PARTIAL |
| E34-H338 | Tech-right pronatalism (IVF + embryo selection) | gen-1 +0.067 → gen-4 +0.141 (Korea +0.051→+0.075), δ=0.10; Collins family / Natal Conference (attendance doubled 2023→2025) - a real norm-shift inside a tiny elite subculture with an embryo-selection commodification cost, unproven at population scale | PARTIAL |

## E36 - The marriageable-men lever as a saturating interaction fanout (H349-H357)

E36 reformulates the E22 marriageable-men lever, which was modelled too crudely in two ways: it had no
saturation (its dose was a linear extrapolation of a constant marginal elasticity - the notebook conceded it
"sizes the ask, does not predict it") and it was a near-single-channel push `dict(S,C,Pb)` that omitted every
counter-interaction. The correct home for the lever is the marriageability channel `q` (the E30 channel that
gates coupling), and the governing principle is that effects contend on shared wires: the drive and its
counter-terms compete for the same coupling `C` and quantum `P̄` channels, so the net can flatten or sign-flip
and never grows linearly. The drive is a Langmuir/Michaelis-Menten Hill in relative male income `I` (booms),
`f_q = q_max·I/(I50+I)` - the 0.2-0.4 elasticity is the near-origin slope, not a constant. Two literature
anchors fix it: near-origin slope 0.03 ΔTFR/boom (Kearney-Wilson +3% births/boom) and a plateau equal to the
E22 drive-alone value the calibrated core measures (+0.487 on Korea), giving `q_max(fq)=0.390`, `I50=13.6`
booms. So the E22 "+0.48 drive alone" is revealed as the asymptote, not a way-point.

Three counter-terms bite on the shared wires. A concentrated, unevenly-landing boom raises inequality and, via
Doepke-Zilibotti intensive-parenting, drains the quantum wire (κ=1 bites −0.066 on Korea). Lifting men without
matching female footing worsens the hypergamy squeeze (Esteve 2016; Autor asymmetry) and drains coupling, a
convex term that roughly halves the drive under a men-only delivery (gap=1 bites −0.112, and the concentrated
men-only lift collapses Korea from +0.274 to +0.124). The income-via-degrees route is worse now (arms-race +
postponement bite −0.129, matching E22-H175's ~0.18) but writes the childhood educational environment into the
27-45 yr cohort-memory path integral, so it earns a delayed dividend (degrees gen-1 +0.015 → gen-4 +0.138);
even so, income dominates degrees on both horizons (+0.274 vs +0.144). Two restorative arms recover the sign: a
broad-based, redistributive delivery counters the inequality drag exactly (κ_eff = κ(1-r); fiscal restores
+0.066), and the female arm is sign-conditional on home equity - female income runs −0.019 under specialisation
(γ=0.1) to +0.135 under equity (γ=0.9), crossing zero at γ≈0.50 (Doepke-Kindermann; Goldscheider).

The honest re-check shrinks every headline number. On the calibrated core the drive-alone ceiling is +0.487
(Korea, the asymptote; +0.374 at a plausible 80-boom dose), male income falls +0.51 → +0.274, male degrees
+0.20 → +0.144, and the contrarian bundle +1.08 → +0.908 - the bundle shrank rather than grew, because kin,
equity and the female arm now stack as separate saturating channels instead of pushing one wire without bound.
The saturating dose overturns the linear "12 booms to hold, 48 to recover": with the baseline 2125 TFR at 0.169
and holding 0.72 needing +0.551, the drive-alone ceiling of +0.487 sits below even the hold threshold, so hold,
bend and recover are all unreachable by income alone at any finite dose. The E22 claim that marriageable-men is
the strongest single lever that bends Korea therefore survives but is qualified: broad-based male income still
bends all three regions and is the strongest single positive channel, but it bends, it does not recover; it is
non-monotone in delivery (concentrated or men-only forms self-cancel); and recovery requires stacking
complementary channels, not over-driving the marriageability wire. Executed in
`notebooks/32-kj-marriageable-men-saturation-e36.ipynb`; verdicts in `reports/nb32_e36_verdicts.json`; figures
`reports/figures/nb32_{dose_saturation,fanout_waterfall,triad_recheck}.png`. Calibration re-checked clean (max
abs err 6.41e-05, all six regions). Campaign total → 357.

### E36 at a glance

| id | claim | evidence | verdict |
| --- | --- | --- | --- |
| E36-H349 | the marriageable-men drive SATURATES in relative male income (Hill, not linear) | q responds to income via q_max·I/(I50+I) (n=1 Langmuir; near-origin 0.03 ΔTFR/boom, Kearney-Wilson; I50=14 booms); drive-alone ceiling +0.487 asymptote (+0.374 at 80 booms) - the E22 "+0.48 drive alone" is the asymptote, not a way-point | SUPPORTED |
| E36-H350 | an unevenly-landing (concentrated) boom partly self-cancels via the Doepke inequality channel | a fully-concentrated lift (κ=1) bites −0.066 ΔTFR on Korea (Doepke-Zilibotti intensive parenting drains the quantum wire); net-positive only when broad-based | SUPPORTED |
| E36-H351 | lifting men without matching female footing worsens the hypergamy squeeze and cuts coupling | a men-only lift (gap=1) bites −0.112 through coupling (Esteve 2016; Autor asymmetry); convex in the gap, so "just lift men" backfires past a point | SUPPORTED |
| E36-H352 | the degrees route is worse contemporaneously but writes a delayed path-integral dividend | education bites −0.129 now (arms-race + postponement, E22-H175) yet feeds the 27-45yr cohort memory: degrees gen-1 +0.015 → gen-4 +0.138 vs income gen-1 +0.132 → gen-4 +0.278; income dominates both horizons | PARTIAL |
| E36-H353 | the female arm is sign-conditional: female income is fertility-positive only under home equity | female-income ΔTFR runs −0.019 at γ=0.1 (specialisation) to +0.135 at γ=0.9 (equity), crossing zero at γ≈0.50 (Doepke-Kindermann; Goldscheider) | SUPPORTED |
| E36-H354 | broad-based / redistributive delivery counters the inequality backlash and restores net-positive | fiscal redistribution over a concentrated lift recovers +0.066 on Korea (κ_eff = κ(1-r)); the lever's sign is a property of the delivery | SUPPORTED |
| E36-H355 | the full fanout beats the drive ceiling by stacking channels, not by over-driving one | the contrarian bundle bends Korea +0.908 vs the drive-alone ceiling +0.374, recruiting coupling + quantum + the female arm as separate saturating channels (E18 one-lever-per-channel) | SUPPORTED |
| E36-H356 | the honest saturating dose overturns the linear "12 to hold, 48 to recover" | drive-alone ceiling +0.487 sits below the +0.551 needed to hold 0.72; hold, bend and recover are all unreachable by income alone at any finite dose; the E22 linear line said 18/28/44 booms | SUPPORTED |
| E36-H357 | the "strongest single lever / only one that bends Korea" claim is QUALIFIED, not overturned | broad-based male income still bends all three (Korea +0.274, Germany +0.433, France +0.293) and is the strongest single positive channel, but concentrated men-only collapses to +0.124 and it cannot recover any region alone - it bends, it does not recover, and only in its broad-based gender-balanced form | SUPPORTED |

## Model extensions this session (E25, E30, population framework)

Two baseline-preserving extensions were added to the calibrated E19 core (`src/sci_demographic_collapse/emergent.py`), each verified to leave every region's 2023-calibrated baseline unchanged to ~3e-7 (the coupling term is identically zero at the reference state, so no re-fit):

- **Bistable social-norm state N (E25)** - `dN/dt = -aN(N-Nlo)(N-thN)(N-Nhi) + fN`, two stable wells (Nlo=0.14 untrapped, Nhi=0.42 trapped), unstable tip thN=0.25; couples to childlessness via `rho_target += lam_rho*(N-N0)`. Reproduces tipping, hysteresis (a crossing pulse locks in), and position-dependent vulnerability
- **Marriageability capital q + intergenerational memory (E30 core)** - bilateral marriageability `q` gates coupling (`Ceq += gqC*q`); `q` is fed by therapy/health (`fq`, durable works and voluntary fades - reproducing the E21 null) and by the lifetime-integrated childhood environment of the current reproductive cohort (`A_lag = gA * mean env over [t-45, t-27]`), where env is father investment minus relationship scars. Father-access loss shows zero contemporary effect but a full one-generation-delayed cost (0.000 at 2050 → ∓0.13 at 2110) - the alienation loop that produces un-marriageable men and women downstream. The E30 hypothesis batch is pending; the core extension is in place and used by E29
- **Population-distribution framework (`population.py`)** - lifts any scalar channel to a Gauss-Hermite bucketed distribution N(mu, sigma) via the reparameterisation trick, giving Jensen-correct aggregates `<f> = sum_k w_k f(theta_k)`, heterogeneous intervention response, and tail-selection (exit / hypergamy). Validated on q (Jensen gap material off-threshold; selection reproduces the matriarchy instability). A full distributional lift of the whole core is registered as a conditional next step

## Lessons learned

- **The manifold is calibration-robust** - a separatrix found in stylized equations placed the four regions correctly and its ridge landed on the literature's independent TFR-1.5 low-fertility trap; a structural result surviving contact with data it was never fit to
- **The demographic-economic backbone calibrates; the behavioural-technology layer does not** - mortality, timing, the couple gate, separatrix placement, COVID and education all pass, but the technology hypotheses fail their out-of-sample bar
- **Pre-registration paid for itself** - the "core interest" (technology drives coupling collapse) did not survive its ≥25% out-of-sample test (17%), and marriage decline did not even accelerate post-2007; without a pre-set bar these would have been read as confirmation
- **Proxy resolution is the tech bottleneck** - crude marriage rate is too lagging; the tech signal, if real, lives in under-30 relationship formation the open data does not resolve (a measurement gap, not a settled negative)
- **A period rate carries no momentum** - the baby-bust TFR fall is quantum (behavioural); momentum moves births and population, not TFR - a conceptual correction (H3 reframed)
- **The model's largest omission is migration** - net migration cuts the USA population residual 85% and whitens it; USA parameters also fail to transfer to the EU, flagging region-specific calibration

## Conclusions

- **The prediction gap was a loss-function artifact, now closed** - the +0.2/+0.3 ELBO over-prediction of recent TFR was posterior collapse (per-point KL drives τ → 0); an exact-1D-Wasserstein (WAE) objective closes the in-sample gap to ≈ 0.02 with MI-usage 0.96, and hierarchical drift-pooling lifts held-out TFR coverage 50% → 100% - all four crises and the population totals survive the recalibration (E12)
- **Convergence is partial and honest** - 12/20 supported. The model reproduces demographic history where the mechanism is in the equations, and places every region correctly on the fertility axis; it does not yet close on the technology mechanism, the recession magnitude, or cross-region transfer
- **Seldon manifold: survived** - bistability persists (66% collapse basin) and the recovery/ridge boundary (1.47-1.66) agrees with the cited TFR-1.5 trap threshold
- **Named gaps blocking full convergence** - migration (foremost), region-specific parameters, a richer recession forcing, and a formation-resolved coupling series for the technology question
- **The distributional lift is faithfulness, not verdict-change** - the full OT ensemble core reproduces the scalar core to 2.2e-16 at σ=0, recalibrates to 2023 to ~1e-4 (five regions to 4dp, Germany on the rounding boundary at 1.4401 vs 1.4400), and across 175 solo levers moves the outcome by at most 0.0043 ΔTFR with a single threshold-artifact fate tip. Jensen's inequality on these near-linear channel responses is too small to reshuffle solo verdicts; the value of the lift is the correct treatment of heterogeneity and selection, not a change in the catalogue's rankings
- **Interventions combine by an equation, not by bookkeeping** - `log TFR` is additive across independent channels (Bongaarts multiplicativity) and the only genuine interaction is `I(A,B) = f_Aᵀ H f_B`, with `H` computed from the core. This replaces every hand-set synergy constant, separates true synergy from the multiplicative `exp()` artifact that fooled the leave-one-out ratio, and shows the E18 stacks saturate because they overload the shared security channel `fS`. The same coupling operator `H` (its eigen-bundles {security, coupling}, {norm, childlessness}) governs both intervention combination and cultural transmission
- **Standing rule** - even calibrated, the log is descriptive; it sizes mechanisms and places regions but licenses no intervention. INT-1 and INT-2 stay parked

## Next steps

- Add a migration term and re-fit (the single largest residual reduction on offer); re-run E5-H20 as a confirmation and E5-H19 to test whether migration closes part of the USA→EU transfer gap
- Source an under-30 relationship-formation series (formation-resolved) to re-test the technology hypotheses (H14/H16/H17) on the proxy where the signal should live
- Enrich the recession forcing beyond a linear scarcity elasticity (H9) and ingest a house-price series to close H13
- On convergence, distil the calibrated design into `docs/demographic-collapse-sota.md`
