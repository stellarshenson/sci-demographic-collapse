# E47 Bias-Correction Hypothesis Fanout (Pre-Registered)

Ranked, pre-registered hypotheses for the E47 structural-bias round, one per candidate defect fix,
each grounded in a standalone toy model (`scratchpad/toy_e47_*.py`) and the literature. The governing
rule is Occam / "elegance must move the numbers": a fix is KEEP-only-if a toy shows it plausibly
moves the E41 backtest (the four missed recoveries) or a recorded verdict, and REMOVE otherwise. The
E41 backtest is the gate: it REJECTED the core under B5-R1 because the SIGN of the observed 2000->2019
TFR change is missed for **4 of 8 regions** (Germany +0.155, Italy +0.010, Poland +0.049, Israel
+0.113 - all real recoveries the down-only core cannot express), at chi2/dof = 3.638 (bar 2.0). Korea's
monotone decline (R2) and the MAC-rise / marriage-decline directions (R3/R4) all pass, so the failure
is specifically the model's structural inability to turn UP.

Any surviving fix must re-solve `PB_SCALE_ENS`, re-run the guard suite, and re-measure the blast radius
on all 425 recorded verdicts (the E40 precedent). Every change is additive or sign-symmetrising and
baseline-preserving (identically zero at the 2023 calibrated fixed point), so baselines stay bit-for-bit
when the new coefficient is zero - the guard that keeps the correction honest.

## Ranking summary

| rank | H | defect | fix | toy verdict | Occam default |
|---|---|---|---|---|---|
| 1 | H430 | DEF-5 | quantum mean-reversion / recuperation | MOVES: flips net TFR -0.055 -> +0.081 (sign miss -> match) | KEEP-if flips >=2 sign-misses |
| 2 | H431 | DEF-3 | pronatal third well (tri-stable norm) | MOVES: locks pronatal state 0.14 -> 0.014, anchors Israel basin | KEEP-if a norm-durability verdict or Israel fit moves |
| 3 | H432 | DEF-1 | zero / sign-flip the secular drift | INERT: monotone drift can't make a U; backtest wants it DOWN | REMOVE (fold zeroing into H430) |
| 4 | H433 | DEF-6 | parity two-child social multiplier | MOVES but CONFOUNDS H431 (same contagion, second layer) | REMOVE unless it adds beyond H431 |
| 5 | H434 | DEF-2 | signed dependency dividend | INERT on backtest (bit-identical in an aging window) | REMOVE (forward-run symmetry note only) |

**Try first: H430 (DEF-5).** It is the only fix a toy shows can flip the backtest sign, and it directly
attacks the confirmed falsification. The others are either indirect (H431), inert (H432, H434), or
confounded with a higher-ranked fix (H433).

---

## H430 - DEF-5: quantum mean-reversion / recuperation (TRY FIRST)

**Hypothesis**: the core misses the four 2000->2019 recoveries because the quantum `C*(1-rho)*Pb` has
only down-forces (secular drift, the one-way coupling trap, rising rho) and no restoring term, so once
depressed by a postponement/transition transient it cannot come back. Adding a recuperation reservoir
that returns a fraction `f` of postponed births as a QUANTUM level rebound - while MAC keeps rising -
lets the model reproduce the recoveries (E46's "quantum, not tempo" finding; E46-H428 already demoted
the tempo-oscillator route).

**Exact emergent.py change** (additive, baseline-preserving):
- Carry a scalar recuperation reservoir `D` per run, filled by the annual tempo loss and drained over
  a lag `L_rec`: each year `D <- D + kBF*max(dtau, 0) - D/L_rec`.
- Add the drained flux back to the period TFR: `tfr = qv*fv*tp + f_rec * (D/L_rec)` (in `run`,
  `run_dist`, and the `run_ens` per-agent aggregation at emergent.py:700 / 374 / 527).
- New PARAMS: `f_rec` (Sobotka recuperation index, central **0.65**, sweep [0.37, 1.0]) and `L_rec`
  (central **7 yr**, sweep [5, 12]).
- Baseline preservation: at the 2023 fixed point `dtau = 0 => D -> 0 => flux = 0`, so `f_rec = 0`
  reproduces `run` bit-for-bit (guard). The reservoir self-limits: it releases only as postponement
  DECELERATES, so a region still postponing fast (Korea) gets little lift - the desired behaviour.

