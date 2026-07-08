# Demographic Collapse - SOTA Model

**Canonical SOTA Document**

The distilled, calibrated design that survived the full E1-E35 campaign - 348 pre-registered
hypotheses across thirty-five rounds. It is an age-structured cohort-component (Leslie) core of national
populations, wrapped in a seven-channel coupled behavioural layer whose baseline reproduces each region's
real 2023 fertility, calibrated by an information-preserving Wasserstein objective, backtested
out-of-sample, stress-tested against four historical crises, and used to size, rank and ablate the entire
intervention catalogue over four generations. The full evidence trail is in
[the experiments log](experiments/demographic-collapse-experiments.md); the executable record is Notebooks
3-28 and the core modules `src/sci_demographic_collapse/coremodel.py` (Leslie) and `emergent.py` (the
coupled behavioural × Leslie model, the judge every intervention is scored on).

## Overview

The project began as a stylized nine-state ODE (Notebook 1) and a scalar calibration (Notebook 2). Those
established the qualitative picture - a bistable "Seldon manifold" whose ridge lands on the literature's
TFR-1.5 low-fertility trap - but a scalar state cannot carry an age pyramid, so population momentum had to
be reframed rather than reproduced (E1-H3). The SOTA fixes that on two levels. The demographic core is an
age-vector Leslie operator driven by observed schedules; it reproduces the accounting exactly, separates
recoverable postponement from real fertility loss, states its own uncertainty, predicts unseen years, and
reproduces four crises. On top of it sits a behavioural layer that says *why* fertility moves: TFR is the
emergent product of coupled, observable channels, each with its own dynamics, and every intervention in the
campaign is judged by integrating that coupled system multiple generations forward rather than by reading a
static curve. The central question the project set out to answer is settled: low fertility sets the
destination, but age structure and momentum govern the timing and depth of the decline, and where a region
sits on the manifold decides whether a maximal effort reverses its trend or merely softens its fall.

## The model

The demographic state is two age vectors, female and male, `Nᶠ, Nᵐ ∈ ℝ¹⁰¹` over single years 0-100+
(thousands). One year is a linear operator - the **Leslie map** - a weighted directed graph with a Markov
aging backbone and a fertility renewal edge:

- **Aging** - `N′ₐ = Nₐ₋₁ · Sₐ` for ages 1-99, the open interval at 100+ accumulating; `Sₐ` the
  life-table survival ratio (`Sₐ = L(a)/L(a-1)`, `S₀ = L₀/l₀` for birth → age 0)
- **Births** - `B = Σₐ fₐ · Nᶠₐ` over ages 15-49, `fₐ` the per-woman age-specific fertility rate; newborns
  enter age 0 split by the sex ratio at birth and the birth-survival `S₀`
- **Deaths** - the closed-population identity `D = (ΣN + B) − ΣN′`
- **Migration** - net migrants added by a Rogers-Castro age schedule (a labour-force peak plus a childhood
  echo), scaled to the annual net-migration total

The eigenstructure carries the long-run fate directly: the dominant eigenvalue λ₁ is the intrinsic growth
rate (r = ln λ₁), its eigenvector the stable pyramid. Across the study regions λ₁ orders monotonically by
fertility, all below 1 - every region is sub-replacement, USA highest (0.992), Korea lowest (0.970,
r = −3.1%/yr) (E6-H23). Momentum, the growth built into a non-stationary pyramid, is the Keyfitz ratio from
that eigenvector, and it is finite and depleting: the USA slid from 1.09 in 1990 to 0.98 in 2023 while
Japan (0.72) and Korea (0.81) sit deep in negative momentum (E6-H22). Driven by observed schedules, the
one-step operator reproduces annual births to 0.17% and deaths to 0.00% (E6-H21); Rogers-Castro migration
closes the USA total to 0.06% MAPE and beats an age-uniform allocation at the labour ages (E7-H24).

### The seven behavioural channels

The Leslie core answers what a fertility schedule does to a population; it does not say why fertility
moves. The behavioural layer (`emergent.py`, calibrated in E19) supplies that: fertility is the product of
coupled, observable states, each with first-order dynamics adapted from the nine-state ODE. Seven channels
carry the whole campaign:

