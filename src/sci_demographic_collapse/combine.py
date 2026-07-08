"""How interventions COMBINE in the emergent core - the log-TFR bilinear combination law.

The core's TFR is a product of bounded channel factors (Bongaarts multiplicativity):

    TFR = C * (1 - rho) * Pbar * fec(tau) * (1 - kBF * dtau)

so on the LOG scale the channels are ADDITIVE. Write the log-TFR steady-state response to a forcing
vector f (the 9-channel `interventions.CHANNELS` amplitudes) as L(f) = log TFR(f). The honest
combination law is the second-order (response-surface) expansion of L about the calibrated baseline f=0:

    L(f) = L(0) + g . f + 1/2 f^T H f ,        g = grad L(0),  H = Hessian L(0)

For two disjoint single-channel pushes f_A, f_B the genuine interaction is the mixed Hessian block

    I(A, B) = L(f_A + f_B) - L(f_A) - L(f_B) + L(0)  ~=  f_A^T H f_B .

Orthogonal channels (H off-diagonal = 0) => log-additive => TFR multiplicative => I = 0. The apparent
"super-additivity" of a bundle on the RAW dTFR scale is NOT interaction: it is the curvature of exp(),
  dTFR_joint - (dTFR_A + dTFR_B) = TFR_0 * (e^{L_A}-1)(e^{L_B}-1) > 0
for two positive pushes. This module reads that artifact off and returns the honest, sign-correct H.

H is NEVER hand-set: `grad_hess` estimates g and H by central finite differences on `EmergentModel.run_cal`
(the calibrated ensemble core). Its three mechanistic parts:
  * diagonal H_cc < 0  = same-channel saturation (a bounded link pushed twice composes sub-additively);
  * off-diagonal H_ab  = cross-channel ODE coupling (S->C, q->C, N->rho, S->tau) - the Jacobian of the
    channel-state response, the same coupling operator whose eigenvectors are the culture-bearer Phi's V;
  * diagonal H_cc > 0 and large near the bistable-N / coupling ridge = threshold synergy (two sub-tip
    pushes jointly cross the separatrix); this is where the second-order truncation is only local.

Baseline-preserving: at f=0, `predict` returns L(0) exactly and I(.,.) vanishes when channels decouple.
"""

from __future__ import annotations

import numpy as np

from .interventions import force_of

# central-difference step per channel (raw forcing-amplitude units), small vs bundle magnitudes
H_STEP = {
    "fS": 0.05,
    "fC": 0.03,
    "fPb": 0.10,
    "fTau": 1.0,
    "fRV": 0.03,
    "fN": 0.03,
    "fq": 0.03,
    "fF": 0.03,
    "fScar": 0.03,
}


def log_tfr(model, region: str, f: dict | None = None) -> float:
    """L(f) = log endpoint TFR of `region` under channel forcing dict `f` (None = baseline)."""
    force = force_of(f) if f else None
    return float(np.log(model.run_cal(region, force=force)["tfr"]))


def grad_hess(
    model, region: str, channels=("fS", "fC", "fPb", "fTau", "fRV", "fN"), step: dict | None = None
):
    """Central-difference gradient g and Hessian H of L=log TFR at f=0, over `channels`.

    Returns (channels, g, H, L0). H is symmetric; diagonal = own-curvature (saturation / threshold),
    off-diagonal H_ab = cross-channel coupling. Costs ~ 2n (grad+diag) + 4*nC2 (off-diag) run_cal evals.
    """
    h = {c: (step or H_STEP)[c] for c in channels}
    n = len(channels)
    L0 = log_tfr(model, region, None)

    def L(vec):  # vec: dict channel->amplitude
        return log_tfr(model, region, {k: v for k, v in vec.items() if v})

    lp = {c: L({c: h[c]}) for c in channels}  # L(+h e_c)
    lm = {c: L({c: -h[c]}) for c in channels}  # L(-h e_c)
    g = np.array([(lp[c] - lm[c]) / (2 * h[c]) for c in channels])
    H = np.zeros((n, n))
    for i, c in enumerate(channels):
        # own second derivative. NOTE fN: the norm channel sits on a double-well fixed point, so
        # L has a KINK at fN=0 - its second difference does not converge as O(h^2) and the fN
        # diagonal magnitude is step-dependent (only its SIGN is meaningful: + trapped, - basin).
        # Near the ridge use the direct interaction (`interaction`), not this quadratic term.
        H[i, i] = (lp[c] - 2 * L0 + lm[c]) / h[c] ** 2
    for i in range(n):
        for j in range(i + 1, n):
            ci, cj = channels[i], channels[j]
            hpp = L({ci: h[ci], cj: h[cj]})
            hpm = L({ci: h[ci], cj: -h[cj]})
            hmp = L({ci: -h[ci], cj: h[cj]})
            hmm = L({ci: -h[ci], cj: -h[cj]})
            H[i, j] = H[j, i] = (hpp - hpm - hmp + hmm) / (4 * h[ci] * h[cj])
    return list(channels), g, H, L0