**Toy evidence** (`scratchpad/toy_e47_def5.py`): a Germany-like run with MAC rising monotonically
30.6 -> 31.7 (dtau > 0 every year, the E46 signature). The CURRENT down-only quantum gives net TFR
**-0.055** (a sign MISS - model declines while Germany rose). The mean-reversion fix recovers a
fraction `f = 0.81` of the quantum deficit and gives net TFR **+0.081** (sign MATCH). The sensitivity
sweep shows even the Spain-floor recuperation (`f = 0.35`) flips the sign to +0.013; central values
(`f = 0.54-0.81`) give +0.042 to +0.081 - same order as the observed +0.11 to +0.20.

**Literature grounding**: Goldstein, Sobotka & Jasilioniene (2009), *The End of 'Lowest-Low'
Fertility?* - the developed-world turn-around (countries below 1.3 fell 21 in 2003 to 5 in 2008;
Spain 1.16 -> 1.46, +0.20; Italy +0.11), with the rise concentrated at OLDER ages as delayed cohorts
recuperate - a quantum swing of 0.2-0.4 children back up while MAC still rises. Sobotka-Zeman-Frejka
(2011) sets the recuperation fraction (RI ~0.65 central, 0.37 Spain to >1 US). Both digested in
`references/papers/`.

**Pre-registered pass/fail bar**: re-run the E41 backtest with the fix (fitting `f_rec`, `L_rec`
inside their brackets). KEEP iff B5-R1 sign-misses drop from 4 to **<= 1 of 8** (Germany, Italy,
Poland or Israel net TFR turns positive) AND Korea's monotone decline (R2) still passes AND chi2/dof
does not worsen (<= 3.638). REMOVE if it flips < 2 sign-misses or breaks R2 (over-lifts Korea).

**Occam default**: KEEP-if-moves. This is the fix most likely to move the numbers and the one to try
first. Primary calibration RISK: a uniform recuperation term could over-lift Korea and break its R2
monotone-decline gate - the reservoir's self-limiting design (release only on deceleration) should
prevent this, but it is the first thing to verify.

---

## H431 - DEF-3: pronatal third well (tri-stable norm)

**Hypothesis**: the norm channel is antinatal-only - a childfree lock-in well (Nhi = 0.42) and no
stable well below Nlo = 0.14 - so a pronatal norm cannot lock in and the model's richest channel points
only down. Adding a third stable well near N ~ 0.02 (tri-stable) gives the structural home for a
self-reinforcing pronatal subculture (Israel/Haredi), and for the durable half of a recovery.

**Exact emergent.py change**: replace the cubic double-well `dN = -aN*(N-Nlo)*(N-thN)*(N-Nhi)`
(emergent.py:284, 518, 580) with a quintic tri-well
`dN = -aN*cN*(N-Npro)*(N-tip_pro)*(N-Nlo)*(N-thN)*(N-Nhi)`, new PARAMS `Npro = 0.02`,
`tip_pro = 0.08`, and a normaliser `cN` chosen so the mid-well curvature matches the current channel
(baseline-preserving: regions start snapped to their existing wells, so the norm->rho coupling stays
zero at 2023). Optionally re-anchor Israel's `NORM0` to the pronatal well.

**Toy evidence** (`scratchpad/toy_e47_def3.py`): push-and-release a pronatal lever, then remove it.
The double-well relaxes straight back to Nlo = 0.140 (no durable pronatal state). The tri-well locks
into Npro and STAYS at **0.014** after release. Verified three genuine stable fixed points at
[0.02, 0.14, 0.42] - the missing mirror of the childfree well.

**Literature grounding**: Okun (2017) on Israeli Jewish religiosity and fertility, Kaufmann-Goujon-
Skirbekk (2012) on the end of secularization (pronatal subcultures outgrow the secular majority),
Greksa-Korbin (2002) on Old Order Amish fertility - all in-library digests; the self-reinforcing
pronatal subculture is a documented lock-in, not a fitted artefact.

**Pre-registered pass/fail bar**: KEEP iff (a) a recorded norm-lever DURABILITY verdict flips (a
pronatal push that currently fades now locks in, changing an E25/E38/E43/E44/E45 verdict for a
documented reason), OR (b) Israel's backtest fit improves (its R1 sign-miss resolves or its
rms_std_resid 1.18 drops) once its basin is a genuine well. REMOVE if no verdict moves.

