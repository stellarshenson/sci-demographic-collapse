"""Coupled emergent behavioural model (E19/E22), extracted for reuse.

The behavioural layer models fertility as an emergent product of five coupled, observable channels -
coupling C, childlessness rho, parity Pbar, tempo tau, and economic security S - each with its own
first-order dynamics, wrapped around the calibrated Leslie core in `coremodel`. TFR is
`quantum(C, rho, Pbar) * fec(tau) * (1 - kBF * dtau)` with a Bongaarts-Feeney period term, a soft-bistable
coupling trap near the empirical TFR-1.5 ridge, and a dependency->security feedback through the age pyramid.

Interventions enter as a forcing function `force(year) -> [fS, fC, fPbar, ftau, frho]`. This is the same
model validated in notebooks 14-17; import it instead of re-deriving it.

    m = EmergentModel(data_dir="data/raw/unwpp")
    base = m.run("Korea")                       # baseline TFR trajectory to 2125
    lifted = m.run("Korea", m.coupling(0.20))   # a coupling push
"""

from __future__ import annotations

import numpy as np
import torch

from . import coremodel as cm
from .ot import CohortMemory

# 2023 calibration targets (TFR, mean age at first birth) and channel start values
REAL = {
    "USA": (1.62, 29.4),
    "France": (1.64, 31.1),
    "Germany": (1.44, 31.0),
    "Italy": (1.20, 31.8),
    "Japan": (1.21, 31.4),
    "Korea": (0.72, 32.9),
    # Poland: TFR from GUS (national office) 2023 = 1.16, not UN WPP's 1.30; age-at-childbearing
    # 29.9 from the same UN WPP series the others use. GUS 2024 fell further to 1.099.
    "Poland": (1.16, 29.9),
}
C0 = {
    "USA": 0.90,
    "France": 0.95,
    "Germany": 0.86,
    "Italy": 0.83,
    "Japan": 0.80,
    "Korea": 0.52,
    "Poland": 0.82,
}
RV0 = {
    "USA": 0.07,
    "France": 0.07,
    "Germany": 0.09,
    "Italy": 0.10,
    "Japan": 0.10,
    "Korea": 0.08,
    "Poland": 0.10,
}
S0 = {
    "USA": 0.58,
    "France": 0.62,
    "Germany": 0.52,
    "Italy": 0.45,
    "Japan": 0.45,
    "Korea": 0.40,
    "Poland": 0.45,
}

# social-norm state N (E25): share endorsing a childfree ideal, modelled as a bistable
# contagion with two stable wells (Nlo untrapped, Nhi trapped) and an unstable tipping point
# thN. Each region starts snapped to its basin so baseline N is a fixed point of the unforced
# dynamics and the norm->rho coupling lam_rho*(N-N0) is identically zero at today's calibration.
NORM0 = {
    "USA": 0.14,
    "France": 0.14,
    "Germany": 0.14,
    "Italy": 0.42,
    "Japan": 0.42,
    "Korea": 0.42,
    "Poland": 0.42,
}

# ensemble calibration (Phase 2, the distributional core). SIGMA_CAL is the grounded, structural
# population-heterogeneity spread per channel (age-at-first-birth SD ~3yr; parity intentions spread widest;
# norm/security/marriageability moderate; coupling/childlessness tight) - these are NOT fit parameters.
# PB_SCALE_ENS is the one calibration free parameter re-solved per region so the DISPERSED baseline still
# reproduces the 2023 REAL TFR (Pb is how the scalar PB0 was calibrated too). Regenerate via calibrate_ens().
SIGMA_CAL = {"C": 0.05, "rv": 0.03, "Pb": 0.15, "tau": 3.0, "S": 0.10, "N": 0.06, "q": 0.10}
PB_SCALE_ENS = {
    "USA": 1.0276,
    "France": 1.0404,
    "Germany": 1.0350,
    "Italy": 1.0301,
    "Japan": 1.0322,
    "Korea": 1.0333,
    "Poland": 1.0372,  # re-solved by calibrate_ens; dispersed baseline reproduces GUS TFR 1.16 exactly
}

