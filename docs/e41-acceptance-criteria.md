# E41 Acceptance Criteria - Calibration Extension to Multi-Observable Targets

Acceptance-criteria log for the E41 round (the calibration-extension research → blocker resolution →
implementation arc). Each criterion is a yes/no check verifiable by one command or one artifact.
Status values: **MET** / **OPEN** / **GATED** (blocked on explicit user approval). Statuses are updated
in place as waves complete; criteria text is append-only. Regardless of any status below: no git
commit, push, or tag without explicit per-action user approval, `data/raw/` stays immutable, and the
model (`src/sci_demographic_collapse/`) is untouched until W3.1.

## Wave 1 - target research

- **W1.1 MET** - human-readable dossier exists: `docs/e41-calibration-extension-research.md`
- **W1.2 MET** - machine payload with per-value source + URL exists:
  `reports/e41_calibration_targets_research.json` (keys `inventory`/`targets`/`gapfills`/`synthesis`/`critiques`)
- **W1.3 MET** - ≥ 9 observable families × 8 regions collected; 70/72 values filled; both nulls
  (Israel childfree-ideal share, Israel adjTFR) flagged with where-to-look notes
- **W1.4 MET** - two adversarial critiques recorded verbatim in the payload: 18 BLOCKER/MAJOR
  findings (C0: 1 BLOCKER + 8 MAJOR; C1: 2 BLOCKER + 7 MAJOR), extracted to
  `scratchpad/e41-findings-for-resolvers.json`

## Wave 2 - blocker resolution (the current mandate: "remove all blockers")

- **W2.1 MET** - every one of the 18 BLOCKER/MAJOR findings carries a disposition row in
  `reports/e41_blocker_resolutions.json`: 9 RESOLVED (data delivered, source + URL + year per value),
  9 AMENDED (protocol text rewritten to the critics' fix), zero OPEN; disposition tally verified from
  the persisted report
- **W2.2 MET** - both Wave-1 nulls filled (C1F4 RESOLVED): Israel adjTFR computed locally from WPP
  single-age ASFR (2015-2023 series, tempo gap +0.165 → ~0 by 2022-23, method-consistent with the HFC
  BF-from-total convention); Israel childfree-ideal delivered as CBS Social Survey 2019 Table 39
  \<0.01 hard upper bound (exact zero-only share stays a named residual)
- **W2.3 MET** - parity distributions (0/1/2/3+) delivered for all 5 null regions (C1F3 RESOLVED:
  KOSIS 2020, CBS Census 2022, GUS NSP 2011, INSEE EFL 2011, ISTAT FE1); each sums to 1.000, parity-0
  coordinates with the cohort-childlessness family; Japan/FR/IT finer splits noted as remaining gaps
- **W2.4 MET** - C0F0 resolved: lifetime ever-in-union C-construct collected 8/8 from primary
  sources, feasibility re-verified with a period screen PB0 ≥ 1.15 (= 1+SIGMA_CAL[Pb], the empirical
  pass boundary, stricter than the naive C0 ≥ 1−p0) checked 8/8; Korea alone decouples to a
  period-epoch pair (C0=0.70/RV0=0.09, Yoo 2026), recorded with its residual MAJOR caveats under W2.6
- **W2.5 MET** - protocol v2 written (7 stages, in the report and dossier) containing all six
  amendments: C0F1 (kBF adjudicated on gap dynamics G = 1−TFR/adjTFR, not levels), C0F2 (epoch-matched
  PB0 cross-check via a spliced b.1975 pseudo-cohort CFR at new Stage 3b), C0F3 (|PB_SCALE_ENS−1|
  honesty metric deleted, replaced by a per-stage PB0-convergence table), C0F6 (option A leaves the
  `NORM0` dict byte-untouched), C0F7 (Stage-5 guard re-baselining enumerating every band in the
  63-test suite), C0F8 (WLS scope restriction + s_struct term)
- **W2.6 MET (round 3)** - closed per the user's decision (2026-07-11): the ~5 round-2 MAJORs (all on
  the C0F0 Korea/Israel decoupling) were formally reclassified to ACCEPTED-RESIDUAL, each with a
  named Wave-3 action and a verdict-insensitivity argument, and the same two reviewer personas re-ran
  as round 3 (Fable 5, fresh context): **both returned APPROVE - zero BLOCKER, zero MAJOR** - after
  independently re-deriving the PB0/margin/RV0 arithmetic (no recorded verdict flips; NORM0 confirmed
  byte-untouched). The bar - zero BLOCKER and every remaining MAJOR only at an ACCEPTED-RESIDUAL
  disposition - now holds with zero MAJORs outstanding. Six convergent MINOR sharpenings were folded
  into the wave3_actions (AR1 marked superseded-by-AR4 so the retired p0=0.11 cannot be implemented;
  AR1 period-screen figures corrected to the persisted 0.9215/3.15; Korea PB0 band restated
  [1.167,1.30] with the Stage-2 re-run at the joint corner C0=0.72, rv=0.065; the AR2 exemption
  denominator pinned). Full record in `reports/e41_blocker_resolutions.json` under `w26_close`
- **W2.7 MET** - dossier updated in place (`docs/e41-calibration-extension-research.md`) with a
  "Wave 2 - blocker resolution outcome (v2)" section (new values, protocol v2, disposition summary,
  residual-MAJOR caveats) and a revised Status block; this file's Wave-2 statuses flipped
- **W2.8 MET** - the experiments log's E41 section extended (append-only) with the Wave-2 outcome

## Wave 3 - implementation (not started)

- **W3.1 GATED** - explicit user approval to touch the model recorded in conversation
- **W3.2 GATED** - Stage 0/1 anchor replacements applied per protocol v2; `PB_SCALE_ENS` re-solved;
  every affected numeric band in the 63-test guard suite re-derived and updated in the same change
  (the E40 convention), `make test` green
- **W3.3 GATED** - observability harness additive only: existing return keys of
  `run()`/`run_ens()`/`run_cal()` unchanged and baseline trajectories reproduced bit-for-bit with
  the harness off vs on
- **W3.4 GATED** - the 2000→2023 backtest executed as a REJECTION test with pre-registered pass/fail
  bars (written before the run), results recorded whichever way they land
- **W3.5 GATED** - `make test` and `make lint` green on the final tree
- **W3.6 GATED** - experiments log, SOTA, and README reconciled to the post-E41 state; journal via
  the plugin with `journal-tools check` exit 0
- **W3.7 GATED** - implementation passed `/adversarial-review` with a clean confirming round