- **C - coupling** - the share pairing into lasting, child-bearing unions; a soft-bistable state with a
  ceiling `C_thr = 0.66` and a trap
- **ρ - childlessness** - the extensive margin, permanent non-parenthood
- **P̄ - parity** - the intensive margin, completed children per mother
- **τ - tempo** - mean age at childbearing, the timing state
- **S - economic security** - the affordability/precarity state, coupled to the age pyramid through a
  dependency→security feedback
- **N - social norm** - a bistable double-well contagion (the share endorsing a childfree ideal), added in
  E25
- **q - marriageability** - a bilateral capital that gates coupling, fed by health/therapy and by the
  lifetime-integrated childhood environment of the current reproductive cohort, added in E30

Period fertility is their multiplicative composition with a Bongaarts-Feeney tempo term:

$$\text{TFR} = C\,(1-\rho)\,\bar P\,\text{fec}(\tau)\,(1 - k_{BF}\,\Delta\tau)$$

with `fec(τ)` a fecundability decay above age 30 and `k_BF = 0.6`. The multiplicative form is the whole
reason the combination law below is clean: on the log scale the channels are additive (Bongaarts
proximate-determinants multiplicativity). The completed-fertility quantum is `C·(1−ρ)·P̄`; the tempo term
makes a pure timing lever spike then revert - a mirage that borrows births from the future and changes no
completed family (E19).

### The bistable coupling trap

Coupling `C` sits in a soft-bistable potential whose separatrix lands on the empirical TFR-1.5 ridge. This
is the Seldon manifold, and it survived calibration: a structure found in stylized equations placed all six
regions correctly, its recovery/collapse boundary bracketing the EU-USA gap (1.47-1.66) and agreeing with
the independently cited Lutz-Skirbekk-Testa low-fertility-trap threshold of 1.5 ± 0.2 (E2-H8, E13-C14).
Position on the manifold, not fertility magnitude alone, decides an intervention's fate: the same lever
recovers near-ridge France, bends mid-basin Germany, and only softens deep-basin Korea (E19, E20-H169).

### The social-norm double well

The norm state `N` is not a passive parameter but a contagion with memory:

$$\frac{dN}{dt} = -a_N (N-N_{lo})(N-\theta_N)(N-N_{hi}) + f_N(t), \qquad \rho_{target}\mathrel{+}=\lambda_\rho (N-N_0)$$

with two stable wells (untrapped `N_lo = 0.14`, trapped `N_hi = 0.42`) split by an unstable tip
`θ_N = 0.25`. A push that crosses the tip **locks in** - the hysteresis that makes a norm shift a one-way
street. The consequence is asymmetric: on a coupling-limited country a pronatal push barely moves TFR, but
a modest stigma push tips an untrapped country *down* by ≈0.13 far more easily than any pronatal campaign
lifts a trapped one (E25-H187). It is a confirmed mechanism and a defensive vulnerability, not a strong
pronatal lever.

### The distributional (optimal-transport) core

A representative-agent scalar hides two things that decide outcomes near a threshold: the Jensen gap (a
heterogeneous population near a nonlinearity behaves unlike its mean - a trapped population's coupling runs
66% above the mean prediction because its upper tail crosses) and selection (a cutoff that truncates or
reweights a distribution tail, which a scalar cannot express). The production core (`run_cal`) is therefore
a K-agent ensemble carrying the full joint state `(C, ρ, P̄, τ, S, N, q)`, spread by a grounded structural
heterogeneity per channel, aggregated Jensen-correctly, and evolved with exact one-dimensional optimal
transport - the same Wasserstein machinery that closed the calibration gap in E12, here carrying each
channel as a quantile function (`ot.py`, `flow.py`). It reproduces the scalar core to machine epsilon
(2.2e-16) at zero dispersion, and it is the object every intervention is scored on. Its honest verdict:
across 175 catalogue levers the distributional lift moves solo outcomes by at most 0.0043 TFR versus the
scalar core (one threshold-artifact fate tip). On these near-linear channel responses the lift is
*faithfulness* - the correct treatment of heterogeneity and selection, which the matriarchy exit-and-
hypergamy analysis (E29) genuinely required - not a re-ranking of the catalogue.

