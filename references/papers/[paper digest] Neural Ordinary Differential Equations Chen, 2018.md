# [Paper digest] Neural Ordinary Differential Equations

**Authors**: Ricky T. Q. Chen, Yulia Rubanova, Jesse Bettencourt, David Duvenaud<br>
**Year**: 2018  **Venue**: Advances in Neural Information Processing Systems 31 (NeurIPS 2018), best-paper award  (arXiv:1806.07366)<br>
**Original (link)**: [https://arxiv.org/abs/1806.07366](https://arxiv.org/abs/1806.07366)<br>
**Local PDF**: `[paper] Neural Ordinary Differential Equations, 2018.pdf`<br>
**Used in**: E49 data-driven-dynamics round - the flexible black-box counterpart to SINDy; learns the vector field as a neural network fit by a differentiable ODE solver, the fallback when the dynamics are not sparse in any hand-chosen library

## Key mechanism

A neural ODE parameterizes the derivative of the hidden state directly: dh/dt = f(h, t; theta), where f is a neural network. The output is obtained by integrating this ODE from an initial state with any black-box numerical solver, replacing the discrete stacked layers of a residual network with continuous depth. Training backpropagates through the solver using the adjoint sensitivity method - solving a second, augmented ODE backward in time - which gives gradients at O(1) memory cost, independent of solver depth, without storing intermediate activations.

## Main findings

- Continuous-depth residual networks match discrete ResNet performance while training at constant memory in the number of solver steps
- The adjoint method decouples memory from integration depth - the whole point that makes deep continuous models trainable
- Adaptive solvers let the model trade numerical precision against compute at evaluation time, and error tolerance becomes a tunable knob
- Latent-ODE time-series model handles irregularly-sampled and continuous-time data natively, outperforming RNNs on such data
- Continuous normalizing flows compute exact change-of-density via the instantaneous change-of-variables formula, enabling maximum-likelihood generative training without partitioning or ordering data dimensions

## Method and computation

- Forward pass: integrate dh/dt = f(h,t;theta) with an off-the-shelf ODE solver (e.g. Dormand-Prince / adaptive Runge-Kutta) from t0 to t1
- Backward pass: adjoint sensitivity method integrates the adjoint a(t) = dL/dh(t) backward, giving dL/dtheta as an integral, at O(1) memory vs O(depth) for storing activations
- Number of function evaluations (solver steps) grows with training as dynamics stiffen - the analogue of depth, set adaptively by solver tolerance
- Latent-ODE: an encoder (RNN) infers an initial latent state, the ODE evolves it deterministically, a decoder emits observations - fit by variational inference
- Reference implementation: `torchdiffeq` (github.com/rtqichen/torchdiffeq) provides `odeint` and `odeint_adjoint`

## Key takeaways (for E49)

- Neural ODE is the expressive but opaque option - it can fit a demographic vector field with no library assumption, but returns weights, not readable terms, so it complements rather than replaces SINDy
- Use it as the flexibility ceiling: if a neural ODE fits the synthetic data well and SINDy does not, the dynamics are not sparse in the chosen basis (a library-design problem, not a data problem)
- The latent-ODE handles irregular sampling - relevant if demographic observations are unevenly spaced in time
- Constant-memory adjoint training makes multi-generation trajectory fitting tractable; solver tolerance is the accuracy/compute knob to report

**Tags**: neural-ODE, continuous-depth, adjoint-method, system-identification, latent-ODE, differentiable-solver, time-series
