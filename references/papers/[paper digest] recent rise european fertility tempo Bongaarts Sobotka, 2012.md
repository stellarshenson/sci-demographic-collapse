# [Paper digest] Demographic Explanation for the Recent Rise in European Fertility

**Authors**: John Bongaarts, Tomáš Sobotka<br>
**Year**: 2012  **Venue**: Population Studies (working-paper version, VID / Population Council), OA<br>
**Original (link)**: [https://www.humanfertility.org/File/GetDocument/Docs/Symposium/Bongaarts_Sobotka.pdf](https://www.humanfertility.org/File/GetDocument/Docs/Symposium/Bongaarts_Sobotka.pdf)<br>
**Local PDF**: `[paper] recent rise european fertility tempo Bongaarts Sobotka, 2012.pdf` (OA, 53 pp)<br>
**Used in**: E46 second-order tempo anchor (PERIOD-level recovery episode timescale + the Bongaarts-Feeney tempo mechanism that couples tau_dot to observed TFR)

## Summary

Explains the first continent-wide rise in the period TFR since the 1960s - **between 1998 and 2008** - as mostly the fading of the tempo distortion that had held the TFR down while the mean age at childbearing was rising fast. Introduces the tempo-and-parity-adjusted TFR (TFR_p*). This paper is the period-frame counterpart to Sobotka-Zeman-Frejka: it gives the length of a real recovery EPISODE (~a decade) and, crucially, the mechanism that links the model's `tau` (mean age at birth) to observed fertility - the Bongaarts-Feeney relation `TFR_obs = TFR_quantum·(1 - r)` where `r = d(tau)/dt` is the pace of postponement.

## Parameters for the model

- **Recovery episode length**: the continent-wide period-TFR rise ran **1998 -> 2008, i.e. ~10 years** from trough to the recent peak - the period-frame recuperation timescale
- **Recovery magnitude**: increases from the minima reached **as high as +0.51 children/woman (Denmark)**; **eighteen countries rose by more than +0.2**; Spain went from **1.16 (1998) to 1.46 (2008)**, +0.30 over the decade, almost entirely at birth orders one and two
- **Bongaarts-Feeney tempo mechanism**: the period tempo distortion is proportional to the RATE of change of the mean age; their simulated illustration uses `TFR_obs = TFR_quantum·(1 - r)`, e.g. `0.9·(1 - 0.31) = 0.62`, so an annual mean-age rise of `r ~ 0.1-0.3 years/year` depresses the observed TFR by 10-30%
- **Trend that drove the recovery**: the tempo effect (gap between adjusted and unadjusted TFR) **declined over 1998-2008 in all countries except Austria**, and vanished entirely in Spain - the recovery is the postponement PACE decelerating, not the quantum rising
- **Variance signature**: in their simulation the variance of the period fertility schedule first FALLS during the TFR decline, then RISES back to its initial value during the TFR recovery - the recovery is carried by the widening age schedule, with no shift in the modal age
- **Two mechanisms, both present**: (i) disappearance of the downward period tempo distortion, and (ii) a cohort-driven recuperation at older ages of births postponed at younger ages - the same phenomenon read in period vs cohort terms

## Caveats

The paper is explicit that period and cohort descriptions are two views of one process (`c = t - a`), so the ~10-year period episode and the ~15-year cohort span (Sobotka-Zeman-Frejka) are not independent measurements - the period recovery is faster because it compresses the tail of within-cohort catch-up. The recovery is attributed largely to tempo (a mechanical consequence of the mean age decelerating), which is precisely what a second-order `tau` law can generate endogenously: when `tau` overshoots its target and `tau_dot` reverses sign, `(1 - r)` briefly exceeds 1 and the observed TFR bumps above quantum (the overcompensation seen in the US/Czech cohorts). For the model: use ~10 years as the period trough-to-recovery timescale and the `TFR_obs = TFR_q·(1 - tau_dot)` link to convert `tau` dynamics into a fertility bump.