## Calibration

A falling period TFR mixes recoverable timing and structural loss, and the model must tell them apart. The
**Bongaarts-Feeney** decomposition `adjTFR = TFR/(1 − r)`, `r` the rate of rise of mean age at childbearing,
splits the observed rate into recoverable **tempo** and structural **quantum** (E8-H26). The result reframes
the collapse country by country: the USA's low period TFR is largely tempo - its quantum sits near or above
replacement - whereas Korea's is a genuine quantum deficit (E8-H27). A two-parameter skew-normal at the mean
age scaled to the quantum reconstructs the single-year ASFR to within 3% of its peak (E8-H28), a
low-dimensional interpretable driver.

That driver was calibrated by minimizing a free energy. The first attempt (variational, `F = −ELBO`, Pyro
SVI) failed instructively - **posterior collapse**: the per-point Kullback-Leibler penalty drove the
innovation scale τ → 0, flattening the trend so the median over-predicted recent TFR by +0.2 to +0.3
(E12-H40). The fix replaces the per-point KL with a penalty on the *aggregate* posterior only - a
Wasserstein Auto-Encoder / InfoVAE(α=1) objective that preserves latent-data mutual information. A three-way
tournament (ELBO vs RBF-MMD vs exact one-dimensional Wasserstein-2) picks the optimal-transport penalty: it
closes the in-sample 2023 gap to ≈0.018 with MI-usage restored 0.04 → 0.96 and a 2023 population residual of
0.69%, beating both MMD and the ELBO (E12-H41/H42), and hierarchical drift-pooling lifts held-out TFR
coverage 50% → 100% (E12-H43). The behavioural baseline is calibrated to real 2023 TFR for all six regions
(USA, France, Germany, Italy, Japan, Korea) to under 1e-4 - max residual 6.4e-5, Germany at the fourth-
decimal rounding boundary - with every channel's coupling term identically zero at the reference state, so
each 2023 baseline is a fixed point and no lever perturbs history. The baseline reproduces reality region by
region: Korea collapses alone, no region recovers spontaneously (E19). That is what licenses the model to
act as the judge of an intervention.

## What the model reproduces

**Backtest** - trained on 1990-2015 and asked to predict 2016-2023, the population forecast holds
everywhere (MAPE ≤ 1%). Period-TFR *point* forecasts cannot anticipate a post-2015 regime change - an
intrinsic limit of any period-rate forecast - but the recalibration handles it honestly by widening the
band to cover the held-out TFR 100% (E9-H30, E12-H43). The sharper lesson stands: **population is
point-predictable, period TFR is only interval-predictable**, because momentum and age structure, not this
year's rate, govern the medium term.

**Crisis battery** - four historical crises are reproduced and their demographic cost measured by
counterfactual (E10): COVID-19 as a *mortality* shock (985k modelled excess deaths over 2020-21, real ≈1M,
with a recoverable tempo dip); the 2008 recession as *postponement that never recovered* (≈2.8M births
forgone); Korea's 1997 IMF crisis as a *permanent quantum step* (≈3.15M forgone); German reunification in the
national aggregate (≈0.72M forgone). The tempo-quantum lens is what makes the distinction crisp - a
recoverable postponement told apart from a permanent loss - and it is the same axis that decides whether an
intervention can work. All four survive the Wasserstein recalibration by sign (E12-H44). A 25-hypothesis
contrarian audit (E13) then attacked every finding: the age model crushes a persistence baseline, the
Rogers-Castro shape genuinely matters, the eigenvalue tracks TFR, and intervention timing is decisive - while
the fertility-forecast and USA-tempo claims were honestly *qualified* (the USA quantum is itself eroding; its
recent trajectory is migration-led).

## The drivers of collapse

- **Momentum governs timing and depth** - the answer to the project's central question. Low fertility sets
  the destination; the age pyramid sets when and how steeply a population reaches it. It is why the USA and
  Korea, both sub-replacement, sit on utterly different trajectories, and why the near term is unmovable -
  97% of Korea's 2050 births come from women already alive in 2023 (E13-C13)
