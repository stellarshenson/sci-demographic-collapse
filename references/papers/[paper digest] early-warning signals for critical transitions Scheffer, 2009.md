# [Paper digest] Early-warning signals for critical transitions

**Authors**: Marten Scheffer, Jordi Bascompte, William A. Brock, Victor Brovkin, Stephen R. Carpenter, Vasilis Dakos, Hermann Held, Egbert H. van Nes, Max Rietkerk, George Sugihara<br>
**Year**: 2009  **Venue**: Nature 461:53-59, DOI 10.1038/nature08227 (Review)<br>
**Original (link)**: [https://www.nature.com/articles/nature08227](https://www.nature.com/articles/nature08227) (publisher version paywalled)<br>
**Local PDF**: `[paper] early-warning signals for critical transitions Scheffer, 2009.pdf` - freely-accessible academic-hosted copy ([pdodds.w3.uvm.edu](https://pdodds.w3.uvm.edu/files/papers/others/2009/scheffer2009a.pdf), University of Vermont faculty page); fully-OA companion is the Dakos 2012 PLoS ONE methods paper in this folder<br>
**Used in**: stochastic-tipping / early-warning round on the bistable social-norm (double-well) channel - the canonical review establishing why variance and lag-1 autocorrelation rise before a fold tipping point

## Key mechanism

The paper's spine is **critical slowing down** (CSD). At a fold (catastrophic) bifurcation the dominant eigenvalue governing return to equilibrium goes to zero, so the system recovers ever more slowly from small perturbations as the tipping point nears. Slowing down provably occurs for any continuous model approaching a fold, typically starting far from the threshold and decreasing smoothly to zero. Because real systems are constantly nudged by noise rather than probed experimentally, CSD leaves fingerprints in the fluctuation pattern: the state becomes more like its recent past (rising memory) and shocks accumulate instead of decaying (rising spread). This is exactly the regime of a bistable norm approached by slow social forcing.

## Main findings

- CSD yields three time-series early warnings before a fold: **slower recovery** from perturbation, **increased lag-1 autocorrelation** (AR1), and **increased variance** - all building up well before the transition
- The mechanism is exact for an AR(1) approximation (Box 3): with `y_{n+1} = a·y_n + s·e_n` and `a = e^{λΔt}`, the stationary variance is `s²/(1 − a²)`; as recovery rate `λ → 0` the autocorrelation `a → 1` and variance diverges
- **Skewness** can also rise, by a different mechanism (not CSD): near a catastrophic bifurcation the unstable basin boundary approaches the attractor from one side, so the system dwells asymmetrically; skewness may rise or fall depending on which side the alternative state lies
- **Flickering**: if noise is strong enough in the bistable region before the bifurcation, the system hops back and forth between the two basins, showing increased variance, skewness and **bimodality** - itself an early warning of a possible permanent shift
- Signals generalise across fold, Hopf, and some non-local/phase-locking bifurcations, and across ecosystems, climate (8/8 abrupt palaeoclimate shifts showed rising AR1), epileptic seizures (rising EEG variance), and financial markets (variance, AR1, spatial coherence)
- **Spatial** early warnings exist too - rising cross-correlation / spatial coherence and scale-invariant patch-size distributions - but are system-class-specific, with no one-size-fits-all pattern

## Method and computation

- Illustrated on a stochastically forced harvested-population model `dX/dt = X(1 − X/K) − c·X²/(X²+1)` driven slowly across the fold by ramping harvest `c`
- Standard recipe (Fig. 2): filter out the slow trend (e.g. Gaussian/moving-average), then over a **moving window** compute the residual's **standard deviation** and **lag-1 AR coefficient**; a rising trend in both as the control parameter increases is the warning

## Caveats

- **False negatives**: no gradual threshold approach (shift caused by a rare extreme event at fixed distance, or by a fast permanent change in conditions), too-short series to detect rising AR1, or a shifting external perturbation regime that distorts the signal
- **False positives**: a supposed signal arising by chance or from a confounding trend in the system or in the noise regime; filtering/detrending sensitivity means results depend on filter parameter choices
- Signals are **relative, not absolute** - measurement noise pushes AR1 below unity, perturbations can trip the transition before the bifurcation, so the trend warns but the exact timing stays unpredictable
- Fundamental precondition: warnings only arise when conditions move the system **slowly** toward the bifurcation

## Key takeaways for the model

- On the bistable norm trajectory, add small dynamic noise, ramp the forcing slowly, then compute residual variance and AR1 in a rolling window - both should climb approaching the tipping point (Kendall-tau trend as the statistic)
- Watch for flickering (bimodal norm state) as a distinct pre-tipping signature; skewness sign depends on the direction of the impending shift
- Discipline the claim: require slow forcing, detrend before measuring, guard against false positives from confounding trends, and treat the signal as proximity-to-threshold, not a dated forecast

**Tags**: `critical-slowing-down` `early-warning-signals` `fold-bifurcation` `tipping-point` `lag-1-autocorrelation` `variance` `skewness` `flickering` `bistability` `AR1` `Scheffer` `2009` `stochastic-tipping`
