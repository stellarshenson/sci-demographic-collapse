"""Hypothesis-guard regression tests.

Each test pins a verdict-bearing number or ordering from the recorded campaign
(docs/experiments/demographic-collapse-experiments.md) to the calibrated core as
corrected by E40. A failure is a SIGNAL that a core change moved a recorded result:
the test name and docstring say which round/hypothesis to revisit - do not silently
widen a band; either the change is a bug or the affected round needs re-judging.

All runs are deterministic (production seed 0, K=64), so orderings are asserted
exactly and magnitudes get bands around the NB36-measured post-E40 values.
"""

import json
from pathlib import Path

import numpy as np
import pytest

import sci_demographic_collapse.emergent as E
from sci_demographic_collapse.emergent import PARAMS, PB_SCALE_ENS, REAL, EmergentModel, ramp
from sci_demographic_collapse.interventions import CATALOGUE, CHANNELS, force_of

PROJ = Path(__file__).resolve().parents[1]
REGIONS8 = ["USA", "France", "Germany", "Italy", "Japan", "Korea", "Poland", "Israel"]


def f9(fS=0.0, fC=0.0, fPb=0.0, fTau=0.0, fq=0.0, d=10):
    """The campaign's 9-channel forcing with the standard 10-year ramp (NB36 convention)."""

    def fy(yr):
        s = ramp(yr, d=d)
        return [fS * s, fC * s, fPb * s, fTau * s, 0, 0, fq * s, 0, 0]

    return fy


@pytest.fixture(scope="module")
def model():
    return EmergentModel(data_dir=str(PROJ / "data" / "raw" / "unwpp"))


@pytest.fixture(scope="module")
def baselines(model):
    """Calibrated century baselines, computed once (seed 0, K=64)."""
    return {r: model.run_cal(r) for r in REGIONS8}


def test_guard_calibration_anchor(model):
    """E12/E40-A3: run_cal year-1 TFR reproduces 2023 REAL for all 8 regions (<5e-4).

    On failure: the calibration is broken - re-solve PB_SCALE_ENS via calibrate_ens
    and re-verify the E40-A3 record before trusting any hypothesis run.
    """
    for r in REGIONS8:
        tfr1 = model.run_cal(r, years=1)["tfr"]
        assert abs(tfr1 - REAL[r][0]) < 5e-4, f"{r}: {tfr1:.4f} vs REAL {REAL[r][0]:.4f}"


def test_guard_kbf_documented_value():
    """E40: kBF is the documented Bongaarts-Feeney 0.6 on the REALIZED annual dtau.

    On failure: the tempo constant was retuned - the E40 section's kBF paragraph and
    the A4g sensitivity band must be re-run and re-documented.
    """
    assert PARAMS["kBF"] == 0.6


def test_guard_collapse_ordering(baselines):
    """E19/E40-A3: Korea is the acute collapse (minimum endpoint, no spontaneous
    recovery); Israel stays the above-replacement outlier (maximum endpoint).

    On failure: the baseline regime moved - re-judge every basin/fate claim
    (Seldon manifold, E14 reversibility, E19 classifications).
    """
    end = {r: baselines[r]["tfr"] for r in REGIONS8}
    assert min(end, key=end.get) == "Korea"
    assert max(end, key=end.get) == "Israel"
    assert end["Korea"] < 0.7, f"Korea endpoint {end['Korea']:.3f}"
    assert end["Israel"] > 1.8, f"Israel endpoint {end['Israel']:.3f}"
    assert end["Korea"] < REAL["Korea"][0], "Korea must not spontaneously recover"


def test_guard_e19_tempo_mirage_amplitude(model, baselines):
    """E19 (superseded amplitudes -> E40-A4a): the Korea fTau=-3 tempo bump peaks in
    the post-fix band [0.03, 0.15] (measured +0.071). The legacy 4x rate-sum gave
    +0.236 - a value outside this band means the tempo term regressed.

    On failure: re-run NB36 A1/A4a; every timing-lever transient is suspect.
    """
    d = model.run_cal("Korea", force=f9(fTau=-3.0))["TFR"] - baselines["Korea"]["TFR"]
    peak = float(d[np.abs(d[:40]).argmax()])
    assert 0.03 < peak < 0.15, f"tempo bump peak {peak:+.3f} outside the post-E40 band"


def test_guard_e19_transience_ordering(model, baselines):
    """E19/E40-A4b: tempo is the most transient channel - its end/peak persistence is
    below the coupling crown's in Korea and Germany.

    On failure: the mirage-vs-durable separation collapsed - re-judge the E19
    classifications and every lever ranked by durability.
    """
    arch = {
        "tempo": f9(fTau=-3.0),
        "crown": f9(fC=0.35 * 0.22, fS=0.3 * 0.22),
    }
    for reg in ["Korea", "Germany"]:
        pers = {}
        for name, f in arch.items():
            d = model.run_cal(reg, force=f)["TFR"] - baselines[reg]["TFR"]
            peak = abs(d[np.abs(d[:40]).argmax()])
            pers[name] = abs(d[-1]) / max(peak, 1e-12)
        assert pers["tempo"] < pers["crown"], f"{reg}: {pers}"


