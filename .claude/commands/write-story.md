# Write Story

Regenerate the popular-science narrative of the project for a curious, busy, educated generalist. The narrative lives in `README.md` - there is no separate `story.md` (it was retired). Refresh the story beats from **current** findings; keep it a flowing essay that survives an educated reader, not a reference dump.

## Read first

- `docs/experiments/demographic-collapse-experiments.md` - findings, verdicts, campaign total
- `docs/demographic-collapse-sota.md` - the distilled design
- `reports/figures/story_*.png` - the four story visuals to embed (two-futures-and-a-ridge, what-collapse-looks-like, the-one-lever-that-bends, the-cheapest-fixes)

## Style (Modus Primaris, popular science)

- Flowing narrative for a non-specialist - tell the story, do not list reference material
- Every empirical claim carries a source `(Author, year)` or "our model finds" - no bare assertions
- Real numbers, never "a lot" / "about a third" - name the effect size, the sample, the comparison
- No em-dashes (use ` - `); escape `\$`; unicode arrows `→`; split long paragraphs into short ones
- Honest register throughout - a rigorous map, not a crystal ball; name the caveats

## Beats to keep and refresh

1. Asimov / psychohistory hook
2. Two futures and a very narrow ridge - embed `story_two_futures.png` (or the Seldon manifold)
3. What collapse actually looks like - embed `story_collapse.png`
4. Why it happens; the hidden clock (momentum)
5. The one fast lever (marriageable men, income **not** degrees) and the slow ones that actually work
6. The cheapest fixes - the star harbingers, each with a concrete mechanism, a real number, and one worked example
7. The honest ending (position and timing decide fate)
8. How we got here - the honest methodology (equations rebuilt more than once, recalibrated until the baseline re-tells history, a large share PARTIAL/REFUTED)
9. Mature research or a toy? - the honest verdict

## After writing

Run `/adversarial-review` with the **popular-science** adversary over the README narrative and apply every axis it raises - jargon, names-without-context, unsourced claim, false vagueness, generic mechanism with no example, vague magnitude where a number exists, argument-as-bullets, uneven list, buried lede, wall-of-text, broken translation. Iterate until it passes clean.
