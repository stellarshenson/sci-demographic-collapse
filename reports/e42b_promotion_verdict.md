# E42b Promotion Verdict — Education E and Wellbeing W as engine states in `emergent.py`

## Verdict

| Variable | Verdict | Wires considered | Carry |
|---|---|---|---|
| **Education E** | **REJECT** | positional arms-race `dE/dt` → `dtau`; attainment level → `dtau`; income cash-out → S/q | none |
| **Wellbeing W** | **KEEP-NOTEBOOK-LOCAL** | misery gate `relu(W_floor−W)` → `f[4]` (childlessness ρ); loss-averse `dW`; hedonic stimulus; norm-broadcast → N | none |
| **QuantileFlow carry (either)** | **REJECT** | E rank-transport; W below-floor tail-mass | none |

Nothing is promoted to the 7-tuple. Both stay notebook-local in `EWModel`, injected through the effective-force vector under the E40-A8 bit-identity discipline. This is the E35 eigen-operator / `flow.py` core-lift precedent applied a third time: the constructs are clean and digest-grounded but do not move numbers no shipped channel already moves. All four judge panels returned ADOPT or ADOPT-WITH-CHANGES on the decline; the changes are to the record, none to the engine.

---

## Education E → REJECT

**Decisive evidence.** E carries no irreducible engine channel. Pure attainment is null 8/8 (`|dTFR2125| < 0.005`, H396). Every positive E number - Germany +0.110 - is the income lever wearing an education label, and income already ships as S/q. The one genuinely new dynamic, the positional arms-race `dE/dt` transient (H394 SUPPORTED), is a tempo push: its coupling `gEtau·(E−E0)` into `dtau` is *identical in form* to the shipped `fTau` wire, same entry point, and it moves only −0.009…−0.020 mid-century - 15-90× below the winning-lever band (marriageable-men income +0.274, contrarian bundle +0.908, in-kind childcare +0.127). The rejection is forced by equation shape, not merely magnitude: a wire that only reproduces what `fTau` can already drive fails the bar by construction.

