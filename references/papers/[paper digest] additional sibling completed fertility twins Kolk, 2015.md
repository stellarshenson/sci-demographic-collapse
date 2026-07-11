# [Paper digest] The causal effect of an additional sibling on completed fertility

**Authors**: Martin Kolk<br>
**Year**: 2015  **Venue**: Demographic Research 32(51), 1409-1420 (open access, CC-BY-NC)<br>
**Original (download)**: [https://www.demographic-research.org/volumes/vol32/51/32-51.pdf](https://www.demographic-research.org/volumes/vol32/51/32-51.pdf)<br>
**Local PDF**: `[paper] additional sibling completed fertility twins Kolk, 2015.pdf`<br>
**Used in**: E46 - the causal-vs-confounded test for the sibling/kin fertility channel

## Summary

Intergenerational transmission of fertility - a positive correlation between a person's number of siblings and their own adult number of children - is well established. This study asks whether that correlation is *causal* (growing up with more siblings makes you have more children) or *confounded* (families that produce many children share preferences and socioeconomic traits that also raise the next generation's fertility). It isolates causation with a twin instrument: a twin birth exogenously adds one extra sibling to a family, independent of parental preferences. Swedish administrative registers, ~300,000-360,000 individuals per sample.

## Key findings

- **Naive (OLS) association**: each additional sibling is linked to **+0.078 own children for first-born men and +0.096 for first-born women** (95% CI 0.074-0.082 and 0.092-0.100) - the standard confounded transmission correlation
- **Causal (2SLS, twin instrument)**: the exogenous effect collapses to **+0.041 (men, not significant, CI -0.011 to 0.093) and -0.042 (women, marginally significant, CI -0.091 to 0.006)** - essentially zero, and slightly negative for women
- First-stage twin instrument is strong (a twin birth raises parental fertility by ~0.79-0.84 children), so the null is not weak-instrument noise
- Across parities the pattern holds: 2SLS estimates are always far below the OLS correlations and straddle zero
- **Conclusion**: the sibling-count / own-fertility correlation is driven by shared family preferences and socioeconomic status, **not** by a causal effect of being raised among many siblings

## Relevance to this project

This is the central discipline on any "family size is self-reinforcing" channel. The raw correlation is real and moderate (~0.08-0.10 children per sibling) but almost entirely confounded - an exogenous extra sibling does not raise, and for women mildly lowers, completed fertility. The mild negative for women is consistent with resource dilution (Blake). For the model this means a sibling-parity feedback into `Pbar` cannot be justified as a structural causal channel; the observed clustering of large families is already captured by regional/preference heterogeneity, not by a within-generation sibling multiplier. A complementary Kolk dissertation PDF (2014, multigenerational correlations) is already in the library.

## Tags

`#sibling-effects` `#intergenerational-transmission` `#resource-dilution` `#confounding` `#causal-inference` `#counter-evidence` `#parity`
