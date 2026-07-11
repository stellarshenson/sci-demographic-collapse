# [Paper digest] Economic Recession and Fertility in the Developed World

**Authors**: Tomáš Sobotka, Vegard Skirbekk, Dimiter Philipov<br>
**Year**: 2011  **Venue**: Population and Development Review 37(2):267-306, Wiley<br>
**Original (link)**: [https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1728-4457.2011.00411.x](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1728-4457.2011.00411.x) (DOI 10.1111/j.1728-4457.2011.00411.x)<br>
**Local PDF**: none - **paywalled** (Wiley/PDR); **digest-only**, parameters read from the published text and its cited studies<br>
**Used in**: E42 HAPPINESS-FERTILITY core (fertility responding to DETERIORATING conditions - the derivative and its lag, pairs with Kahneman-Tversky asymmetry)

## Summary

Literature review of how economic downturns move fertility in developed countries. Recessions depress fertility mainly through unemployment and economic uncertainty (not GDP level per se), the response is pro-cyclical, concentrated in young adults and first births, and it operates with a short lag. The bulk of the effect is tempo (postponement) that is largely recuperated later, but deep or prolonged recessions can leave a permanent quantum dent - the empirical counterpart to the loss-averse, change-driven response.

## Parameters for the model

- **Downturn asymmetry (odds)**: following a year of falling GDP, the period TFR declined in ~four-fifths of country-years, odds ratio of decline **4.2**; under stagnation (GDP growth <1%) TFR fell in two-thirds of 60 observations; with GDP growth >=1% rises and falls were about equal
- **GDP-TFR correlation (weak, lagged)**: pooled r = 0.25 at a **1-year lag**, 0.05 at 2-year lag (0.38 excluding the Finland outlier) - GDP is a blunt indicator; unemployment is sharper
- **Unemployment -> fertility**: Örsal & Goldstein (2010), 22 OECD 1976-2008 - both male and female unemployment depress period TFR, effect pro-cyclical and growing over time (esp. for women); long-term MALE unemployment strongly cuts first births, short-term unemployment barely matters
- **Norway (Kravdal 2002)**: rising unemployment reduced the period TFR by **0.08** in the ~1993 recession, dominated by the aggregate (climate) effect over individual job loss; unemployment depressed 1st and 2nd births but RAISED 3rd/4th births among men
- **Sweden (Santow & Bracher 2001)**: first-birth conception rates **-21%** in recession years vs non-recession, net of controls
- **Consumer confidence (Netherlands, Fokkema 2008)**: +10 index points -> TFR +0.04 (half first births, half second), **2-year lag**; van Giersbergen: +10 points -> +~3,000 births/yr (~1.5% of births), 2.25-yr lag
- **Latvia 2008-2010 (natural experiment)**: unemployment 5% -> 20%; TFR 1.44 (2008) -> 1.16 (2010), a ~-0.28 drop; births tracked unemployment with a lag of only **9 months**
- **Lag structure**: fertility response to unemployment shows at ~9 months to ~1-2 years (pregnancy + reaction time); consumer-confidence effects ~2-2.25 years
- **Who responds**: young adults (<25-30), the childless, and the highly educated postpone first births most; least-educated women can show a small POSITIVE first-birth response to unemployment/low life satisfaction (Kreyenfeld) - a coupling sign that flips by education
- **Life-satisfaction interaction**: low life satisfaction + unemployment + economic worries sharply cut first births among highly educated women (direct SWB -> fertility link inside the recession channel)
- **Tempo vs quantum**: most recession effect is postponement, largely recuperated at older ages; historically the US Great Depression cut period fertility sharply but cohort completed fertility recovered - deep/long recessions risk permanent quantum loss

## Caveats

Review, not a single estimated model - the numbers are assembled from many country studies with different methods, so there is no one clean elasticity; effects vary by welfare regime (generous unemployment benefits blunt the loss), self-employment share, and education. For the model: encode a pro-cyclical, lagged (~9-24 month) response of first- and second-birth hazards to rising unemployment, mostly tempo (recuperable), asymmetric per Kahneman-Tversky, with an education-dependent sign and a magnitude on the order of TFR -0.08 to -0.28 for a severe unemployment shock.