**Structural kicker (science-first).** The race is a relative-position effect - a strand's penalty depends on `E − Ē_cohort`. For a scalar E you *are* the cohort mean, so `E − Ē ≡ 0` and the race is identically inert. E is expressible only under dispersion. But then the two clean baseline resolutions both collapse E to today's notebook capability: freeze `E_ceiling = E0` (kills the expansion wave that is E's sole content) or carry the pure deviation (race `≡ 0` unless a round injects the gap - i.e. exactly the current notebook-local `race` parameter). Either way promotion adds no persistent channel.

---

## Wellbeing W → KEEP-NOTEBOOK-LOCAL

**Decisive evidence.** Real wires (Clark unemployment scarring, Kahneman-Tversky loss aversion), none clearing identification or the bar:

- **hedonic stimulus** - hard null (~1e-4), habituation low-passed by decade-scale fertility (H402)
- **misery gate at `W_floor`** (H400 PARTIAL) - the only selection-shaped construct, but E42 could not identify it against a linear wire (gated 1.03 vs linear 1.00, ~3%) even with the down-shock driving the tail strands below the floor (peak 31% of strands, per the measured `Germany_downshock` diagnostics), and it is regime-dependent (no baseline bite in Germany)
- **norm-broadcast** (H398) - overturned by the interaction gate as a bistable N-crossing artifact (a switch across `thN=0.25`; USA 0.66 / France 0.999 broadcast shares are well-crossing artifacts, France's direct leg dead)
- **persistent content** ("structural security", durability 0.76-1.0) - is channel S, already shipped
- **meaning/hedonia split** - failed LOO identification at n=8 (H401)

**Why KEEP-NOTEBOOK-LOCAL and not REJECT.** Unlike E, W's misery gate is a *genuine* distributional operation in form - on a scalar it is a point evaluation of the mean; on a distribution it is the below-floor tail mass (`ot.Dist.mass(W_floor, side="below")`), where mean ≠ population. That is a real, digest-grounded coupling worth keeping available in `EWModel` for future rounds. It simply cannot ship: it is unidentified, and promoting an unidentified gate shape is precisely what the discipline forbids.

**The baseline breach that blocks a zero-deviation ship.** Germany's modelled population already sits below `W_floor = −0.15`, so `max(W_floor − W, 0)` is non-zero at Germany's baseline. Promotion would force `PB_SCALE_ENS[Germany]` to silently absorb it - the exact failure `test_guard_calibration_anchor` (year-1 TFR `<5e-4`, 8/8, verified against source) exists to catch. Re-anchoring `W_floor` per region to dodge this makes gate position a free parameter, destroying the identification E42 already lacked.

---

## QuantileFlow carry (both) → REJECT

`flow.py`'s `QuantileFlow` delivers reparameterisation, exact 1-D W2, and Jensen-correct aggregation in one differentiable object - the right tool where rank/tail carries signal the mean discards. Here it is inert:

- **E** presents no threshold and no tail op - the arms-race transient is a curvature-free mean/rate shift → Jensen gap ≈ 0
- **W's** only threshold (the misery gate) failed identification at *scalar* amplitude, so a dispersed Jensen gap is a few percent of an already ~1e-4/3% effect

Both land in the same ≤4.65e-4 dead zone that pruned the full core lift, at K× (48-64×) per-year compute. The operational selection test - disperse + apply nonlinearity must move TFR beyond the ~5e-4 floor via a material Jensen gap or a real threshold-crossing sub-population - fails for both. Paying 48-64× compute to buy ≤4.65e-4 is the identical trade already rejected.

---

## Judges' strongest objections and how they are weighed

**1. The W misery-gate identification was run only in Germany, where the gate is locally linear by construction (population already below the floor).** So "failed to identify (1.03 vs 1.00)" may reflect testing in a regime where the gate *cannot* bite, not proof it is unidentifiable everywhere. This is the single genuine soft spot in the decline. Weight: it does not change the verdict - the rebuttal holds (chasing a floor-crossing region means making `W_floor` a free parameter, forfeiting identification anyway) - but the decline currently rests on prose, not a pre-registered test. Addressed by residual action R1 below.

**2. The dispersed-E Jensen gap is inferred, not measured.** The ≤4.65e-4 figure is imported from the core-lift precedent via a curvature×variance argument, not from actually dispersing E in `EWModel`. The exact quantity that could reopen E is the one number never put on the scale. Weight: immaterial to the verdict - even the mean-shift race at ~0.01 is already 5× below the 0.05 promotion bar, so any Jensen gap on top is doubly buried - but recorded as R2 to pre-satisfy the future mandatory-distributional condition.

**3. Shared-wire double-counting (the structural interactions objection).** E's `gEtau→dtau` sits on top of `fTau`; W's `−gWS·relu(W_floor−W)→dS` sits on top of channel S. Promoting either creates two wires driving one channel that `calibrate_ens` cannot partition - unidentifiable at calibration, independent of magnitude. Weight: this is the strongest reason to decline and is fully accepted; it makes promotion actively risky, not merely inert.

**4. Basin-flip contamination.** A promoted W-with-broadcast wire imports the `thN=0.25` N well-crossing the interaction gate already flagged as artifactual into every future intervention's N basin. Weight: accepted; reinforces excluding the broadcast wire entirely and keeping W notebook-local.

**5. The `run_dist` drift footgun.** `run_dist` (L436, verified) inlines its own scalar dynamics for `C,rv,Pb,tau,S,qc` and never calls `_estep`, so any future engine-state addition must hand-patch it or the distributional core silently diverges from `run`. Weight: accepted as a standing hazard to record (R3 below), since it is the one place the E40-A8 bit-identity discipline is not guard-enforced.

---

## What would reopen the question — tied to the three named gate residuals

Promote only if a future round produces a lever whose E- or W-borne content clears the campaign bar (**> ~0.05 TFR**) through a channel `tau/S/q/N` cannot already carry. For W specifically, the reopen is gated on all three named interaction-gate residuals plus a measured Jensen gap:

- **R1 — floor-crossing identification (gate residual: per-region full-minus-direct well-posedness).** Register as a pre-registered bar: gate vs linear wire in a region that crosses `W_floor` *during* the run, with `W_floor` held fixed. This is a new identification design, not a re-run - E42 already failed the scalar-amplitude attempt. Closes objection 1.
- **R2 — measured dispersed-E Jensen gap (gate residual: gWN dial-vs-switch sweep applied to the E race).** One `EWModel` run: disperse E at `sigE≈0.08`, apply the `race` coupling, read ΔTFR vs the scalar-injected ~0.01. Converts the inferred ≤5e-4 into a measured one and pre-satisfies the mandatory-distributional QuantileFlow re-audit. Closes objection 2.
- **R3 — decouple W from the N well-crossing (gate residual: triple wave × deterioration × broadcast).** The broadcast bite must be shown to be a genuine W tail response, not a `thN=0.25` basin switch, before any W wire ships. Until resolved, the broadcast wire is excluded and any promoted W signal is confounded. Closes objections 3-4 on the W side.

If a lever ever clears the bar through E, its promotion is **mandatory-distributional** (a scalar E is inert by construction), at which point re-audit the QuantileFlow carry against the *measured* R2 gap. Absent R1-R3 resolved and a > 0.05 lever, the answer stands.

---

## Record actions (gated on user approval, no engine change)

1. Write **E = REJECT** and **W = KEEP-NOTEBOOK-LOCAL** into `reports/nb38_e42_verdicts.json`, citing the E35 / `flow.py` precedent
2. Reframe the W note so it reads as a future research question: E42's own identification attempt failed at full scalar amplitude, so R1 is a new design, not a ready lever - not "nearly ready"
3. Record the **Germany-W baseline breach** explicitly as the concrete reason the gate cannot ship as a zero-deviation coupling, preserving the invariant for the next round
4. Record the **`run_dist` (L436) drift** as a blocking note: any future engine-state addition must hand-patch it or the distributional core silently diverges from `run`
5. Register **R1-R3** as the pre-registered reopen bars tied to the three interaction-gate residuals

Because the declined design would be zero-deviation at baseline (except Germany-W), no calibrated baseline moves and **zero verdict flips** are expected - which is exactly why promotion buys nothing. No `PB_SCALE_ENS` re-solve, no guard re-derivation, no re-run list is triggered by this verdict.

**Bottom line: elegance must move the numbers. E routes through `fTau` (and S/q for its income content) at ~0.01; W's identified content is channel S plus a ~1e-4 null; the QuantileFlow carry lands in the ≤4.65e-4 dead zone. Neither earns a seat. E → REJECT, W → KEEP-NOTEBOOK-LOCAL, no QuantileFlow carry.**

---

## Post-review amendments (2026-07-11, round-1 methodology review)

The E42 adversarial review (round 1) returned three findings that touch this report. The verdicts
(E REJECT, W KEEP-NOTEBOOK-LOCAL, no QuantileFlow carry) are unchanged; the evidence base and one
mechanism label are corrected:

- **H396 is by-construction, not decisive evidence.** The "pure attainment is null 8/8" line cited
  as decisive above cannot fail: the notebook architecture contains no direct E→demography wire
  (`fE` alone leaves the force vector untouched), so the null is an architectural statement -
  H396 was re-graded SUPPORTED→PARTIAL in the round record. The E rejection stands on its
  independent legs, already stated: the equation-shape argument (the arms-race coupling is the
  shipped `fTau` wire in form and entry point) and the magnitude argument (~0.01, 15-90x below
  the winning-lever band)
- **The baseline floor breach is Korea-led, not Germany.** The "Germany already below the floor"
  premise (objection 1, record action 3, and the zero-deviation clause above) was never measured;
  the review's floor-diagnostics cell measured it and found Germany's baseline mean W bottoms
  near -0.12 and never crosses W_floor = -0.15 (the gate opens only in the shocked tail strands,
  a few percent of the direct S-channel response - the H400 null is an amplitude problem, not a
  saturated regime). Four regions breach the floor at baseline - Italy, Japan, Korea and Poland,
  all at 100% of strands - with KOREA dominant at 33x the next region's gate mass (0.086 vs
  0.0026, per `floor_diag` in `reports/nb38_e42_verdicts.json`). This *strengthens* the
  no-zero-deviation-ship argument; record action 3 should be read as the **Korea-led W baseline
  breach**, and objection 1's "locally linear by construction" premise is replaced by "the gate
  contribution is too small relative to the direct channel" - R1 (the floor-crossing
  identification design) remains the named reopening condition, now with Korea as the natural
  test region
- **Wire label corrected.** The misery gate enters `f[4]` (childlessness ρ, on top of `fRV`),
  not channel S as the objection-3 notation suggested; the shared-wire unidentifiability
  argument survives with the channel relabeled
