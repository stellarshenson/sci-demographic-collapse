# E51 Decline-Bias Root-Cause Hypothesis Fanout (Pre-Registered)

Pre-registered hypotheses H464-H470 for the E51 root-cause round, attacking the CAUSES of the decline
bias (DEF-1/2/3/4/6) rather than the recuperation symptom (DEF-5, promotion-DECLINED at E50). Every
hypothesis is stated with its defect-vs-feature NULL: the null is that the down-drift / ratchet /
antinatal-only well is the model correctly encoding decline, so that removing it makes the E41 2000-2023
backtest WORSE. The governing rule is Occam / "elegance must move the numbers": a fix is KEPT only if it
IMPROVES the backtest (fewer sign-misses AND lower chi2/dof on the recoveries) WITHOUT (a) breaking the
2023 calibration (each region's year-1 TFR reproduces REAL to < 5e-4 after re-solving PB_SCALE_ENS),
(b) letting Korea spuriously recover (R2: model 2019 within 0.15 of 0.918 AND path falls 2015-2019), or
(c) wrecking the recorded guard suite (13/13 in `tests/test_hypothesis_guards.py`) and the 463 recorded
verdicts. If it cannot clear those, the honest verdict is REFUTED-AS-DEFECT - the "defect" was a feature.

Every change is additive or sign-symmetrising and baseline-preserving (identically the shipped core when
its new coefficient is off), verified bit-for-bit in `scratchpad/toy_bias_harness.py` (worst per-channel
`_estep_vec` diff 0.0 with all toggles off).

## Ranking summary

| rank | H | defect | fix under test | toy verdict-so-far | Occam default |
|---|---|---|---|---|---|
| 1 | H464 | DEF-1 | zero / sign-symmetrise the secular drift | FEATURE: zeroing 3.68 -> 8.39 chi2/dof; fit wants drift 3.6-14x STRONGER-down | REFUTED-AS-DEFECT |
| 2 | H468 | DEF-6 | two-child parity bistable multiplier | MOVES recovery RMSE 0.124->0.062 but chi2 3.68->4.26, BREAKS calibration (0.020), wrong-signs decliners | REMOVE (non-selective, calibration-breaking) |
| 3 | H466 | DEF-3 | pronatal tri-well (+ Israel anchor) | INERT on hindcast (norm frozen at its well); forward-durability only | REFUTED-AS-DEFECT for backtest |
| 4 | H467 | DEF-4 | recovery-velocity refit, Israel held out | SUBSUMED: no restoring term, refit only redistributes residuals | REMOVE (downstream of DEF-5) |
| 5 | H465 | DEF-2 | signed dependency dividend | INERT: bit-near-identical in an aging window (max delta 6.8e-4) | REFUTED-AS-DEFECT (forward note) |
| - | H469 | joint | DEF-1+2+3+6 together + interactions | dominated by DEF-1 damage x DEF-6 over-lift | REMOVE |
| - | H470 | meta | the real gap is per-region recuperation, not symmetrisation | constructive pointer to a future DEF-4 x DEF-5 round | direction for next round |

**Make-or-break single fix: H464 (DEF-1).** It is the only defect the backtest directly adjudicates (the
secular constants are fit parameters), so it decides the whole defect-vs-feature question. If the data
wanted less down-drift, the fit would say so; it says the opposite. Run H464 first; the rest follow.

---

## H464 - DEF-1: the secular down-drift is a feature, not a glide-path artifact

**Claim (fix under test).** The four secular constants all point down (secC 0.0007, secPb 0.0010,
secTau 0.006, secS 0.0010); zeroing or sign-symmetrising them removes a built-in glide path and should
not worsen - and might improve - the backtest.

**Null (defect-is-feature).** The down-drift on the quantum channels is the model correctly encoding the
secular fertility decline; the WLS fit, free to choose, sets it STRONGER-down, so removing it makes the
fit worse.

**Exact emergent.py change.** Set `secC = secPb = secTau = secS = 0` in `PARAMS` (lines 148-159); or
widen the backtest fit bounds to admit up-drift (`secC in [-0.01, 0.01]`, `secPb in [-0.02, 0.02]`,
`secTau in [-0.06, 0.06]`, add `secS in [-0.01, 0.01]`) and refit. No dynamics rewrite - the terms are
already present; only their values / bounds change.

**Pre-registered pass bar.** KEEP iff zeroing or the sign-free refit lowers backtest chi2/dof below the
baseline 3.68 AND does not raise R1 sign-misses, with calibration preserved (< 5e-4 after re-solve) and
Korea R2 intact. REFUTED-AS-DEFECT iff zeroing raises chi2/dof or the free fit still selects positive
(down) secC/secPb.

**Prediction (CONFIRMED).** REFUTED-AS-DEFECT. Zeroing raises chi2/dof to 8.4; the free-bounds fit keeps
all four secular terms down (two on their down-rails). The down-drift is correctly-fit signal.

**Honest-negative branch.** If the free fit selects negative (up) secC/secPb and lowers chi2, DEF-1 is a
real defect and the shipped down-drift is over-fit; escalate to a signed-secular shipped change with full
blast-radius re-measure.

**Occam gate.** A monotone drift cannot produce the interior trough-then-rise of a recovery for any sign,
so DEF-1 is the wrong lever for the missed recoveries regardless; keep only if it independently lowers
chi2 (predicted: it does not).

**Toy evidence (measured this round).** Zero-secular chi2/dof 8.39 vs baseline 3.68 (2.3x worse);
standard-bounds refit drives secC 0.0007 -> 0.0025, secPb 0.0010 -> 0.011-0.014, secTau 0.006 -> 0.0. The
free-bounds refit (up-drift allowed) selects secC=0.010 and secS=0.010 (both pinned to the maximum-DOWN
rail), secPb=0.012, secTau=0.019 - NOT ONE term up - and even improves chi2/dof to 3.22 while making the
recoveries WORSE (recovery RMSE 0.124 -> 0.265, all 8 regions turn net-negative, R1 -> the 4 recovery
misses). The down-drift is demanded by the data; NULL (feature) confirmed decisively.

---

## H465 - DEF-2: the signed dependency dividend is inert on the backtest

**Claim.** `dep_pen = dep_fb*max(dep-dep0, 0)` clips the recovery branch; replacing the clip with the
signed `dep_fb*(dep-dep0)` restores a symmetric dependency dividend and should let a younging pyramid
tail-wind fertility.

**Null (defect-is-feature/inert).** Over any historical window the pyramid only ages, so the clip is
never active on its beneficial side; the signed and clipped forms are numerically identical on the gate.

**Exact emergent.py change.** Drop the `max(., 0)` at the three `dep_pen` sites (:390, :542, :718) and in
the backtest runner: `dep_pen = dep_fb*(dep - dep0)`.

**Pre-registered pass bar.** KEEP iff the signed dividend changes backtest chi2/dof or a recorded verdict.
REFUTED-AS-DEFECT iff it is bit-near-identical on the aging backtest window (the demographic-dividend
tailwind requires a pyramid reversal that no region shows in-sample).

**Prediction.** REFUTED-AS-DEFECT (inert). Max series delta 6.8e-4, calibration and Korea untouched.

**Honest-negative branch.** Retain only as a documented FORWARD-run symmetry note: activate if a future
intervention run is shown to reverse a pyramid (the demographic dividend is a multi-decade window - Lee &
Mason 2006), where the clip WOULD suppress a genuine dividend.

**Occam gate.** Zero backtest movement -> not shipped now.

**Toy evidence (measured).** Signed vs clipped max backtest-series delta 6.8e-4 (transient migrant dip in
USA/Israel only). At the refit optimum: chi2/dof 3.684 (= baseline), recovery RMSE 0.124 (= baseline),
calibration drift 6e-5 pre-resolve / 1e-6 post - bit-near-identical, NULL (inert) confirmed.

---

## H466 - DEF-3: the pronatal tri-well is inert on the hindcast (forward-durability only)

**Claim.** The norm double-well is antinatal-only; a third stable well near N~0.02 (anchored to
Israel/Haredi) gives a pronatal norm a place to lock in and should let the durable half of a recovery
express, and improve Israel's fit.

**Null (defect-is-feature/inert).** Regions start snapped to their well, so N is a frozen fixed point on
the hindcast (nothing forces it); a third well changes the potential but not the frozen state, so it moves
no backtest number.

**Exact emergent.py change.** Replace the cubic `dN = -aN*(N-Nlo)*(N-thN)*(N-Nhi) + fN` (:284/:518/:580)
with the quintic tri-well `dN = -aN*cN*(N-Npro)*(N-tip_pro)*(N-Nlo)*(N-thN)*(N-Nhi) + fN`, new PARAMS
`Npro=0.02`, `tip_pro=0.08`, `cN` chosen so the mid-well fixed point stays EXACTLY at NORM0 (the toy's
imperfect cN leaked 8e-3 - the shipped version must pin the mid-well). Optionally re-anchor NORM0[Israel]
to Npro (only coherent WITH the third well).

**Pre-registered pass bar (two-part).** (a) BACKTEST: KEEP iff Israel's R1 sign-miss resolves or its
rms_std_resid (1.18-1.5) drops. (b) FORWARD-DURABILITY: KEEP iff a recorded norm-lever durability verdict
flips (a pronatal push that currently fades now locks in - an E25/E38/E43/E44/E45 verdict changes for a
documented reason), with the blast radius on the 463 verdicts measured. REFUTED-AS-DEFECT for the backtest
iff N stays frozen and the series is unchanged.

**Prediction.** Backtest REFUTED-AS-DEFECT (Israel net +0.005 ~ baseline +0.008, frozen); forward-
durability is the only place it can earn keep and is DEFERRED to a norm-lever re-run (not adjudicable by
the hindcast).

**Honest-negative branch.** If the forward norm-lever re-run shows no durability verdict flips, the third
well is decorative and REMOVED by Occam despite its empirical realism.

**Occam gate.** The pronatal well and the DEF-6 parity multiplier encode the SAME social-contagion
mechanism at two layers; ship at most one (prefer the norm layer). Do not add both.

**Toy evidence (measured).** Tri-well backtest-series delta < 8e-3 (curvature leak, not a recovery force);
Israel re-anchor WITHOUT the tri-well makes Israel worse (0.02 is not a fixed point of the cubic:
net -0.023); WITH the tri-well Israel sits still (net +0.005). At the refit optimum: chi2/dof 3.681 (=
baseline 3.684), recovery RMSE 0.124, Korea 0.828 (falls); calibration drift 3.1e-3 pre-resolve (above the
5e-4 guard - the mid-well leak), 1e-6 after re-solve. Backtest NULL (inert) confirmed.

---

## H467 - DEF-4: recovery-velocity refit holding Israel out (subsumed probe)

**Claim.** The rate constants (kC, decl, gS_C, kTau) were fit on 7 collapsing regions; Israel is a placed
point, never a recovery-velocity constraint. Refitting with Israel as a rising-trajectory constraint may
reveal mis-set recovery constants.

**Null (subsumed).** Without a restoring term the system cannot rise for any rate constants; refitting only
redistributes residuals, and Israel (C0=0.97, above the coupling trap) barely constrains the trap
constants, so the fit is near-invariant to holding it in or out.

**Exact change (probe, no shipped edit).** Refit {kC, decl, gS_C, kTau} on all 8 regions vs the 7
non-Israel regions; compare the constant shifts and the resulting Israel backtest fit.

**Pre-registered pass bar.** KEEP / escalate iff a rate constant shifts materially (> 20%) when Israel is
admitted AND that shift lowers the recovery chi2. SUBSUMED iff the shifts are small and Israel's fit does
not improve without a restoring term.

**Prediction.** SUBSUMED. Small constant shifts; Israel's rise cannot be reproduced by a down-only system
regardless of rate calibration. DEF-4's real content is the DEF-5 pointer (per-region recuperation).

**Honest-negative branch.** If admitting Israel materially moves kC/decl/gS_C, re-open the E19 dynamics
calibration as a separate identifiability round.

**Occam gate.** Not an independent shipped change; a diagnostic that either points to DEF-5 or dissolves.

**Toy evidence (measured, CONFIRMED SUBSUMED).** Refit {kC, decl, gS_C, kTau} all-8 vs hold-Israel-out:
kC, decl, gS_C bit-identical in and out; only kTau shifts 0.00095 (~1.7%). Israel as a velocity
constraint moves nothing material.

---

## H468 - DEF-6: the two-child parity multiplier moves the numbers non-selectively (confound)

**Claim.** Parity Pb and security S are thin linear scalars while the lowering channels are rich and
nonlinear; a two-child bistable multiplier on parity (symmetric to the norm well) lets recovery cascade.

**Null (non-discriminating confound).** The collapsing regions sit below the tip and never cascade; the
apparent lift is the double-well restoring force near the low well being weaker than the linear
relaxation - a quantum-softener that raises decliners and recoverers ALIKE and is re-absorbed by the
secular refit, double-counting DEF-3's contagion signal.

**Exact emergent.py change.** Replace linear `dPb = kPb*(PB0 + gPb*fPb - secPb*100*tn - Pb)`
(:279/:502/:576) with the double-well `dPb = -aP*(Pb-pb0)*(Pb-tipP)*(Pb-Ptwo) - kPb*secPb*100*tn +
kPb*gPb*fPb`, wells `pb0 = PB0*pb_scale` (depressed baseline) and `Ptwo=2.0`, tip `tipP=1.72`, stiffness
`aP` chosen to match the linear curvature at the low well (the toy's arbitrary aP is the confound to
remove).

**Pre-registered pass bar.** KEEP iff, at the REFIT optimum, chi2/dof drops below 3.68 AND the recovery
RMSE drops (selectively on the 4 recovery regions) WITHOUT lifting the decline regions' sign, calibration
preserved, Korea R2 intact, AND (interaction-analyst) it is not double-counting DEF-3. REMOVE otherwise.

**Prediction (partly confirmed, sharpened by measurement).** MOVES-but-REMOVE. The recovery RMSE DID
improve (0.124 -> 0.062, halved) - I under-called that - but non-selectively: the same lift wrong-signs
the DECLINE regions (USA +0.066, Japan +0.033), WORSENS overall chi2/dof (3.68 -> 4.26), and BREAKS the
2023 calibration beyond what PB_SCALE_ENS can restore (0.020 after re-solve, 40x the guard). It fails the
KEEP bar on chi2, calibration, and selectivity, and double-counts DEF-3.

**Honest-negative branch.** If the refit shows a SELECTIVE recovery-RMSE drop that survives the secular
re-fit and the interaction-analyst orthogonality check, DEF-6 is a real fix - promote with the stiffness
`aP` calibrated, not hand-set.

**Occam gate.** Prefer the single norm-layer well (H466); do not add a second reinforcing contagion layer
without evidence it is orthogonal.

**Toy evidence (measured).** Parity well lifts all 8 regions' net 2000-2019 change (max series delta
6.5e-2); no region crosses tipP=1.72. At the refit optimum: chi2/dof 4.26 (WORSE than baseline 3.68),
R1 3 (the decline regions USA/Japan/Korea), recovery RMSE 0.062 (halved but non-selective), Korea 0.781
(R2 passes), calibration drift 0.020 after re-solve (BREAKS the 5e-4 guard).

