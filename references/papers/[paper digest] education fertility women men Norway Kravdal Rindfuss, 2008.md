# [Paper digest] Changing Relationships between Education and Fertility: Women and Men Born 1940-1964

**Authors**: Øystein Kravdal, Ronald R. Rindfuss<br>
**Year**: 2008  **Venue**: American Sociological Review 73(5): 854-873, DOI 10.1177/000312240807300508<br>
**Original**: [SAGE](https://journals.sagepub.com/doi/10.1177/000312240807300508) (paywalled)<br>
**Local PDF**: digest-only, no OA PDF - ASR 2008 is paywalled at SAGE and no author manuscript is openly downloadable; digest written from the public abstract plus the citing literature (companion PNAS 2011 Cohen-Kravdal-Keilman; Jalovaara 2019)<br>
**Used in**: E42 education-fertility arm - Norwegian register evidence that the education-fertility sign is time-varying and sex-specific

## Summary

Norwegian population registers cover complete childbearing histories for cohorts born 1940-1964, letting the authors measure how the education-fertility link changed as female education expanded. For women the historically strong negative relationship between education and completed fertility became *substantially less negative*: better-educated women still start later and are childless more often, but the negative effect of education on higher-order (second- and third-) birth rates - net of the later start - has essentially disappeared. For men the relationship turned *positive*: the better educated father children later but are less often childless, and education increasingly *raises* second- and third-birth rates. The companion analysis (PNAS 2011) makes the reverse-causation point sharply - among Norwegian women, childbearing impeded education more than education impeded childbearing. Together these ground the claim that "education lowers fertility" is a dated, partial, and reversible regularity.

## Parameters for the model

- **Data**: Norwegian registers, birth cohorts **1940-1964**; completed fertility measured at **age 39** (women)
- **Women - completed fertility gradient**: negative but **"substantially less negative"** across the 1940->1964 cohorts (the educational gap in completed fertility narrows over time) -> declining magnitude of a negative coefficient, trending toward zero
- **Women - higher-order births**: the negative effect of education on 2nd/3rd birth rates, net of later first-birth timing, has **disappeared** -> once you condition on tempo (τ), education is roughly neutral on continuation
- **Women - first-birth timing / childlessness**: better-educated women still have **later first births and higher childlessness** -> education loads on the tempo and childlessness channels, not on quantum-per-mother
- **Men - gradient**: **positive** - better educated father later but are **less often childless**, with an "increasingly stimulating effect of education on second- and third-birth rates" -> positive education->fertility coefficient for men, strengthening across cohorts
- **Direction of causation (companion PNAS 2011)**: for Norwegian women, **childbearing impeded education more than education impeded childbearing** - caution against reading the education->fertility correlation as one-way causal

## Model wiring

- Reinforces the sex-split from Jalovaara: female education coefficient decays toward zero over cohorts; male education coefficient is positive
- Separate the education effect into (a) a tempo/childlessness load and (b) a near-zero quantum-per-mother effect once tempo is controlled - do not double-count education as both delaying and reducing continuation
- The reverse-causation caveat argues for treating enrolment (a state, per Ní Bhrolcháin & Beaujouan) rather than attainment as the timing driver

## Caveats

- Hard coefficient values (exact CTF by education level, childlessness percentages) are behind the paywall and are NOT reproduced here - the parameters above are directional/sign magnitudes drawn from the abstract and citing works; do not quote point estimates
- Norway only (early, strong-welfare adopter) - a leading-edge case for the female-gradient attenuation, may lead other countries by decades
- Cohorts end at 1964; more recent reinforcement comes from Jalovaara 2019 (same digest set)
