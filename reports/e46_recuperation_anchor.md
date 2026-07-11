# E46 - Recuperation Anchor for the Second-Order Tempo Channel

Grounds the mass and damping of a proposed second-order law for the mean age at childbearing `tau`,
`tau_ddot + gamma·tau_dot + k·(tau_target - tau) = F`, a damped oscillator. The first-order law the
model currently uses (`tau_dot = k·(tau_target - tau)`) relaxes monotonically and cannot overshoot,
so it has no recuperation mechanism - the reason the E41 backtest missed the mid-2000s fertility
recoveries in Germany and Poland. The empirical recuperation FRACTION and recovery TIMESCALE below
fix `(gamma, k)`, equivalently the damping ratio `zeta` and natural frequency `omega_n`.

## Recommendation

- **Recuperation fraction** `f ≈ 0.65` central; **sweep `f ∈ [0.37, 1.0]`** (Spain floor to full
  recovery; over-recovery `f > 1`, US-style, handled by forcing `F`, not by damping - see caveats)
- **Recovery timescale** `T ≈ 12 years` central (trough-to-recovery); **sweep `T ∈ [10, 15]`**
  (period episode ~10 yr, within-cohort span ~15 yr)
- **Second-order parameters (central)**: `zeta ≈ 0.15`, `omega_n ≈ 0.27 rad/yr` (natural period
  ~24 yr) → **`k = omega_n² ≈ 0.070 /yr²`, `gamma = 2·zeta·omega_n ≈ 0.080 /yr`**
- **Sweep bracket**: `k ∈ [0.048, 0.100] /yr²`, `gamma ∈ [0.059, 0.133] /yr`, `zeta ∈ [0.11, 0.30]`,
  `omega_n ∈ [0.22, 0.32] rad/yr`

## Data

Three OA sources, digests in `references/papers/`:

- **Sobotka, Zeman, Lesthaeghe & Frejka (2011)**, VID EDRP 2011-2 - the Recuperation Index `RI`, its
  per-country values, and the within-cohort timescale (trough age → age 40)
- **Bongaarts & Sobotka (2012)**, Population Studies - the 1998-2008 period recovery episode and the
  Bongaarts-Feeney tempo relation `TFR_obs = TFR_quantum·(1 - tau_dot)` that couples `tau` to fertility
- **Lutz, Skirbekk & Testa (2006)**, Vienna Yearbook - the low-fertility-trap case for a low
  recuperation ceiling; sets the bottom of the `f` sweep and argues the target itself may drift down

## Empirical numbers

Recuperation fraction (share of the young-age fertility deficit recovered at older ages, total birth
orders, 1960s cohorts unless noted; `RI = R_c / (-P_c)`, Sobotka-Zeman-Frejka):

| Region | Recuperation fraction `f` (RI) | Note |
|--------|-------------------------------:|------|
| United States | > 1.0 | overcompensation, cohorts after 1962 (RI > 2 for 3rd+ births, 1965 cohort) |
| 'Healthy' (Nordic, Czech, Netherlands) | ~0.70 | first births > 0.67 everywhere; second ~0.65 |
| Austria, East Germany | < 0.50 | below one half |
| Spain | ~0.37 | Southern-European floor; 3rd+ births ~0 |

- **First births recuperate `>= 0.67` in every country studied**; second births `~0.65` (Austria,
  Czech, Netherlands, Switzerland); third-and-higher often `~0` (permanent loss)
- **Projected completed cohort fertility, early-1980s cohorts: 1.3 (Spain) to 1.9 (Czech)** - the
  spread is driven by recuperation strength, not postponement depth

Recovery timescale:

- **Cohort frame**: trough age `m ≈ 25`, recuperation near-complete by **age 40-42** → span **~15 yr**
- **Period frame**: continent-wide TFR rise **1998 → 2008 ≈ 10 yr** (Bongaarts-Sobotka); magnitudes
  +0.51 (Denmark), 18 countries > +0.2, Spain 1.16 → 1.46
- The period episode is shorter than the cohort span because it compresses the tail of within-cohort
  catch-up; central working value `T ≈ 12 yr`

## Mapping to a second-order tempo