---

## H469 - JOINT: structural symmetrisation and its interactions

**Claim.** Effects compete and compound; turning on DEF-1 (zeroed secular) + DEF-2 (signed dep) + DEF-3
(tri-well) + DEF-6 (parity well) together lets the model reproduce the recoveries from its own corrected
mechanics without a bolt-on.

**Null.** The joint set is dominated by DEF-1's damage (zeroing removes the down-drift the fit demands)
and DEF-6's non-selective softening; DEF-2 and DEF-3 add nothing (inert), so the joint chi2 rises and the
only real interaction is DEF-1 x DEF-6 (both lift the quantum, over-lifting the decliners).

**Exact change.** All four toggles on; secular frozen at 0; refit kTau; re-solve PB_SCALE_ENS.

**Pre-registered pass bar.** KEEP the joint set iff it lowers chi2/dof below 3.68 AND cuts R1 sign-misses
by >= 2 (with recovery RMSE down) AND calibration preserved AND Korea R2 intact AND guards 13/13. REMOVE
otherwise. Report the interaction I(DEF-1, DEF-6) = joint delta minus the sum of singleton deltas.

**Prediction (CONFIRMED).** REMOVE. chi2/dof 7.784 (2.1x baseline; DEF-1 dominates); every region
over-lifted to net-positive; R1 4 (decline misses); recovery RMSE 0.047 (best) but Korea 2019 = 0.683
BREAKS R2 and calibration drift 0.015 after re-solve BREAKS the guard. Interaction: DEF-1(down) and
DEF-6(up) oppose on the recovery axis (DEF-6 wins) and near-add on chi2, with no rescue.

