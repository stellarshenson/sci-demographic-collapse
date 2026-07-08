# [Paper digest] Heritable fertility is not sufficient for positive long-term population growth

**Authors**: Samuel Arenberg, Kevin Kuruc, Nathan Franz, Sangita Vyas, Nicholas Lawson, Melissa LoPalo, Mark Budolfson, Michael Geruso, Dean Spears<br>
**Year**: 2021  **Venue**: Population Wellbeing Initiative (UT-Austin PRC) White Paper No. 1<br>
**Original (download)**: [https://sites.utexas.edu/pwi/files/2021/09/HertiableFertility.pdf](https://sites.utexas.edu/pwi/files/2021/09/HertiableFertility.pdf) (open)<br>
**Local PDF**: `[paper] heritable fertility not sufficient Markov Arenberg Kuruc, 2021.pdf` (in this folder)<br>
**Model class**: deterministic matrix / Markov (two-type, Leslie-compatible)<br>
**Downloaded**: yes (full text)

## The transmission operator (the matrix template we want)

Direct rebuttal of Collins & Page (2019). Two heritable fertility types `i ∈ {H, L}` with reproductive rates `F_H > 1 > F_L` (single-sex, replacement = 1). Types are transmitted parent→offspring with **imperfect fidelity**: offspring of type `i` retain the parent's type with probability `p_{i→i}` and switch with `(1 − p_{i→i})`. The population vector `N = (N_H, N_L)` evolves by

```
N_{t+1} = A N_t ,   A = [ p_{H→H} F_H      (1 − p_{L→L}) F_L ]
                        [ (1 − p_{H→H}) F_H  p_{L→L} F_L      ]
```

- **Fertility-weighted transmission**: every entry of `A` is a transmission probability times the source type's reproductive rate `F_i` - transmission and differential fertility are fused into one operator (a Leslie-style matrix on trait-carrying subpopulations)
- Explicitly "builds on the structure employed by Kolk et al. (2014), but adds imperfect transmission" - i.e. **fidelity `p` is the new ingredient** vs perfect-transmission precursors
- **Persistence condition**: with one-way switching (`p_{L→L}=1`) the high-fertility group evolves as `N_{H,t} = (p_{H→H} · F_H)^t N_{H,0}`, so the pronatal type (and long-run population) grows iff

```
p_{H→H} · F_H > 1     ← fidelity × fertility, the essential eigenvalue condition
```

- Above-replacement fertility `F_H > 1` is **not sufficient**: high outflow (low `p_{H→H}`, e.g. religious→secular drift) can still shrink the pronatal share. A positive parent-child fertility correlation is fully compatible with long-run decline

## How differential fertility enters

As the diagonal weight `F_i` on each retention probability. Selection is governed by the dominant eigenvalue of `A ≈ p_{H→H} F_H`; the leak `(1 − p_{H→H})` is exactly the secularisation-at-the-edge that can defeat high fertility.

## Portability to our ensemble

This is the cleanest structural template for our bearer: a fidelity-times-fertility matrix that is already Leslie-compatible. Read `p_{H→H}` as our per-component fidelity `φ_c` (gated by the retention/boundary term), `F_i` as the campaign-modulated TFR, and the `p·F > 1` eigenvalue as the make-or-break test for whether a pronatal trait compounds. When `φ_c → neutral` the off-diagonal leak restores type-mixing to baseline.

## Tags

`heritability` `matrix-model` `Markov` `imperfect-transmission` `fidelity` `fertility-weighted` `eigenvalue-condition` `edge-leak` `Collins-Page-rebuttal` `Leslie-compatible`
