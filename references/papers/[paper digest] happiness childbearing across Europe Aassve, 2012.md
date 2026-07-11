# [Paper digest] Happiness and Childbearing Across Europe

**Authors**: Arnstein Aassve, Alice Goisis, Maria Sironi<br>
**Year**: 2012  **Venue**: Social Indicators Research 108(1):65-86, Springer<br>
**Original (link)**: [http://discovery.ucl.ac.uk/1490241/1/Aassve_AAM_happiness_and_childbearing_across_europe.pdf](http://discovery.ucl.ac.uk/1490241/1/Aassve_AAM_happiness_and_childbearing_across_europe.pdf) (DOI 10.1007/s11205-011-9866-x)<br>
**Local PDF**: `[paper] happiness childbearing across Europe Aassve, 2012.pdf` (open-access accepted manuscript, UCL Discovery / Dondena WP)<br>
**Used in**: E42 HAPPINESS-FERTILITY core (the first birth is where the happiness gain concentrates; extensive vs intensive margin)

## Summary

European Social Survey (three rounds 2002-2006, ~14 countries), happiness on a 0-10 scale. Decomposes the child-happiness link into the extensive margin (having at least one child) versus the intensive margin (additional children beyond the first). The happiness gain is real but concentrated in the first child and in partnership; extra children add little, and the pattern differs sharply by gender - working fathers are happier, working mothers are not.

## Parameters for the model

- **Number-of-children coefficient** (happiness 0-10 scale): men +0.028 (p<.05), women +0.025 (p<.01) - small positive
- **Extensive margin "at least one child"** (with controls): men +0.074 (p<.01), women +0.042 (p<.05)
- **Intensive margin "additional children beyond the first"** (parents only): men +0.001 (ns), women +0.014 (p<.01) - the second+ child adds essentially nothing for men and little for women
- **Partnership** (strongest covariate): men +0.386 to +0.408, women +0.379 to +0.430 (p<.001) - an order of magnitude larger than the child effect
- **Working**: men +0.237 to +0.249, women only +0.084 to +0.110 (p<.001) - working fathers gain ~2-3x what working mothers do; a gendered penalty
- **Annual household income**: +0.04 to +0.077 (per 10,000, p<.001)
- **Years of education**: +0.012 to +0.018 (p<.05)
- **Age**: negative linear (-0.05 to -0.07) with positive quadratic (age^2 +0.005 to +0.007) - the familiar U-shape in age
- **Sample**: males N ~21,856; females N ~23,662; reference country Denmark; SEs clustered within country; significant cross-country heterogeneity

## Caveats

Cross-sectional ESS pooled - associations not causal, and the first-child coefficient likely conflates selection (happier/partnered people have the first child) with a causal boost; the authors flag that first-child motivations differ from higher-order ones. Country dummies absorb much of the cross-national story. For the model this pins the extensive margin (0 -> 1 child) as the locus of the happiness gain, near-zero returns to the intensive margin, and a structural gender asymmetry in how employment interacts with parenthood happiness.