- **The coupling keystone** - the quantum deficit dominates the 2100 decline (Korea 28M of a 32M loss),
  migration a strong second (14M), momentum a small irreducible lock (4M), recoverable tempo least (3M)
  (E14-H49). Within quantum, the binding margin for Germany, Italy and Japan is *extensive* - nearly three
  in ten women never having a child - so the missing births are missing mothers, the coupling keystone, not
  missing third children; Korea alone is a quantum-collapse special case (E15). Raising parity works only
  where coupling is intact (Germany 1.44 → ~1.95) and is gated where coupling has collapsed (Korea) - the
  keystone is emergent, not assumed (E19)
- **The bistable norm trap and the separatrix** - the coupling potential is bistable and its ridge is the
  TFR-1.5 trap; a country in the basin cannot recover spontaneously, and only levers that rebuild coupling
  cross the separatrix (7 of 88 single levers achieve a coupling-escape on Korea; the rest bend or stall)
  (E19)
- **Position and timing decide fate** - reversal is a property of position, not effort. A serious state-and-
  culture bundle plus migration returns the tempo-recoverable USA to growth (+129%), but the same maximal
  effort only bends ultra-low Korea from a 63% collapse to a 10% decline by 2100, because its reproductive
  base is already hollowed out (E14-H47/H48). Earlier is worth roughly twice as much: the same keystone
  compounds when started in 2025 and is largely wasted a generation late (E19, E20-H167)

Held at current fertility the ultra-low societies roughly halve by 2100 - Korea −63%, Japan −52%, Italy
−39% - while the USA is buffered near flat (+6%) by migration (E11-H37). The collapse is not a distant risk;
it is locked into today's age structure.

## The winning levers

Every surviving lever was put through the mandatory three-stage protocol - analytical decomposition with
literature effect sizes, multi-generation simulation on the Korea/Germany/France triad, and a leave-one-out
ablation for its improvement-per-composite-cost - and then screened for defection (the net a society gets is
the gross times the compliant share, plus a backfire term that can invert the sign when the rich defect) and
for stacked side effects. The levers below are the SUPPORTED survivors, grouped by the throughlines the
campaign found. Each carries its mechanism and its honest caveat. Magnitudes are model ΔTFR on the triad;
the model sizes a lever, it does not prove a policy achieves it.

### 1. Marriageable men - income, not degrees (the strongest single lever)

Raising non-college men's earnings and employment is the strongest causal lever in the campaign and the
*only* single lever that bends deep-basin Korea (+0.48). Two natural experiments agree - the Autor-Dorn-Hanson
China shock cut fertility 6.1/1,000 and marriage 4.2pt, Kearney-Wilson fracking raised births ~3% with
marriage flat - giving an elasticity ~0.2-0.4 (E22-H170). The education paradox sharpens it: raising male
*income* bends Korea +0.51 while pushing male *degrees* returns only +0.20, because the university arms-race
and postponement eat ~0.18 of the gain - the efficient move is income off the university track, not the
credential war (E22-H175). The contrarian bundle male income + kin-proximity + gender-equity-in-the-home
bends Korea +1.08, five-fold the naive "push degrees, hand out cash" bundle (E22-H176). **Caveat**: it raises
births more than marriage (partly non-marital); the required dose is a measurable mountain - ~12 fracking-
booms of sustained male-earnings gain just to *hold* Korea's 0.72, ~48 to *recover* to 1.5.

### 2. Gender equity in the home - the Doepke root lever

Equalising the domestic second shift is the strongest *durable* quantum lever and the root the arms-race
runs on: inequality drives intensive parenting, which suppresses fertility (Doepke-Kindermann). Female
earnings, fertility-suppressing under the old specialisation regime, flip *positive* under gender equity in
the home - the FLFP-fertility correlation itself flipped positive by the 2000s (E22 lessons, E15). **Caveat**:
this is both/and - raise his wage *and* lower her time-cost - not a retreat to traditional roles, which the
campaign repeatedly found backfires (E26-H207, E33-H313).

### 3. In-kind support beats eroding cash (geometry over magnitude)

