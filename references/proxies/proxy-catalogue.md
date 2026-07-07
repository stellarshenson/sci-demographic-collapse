# Proxy Catalogue

Model-ready proxy blueprints for high-value levers with no direct fertility experiment. Each is composed from cited component effect sizes and flagged for how speculative the composition is. Magnitudes are ΔTFR, order-of-magnitude. Channels map to the coupled model's C (coupling), ρ (childlessness/inequality), P̄ (parity/cost-per-child), τ (tempo), S (economic security).

> [!IMPORTANT]
> **Sync with code.** This catalogue and the importable registry `src/sci_demographic_collapse/proxies.py` are two copies of one truth - edit one, mirror it in the other in the same commit. This file is authoritative for citations and narrative; `proxies.py` (`PROXIES`, `education_cost_multiplier`) is authoritative for the numbers a model imports.

> [!IMPORTANT]
> Kim-Tertilt-Yum (AER 2024) correction, load-bearing across several proxies: a **22% education tax + moderate transfers → +11% fertility, −39% education spend**. The often-quoted **+28%** is the *full externality-removal* counterfactual, not the tax effect. Do not conflate them.

## 1. Free public university, progressively funded

- **Channel** cost-per-child + S · **Sign** ambiguous, weakly positive · **Composed magnitude** +0.03 to +0.08 ΔTFR
- **Components**
  - debt removal → fertility: ~\$60k student debt ≈ −42% likelihood of children; ~7.5pp completed-fertility gap (Nau, Dwyer & Hodson 2015) - diluted across the ~30-40% debt-holding share
  - opportunity-cost, countervailing: an extra year of schooling lowers completed number of children though it raises any-birth probability (Fort, Schneeweis & Winter-Ebmer 2016)
  - partial de-positionalisation: flattening the wealth-gate lowers the private return to buying entry, but free base-tier leaves the elite-slot race intact (Kim-Tertilt-Yum 2024)
- **Key uncertainty** two primitives point opposite ways - the sign is not guaranteed positive
- **Honesty flag** highly composed

## 2. Lottery / sample admission above a competence bar

- **Channel** cost-per-child (quantity-quality) · **Sign** positive · **Composed magnitude** ~+0.08 ΔTFR (ceiling ~+0.20 at full externality removal)
- **Components**
  - un-buyable rank zeroes the marginal return to tutoring - functionally KTY's 22% tax → +11% fertility, −39% spend
  - arms-race size: Korea ₩27tn (~\$21bn), 78% of pupils tutored, "edu-poverty" in ~4/10 families, TFR 0.72 (Seoul/CNN 2023)
  - documented peer spillover in positional spend (KTY 2024)
- **Key uncertainty** displacement - competition re-routes to other buyable signals (English, overseas, extracurriculars) or gaming the bar
- **Honesty flag** moderately composed, tightly anchored to a published GE counterfactual

## 3. Dating-app market redesign (intent-verification, choice caps, match-not-search)

- **Channel** coupling → quantum · **Sign** positive, small · **Composed magnitude** +0.02 to +0.05 ΔTFR
- **Components**
  - current apps: no aggregate marriage gain, higher divorce/separation (Jung & Lusher 2026, Tinder-exposure IV)
  - search up, pairing flat: online is the #1 meeting mode yet pairing rate did not rise (Rosenfeld, Thomas & Hausen 2019)
  - redesign → more/better unions → births: **unmeasured** - no natural experiment exists
- **Key uncertainty** the decisive link has no effect size anywhere; redesign only claws back an app-induced coupling wedge
- **Honesty flag** MOST speculative of the set - one full link is un-priced

## 4. Pension rewiring (child-linked pension credits)

- **Channel** economic security (old-age-security return on children) · **Sign** positive · **Composed magnitude** +0.1 to +0.4 ΔTFR
- **Components**
  - PAYG externality: pensions 0 → 10% of GNP associate with −0.7 to −1.6 TFR, ~55-65% of the Europe-US gap (Boldrin, De Nardi & Jones 2005)
  - reverse pass-through: a child-linked credit restores a fraction f of the child→old-age-return linkage; realistic f = 10-25% recovers 0.1-0.4 TFR
- **Key uncertainty** the base is a cross-country association, not a within-country experiment; credit → perceived-return pass-through is unmeasured (people may not trust the linkage)
- **Honesty flag** direction and externality size well-cited; magnitude composed

## 5. Break the marriage-birth package (non-marital-birth equality, East Asia)

- **Channel** coupling / quantum (unlock gated births) · **Sign** positive · **Composed magnitude** +0.05 to +0.2 ΔTFR
- **Components**
  - births gated behind a collapsing marriage: non-marital <2-4% (Japan/Korea) vs 40-60%+ (France); legal "illegitimacy" discrimination is a documented suppressor
  - legal recognition keeps the union-fertility link intact: France PACS - after 1999 marriage-fertility weakened but marriage+PACS still tracks fertility at TFR ~1.8 (Oreffice 2011; Rault)
- **Key uncertainty** culture, not statute, may bind - PACS worked in an already cohabitation-tolerant France; East Asian stigma may not yield to law alone
- **Honesty flag** direction well-grounded ecologically; the legal→behaviour magnitude in a high-stigma setting is the leap

## 6. Positional arms-control (tax/cap on positional education spending)

- **Channel** cost-per-child / inequality (quantity-quality via status competition) · **Sign** positive · **Composed magnitude** ~+0.08 ΔTFR (ceiling ~+0.20)
- **Components**
  - KTY (2024) GE experiment: 22% education tax + moderate transfers → +11% fertility, −39% education spend; the status externality puts fertility 28% below the no-externality counterfactual
  - empirically documented private-education spillover (KTY motivating evidence)
- **Key uncertainty** a calibrated GE model - external validity and the assumed spillover elasticity drive the number; keep +11% (policy) and +28% (full removal) distinct
- **Honesty flag** TIGHTEST proxy - essentially one published GE-modelled number; only model-versus-world remains

## 7. Education interface (the synthesis - a reusable 2-parameter term)

Generalises the whole education-financing/access theme: fertility responds not to education *quantity* but to the privately-borne share of the age-0-24 human-capital bill, multiplied by positionality.

- **Interface** `effective_cost_per_child = base × private_share × (1 + k·π)`, with `private_share ∈ [0,1]` (family vs society funding) and positionality `π ∈ [0,1]`
- **Calibration** `k` from Korea's shadow-spend elasticity - a 1% rise in private education spend → 0.18-0.26% TFR decline (J. Population Economics 2026); the π→0 limit from the Dutch numerus-fixus lottery on/off/on (1972 / 2017 / 2023)
- **Channel** P̄ (cost) modifier coupled to ρ (inequality) · **Sign** lowering private_share raises fertility **only if π is low** (else captured - the Spence 1973 signalling trap: subsidising a positional signal just inflates it)
- **Key uncertainty** π is not directly observable and must be inferred; the sign-flip at high π is the whole refinement of INCOME-NOT-DEGREES
- **Honesty flag** a composed interface, not a single measured coefficient - but both anchors (Korea slope, Dutch limit) are real

---

**Most defensible** - #6 positional arms-control and #4 pension rewiring (both rest on directly cited magnitudes; #2 lottery shares #6's evidence base). **Most speculative** - #3 dating-app redesign (its load-bearing link is un-priced). Regenerate or supersede any entry when a direct experiment appears.
