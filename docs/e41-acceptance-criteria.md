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

- **W2.1 OPEN** - every one of the 18 BLOCKER/MAJOR findings carries a disposition row in
  `reports/e41_blocker_resolutions.json`: RESOLVED (data delivered, source + URL + year per value),
  AMENDED (protocol text rewritten to the critics' fix), or ACCEPTED-RESIDUAL (named justification +
  what was tried); zero findings left without a disposition
- **W2.2 OPEN** - the two Wave-1 nulls filled with sourced values, or ACCEPTED-RESIDUAL naming the
  exhausted sources (Israel childfree-ideal via CBS Social Survey; Israel adjTFR via Okun
  decompositions or computed B-F from on-disk CBS/WPP ASFR + MAC)
- **W2.3 OPEN** - parity distributions (0/1/2/3+) delivered for France, Italy, Korea, Poland, Israel
  (C1F3) or ACCEPTED-RESIDUAL per region with the named unavailable table
- **W2.4 OPEN** - the C-construct blocker (C0F0) resolved: one construct chosen (critics' proposal:
  lifetime ever-in-union by 45-49), and the feasibility bound C0 ≥ 1−p0 re-verified arithmetically
  for all 8 regions with the delivered numbers
- **W2.5 OPEN** - protocol v2 written containing all six amendments: C0F1 (kBF adjudicated on gap
  dynamics, not levels), C0F2 (epoch-matched PB0 cross-check), C0F3 (honesty metric = PB0 vs
  epoch-matched check, not |PB_SCALE_ENS−1|), C0F6 (option A leaves the `NORM0` dict untouched),
  C0F7 (guard-suite re-baselining stage enumerating every numeric band in
  `tests/test_hypothesis_guards.py`), C0F8 (WLS structural-error term or scope restriction)
- **W2.6 OPEN** - re-critique clean: both adversarial critics re-run against the v2 dossier +
  disposition table; bar = zero BLOCKER, and every remaining MAJOR points only at an explicitly
  ACCEPTED-RESIDUAL disposition; loop until the bar holds (rounds protocol)
- **W2.7 OPEN** - dossier updated in place (`docs/e41-calibration-extension-research.md`) with the
  new values, protocol v2, and disposition summary; this file's Wave-2 statuses flipped to MET
- **W2.8 OPEN** - the experiments log's E41 section extended (append-only) with the Wave-2 outcome

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
