# Recovery State

## BRACE 2026-07-10 (Fri) ~17:45 - E40 rigor audit, review round 2 pending

**Session goal (Stop-hook, still active)**: "All rigor audits completed, every confirmed mathematics or
simulation bug fixed with its reproduction on record, every affected hypothesis round re-executed and its
verdict corrected, calibration reproduced for all 8 regions, make test green, make lint green, the
experiments log, SOTA and README reconciled to the corrected numbers, the result passed /adversarial-review
with a clean confirming round, the journal updated via the plugin with journal-tools check exit 0, awaiting
only the user's commit and push approval."

### What is DONE and valid on disk (all committed by this brace checkpoint)

- **The E40 finding + fix**: `emergent.py` Bongaarts-Feeney period factor was `1 − kBF·Σ₄(substep rates)`
  = exactly 4× the documented `(1 − 0.6·τ̇)`; phantom term at τ clips; unguarded negative per-agent factors
  LIVE in the calibrated baseline (7/8 regions, worst −0.221 yr-1); observable was integrator-dependent
  (endpoints moved 0.16 TFR under substep halving). FIX shipped in all three integrators
  (`run`/`run_dist`/`run_ens`): `max(1 − kBF·Δτ_realized, 0)` per agent; `PB_SCALE_ENS` re-solved (all 8
  lower 0.1-1.3%); calibration 8/8 ≤1.3e-4; first-order convergence restored.
- **notebooks/36-kj-rigor-audit-e40.ipynb** - executed green (exit 0), 34 cells: A1-A7 reproductions,
  verbatim `run_ens_legacy` (proven vs committed calibration 1.2e-4), blast radius. Builder:
  `scratchpad/build_nb36.py`. Verdicts: `reports/nb36_e40_verdicts.json` (A1/A2 CONFIRMED-FIXED,
  A3 CONFIRMED, A4 MEASURED-HOLDS, A5-A7 DOCUMENTED). Figures `reports/figures/nb36_{tempo_fix,blast_radius}.png`.
- **Blast radius measured**: tempo bumps deflate ~4× (Korea fTau=−3 peak +0.236→+0.071) - amplitudes of
  E19/E33/E37 tempo levers declared superseded; endpoints stable <0.03; transplant +0.736/+0.818 (was
  +0.717/+0.798), gH* 0.1430 (was 0.1423), Korea fission crossing 2062 (unchanged), inequality>male 2/2.
- **nb17 story figures re-executed on the corrected core** (exit 0; README embeds them; Korea dumbbell now
  +0.69 vs +0.28).
- **Records reconciled**: README (40 rounds E1-E40, 36 notebooks, E40 sentence, formula floored, transplant
  +0.74/+0.82, dumbbell alt text), SOTA (period-fertility section rewritten with the E40 correction),
  experiments log (E40 section + roll-up row + total row + exec summary + status line), reports/README +
  logs/README entries. `make test` 52 passed; `make lint` clean (re-verify after the 3 post-review comment
  edits - they are comment-only).
- **scripts/graphify_rebuild.sh** - new tracked harness (rebuilds the knowledge graph; not part of make build).
- **Graphify map** (temporary artefact): /tmp session scratchpad `graphify-out/` - 528 nodes/835 edges;
  regenerate any time with `scripts/graphify_rebuild.sh`.
- **Kolomolo Bedrock**: usable models `eu.anthropic.claude-opus-4-5-20251101-v1:0` (reviews ran on this),
  sonnet-4-5, haiku-4-5; profile `kolomolo`, region eu-central-1; `claude -p` with
  `--dangerously-skip-permissions` is blocked by the auto-mode classifier - use plain
  `aws bedrock-runtime converse` (Mode 1) or `claude -p --allowedTools "Read" "Grep" "Glob"` (Mode 2).

### Adversarial review state (round 1 done, round 2 = FIRST ACTION)

Round-1 results persisted: `scratchpad/e40-review1-mode1-result.txt` (diff review, Bedrock Opus 4.5) and
`scratchpad/e40-review2-mode2-result.txt` (data-scientist Mode 2). Triage state:

- Mode 1 findings: #3 unbounded-factor REFUTED (dynamics bound |Δτ|≤0.96/yr → factor ≤1.6; >1 is genuine
  B-F for advancing births) - comment added in run_ens; #1/#6 vestigial dtau return - docstring note added
  (_estep marked DIAGNOSTIC); #4 self.P→p style - fixed. All three edits are in emergent.py (comment-only).
