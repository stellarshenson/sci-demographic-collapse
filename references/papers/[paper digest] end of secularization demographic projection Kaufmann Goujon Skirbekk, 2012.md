# [Paper digest] The end of secularization in Europe? A socio-demographic perspective

**Authors**: Eric Kaufmann, Anne Goujon, Vegard Skirbekk<br>
**Year**: 2012  **Venue**: Sociology of Religion 73(1):69-91<br>
**Original**: [https://doi.org/10.1093/socrel/srr033](https://doi.org/10.1093/socrel/srr033) — repository copy [http://pure.iiasa.ac.at/id/eprint/9976/](http://pure.iiasa.ac.at/id/eprint/9976/) (**PAYWALLED / abstract**)<br>
**Local PDF**: none (ABSTRACT-ONLY)<br>
**Model class**: applied cohort-component projection with religious-affiliation states + switching (the modular-bearer analogue in demography)<br>
**Downloaded**: no - **ABSTRACT-ONLY**

## The model (the applied modular bearer)

A **cohort-component projection** disaggregated by religiosity, run for European countries. Population is split into religious/secular states projected forward with four parameters:

- **Fertility** differential by state (the religious out-reproduce the secular) - differential fertility drives the pronatal state's share up
- **Migration** (adds religious inflow)
- **Switching / retention** between states (secular drift out of religion is the leak; retention is the fidelity `φ`)
- **Age-sex structure** and reproductive momentum

Result: reproductive momentum of the religious can slow or **reverse** secularisation - higher religiosity by 2100 than 2000 in some scenarios - *unless* switching (secular defection) stays high. It is the empirical, state-based, Leslie-embedded version of the heritable-fertility rebound.

## How differential fertility enters

As state-specific fertility rates inside a standard cohort-component matrix; the projection multiplies each religious state by its own TFR each cycle, while the switching matrix moves people between states - exactly `transmission (retention/switching) × fertility` embedded in age structure.

## Portability to our ensemble

The template for our **modular OFF switch and Leslie embedding**: model the bearer as extra state labels on the cohort-component/OT ensemble, with a retention/switching sub-matrix (our `φ_c` and edge-leak) applied at reproduction. Set switching to its neutral (baseline mixing) value and fertility differentials to zero → the projection collapses to the ordinary single-population Leslie run, giving an exact baseline-preserving disable.

## Tags

`cohort-component` `religiosity` `retention-switching` `differential-fertility` `momentum` `secularization-reversal` `state-labels` `modular-bearer` `abstract-only` `Leslie-embedded`