Universal in-kind childcare is the strongest welfare lever in its batch (+0.127), a durable P̄+S geometry
that equivalent cash does not match (E25-H185, E26-H196 +0.097). The cleanest natural experiment is the
kibbutz: socialising the marginal cost of a child held above-average fertility, and privatisation cut
lifetime fertility 0.65 - the channel is *cost*, not communalism (E26-H194). The delivery axes are the
finding, not the magnitude: universal beats a means-test cliff, in-kind beats eroding cash, credible
permanence beats a policy believed temporary, national beats a local bonus that only relocates births, and
state funding beats an employer mandate that triggers hiring discrimination against young women (E17). A
quarter of the coupling premium is affordability, so pairing is itself an economic lever (E17). **Caveat**:
cash transfers are the campaign's weakest fertility lever - a mirage on the cost axis (efficiency 0.01),
Korea's USD 270B over two decades the proof (E15, E20-H166).

### 4. The commitment-insurance / exit machinery - safely-gated shared custody

A rebuttable shared-custody presumption is the load-bearing exit-machinery lever and carries the one clean
causal fertility estimate in the space: Halla (2013) found staggered US joint-custody reforms raised marital
fertility 8-14%. It caps the male downside of dissolution and raises willingness to commit - channel C
(E24-H180 +0.241, E31-H261 +0.323). Designed *with* a domestic-violence carve-out it keeps the fertility gain
and zeroes the scar - Spain's safety-gated joint custody saw intimate-partner violence fall ~45% (E31-H268
+0.258). Early mediation preserves contact and feeds the delayed dividend (E31-H267 +0.111); the prevention-
over-punishment bundle (shared-custody default + mediation + co-parenting education + carve-out + a
weaponisation screen, *excluding* criminalisation) is super-additive (E31-H270 +0.409). **Caveat**: it is
marriage-centred and the model lacks a marital-share gate, so France is likely overstated; punishment is
conflict - fines, criminalisation and forced reunification are refuted, because they feed the scar channel
and hand an abuser a weapon against a protective parent (E31-H263/H264/H265). The wider principle -
**the exit is the valve** - is that de-risking the stressors that dissolve unions works, while raising the
cost of leaving backfires (no-fault divorce cut female suicide up to ~20%), so lock-in, covenant marriage
and adultery penalties remove the bargaining that de-escalates (E17).

### 5. The carrot beats the stick, and stakes drive weaponisation

Across the alienation-combat toolkit the carrot dominates the stick on every axis: a symmetric two-sided
bond where both parents post the identical stake is un-weaponisable, with the lowest defection in the batch
(δ 0.05) (E32-H280, H277 +0.314), a loss-framed reward beats a gain-framed one at equal cost (E32-H281),
and contingency-management milestone rewards are the largest psychosocial effect (E32-H278). A credible
carrot drops the stick's marginal value to ~0 (E32-H285). The key mechanism: **weaponisation tracks stakes,
not certainty** - a civil ticket at the same certainty as criminalisation is safe because it cannot become a
custody weapon (E32-H289), where criminalisation is refuted (E32-H274). The reward × shared-custody ×
mediation stack is the largest intergenerational dividend in the campaign (E32-H284 +0.480). **Caveat**: cash
make-whole to the wronged parent creates a perverse incentive to provoke denials (net-positive only as
make-up *contact* time); jail is the off-limit top rung even decoupled from custody, because it removes a
parent from the child (E32-H297 −0.234).

### 6. Marriageability and the two-generation dividend

Durable population-scale therapy/health clears the voluntary-program null (Building Strong Families /
Supporting Healthy Marriage / Army-PREP all faded) because it works through *marriageability* q - a channel
the relationship-repair trials never touched (E30-H247 +0.140); a voluntary one-off program still fades
(E30-H248). The intergenerational path integral gives father-access loss a zero contemporary effect but a
delayed cost that *compounds* over the horizon (0.000 at 2050 → −0.19 by 2124) - an alienation spiral that
produces un-marriageable men and women a generation downstream (E30-H250/H251). It also turns shared
custody, paternity certainty and therapy into levers with a second, delayed dividend through the child
cohort (E30-H253/H254). **Caveat**: cash cannot buy marriageability - it moves security, not q (E30-H259);
and the whole channel only shows up on a multi-generation horizon, so a single-generation ledger misprices
every structural lever (E30-H260).

