# [Paper digest] A Global Perspective on Happiness and Fertility

**Authors**: Rachel Margolis, Mikko Myrskylä<br>
**Year**: 2011  **Venue**: Population and Development Review 37(1):29-56<br>
**Original (link)**: [https://www.demogr.mpg.de/publications/files/4061_1298610811_1_PDR-Happiness-Fertility-Margolis-Myrskyla.pdf](https://www.demogr.mpg.de/publications/files/4061_1298610811_1_PDR-Happiness-Fertility-Margolis-Myrskyla.pdf) (DOI 10.1111/j.1728-4457.2011.00389.x)<br>
**Local PDF**: `[paper] global happiness and fertility Margolis Myrskyla, 2011.pdf` (open-access author copy, Max Planck Institute)<br>
**Used in**: E42 HAPPINESS-FERTILITY core (how the happiness-fertility sign depends on age and context)

## Summary

World Values Surveys, 86 countries, N=201,988, happiness on a 1-4 scale regressed on number of children. Globally happiness falls with the number of children, but the sign is not fixed: it is negative for young adults, neutral in the 30s, and turns positive after age 40 - strongest where children are the old-age safety net (former-socialist and Southern Europe, low-fertility regimes). This is the paper that says the W-fertility coupling is a function of age and welfare context, not a constant.

## Parameters for the model

- **Raw number-of-children coefficients** (Model 1, no confounder controls; ref = childless): 1 child +0.041, 2 children +0.062, 3 children +0.060, 4+ children +0.002 (concave, peak at 2-3)
- **Controlled coefficients** (Model 2, adds income/SES/marital status; ref = childless): 1 child -0.032, 2 children -0.034, 3 children -0.026, 4+ children -0.055 (all p<.001) - net negative once marriage and income are held fixed
- **Effect size framing**: the childless-vs-1/2-child gap (~0.03) equals the male-female happiness gap (0.03); the childless-vs-4-child gap (0.06) equals the middle-vs-high-income gap (0.05); ~5-8% of a happiness SD
- **Age gradient (the key nonlinearity)**: under 30 happiness decreases ~monotonically with parity; at 30-39 the negative association vanishes; at 40-49 and 50+ it turns positive (three-or-more-children parents happiest)
- **Age main effects** (ref 15-19): ages 20-39 -0.111, age 40+ -0.181 (older people less happy overall, independent of children)
- **Income moderation**: the negative young-adult happiness-fertility slope is steepest for low income, weakest for high income; at 40+ no income difference
- **Partnership**: association is "remarkably similar" for partnered and unpartnered within each age band (partnership does not flip the sign)
- **Welfare-regime moderation**: young-adult negative slope weakest in social-democratic and conservative regimes; older-age positive slope strongest in former-socialist states
- **Fertility-level moderation**: the lower a country's TFR, the more positive the happiness-fertility link (selection of the child-valuing into parenthood); lowest-low (<1.3) countries lose the parity-3 decline
- **Comparison marital-status coefficients** (Model 2): separated/divorced -0.277, widowed -0.243, single -0.157, cohabiting -0.083 (all vs married) - partnership dissolution dwarfs the child effect

## Caveats

Cross-sectional WVS - associations, not causal; happiness is a 4-point item; the age gradient is an age-cross-section not a within-cohort trajectory, so "positive after 40" mixes selection (child-valuers keep having children) with genuine old-age support. Developing-country samples skew urban/wealthy. For the model: treat the W-fertility coupling coefficient as age-dependent, sign-flipping from negative (age<30) through zero (30s) to positive (40+), and scaled by welfare generosity and by how low the country's TFR already is.