# behavioural rate constants (calibrated in E19; norm constants added in E25; marriageability +
# intergenerational-memory constants added in E30)
PARAMS = dict(
    kC=0.08,
    C_thr=0.66,
    C_floor=0.24,
    decl=0.05,
    gS_C=0.9,
    secC=0.0007,
    kPb=0.05,
    gPb=1.2,
    secPb=0.0010,
    kTau=0.06,
    gTau=6.0,
    secTau=0.006,
    kRV=0.03,
    gRV=0.012,
    kS=0.06,
    secS=0.0010,
    kBF=0.6,
    dep_fb=0.22,
    aN=2.5,
    thN=0.25,
    Nlo=0.14,
    Nhi=0.42,
    lam_rho=0.30,
    # marriageability capital q (bilateral) gates coupling; fed by therapy/health and by the
    # lifetime-integrated childhood environment of the current reproductive cohort (alienation).
    kq=0.06,
    gqC=0.9,
    phi=0.4,
    wF=0.6,
    wS=0.3,
    wScar=0.5,
    gA=0.5,
    lagLo=27,
    lagHi=45,
)


def fec(tau: float) -> float:
    """Fecundability multiplier: decays above age 30."""
    return np.exp(-0.03 * max(tau - 30.0, 0.0))


def quantum(C: float, rv: float, Pb: float) -> float:
    """Completed-fertility quantum before the tempo term: C*(1-rho)*Pbar."""
    return C * (1 - rv) * Pb


def ramp(yr: int, start: int = 0, s: int = 2, d: int = 10) -> float:
    """Linear policy ramp: 0 until `s`, full after `s+d`."""
    yr = yr - start
    return min(max((yr - s) / d, 0.0), 1.0) if yr >= 0 else 0.0


def erode(yr: int, s: int = 2, d: int = 10) -> float:
    """Durability envelope for non-permanent levers: full then exponential decay."""
    return 1.0 if yr <= s + d else float(np.exp(-(yr - s - d) / 12))


def _shift_profile(asfr: np.ndarray, mult: float, dtau: float) -> np.ndarray:
    """Scale an ASFR profile by `mult` and shift it by `dtau` years (tempo)."""
    b = asfr * mult
    s = int(round(dtau))
    if s > 0:
        b = np.concatenate([np.zeros(min(s, len(b))), b[:-s]]) if s < len(b) else b * 0
    elif s < 0:
        b = np.concatenate([b[-s:], np.zeros(min(-s, len(b)))]) if -s < len(b) else b * 0
    return np.clip(b, 0, None)


