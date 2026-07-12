# E51 confirming methodology review - the decline-bias defect register

**Verdict: METHOD SOUND (3 findings; 1 MAJOR, 2 MINOR).**

The round's conclusion - EARNED-SIGNAL, no `emergent.py` graft, monotone-decline baseline retained - is
earned by its own computed evidence. The FAIR DEF-6 well is genuinely fair on the three axes the charge
names, the cal-drift 3.0e-06 clean re-solve is computed (not asserted), the make-or-break H464
recovery-weighted refit is run live and rails down, and every verdict is wired to an adjudication function
with a reachable alternate branch. The one substantive gap is that the load-bearing "REMOVE earned against
the well CLASS" is airtight for Israel but only instance-level (plus a strong inference) for Germany, and
the round's prose overstates it as structural for both. The verdict itself is not overturned.

---

## Load-bearing adjudication (charge Q1-Q3)

### Q1 - is the fair well genuinely fair? YES.
Cell 10 computes, per region, three properties and asserts them:
- **Ordering** - active iff `pb0 < TIPP` (harness:139); active set computed to exactly {Italy, Korea, Poland}; the five with `pb0 >= 1.72` degenerate to the shipped linear relaxation.
- **Curvature match** - near-well restoring rate measured by finite difference equals `kPb=0.05` to `max dev 3e-08` (assert `worst_rate < 1e-6`, cell 10). This is the maximally-charitable choice: near the low well the fair form is bit-indistinguishable from shipped, so the ONLY deviation the well can introduce is an *upward* cascade above the tip. The construction can therefore only ever HELP a recovery - it is not tilted toward REFUTE; the negative it produces is genuine.
- **Clean anchor** - fixed-point residual `dPb(pb0) = 0.0` exactly for all 8 regions; spurious motion at the calibrated 2023 anchor `< 8e-04` (assert `worst_anchor < 1e-3`). Low well at unscaled `PB0`, not `PB0*PB_SCALE_ENS`, so `calibrate_ens` converges. No residual construction choice tilts the well toward REFUTE.

### Q2 - is the REMOVE earned against the CLASS or only this instance? SPLIT - see MAJOR-1.
- **Israel: STRUCTURAL, final.** `pb0 = 3.152 > PTWO = 2.0`. Any two-child well requires the unstable tip below the two-child plateau (`tip < PTWO = 2.0`, the cubic-stability ordering `pb0 < tip < PTWO`). Since Israel's baseline parity exceeds the plateau itself, NO admissible tip can place Israel below its tip. A two-child cascade (plateau 2.0) is the wrong instrument for a >2-child society by construction. The earned-negative is final for Israel. (France, pb0=2.000, is likewise structurally excluded.)
- **Germany: NOT structural; instance-level + strong inference.** `pb0 = 1.803 < PTWO = 2.0`. A shared tip placed anywhere in `(1.803, 2.0)` would flip Germany to active - so its inertness is contingent on the *carried* constant `TIPP=1.72`, not on the well class. The round fixed the tip at 1.72 and did not sweep it. The class-level conclusion nonetheless HOLDS, on computed evidence the round did run:
  1. at tip 1.72 Germany MISSES (net +0.006 vs obs +0.155, cell 26);
  2. when a below-tip region IS activated and its parity crosses the tip it OVERSHOOTS - Poland cascades to net **+0.219 vs obs +0.049** (cell 26), and Korea is spuriously lifted to 2019 TFR **1.037** (obs 0.918), failing the R2 gate (`korea6_ok=False`);
  3. the tip is a SHARED scalar - raising it to catch Germany also raises it for {Korea, Italy, Poland}, so a single tip cannot be tuned to Germany without disturbing the collapsers; a per-region tip would be over-fitting outside the well class.
  So no admissible shared-tip two-child well reproduces Germany's +0.155 selectively: it either misses (parity never crosses) or cascades to the 2.0 plateau (overshoot). The conclusion is right; the round's phrasing "the two-child cascade cannot reach Germany" is the overstatement (see MAJOR-1).

### Q3 - is cal-drift 3.0e-06 computed, not asserted? YES.
Cell 26 calls `calibration_drift(fix={"parity_well": True})` (harness:335-351), which builds the fair model, measures drift, runs the real `calibrate_ens(sigma=SIGMA_CAL, K=64)` PB_SCALE re-solve, patches the module scale, and re-measures. Output: `drift 0.011098 before -> 3.00e-06 after`. The disk JSON records `2.999296184080791e-06`, matching. This is a genuine re-solve: the fair well drifts 0.011 *before* re-solve and 3e-6 *after*, whereas the malformed well stayed at 0.0203 *after* re-solve (VAL table, cell 12) - the "40x break" (0.0203/0.0005 = 40.6x) was the self-referential-anchor artifact, now demonstrated by the clean fair re-solve. Confirmed computed.

---

## Findings (severity-ordered)

