# Model Defects - the Structural Decline-Bias Register

Tracked defects in the shipped behavioural core (`emergent.py`), found by the E47 structural-bias
audit (`reports/e47_bias_audit.md`) and refined by the E46 second-order round and the kin/sibling
research. Each is a candidate fix targeted by the E47 hypothesis fanout. **Governing rule (Occam /
"elegance must move the numbers"): a fix is KEPT only if it demonstrably moves the E41 backtest or
a recorded verdict; otherwise it is removed, not kept as decorative complexity.** Any fix that
survives its test must re-solve the calibration, re-run the guard suite, and re-measure the blast
radius on the 425 recorded verdicts (the E40 precedent).

| id | defect | materiality | proposed fix | status |
|---|---|---|---|---|
| DEF-1 | all four secular drift constants point down (secC/secPb/secTau/secS); no upward secular term - a built-in glide path, not a neutral fixed point | HIGH | zero or sign-symmetrise the secular terms; re-run the E41 backtest | OPEN |
| DEF-2 | the age-structure feedback is a one-way ratchet: `dep_pen = dep_fb*max(dep-dep0,0)` clips the recovery branch, so a younger pyramid gets no dividend | HIGH | replace the clip with the signed `dep-dep0` (a symmetric dependency dividend) | OPEN |
| DEF-3 | the norm channel is antinatal-only - a childfree lock-in well (Nhi) and no pronatal well below Nlo; the richest mechanism points only down | HIGH | add a third stable (pronatal) well near N~0.02, anchored to the Israel/Haredi case; re-run the norm levers | OPEN |
| DEF-4 | dynamic rate constants calibrated only on 7 collapsing regions; Israel is a placed point, never a recovery-velocity constraint | HIGH | hold Israel out / admit a rising trajectory in the fit; do kC/decl/gS_C shift? | OPEN |
| DEF-5 | no recuperation mechanism (E41 backtest REJECTED on 4 real recoveries) - the empirical shadow of DEF-1..3. **E46 refined this: Germany's recovery was QUANTUM (MAC rose monotonically), not tempo** - so the fix is a quantum rebound, not tempo inertia (E46-H428 demoted the tempo route). **DUAL VALUE: this is not only a backtest fix - a working quantum-recuperation channel gives the model NEAR-TERM quantum-recovery PREDICTION, the single most policy-relevant output the campaign lacks (the model currently predicts the far-future basin but is blind to the near-term bounce a minister plans against)** | HIGH (top priority) | add a quantum mean-reversion / bounce-back term; **score on PREDICTIVE SKILL - reproduce the magnitude AND timing of the 4 observed recoveries (Germany +0.15 to 2016, Poland +0.05, Israel +0.11), not just their sign** | PARTIALLY RESOLVED (E47, notebook-local): the gated UN-AR(1) quantum mean-reversion + Israel pronatal well takes the R1 sign-misses 4 -> 0 with Korea preserved; the SIGN half is fixed. The MAGNITUDE half is NOT (see DEF-8). Shipped-core promotion still pending. **PROMOTION DECISION (E50, coordinator): the recuperation stays NOTEBOOK-LOCAL and is NOT grafted into `emergent.py`.** Rationale (Occam / contrarian): the mechanism is SIGN-ONLY (magnitude unfixable per DEF-8), a core graft is high-blast-radius (re-solve PB_SCALE_ENS + re-measure all 463 recorded verdicts) and risks implying recovery depths the model cannot predict; the honest baseline (monotonic decline for trapped regions, no spurious recovery) is the more defensible shipped default. The H456 Israel scalar recalibration is the one clean improvement available IF a future user-gated promotion happens - and that graft must ship the fit-selected best_oos value, not the in-sample best_in (E50 confirming-review MINOR-1). |
| DEF-6 | fertility-raising channels (parity Pbar, security S) are thin linear scalars while lowering channels (C, N, tau, q) are rich and nonlinear - recovery cannot cascade, collapse can | MED-HIGH | give parity a nonlinear two-child-norm social multiplier symmetric to the norm well | OPEN |
| DEF-7 | sibling / horizontal-kin mutual-support blind spot - parity is a scalar mean; no upward kin cascade to mirror the downward norm cascade | MED | **kin/sibling research verdict: the sibling->family-size cascade is CONFOUNDED (Kolk twin instrument -> ~0/negative); do NOT wire it as structure. Only a narrow kin-childcare-availability term on security S survives (small, saturating, net of resource dilution).** Default: REMOVE the cascade by Occam; test only the S-side availability term | OPEN (cascade pre-demoted) |
| DEF-8 | the E47 recuperation fixes the recovery SIGN but not its MAGNITUDE - the backtest RMSE is a wash (0.219 vs 0.213 baseline); the recovery DEPTH and TIMING are uncalibrated (a single shared g_rec pulls every gated region toward one asymptote mu_c, so it cannot match Germany +0.15 vs Poland +0.05 vs Israel +0.11 individually) | MED-HIGH | pre-register a fix fanout: per-region recovery asymptotes / depth targets, a Bayesian hierarchical g_rec (partial pooling across regions), or an explicit recovery-magnitude likelihood term - score on RMSE reduction against the observed recovery depths, not just the sign gate; keep by Occam only if magnitude fit demonstrably improves | RESOLVED (notebook-local): CLOSED by E50-H456 - the magnitude miss was a single-region error-model artifact, not the Bayesian regularization (refuted) nor de-pooling / filtering (Occam-pruned by the OOS gate). Recalibrating the one Israel pronatal-well scalar 0.06 → 0.015 closes it notebook-local; a shipped-core graft is DECLINED (see DEF-5). |

## The E47 discipline

- Each defect is an additive or sign-symmetrising change to `emergent.py`, non-destructive to test.
- Pre-register one hypothesis per defect with the E41 backtest (or a recorded verdict) as the
  pass/fail gate.
- KEEP a fix iff it moves the numbers (reduces backtest sign-misses / lowers chi2 / changes a
  verdict for a documented reason); else remove it - Occam's razor over elegance.
- A survivor re-solves PB_SCALE_ENS, re-runs the guard suite, and re-measures the blast radius on
  all 425 verdicts; a bias correction that changes verdicts is adjudicated, not silently absorbed.
- Toy models (isolated 1-2 channel systems) ground each fix cheaply before any shipped-core edit.
