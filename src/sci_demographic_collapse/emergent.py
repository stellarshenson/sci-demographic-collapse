"""Coupled emergent behavioural model (E19/E22), extracted for reuse.

The behavioural layer models fertility as an emergent product of seven coupled, observable channels -
coupling C, childlessness rho, parity Pbar, tempo tau, economic security S, the social norm N (E25),
and marriageability q (E30) - each with its own first-order dynamics, wrapped around the calibrated
Leslie core in `coremodel`. TFR is
`quantum(C, rho, Pbar) * fec(tau) * max(1 - kBF * dtau, 0)` with a Bongaarts-Feeney period term on the
REALIZED annual change of tau (dtau = tau_t - tau_{t-1}, post-clip; the E40 audit found the earlier
substep rate-sum overstated the documented `(1 - k_BF*taudot)` by the substep count, kept a phantom
tempo term alive at the tau clips, and let the factor go negative), a soft-bistable coupling trap near
the empirical TFR-1.5 ridge, and a dependency->security feedback through the age pyramid.

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

# 2023 calibration targets (TFR, mean age at CHILDBEARING - MAC, not first birth) and channel start
# values. E41 Stage 1: MAC re-pinned to the on-disk UN WPP 2024-revision 2023 series
# (data/raw/unwpp/demographic_indicators.csv, MAC column) - the earlier values were a stale vintage
# ~0.5yr low. The MAC-vs-MAB1 fork (re-keying fec/gRV off tau_entry = MAC - Delta1_r) is registered
# as a named structural experiment (C1F6), not acted on this round.
REAL = {
    "USA": (1.62, 29.898),
    "France": (1.64, 31.58),
    # Germany: TFR from Destatis (Zensus-2022-rebased) 2023 = 1.38, not UN WPP's 1.44 - the
    # national-office convention already applied to Poland (GUS) and Korea (KOSIS). E41 Stage 0(b).
    "Germany": (1.38, 31.466),
    "Italy": (1.20, 32.309),
    "Japan": (1.21, 31.915),
    "Korea": (0.72, 33.424),
    # Poland: TFR from GUS (national office) 2023 = 1.16, not UN WPP's 1.30; MAC 29.889 from the
    # same UN WPP series the others use. GUS 2024 fell further to 1.099.
    "Poland": (1.16, 29.889),
    # Israel: the sole developed / OECD country above replacement. UN WPP 2023 TFR 2.83 (Israel CBS
    # 2.85, they agree - unlike Poland/GUS), MAC 30.867 - same UN WPP series the others use. National
    # TFR is a composition of Haredi (6.38), national-religious (3.77), traditional (2.22-2.80),
    # secular Jewish (1.98 - still the developed world's highest) and Arab (~2.9) sub-populations;
    # Israel's own replacement level is 2.08. It sits in the healthy (untrapped) basin, not collapse.
    "Israel": (2.83, 30.867),
}
# E41 Stage 1: C0 is the LIFETIME ever-in-union share (never-partnered complement at 45-49,
# cohort-matched to p0; band centrals where the source gives a band) - no longer the hand-set
# 25-39 partnership stock, which is demoted to a trend witness. Two regions are cohort-reference-
# DECOUPLED period-epoch pairs: Korea's joint cohort identity gives PB0=0.93 below the Pb floor,
# so its 2023 state is the period ever-partnering quantum (Yoo 2026, Demographic Research 54(3):
# PPEM 0.667 / tempo-adjusted PPEM* 0.698; band 0.667-0.72 incl. a ~1-2pp non-marital-union leak);
# Israel's cohort pairing is infeasible under the census-grade p0=0.068-0.070 (CBS Census 2022),
# so its period pair is retained unchanged and the cohort reference carries a declared
# non-marital/late-fertility leak (AR4). Pairing table, margins and period feasibility screen
# (PB0 >= 1.15, checked 8/8): reports/e41_stage1_anchors.json.
C0 = {
    "USA": 0.94,  # NSFG 2015-19 via NCFMR FP-23-26: ~6% never married nor cohabited at 40-44
    "France": 0.91,  # INSEE-INED EPIC 2013-14: ever-cohabited 0.90-0.92, gens 1968-77
    "Germany": 0.905,  # Eurostat census 2021 ever-married 0.8133 + cohabitation -> 0.88-0.93
    "Italy": 0.825,  # Eurostat census 2021 ever-married 0.7698 + libere unioni -> 0.80-0.85
    "Japan": 0.835,  # 2020 census ever-married at 50 = 0.8219 (de-facto incl.) -> 0.82-0.85
    "Korea": 0.70,  # period-epoch pair: PPEM/PPEM* 2023 (Yoo 2026 DR 54(3)); band 0.667-0.72
    "Poland": 0.91,  # Eurostat census 2021 (GUS NSP) ever-married 0.8885 + cohabitation -> 0.90-0.92
    "Israel": 0.97,  # period-epoch pair retained (cohort reference decoupled, AR4); familism well
}
# E41 Stage 1: RV0 = 1 - (1-p0)/C0, within-union permanent childlessness derived JOINTLY with C0
# from cohort-MATCHED {p0, ever-in-union} - no longer hand-set. Feasibility margins recorded 8/8
# BEFORE the derivation (no negative RV0); IL/PL/FR/USA carry a ~1-2pp non-marital-fertility leak
# making RV0 a lower bound. Korea/Israel are period-epoch pairs (see C0).
RV0 = {
    "USA": 0.112,  # p0=0.165 (CPS 2022, cohorts ~1972-77)
    "France": 0.055,  # p0=0.14 (INSEE EFL, b.~1970)
    "Germany": 0.116,  # p0=0.20 (Mikrozensus, b.1969-73)
    "Italy": 0.067,  # p0=0.23 (ISTAT, b.1975)
    "Japan": 0.126,  # p0=0.27 (IPSS/census, b.~1970)
    "Korea": 0.09,  # RV_ref = 1-(1-0.156)/EIU, KOSIS 2020 census b.1971-75; band 0.065-0.09 (AR5)
    "Poland": 0.091,  # p0 = late-window central 0.1725 of the 0.15-0.195 bracket (C0F4)
    "Israel": 0.05,  # period-epoch retained; cohort p0=0.068-0.070 infeasible vs EIU 0.89-0.92 (AR4)
}
# E41 Stage 1(6): S0 is a GAUGE, not a fit - only S-S0 deviations enter the dynamics (S starts at
# S0 and relaxes to S0 - dep_pen + fS), so these values carry no baseline dynamical content. They
# are operationalised documentarily against young-adult parental co-residence 25-34 (2023: USA 0.18,
# FR 0.16, DE 0.13, IT 0.51, JP 0.38, KR 0.55, PL 0.53, IL 0.32 - Eurostat ilc_lvps08 / national
# offices): S0 rank-orders inversely with co-residence. Values unchanged this round.
S0 = {
    "USA": 0.58,
    "France": 0.62,
    "Germany": 0.52,
    "Italy": 0.45,
    "Japan": 0.45,
    "Korea": 0.40,
    "Poland": 0.45,
    "Israel": 0.58,  # strong familial/kin support offsets high cost of living
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
    "Israel": 0.14,  # pronatal familism -> childfree ideal in the low well (untrapped basin)
}

# ensemble calibration (Phase 2, the distributional core). SIGMA_CAL is the grounded, structural
# population-heterogeneity spread per channel (age-at-first-birth SD ~3yr; parity intentions spread widest;
# norm/security/marriageability moderate; coupling/childlessness tight) - these are NOT fit parameters.
# PB_SCALE_ENS is the one calibration free parameter re-solved per region so the DISPERSED baseline still
# reproduces the 2023 REAL TFR (Pb is how the scalar PB0 was calibrated too). Regenerate via calibrate_ens().
SIGMA_CAL = {"C": 0.05, "rv": 0.03, "Pb": 0.15, "tau": 3.0, "S": 0.10, "N": 0.06, "q": 0.10}
PB_SCALE_ENS = {
    # re-solved by calibrate_ens on the E41 Stage-1 anchors (data-derived C0/RV0, re-pinned MAC,
    # Destatis Germany 1.38); dispersed baselines reproduce 2023 REAL to <5e-4 for 8/8
    # (reports/e41_stage2_calibration.json). USA's |s-1| grew +0.0128 over E40's 1.0267: +0.0118 at
    # the Stage-2 anchors (of which +0.0084 from the MAC re-pin alone - 29.4 -> 29.898 crosses the
    # fec knee at 30 under sigma_tau=3.0, an attributed Jensen effect recorded as a named deviation
    # there) plus +0.0010 from the Stage-4 kBF move (post_kbf_move in the same report).
    "USA": 1.0395,
    "France": 1.0233,
    "Germany": 1.0232,
    "Italy": 1.0163,
    "Japan": 1.0188,
    "Korea": 1.0088,
    "Poland": 1.0349,  # dispersed baseline reproduces GUS TFR 1.16 exactly
    "Israel": 1.0404,  # dispersed baseline reproduces UN WPP TFR 2.83 exactly
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
    # Bongaarts & Feeney 1998 ("On the quantum and tempo of fertility", PDR 24(2)): the tempo
    # adjustment TFR/(1 - r) with r the annual change in mean age at childbearing, applied on the
    # REALIZED annual dtau (E40). E41 Stage-4 gate: adjudicated on GAP dynamics G = 1-TFR/adjTFR
    # against the delivered adjTFR series (grid {0.4,0.6,0.8,1.0}), argmin 1.0 beats the former
    # 0.6 by 37.8 chi2 (>4 bar) - the damped value underexplained every observed tempo gap
    # (systematic residual sign -0.86, logged as a scope finding: even 1.0 underexplains). 1.0 is
    # the canonical undamped B-F factor. The E40-A4g sweep note ({0.4,0.6,0.8}, no verdict rode on
    # the choice) is superseded by this data-adjudicated value (reports/e41_backtest_results.json).
    kBF=1.0,
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
    wS=0.3,  # DEAD (E41 Stage 0(e)): defined but never referenced by any dynamics; kept in place
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


# E41 observability harness: the per-year series collected when run()/run_ens() are called with
# trajectories=True. Purely additive - collection never feeds back into the dynamics, so baselines
# are bit-for-bit identical with the harness off vs on (guarded in tests).
_TRAJ_KEYS = (
    "C",
    "rv",
    "Pb",
    "tau",
    "S",
    "N",
    "q",
    "quantum",
    "fec",
    "tempo_factor",
    "dtau",
    "adjTFR_model",
    "TFR",
    "births",
    "deaths",
    "pop_total",
    "dependency",
    "dep_pen",
)


def _traj_append(traj: dict, **vals) -> None:
    """Append one year of observables to a harness dict (floats only, no tensors)."""
    for k in _TRAJ_KEYS:
        traj[k].append(float(vals[k]))


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
        # returns (new_state, dtau_rate); the rate is DIAGNOSTIC only since E40 - the TFR
        # observable uses the realized annual change of tau, never a sum of substep rates
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

    def run(self, region: str, force=None, years: int = 102, trajectories: bool = False) -> dict:
        """Integrate `region` forward `years` from 2023 under an optional forcing function.

        `force` maps a year index to `[fS, fC, fPbar, ftau, frho]`; None means the baseline.
        Returns dict with the TFR and C trajectories, end states, and percent population change.

        `trajectories=True` (E41 observability harness, additive - existing keys unchanged)
        attaches a `trajectories` dict of per-year series: the 7 channel states, the TFR
        decomposition (quantum / fec / tempo factor / dtau / model-adjTFR = quantum*fec),
        and the Leslie observables the loop already computes but previously discarded
        (births, deaths, total population, dependency ratio, dep_pen).
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
        traj = (
            {k: [] for k in _TRAJ_KEYS} if trajectories else None
        )  # E41 harness (off by default)
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
            tau_prev = st[3]
            for _ in range(4):
                st, _ = self._estep(region, st, f, yr / 100.0, dep_pen, A_lag)
            C, rv, Pb, tau, S, N, q = st
            # realized annual tempo change (post-clip) - the documented B-F rate (E40 fix)
            dtau = tau - tau_prev
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
            qv = quantum(C, rv, Pb)
            fv = fec(tau)
            tp = max(1 - p["kBF"] * dtau, 0.0)
            tfr = qv * fv * tp
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
            if traj is not None:
                _traj_append(
                    traj,
                    C=C,
                    rv=rv,
                    Pb=Pb,
                    tau=tau,
                    S=S,
                    N=N,
                    q=q,
                    quantum=qv,
                    fec=fv,
                    tempo_factor=tp,
                    dtau=dtau,
                    adjTFR_model=qv * fv,
                    TFR=tfr,
                    births=float(_b),
                    deaths=float(_d),
                    pop_total=float(tot.sum()),
                    dependency=dep,
                    dep_pen=dep_pen,
                )
        out = dict(
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
        if traj is not None:
            out["trajectories"] = {k: np.array(v) for k, v in traj.items()}
        return out

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
            tau_prev = tau
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
            # realized annual tempo change (post-clip) - the documented B-F rate (E40 fix)
            tfr = quantum(C, rv, Pb) * fec(tau) * max(1 - p["kBF"] * (tau - tau_prev), 0.0)
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
        trajectories=False,
    ):
        """The full distributional core: carry the joint state as a K-agent ensemble and aggregate
        Jensen-correctly. Each channel is spread by a Latin-hypercube marginal (deterministic, decorrelated
        across channels via seeded permutations), so `sigma`->0 reproduces the scalar `run` to machine
        precision, while a real dispersion recovers the heterogeneity the representative agent throws away
        (the bistable-N split, the coupling-trap gate, the tail selection). TFR is the population mean of
        per-agent TFR; the Leslie birth profile is the ensemble-mean of each agent's tempo-shifted profile.

        `trajectories=True` (E41 harness, additive) attaches per-year ensemble-mean series: channel
        states, the Jensen-honest TFR decomposition (means of the per-agent quantum / fec / tempo
        factor / dtau; adjTFR_model = mean of per-agent quantum*fec), and the Leslie observables.
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
        traj = {k: [] for k in _TRAJ_KEYS} if trajectories else None  # E41 harness
        tfr = tfrb
        for yr in range(years):
            f = force(yr)
            fF = f[7] if len(f) > 7 else 0.0
            fScar = f[8] if len(f) > 8 else 0.0
            tau_prev = st[:, 3].copy()
            for _ in range(4):
                st, _ = self._estep_vec(region, st, f, yr / 100.0, dep_pen, A_lag)
            C, rv, Pb, tau, S, N, q = (st[:, i] for i in range(7))
            # realized annual tempo change per agent (post-clip) - the documented B-F rate (E40 fix).
            # The factor is floored at 0; above 1 (advancing births) is genuine Bongaarts-Feeney and
            # bounded by the dynamics: |dtau| <= kTau * (tau range) ~ 0.96/yr, so factor <= ~1.6
            qv_i = C * (1 - rv) * Pb
            fv_i = np.exp(-0.03 * np.clip(tau - 30.0, 0, None))
            tp_i = np.clip(1 - p["kBF"] * (tau - tau_prev), 0.0, None)
            tfr_i = qv_i * fv_i * tp_i
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
            if traj is not None:
                _traj_append(
                    traj,
                    C=C.mean(),
                    rv=rv.mean(),
                    Pb=Pb.mean(),
                    tau=tau.mean(),
                    S=S.mean(),
                    N=N.mean(),
                    q=q.mean(),
                    quantum=qv_i.mean(),
                    fec=fv_i.mean(),
                    tempo_factor=tp_i.mean(),
                    dtau=(tau - tau_prev).mean(),
                    adjTFR_model=(qv_i * fv_i).mean(),
                    TFR=tfr,
                    births=float(_b),
                    deaths=float(_d),
                    pop_total=float(tot.sum()),
                    dependency=dep,
                    dep_pen=dep_pen,
                )
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
        if traj is not None:
            out["trajectories"] = {k: np.array(v) for k, v in traj.items()}
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
        self,
        region,
        force=None,
        K: int = 64,
        years: int = 102,
        return_dist: bool = False,
        trajectories: bool = False,
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
            trajectories=trajectories,
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
