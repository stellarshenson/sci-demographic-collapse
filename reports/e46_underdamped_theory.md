# E46 - Does Inertia Change the Norm Channel's Tipping Physics?

Decides whether adding a second-order (inertial) term to the bistable social-norm channel changes
its escape rate, most-probable path, or fate map enough to be worth modelling. The current channel is
an OVERDAMPED gradient flow `dN = -V'(N) dt + sqrt(2 eps) dB` on a quartic double well (wells at 0.14
and 0.42, tip at 0.25); E43 validated overdamped Kramers escape to ~0.4%. The proposed change is the
full Langevin `m N_ddot + gamma N_dot + V'(N) = F + noise` - a damped particle in the same well. This
is the classic overdamped-to-full-Langevin transition, and the physics is settled (Kramers 1940,
Hanggi-Talkner-Borkovec RMP 1990, Berglund 2011, both in the library).

## Verdict

- **Overdamped is the physically-justified default for a social norm.** A norm is a diffusive process
  with no ballistic overshoot - it does not coast past its target and swing back. There is no empirical
  basis for norm "momentum" in the demographic or opinion-dynamics literature; second-order social
  models exist but are borrowed devices (flocking/alignment, affective-velocity), not forced by data.
  Overdamped = the standard, defensible modelling choice
- **Inertia cannot change the tipping barrier or the escape exponent.** Across every friction regime
  the Arrhenius exponent is `deltaV / (noise)` - the barrier height. Damping and mass rescale only the
  PREFACTOR (attempt frequency), never the exponent. E43's escape probability and the fate map are
  set by the exponent, so they are robust to adding an inertial term
- **The prefactor correction is negligible unless the norm is weakly damped.** The overdamped
  (Smoluchowski) rate is the `gamma -> infinity` limit of the full Kramers rate; its fractional error
  is `~ 1/(4 zeta^2)` with damping ratio `zeta = gamma / (2 omega_b)`. It stays under 10% for
  `gamma / omega_b > ~2.8`. A social norm sits far above this - `gamma / omega_b` is effectively huge
- **Recommendation: do NOT add the inertial term.** It changes no verdict-bearing quantity (barrier,
  escape probability, basin of attraction), adds a mass parameter with no data to anchor it, and its
  only effect - a small prefactor shift - is negligible in the regime a social norm actually occupies

## The overdamped-validity condition (when the project's current formula is correct)

The project uses the overdamped Eyring-Kramers mean-first-passage law (Berglund eq 1.8):

```
E[tau] ~= (2 pi / sqrt(V''(min) * |V''(saddle)|)) * exp(deltaV / eps)
```

This is the `gamma -> infinity` (Smoluchowski) limit of the full inertial escape problem. It is correct
when two conditions hold:

- **Rare-escape / small-noise**: `eps << deltaV`. E43 already satisfies this - barriers are `~1e-4`,
  the anchored `eps ~ 5e-5`, so `deltaV/eps ~ 3-8` and escapes are genuinely rare (the metastability
  E43 relies on)
- **Strong damping**: `gamma >> omega_b`, where `omega_b = sqrt(|V''(saddle)|/m)` is the barrier
  angular frequency. This is the regime where the norm relaxes without overshoot - the diffusive
  regime a social norm lives in. It is the condition being tested here, and it holds comfortably for
  any plausible social-norm damping

Both conditions are met by the current channel, so the overdamped formula is the right one.

## Escape-rate correction as a function of damping

Introducing `m N_ddot + gamma N_dot + V'(N) = noise` (noise obeying fluctuation-dissipation) puts the
channel into the full Kramers problem with three friction regimes (Hanggi-Talkner-Borkovec 1990):

- **Spatial-diffusion (moderate-to-high friction)** - Kramers 1940:
  `r_SD = kappa * (omega_0 / 2pi) * exp(-deltaV/eps)`, with the transmission factor
  `kappa = sqrt(1 + zeta^2) - zeta`, `zeta = gamma/(2 omega_b)`. As `gamma -> infinity`,
  `kappa -> omega_b/gamma` and this collapses to the project's overdamped rate
  `(omega_0 omega_b)/(2pi gamma) exp(-deltaV/eps)`
- **Energy-diffusion (low friction)** - `r_ED ~ (gamma * deltaV/eps) (omega_0/2pi) exp(-deltaV/eps)`;
  the rate rises with `gamma` (slow energy exchange is the bottleneck)
- **Kramers turnover** - the rate is non-monotonic in `gamma`: it rises as `gamma` at low friction,
  peaks near `gamma ~ omega_b`, and falls as `1/gamma` at high friction

The fractional error of the project's overdamped prefactor against the full spatial-diffusion rate is
`r_Kramers / r_overdamped = 2 zeta (sqrt(1+zeta^2) - zeta) ~ 1 - 1/(4 zeta^2)`. Tabulated for the
project's barrier frequency `omega_b = sqrt(0.047) = 0.217/yr` (unit mass):