### MAJOR-1 - Germany's non-reachability is stated as structural but is instance-level; the shared tip was not swept
`reports/nb48_e51_verdicts.json` H468 note and cell 27 `note6`: "the two child cascade cannot reach" Germany
**and** Israel are grouped as one structural claim. Only Israel is structural (`pb0 3.152 > PTWO 2.0`).
Germany (`pb0 1.803 < PTWO 2.0`) is reachable-in-principle by any shared tip in `(1.803, 2.0)`; its
inertness depends on the carried constant `TIPP=1.72` (harness:96), which E51 did not sweep. Per the
charge's own framing this means "a placement was left untested." The REMOVE verdict is **not overturned** -
the two failure horns are both demonstrated in-notebook (Germany miss at tip 1.72; Poland overshoot +0.219;
Korea spurious 1.037) and the shared-constant constraint blocks tuning the tip to Germany alone - but the
round should say "no admissible *shared-tip* two-child well reproduces Germany selectively (it misses or
overshoots)", not "the cascade cannot reach" it. Honest close: one sentence, or convert the inference to a
computed result with a small tip sweep over `(1.72, 2.0)` showing Germany flips miss -> overshoot with no
selective sweet spot.

### MINOR-2 - the H468 note understates its own refute evidence
Cell 27 `note6` characterizes the failure as "overshooting Italy while leaving the regions that most need
help untouched." The computed nets (cell 26) show the stronger case: Italy is the *mild* overshoot (+0.028
vs +0.010), while **Poland overshoots hard (+0.219 vs +0.049)** and **Korea is spuriously recovered to
1.037** (obs 0.918), breaking the Korea R2 monotonicity gate (`korea6_ok=False`). Korea - the region that
most needs to stay collapsed - is not "left untouched"; it is wrong-signed upward by the cascade. The
deciding-metric line does record `active [Italy, Korea, Poland]` and `Korea R2 False`, so the numbers are
present; only the prose picks the weakest example. The Korea spurious-recovery is arguably a decisive REFUTE
reason independent of RMSE and deserves to lead the note.

### MINOR-3 - the tip/plateau constants are carried, and 1.72 is the one un-exercised degree of freedom
Plateau `PTWO=2.0` is grounded (two-child ideal, Sobotka-Beaujouan 2014, cited in
`reports/def_biascorrection_research.md:295`). The unstable tip `TIPP=1.72` (harness:96) is a modeling
midpoint carried from the malformed round, not empirically anchored and not swept in E51. Since the entire
active/inert partition (and thus MAJOR-1) pivots on it, it is worth an explicit "single shared tip, not
swept" caveat in the writeup. H470's "no lower-left corner" is likewise an existence check over 4 configs
(cell 31), sound as a pointer but not a proof that no config anywhere improves both axes.

---

## What is already sound

- **Baseline preservation is real, not a hardcoded pass.** Cell 8 asserts `worst_ident == 0.0` bit-for-bit
  between `BiasModel` (toggles off) and the shipped `EmergentModel._estep_vec` across 8 regions x 4 secular
  clocks on perturbed states; cell 16 additionally guards the live baseline `chi2/dof 3.684` and recovery
  RMSE 0.1238 against the disk checkpoint within tolerance. Both computed.
- **H464 make-or-break is run live and honest.** Zeroing the four secular terms sends chi2/dof 3.68 -> 8.39
  (cell 16). The free-bounds fit picks every secular term DOWN with recovery RMSE 0.265 (worse). The
  recovery-weighted (5x) refit is a live 370s Nelder-Mead (cell 17) and still rails secC/secPb down
  (+0.0049/+0.0122) - the falsification the honest version owed is executed, not asserted. Both KEEP
  branches of `adjudicate_h464` are shown reachable (cell 18 asserts).
- **INERT-ON-HINDCAST (H465/H466) is the honest label, not an escape hatch.** DEF-2's dividend branch is
  algebraically inexercisable because all 8 regions age over 2000-2023 (`dep>dep0`, so `max(dep-dep0,0)`
  reduces to identity; series delta 0.000679). DEF-3's tri-well is inexercisable because N starts snapped to
  NORM0 with `fN=0` and nothing forces it (delta 0.00483). Neither branch is *visited* by the hindcast, so
  REFUTED would be dishonest (claiming disproof of an untested branch); INERT is correct, and the round
  claims neither as a win (both deferred to a forward-run verdict). Cell 22 also shows the Israel re-anchor
  drifts without the tri-well (-0.023) but sits still with it (+0.005), correctly attributing the tri-well's
  role.
- **cal-drift 3.0e-06 computed via a real PB_SCALE re-solve** (Q3 above).
- **Verdict wiring is computed, not literal.** Every verdict comes from an `adjudicate_*` function on
  computed numbers, each with a reachability assert for the alternate branch (cells 18, 20, 22, 24, 27, 29,
  31). The omnibus disposition is `graft_warranted = any(verdict in {GRAFT-CANDIDATE,KEEP,KEEP/PROMOTE,
  ESCALATE})` (cell 35) - a reachable if/else, currently EARNED-SIGNAL because no verdict is a graft label.
  The JSON is dumped from the `VERDICTS` dict; disk values match the notebook outputs exactly.
- **Executed top-to-bottom**, execution counts 1-19 monotonic, no unrun cells - outputs are not stale.
