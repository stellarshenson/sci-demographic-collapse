# The culture-bearer transmission operator

**In one line**: a culture bearer is a parent who hands a coherent BUNDLE of channel traits to the next cohort; cultures that hand the bundle to more children and retain it grow their population share generation after generation, and the whole thing is a single linear operator `Φ = r · V Λ V⁻¹` acting on the trait vector, built from the SAME channel-coupling eigenstructure that governs how interventions combine.

## Overview

The coupled core (`emergent.py`) treats fertility as an emergent product of channel states carried by a representative agent (or a dispersed ensemble). What it does not yet carry is INHERITANCE: that the norm, the desired family size, the partnership pattern a cohort holds are partly transmitted from its parents, and that the parents who transmit are over-weighted by how many children they had. This document grounds a modular, default-OFF operator that adds exactly that - cultural transmission with fertility-weighted selection - to the coupled-ODE core.

## Key facts from the literature

- **Transmission is a probability operator** (Cavalli-Sforza & Feldman, 1981) - the child's trait is drawn from a transmission matrix `b` indexed by the parents' traits; perfect transmission is the identity `b = I`, imperfect transmission spreads probability off-diagonal. This is the exact formal justification for a baseline-preserving operator: at neutral fidelity the operator is the identity and disabled equals baseline
- **Three channels** - vertical (parent→child), oblique (older non-parents), horizontal (peers) (Colleran, 2016). The bearer models the VERTICAL channel; secularisation / novelty influx is the oblique-horizontal leak. Purely vertical transmission makes a culture static, so change needs the leak - our retention gate `r`
- **Fertility is a heritable cultural trait** (Collins & Page, 2019) - the per-generation response to selection is the breeder's equation `R = h² · S`, `S` the selection differential (higher-fertility types leave more descendants who partly share the trait). This is the continuous-trait form of the drift we implement, and its documented failure mode (an unrealistic rebound) is exactly why it must be paired with an explicit fidelity/leak term (`p·F > 1`, Arenberg et al., 2021)
- **Niche construction gates transmission** (Ihara & Feldman, 2004) - one culturally inherited trait (education) sets the RATE at which a second (small-family preference) transmits; even a slight over-representation of low-fertility types then fixes small family size when the gate is strong enough. This motivates a single scalar RETENTION gate `r` multiplying the whole operator: neutral gate → components transmit at their own baseline (clean OFF)
- **Retention, not fertility, is the dominant term** - across the maintenance-model literature the balance that decides whether a norm is stable or erodes is transmission fidelity and the vertical-vs-oblique share, not the reproductive differential itself (Colleran, 2016; the `p·F > 1` condition, Arenberg et al., 2021). A high-fertility subgroup that leaks its children to the secular mainstream every generation does not grow its share; a lower-fertility subgroup with near-perfect retention can. The selection differential only bites through the retained fraction

## The operator

Each reproductive cohort carries a cultural trait vector `x` - the subset of the seven channels that are transmitted as IDEALS rather than set by structure (see below). Culture is a linear machine that bends the parents' arrow into the child's: it ROTATES (turning up one trait nudges the traits it travels with) and SCALES (amplifies some bundles, fades others). At cohort renewal,

```
Δx  =  r · V Λ V⁻¹ · ( x̄ᵂ_parents − x_current )
x_next  =  x_baseline_next  +  Δx
```

- `V` - the cultural-archetype eigenvectors (coherent channel bundles). NOT invented: they are the eigenvectors of the cultural sub-block of the intervention-combination Hessian `H = ∇²logTFR(0)` (`combine.grad_hess`). The same coupled directions that diagonalise how interventions combine diagonalise how culture transmits - one operator, two phenomena. `H` is symmetric so `V` is orthonormal and `V⁻¹ = Vᵀ`
- `Λ` - diagonal per-bundle transmission FIDELITY (`>1` amplify a bundle, `<1` fade it). This is the composite / per-component knob; `Λ = I` is isotropic retention with no bundle differentiation
- `r` - the scalar RETENTION gate and the single on/off switch. `r = 0 → Δx = 0`, the operator is a mathematical no-op, and the core reproduces its committed baseline to machine precision
- `x̄ᵂ_parents` - the FERTILITY-WEIGHTED parental mean, weight `∝` each subgroup's realised TFR. This weighting is what makes iterated application arc the population toward the operator's dominant eigenvector - whichever culture out-reproduces (and retains) the rest (Perron-Frobenius = the Collins-Page selection result). A small `ε` noise term is permitted

