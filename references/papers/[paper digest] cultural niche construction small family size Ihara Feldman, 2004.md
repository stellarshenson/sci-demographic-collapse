# [Paper digest] Cultural niche construction and the evolution of small family size

**Authors**: Yasuo Ihara, Marcus W. Feldman<br>
**Year**: 2004  **Venue**: Theoretical Population Biology 65(1):105-111<br>
**Original**: [https://doi.org/10.1016/j.tpb.2003.07.003](https://doi.org/10.1016/j.tpb.2003.07.003) — [PubMed 14642348](https://pubmed.ncbi.nlm.nih.gov/14642348/) (**PAYWALLED**)<br>
**Local PDF**: none (ABSTRACT-ONLY)<br>
**Model class**: deterministic recursion on trait frequencies (Cavalli-Sforza/Feldman gene-culture frame, two coupled cultural traits)<br>
**Downloaded**: no - **ABSTRACT-ONLY** (model structure from abstract + Colleran 2016 review, downloaded)

## The model (the gating idea we want)

Two culturally transmitted traits with a **niche-construction coupling**:

- Trait 1 = a general predisposition (a preference for high education), transmitted **vertically** (parent→child). Its population frequency defines the "cultural niche" / background
- Trait 2 = a fertility-reducing preference (small family size), transmitted both vertically and **obliquely** (e.g. from teachers)
- **The gate**: the frequency of Trait 1 (the education niche) sets the **rate of oblique relative to vertical transmission** of Trait 2. High average education raises the oblique share, so Trait 2 percolates faster than vertical transmission alone permits
- **Result**: even a slight over-representation of low-fertility individuals drives the fixation of small family size, *provided* the oblique-transmission rate depends strongly enough on the cultural background - i.e. the niche gates the second trait's spread

## How differential fertility enters

Weakly and asymmetrically: low-fertility individuals are slightly under-reproducing, yet the education-gated boost to oblique transmission of the fertility-reducing trait overwhelms that reproductive disadvantage - a cultural-transmission advantage beating a fertility disadvantage (the same logic Wodarz 2020 later put in ODE form via `β` vs `r`).

## Portability to our ensemble

This is the literature source for our **gating retention term**: one bearer component (a boundary/background trait) multiplicatively sets the transmission rate of the others, exactly our design where a retention/boundary term gates the norm `N`, parity `P̄`, marriageability `q`, and coupling `C`. When the gate is neutral, the gated components transmit at their own baseline rate - clean OFF condition.

## Tags

`niche-construction` `two-trait-coupling` `gating` `vertical-oblique` `education` `small-family-size` `transmission-rate-modulation` `abstract-only` `retention-gate-source`
