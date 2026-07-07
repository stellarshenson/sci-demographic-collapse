"""Population-distribution framework (E30+) - lift a scalar channel to a heterogeneous population.

Every behavioural channel in `emergent` is, by default, a representative-agent scalar (one value for the
whole country). Real populations are heterogeneous: coupling propensity, marriageability, responsiveness to
an intervention all vary person to person. This module lifts a scalar parameter theta to a population random
variable via the reparameterisation trick,

    theta = mu + sigma * eps,      eps ~ N(0, 1),

and discretises p(theta) into K buckets with Gauss-Hermite quadrature (nodes eps_k, weights w_k). Any
observable is then the Jensen-correct population average

    <f> = sum_k w_k * f(mu + sigma * eps_k)   !=   f(mu),

which is what matters wherever f is nonlinear (a bistable norm, the coupling trap, a marriageability
threshold) or wherever an intervention acts on the tail of the distribution (selection - the matriarchy
male-exit and female hypergamy are literally tail operations on the marriageability distribution).

The same machinery lifts any channel; the payoff is largest for the nonlinear and selection-driven ones.

    q = PopChannel(mu=0.0, sigma=0.25, K=7)
    q.aggregate(gate)                 # Jensen-correct coupling gate over the population
    q.respond(0.15, lambda t: 1-t)    # therapy helps the low-marriageability tail more, accumulates
    kept = q.select(thresh=0.3, side="below")   # high-q men exit -> retained (weight, mean) of the rest
"""
from __future__ import annotations

import numpy as np


class PopChannel:
    """A scalar channel lifted to a bucketed population distribution N(mu, sigma) via Gauss-Hermite nodes.

    Buckets are fixed-probability quadrature nodes: values track mu and sigma, weights are constant. Use
    `aggregate` for Jensen-correct observables, `shift`/`respond` for interventions on the mean/spread/tail,
    `select` for selection (exit, hypergamy), and `step` to evolve each bucket under its own dynamics.
    """

    def __init__(self, mu: float = 0.0, sigma: float = 1.0, K: int = 7):
        if K < 1:
            raise ValueError("K must be >= 1")
        self.mu = float(mu)
        self.sigma = float(sigma)
        # Gauss-Hermite nodes/weights for E[f] under N(mu, sigma): x = mu + sqrt(2) sigma * node
        nodes, weights = np.polynomial.hermite_e.hermegauss(K)  # weights sum to sqrt(2 pi)
        self.eps = nodes                                        # standard-normal quadrature abscissae
        self.w = weights / weights.sum()                       # normalised population weights
        # explicit per-bucket values, so buckets can also be evolved independently of (mu, sigma)
        self.theta = self.mu + self.sigma * self.eps

    # -- observables -------------------------------------------------------
    def values(self) -> np.ndarray:
        """Current per-bucket parameter values theta_k."""
        return self.theta

    def aggregate(self, f) -> float:
        """Jensen-correct population average <f> = sum_k w_k f(theta_k)."""
        return float(np.sum(self.w * np.vectorize(f)(self.theta)))

    def mean(self) -> float:
        """Population mean of theta (weight-weighted)."""
        return float(np.sum(self.w * self.theta))

    def std(self) -> float:
        """Population standard deviation of theta."""
        m = self.mean()
        return float(np.sqrt(np.sum(self.w * (self.theta - m) ** 2)))

    def jensen_gap(self, f) -> float:
        """<f> - f(<theta>): the heterogeneity correction to a representative-agent evaluation."""
        return self.aggregate(f) - float(np.vectorize(f)(self.mean()))

    # -- interventions -----------------------------------------------------
    def shift(self, dmu: float = 0.0, dsigma: float = 0.0) -> "PopChannel":
        """Shift the whole distribution's mean and/or spread (e.g. inequality widens sigma). In place."""
        self.mu += dmu
        self.sigma = max(self.sigma + dsigma, 0.0)
        self.theta = self.mu + self.sigma * self.eps
        return self

    def respond(self, effect: float, response_fn=None) -> "PopChannel":
        """Apply a heterogeneous intervention: theta_k += effect * response_fn(theta_k), accumulating.

        `response_fn` maps a bucket's current value to its responsiveness in [0, 1] (default: uniform 1.0).
        This is the distributional generalisation of a scalar delta - the treatable tail responds, the
        resistant tail barely moves. Operates on per-bucket theta directly (mu/sigma re-derived).
        """
        r = np.ones_like(self.theta) if response_fn is None else np.vectorize(response_fn)(self.theta)
        self.theta = self.theta + effect * r
        self.mu = self.mean()
        self.sigma = self.std()
        return self

    def step(self, dfn, dt: float = 1.0) -> "PopChannel":
        """Evolve each bucket by its own dynamics: theta_k += dt * dfn(theta_k). In place."""
        self.theta = self.theta + dt * np.vectorize(dfn)(self.theta)
        self.mu = self.mean()
        self.sigma = self.std()
        return self

    # -- selection (tail operations) --------------------------------------
    def select(self, thresh: float, side: str = "below") -> dict:
        """Tail selection: keep buckets on one side of `thresh` (e.g. the low-value men who stay).

        Returns the retained sub-population's weight and mean without mutating self. `side="below"` keeps
        theta < thresh (the retained low-value tail after the high-value tail exits); `side="above"` keeps
        theta >= thresh (the acceptable partners a hypergamous chooser will consider).
        """
        mask = self.theta < thresh if side == "below" else self.theta >= thresh
        wk = self.w[mask]
        tot = float(wk.sum())
        mean = float(np.sum(wk * self.theta[mask]) / tot) if tot > 0 else float("nan")
        return dict(weight=tot, mean=mean, n=int(mask.sum()))

    def match_prob(self, thresh: float) -> float:
        """Share of the population acceptable to a chooser with a hypergamy bar at `thresh`."""
        return self.select(thresh, side="above")["weight"]

    def copy(self) -> "PopChannel":
        c = PopChannel(self.mu, self.sigma, len(self.eps))
        c.theta = self.theta.copy()
        return c


def representative_gap(mu: float, sigma: float, f, K: int = 7) -> float:
    """Convenience: the Jensen gap of f for a N(mu, sigma) population at spread sigma."""
    return PopChannel(mu, sigma, K).jensen_gap(f)
