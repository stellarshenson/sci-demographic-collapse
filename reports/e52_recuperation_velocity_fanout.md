# E52 Fanout - Per-Region Recuperation Velocity (H471-H478)

Pre-registration for the E52 round, executing the E51 constructive pointer (H470 SUPPORTED):
"the recovery gap is per-region recuperation (DEF-4 heterogeneity x DEF-5 transient
postponement-recuperation) - a pooling problem, not a missing up-well." Bars are written BEFORE the
notebook runs; verdicts are earned against them, never re-fit after the fact.

## What prior rounds already settled (the design constraints)

Two refutations box this round in; any design that ignores them just re-runs a lost experiment:

- **E50 (H454): per-region DEPTH knobs die on the OOS gate** - a per-region recovery-depth fit does
  not generalize (fair FIT-only pool 0.212 beat per-region 0.229 out-of-sample). Therefore E52 may
  not introduce per-region FITTED constants unless each survives the same leave-one-recovery-out
  gate. The per-region content must come from somewhere other than fitting
- **E46 (H427/H428): Germany's recovery was QUANTUM, not tempo** - its MAC rose monotonically
  through the recovery; the tempo second-derivative fits 3.5x worse. Therefore no single-channel
  tempo story covers all recoveries
- E47 fixed the recovery SIGN (R1 misses 4 → 0) with one shared gated quantum AR(1)
  (`pull = g_rec [mu_c - quantum]+`, Myrskyla equity gate) + the Israel pronatal well; E50-H456
  fixed the magnitude artifact (Israel scalar 0.06 → 0.015). Both stay notebook-local
- E51 (H470): no configuration reaches the both-improve corner (chi2/dof < 3.684 AND recovery
  RMSE < 0.1238); a single shared quantum knob cannot fit collapsers and recoverers at once

## The design principle

Per-region heterogeneity WITHOUT per-region fitting. Two sources, both legitimate under E50:

1. **Channel ROUTING from data signatures** - each recovery region is assigned the recuperation
   channel its own observed data demand (tempo-transient vs quantum vs pronatal), classified by a
   pre-registered signature test (H471), not by what fits best
2. **Parameter-free TIMING** - the tempo-transient channel's velocity is slaved to the region's own
   MAC-rise deceleration. The Bongaarts-Feeney factor is ALREADY in the shipped core at the
   canonical kBF = 1.0: when dMAC/dt falls toward zero the period TFR mechanically rebounds at
   constant quantum (Bongaarts-Sobotka 2012, Goldstein-Sobotka 2009). The transient bump is the
   core's own tempo term doing its unwind - the open question is whether the model's endogenous tau
   trajectory decelerates ON TIME, not whether a new term is needed. No second tempo term may be
   added (double-counting ban)

The honest negative is a live outcome: if channel routing + parameter-free timing does not beat the
shared E47 knob, the recovery gap stays open, DEF-5 stays sign-only, and the round closes as a
confirmation of E50/E51 - that verdict is as publishable as a win.

## Data (all on disk - no external access)

- Observed TFR 2000-2023: UN WPP `data/raw/unwpp/demographic_indicators.csv` with GUS/KOSIS
  national-office replacements for Poland/Korea (E41 Wave-1 payload,
  `reports/e41_calibration_targets_research.json`)
- Observed MAC 2000-2023: same UN WPP file, all 8 regions (the primary tempo signature)
- Tempo-adjusted adjTFR (Bongaarts-Feeney): E41 payload; coverage is PARTIAL - Germany 2011-2016,
  Italy 2015-2021, Poland 2013-2021, Japan/Korea/USA partial, France/Israel NONE. adjTFR is
  corroboration where it overlaps, never the primary classifier
- Recovery accounting: OBS_NET = TFR(2019) - TFR(2000) per region (the E47/E51 convention);
  the sign-gate recovery set is {Germany +0.155, Italy, Poland +0.049, Israel +0.113}

## Hypotheses and pre-registered bars