**Occam default**: KEEP-if a verdict moves. Ranked second because it supplies the upward-cascade
structure and the Israel anchor, but its backtest relevance is INDIRECT (durability and the Israel
basin), not a direct sign-flip like H430. RISK: the third well is a new bistable structure that could
change many norm-lever verdicts at once - the blast radius on the 425 verdicts must be measured before
it is kept.

---

## H432 - DEF-1: zero / sign-flip the secular drift (REMOVE candidate)

**Hypothesis (under test for removal)**: the four secular constants (secC 0.0007, secPb 0.0010,
secTau 0.006, secS 0.0010) all push down - a built-in glide path. Zeroing or sign-symmetrising them
would remove the down-bias.

**Exact emergent.py change tested**: set secC/secPb/secTau/secS to 0 (PARAMS lines 148-159), or flip
a sign, and re-run the backtest.

**Toy evidence** (`scratchpad/toy_e47_def1.py`): a monotone linear secular drift is MONOTONE for ANY
sign - shipped-down, zeroed, and sign-flipped-up all give a monotone TFR path with NO interior trough.
A drift cannot produce a recovery; a sign-flip just swaps one monotone glide for another. HONEST
EVIDENCE FROM THE BACKTEST: the E41 refit drove secC 0.0007 -> 0.00257 and secPb 0.001 -> 0.0108
(3.7x and 10.8x STRONGER down-drift) and secTau 0.006 -> 0.0 (off). The data wanted MORE quantum
down-drift, not less - so zeroing secC/secPb WORSENS the quantum fit.

**Literature grounding**: none needed - this is an internal identifiability result. The secular term
is a slow trend, not the recovery mechanism (the recovery is the fast quantum rebound, Goldstein 2009).

**Pre-registered pass/fail bar**: KEEP iff zeroing/flipping the secular terms improves the backtest
chi2/dof or reduces sign-misses on its own. The toy predicts it will NOT (monotone term, and the fit
wants the drift retained).

**Occam default**: REMOVE as a standalone recovery fix. The correct role of DEF-1 is that the H430
mean-reversion attractor REPLACES the fixed declining target, so the down-drift is softened by the
restoring term, not by a hand-set sign flip. Fold DEF-1 into H430; do not ship a standalone secular
sign change.

---

## H433 - DEF-6: parity two-child social multiplier (REMOVE candidate - confounds H431)

**Hypothesis**: parity Pbar is a thin linear scalar while the lowering channels are rich and nonlinear;
give parity a bistable two-child-norm social multiplier (symmetric to the norm well) so recovery can
cascade.

**Exact emergent.py change tested**: replace the linear
`dPb = kPb*(PB0 + gPb*fPb - secPb*100*tn - Pb)` (emergent.py:279, 502, 576) with a double-well
`dPb = -aP*(Pb-PB0)*(Pb-tipP)*(Pb-Ptwo) + kPb*gPb*fPb`, wells at the depressed baseline and a
two-child plateau Ptwo ~ 2.0, tip ~ 1.72.

**Toy evidence** (`scratchpad/toy_e47_def6.py`): a linear push always decays back to the depressed
baseline (1.50) on release. The multiplier is sub-critical for a small push (also decays) but
SUPER-critical once the push clears the tip: parity cascades to the two-child plateau (2.00) and STAYS.
Two stable wells at [1.5, 2.0]. So the mechanism CAN move the numbers (a threshold cascade).

**Literature grounding**: Kohler-Billari-Ortega (2002) social multiplier (no OA PDF - paywalled),
covered in-library by Lutz-Skirbekk-Testa (2006) low-fertility-trap (self-reinforcing dynamics) and
Sobotka-Beaujouan (2014) two-child family ideal (the two-child norm persists as an attractor).

**Pre-registered pass/fail bar**: KEEP iff, WITH H431 already in place, the parity multiplier adds a
verdict change beyond what the pronatal norm well already delivers (an interaction-analyst check that
it is not double-counting the same social-contagion signal).

**Occam default**: REMOVE unless it demonstrably adds beyond H431. The two-child parity multiplier and
the pronatal norm well encode the SAME social-contagion mechanism at two different layers - shipping
both is the double-counting failure mode this project audits for (the E15/E16 shared-channel saturation
lesson). Prefer the single norm-layer well (H431); do not add a second reinforcing layer without
evidence it is orthogonal.

---

## H434 - DEF-2: signed dependency dividend (REMOVE candidate - inert on backtest)