def test_guard_e15_coupling_dominance_over_cash_korea(model, baselines):
    """E15/E19 (coupling keystone, cash mirage): on Korea - where coupling has
    collapsed - the coupling crown's century endpoint beats equal-convention cash
    (quantum is gated without coupling).

    On failure: the campaign's central verdict is moving - re-judge E15-H51..H100
    and the E19 quantum-needs-coupling gate.
    """
    dcrown = model.run_cal("Korea", force=f9(fC=0.35 * 0.22, fS=0.3 * 0.22))["tfr"]
    dcash = model.run_cal("Korea", force=f9(fPb=0.10))["tfr"]
    base = baselines["Korea"]["tfr"]
    assert dcrown - base > dcash - base, (
        f"crown {dcrown - base:+.3f} must beat cash {dcash - base:+.3f} on Korea"
    )


def test_guard_e36_inequality_over_male_lever(model, baselines):
    """E36/E39-H391 (the README dumbbell): narrowing inequality (nb17 convention)
    beats the saturated male-prospects lever (E36 Hill drive at income +30%) on the
    open core in Korea and Germany.

    On failure: the README head-to-head and the E36 H349-H357 ranking need re-judging.
    """
    qmax, i50 = 0.390, 13.6
    male = f9(fq=qmax * 30 / (i50 + 30))
    ineq = f9(fS=1.2 * 0.26, fC=0.5 * 0.26)
    for reg in ["Korea", "Germany"]:
        base = baselines[reg]["tfr"]
        di = model.run_cal(reg, force=ineq)["tfr"] - base
        dm = model.run_cal(reg, force=male)["tfr"] - base
        assert di > dm > 0, f"{reg}: inequality {di:+.3f} must beat male {dm:+.3f}"


def test_guard_e37_h363_coupling_transplant(model, baselines):
    """E37-H363/E40-A4d: the Israel-coupling transplant (C0 Korea -> 0.97) lifts the
    open-core Korea endpoint by +0.6..+0.9 (measured +0.736 post-E40).

    On failure: the familism-lives-in-coupling verdict moved - re-judge E37-H363 and
    the E39 closed-loop echo (+0.818).
    """
    c0 = E.C0["Korea"]
    try:
        E.C0["Korea"] = 0.97
        lift = model.run_cal("Korea")["tfr"] - baselines["Korea"]["tfr"]
    finally:
        E.C0["Korea"] = c0
    assert 0.6 < lift < 0.9, f"transplant lift {lift:+.3f} outside the recorded band"


def test_guard_catalogue_integrity():
    """E14-E33: the single-source-of-truth lever catalogue keeps its shape - 182
    levers, every forcing key a valid channel, and the standard ramp (zero before
    year 2, full at year 12).

    On failure: the catalogue drifted - every batch total and the A4f stratified
    sample base are suspect.
    """
    assert len(CATALOGUE) == 182
    for lever in CATALOGUE:
        assert set(lever["f"]) <= set(CHANNELS), lever["id"]
    fy = force_of({"fS": 1.0})
    assert fy(1)[CHANNELS.index("fS")] == 0.0
    assert fy(12)[CHANNELS.index("fS")] == 1.0


def test_guard_experiments_log_verdict_tally():
    """Campaign roll-up: the experiments log's per-hypothesis verdict rows tally EXACTLY to the
    executive-summary counts - 392 unique H ids, no gaps H1-H392, 211 SUPPORTED / 109 PARTIAL /
    69 REFUTED / 2 REFRAMED / 1 INCONCLUSIVE.

    On failure: a recorded verdict changed, a row was added without updating the roll-up, or the
    roll-up was edited without a row - reconcile the exec summary against the tables before
    trusting any campaign-total claim. (An E40 round-9 reviewer miscounted these by hand; this
    guard settles the tally by parse, not by eye.)
    """
    import re
    from collections import Counter

    txt = (PROJ / "docs" / "experiments" / "demographic-collapse-experiments.md").read_text()
    verdicts = ("SUPPORTED", "PARTIAL", "REFUTED", "REFRAMED", "INCONCLUSIVE")
    rows = {}
    for line in txt.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        m = re.fullmatch(r"(?:E\d+-)?(H\d+)[a-z]?(?:\s*\(.*\))?", cells[0].strip(" *`"))
        if not m:
            continue
        v = next((k for k in verdicts if cells[-1].upper().strip("*").startswith(k)), None)
        if v:
            assert rows.get(m.group(1), v) == v, f"conflicting verdicts for {m.group(1)}"
            rows[m.group(1)] = v
    assert len(rows) == 392, f"expected 392 unique H rows, parsed {len(rows)}"
    assert not [n for n in range(1, 393) if f"H{n}" not in rows], "gap in H numbering"
    assert Counter(rows.values()) == Counter(
        SUPPORTED=211, PARTIAL=109, REFUTED=69, REFRAMED=2, INCONCLUSIVE=1
    )


def test_guard_e40_audit_record():
    """E40: the audit record stands - A1-A7 present with their recorded verdicts.

    On failure: the verdicts file was regenerated with different findings - the
    experiments log's E40 section no longer matches its artifact.
    """
    v = {x["id"]: x["verdict"] for x in json.load(open(PROJ / "reports" / "nb36_e40_verdicts.json"))}
    assert v == {
        "A1": "CONFIRMED-FIXED",
        "A2": "CONFIRMED-FIXED",
        "A3": "CONFIRMED",
        "A4": "MEASURED-HOLDS",
        "A5": "DOCUMENTED",
        "A6": "DOCUMENTED",
        "A7": "DOCUMENTED",
        "A8": "CONFIRMED-FIXED",
    }