### 7. The cheap harbingers - coupling nudges near the ridge

The best improvement-per-cost lever is near-free: cohabitation legal recognition (efficiency 2.47 at cost
0.09, +0.22 TFR) tops all twelve harbingers (E20-H164). A full recovery bundle ablates to a lean three-lever
core - inequality-compression + gender-equity + legal recognition - that keeps the full +1.28 TFR gain at
roughly a quarter of the cost, and coupling is non-ablatable (E20-H165/H166). Anti-atomisation and kin
proximity are cheap coupling nudges (E22-H173, E25-H186, E26-H192). **Caveat**: harbingers are cheap
*coupling* nudges, not big fiscal levers, and they are position-specific - the same near-free lever bends
Korea and recovers France, its efficiency climbing toward the ridge (E20-H169).

### 8. The un-buyable incentive geometry

Where a lever moves an arms-race prize, only an un-buyable design survives defection: a lottery-band that
makes the admission prize un-buyable, or a multi-dimensional test rewarding un-coachable traits, deflate the
race at its source, while an outright tutoring ban backfires (the rich buy covert tutoring and inequality
widens - Korea 1980) (E16). The defection screen drops bans, propaganda, wealth caps and exhortation below
zero and lifts inequality compression, lottery bucketing, universal motherhood-penalty removal and
structural defaults to the top - what a state can *enforce*, not what sounds strong, bends the curve. The
Western natural experiments anchor the pattern: Israel's near-universal default plus universal IVF holds
even secular fertility near replacement without coercion, Hungary's 5-6% of GDP buys mostly tempo, and
housing's real lever is supply for young renters, not a price subsidy to owners (E16).

### 9. The transferable secular ingredients of religion, and enforced monogamy

Religion is almost never a model primitive - it is a bundle that loads channels the model already owns, and
it is *intensity and retention, not nominal affiliation*, that carry the effect (E33-H298). Two genuinely
transferable *secular* ingredients survive: a pronatal norm without piety (Israel's ~75% secular Jews at or
above replacement at low religiosity, E33-H305 +0.349) and congregation-as-community support fS (co-
religionist aid predicts fertility and persists where secular support decays; secular equivalent = durable
kin networks, E33-H312 +0.126); low permanent childlessness ρ→0 is the largest single quantum contribution
but is a within-observant property, partly compounding-internal (E33-H311). Separately, in the developed
regime state suppression of polygyny - *enforced monogamy* - is fertility-and-stability-favouring (the
Henrich WEIRD dividend, +0.698), because it reverses the excluded-male externality on coupling; the sign
flips only in low-development settings (E28-H213/H216). **Caveat**: religious union stability helps only as
*voluntary* stability - if it runs through raised exit-cost/lock-in it backfires (E33-H308); traditional
gender roles are refuted as the mechanism, religious fertility being *despite* not because of them
(E33-H313); every exotic structure tested to raise fertility by concentrating or rearranging mating -
polygyny, polyandry, matriliny, matriarchy, polyamory - was dominated once its excluded-sex, autonomy and
crime side-effects were priced (E26-E29).

### Migration - a bridge, not a cure

Migration is the biggest single raw lever (mean +115pp population) but it leaves coupling C unmoved - it
buys time, it does not cure, and it is a one-time bridge (E19, E14). For the USA, fertility still out-pulls
migration as a 2100 lever (E13-C8/C11).

## How interventions combine

How multi-lever bundles compose is solved at the equation level, not by bookkeeping. Because TFR is a
product of bounded channel factors, `log TFR` is additive across independent channels (the same
multiplicativity Bongaarts built the proximate-determinants model on), so the honest combination law is
addition in log-TFR plus a single interaction - the mixed second derivative of the response,

$$L(f)=L(0)+\sum_a\big[L(f_a)-L(0)\big]+\sum_{a<b} f_a^\top H\, f_b, \qquad H=\nabla^2\log\text{TFR}(0)$$

