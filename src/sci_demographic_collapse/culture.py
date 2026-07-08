"""Culture-bearer transmission operator (GOAL-16 Phase A), a modular default-OFF addition.

A culture bearer is a parent handing a coherent BUNDLE of channel traits to the next cohort; cultures
that transmit the bundle to more children and RETAIN it grow their population share generation after
generation (cultural natural selection, Perron-Frobenius). Culture is a single linear machine acting on
the trait vector `x` - it ROTATES (correlated traits travel together) and SCALES (amplifies some bundles,
fades others). At cohort renewal,

    Δx  =  r · V Λ V⁻¹ · ( x̄ᵂ_parents − x_current )          x_next = x_baseline_next + Δx

  * V - cultural-archetype eigenvectors (coherent channel bundles). NOT invented: the eigenvectors of
        the cultural sub-block of the intervention-combination Hessian H = ∇²logTFR(0) (`combine.grad_hess`).
        H is symmetric so V is orthonormal (V⁻¹ = Vᵀ). One operator, two phenomena: the directions that
        diagonalise how interventions combine also diagonalise how culture transmits.
  * Λ - diagonal per-bundle transmission FIDELITY (>1 amplify, <1 fade); the composite/per-component knob.
  * r - scalar RETENTION gate and the single on/off switch. r=0 → Δx=0 → mathematical NO-OP, so the core
        reproduces its committed baseline to machine precision.
  * x̄ᵂ - FERTILITY-WEIGHTED parental mean (weight ∝ each subgroup's realised TFR); this weighting is what
        arcs iterated application toward the operator's dominant eigenvector = whichever culture out-
        reproduces and retains the rest (Collins-Page selection). A small ε noise term is permitted.

Cultural subset = the four channels transmitted as IDEALS: coupling C, childlessness ρ, parity P̄, norm N
(state indices 0, 1, 2, 5). Security/tempo/marriageability are structural background (they GATE
transmission, per Ihara-Feldman, but are not the transmitted trait) and are excluded. Grounding and the
derivation of V from H are in `docs/culture-bearer-modelling.md`.

Depends only on numpy at module load (no emergent/combine import) to avoid an import cycle; `from_model`
imports `combine` lazily.
"""
from __future__ import annotations

import numpy as np

# cultural channels carried by the bearer, as (state-vector index, combine.py Hessian channel).
# state order in emergent is [C, rv, Pb, tau, S, N, q]; H channel order is (fS, fC, fPb, fTau, fRV, fN).
CULTURAL = (("C", 0, "fC"), ("rv", 1, "fRV"), ("Pb", 2, "fPb"), ("N", 5, "fN"))
STATE_IDX = tuple(s for _, s, _ in CULTURAL)          # (0, 1, 2, 5) columns of the 7-vector
HCHAN = tuple(h for _, _, h in CULTURAL)              # ("fC", "fRV", "fPb", "fN")
# emergent's channel bounds for the cultural columns, so a nudged trait stays in the valid range
CLIP = ((0.02, 0.999), (0.0, 0.6), (1.0, np.inf), (0.0, 1.0))

# Empirically anchored config (GOAL-16 Phase B). The MODULAR DEFAULT STAYS OFF (r=0); this is opt-in.
# r is pinned to the observed one-generation parent-child fertility correlation. Along an eigen-direction
# the update is x_next = (1-phi) x + phi xbar_W with eigenvalue phi = r*lam, so the population mean-response
# is R = phi*S with S the fertility-weighted selection differential - exactly the breeder's equation
# R = h^2*S (Collins & Page, 2019). h^2 is the offspring-on-parent regression = the intergenerational
# fertility correlation, so implied corr = r*lam. A single aggregate correlation identifies only the
# product, so Lambda = I (no per-bundle fidelity evidence) and r = corr. Kolk (2014) parent-child
# completed-fertility correlation ~0.10-0.20 -> r = 0.15 (midpoint). With Lambda = I, Phi = r*V V^T = r*I,
# so V is IMMATERIAL (any region's eigenbasis gives the same operator). gen = 30yr = one generation (the
# breeder's response is per-generation; the nudge fires once per 30yr, not annually). Measured effect once
# anchored: max|dTFR| ~ 4e-4 over 2050-2125 (negligible) - it does NOT touch the 2023 calibration (first
# renewal is post-2023 at yr=gen). Build via `CultureOperator.anchored(model, region)`.
CULTURE_ANCHOR = {"r": 0.15, "lam": (1.0, 1.0, 1.0, 1.0), "gen": 30, "corr_range": (0.10, 0.20)}


