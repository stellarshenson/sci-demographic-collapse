# Second derivatives of population growth rate: calculation and applications

**Shyu & Caswell, 2016** (Methods Ecol. Evol.; ext. of Caswell 1996). Europe PMC PMC4358155. Open access.

Download: https://europepmc.org/articles/PMC4358155?pdf=render

## What it establishes
- The SECOND derivatives (Hessian) of the dominant eigenvalue lambda of a matrix population model
  measure the CURVATURE of lambda's response to parameter perturbations. Computed with matrix calculus
  and Magnus-Neudecker identification: d2 lambda = dx^T B dx, so the Hessian B is read straight off the
  second differential.
- The MIXED partial d2 lambda / d theta_i d theta_j is the INTERACTION between two parameters:
  positive = correlational (sensitivity to i rises with j, coupling amplifies), negative = decoupling
  (sensitivity to i falls with j), ZERO = the parameters act independently. This is exactly the
  off-diagonal-Hessian interaction law used in `docs/intervention-combination-law.md`.
- Honest caveat carried into our doc: the first-order approximation dlambda ~ (dlambda/dtheta) dtheta
  breaks down when the response is strongly nonlinear (large curvature, large perturbations, several
  parameters moving together); a second-order truncation "may in some cases provide accuracy - this is
  not guaranteed". Grounds our warning that the bilinear law is a local expansion that fails near the
  bistable ridge.

## Grounds
The bilinear interaction form I(A,B) = f_A^T H f_B (H = Hessian of the steady-state log-TFR response)
and its sign reading (saturation negative, threshold synergy positive), plus the near-ridge limitation.
