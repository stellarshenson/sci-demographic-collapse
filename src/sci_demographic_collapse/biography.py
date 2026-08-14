"""Cohort biography reader (task 70) - narrate one birth-cohort's life-course from the model's own state.

Read-only over `EmergentModel`. Given a region and a birth-cohort year, this follows that cohort down its
Lexis life-line and reports the environment it actually passed through, grounded entirely in the numbers the
coupled model produced - nothing invented. It reuses `EmergentModel.run` (the per-calendar-year trajectories)
and `ot.CohortMemory` (the Lagrangian childhood path-integral); it does NOT re-derive any dynamics.

What the model exposes at cohort resolution vs what it only aggregates:
- Per calendar year (hence sliceable onto a cohort's window): coupling C, norm N, marriageability q, and TFR.
  `run` records exactly these four as year-by-year arrays (index i == calendar year 2023 + i, 102 yrs to 2124).
- Only as end-of-run (2124) scalars, NOT per year: tempo tau, parity Pbar, childlessness rho, security S.
  The reader is honest about this - it narrates them only when the cohort's reproductive window reaches the
  final year, otherwise it states the model does not retain them per cohort.

    m = EmergentModel(data_dir="data/raw/unwpp")
    rec = cohort_biography(m, "Korea", 2000)
    print(rec["narration"])
"""

from __future__ import annotations

import numpy as np

from .emergent import C0, NORM0, REAL
from .ot import CohortMemory

SIM_Y0 = 2023  # run() integrates forward from the 2023 calibration; array index i == year 2023 + i
SIM_YEARS = 102  # ... to 2124
CHILDHOOD = 18  # ot.CohortMemory default used inside run(): childhood ages 0..17


def _window_stats(traj: np.ndarray, y_lo: int, y_hi: int) -> dict | None:
    """Mean / first / last / min / max of a per-year trajectory over calendar years [y_lo, y_hi] inclusive.

    Only years inside the simulation window [2023, 2124] contribute; `coverage` is the fraction of the
    requested window that the simulation actually spans. Returns None if the window misses the sim entirely.
    """
    idx = [y - SIM_Y0 for y in range(y_lo, y_hi + 1)]
    valid = [i for i in idx if 0 <= i < len(traj)]
    if not valid:
        return None
    seg = np.asarray([traj[i] for i in valid], dtype=float)
    return {
        "mean": float(seg.mean()),
        "first": float(seg[0]),
        "last": float(seg[-1]),
        "min": float(seg.min()),
        "max": float(seg.max()),
        "coverage": len(valid) / len(idx),
        "y_lo": y_lo,
        "y_hi": y_hi,
    }


def _childhood_coupling_integral(c_traj: np.ndarray, region: str, birth_year: int) -> dict:
    """The cohort's childhood path-integral of the coupling deviation, via `ot.CohortMemory` itself.

    This is the model's own Lagrangian object, used to extract a SINGLE cohort's completed childhood integral
    J(b): setting the reproductive window to a single age (repro_lo == repro_hi == CHILDHOOD) leaves exactly the
    target cohort in `reproductive_mean()` at time t = birth_index + CHILDHOOD. The integrated signal is the
    coupling deviation C(year) - C0(region), so the number reads as "the partnership climate this cohort grew up
    in, relative to today". Pre-2023 childhood years are counted as zero deviation by CohortMemory (b < 0 branch).
    """
    env = np.asarray(c_traj, dtype=float) - C0[region]
    bi = birth_year - SIM_Y0
    t = bi + CHILDHOOD
    child_years = range(birth_year, birth_year + CHILDHOOD)
    covered = sum(0 <= (y - SIM_Y0) < len(env) for y in child_years)
    coverage = covered / CHILDHOOD
    if t < 0 or t >= len(env):
        return {"value": None, "coverage": coverage}
    mem = CohortMemory(childhood=CHILDHOOD, repro_lo=CHILDHOOD, repro_hi=CHILDHOOD)
    for e in env[: t + 1]:
        mem.push(e)
    return {"value": float(mem.reproductive_mean()), "coverage": coverage}


def cohort_biography(model, region: str, birth_year: int, force=None) -> dict:
    """Narrate the life-course of the `birth_year` cohort in `region`, grounded in the model's trajectory.

    Runs `model.run(region, force)` once and reads the per-year C / N / q / TFR arrays over this cohort's
    childhood (ages 0-17) and reproductive (ages 27-45) calendar windows. Returns a structured record plus a
    plain-language `narration` in which every claim traces to one of those numbers. `force` is passed straight
    through to `run`, so a cohort's story can be told under baseline or under any intervention forcing.
    """
    if region not in REAL:
        raise ValueError(f"unknown region {region!r}; known: {sorted(REAL)}")
    repro_lo, repro_hi = (
        model.P["lagLo"],
        model.P["lagHi"],
    )  # 27..45, the model's reproductive-age window
    c_thr, th_n = model.P["C_thr"], model.P["thN"]

    res = model.run(region, force)
    ry_lo, ry_hi = birth_year + repro_lo, birth_year + repro_hi
    cy_lo, cy_hi = birth_year, birth_year + CHILDHOOD - 1

    repro = {ch: _window_stats(res[ch], ry_lo, ry_hi) for ch in ("C", "N", "q", "TFR")}
    child = {ch: _window_stats(res[ch], cy_lo, cy_hi) for ch in ("C", "N", "q")}
    child_integral = _childhood_coupling_integral(res["C"], region, birth_year)

    # end-of-run scalars are only meaningful for this cohort if its reproductive window reaches the final year
    reaches_end = ry_hi >= SIM_Y0 + SIM_YEARS - 1
    end_scalars = {
        "tau": res["tauend"],
        "Pbar": res["Pbend"],
        "rho": res["rvend"],
        "S": res["Send"],
    }

    record = {
        "region": region,
        "birth_year": birth_year,
        "reproductive_window": (ry_lo, ry_hi),
        "childhood_window": (cy_lo, cy_hi),
        "anchors": {
            "C0": C0[region],
            "NORM0": NORM0[region],
            "C_thr": c_thr,
            "thN": th_n,
            "replacement": 2.1,
            "ridge": 1.5,
        },
        "reproductive": repro,
        "childhood": child,
        "childhood_coupling_integral": child_integral,
        "end_scalars": end_scalars if reaches_end else None,
        "exposed": ["C (coupling)", "N (norm)", "q (marriageability)", "TFR"],
        "aggregated_only": ["tau (tempo)", "Pbar (parity)", "rho (childlessness)", "S (security)"],
    }
    record["narration"] = _narrate(record)
    return record


