# [Paper digest] The instanton method and its numerical implementation in fluid mechanics

**Author**: Tobias Grafke (Weizmann), Rainer Grauer (Bochum), Tobias Schaefer (CUNY)<br>
**Year**: 2015  **Venue**: Journal of Physics A: Mathematical and Theoretical (topical review)<br>
**Original (download)**: [https://arxiv.org/abs/1506.08745](https://arxiv.org/abs/1506.08745) - open access<br>
**Local PDF**: `[paper] instanton method large deviations fluid Grafke, 2015.pdf` (40 pp, full text)<br>
**Model class**: methods review (Freidlin-Wentzell action, instanton = most-probable path, numerical minimisation)<br>
**Downloaded**: yes (full text)

## What it establishes

A physicists' review of the Freidlin-Wentzell / instanton machinery and how to compute the most-probable path numerically. Complementary to Berglund: Berglund gives the escape-time formula with prefactor, this gives the path-space picture - the action, the instanton as the maximum-likelihood trajectory, and the Hamiltonian (Euler-Lagrange) equations the instanton solves. Written for SPDEs (Burgers) but the finite-dimensional SDE section is exactly our setting.

## Noise convention

SDE (its eq 19): `du_eps = b[u] dt + sigma*sqrt(eps) dW`, with `chi = sigma^T sigma` the covariance. For 1-D additive noise with `sigma = sqrt(2)` this is `du = b(u) dt + sqrt(2 eps) dW` - matching Berglund and the round. Below, `b = -V'` and `chi = 2`.

## The exact formulas the round will use

- **Freidlin-Wentzell rate function / action (its eqs 21-22)**:

  `I_T(u) = (1/2) integral <u_dot - b[u], chi^{-1} (u_dot - b[u])> dt`

  For 1-D gradient `b=-V'`, `chi=2`: `I_T = (1/4) integral (N_dot + V'(N))^2 dt`. (Berglund uses the `sqrt(2eps)` normalisation that absorbs the `chi=2`, giving his `(1/2) integral (phi_dot + V')^2`; the two agree once the `1/2eps` vs `1/eps` prefactor bookkeeping is tracked - see caveat.)

- **Instanton = most-probable path (its Section 2.1, bullet at p.6)**: in the small-`eps` saddle-point limit the instanton "corresponds to the most probable trajectory connecting the initial conditions to a final configuration" - the minimiser `psi*` of the rate function. For a gradient double well this is Berglund's time-reversed gradient climb `N_dot = +V'(N)` from well to saddle

- **Hamiltonian form (its eqs 14-15, 20)**: with conjugate momentum `p`, `H(u,p) = <b[u],p> + (1/2)<p, chi p>`; the instanton solves Hamilton's equations `u_dot = dH/dp`, `p_dot = -dH/du` at conserved energy `H=0` for the T->infinity transition. The Lagrangian is eq 18/21. For our 1-D case: `H(N,p) = -V'(N) p + p^2`, instanton `N_dot = -V' + 2p`, `p_dot = V''(N) p`; the `p=V'` branch gives the uphill escape path

## Validity conditions

- **Saddle-point / small-noise limit** (its p.6-7): the instanton dominates the path integral only when the smallness parameter (`eps`) justifies the saddle-point approximation - the same `eps -> 0` regime as Kramers. Away from it, fluctuations around the instanton (the prefactor) matter and eventually the single-path picture breaks
- The action gives the **exponent** of the transition probability; it does not by itself fix the prefactor (for that use Berglund eq 1.8). Consistency check: the minimised action equals Berglund's quasipotential `2*deltaV`

## Numbers / sections the formulas come from

Section 2.1 (path-integral / MSRJD action, observable definition eqs 9-13), Section 2.2 (Hamiltonian eqs 14-15, instanton = classical trajectory), Section 3 / eqs 18-22 (finite-dimensional SDE, eq 19 SDE with `sigma sqrt(eps)`, eq 21 Lagrangian, eq 22 rate function `I_T`). Euler-Lagrange / Hamilton equations for the minimiser are eqs 11-12.

## Portability to our norm round

Confirms the instanton characterisation Berglund states abstractly: the most-probable escape of our norm `N` over the `thN=0.25` saddle is the time-reversed anti-gradient path `N_dot = +V'(N)`, and its action equals `2*deltaV`. Use this paper for the path picture and any future numerical most-probable-path (string / gMAM) computation; use Berglund eq 1.8 for the actual mean escape time.

## Tags

`instanton` `freidlin-wentzell` `large-deviations` `action-functional` `most-probable-path` `hamiltonian-formulation` `rate-function` `saddle-point` `quasipotential` `numerical-minimisation`
