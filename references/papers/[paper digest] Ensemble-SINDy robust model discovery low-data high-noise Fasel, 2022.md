# [Paper digest] Ensemble-SINDy: Robust Sparse Model Discovery in the Low-Data, High-Noise Limit, with Active Learning and Control

**Authors**: Urban Fasel, J. Nathan Kutz, Bingni W. Brunton, Steven L. Brunton<br>
**Year**: 2022  **Venue**: Proceedings of the Royal Society A 478(2260):20210904, DOI 10.1098/rspa.2021.0904  (arXiv:2111.10992)<br>
**Original (link)**: [https://arxiv.org/abs/2111.10992](https://arxiv.org/abs/2111.10992)<br>
**Local PDF**: `[paper] Ensemble-SINDy robust model discovery, 2022.pdf`<br>
**Used in**: E49 data-driven-dynamics round - bootstrap/bagging over trajectories and library terms giving inclusion probabilities and uncertainty, the practical path to discovery from short, noisy demographic records

## Key mechanism

Ensemble-SINDy (E-SINDy) wraps standard SINDy in bootstrap aggregating (bagging). It fits many SINDy models on resampled subsets - of the data points (data bagging) and of the library columns (library bagging) - then aggregates. Across the ensemble, each candidate term gets an inclusion probability (fraction of models that keep it), and the coefficients get a distribution rather than a point estimate. Thresholding on inclusion probability selects the robust active terms, and the coefficient spread gives uncertainty quantification and probabilistic forecasts.

## Main findings

- Uncovers PDE models from data with more than twice the measurement noise previously reported for sparse identification
- Substantially improves accuracy and robustness of discovery in the extremely-noisy and limited-data regime where single-shot SINDy fails
- Recovers Lotka-Volterra predator-prey dynamics from the historical 1900-1920 lynx-hare pelt record - short, noisy, real ecological data
- Inclusion probabilities double as a built-in model-selection and confidence signal, avoiding brittle single-threshold choices
- Ensemble statistics feed active learning (choose next-most-informative data) and model predictive control, at compute cost comparable to plain SINDy
- Library bagging is especially effective when the candidate library is large or correlated

## Method and computation

- Data bagging: draw bootstrap resamples of the time series, fit SINDy (STLSQ) on each, collect coefficient matrices
- Library bagging: randomly drop a subset of library columns per model, forcing robustness to correlated/redundant candidate terms
- Aggregate: inclusion probability per term = fraction of ensemble models retaining it; keep terms above a probability threshold; coefficients averaged (optionally probability-weighted) over the ensemble
- Uncertainty: the ensemble coefficient distribution yields error bars and probabilistic (ensemble) forecasts
- Composable with the weak form - use WSINDy as the base learner for the noisiest cases
- Reference implementation: `pysindy` (github.com/dynamicslab/pysindy) provides `EnsembleOptimizer` (data and library bagging) that wraps any base optimizer

## Key takeaways (for E49)

- This is the method to reach for when the demographic record is short and noisy - exactly the real-data condition after synthetic validation
- Inclusion probability gives a principled, reportable confidence per discovered term - stronger evidence than a single lambda fit surviving
- ~2x noise tolerance over single-shot SINDy is the concrete headroom; the lynx-hare demo is a directly relevant short-noisy population-dynamics precedent
- Uncertainty quantification lets the round state discovery claims with error bars instead of a bare point estimate

**Tags**: SINDy, ensemble, bagging, bootstrap, uncertainty-quantification, system-identification, sparse-regression, noise-robustness, active-learning