class CultureOperator:
    """The transmission machine Φ = r · V Λ V⁻¹ acting on the cultural sub-vector of the channel state.

    Construct from a Hessian (`from_hessian`) or from a model+region (`from_model`, which computes H once).
    `r` defaults to 0 → the operator is the zero map and every call is a no-op. `lam` (the Λ diagonal)
    defaults to ones → isotropic retention with no bundle differentiation.
    """

    def __init__(self, V: np.ndarray, r: float = 0.0, lam: np.ndarray | None = None,
                 eps: float = 0.0, gen: int = 30, seed: int = 0):
        self.V = np.asarray(V, dtype=float)              # (d, d) orthonormal eigenvectors (columns = bundles)
        self.d = self.V.shape[0]
        self.r = float(r)
        self.lam = np.ones(self.d) if lam is None else np.asarray(lam, dtype=float)
        self.eps = float(eps)
        self.gen = int(gen)                              # cohort-renewal period in years (generation length)
        self.state_idx = np.array(STATE_IDX)
        self._rng = np.random.default_rng(seed)

    @classmethod
    def from_hessian(cls, channels, H: np.ndarray, **kw) -> "CultureOperator":
        """Build V from the cultural sub-block of a full Hessian `H` over `channels` (its channel names).

        Restricts H to the (fC, fRV, fPb, fN) rows/cols, symmetric-eigendecomposes it (orthonormal V).
        """
        idx = [list(channels).index(h) for h in HCHAN]
        sub = np.asarray(H, dtype=float)[np.ix_(idx, idx)]
        _, V = np.linalg.eigh(0.5 * (sub + sub.T))       # symmetrise defensively; eigh → orthonormal V
        return cls(V, **kw)

    @classmethod
    def from_model(cls, model, region: str, **kw) -> "CultureOperator":
        """Compute H once on `model` for `region` (calibrated core) and build V from its cultural block."""
        from . import combine
        chans, _g, H, _L0 = combine.grad_hess(model, region, channels=("fS", "fC", "fPb", "fTau", "fRV", "fN"))
        return cls.from_hessian(chans, H, **kw)

    @classmethod
    def anchored(cls, model, region: str = "Germany", **kw) -> "CultureOperator":
        """The empirically anchored operator (`CULTURE_ANCHOR`): r=0.15 to the observed intergenerational
        fertility correlation (Kolk 2014; breeder's equation, Collins-Page 2019), Lambda=I, gen=30. Opt-in
        - the module default stays OFF (r=0). V is immaterial under Lambda=I (Phi=r*I), so `region` only
        sets which eigenbasis is built; the anchored operator is region-independent."""
        a = CULTURE_ANCHOR
        return cls.from_model(model, region, r=a["r"], lam=np.array(a["lam"]), gen=a["gen"], **kw)

    @property
    def matrix(self) -> np.ndarray:
        """The operator Φ = r · V Λ V⁻¹ (= r · V Λ Vᵀ, V orthonormal). r=0 → zero matrix."""
        return self.r * (self.V * self.lam) @ self.V.T

    def dominant(self) -> np.ndarray:
        """Unit eigenvector of Φ with the largest |eigenvalue| = the bundle iterated application arcs to."""
        return self.V[:, int(np.argmax(np.abs(self.r * self.lam)))]

    @staticmethod
    def weighted_mean(X: np.ndarray, w: np.ndarray) -> np.ndarray:
        """Fertility-weighted parental mean x̄ᵂ = Σ w_k x_k / Σ w_k over the K subgroups (rows of X)."""
        w = np.clip(np.asarray(w, dtype=float), 0.0, None)
        s = w.sum()
        return (w @ X) / s if s > 0 else X.mean(axis=0)

    def delta(self, X: np.ndarray, w: np.ndarray) -> np.ndarray:
        """Per-subgroup trait update Δx = r · Φ · (x̄ᵂ − x) + ε ξ over the K rows of the cultural block X.

        X: (K, d) cultural sub-vectors; w: (K,) fertility weights. r=0 → exact zeros (no-op guarantee).
        """
        if self.r == 0.0:
            return np.zeros_like(X)
        xbar = self.weighted_mean(X, w)
        dx = (self.matrix @ (xbar - X).T).T
        if self.eps > 0.0:
            dx = dx + self.eps * self._rng.standard_normal(X.shape)
        return dx

    def is_renewal(self, yr: int) -> bool:
        """True at cohort-renewal years (every `gen` years, excluding the initial year)."""
        return self.r != 0.0 and yr > 0 and yr % self.gen == 0

    def apply(self, st: np.ndarray, tfr: np.ndarray, yr: int) -> np.ndarray:
        """Apply the operator to the (K, 7) ensemble state at year `yr`; identity unless a renewal year.

        Nudges only the cultural columns (C, rv, Pb, N) by `delta`, weighting subgroups by realised TFR.
        Returns `st` UNCHANGED (same array) off renewal years or when r=0, so the baseline is byte-identical.
        """
        if not self.is_renewal(yr):
            return st
        X = st[:, self.state_idx]
        Xn = X + self.delta(X, tfr)
        for j, (lo, hi) in enumerate(CLIP):
            Xn[:, j] = np.clip(Xn[:, j], lo, hi)
        st[:, self.state_idx] = Xn
        return st
