# Bayesian Population Projections for the United Nations - Raftery, Alkema, Gerland (2014)

**Statistical Science 29(1), 58-68** (the methods companion to Alkema et al. 2011, *Demography* 48(3),
815-839, which is the primary UN WPP TFR model). OA arXiv:1405.4708, PDF in this folder. This is the
established, trusted recovery mechanism the E47 recuperation round borrows.

## Key mechanism - the three-phase TFR model with an explicit recovery phase

The UN models a country's TFR trajectory in three phases: Phase I pre-transition high fertility;
Phase II the fertility transition (decline); **Phase III the post-transition phase in which fertility
recovers toward and fluctuates around a country-specific long-term level**. Phase III is where the UN
builds in the recovery that our down-only core lacks.

- **Phase II decline** - the annual decrement is a **double-logistic** function of TFR level,
  `d(f) = (d_max) [ logistic(f; parameters for the fast mid-transition drop) - logistic(...) ]`,
  estimated in a Bayesian hierarchical model that pools decline curves across all countries. A random
  walk with drift (the drift = minus the double-logistic decrement) carries TFR down through Phase II.
- **Phase III recovery - a Bayesian hierarchical AR(1)** around a country asymptote:

  ```
  f_{c,t+1} = mu_c + rho_c * (f_{c,t} - mu_c) + epsilon_{c,t},   epsilon ~ N(0, sigma_eps^2)
  ```

  A country whose TFR sits BELOW its asymptote `mu_c` is pulled UP a fraction `(1-rho_c)` of the gap
  each period - this is the mean-reverting rebound. Country parameters are drawn from world-level
  hierarchical priors (partial pooling), so a country with little post-transition data borrows the
  recovery behaviour of countries that have already turned up.

## Parameter values / priors (the numbers to borrow)

- **Classic (non-hierarchical) form** (Fosdick-Raftery): `mu_c = 2.1` (replacement), `rho = 0.9`,
  `sigma_eps = 0.2` - i.e. TFR reverts 10% of the gap to replacement per period, ~0.2 innovation noise.
- **Hierarchical form** (the WPP production version) estimates country-specific `mu_c` and `rho_c` by
  MCMC. `bayesTFR` default priors: **`mu_c` in [0, 2.1]** (the asymptote is bounded ABOVE by
  replacement - post-transition countries do not revert past 2.1), `rho_c` in [0, 1),
  `sigma_mu` in [1e-5, 0.318], `sigma_rho` in [1e-5, 0.289], `sigma_eps` in [1e-5, 0.5].
- **Phase III entry rule** - a country enters Phase III after its TFR reaches a local minimum and
  posts two successive increases below replacement (the empirical "end of decline" trigger).

## Key takeaways for the model

- The trusted recovery term is a **mean-reversion toward a bounded country asymptote**, not a tempo
  oscillator - directly matching the E46 "quantum, not tempo" finding. `mu_c <= 2.1` is the ceiling
  that keeps the rebound from overshooting.
- The hierarchical structure is the template for **Bayesian calibration** of our recuperation
  parameters: infer a country asymptote and reversion rate with partial pooling across the recovery
  regions rather than hand-setting them.
- `rho = 0.9`, `sigma = 0.2`, asymptote `<= 2.1` are the literature-anchored central values / brackets
  for the reversion strength and its ceiling.

Tags: #un-wpp #bayesian-hierarchical #phase-iii-recovery #AR1 #mean-reversion #recuperation #calibration
