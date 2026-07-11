# The quantum probe (E48) - classifying interventions as durable quantum vs borrowed tempo

## Overview

A policymaker facing a projected fertility recovery needs one thing the period TFR cannot tell them: is this
a durable gain in completed family size (quantum), or a timing mirage that borrows births from the future and
reverts (tempo)? The quantum probe is a standalone diagnostic that reads the model's own Bongaarts-Feeney
decomposition and returns that verdict automatically for any intervention, plus a policy-facing triple -
"X% quantum, Y% tempo; Z% of the peak effect survives to 2125".

The probe reuses the E41 observability harness (`run_cal(..., trajectories=True)`) and adds no new model
mechanism and no free parameter beyond four pre-registered thresholds. Code: `scratchpad/probe_quantum.py`.
Validation record: `reports/e48_quantum_probe_validation.json`.

## Grounding

The model composes period fertility exactly as Bongaarts and Feeney prescribe (their 2006 general framework,
extending the 1998 *PDR* original; digest in `references/papers/`):

```
TFR = adjTFR_model * tempo_factor
adjTFR_model = quantum * fec = C(1-rho)Pbar * fec(tau)      # the tempo-ADJUSTED TFR* = TFR/(1 - r_p)
tempo_factor = max(1 - kBF*dtau, 0)                         # the Bongaarts-Feeney (1 - r_p) term, kBF=1.0
```

`adjTFR_model` is the tempo-adjusted TFR\* (Bongaarts-Feeney eq. 6): a change in it is a real change in
completed family size. `tempo_factor` is the timing distortion: a rising mean age at childbearing (`dtau > 0`)
deflates the TFR below its quantum, a falling mean age (`dtau < 0`) inflates it - borrowed births that revert
when the mean-age shift stops. The probe turns this identity into a classifier.

## The probe - two axes, four classes

An intervention's effect on TFR splits into a durable part carried by the adjusted TFR\* and a transient part
carried by the tempo factor. Both axes are needed because a lever can be quantum in *composition* yet still
fail to last (an eroding transfer), and a pure timing lever can leave a small durable residual that fools a
durability-only test.

**Axis 1 - composition (Bongaarts-Feeney).** At the year of peak effect, split `dTFR` into

- quantum contribution `q_c = tempo_factor_bar * d(adjTFR_model)` - durable, completed-fertility
- tempo contribution `t_c = adjTFR_bar * d(tempo_factor)` - transient, borrowed timing

and report `tempo_share = |t_c| / (|t_c| + |q_c|)`. High tempo_share is a genuine Bongaarts-Feeney mirage.

**Axis 2 - durability (reversion).** `persistence = d(adjTFR_model)_end / d(adjTFR_model)_peak` - does the
durable component itself survive to the century mark, or does it revert because the lever was withdrawn or
believed temporary. A policy-facing `survive_pct = 100 * dTFR_end / dTFR_peak` reports the same on the whole
effect.

**Classification (pre-registered thresholds):**

| tempo_share | persistence | class | meaning |
|---|---|---|---|
| >= 0.60 | any | **TEMPO-MIRAGE** | timing borrowed; adjTFR\* barely moves, reverts |
| < 0.40 | >= 0.60 | **QUANTUM-DURABLE** | real completed-family gain that lasts |
| < 0.40 | < 0.40 | **QUANTUM-TRANSIENT** | real while funded, reverts on withdrawal (a durability mirage) |
| 0.40-0.60 band, or persistence 0.40-0.60 on the deciding side | | **MIXED** | both components material |

Policy triple: `quantum_pct = 100(1 - tempo_share)`, `tempo_pct = 100*tempo_share`, `survive_pct`.

## Validation on known levers

The probe was run against four levers whose verdicts the campaign already recorded
(`reports/nb14_e19_verdicts.json`, SOTA calibration section), across the two trapped and one basin region:

| lever | Korea | Germany | France | campaign verdict | match |
|---|---|---|---|---|---|
| cash, eroding transfer (`fPb=0.4`, non-durable) | QUANTUM-TRANSIENT (q100/t0, surv 17%) | QUANTUM-TRANSIENT (surv 15%) | QUANTUM-TRANSIENT (surv 15%) | cash = mirage | yes |
| coupling crown (`mag=0.30`) | QUANTUM-DURABLE (q98/t2, surv 100%) | QUANTUM-DURABLE | QUANTUM-DURABLE | coupling escape / quantum | yes |
| tempo push (`fTau=-3.0`) | TEMPO-MIRAGE (q17/t83, surv 35%) | TEMPO-MIRAGE (t87) | TEMPO-MIRAGE (t86) | tempo mirage | yes |
| cash, durable parity (`fPb=0.4`) | QUANTUM-DURABLE (q100/t0, surv 90%) | QUANTUM-DURABLE | QUANTUM-DURABLE | control (durable = quantum) | yes |

All four levers tagged correctly in all three regions. The probe reproduces the campaign's central
classifications - cash is a mirage, coupling is quantum, the tempo push is tempo - without human judgement.

**A sharper finding the probe surfaces.** The flat "cash = mirage" hides two different failure modes. The
tempo push is a true Bongaarts-Feeney mirage (tempo_share 0.83-0.94: it borrows timing and the adjusted TFR\*
never moves). An eroding cash transfer is *not* - its composition is 100% quantum (it does lift completed
family size while paid), but it reverts on withdrawal (survive 15-17%), a durability mirage. A durable parity
transfer that is believed permanent is a genuine quantum lever (survive 90-100%). The probe separates
"borrowed timing" from "withdrawn funding" - two things the single word "mirage" conflates.

## Pre-registered hypothesis fanout (E48, H435-H440)

