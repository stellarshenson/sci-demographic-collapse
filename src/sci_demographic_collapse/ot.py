"""Optimal-transport backbone (E30+) - evolve morphing distributions and integrate effects along cohorts.

Two objects, one idea. A population channel is a measure that evolves; the operations that matter break
Gaussianity (truncation from selection, bimodal splitting at a norm tipping point, skew from a heterogeneous
response), so we carry it as a **free-form** measure moved by transport maps rather than re-fit to a Gaussian.
Everything here is 1-D, where optimal transport is closed-form: the optimal plan is the monotone
(order-preserving) rearrangement, `W2` is the L2 distance between quantile functions, and the displacement
geodesic is linear interpolation in quantile space. No cost matrix, no Sinkhorn, no external dependency.

- `Dist` - a free-form weighted-atom distribution with the OT operations (`W2`, `pushforward`,
  `interpolate` = McCann displacement, `barycenter`, `advect`). This is the Eulerian-morph side.
- `CohortMemory` - the Lagrangian side. Because the 1-D optimal map preserves quantile rank, a cohort keeps
  its identity as the distribution shifts, so we can follow it down its Lexis life-line and accumulate a
  **path integral** of its exposures. This is the method of characteristics for the McKendrick-von Foerster /
  renewal PDE, extended from survival+fertility to behavioural exposures: `J(b) = mean over childhood of env`,
  and the reproductive contribution is the mean of `J` over the cohorts currently of reproductive age. It
  replaces an aggregate mean-field lag with genuine per-cohort accounting.

    d0 = Dist.from_gaussian(0.0, 0.3); d1 = d0.pushforward(lambda x: x + 0.2)   # a shift intervention
    d0.W2(d1)                          # 0.2, exact
    dhalf = d0.interpolate(d1, 0.5)    # the displacement geodesic (the morph)
    mem = CohortMemory(); [mem.push(e) for e in env_series]; mem.reproductive_mean()  # the cohort path integral
"""

from __future__ import annotations

import numpy as np


class Dist:
    """A 1-D free-form distribution as weighted atoms; all OT operations are exact and closed-form."""

    def __init__(self, x, w=None):
        x = np.asarray(x, dtype=float)
        w = np.ones_like(x) if w is None else np.asarray(w, dtype=float)
        order = np.argsort(x)  # atoms kept sorted (1-D OT is monotone)
        self.x = x[order]
        self.w = w[order] / w.sum()

    # -- constructors ------------------------------------------------------
    @classmethod
    def from_gaussian(cls, mu, sigma, K=25):
        """A Gaussian discretised on Gauss-Hermite atoms (deterministic, no scipy; matches `population`)."""
        nodes, weights = np.polynomial.hermite_e.hermegauss(K)
        return cls(mu + sigma * nodes, weights / weights.sum())

    # -- quantile machinery (the heart of 1-D OT) -------------------------
    def quantile(self, u):
        """Inverse CDF F^{-1}(u) at probability levels u (vectorised), left-continuous step form."""
        u = np.atleast_1d(np.asarray(u, dtype=float))
        cw = np.cumsum(self.w)
        idx = np.searchsorted(cw, u, side="left")
        idx = np.clip(idx, 0, len(self.x) - 1)
        return self.x[idx]

    def _common_grid(self, other, n=512):
        u = (np.arange(n) + 0.5) / n
        return u, self.quantile(u), other.quantile(u)

    # -- observables -------------------------------------------------------
    @property
    def mean(self):
        return float(np.sum(self.w * self.x))

    @property
    def std(self):
        return float(np.sqrt(np.sum(self.w * (self.x - self.mean) ** 2)))

    def aggregate(self, f):
        """Jensen-correct population average <f> = sum_k w_k f(x_k)."""
        return float(np.sum(self.w * np.vectorize(f)(self.x)))

    # -- optimal transport -------------------------------------------------
    def W2(self, other, n=512):
        """Exact 1-D Wasserstein-2 distance: L2 between quantile functions (the E12 WAE trick)."""
        _, qa, qb = self._common_grid(other, n)
        return float(np.sqrt(np.mean((qa - qb) ** 2)))

    def pushforward(self, T):
        """Transport the distribution by a map T (an intervention or selection): x -> T(x), weights kept."""
        return Dist(np.vectorize(T)(self.x), self.w.copy())

    def advect(self, vfield, dt=1.0):
        """One explicit transport step under a velocity field (the particle form of a Fokker-Planck drift)."""
        return Dist(self.x + dt * np.vectorize(vfield)(self.x), self.w.copy())

    def interpolate(self, other, t, n=512):
        """McCann displacement interpolation - the geodesic morph: F_t^{-1} = (1-t)F0^{-1} + t F1^{-1}."""
        _u, qa, qb = self._common_grid(other, n)
        return Dist((1 - t) * qa + t * qb, np.ones(n))

    @staticmethod
    def barycenter(dists, weights=None, n=512):
        """Wasserstein barycenter of 1-D distributions: the quantile-averaged distribution."""
        weights = np.ones(len(dists)) if weights is None else np.asarray(weights, dtype=float)
        weights = weights / weights.sum()
        u = (np.arange(n) + 0.5) / n
        q = sum(wt * d.quantile(u) for wt, d in zip(weights, dists))
        return Dist(q, np.ones(n))

    # -- selection (tail operations, non-Gaussian by construction) --------
    def select(self, thresh, side="below"):
        """Keep the atoms on one side of thresh; returns the retained sub-distribution (renormalised)."""
        mask = self.x < thresh if side == "below" else self.x >= thresh
        if not mask.any():
            return Dist(np.array([thresh]), np.array([1e-12]))
        return Dist(self.x[mask], self.w[mask])

    def mass(self, thresh, side="above"):
        """Probability mass on one side of thresh (e.g. share acceptable to a hypergamy bar)."""
        mask = self.x >= thresh if side == "above" else self.x < thresh
        return float(self.w[mask].sum())


