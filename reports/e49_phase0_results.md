# E49 Phase 0 - Data-Driven Discovery: Grounding and the Identifiability Gate

**The question of the round**: can the coupled fertility vector field be DISCOVERED from data
(SINDy / sparse regression) instead of hand-written? Phase 0 grounds the method and runs the
make-or-break synthetic-recovery gate (H441) that decides whether the round proceeds at all.

**Headline**: the gate PASSES - sparse regression recovers the shipped model's governing equations
to machine precision from clean abundant EXCITED data (7/7 channels, all 8 regions). But the pass
comes with a decisive asterisk that reframes the whole round: the binding constraint is not the
algorithm, it is EXCITATION. The real data we have - the 8 national baseline trajectories - freezes
the marriageability channel q entirely (0/8 regions move) and barely stirs the social norm N (median
range 0.009 across its 0.14-0.42 double-well). The double-well emergence term the analyst hand-wrote
is essentially invisible in baseline observation, and is also the single term the realistic
finite-difference pipeline loses first. Data-driven discovery of THIS system is possible in
principle and demonstrated on excited data; on baseline national data alone it is not.

## Grounding

Four open-access papers downloaded to `references/papers/` with structured digests:

- **SINDy** (Brunton, Proctor, Kutz 2016, PNAS 113(15):3932-3937, arXiv:1509.03580) - the core
  method: build a library Theta(X) of candidate terms, solve dX/dt = Theta(X)Xi by sparse
  regression (sequentially thresholded least squares, STLSQ)
- **Weak SINDy** (Messenger, Bortz 2021, SIAM MMS 19(3):1474-1497, arXiv:2005.04339) - the
  integral / Galerkin weak form that removes pointwise derivative estimation, the main noise
  amplifier - the noise-robust upgrade for H442
- **Ensemble-SINDy** (Fasel, Kutz, Brunton, Brunton 2022, Proc. R. Soc. A 478:20210904,
  arXiv:2111.10992) - bagging over data and library subsets for the low-data / high-noise limit,
  and the multi-trajectory pooling that grounds H444
- **Neural ODEs** (Chen et al. 2018, NeurIPS, arXiv:1806.07366) - the expressive-but-opaque
  alternative for the H448 accuracy-vs-interpretability comparison

`pysindy` (github.com/dynamicslab/pysindy) is the reference implementation and is installed in the
venv. The STLSQ used below is the transparent hand-rolled core; a `pysindy.STLSQ` cross-check
reproduces it exactly (below).

## H441 - the identifiability gate: PASS on clean excited data

`emergent.py` is a known 7-channel system (C, rv, Pb, tau, S, N, q), each channel a first-order
relaxation with region-specific offsets, plus the bistable social-norm cubic and two hinges (the
coupling well on C, the fecundity hinge max(tau-30,0) on rv). We generated the cleanest possible
recovery problem: 20,000 states sampled uniformly across the operating box, EXACT analytic
derivatives (no finite-difference error), forcing off and the two latent population couplings
(dep_pen from the age pyramid, A_lag from cohort memory) set to zero, so the system is autonomous
save for an explicit calendar-time drift supplied as a known control. The library is a full
quadratic in the 7 channels (35 cross-term distractors) plus the specific nonlinear basis the true
model uses (N^3, the two hinges) and time. STLSQ must find the true sparse subset and reject the 35
distractors.

**Result: 7/7 channels recovered in all 8 regions, to machine precision.** Coefficients match the
true values at relative error ~0 (e.g. Korea dC: C -0.08000, S +0.07200, q +0.07200, Cwell -0.05000,
tn -0.00560 - each exact). The double-well cubic is recovered exactly (dN: N^3 -2.500, N^2 +2.025,
N -0.497, const +0.0368). Zero spurious terms - all 35 quadratic distractors correctly rejected.

**pysindy cross-check**: `pysindy.STLSQ` with a degree-3 `PolynomialLibrary` recovers the same dN
cubic (N^3 -2.5000, N^2 +2.0250, N -0.4970, const +0.0367) to four decimals, confirming the pass is
the method's, not the hand-rolled scoring's.

A single global STLSQ threshold initially failed the linear channels while passing the cubic - an
artifact of the channels' wildly different derivative scales (the childlessness channel rv has rate
constant 0.03, so its true derivatives sit near 0.01). Scaling the regression target to unit
variance per channel - standard practice - put every channel on equal footing and gave the clean
7/7. This is worth recording: naive SINDy on multi-scale demographic channels needs per-channel
normalization or it silently drops the slow channels.

## The decisive asterisk - excitation, not the algorithm, is the floor

H441 passes because the sampled data EXCITES every channel. The data we actually have does not. An
audit of the 8 national baseline trajectories (`run_cal`, 102 years) measured how far each channel
travels:

- **q (marriageability)**: frozen at exactly 0 in all 8 regions - zero excitation. On baseline the
  memory input is proportional to q itself, so q that starts at 0 stays at 0. Its dynamics are
  formally unidentifiable from baseline data
- **N (social norm)**: median range 0.009 across regions, and only that much because the ensemble
  disperses it - the representative norm barely leaves its well. The double-well curvature spanning
  N in [0.14, 0.42] is invisible in a 0.009-wide arc
- **C, Pb, tau, S**: move meaningfully (ranges 0.16, 0.12, 1.1, 0.12) - identifiable
- **rv**: range 0.03 - marginal

The scientific point: a channel sitting at a fixed point carries no information about its own
dynamics, and no length of series recovers a term the data never exercises. Excitation comes from
perturbation or forcing (interventions). So the data-efficiency claims below are quantified on
EXCITED (perturbed-initial-condition) trajectories - the best case - and the baseline data sits
below that floor for q and N. This is also a direct preview of H450 (the emergence test): the
hand-written double-well is doing load-bearing work that baseline observation cannot supply.