**Honest-negative branch.** If the joint set clears all bars, escalate to a full shipped-core promotion
round with the E40-precedent blast-radius protocol on all 463 verdicts.

**Occam gate.** A joint set that only works because DEF-6 over-lifts everyone and DEF-1 removes the trend
is not a mechanism; keep only on a clean, selective, calibration-preserving improvement.

**Toy evidence (measured, CONFIRMED REMOVE).** Joint refit: chi2/dof 7.784, R1 4 (decline misses),
recovery RMSE 0.047, Korea 0.683 (R2 BROKEN), calibration 0.015 after re-solve (BROKEN). No clean
interaction rescues the fit.

---

## H470 - META: the real gap is per-region recuperation, not symmetrisation

**Claim (constructive corollary).** The missed recoveries are NOT caused by a missing up-structure. At the
shipped drift the model already produces a small universal tempo-transient rise; the sign is "missed" only
because a SINGLE GLOBAL secular drift, forced to fit the large collapses, over-suppresses the recoverers.
The real gap is (i) per-region heterogeneity in the drift / recovery velocity (DEF-4) and (ii) a transient
postponement-recuperation quantum rebound (DEF-5, Bongaarts-Sobotka 2012 / Goldstein 2009) - neither of
which any symmetrisation of the decline-bias supplies.