| id | hypothesis | bar | prediction |
|---|---|---|---|
| H471 | Channel decomposition: the four observed recoveries classify into distinct channels by their own data signatures - tempo-transient iff the TFR rise coincides with falling dMAC/dt AND (where covered) flat/lower adjTFR; quantum iff adjTFR itself rises (or MAC rise stays un-decelerated through the rise, per E46); Israel pronatal (adjudicated E47/E50, carried not re-tested). Predicted map: Germany quantum, Italy tempo-transient, Poland tempo-transient, Israel pronatal | >= 3 of 4 land as predicted with the stated signatures → SUPPORTED; 2 → PARTIAL; else REFUTED | SUPPORTED |
| H472 | The shared-knob mis-timing diagnosis: the E47 AR(1) is monotone-approach by construction, so it cannot produce the observed rise-then-refall of Italy (peak ~2010, fall to 2023) and Poland (peak ~2017, fall to 2023); and the measured per-region recovery half-times differ by >= 2x, so one shared velocity misses at least one region on timing | both shown computationally in the one harness: post-peak model slope sign vs obs sign, and the half-time spread quantified | SUPPORTED |
| H473 | Prescribed-tempo diagnostic (parameter-free): feeding each region's OBSERVED MAC path through the core's own BF factor (kBF = 1.0, no new constant) reproduces the Italy/Poland transient bumps - peak year within +/- 5y and post-peak re-fall sign correct | 2/2 bump regions pass both timing and sign → SUPPORTED; 1/2 or timing-only → PARTIAL | SUPPORTED |
| H474 | Endogenous-timing audit: the shipped tau channel's own deceleration timing vs observed - per-region error in the year of peak MAC deceleration | error <= 5y in >= 6/8 regions → SUPPORTED; 4-5/8 → PARTIAL; else REFUTED (and the mis-timing is the named residual defect) | PARTIAL |
| H475 | Channel-matched recuperation (make-or-break): route each recovery region through its H471 channel - tempo unwind (parameter-free) for the bump regions, the E47 gated quantum AR(1) (shared g_rec) for quantum regions, the H456 Israel scalar 0.015 - and score on the full harness | sign gate stays 0 misses AND Korea monotone preserved AND recovery RMSE improves >= 10% over the shared-E47 comparator (recomputed in the same harness) with chi2/dof no worse than +2% → SUPPORTED; one side improves without degrading the other → PARTIAL; else REFUTED | PARTIAL |
| H476 | The E50 OOS gate on anything fitted: any constant refit in H475 (e.g. the shared g_rec) passes leave-one-recovery-out - OOS pooled recovery RMSE beats the shared-pool comparator recomputed in this harness. Parameter-free channels are exempt by construction | OOS <= shared-pool OOS → pass; else the fitted piece is REMOVED and H475 re-scored without it | PARTIAL |
| H477 | The re-fall discriminator: the channel-matched model reproduces Poland's post-2017 and Italy's post-2010 re-fall SIGN (which no monotone knob can), magnitude within factor 2 for at least one of the two | 2/2 signs + 1/2 magnitude → SUPPORTED; 2/2 signs only → PARTIAL; else REFUTED | SUPPORTED |
| H478 | META - blast radius + promotion: forward 2023→2100 fate map under the winner is unchanged in end-state basin classification for all 8 regions (transients decay, attractors stand); graft verdict by the standing Occam bar (both-improve corner vs shipped baseline: chi2/dof < 3.684 AND recovery RMSE < 0.1238) | fate map unchanged 8/8 → SUPPORTED as disposition; the corner verdict recorded either way; expectation: corner unreached → notebook-local, no graft | SUPPORTED |

Predicted mix (honest): 4 SUPPORTED, 4 PARTIAL, with H475/H476 the live REFUTED risks - magnitude
has died twice (E47, E50) and this round's only new weapon is timing.

## Harness and discipline

- **One harness, all comparators recomputed** - start from the E51-reviewed
  `scratchpad/toy_bias_harness.py` lineage (METHOD SOUND, `reports/nb48_e51_review.md`) extended
  with the E47 RecupModel (`notebooks/44-kj-e47-recuperation.ipynb`) and the E50 OOS gates + H456
  scalar (`notebooks/47-kj-e50-def8-magnitude.ipynb`). Every number quoted in a verdict (baseline,
  shared-E47, channel-matched, OOS pools) is computed IN THIS NOTEBOOK in the same configuration -
  no cross-round number splicing (chi2 3.684 vs 3.93 across rounds are different harness configs)
- **Reference bars carried verbatim** from `reports/nb48_e51_verdicts.json` `reference_bars`:
  base_chi2_dof 3.684, base_recovery_rmse 0.1238, korea_obs_2019 0.918, tol_cal 0.0005
- **Notebook-local only** - zero `src/emergent.py` edits; subclass pattern, baseline-preserving
  (deviations identically zero at g_rec = 0 / unwind off); any recalibration re-solves
  PB_SCALE_ENS with drift <= tol_cal and says so
- **No double tempo term** - the unwind is the core's existing kBF = 1.0 BF factor; the only
  admissible tempo intervention is on the TAU TRAJECTORY (prescribed-observed as a diagnostic;
  any fitted tau-timing correction goes through the H476 OOS gate)
- **Pre-registered windows** - OBS_NET to 2019 for the sign accounting, chi2 over the full
  2000-2023 window, Korea monotone over the full window; peak years measured from the observed
  national series, not chosen to flatter the model
- 64-strand ensemble, pinned seeds, deterministic re-execution expected bit-identical

## Deliverables

- `notebooks/49-kj-e52-recuperation-velocity.ipynb` - built by `scratchpad/build_nb49.py`
  (nbformat), executed detached in place, kernel `sci-demographic-collapse`, log
  `logs/nb49-execute.log`
- Figures (reports/figures/): `nb49_e52_channel_decomposition.png` (per-region TFR vs adjTFR vs
  dMAC/dt, recovery windows shaded), `nb49_e52_transient_fits.png` (Italy/Poland bumps: obs vs
  shared knob vs channel-matched), `nb49_e52_pareto.png` (chi2/dof vs recovery RMSE, all configs
  incl. the E51 points recomputed)
- `reports/nb49_e52_verdicts.json` - per-hypothesis verdict + metric + note, summary with
  disposition and promotion line, reference bars echoed

## Records (after the review closes clean)

Experiments log E52 section + at-a-glance rows (campaign → 478/52), tally guard 478, defects.md
DEF-4/DEF-5 status lines updated with the E52 disposition, README counts, SOTA only if a structural
finding survives, journal via the plugin, memory sync. Commit + push at the clean round boundary
under the continued autonomous mandate.