## H443/H444/H445 - the data-efficiency spine (the market-research payoff)

Because H441 passed, we ran the transferable core on the realistic pipeline: integrate
perturbed-IC trajectories, sample annually, estimate derivatives by centered FINITE DIFFERENCE
(dt = 1 year, the real annual-sampling error), then STLSQ. Finite differences cap recovery below the
exact-derivative ceiling.

**H443 - data-sufficiency surface** (median channels recovered / 7 over Korea, Germany, France):

| trajectories | L=10 | L=25 | L=50 | L=100 |
|---|---|---|---|---|
| 1 | 0 | 1 | 1 | 1 |
| 2 | 2 | 4 | 4 | 2 |
| 4 | 2 | 4 | 4 | 4 |
| 8 | 4 | 4 | 4 | 5 |
| 16 | 4 | 5 | 5 | 5 |
| 32 | 5 | 4 | 5 | 5 |

The message is clean: BREADTH beats LENGTH. Number of trajectories (diverse initial conditions =
diverse excitation) drives recovery; series length saturates by ~25 years because a relaxation
reaches equilibrium and stops exciting. A single trajectory of any length recovers at most 1/7 - one
relaxation path is too collinear to identify a coupled field. Roughly 8-16 excited trajectories are
needed to reach 5/7 under realistic finite-difference noise. The pipeline plateaus at 5-6/7, not
7/7: the consistent casualty is N (the double-well cubic), whose curvature the annual-sampling
derivative cannot resolve to tolerance, with the coupling channel C the second to fall. The linear
relaxations survive realistic noise; the nonlinear emergence structure is the fragile one.

**H444 - multi-trajectory pooling: decisive.** Pooling the 8 regions as trajectories of ONE shared
system (shared slopes, per-region constant via demeaning) against fitting each region alone with the
same short series:

| points/region | single region alone | pooled 8 regions |
|---|---|---|
| L=8 | 0/7 | 4/7 |
| L=12 | 0/7 | 6/7 |
| L=20 | 0/7 | 4/7 |

A single short relaxation recovers nothing (0/7); pooling eight of them recovers 4-6 of 7 channels.
This is the market-research thesis made concrete: when series share dynamics, the field is
identifiable from many short series where no single series suffices. The slopes are physically shared
(same rate constants across regions), so pooling is not a trick - it is the correct model.

**H445 - few-shot transfer.** Discover the shared slopes on 7 regions, fix the 8th region's
constants from only its first 10 years, integrate forward 60 years, and compare per-channel
normalized forecast RMSE against persistence and 10-year linear extrapolation:

- Discovered field beats BOTH baselines in **6 of 8 regions** (e.g. Germany 1.25 vs persist 1.69 vs
  linear 5.59; Japan 1.16 vs 1.79 vs 2.22)
- **USA** loses narrowly to persistence (1.996 vs 1.676)
- **Israel** BLOWS UP (RMSE 19.2) - the sole above-replacement, untrapped region. Transferring a
  field learned on seven trapped low-fertility regions to the one out-of-regime region is
  unstable - a clean preview of the H449 degeneracy failure mode, honestly reported

Two caveats bound H445. First, the forecast target is the real `run_cal` series, which includes the
latent dep_pen age-pyramid feedback the discovered autonomous field omits - so the discovered field
captures the behavioral relaxation but not the demographic feedback, a structural ceiling on
pure-behavioral-channel discovery (and part of why the win over persistence is modest, ~30%).
Second, all normalized RMSEs exceed 1 because these are large 60-year relaxations; "best of a hard
lot" is the honest description, not "solved".

## Verdict and what it means for the round

- **H441 (gate): PASS.** The field is recoverable from clean abundant excited data - 7/7 channels,
  all regions, machine precision, cross-confirmed by pysindy. Data-driven discovery is on the table
  for this system
- **The real constraint is excitation, not the algorithm.** Baseline national data freezes q (0/8)
  and barely moves N; those terms - crucially the double-well emergence structure - are
  unidentifiable from baseline observation regardless of series length
- **Data-efficiency (H443/444/445): supported with honest limits.** Breadth beats length; pooling
  shared-dynamics series recovers a field no single series can (0/7 to 6/7); few-shot transfer beats
  naive baselines in 6/8 regions but destabilizes on the out-of-regime region and is capped by the
  omitted latent coupling
- **Emergence is the fragile term** (preview of H450): the hand-written double-well is exactly what
  survives clean recovery but dies first under realistic derivative noise and is invisible in
  baseline data - evidence the hand-written structure supplies something the available data cannot

The round is NOT stopped by an identifiability floor - the method works. It is bounded instead by
DATA EXCITATION, which is a sharper and more useful finding: discovery of national fertility dynamics
needs perturbed / forced observations (natural experiments, interventions, cross-country pooling),
not longer baseline series. That is the honest bridge to Act II and the transferable market-research
corollary: capture a system's dynamics from many short, VARIED series - not one long quiet one.

## Artifacts

- `scratchpad/toy_e49_h441.py` - the identifiability gate (exact-derivative STLSQ, per-channel scoring)
- `scratchpad/toy_e49_baseline_audit.py` - the real-data excitation audit
- `scratchpad/toy_e49_dataeff.py` - H443/H444/H445 realistic finite-difference pipeline
- `scratchpad/e49_h441_results.json`, `e49_baseline_audit.json`, `e49_dataeff_results.json` - results
- `references/papers/[paper digest] *.md` - SINDy, Weak SINDy, Ensemble-SINDy, Neural ODE digests