class EmergentModel:
    """The coupled behavioural x Leslie model, calibrated to real 2023 fertility."""

    def __init__(self, data_dir: str, y0: int = 1990, y1: int = 2023, params: dict | None = None):
        self.REG = cm.load_unwpp(data_dir=str(data_dir), y0=y0, y1=y1)
        self.DEV = cm.DEV
        self.RC = cm.rogers_castro()
        self.P = dict(params or PARAMS)
        # parity constant that reproduces each region's 2023 TFR at its start state
        self.PB0 = {nm: T / (C0[nm] * (1 - RV0[nm]) * fec(mab)) for nm, (T, mab) in REAL.items()}

    def _estep(self, nm, st, force, tn, dep_pen, A_lag=0.0, dt=0.25):
        p = self.P
        C, rv, Pb, tau, S, N, q = st
        fS, fC, fPb, fTau, fRV = force[:5]
        fN = force[5] if len(force) > 5 else 0.0
        fq = force[6] if len(force) > 6 else 0.0
        dS = p["kS"] * (S0[nm] + fS - dep_pen - S) - p["secS"]
        # marriageability capital q (deviation from 0): therapy/health + integrated intergenerational env
        dq = p["kq"] * (fq + A_lag - q)
        # q gates coupling as a baseline-preserving deviation (bilateral marriageability -> partnership)
        Ceq = C0[nm] + p["gS_C"] * (S - S0[nm]) + p["gqC"] * q + fC - p["secC"] * 100 * tn
        dC = p["kC"] * (Ceq - C) - p["decl"] * max(p["C_thr"] - C, 0) * max(
            C - p["C_floor"], 0
        ) / (p["C_thr"] - p["C_floor"])
        dPb = p["kPb"] * (self.PB0[nm] + p["gPb"] * fPb - p["secPb"] * 100 * tn - Pb)
        dtau = p["kTau"] * (
            REAL[nm][1] + p["gTau"] * (S0[nm] - S) + fTau + p["secTau"] * 100 * tn - tau
        )
        # bistable social norm: cubic double-well (wells Nlo, Nhi; unstable tip thN) plus forcing
        dN = -p["aN"] * (N - p["Nlo"]) * (N - p["thN"]) * (N - p["Nhi"]) + fN
        # norm couples to childlessness as a baseline-preserving deviation from N0
        drv = p["kRV"] * (
            RV0[nm]
            + p["gRV"] * max(tau - 30, 0)
            - 0.05 * (S - S0[nm])
            + p["lam_rho"] * (N - NORM0[nm])
            + fRV
            - rv
        )
        return np.array(
            [
                np.clip(C + dt * dC, 0.02, 0.999),
                np.clip(rv + dt * drv, 0, 0.6),
                max(Pb + dt * dPb, 1.0),
                np.clip(tau + dt * dtau, 24, 40),
                np.clip(S + dt * dS, 0.05, 0.95),
                np.clip(N + dt * dN, 0.0, 1.0),
                np.clip(q + dt * dq, -1.0, 1.0),
            ]
        ), dtau

    def run(self, region: str, force=None, years: int = 102) -> dict:
        """Integrate `region` forward `years` from 2023 under an optional forcing function.

        `force` maps a year index to `[fS, fC, fPbar, ftau, frho]`; None means the baseline.
        Returns dict with the TFR and C trajectories, end states, and percent population change.
        """
        if force is None:
            force = lambda yr: [0.0] * 6  # noqa: E731
        st = np.array(
            [
                C0[region],
                RV0[region],
                self.PB0[region],
                REAL[region][1],
                S0[region],
                NORM0[region],
                0.0,
            ]
        )
        R = self.REG[region]
        nf = torch.tensor(R["pop_f"][-1].copy(), device=self.DEV)
        nm = torch.tensor(R["pop_m"][-1].copy(), device=self.DEV)
        Sx0 = R["Sx"][-1].copy()
        srb = float(R["ind"]["SRB"][-1])
        base = R["asfr"][-1].copy()
        tfrb = base.sum()
        pop0 = float(nf.sum() + nm.sum())
        d0 = (nf + nm).cpu().numpy()
        dep0 = float(d0[65:].sum() / max(d0[20:65].sum(), 1))
        dep_pen = 0.0
        Ctr, Ttr, Ntr, Qtr = [], [], [], []
        p = self.P
        # per-cohort path integral (ot.CohortMemory) - the Lagrangian method-of-characteristics form of the
        # intergenerational memory, replacing the earlier aggregate mean-field lag over calendar years
        mem = CohortMemory(childhood=18, repro_lo=p["lagLo"], repro_hi=p["lagHi"])
        A_lag = 0.0
        tfr = tfrb
        for yr in range(years):
            f = force(yr)
            fF = f[7] if len(f) > 7 else 0.0  # father-access / paternity forcing
            fScar = f[8] if len(f) > 8 else 0.0  # relationship-scar forcing
            dtau = 0.0
            for _ in range(4):
                st, dt_ = self._estep(region, st, f, yr / 100.0, dep_pen, A_lag)
                dtau += dt_
            C, rv, Pb, tau, S, N, q = st
            # childhood environment this year: father investment (access + healthier fathers via q) minus
            # relationship scars; the current reproductive cohort's marriageability is the integral of the
            # environment they experienced 27-45 years ago (a one-generation distributed lag). Measured as a
            # deviation from intervention only (no baseline-S coupling), so env is identically zero on baseline.
            F = fF + p["phi"] * q
            env = p["wF"] * F - p["wScar"] * fScar
            mem.push(env)
            A_lag = (
                p["gA"] * mem.reproductive_mean()
            )  # mean completed childhood integral over reproductive cohorts
            tfr = quantum(C, rv, Pb) * fec(tau) * (1 - self.P["kBF"] * dtau)
            Sx = 1 - (1 - Sx0) * (1 - 0.003) ** (yr + 1)
            nf, nm, _b, _d = cm.leslie_step(
                nf,
                nm,
                torch.tensor(Sx, device=self.DEV),
                torch.tensor(
                    _shift_profile(base, tfr / tfrb if tfrb > 1e-6 else 0, tau - REAL[region][1]),
                    device=self.DEV,
                ),
                srb,
                torch.tensor(0.0 * self.RC, device=self.DEV),
            )
            tot = (nf + nm).cpu().numpy()
            dep = float(tot[65:].sum() / max(tot[20:65].sum(), 1))
            dep_pen = self.P["dep_fb"] * max(dep - dep0, 0)
            Ctr.append(C)
            Ttr.append(tfr)
            Ntr.append(N)
            Qtr.append(q)
        return dict(
            C=np.array(Ctr),
            TFR=np.array(Ttr),
            N=np.array(Ntr),
            q=np.array(Qtr),
            Cend=float(C),
            Nend=float(N),
            qend=float(q),
            Pbend=float(Pb),
            Send=float(S),
            rvend=float(rv),
            tauend=float(tau),
            tfr=float(tfr),
            pop_pct=(float(tot.sum()) / pop0 - 1) * 100,
        )

    def run_dist(
        self, region: str, force=None, sigmaN: float = 0.06, Kd: int = 41, years: int = 102
    ) -> dict:
        """Distributional-norm variant of `run` (the first channel of the distributional core rebuild).

        The bistable norm N is carried as a `Kd`-atom population with dispersion `sigmaN`, so it SPLITS at the
        tipping point instead of switching as one block; the rho coupling uses the population mean. `sigmaN`->0
        reproduces `run` exactly (baseline-preserving); a real dispersion recovers the fidelity the
        representative agent throws away near the tip. Only the norm channel is lifted here - the others stay
        scalar (the lift only earns its keep where the channel is nonlinear).
        """
        if force is None:
            force = lambda yr: [0.0] * 6  # noqa: E731
        p = self.P
        C, rv, Pb, tau, S, qc = (
            C0[region],
            RV0[region],
            self.PB0[region],
            REAL[region][1],
            S0[region],
            0.0,
        )
        u = (np.arange(Kd) + 0.5) / Kd
        z = torch.special.ndtri(torch.tensor(u, dtype=torch.float64)).numpy()
        Nd = np.clip(
            NORM0[region] + sigmaN * z, 0.0, 1.0
        )  # the norm population, spread around its well
        R = self.REG[region]
        nf = torch.tensor(R["pop_f"][-1].copy(), device=self.DEV)
        nm = torch.tensor(R["pop_m"][-1].copy(), device=self.DEV)
        Sx0 = R["Sx"][-1].copy()
        srb = float(R["ind"]["SRB"][-1])
        base = R["asfr"][-1].copy()
        tfrb = base.sum()
        pop0 = float(nf.sum() + nm.sum())
        d0 = (nf + nm).cpu().numpy()
        dep0 = float(d0[65:].sum() / max(d0[20:65].sum(), 1))
        dep_pen = 0.0
        mem = CohortMemory(childhood=18, repro_lo=p["lagLo"], repro_hi=p["lagHi"])
        A_lag = 0.0
        Ttr, Ntr = [], []
        tfr = tfrb
        dt = 0.25
        for yr in range(years):
            f = force(yr)
            fS, fC, fPb, fTau, fRV = f[:5]
            fN = f[5] if len(f) > 5 else 0.0
            fq = f[6] if len(f) > 6 else 0.0
            fF = f[7] if len(f) > 7 else 0.0
            fScar = f[8] if len(f) > 8 else 0.0
            tn = yr / 100.0
            dtau_acc = 0.0
            for _ in range(4):
                Nmean = float(Nd.mean())
                dS = p["kS"] * (S0[region] + fS - dep_pen - S) - p["secS"]
                dq = p["kq"] * (fq + A_lag - qc)
                Ceq = (
                    C0[region]
                    + p["gS_C"] * (S - S0[region])
                    + p["gqC"] * qc
                    + fC
                    - p["secC"] * 100 * tn
                )
                dC = p["kC"] * (Ceq - C) - p["decl"] * max(p["C_thr"] - C, 0) * max(
                    C - p["C_floor"], 0
                ) / (p["C_thr"] - p["C_floor"])
                dPb = p["kPb"] * (self.PB0[region] + p["gPb"] * fPb - p["secPb"] * 100 * tn - Pb)
                dtau = p["kTau"] * (
                    REAL[region][1]
                    + p["gTau"] * (S0[region] - S)
                    + fTau
                    + p["secTau"] * 100 * tn
                    - tau
                )
                drv = p["kRV"] * (
                    RV0[region]
                    + p["gRV"] * max(tau - 30, 0)
                    - 0.05 * (S - S0[region])
                    + p["lam_rho"] * (Nmean - NORM0[region])
                    + fRV
                    - rv
                )
                dNd = -p["aN"] * (Nd - p["Nlo"]) * (Nd - p["thN"]) * (Nd - p["Nhi"]) + fN
                C = float(np.clip(C + dt * dC, 0.02, 0.999))
                rv = float(np.clip(rv + dt * drv, 0, 0.6))
                Pb = max(Pb + dt * dPb, 1.0)
                tau = float(np.clip(tau + dt * dtau, 24, 40))
                S = float(np.clip(S + dt * dS, 0.05, 0.95))
                qc = float(np.clip(qc + dt * dq, -1.0, 1.0))
                Nd = np.clip(Nd + dt * dNd, 0.0, 1.0)
                dtau_acc += dtau
            tfr = quantum(C, rv, Pb) * fec(tau) * (1 - p["kBF"] * dtau_acc)
            Sx = 1 - (1 - Sx0) * (1 - 0.003) ** (yr + 1)
            nf, nm, _b, _d = cm.leslie_step(
                nf,
                nm,
                torch.tensor(Sx, device=self.DEV),
                torch.tensor(
                    _shift_profile(base, tfr / tfrb if tfrb > 1e-6 else 0, tau - REAL[region][1]),
                    device=self.DEV,
                ),
                srb,
                torch.tensor(0.0 * self.RC, device=self.DEV),
            )
            tot = (nf + nm).cpu().numpy()
            dep = float(tot[65:].sum() / max(tot[20:65].sum(), 1))
            dep_pen = p["dep_fb"] * max(dep - dep0, 0)
            F = fF + p["phi"] * qc
            env = p["wF"] * F - p["wScar"] * fScar
            mem.push(env)
            A_lag = p["gA"] * mem.reproductive_mean()
            Ttr.append(tfr)
            Ntr.append(float(Nd.mean()))
        return dict(
            TFR=np.array(Ttr),
            N=np.array(Ntr),
            Nend=float(Nd.mean()),
            Cend=float(C),
            tfr=float(tfr),
            pop_pct=(float(tot.sum()) / pop0 - 1) * 100,
        )

    def _estep_vec(self, nm, st, force, tn, dep_pen, A_lag=0.0, dt=0.25):
        """Vectorised `_estep` over a K-agent ensemble. `st` is (K,7); returns ((K,7), dtau (K,)).

        Identical dynamics to `_estep`, elementwise over agents. The population-level couplings (`dep_pen`
        from the age pyramid, `A_lag` from the cohort path integral, `tn`) are shared scalars; every other
        term uses each agent's OWN state, which is where the Jensen gap and the bistable-N split live.
        """
        p = self.P
        C, rv, Pb, tau, S, N, q = (st[:, i] for i in range(7))
        fS, fC, fPb, fTau, fRV = force[:5]
        fN = force[5] if len(force) > 5 else 0.0
        fq = force[6] if len(force) > 6 else 0.0
        dS = p["kS"] * (S0[nm] + fS - dep_pen - S) - p["secS"]
        dq = p["kq"] * (fq + A_lag - q)
        Ceq = C0[nm] + p["gS_C"] * (S - S0[nm]) + p["gqC"] * q + fC - p["secC"] * 100 * tn
        dC = p["kC"] * (Ceq - C) - p["decl"] * np.clip(p["C_thr"] - C, 0, None) * np.clip(
            C - p["C_floor"], 0, None
        ) / (p["C_thr"] - p["C_floor"])
        dPb = p["kPb"] * (self.PB0[nm] + p["gPb"] * fPb - p["secPb"] * 100 * tn - Pb)
        dtau = p["kTau"] * (
            REAL[nm][1] + p["gTau"] * (S0[nm] - S) + fTau + p["secTau"] * 100 * tn - tau
        )
        dN = -p["aN"] * (N - p["Nlo"]) * (N - p["thN"]) * (N - p["Nhi"]) + fN
        drv = p["kRV"] * (
            RV0[nm]
            + p["gRV"] * np.clip(tau - 30, 0, None)
            - 0.05 * (S - S0[nm])
            + p["lam_rho"] * (N - NORM0[nm])
            + fRV
            - rv
        )
        out = np.stack(
            [
                np.clip(C + dt * dC, 0.02, 0.999),
                np.clip(rv + dt * drv, 0, 0.6),
                np.clip(Pb + dt * dPb, 1.0, None),
                np.clip(tau + dt * dtau, 24, 40),
                np.clip(S + dt * dS, 0.05, 0.95),
                np.clip(N + dt * dN, 0.0, 1.0),
                np.clip(q + dt * dq, -1.0, 1.0),
            ],
            axis=1,
        )
        return out, dtau

    # per-channel population dispersion for the ensemble core; 0 keeps a channel a point mass, so the
    # ensemble reduces EXACTLY to the scalar `run` (the baseline-preservation guarantee). Phase-2
    # calibration overrides these so the dispersed ensemble still hits each region's 2023 TFR.
    SIGMA0 = {"C": 0.0, "rv": 0.0, "Pb": 0.0, "tau": 0.0, "S": 0.0, "N": 0.0, "q": 0.0}

    def run_ens(
        self,
        region,
        force=None,
        sigma=None,
        K=48,
        years=102,
        seed=0,
        return_dist=False,
        pb_scale=1.0,
    ):
        """The full distributional core: carry the joint state as a K-agent ensemble and aggregate
        Jensen-correctly. Each channel is spread by a Latin-hypercube marginal (deterministic, decorrelated
        across channels via seeded permutations), so `sigma`->0 reproduces the scalar `run` to machine
        precision, while a real dispersion recovers the heterogeneity the representative agent throws away
        (the bistable-N split, the coupling-trap gate, the tail selection). TFR is the population mean of
        per-agent TFR; the Leslie birth profile is the ensemble-mean of each agent's tempo-shifted profile.
        """
        chans = ["C", "rv", "Pb", "tau", "S", "N", "q"]
        if force is None:
            force = lambda yr: [0.0] * 6  # noqa: E731
        p = self.P
        start = np.array(
            [
                C0[region],
                RV0[region],
                self.PB0[region] * pb_scale,
                REAL[region][1],
                S0[region],
                NORM0[region],
                0.0,
            ]
        )
        sig = dict(self.SIGMA0)
        if sigma:
            sig.update(sigma)
        z = torch.special.ndtri(
            torch.tensor((np.arange(K) + 0.5) / K, dtype=torch.float64)
        ).numpy()
        rng = np.random.default_rng(seed)
        lims = {
            "C": (0.02, 0.999),
            "rv": (0.0, 0.6),
            "Pb": (1.0, None),
            "tau": (24, 40),
            "S": (0.05, 0.95),
            "N": (0.0, 1.0),
            "q": (-1.0, 1.0),
        }
        st = np.tile(start, (K, 1))
        for i, c in enumerate(chans):
            if sig[c] > 0:
                st[:, i] = (
                    start[i] + sig[c] * z[rng.permutation(K)]
                )  # decorrelated marginal spread
                lo, hi = lims[c]
                st[:, i] = np.clip(st[:, i], lo, hi)
        R = self.REG[region]
        nf = torch.tensor(R["pop_f"][-1].copy(), device=self.DEV)
        nmv = torch.tensor(R["pop_m"][-1].copy(), device=self.DEV)
        Sx0 = R["Sx"][-1].copy()
        srb = float(R["ind"]["SRB"][-1])
        base = R["asfr"][-1].copy()
        tfrb = base.sum()
        pop0 = float(nf.sum() + nmv.sum())
        d0 = (nf + nmv).cpu().numpy()
        dep0 = float(d0[65:].sum() / max(d0[20:65].sum(), 1))
        dep_pen = 0.0
        mem = CohortMemory(childhood=18, repro_lo=p["lagLo"], repro_hi=p["lagHi"])
        A_lag = 0.0
        Ttr, Ntr = [], []
        tfr = tfrb
        for yr in range(years):
            f = force(yr)
            fF = f[7] if len(f) > 7 else 0.0
            fScar = f[8] if len(f) > 8 else 0.0
            dtau_acc = np.zeros(K)
            for _ in range(4):
                st, dtau = self._estep_vec(region, st, f, yr / 100.0, dep_pen, A_lag)
                dtau_acc = dtau_acc + dtau
            C, rv, Pb, tau, S, N, q = (st[:, i] for i in range(7))
            tfr_i = (
                C
                * (1 - rv)
                * Pb
                * np.exp(-0.03 * np.clip(tau - 30.0, 0, None))
                * (1 - p["kBF"] * dtau_acc)
            )
            tfr = float(tfr_i.mean())
            prof = np.zeros_like(base)
            for k in range(K):
                mult = (tfr_i[k] / tfrb) if tfrb > 1e-6 else 0.0
                prof = prof + _shift_profile(base, mult, tau[k] - REAL[region][1])
            prof = prof / K
            Sx = 1 - (1 - Sx0) * (1 - 0.003) ** (yr + 1)
            nf, nmv, _b, _d = cm.leslie_step(
                nf,
                nmv,
                torch.tensor(Sx, device=self.DEV),
                torch.tensor(prof, device=self.DEV),
                srb,
                torch.tensor(0.0 * self.RC, device=self.DEV),
            )
            tot = (nf + nmv).cpu().numpy()
            dep = float(tot[65:].sum() / max(tot[20:65].sum(), 1))
            dep_pen = p["dep_fb"] * max(dep - dep0, 0)
            F = fF + p["phi"] * float(q.mean())
            env = p["wF"] * F - p["wScar"] * fScar
            mem.push(env)
            A_lag = p["gA"] * mem.reproductive_mean()
            Ttr.append(tfr)
            Ntr.append(float(N.mean()))
        out = dict(
            TFR=np.array(Ttr),
            N=np.array(Ntr),
            Nend=float(N.mean()),
            Cend=float(C.mean()),
            qend=float(q.mean()),
            Pbend=float(Pb.mean()),
            Send=float(S.mean()),
            rvend=float(rv.mean()),
            tauend=float(tau.mean()),
            tfr=tfr,
            pop_pct=(float(tot.sum()) / pop0 - 1) * 100,
        )
        if return_dist:
            out["dist_end"] = {c: st[:, i].copy() for i, c in enumerate(chans)}
        return out

    def calibrate_ens(self, sigma=None, K: int = 64):
        """Re-solve the per-region parity rescale so the dispersed ensemble baseline hits 2023 REAL TFR.

        Returns the `pb_scale` dict; regenerate `PB_SCALE_ENS` with this after any change to `sigma`/`K`.
        Pb is ~linear on TFR so the fixed-point converges in one or two steps.
        """
        sig = sigma or SIGMA_CAL
        out = {}
        for r in REAL:
            s = 1.0
            for _ in range(4):
                s *= REAL[r][0] / self.run_ens(r, sigma=sig, K=K, pb_scale=s, years=1)["tfr"]
            out[r] = float(s)
        return out

    def run_cal(
        self, region, force=None, K: int = 64, years: int = 102, return_dist: bool = False
    ):
        """The calibrated distributional core (the production run): the dispersed K-agent ensemble under
        SIGMA_CAL, re-anchored to 2023 REAL TFR by PB_SCALE_ENS. This is what all hypotheses are scored on."""
        return self.run_ens(
            region,
            force=force,
            sigma=SIGMA_CAL,
            K=K,
            years=years,
            pb_scale=PB_SCALE_ENS[region],
            return_dist=return_dist,
        )

    def baselines(self, regions=None) -> dict:
        """Baseline (no-intervention) run for each region."""
        return {r: self.run(r) for r in (regions or REAL)}

    @staticmethod
    def coupling(mag: float, start: int = 0):
        """A coupling push (security + coupling) - the shape of levers that bend fate."""
        return lambda yr: [
            1.2 * mag * ramp(yr, start),
            0.35 * mag * ramp(yr, start),
            0.0,
            0.0,
            0.0,
        ]

    @staticmethod
    def forcing(
        fS=0.0,
        fC=0.0,
        fPb=0.0,
        fTau=0.0,
        fRV=0.0,
        fN=0.0,
        fq=0.0,
        fF=0.0,
        fScar=0.0,
        mag=1.0,
        start=0,
        durable=True,
    ):
        """Build a forcing from per-channel coefficients (fN drives the norm; fq/fF/fScar the E30 memory)."""

        def fy(yr):
            s = mag * ramp(yr, start) * (1.0 if durable else erode(yr))
            return [fS * s, fC * s, fPb * s, fTau * s, fRV * s, fN * s, fq * s, fF * s, fScar * s]

        return fy

    @staticmethod
    def norm(mag: float, start: int = 0, durable: bool = True):
        """A social-norm / media push on N; negative mag is pronatal (lowers the childfree ideal)."""

        def fy(yr):
            s = mag * ramp(yr, start) * (1.0 if durable else erode(yr))
            return [0.0, 0.0, 0.0, 0.0, 0.0, s]

        return fy

    @staticmethod
    def therapy(mag: float, start: int = 0, durable: bool = True):
        """A marriageability push on q via therapy/health; durable=False reproduces the voluntary-program fade."""

        def fy(yr):
            s = mag * ramp(yr, start) * (1.0 if durable else erode(yr))
            return [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, s, 0.0, 0.0]

        return fy