**Hypothesis (under test for removal)**: `dep_pen = dep_fb*max(dep-dep0, 0)` (emergent.py:390, 542,
718) clips the beneficial branch - aging harms security but a younger pyramid gives no reverse
tailwind. Replacing the clip with the signed `dep_fb*(dep-dep0)` would add a symmetric dependency
dividend.

**Exact emergent.py change tested**: drop the `max(..., 0)` clip in the three `dep_pen` sites.

**Toy evidence** (`scratchpad/toy_e47_def2.py`): over the 2000-2019 backtest window every region's
dependency ratio rose MONOTONICALLY (population aging), so `dep > dep0` every year and
`max(dep-dep0, 0) == (dep-dep0)` EXACTLY - the signed and clipped forms are BIT-IDENTICAL (max
difference 0.0). The dividend branch only activates when the pyramid YOUNGS (dep < dep0), which no
region did in-window; it can only bite deep in a FORWARD run after an intervention first reverses the
pyramid - a slow, second-order effect.

**Literature grounding**: Lee-Mason National Transfer Accounts demographic-dividend framework (not
downloaded - the fix is inert on the backtest, so not load-bearing).

**Pre-registered pass/fail bar**: KEEP iff the signed dividend changes the backtest (it cannot - the
toy proves bit-identity in an aging window) OR flips a FORWARD-run verdict where an intervention youngs
the pyramid. REMOVE otherwise.

**Occam default**: REMOVE for the backtest. Retain only as a documented forward-run symmetry note: the
clip is a genuine asymmetry, but it is inert on every backtest region and moves no recorded verdict, so
by Occam it is not shipped now. Revisit only if a forward intervention run is shown to reverse a
pyramid.

---

## DEF-4 and DEF-7 (prose only - no toy model)

**DEF-4 (calibration-on-collapse)**: the dynamic rate constants (kC, decl, gS_C, kTau) were fit in E19
on 7 collapsing regions; Israel is a placed point (period-epoch pair, low-well NORM0 by fiat), never a
recovery-velocity constraint. This is an identifiability / data-coverage concern, not a mechanism, so
it gets no toy. It is DOWNSTREAM of H430: refitting on Israel or admitting a rising trajectory only
moves constants - without a recuperation term (H430) the structural incapacity to turn up remains, so
the refit would just redistribute residuals. The disciplined action is to hold Israel out, refit after
H430 is in place, and check whether kC/decl/gS_C shift materially; if they do not, DEF-4 is subsumed by
H430 and needs no separate change. Address only after H430's verdict is known.

**DEF-7 (sibling / horizontal-kin cascade)**: PRE-DEMOTED as confounded by the E46 kin/sibling anchor.
Kolk's (2015) twin instrument collapses the raw sibling-count -> own-fertility correlation
(+0.078 to +0.096) to +0.041 (men, n.s.) / -0.042 (women, marginal) - essentially zero, slightly
negative, with a genuine resource-dilution counter-arm (Blake). Wiring a sibling -> parity cascade
would encode a confounded correlation as structure, exactly the failure mode this round audits for.
REMOVE the cascade by Occam. The ONLY surviving arm is a kin-childcare-AVAILABILITY modifier on
security S (the ~4x-odds / +31pp second-birth effects of Zhang-Emery and Kaptijn-Thomese), entering as
a small, saturating uplift to effective S in high-kin-availability regions, net of a resource-dilution
counter-term, and touching neither Pbar directly nor first-birth entry. That S-side term is a minor
recalibration, not a headline driver, and is out of scope for the backtest gate; log it as a candidate
for a later security-channel refinement, not an E47 structural change.

## E47 discipline recap

- One hypothesis per defect, each with a toy model and the E41 backtest (or a recorded verdict) as its
  refutation gate.
- KEEP a fix iff it moves the numbers; the toys already predict H430 moves, H431 moves indirectly, and
  H432/H433/H434 are inert or confounded and default to REMOVE.
- Any survivor re-solves PB_SCALE_ENS, re-runs the guard suite, and re-measures the blast radius on all
  425 verdicts; a bias correction that changes verdicts is adjudicated, not silently absorbed.
- Recommended ordering: **H430 first** (the direct falsification attack), then H431 (the upward-cascade
  structure + Israel anchor) only if a durability/Israel verdict moves; H432, H433, H434 are removed
  unless their own gates fire.
