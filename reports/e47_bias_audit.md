# Structural-Bias Audit - the Model's Asymmetry Toward Decline (E47 input)

A read-only adversarial audit (2026-07-11) of `emergent.py`, the experiments log and the SOTA,
asking one question: does the design make decline structurally easier to express than recovery?
The answer is yes, in seven reinforcing ways. This report feeds the E47 bias-correction round;
each finding is a pre-registered, non-destructive, testable engine change with the E41 backtest
(or a pre-existing verdict) as its refutation gate.

## Findings, ranked by materiality

- **A - Every secular drift term points down (HIGH).** The four secular constants (`secC` 0.0007,
  `secPb` 0.0010, `secTau` 0.006, `secS` 0.0010) all push fertility down over time; none moves any
  channel up. `tn`-scaled so they vanish at 2023 then activate forward - a built-in glide path,
  not a neutral fixed point. Test: zero all four, re-run baselines; do the collapse verdicts and
  the E41 sign-misses weaken?
- **B - The age-structure feedback is a one-way ratchet (HIGH).** `dep_pen = dep_fb*max(dep-dep0, 0)`
  (emergent.py:390) clips the beneficial branch: aging harms security, but a younger pyramid gives
  no reverse tailwind. The only endogenous macro-feedback is sign-restricted to decline. Test:
  replace with the signed `dep - dep0` (a symmetric dependency dividend).
- **C - The norm channel is antinatal-only: no pronatal well (HIGH).** The double-well has a
  childfree lock-in well (Nhi=0.42) and no pronatal well below Nlo=0.14; a pronatal norm cannot
  lock in. The campaign's richest, most-developed channel (E25/E38/E43/E44/E45) points only down.
  Test: add a third stable well near N~0.02 (tri-stable), anchored to the Israel/Haredi pronatal
  case; re-run the norm levers.
- **D - Rate constants calibrated only on collapse; Israel not a symmetric anchor (HIGH).** 7/8
  regions are sub-replacement; the E19 dynamics fit never saw a rising trajectory. Israel is a
  placed point (period-epoch pair, low-well NORM0 by fiat), never a recovery-velocity constraint.
  Test: hold Israel out, refit, predict its dynamics; then refit admitting a rising trajectory -
  do kC/decl/gS_C shift?
- **E - No recuperation mechanism (HIGH, known).** The E41 backtest REJECTED the core on
  hindcasting - it cannot reproduce the observed 2000-2019 rises (Germany +0.155, Poland +0.049,
  Israel +0.113, Italy +0.010). This is the empirical shadow of A-C. Test: add a recuperation term
  (tempo rebound / quantum bounce-back), re-run the backtest as the gate. **E46's second-order
  tempo is the first attack on this finding.**
- **F - Fertility-raising channels modelled thinly, lowering ones richly (MEDIUM-HIGH).** The rich
  nonlinear feedback channels (C, N, tau, q) express decline or gating; parity Pbar and security S -
  the channels that would carry recovery - are thin linear scalars with downward drift. Recovery
  cannot cascade; collapse can. Test: give parity a nonlinear two-child-norm social multiplier
  symmetric to the norm well.
- **G - Sibling / horizontal-kin mutual-support blind spot (MEDIUM).** Parity is a scalar mean; the
  model cannot represent that a child with siblings sits in a mutual-support network (shared
  childcare, cost, social capital) lowering the next generation's cost - a parity->parity positive
  feedback across generations. Kin appears only vertically (the E18 grandmother bridge, an
  endowment). This is the mirror image of C at the parity layer. Test: add a sibling-network term
  to parity dynamics carried through the `ot.py` cohort path integral. (Grounding: the E46 kin/
  sibling research anchor.)

## Synthesis

The model is materially biased toward decline, structurally rather than parametrically: the
machinery to express suppression is richer, more nonlinear and better-anchored than the machinery
to express support. It does not show as a narrow catalogue - many protective levers were tested -
but as a capping: a protective lever cannot trigger a self-reinforcing recovery because the upward
bistable/feedback structures that would let it cascade do not exist, so recovery is capped by
construction while collapse is amplified by it.

**Top 3 to restore symmetry:** (1) a recuperation / upward-drift mechanism (A+E jointly, the E41
backtest as gate) - highest value; (2) a symmetric dependency dividend (B); (3) an upward social
cascade - a pronatal third well (C) or a sibling-network parity feedback (G).

## E47 discipline note

These are changes to the SHIPPED core (`emergent.py`), so any that survives its test must
re-solve the calibration, re-run the guard suite, and re-measure the blast radius on the 425
recorded verdicts (the E40 precedent). Default is DEMOTE unless the backtest improves; a bias
correction that changes verdicts must be adjudicated, not silently absorbed. Each finding is
additive/sign-symmetrising and non-destructive to test.