def _vec(channels, f: dict) -> np.ndarray:
    return np.array([f.get(c, 0.0) for c in channels])


def predict(channels, g, H, L0: float, f: dict) -> float:
    """Pure second-order Taylor log-TFR L(f) ~= L0 + g.f + 1/2 f^T H f. f=0 returns L0 exactly.
    A LOCAL expansion: at large single-channel amplitude it carries the usual truncation error - the
    honest bundle law is `predict_bundle`, which uses the exact measured solo effects as main terms."""
    x = _vec(channels, f)
    return L0 + float(g @ x) + 0.5 * float(x @ H @ x)


def predict_bundle(channels, H, L0: float, solo_logeff: dict, f: dict) -> float:
    """The honest combination law for a multi-channel bundle, on the log scale:

        L(f) ~= L0 + sum_c [L(f_c) - L0]        # EXACT measured solo main effects (Bongaarts indices)
                   + sum_{a<b} f_a^T H f_b       # bilinear cross-channel interaction (mixed Hessian)

    `solo_logeff[c]` = measured L(f_c) - L0 for each active channel c (so a single-channel bundle
    reduces EXACTLY to its scalar result). Same-channel saturation lives inside the exact solo term;
    only genuine cross-channel coupling is the quadratic H residual."""
    active = [c for c in channels if f.get(c, 0.0)]
    main = sum(solo_logeff[c] for c in active)
    cross = 0.0
    for i in range(len(active)):
        for j in range(i + 1, len(active)):
            a, b = active[i], active[j]
            cross += interaction(channels, H, {a: f[a]}, {b: f[b]})
    return L0 + main + cross


def predict_tfr(channels, g, H, L0, f, tfr0: float) -> float:
    """Predicted endpoint TFR = exp(pure-Taylor predicted log-TFR). tfr0 = exp(L0) baseline."""
    return float(np.exp(predict(channels, g, H, L0, f)))


def interaction(channels, H, fA: dict, fB: dict) -> float:
    """Bilinear interaction I(A,B) = f_A^T H f_B (mixed-Hessian coupling). >0 synergy, <0 saturation."""
    return float(_vec(channels, fA) @ H @ _vec(channels, fB))


def raw_curvature_artifact(LA: float, LB: float, tfr0: float) -> float:
    """The RAW-scale apparent super-additivity from pure exp() curvature (zero true interaction):
    dTFR_joint - dTFR_A - dTFR_B = TFR0 (e^{LA}-1)(e^{LB}-1). This is what the plumbing misread."""
    return tfr0 * (np.exp(LA) - 1.0) * (np.exp(LB) - 1.0)


if __name__ == "__main__":  # self-test: baseline preservation + orthogonal-channel decoupling
    from pathlib import Path

    from .emergent import EmergentModel

    proj = Path(__file__).resolve().parents[2]
    m = EmergentModel(data_dir=str(proj / "data" / "raw" / "unwpp"))
    chans, g, H, L0 = grad_hess(m, "Germany")
    tfr0 = float(np.exp(L0))

    # 1. baseline preservation: predict(f=0) == L0 exactly; empty-bundle law == L0
    assert abs(predict(chans, g, H, L0, {}) - L0) < 1e-12
    assert abs(predict_bundle(chans, H, L0, {}, {}) - L0) < 1e-12

    # 2. a single-channel bundle reduces EXACTLY to its scalar result (measured solo main effect)
    fA, fB = {"fS": 0.15}, {"fPb": 0.4}
    solo = {"fS": log_tfr(m, "Germany", fA) - L0, "fPb": log_tfr(m, "Germany", fB) - L0}
    assert abs(predict_bundle(chans, H, L0, solo, fA) - (L0 + solo["fS"])) < 1e-12

    # 3. a cross pair: measured joint-minus-solos interaction ~= f_A^T H f_B (the bilinear law)
    LA, LB = solo["fS"], solo["fPb"]
    LAB = log_tfr(m, "Germany", {**fA, **fB}) - L0
    I_meas = LAB - LA - LB
    I_pred = interaction(chans, H, fA, fB)
    art = raw_curvature_artifact(LA, LB, tfr0)
    print(
        "combine.py self-test passed:",
        f"L0={L0:+.4f} tfr0={tfr0:.4f}",
        f"| I_meas(S,Pb)={I_meas:+.5f} I_pred={I_pred:+.5f}",
        f"| bundle-law resid={predict_bundle(chans, H, L0, solo, {**fA, **fB}) - (L0 + LAB):+.5f}",
        f"| raw-artifact(+dTFR)={art:+.5f}",
        f"| diag(H)={np.round(np.diag(H), 3)}",
    )
    assert abs(I_meas - I_pred) < 5e-3
