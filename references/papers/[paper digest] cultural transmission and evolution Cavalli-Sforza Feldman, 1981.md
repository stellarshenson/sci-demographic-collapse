# [Paper digest] Cultural Transmission and Evolution: A Quantitative Approach

**Authors**: Luigi Luca Cavalli-Sforza, Marcus W. Feldman<br>
**Year**: 1981  **Venue**: Princeton University Press (Monographs in Population Biology 16)<br>
**Original**: [Google Books](https://books.google.com/books/about/Cultural_Transmission_and_Evolution.html?id=pBGvyNXkWYcC) (**book, PAYWALLED**)<br>
**Local PDF**: none (ABSTRACT-ONLY - foundational reference)<br>
**Model class**: canonical deterministic transmission-operator formalism (transmission-probability matrices)<br>
**Downloaded**: no - **ABSTRACT-ONLY** (formalism summarised from the literature; it is the framework Ihara-Feldman, Kolk, Wodarz all inherit)

## The transmission-operator formalism (our vocabulary root)

Defines cultural transmission as any non-genetic transmission and gives the canonical operator: for a discrete trait, the probability that a naive individual acquires state `j` is a **transmission-probability matrix** `b` indexed by the phenotypes of the transmitter(s).

- **Three channels**: vertical (parent→child), oblique (older non-parents), horizontal (peers) - each with its own transmission matrix
- **Vertical uniparental / biparental**: transmission probabilities `b(child-state | parent-states)` written as a full mating table over parental phenotype combinations; a "group effect" adds a random oblique contribution mixed with the vertical one
- **Fidelity is the diagonal of `b`**: perfect transmission = identity matrix (`b_{jj}=1`); imperfect transmission spreads probability off-diagonal (this is exactly our per-component `φ_c`, with `φ_c → 1` = faithful, `φ_c → neutral`/off-diagonal = leak)
- Key qualitative result: purely vertical downward transmission makes cultures static; horizontal/oblique channels are needed for rapid change - the basis for treating secularisation/novelty as an oblique leak

## How differential fertility enters

Not intrinsic to the base operator - Cavalli-Sforza & Feldman separate *transmission* from *selection/fitness*. Differential fertility is layered on as a fitness weight `w_i` on each cultural type (the fertility-weighting that Kolk 2014 and Arenberg 2021 then fuse into `A = P∘F`).

## Portability to our ensemble

The transmission-matrix `b` with its identity-matrix OFF condition is the exact formal justification for our modular, baseline-preserving bearer: each composite component gets its own `b_c(φ_c)`; set every `b_c = I` (φ neutral) and the operator is the identity, so disabled == baseline. Fertility-weighting is applied on top as a separate multiplicative fitness term.

## Tags

`canonical-formalism` `transmission-matrix` `vertical-oblique-horizontal` `fidelity` `identity-off-condition` `selection-vs-transmission` `foundational` `abstract-only`
