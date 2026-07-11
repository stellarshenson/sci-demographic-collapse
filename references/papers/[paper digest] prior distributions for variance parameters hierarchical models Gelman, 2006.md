# Prior distributions for variance parameters in hierarchical models (Gelman, 2006)

**Bayesian Analysis 1(3):515-533.** The reference text on how to put a prior on the
group-level scale `tau` (the between-group SD) in a two-level model, and why that choice
matters most exactly when there are FEW groups - the DEF-8 regime (8 regions).

## Key mechanism

Two-level normal model: `y_ij ~ N(mu + alpha_j, sigma_y^2)`, `alpha_j ~ N(0, tau^2)`,
`j = 1..J` groups. The hierarchical SD `tau` controls the pooling:

- `tau -> 0` collapses every group to the grand mean - **complete pooling** (E47's shared
  single `g_rec` is exactly this limit)
- `tau -> infinity` frees every group - **no pooling** (a separate per-region fit)
- finite `tau` is **partial pooling** - each group shrinks toward the mean by a factor that
  depends on `tau` and its own data precision

## Main findings

- **The inverse-gamma(epsilon, epsilon) "noninformative" prior is bad.** It has no proper
  limiting posterior as epsilon -> 0, so inferences are sensitive to epsilon - it cannot be
  "comfortably set to 0.001". A spuriously data-dependent answer.
- **Use a uniform prior on `tau` (the SD, not the variance), or a half-t / half-Cauchy when
  the number of groups is small.** The uniform(0, A) prior yields a proper posterior **as
  long as J >= 3**; for finite large A, inferences are insensitive to A.
- **Few groups is the danger zone.** With small J the data carry little information about
  `tau`, so the prior on `tau` does real work; a heavy inverse-gamma can wrongly pull `tau`
  toward 0 (over-pooling) or a flat prior can let it run to no-pooling. The half-t is the
  weakly-informative compromise.
- The folded-noncentral-t family is conditionally conjugate, so it survives hierarchical
  model expansion (ordinary conjugacy does not).

## Key takeaways for DEF-8

- E47's single shared `g_rec` is the `tau = 0` complete-pooling corner - the most extreme
  regularization on the ladder, chosen implicitly, never estimated
- with only 8 regions, `tau_g` (the spread of per-region recovery strengths) is weakly
  identified - the partial-pooling cure must put a half-t/half-Cauchy prior on `tau_g`, not
  an inverse-gamma, and must expect the data to leave `tau_g` uncertain
- partial pooling - not no-pooling - is the textbook fix; with thin per-group data, no-pooling
  overfits and can generalize worse than complete pooling out-of-sample (confirmed by the
  DEF-8 held-out toy)

**Tags**: bayesian-hierarchical, partial-pooling, shrinkage, variance-prior, few-groups,
half-cauchy, complete-pooling-limit, DEF-8