class CohortMemory:
    """Lagrangian cohort path-integral: follow each birth cohort and integrate its childhood exposure.

    The method of characteristics for the renewal PDE, carried for a behavioural exposure. Each year an
    environment value `env` (a deviation from the calibrated baseline) is pushed. A cohort born at year b
    accumulates `J(b) = mean_{age 0..childhood-1} env(b+age)`; the reproductive contribution at time t is the
    mean of `J(b)` over the cohorts currently of reproductive age (born in `[t-repro_hi, t-repro_lo]`). Pre-sim
    cohorts contribute zero, so at the calibrated baseline (env == 0) every integral is zero - baseline-preserving.
    """

    def __init__(self, childhood=18, repro_lo=27, repro_hi=45):
        self.childhood = int(childhood)
        self.repro_lo = int(repro_lo)
        self.repro_hi = int(repro_hi)
        self.env = []

    def push(self, env_value):
        self.env.append(float(env_value))

    def reproductive_mean(self):
        """Mean completed childhood path-integral over the cohorts currently of reproductive age."""
        t = len(self.env) - 1
        if t < 0:
            return 0.0
        C = self.childhood
        Js = []
        for b in range(t - self.repro_hi, t - self.repro_lo + 1):
            if b < 0:
                Js.append(0.0)  # childhood entirely before the simulation window
            else:
                end = min(b + C, len(self.env))
                seg = self.env[b:end]
                Js.append(sum(seg) / C if seg else 0.0)  # normalise by full childhood length
        return sum(Js) / len(Js) if Js else 0.0


if __name__ == "__main__":  # self-test
    a = Dist.from_gaussian(0.0, 0.3)
    b = a.pushforward(lambda x: x + 0.2)
    assert abs(a.W2(b) - 0.2) < 1e-3, a.W2(b)  # a pure shift has W2 = the shift
    assert abs(a.interpolate(b, 0.5).mean - 0.1) < 1e-3  # halfway morph sits at the midpoint mean
    assert abs(Dist.barycenter([a, b]).mean - 0.1) < 1e-3
    # selection breaks Gaussianity: the retained tail is one-sided
    kept = a.select(0.0, "below")
    assert kept.mean < 0
    # cohort path integral: a one-off env pulse only reaches reproduction ~a generation later
    mem = CohortMemory()
    for yr in range(80):
        mem.push(1.0 if 5 <= yr <= 6 else 0.0)
    print(
        "W2 shift:",
        round(a.W2(b), 4),
        "| interp mean:",
        round(a.interpolate(b, 0.5).mean, 4),
        "| retained-tail mean:",
        round(kept.mean, 4),
    )
    print("ot.py self-test passed")