- Mode 2 (data-scientist) CONFIRMED-REAL items still TO DO:
  1. **[MAJOR] Crisis fidelity - RESOLVED (moot).** CONFIRMED this session: nb05 (E10 crises), nb07
     (E12 incl. H44) and nb14 (E19) all `from sci_demographic_collapse import coremodel as cm` and
     import NO emergent core - the crisis battery validates the Leslie/data layer, which E40 did not
     touch. The emergent behavioural core (where the tempo term lives) has no recorded crisis
     validation to invalidate; its recorded validation surface is the 2023 calibration (A3, 8/8).
     DONE in `scratchpad/build_nb36.py`: A4 markdown now states this by construction. No re-run needed.
  2. **[MAJOR] Blast-radius sample thin (2 regions/3 archetypes)** - extend nb36 A4b to all 8 regions
     (endpoint-delta stability table) or justify worst-case coverage.
  3. **[MAJOR] Floor-bias unmeasured** - report % of agent-years hitting the factor floor under (a)
     baseline (should be ~0 post-fix - negatives were a LEGACY artifact; verify) and (b) strongest fTau
     forcing; bound the TFR bias.
  4. **[MINOR] supersede markers** - add `[superseded-amplitude → E40]` pointers inline to E19/E33-H310/E37
     tempo-amplitude rows in the experiments log (append-only rule: a marker pointer is allowed, never a
     rewrite of the verdict).
  5. kBF=0.6 choice: defensible IF crisis fidelity passes (document in E40 section); else sweep kBF.
- After fixes: re-run BOTH reviewers (same prompts, updated tree) until a clean confirming round
  (Mode 1 prompt needs the fresh `git diff HEAD~1` equivalent or the full current emergent.py section).

### Remaining after review clean

- `/journal:update` entry for E40 (Extended), `journal-tools check` exit 0.
- Memory update: `project-goals.md` E40 paragraph + `MEMORY.md` israel-region-e37 line → "campaign 392/40,
  E40 rigor audit: tempo term fixed 4x, verdicts stand, amplitudes superseded".
- Report to user; git commit/push ONLY on explicit approval (the brace commit itself is authorized by /brace).

### PARKED 2026-07-10 ~17:50 by user ("park this work for now, stop until I resume later")

In-flight edits sit in `scratchpad/build_nb36.py` (gitignored, on disk), NOT yet rebuilt/executed into
the notebook, NOT committed:
- Mode-2 finding 1 (crisis fidelity): DONE - A4 markdown states it is moot by construction (see above).
- Mode-2 finding 2 (thin sample): DONE in the builder - added an `A4b(8)` cell sweeping all 8 regions x
  {tempo, coupling crown} endpoint deltas, asserting worst shift < 0.03.
- Mode-2 finding 3 (floor bias): PARTIAL - `run_ens_legacy` gained a `fixed=True` mode that measures the
  fixed core's floor-hit share; still need to ADD the A4e cell that calls it on baseline + strongest fTau
  and reports the floor-hit % (expect ~0 at baseline - negatives were a legacy artifact).
- Mode-2 finding 4 (supersede markers): NOT STARTED - add `[amplitude superseded → E40]` inline pointers
  to the E19 / E33-H310 / E37 tempo-amplitude rows in the experiments log (marker only, never a verdict
  rewrite; append-only safe).
- Mode-1 findings: all addressed (comments in emergent.py, committed in cdcda5e).

### FIRST ACTION on resume

Read this file. Then finish the builder: add the A4e floor-share cell (finding 3), then add the supersede
markers to the experiments log (finding 4). Rebuild + execute:
`CUDA_VISIBLE_DEVICES=GPU-58ae1f45-295c-681b-60ad-843265f52997 .venv/bin/jupyter nbconvert --to notebook
--execute --inplace --ExecutePreprocessor.kernel_name=sci-demographic-collapse notebooks/36-kj-rigor-audit-e40.ipynb`.
Then re-run BOTH Bedrock reviewers on the updated tree (recipes above) for the clean confirming round; then
`/journal:update` (E40, Extended) + `journal-tools check`; memory (`project-goals.md` + `MEMORY.md`); report
to user; commit/push only on explicit approval.

### Invalid / quarantined

- Nothing quarantined. The pre-E40 tempo-bump amplitudes in E19/E33/E37 records are superseded (not
  quarantined - the supersession is recorded in the E40 section; inline markers pending, item 4 above).