| gamma / omega_b | zeta = gamma/2omega_b | kappa | r_Kramers / r_overdamped | overdamped error |
|----------------:|----------------------:|------:|-------------------------:|-----------------:|
| 0.5 | 0.25 | 0.781 | 0.390 | 61% |
| 1.0 | 0.50 | 0.618 | 0.618 | 38% |
| 2.0 | 1.00 | 0.414 | 0.828 | 17% |
| 2.8 | 1.42 | 0.311 | 0.900 | 10% |
| 4.0 | 2.00 | 0.236 | 0.944 | 6% |
| 10  | 5.00 | 0.099 | 0.990 | 1% |
| 20  | 10.0 | 0.050 | 0.998 | 0.2% |

The correction is on the PREFACTOR (attempt rate) only. Nothing in this table touches the exponent
`deltaV/eps`, so E43's escape probability changes at most by this prefactor factor, and the tipping
threshold (barrier height) does not move at all.

## The damping threshold below which second-order would matter

The material threshold is `gamma / omega_b ~ 2.8` (damping ratio `zeta ~ 1.4`), where the overdamped
prefactor error first reaches 10%. In project units (`omega_b = 0.217/yr`, unit mass) that is a
friction `gamma ~ 0.6/yr`, i.e. a norm-relaxation time `~1/gamma ~ 1.6 yr` becoming comparable to the
inertial timescale. Below the turnover (`gamma <~ 2 omega_b`) the overdamped formula fails
qualitatively - it keeps rising as `1/gamma` where the true rate turns over. But reaching that regime
requires a norm that ballistically overshoots and oscillates around its target, for which there is no
demographic evidence. A social norm's relaxation is monotone and overdamped, keeping `gamma/omega_b`
far above 2.8.

## Does the instanton (most-probable escape path) change?

- **Overdamped instanton** (Berglund eq 2.11-2.12, Grafke 2015): the most-probable escape is the
  time-reversed gradient climb `N_dot = +V'(N)` from well to saddle; relaxation back is ordinary
  gradient descent. Action `= 2 deltaV`
- **Full-Langevin instanton**: the escape path now lives in phase space `(N, N_dot)` and acquires a
  velocity component - the escaping trajectory carries momentum over the saddle. In the moderate-damping
  regime the projected configuration-space path can deviate slightly from the time-reversed relaxation
- **What does NOT change**: the full Langevin with fluctuation-dissipation noise is an equilibrium
  (detailed-balance) system whose stationary phase-space density is Boltzmann,
  `~ exp(-[½ m N_dot^2 + V(N)] / eps)`. The most-probable escape configuration is still the saddle of
  `V` at `N_dot = 0`, so the barrier location (N = 0.25) and height (`deltaV`) - hence the escape
  exponent and which basin the norm falls into - are damping-independent. For a 1-D gradient double
  well the exit always goes over the same saddle. The tipping topology and fate map are unchanged; only
  the phase-space shape of the path (and its prefactor) differs

## Is there any empirical basis for norm inertia?

Short answer: no, and overdamped is the justified default.

- **Opinion / social-dynamics modelling default is first-order (overdamped).** Canonical social-tipping
  and norm-change models (Andreoni-Nikiforakis-Siegenthaler-style benefit-cost tipping, Centola's 25%
  committed-minority threshold, Colleran's cultural-evolution diffusion of low fertility - the last
  already in the project library) are first-order threshold/gradient dynamics with no inertial term.
  They reproduce the observed tipping without needing a mass
- **Second-order social models exist but are borrowed devices, not data-forced.** Inertial /
  "affective-velocity" opinion models introduce a momentum coefficient by analogy with damped
  mechanical systems or optimizer momentum; second-order dynamics in the collective-behavior literature
  come mainly from animal flocking/alignment. None establishes that a real social norm ballistically
  overshoots its equilibrium and swings back - which is the physical content of inertia
- **A norm has no ballistic overshoot.** Diffusive social processes relax monotonically toward their
  attractor; they do not coast past it. That is precisely the overdamped assumption. Adding inertia
  would predict oscillatory norm relaxation (damped ringing around the well), for which there is no
  demographic signal

## Bottom line for the model

Keep the norm channel overdamped. The inertial term introduces a mass parameter with no data to anchor
it, cannot move the barrier or the escape exponent that carry E43's verdict, and its sole effect - a
prefactor rescaling - is under 10% for any `gamma/omega_b > 2.8`, a threshold a diffusive social norm
clears by a wide margin. The overdamped-to-full-Langevin extension is physically well-understood and
here it changes nothing worth modelling.

## References

- Hanggi, Talkner, Borkovec (1990), *Reaction-rate theory: fifty years after Kramers*, Rev. Mod. Phys.
  62, 251 - the three friction regimes, turnover, damping-dependent prefactor. Full text downloaded to
  `references/papers/[paper] reaction-rate theory fifty years after Kramers HTB, 1990.pdf`, digest at
  `references/papers/[paper digest] reaction-rate theory fifty years after Kramers HTB, 1990.md`
- Berglund (2011), *Kramers' law: validity, derivations and generalisations*, arXiv:1106.5799 -
  overdamped Eyring-Kramers formula, instanton = time-reversed gradient flow. Already in library
- Grafke, Grauer, Schaefer (2015), *The instanton method...*, arXiv:1506.08745 - path-space / instanton
  picture, phase-space Hamiltonian form. Already in library
- E43 noise-amplitude anchor (`reports/e43_epsilon_anchor.md`) - `eps ~ 5e-5/yr`, barrier curvatures,
  the ~0.4% overdamped escape this report shows is inertia-robust
