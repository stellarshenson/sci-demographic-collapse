# [Paper digest] Education, Gender, and Cohort Fertility in the Nordic Countries

**Authors**: Marika Jalovaara, Gerda Neyer, Gunnar Andersson, Johan Dahlberg, Lars Dommermuth, Peter Fallesen, Trude Lappegård<br>
**Year**: 2019  **Venue**: European Journal of Population 35: 563-586, DOI 10.1007/s10680-018-9492-2 (open access)<br>
**Original (download)**: [Springer OA](https://link.springer.com/article/10.1007/s10680-018-9492-2)<br>
**Local PDF**: `[paper] education gender cohort fertility Nordic Jalovaara, 2019.pdf`<br>
**Used in**: E42 education-fertility arm - the education-fertility gradient REVERSAL by sex (the sign of the education coefficient is not fixed)

## Summary

Harmonised national-register data for Denmark, Finland, Norway and Sweden track completed cohort fertility (CTF) and ultimate childlessness for cohorts born from 1940, by sex and educational level. The headline: the classic *negative* education gradient for women's fertility has essentially vanished (except Finland), while men's *positive* gradient has persisted throughout. Childlessness has flipped - once highest among the most-educated women, it is now highest among the *least*-educated women in Denmark, Norway and Sweden; for men it has always been highest among the least educated. Nordic cohort fertility itself stayed remarkably stable near replacement across cohorts even as period TFR swung, because postponed births are recuperated at older ages. The finding refutes any model that hard-codes education as a uniformly fertility-depressing force: at the population scale the sign depends on sex and institutional context.

## Parameters for the model

- **Cohorts**: born 1940 to 1972/74 (women) / 1940 to 1967/69 (men); 5-year cohort groups (3-year for the youngest Finland/Sweden)
- **Outcome ages**: CTF and childlessness measured at **age 40 for women, age 45 for men**
- **Cohort total fertility band (all four countries)**: roughly **1.6 to 2.1**; women's CTF stayed close to replacement (~2.0-2.1); Danish men lowest at **~1.6** (near the 1.5 "very low" threshold, Kohler et al. 2006)
- **Women's education gradient in CTF**: negative gradient has **vanished** in Denmark, Norway, Sweden (flat/near-zero); **still weakly negative only in Finland** -> use education coefficient on female quantum ≈ 0 for high-gender-equity contexts
- **Men's education gradient in CTF**: **persistently positive** across all cohorts -> keep a positive education->fertility coefficient for men
- **Childlessness reversal (women)**: oldest cohorts childlessness highest among *highly* educated; recent cohorts highest among *least* educated (DK, NO, SE) - the sign of the education->childlessness slope flips across cohorts
- **Childlessness (men)**: highest among **least educated** in every cohort (stable)
- **Measurement-window sensitivity** (from footnote): adding ages 46-50 for recent male cohorts would add ~**0.03-0.04** children to CTF and cut male childlessness by ~**0.5-0.6 pp** (women ~**0.9-1.0 pp**) - small; age-40/45 truncation is a minor bias

## Model wiring

- Do NOT fix the education->fertility coefficient as negative; make it **sex-specific and context-modulated**: near-zero/flat for women under high gender equity, positive for men, weakly negative only where female second-shift/opportunity cost stays high (Finland-type)
- Route the modern education signal into *childlessness at the low end* (least-educated exclusion) rather than into fewer births among the educated - a compositional, not a quantum-depressing, channel
- Supports the "structure beats a single education dial" prior: cohort fertility can hold near replacement while the education distribution shifts massively

## Caveats

- Four Nordic (high gender-equity, strong family-policy) countries only - the vanished female gradient is context-specific and may not transfer to Italy/Japan/Korea
- Register CTF is descriptive by education level, not a causal effect of education
- Values read from the paper's figures are bands (charts, not a coefficient table); treat the CTF numbers as ranges
