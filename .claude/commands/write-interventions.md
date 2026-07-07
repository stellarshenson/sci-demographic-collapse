# Write Interventions Table

Regenerate the decision-maker intervention ranking from **current** campaign data, and write it to `docs/interventions.md`. This replaces the old hand-maintained doc that drifted stale - never hand-edit the output; always regenerate here so counts, effects and verdicts stay current.

## Read first (the source of truth)

- `docs/experiments/demographic-collapse-experiments.md` - every batch's verdicts, the campaign total, the honest SUPPORTED / PARTIAL / REFUTED mix
- `reports/nb15_harbinger_table.csv`, `reports/nb16_e22_verdicts.json`, and any later `reports/*verdicts*.json` / `reports/*table*.csv` - effect (ΔTFR), composite cost, efficiency, fate
- `docs/demographic-collapse-sota.md` - the distilled winning design

Pull the numbers from these files - do not invent or recall them. If a lever has no modelled ΔTFR, say so rather than guessing.

## Output - `docs/interventions.md`

A `technical-documentation` skill (modus secundis) document: a one-line overview, the star rubric, then the table. Terse, declarative, numbers inline, escape `\$`, no full stop at the end of a bullet, unicode arrows `→`.

### Table columns

| Intervention | Mechanism of effect | Effect (ΔTFR, direction + magnitude) | Cost to society (fiscal / coercion / side-effect) | Side-effects | Evidence | ★ (0-5) | Verdict |

- Sort by ★ then by effect; group into tiers where it helps the reader (harbingers / structural / dominated)
- Mechanism of effect is a concrete cause→parameter→birth chain, not a slogan (an adversary axis will check this)
- Effect and cost are real numbers from the reports; where a value is a composed proxy, mark it `(proxy)` and name the component evidence briefly

### Star rubric (0-5) - decision-maker value, stated at the top so the rating is auditable

- ★★★★★ - large effect, cheap, well-evidenced, SUPPORTED, low side-effects (e.g. cohabitation recognition, inequality compression)
- ★★★★ - strong effect or excellent value-per-cost, SUPPORTED, minor caveats
- ★★★ - real but moderate, conditional, or PARTIAL; or strong-but-costly
- ★★ - weak, thin evidence, or notable side-effects
- ★ - marginal, mostly tempo, or near-null
- ☆ (0) - REFUTED or backfires (cash bonuses, tutoring bans, top-down propaganda)

Stars combine effect size, cost-efficiency, evidence strength and verdict.

## After writing

1. Run `/adversarial-review` with the **popular-science** adversary over `docs/interventions.md` - hunt vague magnitudes ("a lot", "about a third"), generic mechanisms with no worked example, uneven rows, and any unsourced claim; apply the fixes
2. Foot the doc with the campaign total and the date, and a line that it is generated - "regenerate with `/write-interventions`, do not hand-edit"
