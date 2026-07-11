# [Paper digest] Reaction-rate theory: fifty years after Kramers

**Authors**: Peter Hanggi (Augsburg), Peter Talkner, Michal Borkovec<br>
**Year**: 1990  **Venue**: Reviews of Modern Physics 62(2), 251-341<br>
**Original (download)**: [https://opus.bibliothek.uni-augsburg.de/opus4/files/41911/41911.pdf](https://opus.bibliothek.uni-augsburg.de/opus4/files/41911/41911.pdf) - open access (Augsburg OPUS 4 repository, author's institution)<br>
**DOI**: [10.1103/RevModPhys.62.251](https://doi.org/10.1103/RevModPhys.62.251)<br>
**Local PDF**: `[paper] reaction-rate theory fifty years after Kramers HTB, 1990.pdf` (~90 pp, full text scan)<br>
**Model class**: canonical physics review (barrier-crossing / escape-rate theory across all damping regimes)<br>
**Downloaded**: yes (full text)

## What it establishes

The reference review for the full-Langevin escape problem across every friction regime - the piece Berglund (overdamped only) does not cover. Where Berglund gives the Eyring-Kramers mean-first-passage law for the overdamped gradient flow, HTB gives the damping-DEPENDENT escape rate for the inertial equation `m x_ddot + gamma x_dot + V'(x) = xi(t)`, the three friction regimes, and the Kramers turnover that joins them. This is exactly the theory needed to decide whether adding an inertial term to the norm channel changes the escape physics.

## The inertial escape equation and the three regimes

Full Langevin (their Section II): `m x_ddot = -V'(x) - gamma x_dot + xi(t)`, white noise `<xi(t)xi(t')> = 2 gamma k_B T delta(t-t')` (fluctuation-dissipation). Well angular frequency `omega_0 = sqrt(V''(x_min)/m)`, barrier frequency `omega_b = sqrt(|V''(x_saddle)|/m)`. Define the reduced/damping ratio at the barrier from `gamma` (friction per unit mass).

- **Spatial-diffusion (moderate-to-high friction) - the Kramers 1940 result (their eq 4.35/4.49)**:

  `r_SD = (kappa) * (omega_0 / 2pi) * exp(-deltaV / k_B T)`,   `kappa = sqrt(1 + (gamma/2omega_b)^2) - gamma/(2omega_b)`

  `kappa` is the Grote-Hynes / spatial-diffusion transmission factor. In the strongly overdamped limit `gamma >> omega_b`, `kappa -> omega_b/gamma`, giving the Smoluchowski/overdamped rate `r = (omega_0 omega_b)/(2pi gamma) exp(-deltaV/k_B T)` - i.e. Berglund's overdamped prefactor. The rate falls as `1/gamma` at high friction (slow diffusive barrier crossing).

- **Energy-diffusion (low friction) regime (their Section IV.F)**: `r_ED ~ (gamma * deltaV / k_B T) * (omega_0/2pi) exp(-deltaV/k_B T)`. Rate rises PROPORTIONAL to `gamma` - the bottleneck is slow energy exchange with the bath, not spatial diffusion.

- **Kramers turnover (their Section VII)**: the rate is non-monotonic in `gamma`, rising as `gamma` at low friction, peaking near `gamma ~ omega_b`, falling as `1/gamma` at high friction. Uniform turnover formulae: Mel'nikov-Meshkov (1986, friction as perturbation) and Pollak-Grabert-Hanggi (1989, unstable-mode separation).

## The load-bearing invariant: the exponent is damping-independent

Across ALL three regimes the Arrhenius exponent is `deltaV / k_B T` - the barrier height. Friction/inertia rescales only the PREFACTOR (the attempt frequency / transmission factor), never the exponent. This is the decisive fact for the norm round: adding inertia cannot change the barrier the norm must cross, only the attempt rate multiplying the same exponential.

## Validity conditions

- **Barrier well-defined**: `deltaV >> k_B T` (rare escapes, quadratic well and saddle), same small-noise condition as Berglund
- **Overdamped (Smoluchowski) formula valid** when `gamma >> omega_b`; it is the `gamma -> infinity` asymptote of the spatial-diffusion `kappa`. Fractional error of the overdamped prefactor vs the full spatial-diffusion rate is `~ 1/(4 (gamma/2omega_b)^2)` (Taylor expansion of `2a(sqrt(1+a^2)-a)`, `a = gamma/2omega_b`); <10% once `gamma/omega_b > ~2.8`
- **Overdamped formula FAILS** below the turnover (`gamma <~ 2 omega_b`): it keeps rising as `1/gamma` where the true rate turns over and then falls as `gamma` (energy-diffusion). But this failure is on the prefactor only

## Portability to our norm round

The norm channel's overdamped `dN = -V'(N)dt + sqrt(2eps)dB` is the `gamma -> infinity` limit of HTB's inertial equation with `eps = k_B T / gamma` bookkeeping. Barrier curvatures (from Berglund digest): `omega_0(lo)=sqrt(0.077)=0.277`, `omega_b=sqrt(0.047)=0.217`, `omega_0(hi)=sqrt(0.119)=0.345` per year (unit mass). The 10% prefactor threshold `gamma/omega_b ~ 2.8` maps to `gamma ~ 0.6/yr` at unit mass. Because a social norm is a diffusive (heavily overdamped, no ballistic overshoot) process, `gamma/omega_b` is effectively enormous and the inertial correction is negligible; and even at the turnover the exponent - hence E43's escape probability and the fate map - is unchanged.

## Tags

`kramers-turnover` `underdamped` `overdamped` `spatial-diffusion` `energy-diffusion` `escape-rate` `full-langevin` `inertia` `transmission-coefficient` `melnikov-meshkov` `pollak-grabert-hanggi` `prefactor-not-exponent`
