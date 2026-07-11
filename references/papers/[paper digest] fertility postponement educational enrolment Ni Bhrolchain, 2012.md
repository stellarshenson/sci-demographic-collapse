# [Paper digest] Fertility postponement is largely due to rising educational enrolment

**Authors**: Máire Ní Bhrolcháin, Éva Beaujouan<br>
**Year**: 2012  **Venue**: Population Studies 66(3): 311-327, DOI 10.1080/00324728.2012.697569<br>
**Original (open access)**: [PMC3479627](https://pmc.ncbi.nlm.nih.gov/articles/PMC3479627/) (author manuscript, ESRC Centre for Population Change) - also T&F full text<br>
**Local PDF**: not saved - the OA article is Cloudflare/render-blocked from this environment; digest written from the OA PMC full text. Open copy at the PMC link above<br>
**Used in**: E42 education-fertility arm - the enrolment-"incarceration" mechanism on first-birth timing (tempo channel τ)

## Summary

The paper decomposes the well-known rise in the mean age at first birth in Britain and France into two pieces: the part explained by young people simply staying in education longer (people rarely have a first child while still enrolled - the enrolment "incarceration" effect) and the residual behavioural postponement that happens *after* leaving education. Using the British General Household Survey (2000-2007 rounds) and the French Family History Survey linked to the 1999 census, the authors show that most of the postponement across 1980-84 to 1995-99 is a mechanical consequence of extended enrolment, not of couples choosing to wait longer once their education is finished. The interval from end-of-education to first birth barely moved. The policy-relevant implication: educational expansion alone reproduces most of the observed tempo shift.

## Parameters for the model

- **Study window**: birth-cohort period 1980-84 to 1995-99 (mean age at first birth compared between these windows)
- **Share of first-birth postponement explained by rising enrolment**:
  - Britain: **57%** ((1.4 - 0.6)/1.4)
  - France: **79%** ((2.4 - 0.5)/2.4)
- **Total rise in mean age at first birth over the window**: Britain **+1.4 years**; France **+2.4 years**
- **Residual post-enrolment (behavioural) component of the rise**: Britain **+0.6 years**; France **+0.5 years** - i.e. the delay between finishing education and first birth increased only ~0.5-0.6 yr
- **Rise in mean age at end of education** (the driver): Britain **+1.4 years** (18.3 in 1980-84 -> 19.7 in 1995-99); France **+1.8 years** (19.8 -> 21.6)
- **Implied transmission ratio (tempo pass-through)**: roughly **1 year later first birth per ~1 year of extra enrolment** in Britain (1.4 enrolment rise vs 0.8 enrolment-attributable birth-age rise -> ~0.57), and in France the enrolment-attributable rise (1.9 yr) exceeds the enrolment-duration rise (1.8 yr), i.e. pass-through near or above 1

## Model wiring

- Route the education channel's effect on the tempo term τ (age at first birth) primarily through *enrolment duration*, not through a free behavioural-delay parameter: a rise in mean age at end of education feeds first-birth age near 1:1
- Sets a ceiling on how much of the first-birth-age rise the model should attribute to preference/behaviour change: only ~20-45% is post-enrolment behaviour; ~55-80% is mechanical enrolment
- Cross-country: France shows a larger and more complete enrolment pass-through than Britain - use as the high vs moderate anchor for the enrolment->tempo coupling

## Caveats

- Britain and France only; not directly estimated for the eight study countries - use as a mechanism/elasticity prior, not a country calibration
- Concerns *timing* (tempo), not completed quantum - says nothing about whether postponement lowers final family size
- Percentages are simple decompositions of aggregate shifts, not regression coefficients with confidence intervals
- Mean age at end of education is survey-measured (self-report of leaving continuous education)
