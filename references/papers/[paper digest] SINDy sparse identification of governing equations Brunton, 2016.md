# [Paper digest] Discovering Governing Equations from Data by Sparse Identification of Nonlinear Dynamical Systems

**Authors**: Steven L. Brunton, Joshua L. Proctor, J. Nathan Kutz<br>
**Year**: 2016  **Venue**: PNAS 113(15):3932-3937, DOI 10.1073/pnas.1517384113  (arXiv:1509.03580)<br>
**Original (link)**: [https://arxiv.org/abs/1509.03580](https://arxiv.org/abs/1509.03580)<br>
**Local PDF**: `[paper] SINDy sparse identification governing equations, 2016.pdf`<br>
**Used in**: E49 data-driven-dynamics round - the canonical SINDy method whose sparse-regression discovery of a vector field must be validated on synthetic ground truth before any claim of recovering the demographic ODE from data

## Key mechanism

SINDy assumes the governing equations of a dynamical system dx/dt = f(x) have a right-hand side that is sparse in the space of possible candidate functions - only a few terms are active. It builds a large library Theta(X) of candidate nonlinearities (polynomials, trig, etc.) evaluated on the measured states, then solves a sparse regression Xdot = Theta(X)Xi so that each column of the coefficient matrix Xi picks out the handful of active terms per equation. The parsimony (few nonzero coefficients) is what makes the recovered model interpretable and generalizable rather than overfit.

## Main findings

- Correctly recovers the chaotic Lorenz system (all three equations, exact active terms) from trajectory data, reconstructing the attractor
- Identifies the fluid vortex-shedding dynamics behind a cylinder - a mean-field model that historically took nearly 30 years of expert analysis to derive
- Extends to systems with external forcing/inputs and bifurcation parameters by adding the parameter/forcing as a variable in the library
- Model is parsimonious by construction: balances accuracy vs complexity, avoids overfitting even with limited data
- Works on high-dimensional PDE-derived systems after dimensionality reduction (POD/PCA coordinates)

## Method and computation

- Library Theta(X): columns are candidate functions of the state - constant, linear x, quadratic x_i x_j, higher polynomials, sin/cos; user chooses the basis
- Sparse regression by sequentially thresholded least squares (STLSQ): solve least squares, zero out all coefficients below threshold lambda, re-solve on remaining terms, iterate to convergence - cheap and deterministic
- Threshold lambda is the key hyperparameter tuning sparsity; a Pareto sweep of lambda trades model complexity against error
- Derivatives Xdot estimated by numerical differentiation of the measured x(t); noise in x is amplified here, so total-variation regularized differentiation is used for noisy data
- Noise is the main limitation - pointwise derivative estimation degrades under measurement noise, motivating later weak-form and ensemble variants
- Reference implementation: `pysindy` (github.com/dynamicslab/pysindy) provides STLSQ, custom libraries, and differentiation methods out of the box

## Key takeaways (for E49)

- SINDy is the interpretable counterpoint to a neural ODE - it returns explicit symbolic terms, so a recovered demographic vector field can be read and checked against the hand-built ODE
- Requires the true dynamics to be sparse in the chosen library - if the demographic coupling is not expressible in the candidate basis, SINDy cannot find it; library design is the load-bearing choice
- Clean-data recovery is near-exact, but noise on the state (and hence on estimated derivatives) is the binding constraint - validate on synthetic noise-free trajectories first, then characterize the noise floor
- Threshold lambda sweep is the model-selection knob; report the Pareto front, not a single fit

**Tags**: SINDy, system-identification, sparse-regression, STLSQ, governing-equations, interpretable-ML
