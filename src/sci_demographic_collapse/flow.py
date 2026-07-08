"""Torch monotone quantile-flow - the differentiable distributional representation for the core rebuild.

The design decision from the OT work: represent every channel by its quantile function Q(u), u ~ Uniform(0,1),
as a torch tensor on a fixed u-grid. One object, four properties at once:

- **Reparameterisation** - theta = Q(u) is pathwise-differentiable in Q's parameters, for ANY shape
  (Gaussian, a monotone spline / 1-D normalizing flow, or a raw empirical Q). This is the reparameterisation
  trick generalised past the Gaussian.
- **Optimal transport** - W2 is the L2 distance between quantile functions (the E12 WAE trick), the McCann
  morph is linear interpolation in Q, a transport map is a pushforward on Q - all differentiable.
- **Gradient flow** - a Wasserstein-2 gradient flow is an L2 gradient flow on Q, a plain autograd ODE.
- **Baseline-preservation** - a degenerate flow (scale -> 0) is a point mass, and `aggregate(f) -> f(loc)`,
  so a narrow flow reproduces the scalar channel exactly. This is how the distributional core stays calibrated:
  lift a scalar to a near-degenerate flow and the baseline is unchanged.

`population.PopChannel` (Gaussian buckets) and `ot.Dist` (empirical atoms) are the two limits of this object;
this is the differentiable one used for calibration and dynamics.

    q = QuantileFlow.gaussian(loc=0.0, log_scale=torch.log(torch.tensor(0.3)))
    q.aggregate(gate)             # Jensen-correct population coupling gate, differentiable
    q.W2(q.pushforward(lambda x: x + 0.2))   # 0.2, exact
"""

from __future__ import annotations

import torch
import torch.nn.functional as F

_DT = torch.float64


def _ugrid(K: int) -> torch.Tensor:
    return (torch.arange(K, dtype=_DT) + 0.5) / K


class QuantileFlow:
    """A 1-D distribution held as its quantile values Q on a fixed probability grid u; torch-differentiable."""

    def __init__(self, Qv: torch.Tensor, u: torch.Tensor | None = None):
        self.Qv = Qv
        self.K = Qv.shape[0]
        self.u = _ugrid(self.K) if u is None else u

    # -- constructors ------------------------------------------------------
    @classmethod
    def gaussian(cls, loc, log_scale, K: int = 64):
        """A Gaussian quantile-flow: Q(u) = loc + exp(log_scale) * Phi^{-1}(u). loc/log_scale are the leaves."""
        u = _ugrid(K)
        z = torch.special.ndtri(u)  # inverse standard-normal CDF
        loc = torch.as_tensor(loc, dtype=_DT)
        log_scale = torch.as_tensor(log_scale, dtype=_DT)
        return cls(loc + torch.exp(log_scale) * z, u)

    @classmethod
    def spline(cls, loc, log_scale, inc_raw, K: int | None = None):
        """A monotone-spline quantile-flow (a 1-D normalizing flow): the shape z is a learned monotone curve
        from positive increments (softplus), standardised - any distribution, still reparameterisable."""
        inc = F.softplus(inc_raw)
        z = torch.cat([torch.zeros(1, dtype=inc.dtype), torch.cumsum(inc, 0)])
        z = (z - z.mean()) / (z.std() + 1e-9)
        loc = torch.as_tensor(loc, dtype=_DT)
        log_scale = torch.as_tensor(log_scale, dtype=_DT)
        K = z.shape[0]
        return cls(loc + torch.exp(log_scale) * z, _ugrid(K))

    @classmethod
    def scalar(cls, mu, K: int = 64):
        """A degenerate point mass at mu - the scalar-channel limit; aggregate(f) == f(mu)."""
        mu = torch.as_tensor(mu, dtype=_DT)
        return cls(mu * torch.ones(K, dtype=_DT))

    # -- observables (Jensen-correct) -------------------------------------
    @property
    def mean(self) -> torch.Tensor:
        return self.Qv.mean()

    @property
    def std(self) -> torch.Tensor:
        return self.Qv.std()

    def aggregate(self, f) -> torch.Tensor:
        """Jensen-correct population average <f> = mean_k f(Q_k)."""
        return f(self.Qv).mean()

    def jensen_gap(self, f) -> torch.Tensor:
        return self.aggregate(f) - f(self.mean)

    # -- reparameterised sampling -----------------------------------------
    def sample(self, n: int) -> torch.Tensor:
        """Reparameterised draw: u ~ Uniform, theta = Q(u) by linear interpolation - differentiable through Q."""
        uu = torch.rand(n, dtype=_DT)
        idx = torch.clamp(uu * self.K - 0.5, 0, self.K - 1)
        lo = idx.floor().long().clamp(0, self.K - 1)
        hi = (lo + 1).clamp(0, self.K - 1)
        w = idx - lo.to(_DT)
        return self.Qv[lo] * (1 - w) + self.Qv[hi] * w

    # -- optimal transport (exact, 1-D) -----------------------------------
    def W2(self, other: "QuantileFlow") -> torch.Tensor:
        """Exact 1-D Wasserstein-2: L2 between quantile functions."""
        return torch.sqrt(((self.Qv - other.Qv) ** 2).mean())

    def interpolate(self, other: "QuantileFlow", t: float) -> "QuantileFlow":
        """McCann displacement geodesic - linear interpolation in quantile space."""
        return QuantileFlow((1 - t) * self.Qv + t * other.Qv, self.u)

    def pushforward(self, T) -> "QuantileFlow":
        """Transport by a map T (an intervention / selection)."""
        return QuantileFlow(T(self.Qv), self.u)

    def advect(self, vfield, dt: float = 1.0) -> "QuantileFlow":
        """One explicit transport step under a velocity field (the particle Fokker-Planck drift)."""
        return QuantileFlow(self.Qv + dt * vfield(self.Qv), self.u)

    @staticmethod
    def barycenter(flows, weights=None) -> "QuantileFlow":
        """Wasserstein barycenter - the quantile-averaged distribution."""
        n = len(flows)
        w = torch.ones(n, dtype=_DT) if weights is None else torch.as_tensor(weights, dtype=_DT)
        w = w / w.sum()
        Qv = sum(wi * fl.Qv for wi, fl in zip(w, flows))
        return QuantileFlow(Qv, flows[0].u)


