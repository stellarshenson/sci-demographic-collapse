# [Paper digest] The heritability of fertility makes world population stabilization unlikely in the foreseeable future

**Authors**: Jason Collins, Lionel Page<br>
**Year**: 2019  **Venue**: Evolution and Human Behavior 40(1):105-111<br>
**Original**: [https://www.sciencedirect.com/science/article/abs/pii/S1090513817302799](https://www.sciencedirect.com/science/article/abs/pii/S1090513817302799) (**PAYWALLED**)<br>
**Author summary + code**: [blog.jcx.au](https://blog.jcx.au/posts/an-evolutionary-projection-of-global-fertility-and-population-my-new-paper-with-lionel-page-in-evolution-human-behavior) ; OSF data/code [https://osf.io/4r3kh/](https://osf.io/4r3kh/)<br>
**Local PDF**: none (ABSTRACT-ONLY)<br>
**Model class**: deterministic quantitative-genetic projection (breeder's equation on a continuous heritable fertility trait)<br>
**Downloaded**: no - **ABSTRACT-ONLY** (model reconstructed from author summary; the rebuttal Arenberg et al. 2021, downloaded, restates it formally)

## The model (from author summary; formalised in Arenberg 2021)

Replaces the UN's constant-long-run-fertility assumption with an evolutionary dynamic in which **fertility is a heritable trait**. Selection is captured by the **breeder's equation**: the response to selection per generation is `R = h² · S`, where `h²` is the narrow-sense heritability of fertility and `S` the selection differential (higher-fertility individuals leave more descendants who partly share the trait). Iterating this, the high-fertility phenotype rises in frequency and population-level TFR trends **upward**, so global population overshoots current projections rather than stabilising.

- **Differential fertility IS the selection differential** `S` - the mechanism is literally fertility-weighted transmission of a fertility trait
- Continuous-trait analogue of the two-type compounding in Kolk (2014) and the matrix in Arenberg (2021)
- **Key vulnerability (why we need a leak/fidelity term)**: assumes fertility stays heritable and the high-fertility subgroup's TFR stays above replacement. Arenberg et al. (2021, downloaded) show that with imperfect fidelity `p`, the true condition is `p·F > 1`, which real pronatal subgroups (e.g. the religious, via secular outflow) routinely fail - the Collins-Page rebound is not guaranteed

## Portability to our ensemble

Gives the continuous form of our compounding: `R = h² S` is the per-generation drift of a scalar bearer component (e.g. desired parity `P̄`). Adopt it only paired with an explicit fidelity/leak, or it manufactures the same unrealistic rebound the literature disputes.

## Tags

`heritability` `breeders-equation` `continuous-trait` `selection-differential` `population-projection` `abstract-only` `rebound-hypothesis` `needs-fidelity-leak`
