# [Paper digest] Why did Rich Families Increase their Fertility? Inequality and Marketization of Child Care

**Authors**: Michael Bar, Moshe Hazan, Oksana Leukhina, David Weiss, Hosny Zoabi<br>
**Year**: 2018  **Venue**: Journal of Economic Growth 23(4): 427-463, DOI 10.1007/s10887-018-9160-8<br>
**Original (open access working paper)**: [Federal Reserve Bank of St. Louis WP 2018-022A](https://research.stlouisfed.org/wp/more/2018-022)<br>
**Local PDF**: `[paper] rich families fertility inequality marketization Bar Hazan, 2018.pdf` (St. Louis Fed WP 2018-022A, 61 pp)<br>
**Used in**: E42 education-fertility arm - the flattening / U-shape of the income (and education) fertility relationship, and the marketization channel

## Summary

The paper documents that the long-standing *negative* cross-sectional relationship between income and fertility in the US **flattened between 1980 and 2010** - a period of rising inequality - because high-income (and highly educated) families *raised* their fertility. This breaks the standard Beckerian prediction that widening inequality should widen the rich-poor fertility gap in the usual direction. The proposed mechanism is **marketization of parental time**: when high-earning women can buy child-care and household services (nannies, cleaning, prepared food) cheaply relative to their own wage, the effective cost of an extra child falls fastest for the rich, so their fertility rises and the income-fertility curve becomes flat or even U-shaped (rising at the top). A calibrated model reproduces the pattern and yields a sharp policy corollary: raising the cost of that marketized care (e.g. a higher minimum wage) *lowers* the fertility and labour supply of high-income women.

## Parameters for the model

- **Window**: US, **1980 to 2010**; fertility measured as children ever born (CEB), married native-born couples, tabulated by 10 income deciles and by education
- **Shape shift**: 1980 income-fertility relationship clearly **negative**; by 2010 it is **flat, even U-shaped** - unchanged for the bottom half, rising from about the **5th decile up**, most pronounced in the **9th-10th deciles**
- **Fertility rise, top two income deciles, 1980->2010**: **+43.5%** (model **+40%**)
- **Differential fertility (top-two deciles vs 2nd decile)**: **+41%** (model +38.5%) over the same window
- **Education correspondence**: the fertility increase among the **most-educated women** closely tracks the increase among the top income deciles - education and income U-shapes coincide
- **Marketization price pass-through**: a **\$1** rise in the state minimum wage raises home-production-substitute (HPS) sector wages by about **\$0.58** (IV estimate) - i.e. ~58% pass-through to the price of marketized child care
- **Policy elasticity (sign)**: raising the minimum wage (toward \$15/hr in the counterfactual) **reduces** the labour supply and fertility of high-income women - marketization cost and top-decile fertility move in opposite directions

## Model wiring

- Make the education/income->fertility coefficient **non-monotone**: allow a U-shape so the top of the distribution can have a *positive* slope, rather than forcing education/income to depress fertility everywhere
- Add a **marketization affordability** term = (top-decile wage) / (care-sector wage): when it rises, high-education fertility rises; a floor on care wages (minimum wage) is a counter-lever that suppresses it
- Connects to the inequality/Doepke lever already in the campaign: marketization is the channel by which inequality can be *pro-natal at the top* while still anti-natal in the middle
- The +43.5% top-decile rise is a bound on how much the rich-educated recovery can contribute in a US-type calibration

## Caveats

- US only, married native-born couples; the marketization channel depends on a large low-wage care-labour supply (immigration-fed) - weaker where such labour is scarce or care is publicly provided
- Structural calibrated model - the counterfactuals (minimum wage -> fertility) are model-based, not reduced-form causal estimates
- "Fertility" here is completed CEB in a cross-section by income, not a period TFR; maps to quantum, not tempo
- The mechanism concerns the *top* of the distribution; it does not lift middle- or low-income fertility
