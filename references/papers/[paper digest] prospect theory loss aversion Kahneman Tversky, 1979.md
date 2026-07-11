# [Paper digest] Prospect Theory: An Analysis of Decision under Risk (loss aversion, reference dependence)

**Authors**: Daniel Kahneman, Amos Tversky<br>
**Year**: 1979 (loss-aversion coefficient refined in Tversky & Kahneman 1992, "Advances in Prospect Theory")<br>
**Venue**: Econometrica 47(2):263-291 (1979); Journal of Risk and Uncertainty 5:297-323 (1992)<br>
**Original (link)**: [https://www.uzh.ch/cmsssl/suz/dam/jcr:00000000-64a0-5b1c-0000-00003b7ec704/10.05-kahneman-tversky-79.pdf](https://www.uzh.ch/cmsssl/suz/dam/jcr:00000000-64a0-5b1c-0000-00003b7ec704/10.05-kahneman-tversky-79.pdf) (DOI 10.2307/1914185)<br>
**Local PDF**: none saved - foundational theory paper, **digest-only** (widely available); included for the mechanism, not new data<br>
**Used in**: E42 HAPPINESS-FERTILITY core (why fertility responds to the DERIVATIVE - deteriorating vs improving conditions - asymmetrically, not to the level)

## Summary

Prospect theory replaces expected-utility's absolute-wealth argument with value defined over GAINS and LOSSES relative to a reference point. Two features matter for the model: reference dependence (people evaluate change, not level) and loss aversion (losses loom larger than equivalent gains). Applied to fertility, this is the formal basis for making childbearing respond to the change in conditions relative to an adapted baseline, with downturns cutting fertility harder than equal-sized upturns raise it.

## Parameters for the model

- **Loss-aversion coefficient lambda**: median ~2.25 (Tversky & Kahneman 1992) - a loss is felt ~2-2.5x as strongly as an equal-sized gain; common modelling range lambda = 2.0-2.5. This sets the asymmetry ratio for a downturn-vs-upturn fertility response
- **Value-function curvature (diminishing sensitivity)**: exponent alpha = beta ~= 0.88 for both gains and losses (v(x)=x^0.88 for gains, -lambda*(-x)^0.88 for losses) - concave in gains, convex in losses, kink at the reference point
- **Reference dependence**: the argument of value is the deviation from a reference point, not the absolute level - couples judge their situation against an adapted baseline (couples with Clark 2008: the reference point is the adapted W set-point, updated on a ~1-2 year timescale)
- **Probability weighting** (secondary here): small probabilities overweighted, moderate-to-large underweighted (weighting parameter ~0.61-0.69) - relevant if modelling perceived risk of economic shocks
- **Modelling use**: drive the fertility response off d(conditions)/dt relative to reference, apply the kinked value function with lambda ~= 2.25, so a recession of size s suppresses fertility ~2.25x more than a boom of size s raises it - the source of the recession-fertility asymmetry Sobotka 2011 documents empirically

## Caveats

Individual-choice lab theory, not a demographic model - the lambda ~= 2.25 and alpha ~= 0.88 come from monetary-gamble experiments and are used here as a plausible functional form, not a fertility-specific estimate. The reference point's update rule is a modelling choice; pairing it with Clark's adaptation timescale is the disciplined way to set it. Treat as the theoretical scaffold for asymmetric, change-driven coupling, to be calibrated against the empirical recession elasticities in the Sobotka digest.