## The cultural channel subset

The seven channels are `C` (coupling), `ρ` (childlessness), `P̄` (parity), `τ` (tempo), `S` (security), `N` (norm), `q` (marriageability). The bearer carries the four that are transmitted as cultural IDEALS:

- **`N` (norm)** - the childfree / small-family ideal is the canonical vertically-and-obliquely transmitted trait (Colleran, 2016; Cavalli-Sforza & Feldman, 1981)
- **`P̄` (desired parity)** - the fertility-carrying trait itself; `R = h² S` acts directly on it (Collins & Page, 2019; the small-family preference of Ihara & Feldman, 2004)
- **`ρ` (childlessness)** and `N` are the `{norm, childlessness}` coherent bundle in `H` (the `lam_rho` coupling) - they travel together
- **`C` (coupling / partnership pattern)** - partnership formation is culturally transmitted and is the coupling bundle in `H`

Excluded are `S`, `τ`, `q`. These are the STRUCTURAL background - economic security, the timing outcome it drives, and marriageability capital set by the childhood-investment environment and health. In the niche-construction frame they GATE transmission (education/economy set the oblique share) but are not themselves the transmitted ideal (Ihara & Feldman, 2004), and Cavalli-Sforza & Feldman (1981) separate transmission (culture) from the structural fitness/environment it rides on. Folding them into the bearer would double-count the ODE's own security→coupling and security→tempo wiring.

## How V is derived from H

`combine.grad_hess` estimates `H = ∇²logTFR(0)` by central differences on the calibrated core over the forcing channels `(fS, fC, fPb, fTau, fRV, fN)`. The cultural sub-block is the 4×4 restriction to `(fC, fRV, fPb, fN)` - the four cultural carriers. Its symmetric eigendecomposition (`numpy.linalg.eigh`) gives the orthonormal `V`. For Germany (in the basin, the well-converged case) the four eigenvectors are the coherent bundles the literature predicts: a norm mode (≈ `fN`), a coupling mode (≈ `fC` with `fP̄`), a childlessness mode (≈ `fRV`), and a nearly-isolated parity mode (≈ `fP̄`). Only the DIRECTIONS (the rotation into the bundle basis) are used; the eigenVALUES are not - `Λ` is a separate fidelity knob - so the `fN`-diagonal magnitude caveat (a kink at `fN = 0`, non-convergent second difference; see the combination-law doc) does not affect the operator, since it perturbs the eigenvalue, not the sensible pure-`N` direction of that eigenvector.

## Why this is new here

The mechanics - a transmission operator with fertility weighting, Perron-Frobenius selection of the dominant cultural type - have been explored in CELLULAR-AUTOMATA and discrete trait-frequency recursions (Ihara & Feldman, 2004; the models catalogued by Colleran, 2016), where agents sit on a lattice or a frequency simplex decoupled from any structural-fertility model. What is new is embedding the same operator INSIDE a coupled-ODE behavioural core whose channels already carry structural dynamics (the coupling trap, the bistable norm, the dependency→security feedback, the Bongaarts-Feeney tempo term). The bearer does not replace those dynamics; it adds an inheritance term that reuses the core's OWN channel-coupling eigenstructure (the shared `H`/`Φ` bundles), so transmission and intervention-combination are governed by one matrix rather than two disconnected models. Selection then acts on traits that feed back through the full calibrated fertility machine, not on abstract lattice tokens.

## Files

- `src/sci_demographic_collapse/culture.py` - the operator: `CultureOperator` (`from_hessian`, `from_model`, `matrix`, `delta`, `weighted_mean`, `dominant`)
- `src/sci_demographic_collapse/emergent.py` - `run` / `run_ens` accept an optional `culture=` operator (default `None`); `r = 0` is a machine-precision no-op
- `src/sci_demographic_collapse/combine.py` - source of `H` and its eigenstructure (`grad_hess`)
- `references/papers/` - the four grounding digests (Cavalli-Sforza & Feldman 1981; Ihara & Feldman 2004; Colleran 2016; Collins & Page 2019)
