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

### RESOLVED 2026-07-10 ~20:20 (brace-resume complete; the park is closed)

Every FIRST-ACTION item above is done and verified on disk:
- A4e floor cell (finding 3) + supersede markers (finding 4): shipped; NB36 executed green.
- A3b bit-identity proof added (max diff 0.0e+00 vs the git-extracted d52a138 core, tempo + coupling +
  clip-pinning forcings); lineage: the defect is verbatim 101b104 -> d52a138.
- Review rounds: Mode 1 = SHIP (round 3, stands - implementation diff unchanged since). Mode 2 rounds
  2-4 each answered with executed measurements (A4e stress +/-6, A4f stratified sample worst 0.023,
  A4f2 random 5% grid sample, A4g kBF band incl. the 8-region fate map). Round-5 Mode 2 pending on the
  re-executed NB36.
- Guard suite delivered: tests/test_hypothesis_guards.py (10 hypothesis-named regression guards);
  make test 62 passed, make lint clean.
- Journal (E40, Extended) + memory updates: pending the clean confirming round, then user commit approval.
- NEW standing work this session: E41 calibration-extension deep research running as workflow
  wf_9556fa9c-86a (9 observable families x 8 regions + synthesis + critics); fork session delivered the
  README "How the simulation actually works" section + scientific-methods.md revision.

---

## BRACE 2026-07-10 ~23:53 - E40 review loop CLOSED CLEAN; E41 Wave-2 workflow live at brace

### What survives on its own (valid on disk, no action needed)
- **E40 fully done and green**: `emergent.py` tempo fix (realized annual Δτ, floored) + PB_SCALE_ENS re-solved; NB36 (`notebooks/36-kj-rigor-audit-e40.ipynb`) re-executed green 47 cells 0 errors incl. record-faithful A8/A8b/A8c; NB17 fixed at source + green. `reports/nb36_e40_verdicts.json` carries A1-A8. `make test` 63 passed, `make lint` clean.
- **Adversarial review CLOSED**: 12-round Mode 2 Bedrock loop, **round 12 CLEAN** (`scratchpad/e40-review2r12-mode2-result.txt`, log `logs/e40-review2r12.log`). No uncarried claims; one non-blocking MINOR accepted as stated residual.
- **Records reconciled** (uncommitted, staged in working tree): experiments log E40 section incl. A8 lineage + round-12 CLEAN sentence + supersession rows with exact numbers (A8b shift 0.0155, A8c gating x4.5 vs x1.8, Poland shift 0.0031); `logs/README.md`; guard suite `tests/test_hypothesis_guards.py` (pins A1-A8).
- **Journal entry 51** written + `journal-tools check` exit 0. **Memory** synced (project-goals.md E40/E41 paragraphs; MEMORY.md israel index line extended).
- **E41 Wave-1 research** on disk: `reports/e41_calibration_targets_research.json`, `docs/e41-calibration-extension-research.md`, `docs/e41-acceptance-criteria.md`.

### DOWN / dies with this session
- **E41 Wave-2 blocker-resolution workflow `wf_53322579-da8`** (task id `w6ptbzwqt`) was RUNNING attached to this session at brace (last agent write 23:52). It is in its final bounded fix-loop stage - 12 resolvers + synthesis + first critique already DONE. **Its per-agent results ARE checkpointed** at:
  `/home/lab/.claude/projects/-home-lab-workspace-learning-projects-sci-demographic-collapse/c9898e9e-043d-4d91-9eb6-b5e80ecf9847/subagents/workflows/wf_53322579-da8/journal.jsonl` (each agent's StructuredOutput persisted as a `{"type":"result",...}` line; agent-*.jsonl are full transcripts).
  - Confirmed-good disposition already journaled: **C0F0** (C-construct infeasibility) RESOLVED-DESIGN - Korea PB0=0.93<1 collides with the Pb>=1 floor; feasibility boundary PB0>=~1.15; Korea decoupled to period-epoch pair C0=0.70/RV0=0.09 grounded in **Yoo 2026, Demographic Research 54(3)** (2023 tempo-adj marriage quantum). Floor RETAINED, no structural change.
- **DO NOT re-run the workflow from scratch.** If it did not return, reconstruct the 18-finding disposition table from `journal.jsonl` (read the `type:result` lines), THEN do the FIRST ACTION recordings. Re-running via `Workflow({scriptPath:"scratchpad/e41-wave2-workflow.mjs", resumeFromRunId:"wf_53322579-da8"})` returns cached agent results instantly for the unchanged prefix.

### FIRST ACTION for next session
1. Read `journal.jsonl` (path above); collect all 18 findings' dispositions (RESOLVED / AMENDED / ACCEPTED-RESIDUAL) + the synthesis's protocol_v2 + the two critics' re-verdicts.
2. Persist `reports/e41_blocker_resolutions.json` (the disposition table) + the synthesis result verbatim.
3. Update `docs/e41-calibration-extension-research.md` -> v2 (fold protocol_v2 + resolutions).
4. Flip `docs/e41-acceptance-criteria.md` W2.1-W2.8 statuses (MET where the disposition clears them).
5. Extend the experiments-log E41 section (append-only, W2.8) with the Wave-2 outcome.
6. If any critic still returned a BLOCKER -> loop the fix stage per protocol before declaring Wave 2 done.
7. Wave 3 (implementation: anchor replacement + guard re-baselining + additive harness + 2000->2023 rejection backtest) stays **USER-GATED** - do NOT start without explicit approval. Model stays untouched.

### Pending decision for the user
- **Commit approval**: the entire E40 + A8 + guard-suite + docs + journal + memory tree is uncommitted (working tree modified/untracked per `git status`). Awaiting explicit "commit"/"push". No git action taken.
- User asked to run executors on **Fable 5** (model set to Fable 5 this session); honour for future E41 executor waves unless overridden.
