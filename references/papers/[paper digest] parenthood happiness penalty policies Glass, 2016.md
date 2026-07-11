# [Paper digest] Parenthood and Happiness: Effects of Work-Family Reconciliation Policies in 22 OECD Countries

**Authors**: Jennifer Glass, Robin W. Simon, Matthew A. Andersson<br>
**Year**: 2016  **Venue**: American Journal of Sociology 122(3):886-929, University of Chicago Press<br>
**Original (link)**: [https://pmc.ncbi.nlm.nih.gov/articles/PMC5222535/](https://pmc.ncbi.nlm.nih.gov/articles/PMC5222535/) (DOI 10.1086/688892)<br>
**Local PDF**: `[paper] parenthood happiness penalty policies Glass brief, 2016.pdf` - the 3-page UT-Austin Population Research Center research brief (open access); full-article numbers below extracted from the open PMC author manuscript<br>
**Used in**: E42 HAPPINESS-FERTILITY core (parenthood happiness penalty and its policy moderation)

## Summary

Pools comparable adult happiness data across 22 OECD countries (International Social Survey Programme + US General Social Survey) and asks why parents report lower happiness than nonparents in some countries but not others. The parenthood happiness gap is not biological or universal - it tracks the generosity of work-family reconciliation policy. Where paid leave, subsidised childcare and paid sick/vacation time are strong, the penalty vanishes or reverses to a bonus, and crucially those same policies do not lower nonparents' happiness.

## Parameters for the model

- **Parenthood happiness gap, US (largest penalty)**: -0.127 on the logged happiness scale - the reference maximum
- **Countries with a positive parent bonus** (parents happier): Portugal +0.077, Hungary +0.046, Spain +0.031, Norway +0.020, Sweden +0.019, Finland +0.015, France +0.011, Russia +0.007 (all p<.001)
- **Countries with a negative gap** (besides US): Ireland -0.100, Greece -0.087, UK -0.083, New Zealand -0.082, Switzerland -0.070, Poland -0.050, Australia -0.041, Denmark -0.028, Netherlands -0.022; near-zero: Germany -0.006, Belgium -0.001
- **Range of the cross-country gap**: roughly -0.13 (US) to +0.08 (Portugal), i.e. a policy-driven swing of about 0.20 happiness units
- **Policy cross-level interaction coefficients** (effect on the parent-vs-nonparent gap):
  - Paid vacation + sick leave days: b = +0.00329 (SE 0.00116, p<.01) - moving this lever reversed a modeled gap from -0.057 to +0.025
  - Paid parental leave (weeks, generosity): b = +0.0190 (SE 0.0106, p<.05)
  - Paid leave for mothers: b = +0.0134 (SE 0.0084, p<.10)
  - Childcare cost (% of median wage): b = -0.00379 (SE 0.00123, p<.001) - cutting cost from 24.7% to 4.5% of wage raised parental happiness by +0.081
  - Work flexibility: b = -0.00422 (SE 0.00221, p<.05) - the one policy that did NOT help parents more than nonparents
  - Comprehensive Policy Index (CPI): b = +0.0402 (SE 0.0163, p<.01) - fully eliminates the parenthood penalty in high-policy nations
- **Explained variation**: the authors state national policy context "explains up to 100%" of the within-nation parenthood happiness disadvantage
- **No cost to nonparents**: policy main effects on nonparents are zero-to-positive (CPI b = +0.127, p<.001; work flexibility +0.0124, p<.01); "no group of adults reported lower happiness in the presence of policies"

## Caveats

Cross-sectional and observational - coefficients are associations, not experimental effects; the happiness scale is coarse (ISSP/GSS items) and the gap magnitudes (~5-8% of a SD) are small in absolute terms though policy-sized. The penalty is a period snapshot, not a within-person trajectory (contrast Clark 2008 adaptation). Use the country gap values as the level term W_parent - W_nonparent and the CPI/childcare coefficients as the policy moderator on that gap.