Standard form of the proposed law (with `k = omega_n²`, `gamma = 2·zeta·omega_n`):

```
tau_ddot + 2·zeta·omega_n·tau_dot + omega_n²·(tau - tau_target) = F
```

The postponement-recuperation cycle is read as roughly ONE half-cycle of the damped oscillation:
`tau` is displaced upward (postponement), overshoots `tau_target`, and swings back - and the swing-back
is the recuperation (during it `tau_dot < 0`, so via Bongaarts-Feeney `(1 - tau_dot) > 1` and the
observed TFR bumps up). Two observables pin the two parameters:

**1. Timescale → frequency.** Trough-to-recovery `T` is half the damped period, so
`omega_d = pi / T` and `omega_n = omega_d / sqrt(1 - zeta²)`.

```
T = 12 yr  →  omega_d = pi/12 = 0.262 rad/yr  →  omega_n ≈ 0.265 rad/yr  (natural period ~24 yr)
```

**2. Recuperation fraction → damping ratio.** The size of the recuperation swing relative to the
postponement pulse is the single-swing overshoot ratio of an underdamped system,
`f = exp(-zeta·pi / sqrt(1 - zeta²))`, invertible to `zeta = x / sqrt(1 + x²)` with
`x = -ln(f)/pi`.

```
f = 0.62  →  zeta ≈ 0.15      f = 0.70 → zeta ≈ 0.11      f = 0.37 → zeta ≈ 0.30
```

Resulting `(k, gamma)` across the sweep:

| Regime | `T` (yr) | `f` | `zeta` | `omega_n` (rad/yr) | `k = omega_n²` (/yr²) | `gamma = 2·zeta·omega_n` (/yr) |
|--------|---------:|----:|-------:|-------------------:|----------------------:|-------------------------------:|
| Strong/fast (Nordic, Czech) | 10 | 0.70 | 0.11 | 0.316 | 0.100 | 0.059 |
| **Central** | **12** | **0.65** | **0.14** | **0.264** | **0.070** | **0.072** |
| Weak/slow (Spain, trapped) | 15 | 0.37 | 0.30 | 0.220 | 0.048 | 0.133 |

The central cell rounds to **`k ≈ 0.070 /yr²`, `gamma ≈ 0.080 /yr`** (using `zeta ≈ 0.15`).

## Caveats (identifiability)

- **Recovery alone does not require second order.** A first-order `tau` with a moving `tau_target`
  already produces a monotone TFR recovery as `tau_dot` decays to zero. What genuinely needs the
  second-order term is OVERSHOOT - `tau_dot` reversing sign, i.e. the observed TFR briefly exceeding
  quantum (US/Czech overcompensation, `RI > 1`). So the channel is identified by overshoot in the
  data, not by recovery per se; where no overshoot is visible, the damped oscillator is only weakly
  distinguishable from first-order relaxation
- **`zeta` and `omega_n` trade off.** The same trough-to-recovery time `T` is consistent with a family
  of `(zeta, omega_n)` pairs; pinning both needs the recovery SHAPE (is a second, smaller dip visible
  after the recovery?), which aggregate TFR series rarely resolve. The two-observable mapping here
  assumes the cycle is a clean single half-swing - a modelling choice, not a measured trajectory
- **`f > 1` is not a damping value.** A passive linear oscillator has overshoot ratio `< 1`; US-style
  overcompensation (`RI > 1`, up to `> 2`) cannot come from `zeta` and must enter through the forcing
  `F` (a real quantum or policy push). The sweep therefore caps the damping-derived `f` at 1 and
  routes over-recovery to `F`
- **Two distinct timescales.** The ~10-yr period episode and the ~15-yr cohort span are the same
  process in two frames (`c = t - a`), not independent data; the central `T = 12 yr` splits them and
  should not be read as a third measurement
- **Non-stationary target (trap).** Lutz-Skirbekk-Testa warn `tau_target`/quantum may itself drift
  down where low fertility is self-reinforcing. That is a separate slow mode from the fast damped swing;
  if it is folded into the same equation the fitted `k` will be biased and the recuperation ceiling
  will look lower than the tempo dynamics alone imply. Keep the slow target drift and the fast tempo
  oscillation as separate terms