with `H` read straight off the calibrated core by finite differences, never hand-set (`combine.py`,
`docs/intervention-combination-law.md`). `I(A,B) = f_Aᵀ H f_B > 0` is synergy, `< 0` saturation, `= 0`
independence - Caswell's exact reading of the mixed partial of a matrix-population growth rate. This
dissolves the E16/E18 "super-additive" blocker with zero free parameters. The raw leave-one-out ratio
`full/Σmarginals` reads > 1 on 67 of 117 bundles purely because `exp()` is convex - a scale artifact, not
synergy; the log-scale interaction separates the two exactly (the coupling×quantum probe reads raw 1.190 yet
has honest interaction −0.027, while a genuine four-channel synergy reads +0.172). Three mechanisms fall
straight out of the computed `H`: an all-negative diagonal in the basin is same-channel saturation (why
stacks that overload the shared security wire collide), the off-diagonal reproduces the ODE coupling
Jacobian exactly (`H[fS,fC] = −5.14` is the security→coupling link, parity `fPb` off-diagonals ≈ 0 as a pure
multiplicative factor), and the diagonal flips *positive* in trapped Korea (`∂²L/∂fS² = +40` vs −2.5 in the
German basin) - threshold synergy is manifold position, not a hand-tuned bonus. The operational rule: combine
on the log scale, measure the interaction directly as four runs, and use `H` for structure not magnitude
near the ridge, where the closed-form bilinear is only a structural indicator (Caswell's caveat). The
earlier E16/E18 "super-additive stacking" claims were artifacts of hand-set constants: re-run jointly, the
E16 robust bundle is sub-additive (four levers write one wire and saturate; it still beats the fragile
bundle only because the fragile bundle backfires) and two of E18's three named super-additive pairs are
additive - super-additivity requires genuinely orthogonal channels, same-channel levers saturate.

## Culture is a floor, not a lever

The slowest force in the story - the handing-down of a way of living from parents to children - is not a
lever, and proving that cleanly was GOAL-16 (E35). Two machines hide under "cultural transmission", and only
one is real. The **within-population eigen-operator** `Φ = r·VΛV⁻¹` - culture as a matrix bending each
family's trait vector toward its dominant eigenvector - was built and, anchored to the measured
intergenerational-fertility correlation (Kolk 2014, r ≈ 0.15), it moved national TFR by at most 6.8e-4 (~10⁴
below any real channel) and, at that anchor with Λ=I, collapsed to plain scalar multiplication `Φ = r·I`
(the eigenbasis V immaterial to 1e-16) - the wrong object, retired (E35-H339/H343/H347). The transmission it
was meant to add is already carried, ~83× stronger, by the bistable norm N and the cohort-memory path
integral the core already owns.

What actually compounds is **between-group**, not within: a bounded, above-replacement, high-retention
subpopulation reproducing at λ > 1 out-*has* a sub-replacement mainstream and grows its population share
every generation, until its fertility sets the national floor the whole population decays toward - settling
at ~4.3-6.8 over four generations for the Amish/Hutterite/Haredi (E33's validated share replicator,
E35-H340). Two facts govern it: **retention (apostasy rate), not subgroup fertility, is the load-bearing
axis** - the asymptotic share is ~1.8× more sensitive to δ than to TFR, and δ switches the takeover on or
off (E35-H341); and it is **descriptive, not a policy dial** - a bounded high-retention community cannot be
legislated into existence, and a policy raising the *mainstream's* retention of a pronatal norm cannot
compound because the open population has no boundary (E35-H344/H345). The floor is orthogonal to the lever
set: it enters national TFR as an additive share-weighted term, so a within-nation lever's marginal effect
is exactly `(1−x)·ΔTFR_main` - same sign and identical ordering, changing none of the prior verdicts
(E35-H348). Culture is therefore excluded from the levers and treated as the slow attractor they operate
above.

## The two pruned elegances

Two mathematically attractive constructs were built, tested honestly, and cut - the discipline the whole
project runs on is that elegance must move the numbers.

- **The culture-bearer eigen-operator** (`Φ = r·VΛV⁻¹`, E35) - inert at 4e-4 to 6.8e-4 TFR and, at its own
  measured anchor, degenerate to `r·I`, so its eigenbasis was decorative. It was the wrong object for
  cultural transmission and is retired to the project history
- **The quantile-flow core lift** (`flow.py`) - the planned distributional-core representation that carries
  every channel as a monotone quantile function unifying reparameterisation, optimal transport and gradient
  flow in one differentiable object. Evaluated as a full-core lift it moved TFR by ≤ 4.65e-4 - ~1000× below
  the signal of any real channel - because the premise (that population heterogeneity re-ranks the catalogue
  through Jensen curvature) is refuted by the data: the channel responses are too near-linear at catalogue
  magnitudes (E29 lessons, the E19 faithfulness result). The OT machinery it shares with `ot.py` still earns
  its place where selection is genuine (the matriarchy tail operations, E29), but the general core lift did
  not

## Honest limitations

- **Period, not cohort fertility** - the model works in period TFR; period-rate point forecasts cannot
  anticipate regime changes, so trust the population trajectory and the credible band, not a single TFR
  number (the recalibration made the band honest, held-out coverage 100%)
- **A structural indicator near the ridge** - the behavioural layer is a deliberately simplified, roughly
  tuned research instrument, good for ranking forces and comparing the *shape* of levers, not a precision
  predictor; the combination law's bilinear form is exact only in the small-signal limit and only structural
  at bundle amplitude through the stiff bistable channels
- **Migration held at zero for the behavioural runs** - the demographic core carries a canonical
  Rogers-Castro schedule (not a fitted one), and the buffered cases (USA, Germany) rest on elevated recent
  net migration; the intervention runs isolate the fertility channels with migration off
- **No joint (multivariate) channel distributions** - the distributional core disperses each channel
  marginally; a full joint law is a registered next step
- **The culture floor is descriptive** - it is a boundary condition, not a controllable lever, and it rests
  on retention values that are properties of bounded communities, not policy dials
- **National aggregate, descriptive not causal** - sub-national divergence (East/West Germany) is
  unresolved, USA parameters do not transfer to the EU without a region-specific offset, and even calibrated
  the model sizes mechanisms and places regions - it licenses no claim that a given policy achieves a given
  lever

## Reproducibility

- **Core modules** - `coremodel.py` (Leslie map, momentum, eigenstructure, Rogers-Castro, counterfactuals),
  `emergent.py` (the seven-channel coupled behavioural × Leslie model, the judge), `ot.py` / `flow.py`
  (one-dimensional optimal transport, cohort memory), `population.py` (Gauss-Hermite distributional lift),
  `combine.py` (the combination law), `interventions.py` (the 182-lever channel-forcing catalogue)
- **Notebooks** - `03`-`08` the age-structured core, tempo-quantum, Bayesian and Wasserstein calibration,
  the crisis battery and the contrarian audit; `09`-`13` the reversal catalogue and the E14-E18 intervention
  rounds; `14` the dynamical re-examination (the model as judge); `15` the harbinger ablation; `16`-`27` the
  structural / exit-machinery / norms / alternative-structure / religion rounds; `28` the cultural-
  transmission close (E35). All execute end-to-end on the pinned GPU
- **Data** - `data/raw/unwpp/` (UN WPP 2024, CC BY 3.0 IGO) plus the World Bank / Eurostat / OWID
  behavioural panel; provenance in `data/raw/README.md` and the per-source manifests
- **Numbers** - `reports/nb7_parameter_table.csv` (recalibrated per-region parameters), `nb7_predictions.csv`
  (2023 residuals), `nb5_crisis_costs.csv`, `nb6_projection_table.csv` (2100 baseline and interventions),
  `phase4_arbiter.json` / `phase4_ablation.json` / `combine_verification.json` (the solo sweep, bundle
  ablation and combination law), the per-notebook `nb*_verdicts.json`, and the figures in `reports/figures/`
- **Decision-maker view** - a star-ranked intervention table with mechanism-of-effect chains and side
  effects is regenerated on demand via `/write-interventions`; the source library is `references/papers/`
  (48 PDFs + 72 digests)