def _narrate(r: dict) -> str:
    """Plain-language narration; every sentence carries a model number and its interpretation."""
    reg, b = r["region"], r["birth_year"]
    a = r["anchors"]
    rep = r["reproductive"]
    ry_lo, ry_hi = r["reproductive_window"]
    lines: list[str] = []
    lines.append(
        f"The {reg} cohort born in {b}. Its childhood (ages 0-17) spanned {r['childhood_window'][0]}-"
        f"{r['childhood_window'][1]}; its reproductive years (ages 27-45) spanned {ry_lo}-{ry_hi}. "
        f"The model runs {SIM_Y0}-{SIM_Y0 + SIM_YEARS - 1}, so only the part of each window inside that "
        f"span is read from the model."
    )

    ci = r["childhood_coupling_integral"]
    if ci["value"] is not None:
        sign = "above" if ci["value"] >= 0 else "below"
        lines.append(
            f"Childhood partnership climate (the CohortMemory path-integral of coupling relative to today's "
            f"C0={a['C0']:.2f}): {ci['value']:+.3f}, i.e. this cohort grew up in a coupling environment "
            f"{sign} the 2023 baseline (childhood coverage {ci['coverage'] * 100:.0f}%)."
        )
    else:
        lines.append(
            f"Its childhood fell largely outside the {SIM_Y0}-{SIM_Y0 + SIM_YEARS - 1} window "
            f"(coverage {ci['coverage'] * 100:.0f}%), so the model carries no coupling memory for it."
        )

    if rep["C"] is not None:
        c = rep["C"]
        trap = "below" if c["mean"] < a["C_thr"] else "above"
        lines.append(
            f"During its reproductive years the coupling channel C averaged {c['mean']:.3f} "
            f"(from {c['first']:.3f} to {c['last']:.3f}), {trap} the C_thr={a['C_thr']:.2f} coupling-trap ridge "
            f"and {'below' if c['mean'] < a['C0'] else 'above'} today's C0={a['C0']:.2f} - "
            f"{'weak, trap-side partnership formation' if c['mean'] < a['C_thr'] else 'partnership formation held above the trap'}. "
            f"(window coverage {c['coverage'] * 100:.0f}%)"
        )
    if rep["N"] is not None:
        n = rep["N"]
        well = "the trapped childfree-ideal well" if n["mean"] > a["thN"] else "the untrapped well"
        lines.append(
            f"The norm climate N averaged {n['mean']:.3f} against the tipping point thN={a['thN']:.2f} and "
            f"today's N0={a['NORM0']:.2f} - {reg}'s reproductive cohort sat in {well}."
        )
    if rep["q"] is not None:
        q = rep["q"]
        lines.append(
            f"Marriageability capital q averaged {q['mean']:+.3f} (deviation from 0; "
            f"{'eroded' if q['mean'] < 0 else 'intact/lifted'} relative to the calibrated baseline)."
        )
    if rep["TFR"] is not None:
        t = rep["TFR"]
        rel = "sub-replacement" if t["mean"] < a["replacement"] else "at/above replacement"
        ridge = "below the 1.5 collapse ridge" if t["mean"] < a["ridge"] else "above the 1.5 ridge"
        lines.append(
            f"Fertility contributed: the period TFR over its childbearing years averaged {t['mean']:.3f} "
            f"(from {t['first']:.3f} to {t['last']:.3f}) - {rel} and {ridge}. This is the PERIOD rate at those "
            f"calendar years, a proxy for the cohort's realised fertility; the model is period-based and does "
            f"not carry a completed cohort parity per birth-cohort."
        )

    es = r["end_scalars"]
    if es is not None:
        lines.append(
            f"Because this cohort's reproductive window reaches the final simulated year, its end-of-run "
            f"aggregate state is meaningful: mean age at first birth tau={es['tau']:.1f}, parity Pbar="
            f"{es['Pbar']:.2f}, childlessness rho={es['rho']:.3f}, security S={es['S']:.2f}."
        )
    else:
        lines.append(
            "Tempo (tau), parity (Pbar), childlessness (rho) and security (S) are exposed by the model only as "
            "end-of-run (2124) scalars, not per calendar year, so they cannot be attributed to this cohort at "
            "cohort resolution - the reader deliberately does not invent them."
        )
    return "\n".join(lines)


if __name__ == "__main__":  # smoke test
    from .emergent import EmergentModel

    m = EmergentModel(data_dir="data/raw/unwpp")
    for reg, yr in [("Korea", 2000), ("France", 2000)]:
        rec = cohort_biography(m, reg, yr)
        print(f"\n=== {reg} {yr} ===")
        print(rec["narration"])