**Measured Pareto tension (the evidence).** Across the four configs that touch the quantum level, recovery
RMSE falls monotonically as the quantum is lifted (DEF-1-free 0.265 -> baseline 0.124 -> DEF-6 0.062 ->
joint 0.047) while chi2/dof degrades with it (3.22 -> 3.68 -> 4.26 -> 7.78) and Korea's basin erodes
(joint breaks R2). No configuration reaches the lower-left (both chi2/dof < 3.68 AND recovery RMSE <
0.124). A single shared quantum knob cannot fit the collapsers and the recoverers at once - the recovery
gap is heterogeneity, not a missing well.

**Null (omnibus).** The decline-bias is correctly-fit signal; there is no structural asymmetry to fix that
improves the backtest.

**Pre-registered pass bar (for a FUTURE round, not this one).** A per-region recuperation velocity or a
partially-pooled secular drift is KEEP-worthy iff it selectively lowers the recovery RMSE and cuts R1
sign-misses by >= 2 WITHOUT breaking calibration or Korea - the exact bars H464-H469 fail. This hypothesis
records the DIRECTION (heterogeneity + transient), not a shipped change.

**Prediction.** This is where a real fix lives, if one exists; it is out of scope for a decline-bias
symmetrisation round and belongs to a DEF-4 x DEF-5 per-region recuperation round (which E47/E50 already
found is SIGN-only and magnitude-uncalibrated - so even there the honest baseline may remain a monotone
decline for trapped regions).

