# [Paper digest] Methods for Detecting Early Warnings of Critical Transitions in Time Series

**Authors**: Vasilis Dakos, Stephen R. Carpenter, William A. Brock, Aaron M. Ellison, Vishwesha Guttal, Anthony R. Ives, Sonia Kefi, Valerie Livina, David A. Seekell, Egbert H. van Nes, Marten Scheffer<br>
**Year**: 2012  **Venue**: PLoS ONE 7(7):e41010, DOI 10.1371/journal.pone.0041010 (open access, CC-BY)<br>
**Original (download)**: [https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0041010&type=printable](https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0041010&type=printable) (fully OA)<br>
**Local PDF**: `[paper] early warning signals critical transitions methods Dakos, 2012.pdf` (in this folder)<br>
**Used in**: stochastic-tipping / early-warning round on the bistable social-norm (double-well) channel - the practical toolbox and significance-testing recipe that operationalises Scheffer 2009 on a simulated trajectory

## Key mechanism

Same theory as Scheffer 2009 (critical slowing down before a fold), but this is the **methods paper**: it assembles every proposed leading indicator, sorts them into metric-based and model-based families, and applies them to two time series simulated from a harvested-resource model that is known to undergo a fold. The controlled setup makes it the reference for *how to compute and validate* early warnings on a simulated N trajectory, which is exactly the demographic-norm use case.

## Main findings

- Two simulated benchmarks: a **critical slowing down (CSD)** dataset (grazing `c` ramped 1 → 2.677 over 1,000 steps, shift at ~step 970) and a **flickering** dataset (10,000 steps plus time-correlated red-noise inflow), both with added measurement error
- **No single best indicator** - each method needed dataset-specific treatment; a *combination* of metric-based and model-based indicators is the robust route
- Cross-validating families reduces false alarms: a rise in external noise inflates **variance** indicators but not **memory** (AR1) indicators, so agreement between the two is stronger evidence than either alone

## Exact indicators (metric-based)

- **Lag-1 autocorrelation** `r1 = E[(z_t − m)(z_{t+1} − m)] / σ²`; equivalently the AR(1) coefficient `a1` in `z_{t+1} = a1·z_t + e_t` (`r1` and `a1` are mathematically equivalent). **Return rate** = `1/a1` (or `1 − a1`, the fraction of the excursion decaying per step) - falls toward zero at the transition
- **Detrended fluctuation analysis (DFA)** exponent - power-law fluctuation function `F(s) ∝ s^α`, rescaled to reach 1 at transition; needs > 100 points
- **Spectral** measures - reddening (power shifts to low frequency), spectral exponent (log-log slope), spectral ratio (density at 0.05 vs 0.5)
- **Variance** - `SD = sqrt( (1/(n−1)) Σ (z_t − m)² )` or coefficient of variation `CV = SD/m`; rises from both slowing down and flickering
- **Skewness** - standardized third moment; rises near an asymmetric basin boundary but **may increase or decrease** depending on whether the alternative state is above or below the present one
- **Kurtosis** - leptokurtic tails as extreme excursions become likelier before the shift
- Model-based family: **conditional heteroskedasticity**, **BDS test**, time-varying **AR(p)**, nonparametric **drift-diffusion-jump**, threshold AR(p), and **potential analysis** (locating potential wells / bimodality)

## How to compute on a simulated N trajectory

- Detrend the series (Gaussian-kernel / polynomial filter) to residuals, then estimate the indicator inside a **rolling window** (they use half the series length)
- Quantify the *trend* in the indicator across the window sequence with **Kendall's tau** - a strong positive tau in AR1 and SD toward the tipping point is the warning
- Test significance against a **null model**: generate ~1,000 surrogate series from a best-fit ARMA of the residuals and read the P value off the distribution of Kendall trend statistics

## Caveats

- **Sensitivity** to two analyst choices - rolling-window size and filtering/detrending bandwidth (Table 3: AR1, SD, skewness all "++" sensitive); the same data can give different tau depending on them, a route to false positives
- **False alarms** from rising external noise (inflates variance channel); **missed alarms** for transitions driven by large perturbations or chaotic dynamics far from a local bifurcation
- Hard precondition: warnings only work if conditions move the system **slowly** toward the bifurcation - forcing faster than the system's response rate defeats them
- Knowing the **drivers / slow variables** materially improves detection (better null models, driver-informed AR(p) / drift-diffusion fits) - generic indicators are a fallback when mechanism is unknown

## Key takeaways for the model

- Adopt the full recipe: detrend, rolling-window SD + AR1, Kendall-tau trend, ARMA-surrogate significance - do not eyeball a single indicator
- Report AR1 *and* variance together so a pure noise-inflation artefact (variance up, memory flat) is distinguishable from genuine slowing down
- Run a window/bandwidth sensitivity sweep and a surrogate null before claiming an early warning on the norm channel; the slow-forcing precondition must hold for the claim to be valid

**Tags**: `early-warning-signals` `critical-slowing-down` `fold-bifurcation` `AR1` `variance` `skewness` `kurtosis` `DFA` `flickering` `Kendall-tau` `surrogate-null-model` `rolling-window` `detrending-sensitivity` `bistability` `Dakos` `2012` `open-access`
