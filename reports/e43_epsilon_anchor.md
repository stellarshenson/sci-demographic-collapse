# E43 - Noise-Amplitude Anchor for the Fertility-Norm Channel

Establishes a data-grounded value for the diffusion amplitude `eps` of the stochastic norm channel
`N`, whose dynamics are `dN = drift·dt + sqrt(2·eps)·dB` per year on the interval `[0,1]` (wells at
0.14 and 0.42, tip at 0.25, dynamic range 0.28). The anchor comes from the observed year-to-year
wobble of a revealed-preference proxy - the crude marriage rate - rather than from a hand-set guess.

## Recommendation

- **Central value**: `eps ≈ 5e-5` per year (`sigma_N_yr ≈ 0.010`, i.e. a ~1% of dynamic-range annual
  innovation on `N`)
- **Sweep range**: `eps ∈ [2e-5, 2e-4]` - a roughly one-decade bracket spanning the calm regions
  (USA, Japan) to the volatile ones (Korea, Poland), padded slightly at the top for proxy uncertainty
- **Per-region empirical span**: `eps` from `2.2e-5` (USA) to `1.1e-4` (Poland); median `4.9e-5`

## Data

- **Source**: `data/raw/owid/marriage-rate-per-1000-inhabitants.csv` - OWID crude marriage rate
  (marriages per 1000 inhabitants), CC-BY, upstream UN / national statistics; provenance in
  `data/raw/SECONDARY_MANIFEST.json`
- **Coverage** - all 8 focus regions present in the full file (the focus subset lacks Japan and
  Israel; the full file has them): USA 1886-2022, France 1994-2022, Germany 1960-2022, Italy
  1960-2022, Japan 1960-2022, South Korea 1970-2022, Poland 1960-2022, Israel 1970-2021
- **No external fetch was required** - the on-disk series covers every region, so no additions were
  made under `data/raw/owid/` and no `MANIFEST_e43.json` was created

## Method

- **Window** - the last ~40 years (from 1983, or the series start where shorter) to the series end,
  matching the horizon over which the norm channel evolves
- **Detrend** - fit a degree-3 polynomial to the non-COVID points and subtract it; this removes the
  slow secular decline (which belongs to `drift`, not to the noise `dB`) while leaving the year-to-year
  wobble
- **COVID handling** - 2020 and 2021 are excluded from the fit and the volatility, then reported
  separately; they are genuine outliers (marriage postponement), e.g. Italy -1.50 and USA -1.29 per
  1000 in 2020 - large enough to inflate the estimate two-to-threefold if left in
- **Two volatility measures** - the standard deviation of the detrended residual `sd_resid`, and the
  standard deviation of the year-to-year first-difference of the residual `sd_diff`. The
  first-difference std is the primary one: it is the annual innovation and maps directly onto the
  one-year increment std `sqrt(2·eps)` of the diffusion
- **Fractional volatility** - each raw std is divided by the mean series level over the window, giving
  a dimensionless wobble comparable across regions

## Residual volatilities

Raw units are marriages per 1000; `frac` columns are the same divided by the window mean level.

| Region | Window | Level | sd_resid | frac_resid | sd_diff | frac_diff |
|--------|--------|------:|---------:|-----------:|--------:|----------:|
| USA | 1983-2022 | 8.11 | 0.183 | 0.0225 | 0.192 | 0.0237 |
| France | 1994-2022 | 4.15 | 0.109 | 0.0262 | 0.154 | 0.0372 |
| Germany | 1983-2022 | 5.28 | 0.271 | 0.0512 | 0.213 | 0.0403 |
| Italy | 1983-2022 | 4.47 | 0.146 | 0.0326 | 0.146 | 0.0327 |
| Japan | 1983-2022 | 5.74 | 0.194 | 0.0338 | 0.161 | 0.0281 |
| Korea | 1983-2022 | 7.47 | 0.508 | 0.0680 | 0.348 | 0.0465 |
| Poland | 1983-2022 | 5.77 | 0.414 | 0.0718 | 0.302 | 0.0523 |
| Israel | 1985-2021 | 6.42 | 0.236 | 0.0367 | 0.213 | 0.0331 |