**Occam gate.** Prefer the honest monotone-decline baseline over any bolt-on that implies recovery depths
the model cannot predict (the E50 promotion-DECLINE precedent).

---

## Recommended ordering and honest prediction of the mix

**Ordering.** H464 (DEF-1) is make-or-break and runs first - it is the only defect the backtest directly
adjudicates and it settles the omnibus defect-vs-feature question. Then H468 (DEF-6), the only other fix
that moves any number, to test whether its movement is selective (predicted: no). H466 (DEF-3) and H465
(DEF-2) are inert on the hindcast and are adjudicated by the cheap series-identity checks already run;
H467 (DEF-4) is a diagnostic probe; H469 (joint) is the competition/interaction test. H470 records the
constructive direction.

**Honest prediction of the mix (5 defects).** ZERO real fixes; all five REFUTED-AS-DEFECT or subsumed.
- DEF-1: FEATURE (fit wants the drift stronger-down; zeroing 2.3x worse).
- DEF-2: FEATURE/INERT (bit-near-identical in an aging window).
- DEF-3: real structural gap but INERT on the hindcast (forward-durability value only, deferred).
- DEF-4: SUBSUMED (identifiability, downstream of DEF-5).
- DEF-6: MOVES but a non-discriminating confound (REMOVE by Occam).

The valuable outcome of this round is the negative result stated positively: the decline-bias is largely
correctly-fit signal, and the recovery gap is a per-region recuperation phenomenon (H470), so the honest
shipped default remains the monotone-decline baseline - consistent with the E50 promotion-DECLINE.
