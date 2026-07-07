"""Composed proxy blueprints for fertility levers with no direct experiment - as reusable code.

A proxy estimates a lever's fertility effect by composing the researched dynamics of its parts, when
no clean "policy -> fertility" natural experiment exists. Each entry carries a channel, a sign, a
ΔTFR magnitude range, cited component effect sizes, and an honesty flag for how speculative it is.

SYNC: this module and the prose catalogue are two copies of one truth and MUST be updated together.
  - prose companion: ``references/proxies/proxy-catalogue.md``
  - edit one -> mirror the change in the other in the same commit; the catalogue is authoritative for
    citations and narrative, this module is authoritative for the numbers a model imports.

Usage::

    from sci_demographic_collapse.proxies import PROXIES, education_cost_multiplier
    p = PROXIES["pension-rewiring"]           # p.channel, p.dtfr_low, p.dtfr_high, p.components
    mult = education_cost_multiplier(0.1, 0.2)  # near-public, low-positionality cost multiplier
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Proxy:
    """One composed proxy blueprint. Magnitudes are ΔTFR (order of magnitude)."""

    name: str
    channel: str          # model channel: C, rho, Pbar, tau, S (or a combination)
    sign: str             # "+", "-", "±"
    dtfr_low: float
    dtfr_high: float
    components: tuple      # ((effect description, citation), ...)
    uncertainty: str
    flag: str             # honesty flag: how speculative the composition is


PROXIES: dict[str, Proxy] = {
    "free-public-university": Proxy(
        name="Free public university, progressively funded",
        channel="Pbar+S", sign="±", dtfr_low=0.03, dtfr_high=0.08,
        components=(
            ("~$60k student debt ≈ -42% likelihood of children; ~7.5pp completed-fertility gap", "Nau, Dwyer & Hodson 2015"),
            ("extra year of schooling lowers completed number of children (countervailing)", "Fort, Schneeweis & Winter-Ebmer 2016"),
            ("flattening the wealth-gate lowers private return to entry; elite-slot race intact", "Kim-Tertilt-Yum 2024"),
        ),
        uncertainty="two primitives point opposite ways - the sign is not guaranteed positive",
        flag="highly composed",
    ),
    "lottery-admission": Proxy(
        name="Lottery / sample admission above a competence bar",
        channel="Pbar", sign="+", dtfr_low=0.08, dtfr_high=0.20,
        components=(
            ("un-buyable rank ~ 22% education tax -> +11% fertility, -39% edu spend", "Kim-Tertilt-Yum 2024"),
            ("arms-race size: Korea ₩27tn (~$21bn), 78% tutored, TFR 0.72", "Seoul/CNN 2023"),
            ("documented peer spillover in positional spend", "Kim-Tertilt-Yum 2024"),
        ),
        uncertainty="displacement - competition re-routes to other buyable signals or gaming the bar",
        flag="moderately composed, tightly anchored to a published GE counterfactual",
    ),
    "dating-app-redesign": Proxy(
        name="Dating-app market redesign (intent-verification, choice caps, match-not-search)",
        channel="C", sign="+", dtfr_low=0.02, dtfr_high=0.05,
        components=(
            ("current apps: no aggregate marriage gain, higher divorce/separation", "Jung & Lusher 2026"),
            ("online is #1 meeting mode yet pairing rate did not rise", "Rosenfeld, Thomas & Hausen 2019"),
            ("redesign -> more/better unions -> births is UNMEASURED", "no natural experiment"),
        ),
        uncertainty="the decisive link has no effect size anywhere",
        flag="MOST speculative - one full link is un-priced",
    ),
    "pension-rewiring": Proxy(
        name="Pension rewiring (child-linked pension credits)",
        channel="S", sign="+", dtfr_low=0.1, dtfr_high=0.4,
        components=(
            ("pensions 0->10% of GNP associate with -0.7 to -1.6 TFR", "Boldrin, De Nardi & Jones 2005"),
            ("reverse pass-through restores a fraction f=10-25% -> +0.1..+0.4 TFR", "composed"),
        ),
        uncertainty="base is a cross-country association; credit->perceived-return pass-through unmeasured",
        flag="direction and externality size well-cited; magnitude composed",
    ),
    "break-marriage-birth-package": Proxy(
        name="Break the marriage-birth package (non-marital-birth equality, East Asia)",
        channel="C+Pbar", sign="+", dtfr_low=0.05, dtfr_high=0.2,
        components=(
            ("births gated behind marriage: non-marital <2-4% (JP/KR) vs 40-60%+ (FR)", "OECD SF2.4"),
            ("legal recognition keeps the union-fertility link intact (PACS)", "Oreffice 2011; Rault"),
        ),
        uncertainty="culture, not statute, may bind - stigma may not yield to law alone",
        flag="direction ecological; the legal->behaviour magnitude is the leap",
    ),
    "positional-arms-control": Proxy(
        name="Positional arms-control (tax/cap on positional education spending)",
        channel="Pbar+rho", sign="+", dtfr_low=0.08, dtfr_high=0.20,
        components=(
            ("22% education tax + transfers -> +11% fertility, -39% spend (full removal +28%)", "Kim-Tertilt-Yum 2024"),
            ("empirically documented private-education spillover", "Kim-Tertilt-Yum 2024"),
        ),
        uncertainty="calibrated GE model - external validity drives the number; keep +11% and +28% distinct",
        flag="TIGHTEST proxy - essentially one published GE-modelled number",
    ),
}

# Korea shadow-spend elasticity: a 1% rise in private education spend -> ~0.18-0.26% TFR decline
# (J. Population Economics 2026). Used to weight the positionality amplifier below.
EDUCATION_K = 0.22


def education_cost_multiplier(private_share: float, positionality: float, k: float = EDUCATION_K) -> float:
    """Effective cost-per-child multiplier from education financing and positionality (the M12 interface).

    ``base × private_share × (1 + k·π)`` relative to base: lowering ``private_share`` (socialising the
    cost) cuts the term, but only helps if positionality ``π`` is low - otherwise the arms race is
    captured (the Spence 1973 signalling trap). ``private_share`` and ``positionality`` in [0, 1].
    The π->0 limit is anchored on the Dutch numerus-fixus lottery (on/off/on, 1972/2017/2023).
    """
    if not (0.0 <= private_share <= 1.0 and 0.0 <= positionality <= 1.0):
        raise ValueError("private_share and positionality must be in [0, 1]")
    return private_share * (1.0 + k * positionality)
