# E52 Methodology Review

Independent methodology review of `notebooks/49-kj-e52-recuperation-velocity.ipynb` against the
pre-registration `reports/e52_recuperation_velocity_fanout.md` and `reports/nb49_e52_verdicts.json`.

**VERDICT: METHOD SOUND (confirmed round 2)** - the round-1 MINOR finding was dispositioned as
disclosure-not-regrade and resolved in the patched notebook; see "Confirming round" below.

Every earned verdict (H471-H478) follows from its pre-registered bar applied to the numbers the
notebook actually computes; the verdicts JSON is a faithful serialization of the notebook outputs;
baseline preservation, comparator arithmetic, the H476 removal consequence, and the Pareto
reproduction all check out. One MINOR pre-registration-convention deviation is documented below; it
is conservative (yields the stricter verdict) and does not touch the make-or-break or the disposition.

## Findings

### [MINOR] Shape/peak diagnostics use UN WPP peaks; the fanout pre-registers national-series peaks - material only to H473 Poland

- The fanout (`e52_recuperation_velocity_fanout.md`, "Pre-registered windows"): *"peak years measured
  from the observed national series, not chosen to flatter the model."* For Poland the national series
  is GUS (`TFR_OBS`); for Korea it is KOSIS.
- The notebook's shape diagnostics - `classify` (cell 16), `half_time` (cell 18), the H472 mistiming
  (cell 18), the H473 BF timing (cell 20), the H477 re-fall (cell 28) - all read `TFR_WPP`, so
  Poland's peak is taken as **2017** (WPP 1.472). The pre-registered national series (`TFR_OBS`) peaks
  at **2019** (GUS 1.419).
- Materiality: recomputed, only H473 Poland is verdict-sensitive. BF factor peaks 2023;
  `|2023-2017| = 6y` (timing MISS, WPP) vs `|2023-2019| = 4y` (timing OK, national). Under the
  national peak Poland's `timing_ok` becomes True, so `n_timing = 1` and the H473 ladder
  (`SUPPORTED if n_pass==2 else PARTIAL if n_pass==1 or n_timing>=1 else REFUTED`) yields **PARTIAL,
  not the shipped REFUTED**. (H472/H477 verdicts are robust to the peak choice; H471 routing is
  robust - Poland is quantum via adjTFR regardless.)
- Why MINOR, not MAJOR: (1) the deviation is *conservative* - WPP gives the harsher verdict, so it did
  not flatter the model; (2) it is defensible - the GUS series is sparse (no 2016/2017/2018 points),
  its "2019 peak" is a missing-data artifact, and the dense WPP peak (2017) is the more faithful peak;
  (3) H473 is a supporting diagnostic - a REFUTED→PARTIAL move there does not disturb the make-or-break
  (H475 REFUTED) or the DEF-5-sign-only disposition. The gap is that the WPP-for-shape substitution
  and its H473-Poland sensitivity are **not disclosed** in the notebook.

## Per-question findings (7 load-bearing questions)

**Q1 - Verdict-vs-bar fidelity: MET.** All eight verdicts reproduce from the bar applied to the
computed numbers (verified against cell outputs, JSON matches):
- H471 SUPPORTED - 3/4 signatures (Germany/Italy/Israel as predicted; Poland measured quantum vs
  predicted tempo, honestly carried), bar >=3 → SUPPORTED.
- H472 PARTIAL - grade-down from predicted SUPPORTED: `clean_monotone` False (shared-E47 DOES re-fall,
  slopes -0.0041/-0.0015) and half-time spread 1.6x < 2x, so neither specific claim holds; `both_miss`
  True → PARTIAL. Honest and if anything stricter than the literal "both shown" bar.
- H473 REFUTED - 0/2 pass, n_timing 0 (under WPP peaks) → REFUTED. (See MINOR: national peaks →
  PARTIAL.)
- H474 REFUTED - 0/8 within 5y → REFUTED (grade-down from predicted PARTIAL). Model peak-decel pins to
  the 2005 window edge (smooth monotone tau); honest.
- H475 REFUTED (make-or-break) - sign gate misses ['Italy'], RMSE 0.0715 vs 0.0646 (-10.8%, worse) →
  REFUTED. Re-scored without g_rec also REFUTED.
- H476 REFUTED - OOS 0.0953 > shared-pool 0.0579 → gate fails. The pre-registered removal WAS executed
  in-cell (cell 26: `m_nog` built, scored misses ['Germany','Italy','Poland'] RMSE 0.0933, H475
  re-`record`ed unchanged) - not merely asserted.
- H477 PARTIAL - 2/2 signs, 0/2 magnitude → PARTIAL.
- H478 SUPPORTED - basin 8/8 unchanged, corner unreached → SUPPORTED disposition.

**Q2 - Korea-gate substitution: MET (honest).** The R2 convention (2019 within 0.15 of 0.918 AND
falls 2015-2019) is the harness's carried E51 gate, not a new E52 weakening. Recomputed on the
**fitted shipped baseline** (chi2/dof 3.6838, korea_2019 0.829 - both match the notebook's BASELINE
output): the Korea model TFR rises from 0.806 to a 2010 peak 0.8634 then falls - 10 of 23 year-steps
*increase*, so strict monotone-nonincreasing is False at baseline. The substitution therefore does not
weaken a gate that would otherwise hold; it is honest. (The unfitted backtest shows the same hump,
16 increases.)

