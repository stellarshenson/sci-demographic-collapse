"""Age-structured cohort-component (Leslie) core for the demographic-collapse SOTA model.

Factored from the validated Notebook 3 core so calibration / crisis / intervention notebooks reuse one
implementation. Driven by UN WPP 2024 single-year data in ``data/raw/unwpp/``.

State: female/male age vectors ``Nᶠ, Nᵐ ∈ ℝ¹⁰¹`` (single-year buckets 0..100+, thousands).
One annual step is the Leslie map - survival subdiagonal ``Sx`` (survival into age a) plus a fertility
renewal row (per-woman ASFR × female share of births × birth survival ``Sx[0]``).

Import AFTER setting ``CUDA_VISIBLE_DEVICES`` (this module imports torch at load).
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import polars as pl
import torch

# UN WPP location codes
REGIONS = {"USA": 840, "China": 156, "Japan": 392, "Korea": 410,
           "Italy": 380, "Germany": 276, "Spain": 724, "France": 250,
           "Poland": 616, "Europe": 908}
NA = 101                      # single-year buckets 0..100+ (100 is the open interval)
AGES = np.arange(0, NA)
FERT_LO, FERT_HI = 15, 49     # ASFR support
DEV = torch.device("cuda" if torch.cuda.is_available() else "cpu")

_IND_COLS = ["Time", "TFR", "MAC", "Births", "Deaths", "NatChange", "PopChange",
             "SRB", "CBR", "CDR", "TPopulation1Jan", "LEx", "MedianAgePop"]


def mape(model, obs) -> float:
    """Mean absolute percentage error over non-zero observed entries."""
    obs = np.asarray(obs, float); model = np.asarray(model, float)
    m = np.abs(obs) > 1e-9
    return float(np.mean(np.abs((model[m] - obs[m]) / obs[m])) * 100)


def _grid(df, loc, value, y0, y1, amax=100):
    """Dense ``[year, age]`` array over ``y0..y1``, ages ``0..amax`` (amax absorbs the open interval)."""
    out = np.zeros((y1 - y0 + 1, amax + 1))
    sub = df.filter((pl.col("LocID") == loc) & (pl.col("Time") >= y0) & (pl.col("Time") <= y1))
    for t, a, v in sub.select(["Time", "AgeGrpStart", value]).iter_rows():
        if v is not None:
            out[int(t) - y0, min(int(a), amax)] += float(v)
    return out


def load_unwpp(data_dir="data/raw/unwpp", y0=1990, y1=2023, regions=None, varid=2):
    """Load UN WPP 2024 subsets into ``{region: {pop_f,pop_m,Sx,asfr,ind,years}}`` (Medium variant)."""
    data_dir = Path(data_dir)
    regions = regions or REGIONS

    def _load(name):
        return pl.read_csv(data_dir / f"{name}.csv", infer_schema_length=5000).filter(pl.col("VarID") == varid)

    pop, life, fert, ind = _load("population_by_age1"), _load("life_table_both"), \
        _load("fertility_by_age1"), _load("demographic_indicators")
    out = {}
    for name, loc in regions.items():
        di = ind.filter((pl.col("LocID") == loc) & (pl.col("Time") >= y0) & (pl.col("Time") <= y1)).sort("Time")
        out[name] = dict(
            years=np.arange(y0, y1 + 1),
            pop_f=_grid(pop, loc, "PopFemale", y0, y1),
            pop_m=_grid(pop, loc, "PopMale", y0, y1),
            Sx=_grid(life, loc, "Sx", y0, y1),
            asfr=_grid(fert, loc, "ASFR", y0, y1) / 1000.0,          # per-1000 women -> per woman
            ind={c: di[c].to_numpy() for c in _IND_COLS if c in di.columns},
        )
    return out


def leslie_step(nf, nm, Sx, asfr, srb, mig=None):
    """One annual cohort-component step (torch). nf,nm,Sx,asfr: [101]; srb scalar.

    mig: optional [101] net migrants (thousands) added after natural change, split 50/50 by sex.
    Returns nf', nm', births, deaths.
    """
    births = torch.sum(asfr * nf)
    phi = 100.0 / (100.0 + srb)                     # female share of births
    S0 = Sx[0]
    nf_s = torch.zeros_like(nf); nm_s = torch.zeros_like(nm)
    nf_s[1:100] = nf[0:99] * Sx[1:100]; nm_s[1:100] = nm[0:99] * Sx[1:100]
    nf_s[100] = nf[99] * Sx[100] + nf[100] * Sx[100]
    nm_s[100] = nm[99] * Sx[100] + nm[100] * Sx[100]
    nf_s[0] = births * phi * S0
    nm_s[0] = births * (1.0 - phi) * S0
    deaths = (torch.sum(nf) + torch.sum(nm)) + births - (torch.sum(nf_s) + torch.sum(nm_s))
    if mig is not None:
        nf_s = nf_s + 0.5 * mig; nm_s = nm_s + 0.5 * mig
    return nf_s, nm_s, births, deaths


def project(region, mig_schedule=None, asfr_override=None, sx_override=None, dev=DEV):
    """March a region over its window. mig_schedule/asfr_override/sx_override: callables of year index k.

    asfr_override(k) -> [101] per-woman ASFR; sx_override(k) -> [101] survival-into-age (defaults: observed).
    Returns total/births/deaths/pyramids.
    """
    R = region
    t = lambda x: torch.tensor(x, dtype=torch.float64, device=dev)
    nf = t(R["pop_f"][0].copy()); nm = t(R["pop_m"][0].copy())
    n = len(R["years"])
    tot = np.zeros(n); bir = np.zeros(n); dea = np.zeros(n)
    pyr_f = np.zeros((n, NA)); pyr_m = np.zeros((n, NA))
    for k in range(n):
        tot[k] = float(torch.sum(nf) + torch.sum(nm))
        pyr_f[k] = nf.cpu().numpy(); pyr_m[k] = nm.cpu().numpy()
        if k == n - 1:
            break
        asfr = t(asfr_override(k) if asfr_override is not None else R["asfr"][k])
        Sx = t(sx_override(k) if sx_override is not None else R["Sx"][k])
        mig = t(mig_schedule(k)) if mig_schedule is not None else None
        nf, nm, b, d = leslie_step(nf, nm, Sx, asfr, float(R["ind"]["SRB"][k]), mig)
        bir[k] = float(b); dea[k] = float(d)
    return dict(total=tot, births=bir, deaths=dea, pyr_f=pyr_f, pyr_m=pyr_m)


def onestep_fidelity(region, dev=DEV):
    """Apply one Leslie step to the OBSERVED pyramid each year -> births, deaths (operator fidelity)."""
    R = region; n = len(R["years"]) - 1
    bb = np.zeros(n); dd = np.zeros(n)
    t = lambda x: torch.tensor(x, dtype=torch.float64, device=dev)
    for k in range(n):
        _, _, b, d = leslie_step(t(R["pop_f"][k].copy()), t(R["pop_m"][k].copy()),
                                 t(R["Sx"][k]), t(R["asfr"][k]), float(R["ind"]["SRB"][k]))
        bb[k] = float(b); dd[k] = float(d)
    return bb, dd


def build_leslie(asfr_pw, Sx, srb):
    """101x101 female-dominant Leslie matrix from per-woman ASFR and survival-into-age Sx."""
    L = np.zeros((NA, NA))
    phi = 100.0 / (100.0 + srb); S0 = Sx[0]
    for a in range(1, 100):
        L[a, a - 1] = Sx[a]
    L[100, 99] = Sx[100]; L[100, 100] = Sx[100]
    L[0, :] = asfr_pw * phi * S0
    return L


def nrr(asfr_pw, Sx, srb):
    """Net reproduction rate = expected daughters per newborn girl."""
    phi = 100.0 / (100.0 + srb)
    lx = np.ones(NA); lx[0] = Sx[0]
    for a in range(1, NA):
        lx[a] = lx[a - 1] * Sx[a]
    return float(np.sum(asfr_pw * phi * lx))


def keyfitz_momentum(region, k, dev=DEV, iters=800):
    """Keyfitz momentum: rescale ASFR to NRR=1, project to stationarity, ratio final/current."""
    R = region
    asfr = R["asfr"][k].copy(); Sx = R["Sx"][k].copy(); srb = float(R["ind"]["SRB"][k])
    r0 = nrr(asfr, Sx, srb)
    L = torch.tensor(build_leslie(asfr / r0, Sx, srb), dtype=torch.float64, device=dev)
    nf = torch.tensor(R["pop_f"][k].copy(), dtype=torch.float64, device=dev)
    p0 = float(torch.sum(nf))
    for _ in range(iters):
        nf = L @ nf
    return float(torch.sum(nf)) / p0, r0


def leslie_spectrum(region, k):
    """Dominant eigenvalue λ₁ (intrinsic growth), stable age distribution, full spectrum."""
    L = build_leslie(region["asfr"][k], region["Sx"][k], float(region["ind"]["SRB"][k]))
    ev, evec = np.linalg.eig(L)
    i = int(np.argmax(ev.real))
    w = np.abs(evec[:, i].real); w = w / w.sum()
    return float(ev[i].real), w, ev


def rogers_castro(ages=AGES, a1=0.02, alpha1=0.10, a2=0.06, mu2=22.0, lam2=0.40, alpha2=0.18):
    """Rogers-Castro net-migration age schedule (childhood echo + labour-force peak), normalized to sum 1."""
    a = ages.astype(float)
    child = a1 * np.exp(-alpha1 * a)
    labour = a2 * np.exp(-alpha2 * (a - mu2) - np.exp(-lam2 * (a - mu2)))
    m = child + labour
    m[m < 0] = 0
    return m / m.sum()
