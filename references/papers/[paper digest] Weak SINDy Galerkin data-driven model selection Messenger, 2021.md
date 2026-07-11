# [Paper digest] Weak SINDy: Galerkin-Based Data-Driven Model Selection

**Authors**: Daniel A. Messenger, David M. Bortz<br>
**Year**: 2021  **Venue**: Multiscale Modeling & Simulation 19(3):1474-1497, SIAM, DOI 10.1137/20M1343166  (arXiv:2005.04339)<br>
**Original (link)**: [https://arxiv.org/abs/2005.04339](https://arxiv.org/abs/2005.04339)<br>
**Local PDF**: `[paper] Weak SINDy Galerkin model selection, 2021.pdf`<br>
**Used in**: E49 data-driven-dynamics round - the weak/integral formulation that removes pointwise derivative estimation, the single biggest source of SINDy failure on noisy demographic time series

## Key mechanism

Weak SINDy (WSINDy) rewrites the ODE in its weak (integral) form: multiply dx/dt = f(x) by a smooth compactly supported test function phi and integrate by parts over a window, so the time derivative moves onto phi and off the noisy data. The unknown coefficients Xi then appear in a linear system built from integrals of Theta(X) against phi and its derivative - a Galerkin projection. This eliminates numerical differentiation of the measured signal entirely; derivatives are taken analytically on the known test functions instead.

## Main findings

- Recovers the correct nonlinear terms with coefficient error that scales favorably with signal-to-noise ratio, across both small and large noise regimes
- Reports accuracy improvements of orders of magnitude over standard (differential) SINDy on noisy data
- In the noise-free limit, recovers coefficients to as many significant digits as the tolerance of the data-generating integrator
- The weak form also shrinks the linear system size, cutting computational cost relative to pointwise SINDy
- Demonstrated on standard nonlinear benchmarks (e.g. Lorenz, Van der Pol, Duffing-type systems) under added measurement noise

## Method and computation

- Weak-form conversion: integrate Theta(X)Xi against a family of test functions phi_k, moving d/dt onto phi via integration by parts (boundary terms vanish for compactly supported phi)
- Test functions: smooth bump functions (piecewise-polynomial or exponential) placed across the time domain; their number and support width are the main new hyperparameters
- Linear system G Xi = b where G, b are quadrature-evaluated integrals of library terms and data against phi; solved with the same sequentially thresholded least squares (STLSQ) sparse selection as classic SINDy
- Variance reduction: integrating against phi averages out zero-mean measurement noise, so no total-variation differentiation or smoothing of the raw signal is needed
- Threshold lambda still governs sparsity; test-function count/width trade bias vs variance in the integral estimates
- Reference implementation: `pysindy` (github.com/dynamicslab/pysindy) ships a `WeakPDELibrary` / weak-form option implementing this formulation

## Key takeaways (for E49)

- If the demographic trajectories are noisy (real vital-rate series always are), the weak form is the right default - it sidesteps the derivative-estimation step that most degrades SINDy
- The noise-robustness gain is quantified (orders of magnitude, and ~2x tolerable noise appears again in the ensemble follow-up), so it is a concrete lever, not a hand-wave
- New knobs are the test-function support and count - these must be swept and reported alongside lambda
- Weak-form and ensemble ideas compose: use WSINDy inside Ensemble-SINDy for the low-data high-noise limit

**Tags**: SINDy, weak-form, Galerkin, system-identification, sparse-regression, noise-robustness, integral-formulation