**Q3 - Comparator integrity: MET.** channel-matched RMSE 0.0715 vs shared-E47 0.0646 (worse, gain
-10.8%), chi2/dof 3.8307 vs 3.8961 (-1.7%, better) - arithmetic correct. The predicted-map
sensitivity (Poland tempo, cell 24) is present: misses ['Italy','Poland'], RMSE 0.0772, verdict
unchanged. The E51 Pareto points are recomputed in-harness via `fit_params`/`tier2` (cell 32,
366s), not pasted: DEF-1-free 3.221/0.2654, DEF-6 3.795/0.1445, JOINT 7.99/0.0715 all reproduce.

**Q4 - Poland quantum classification: MET, with the MINOR caveat above.** Poland's quantum call rests
on adjTFR rising; recomputed it is robust to COVID - net +0.065 (2013-2021), still +0.065 excluding
2020 and +0.237 excluding the 2021 endpoint. The dual-convention issue is real (shape reads WPP,
OBS_NET reads GUS) but only H473-Poland is verdict-sensitive (MINOR); classification and routing do
not flip.

**Q5 - No-double-tempo-term ban: MET.** `E52Model._estep_vec` (cell 10) adds only the gated quantum
AR(1) on Pb (`out[:,2]`) for quantum-routed regions and the Israel scalar - no tempo term. Tempo
channels rely on the core's own `kBF = em.PARAMS["kBF"]`. H473 (cell 20) computes
`1 - kBF*np.gradient(mac)` from the OBSERVED MAC path as a forcing/diagnostic substitution, not a new
fitted constant.

**Q6 - Baseline preservation + calibration: MET.** Cell 12: bit-for-bit baseline preservation
(worst per-channel diff 0.0 over 8 regions x 4 tn) asserts and passes; baseline chi2/dof 3.6838
reproduces ref 3.684 and recovery RMSE 0.1238 reproduces exactly. Max cal drift across recalibrated
configs 2.02e-06 < tol 5e-4 (cell 24 assert passes).

**Q7 - Disposition honesty: MET.** 2S/2P/4R with the make-or-break (H475) REFUTED under both
routings; corner unreached (chi2 3.831 > 3.684) → src_graft_warranted False →
"DEF-5-SIGN-ONLY (confirmed)" is correct. H478 fate-map 8/8 basin-unchanged and the no-graft call are
grounded in cell 30's forward run.

## Verified strengths

- Verdicts JSON is a byte-faithful serialization of the notebook's `VERDICTS`/`CKPT` dicts (cell 38).
- The H476 pre-registered removal consequence is genuinely executed, not narrated.
- Poland's deviation from the predicted tempo routing is surfaced (headline = measured signature,
  predicted-map scored as sensitivity), not hidden.
- Grade-downs (H472, H473, H474 all below their predictions) show the bars were applied against the
  numbers, not back-fit to the predicted mix.
- Every comparator (baseline, shared-E47, channel-matched, sensitivity, OOS pools, Pareto) is
  recomputed in the one harness with recorded cal drift.

## Confirming round (round 2)

The round-1 MINOR finding (WPP-for-shape substitution undisclosed; H473-Poland verdict-sensitive)
was dispositioned by the coordinator as **disclosure-not-regrade**: H473 stays REFUTED on the WPP
reading, on the ruling that the GUS series' 2019 argmax is a missing-data artifact of its 2016-2018
gap, making WPP the instrument-valid AND conservative choice. The notebook was patched (wording
only) and re-executed (20/20 code cells, 0 errors). Confirming checks:

1. **Finding resolved - YES.** The configuration markdown (cell 7) now carries an
   "Observed-series convention split (disclosed)" paragraph naming exactly the split I found:
   OBS_NET on national `TFR_OBS` (GUS/KOSIS) per pre-registration, shape/peak diagnostics
   (H471/H472/H473/H477) on continuous `TFR_WPP`, with the Poland gap (no GUS 2016-2018 points,
   argmax-2019 artifact vs WPP peak 2017) named. The H473 note now carries the sensitivity verbatim:
   under the GUS national peak Poland's timing error would be 4y and H473 would grade PARTIAL; the
   WPP reading (6y) is retained as conservative and instrument-valid, and it correctly adds that
   Italy fails under either convention (12y both ways - verified in round 1). The disclosure honestly
   and completely represents the finding; the retained-REFUTED rationale is defensible and matches my
   own round-1 materiality analysis.
2. **H476 reword correct - YES.** Cell 26 note now reads "the quantum channel holds just
   ['Germany', 'Poland'], so each held-out fold fits g_rec on the single remaining in-channel
   region and the extrapolation overshoots" - this is the accurate description of the leave-one-out
   mechanics (verified against the fold arithmetic in `oos_leave_one`: with 2 in-channel regions,
   holding one out leaves exactly one region with nonzero slope in the fit pool). The odd round-1
   phrasing is gone; the JSON carries the reworded note.
3. **Numeric spot-check - PASS (bit-identical).** Baseline chi2/dof 3.6838 / RMSE 0.1238 (cell 12);
   channel-matched 0.0715 / 3.8307 (cell 24 output and JSON `configs.channel_matched`); OOS 0.0953 vs
   shared-pool 0.0579 (cell 26). All eight verdict letters unchanged
   (S/P/R/R/R/R/P/S), disposition DEF-5-SIGN-ONLY (confirmed), src_graft_warranted false.
4. **No new issues - CONFIRMED.** The only substantive edits are the cell 7 disclosure paragraph,
   the H473 note sensitivity sentence, and the H476 note reword; every other WPP/GUS/convention
   mention in code cells is a pre-existing round-1 line (imports, plot labels, docstrings). 20/20
   code cells executed, 0 errors, no numeric drift detected.

VERDICT: METHOD SOUND (confirmed round 2)