- **frac_resid**: median 0.035, mean 0.043, span 0.023-0.072
- **frac_diff**: median 0.035, mean 0.037, span 0.024-0.052

The two measures agree at a median of ~3.5% fractional annual wobble. The first-difference measure
is tighter across regions (0.024-0.052) because it is less sensitive to the exact trend shape. A
Savitzky-Golay (11-point, degree-2) detrend gives systematically smaller residuals (~0.10-0.24 raw)
because its short window absorbs part of the noise into the trend; it is treated as a lower bound and
not used for the anchor.

## Mapping to the N scale

The marriage rate is taken as a monotone proxy for coupling behaviour, so a fractional annual wobble
of `x` translates to an `N`-increment of the same fraction of `N`'s dynamic range (0.28):

```
sigma_N_yr = x · 0.28
eps        = sigma_N_yr^2 / 2      (since the 1-year increment std of dN is sqrt(2·eps))
```

Per region, using the first-difference fractional wobble `frac_diff = x`:

| Region | x (frac_diff) | sigma_N_yr = x·0.28 | eps = sigma_N_yr²/2 |
|--------|--------------:|--------------------:|--------------------:|
| USA | 0.0237 | 0.0066 | 2.2e-5 |
| France | 0.0372 | 0.0104 | 5.4e-5 |
| Germany | 0.0403 | 0.0113 | 6.4e-5 |
| Italy | 0.0327 | 0.0092 | 4.2e-5 |
| Japan | 0.0281 | 0.0079 | 3.1e-5 |
| Korea | 0.0465 | 0.0130 | 8.5e-5 |
| Poland | 0.0523 | 0.0146 | 1.1e-4 |
| Israel | 0.0331 | 0.0093 | 4.3e-5 |

**Central-value arithmetic** (median wobble 0.035):

```
sigma_N_yr = 0.035 · 0.28 = 0.0098  ≈ 0.010
eps        = 0.0098^2 / 2 = 9.6e-5 / 2 = 4.8e-5  ≈ 5e-5
```

**Sweep endpoints**:

```
low   (x = 0.023): sigma_N = 0.0064,  eps = 2.1e-5
high  (x = 0.070): sigma_N = 0.0196,  eps = 1.9e-4
```

The empirical per-region `eps` (median 4.9e-5, min 2.2e-5, max 1.1e-4) sits inside this bracket. The
sweep is rounded to `[2e-5, 2e-4]` to leave headroom above the observed maximum for proxy slack.

## Caveats

- **Proxy, not the norm itself** - the marriage rate is a revealed-behaviour signal, not a measured
  share of the childfree-ideal norm. It is used only for its year-to-year *volatility*, which is more
  transportable across proxies than its level, but the mapping assumes the two wobble by comparable
  fractions of their respective ranges
- **Fraction-of-range assumption** - equating an `x`% wobble in the marriage rate to an `x`% of
  0.28 increment on `N` is a modelling choice, not a measured elasticity; it is the single largest
  source of uncertainty and the reason the sweep is a full decade wide
- **Crude rate confounds** - the crude marriage rate is sensitive to age structure and cohort timing,
  so part of the wobble is compositional rather than a genuine norm shock; this biases the anchor
  slightly high, which is acceptable for an upper-inclusive noise sweep
- **Short series** - France (29 yrs) and Israel (37 yrs) give thinner volatility estimates; both land
  mid-range, so they do not drive the endpoints
- **Random-walk vs mean-reversion** - detrended residuals were treated as annual innovations. If `N`'s
  wobble is mean-reverting rather than a pure random walk, the increment std slightly overstates the
  driving noise, again biasing the anchor conservatively high
- **Detrend-order sensitivity** - degree-2 vs degree-3 polynomial and the SG alternative move
  individual fractions by up to ~30%, but the cross-region median stays near 3.5%, so the central
  `eps ≈ 5e-5` is stable to the detrending choice
