# Quantum and tempo of life-cycle events - Bongaarts and Feeney, 2006

**37** pages, MPIDR / Demographic Research Monographs (open access), authors' own general framework extending
their 1998 *Population and Development Review* article "On the quantum and tempo of fertility" (PDR 24(2):
271-291). The load-bearing OA primary for the tempo-quantum decomposition (the 1998 original is paywalled and
403s from cloud IPs; this is the same method by the same authors, generalized to any life-cycle event).

## Key mechanism

- A period rate mixes two things: the **quantum** (how many events a synthetic cohort completes) and the
  **tempo** (the timing / mean age at which events occur). A shift in tempo alone distorts the period
  quantum measure without any change in completed behaviour
- **Tempo distortion** is defined as an inflation or deflation of a period quantum indicator (e.g. the TFR)
  caused purely by a rise or fall in the mean age at which the event occurs - a rising mean age deflates the
  TFR (postponement borrows births from the future), a falling mean age inflates it
- The correction (their eq. 6): the **tempo-adjusted TFR** is
  `TFR*(t) = TFR(t) / (1 - r_p(t))`, where `r_p` is the annual rate of change of the period mean age at
  childbearing. The tempo distortion equals `TFR*(t) - TFR(t)`. This uses only period measures - it does not
  require cohort data and separates tempo distortion from the period-vs-cohort question

## Main findings

- Demonstrated tempo distortion in the TFR across 17 countries: much of the observed late-20th-century
  fertility decline in the developed world was postponement (a rising mean age), not a fall in completed
  family size - the adjusted TFR* sat well above the observed TFR during the postponement decades
- The same framework applies to first marriage, life expectancy, and any life-cycle event - a falling mean
  age at death inflates period life expectancy the same way postponement deflates the TFR
- Adjusted period measures approximate lagged cohort outcomes and indicate "what rates could be if
  postponement ended" - a durable-vs-transient reading of a moving period rate

## Key takeaways for this project

- Directly grounds the model's TFR composition: `TFR = quantum(C,rho,Pbar) * fec(tau) * max(1 - kBF*dtau, 0)`.
  The `max(1 - kBF*dtau, 0)` factor is the Bongaarts-Feeney `(1 - r_p)` term on the realized annual mean-age
  change; `kBF=1.0` is the canonical undamped B-F factor. The model's `adjTFR_model = quantum*fec` is the
  tempo-**adjusted** TFR* (it strips the tempo factor), so `TFR = adjTFR_model * tempo_factor` mirrors the
  paper's `TFR = TFR* * (1 - r_p)` exactly
- The paper is the theory behind the quantum probe: an intervention's durable effect is its change in the
  tempo-adjusted TFR* (`Delta adjTFR_model`); its tempo effect is the residual carried by the tempo factor
  and reverts when the mean-age shift stops
- Caveat the paper itself flags (and the Ni Bhrolchain critique sharpens): the adjustment assumes period
  effects dominate and a smooth mean-age change; it is fragile to shape changes in the age schedule and to
  short-run mean-age volatility. The probe therefore reads the tempo factor from the model's own realized
  dtau rather than re-estimating r_p from noisy data

**Tags**: tempo-quantum, tempo-adjusted TFR, Bongaarts-Feeney, postponement, mean age at childbearing,
period-vs-cohort, calibration, probe-grounding