if __name__ == "__main__":  # self-test - the properties that make the rebuild safe

    def gate(q):  # a nonlinear coupling gate
        return torch.sigmoid(6.0 * q)

    # 1. degenerate limit reproduces the scalar (baseline-preservation route)
    s = QuantileFlow.scalar(0.3)
    assert torch.allclose(s.aggregate(gate), gate(torch.tensor(0.3, dtype=_DT)), atol=1e-9)

    # 2. W2 of a pure shift equals the shift
    a = QuantileFlow.gaussian(0.0, torch.log(torch.tensor(0.3, dtype=_DT)))
    b = a.pushforward(lambda x: x + 0.2)
    assert abs(a.W2(b).item() - 0.2) < 1e-6

    # 3. McCann midpoint sits at the midpoint mean
    assert abs(a.interpolate(b, 0.5).mean.item() - 0.1) < 1e-9

    # 4. reparameterisation gradient flows through a sample-based loss
    loc = torch.tensor(0.0, dtype=_DT, requires_grad=True)
    fl = QuantileFlow.gaussian(loc, torch.log(torch.tensor(0.2, dtype=_DT)))
    loss = (fl.sample(4096).mean() - 1.0) ** 2
    loss.backward()
    assert loc.grad is not None and torch.isfinite(loc.grad)

    # 5. calibration gradient through aggregate (the Jensen-correct observable)
    loc2 = torch.tensor(0.0, dtype=_DT, requires_grad=True)
    fl2 = QuantileFlow.gaussian(loc2, torch.log(torch.tensor(0.3, dtype=_DT)))
    (fl2.aggregate(gate) - 0.7).pow(2).backward()
    assert loc2.grad is not None and abs(loc2.grad.item()) > 1e-6

    # 6. Jensen gap is nonzero off-threshold for a wide flow
    wide = QuantileFlow.gaussian(-0.3, torch.log(torch.tensor(0.4, dtype=_DT)))
    assert abs(wide.jensen_gap(gate).item()) > 1e-3

    print(
        "flow.py self-test passed:",
        f"W2-shift={a.W2(b).item():.4f}",
        f"| scalar aggregate={s.aggregate(gate).item():.4f}",
        f"| dloss/dloc={loc.grad.item():+.3f}",
        f"| jensen_gap={wide.jensen_gap(gate).item():+.4f}",
    )
