# [Paper digest] Kramers' law: validity, derivations and generalisations

**Author**: Nils Berglund (MAPMO, Universite d'Orleans)<br>
**Year**: 2011 (updated Jan 2013)  **Venue**: Markov Processes and Related Fields; review based on IHP talk<br>
**Original (download)**: [https://arxiv.org/abs/1106.5799](https://arxiv.org/abs/1106.5799) (arXiv:1106.5799v2, math.PR) - open access<br>
**Local PDF**: `[paper] kramers law validity derivations Berglund, 2011.pdf` (26 pp, full text)<br>
**Model class**: mathematical review (rigorous proofs of the Eyring-Kramers mean-escape-time law)<br>
**Downloaded**: yes (full text)

## What it establishes

The reference proof-review for Kramers' law: the mean time an overdamped Brownian particle takes to cross a potential barrier between two wells. It links the large-deviation (Freidlin-Wentzell) route, which controls only the exponent, to the analytic routes (potential theory, spectral theory) that also nail the prefactor. This is exactly the theory our noise round needs, and its convention matches the round's SDE term-for-term.

## Noise convention (verify this - the round uses it verbatim)

Berglund's SDE (his eq 2.1) is

`dx_t = f(x_t) dt + sqrt(2*eps) dW_t`, gradient case `f = -grad V`, so `dN = -V'(N) dt + sqrt(2*eps) dB`.

Here `eps` is the parameter appearing inside `sqrt(2 eps)`; the noise intensity is `sqrt(2 eps)` and the diffusion coefficient is `eps`. All exponents below are `deltaV / eps` (NOT `deltaV / 2eps`). This is identical to the round's `dN = -V'(N) dt + sqrt(2 eps) dB`, so no rescaling is required.

## The exact formulas the round will use

- **Eyring-Kramers, 1-D (his eq 1.8)** - mean first-passage from well `x*` over saddle `z*`:

  `E[tau] ~= (2*pi / sqrt(V''(x*) * |V''(z*)|)) * exp((V(z*) - V(x*)) / eps)`

  with `V''(x*) > 0` at the minimum and `V''(z*) < 0` at the saddle. This is the round's target formula exactly, with `deltaV = V(z*) - V(x*)`.

- **Freidlin-Wentzell action / rate function (his eq 2.3)**: `I(phi) = (1/2) integral_0^T ||phi_dot - f(phi)||^2 dt`; large-deviation principle `P{x ~= phi} ~= exp(-I(phi) / 2eps)` (his eq 2.2). `I >= 0`, zero iff `phi` follows the deterministic flow.

- **Quasipotential (his eqs 2.8, 2.11-2.12)**: `V_quasi(z) = inf over paths I(phi)`. Completing the square, `I(phi) = (1/2) integral ||phi_dot - grad V||^2 + 2[V(phi(T)) - V(phi(0))]`; the square term vanishes on the **time-reversed deterministic flow** `phi_dot = +grad V` (the uphill anti-gradient path). Hence for gradient systems `V_quasi = 2[V(z*) - V(x*)] = 2*deltaV` (his eq 2.12). The instanton = most-probable escape path is this time-reversed gradient climb; relaxation back is ordinary gradient descent.

- **Arrhenius exponent (his Cor 2.4, eq 2.13)**: `lim_{eps->0} eps*log E[tau] = V(z*) - V(x*) = deltaV`. Note `V_quasi / (2 eps) = deltaV / eps`, so the large-deviation and Eyring-Kramers exponents agree.

## Validity conditions

- **Small-noise asymptotic**: the `~=` in eq 1.8 is `E[tau_eps]/E[tau_KL] -> 1` as `eps -> 0`. Rigorous proof (Bovier-Eckhoff-Gayrard-Klein 2004, via potential theory / capacities) gives multiplicative error `1 + O((eps*|log eps|)^{1/2})`. Requires `eps << deltaV`, i.e. the barrier must be several times the noise intensity for escapes to be rare and the exponential separation to hold
- **Non-degenerate saddle**: `z*` an index-1 critical point, Hessian with one negative and the rest positive eigenvalues (quadratic saddle). Berglund's Section 4 shows the classical formula FAILS at degenerate saddles (e.g. `V'' = 0` at the saddle), where the prefactor picks up different `eps`-powers
- **Exponential law of exit time** (his Thm 2.3, Day 1983): `tau / E[tau]` is asymptotically Exponential(1); escape is memoryless, so a single mean fully characterises the process

## Numbers / sections the formulas come from

Section 1.2 eq 1.8 (1-D Eyring-Kramers), eqs 1.9-1.10 (multi-D). Section 2: eq 2.1 (SDE + noise convention), eq 2.3 (FW action), eqs 2.8-2.13 (quasipotential = 2 deltaV, instanton = time-reversed gradient flow, Arrhenius exponent). Section 3 gives the analytic prefactor proofs; Section 4 the failure cases.

## Portability to our norm round

Our norm channel `V'(N) = aN(N-Nlo)(N-thN)(N-Nhi)` (aN=2.5, wells Nlo=0.14, Nhi=0.42, saddle thN=0.25) is a 1-D quartic double well - the exact setting of eq 1.8. Computed curvatures: `V''(0.14)=0.077`, `|V''(0.25)|=0.047`, `V''(0.42)=0.119`; barriers `deltaV(lo->hi)=1.3e-4`, `deltaV(hi->lo)=4.0e-4`; prefactors `2pi/sqrt(V''min|V''sad|)` = 105 (lo) and 84 (hi). Because the barriers are ~1e-4, the validity condition `eps << deltaV` demands `eps ~ 1e-5` or smaller for genuine metastability; at `eps >~ 1e-3` the exponential is ~1 and the wells are not separated (free diffusion over the barrier).

## Tags

`kramers-law` `eyring-kramers` `freidlin-wentzell` `large-deviations` `quasipotential` `instanton` `mean-first-passage` `double-well` `metastability` `noise-convention-sqrt2eps`