Three arms: (i) validate the probe against the campaign's classified levers, (ii) apply it to reclassify
ambiguous verdicts, (iii) turn it into a policy-facing output. Each hypothesis carries its falsification bar
and an Occam gate (the probe must earn each rule against a simpler alternative).

### Arm (i) - validate the classifier

**H435 - the probe reproduces the campaign's recorded tempo/quantum verdicts.**
Run the probe on the canonical E19/E14 levers with a recorded `dynamical_verdict`, mapping
{tempo mirage, weak/stall} to {TEMPO-MIRAGE, QUANTUM-TRANSIENT} and {coupling escape, sustained recovery} to
QUANTUM-DURABLE.
Prediction: >= 90% agreement.
Bar: agreement >= 0.90 across the scored levers; every disagreement adjudicated on its trajectory (not waved
through). FAIL if < 0.80 or if any coupling lever reads TEMPO.
Occam gate: the four thresholds are fixed before scoring and not tuned to the outcome; a no-axis null (label
everything by the sign of `dTFR_end`) must score strictly worse.

**H436 - the composition axis is necessary, not decorative.**
A durability-only classifier (persistence alone) is tested against the two-axis rule on the pure tempo push.
Prediction: the tempo push leaves a durable `fec` residual (its equilibrium lowers the mean age), so
persistence reads high and a one-axis rule calls it QUANTUM - wrongly.
Bar: one-axis misclassifies `fTau` in >= 2 regions while two-axis tags it TEMPO in >= 7/8. Seed result:
one-axis wrong in **8/8** (persistence 0.74-1.00), two-axis TEMPO in **8/8** (tempo_share 0.83-0.94). CONFIRMED
in seeding; the confirmatory run re-checks under the frozen thresholds.
Occam gate: the second axis is justified only if it fixes a real error the first axis makes - which 8/8 does.
If a one-axis rule matched two-axis everywhere, the composition axis would be dropped as slop.

### Arm (ii) - reclassify ambiguous verdicts

**H437 - "cash mirage" splits into a Bongaarts-Feeney mirage and a durability mirage.**
Probe the eroding vs durable belief of each cash/parity lever.
Prediction: all cash/parity variants are quantum in composition (tempo_share < 0.40); the eroding variants
revert (survive_pct < 40) and the durable variants persist (survive_pct > 60). None is a true tempo mirage.
Bar: 0 cash/parity levers read tempo_share >= 0.40; eroding survive_pct < 40 and durable > 60 in >= 7/8
region-runs.
Occam gate: no new mechanism - only the durability envelope (`durable` flag) the model already carries. The
reclassification must change the *label*, not the model.

**H438 - full-catalogue reclassification screen.**
Apply the probe to the full E19/E14 lever catalogue and flag every lever whose probe class disagrees with its
recorded `dynamical_verdict`.
Prediction: a small number of borderline levers (channel = mixed, e.g. leave / housing) land in MIXED or flip
between TEMPO and QUANTUM-TRANSIENT.
Bar: each flagged disagreement is adjudicated by reading its `adjTFR_model` and `tempo_factor` trajectory and
either re-verdicted or explained; clean confirmation (0 disagreements) is an acceptable outcome, recorded as
such.
Occam gate: a disagreement re-verdicts a lever only if its trajectory decomposition unambiguously supports the
probe over the old label; otherwise the old label stands and the probe is noted as inconclusive there.

### Arm (iii) - policy-facing output

**H439 - the composition axis is a region-portable property of a lever; durability is position-dependent.**
Report the policy triple for each canonical lever across all eight regions.
Prediction: tempo_share (what *kind* of lever it is) is near-invariant across regions, while survive_pct (whether
it lasts *here*) varies with basin.
Bar: tempo_share range across 8 regions <= 0.15 for each canonical lever; survive_pct allowed to vary (that is
the intended position signal, not noise). Seed result: tempo_share ranges cash 0.00, coupling 0.00, cash-durable
0.01, tempo push 0.10 - all <= 0.15; survive_pct spreads 23-71% for the tempo push, 90-100% for durable levers.
CONFIRMED in seeding.
Occam gate: if tempo_share were as position-variable as survive_pct, the "what kind of lever" claim would
collapse and the probe would report only a per-region number, not a portable classification.

**H440 - the classification is robust to the one calibrated tempo constant.**
Re-run the probe under `kBF` in {0.6, 1.0} (the E40 damped value and the E41-adjudicated undamped value).
Prediction: no lever changes class; tempo_share moves monotonically with kBF but stays on its side of 0.60.
Bar: 0 class flips across the grid. Seed result: the tempo push stays TEMPO-MIRAGE at both kBF in Korea and
Germany; no flips. CONFIRMED in seeding.
Occam gate: if a lever's class flipped with kBF, the probe's verdict would be an artefact of the tempo
calibration rather than a property of the intervention, and the classifier would be withdrawn as unreliable.

## Limitations

- The probe reads the model's realized `dtau`, not a re-estimated `r_p` from noisy data, so it inherits the
  model's tempo term but sidesteps the Ni Bhrolchain critique that the Bongaarts-Feeney adjustment is fragile
  to age-schedule shape changes and short-run mean-age volatility
- The tempo push leaves a small durable `fec` residual because lowering the mean age at childbearing raises
  fecundability durably - this is real model structure, correctly handled by checking composition before
  durability, but it means "pure tempo" is never exactly 100% tempo in this model (peaks at ~94%)
- Classification thresholds (0.40 / 0.60) are pre-registered and defensible but not derived; the MIXED band is
  deliberately wide so borderline levers are flagged for adjudication rather than force-labelled
