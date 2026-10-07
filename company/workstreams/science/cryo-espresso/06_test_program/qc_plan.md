# QC PLAN AND PROCESS CONTROLS
## Cryo-plate espresso batching — analytical track
Designed for the CORRECTED configuration (thermal break, enclosed stainless flow path,
food-contact surface held between -20 and +2 degC, active control), NOT the original drawing.

---

## 0. WHAT THIS PANEL IS FOR

Phase 0 established that chilling RATE explains at most 3.3% of predicted quality variance,
and that the cryo-plate beats a 10 s plate heat exchanger by AT MOST 1.05 percentage points of
marker retention anywhere in an 840-cell comparator matrix. Oxygen exclusion is worth +40 pp of
2-furfurylthiol retention at 24 h.

The power arithmetic follows directly and dictates the whole design:

| effect under test | size | power at n=3 batches/arm |
|---|---|---|
| inert flush vs air (oxygen) | +40 pp | **0.98** |
| cryo-plate vs PHE (chilling rate) | 1.05 pp | **0.04** |

At n=3 the smallest equivalence margin this trial can certify is ~18 pp (CV 15%); certifying
1.05 pp would need n in the thousands. **This trial is therefore NOT powered to detect the
chilling-rate effect and must not be reported as having tested it.** It is powered to detect the
oxygen effect decisively, and to bound the chilling effect as "smaller than the analytical noise
floor." The 2x2 arm structure (chill method x atmosphere) exists so the oxygen main effect is
estimated with the chilling factor blocked out, and so a chill x atmosphere interaction would be
visible if one existed.

Report the cryo-vs-PHE contrast as an equivalence result with its true margin, never as a
non-significant difference test.

---

## 1. THE PRIMARY ENDPOINT: OXIDATION INDEX

Oxidation index = (total thiol - free thiol) / total thiol, per analyte.

- **Free thiol (V2)** — aliquot drawn under argon, EDTA present, no reductant.
- **Total thiol (V3)** — parallel aliquot, 1 mM TCEP, 30 min at 25 degC under argon, which
  reduces difurfuryl disulfide and dimethyl disulfide back to the parent thiols.
- **Orthogonal confirmation** — direct DFDS (m/z 81, quals 162/53) and DMDS (m/z 94, quals
  79/45) peak areas from the V1 run.

**Why this is the single most important measurement.** Absolute thiol concentration falls for
three different reasons that a single number cannot separate: it was stripped during transit, it
oxidised to disulfide, or it was never extracted in the first place. The ratio responds to
OXYGEN EXPOSURE specifically rather than to elapsed time generally. A sample that is simply old
shows falling absolute thiol with a low index; a sample whose inert flush failed shows a high
index early, at a timepoint where age alone cannot explain it.

Diagnostic table:

| absolute free thiol | oxidation index | interpretation |
|---|---|---|
| low | high | **flush failed / seal leaking** — check P2 headspace O2 |
| low | low | product is simply old, or was stripped in transit |
| low | low, and total thiol also low at t=0 | extraction/dose problem — check N3 caffeine |
| high | low | intact, well-flushed sample |

---

## 2. VOLATILE METHOD — THE TWO TRAPS

**Trap 1: hot incubation.** The intuitive move is to incubate at 40-60 degC for sensitivity.
Do not. A hot incubation generates Maillard and Strecker artefacts in situ — it makes furfural,
methylfurfural and pyrazines that were not in the sample — and it re-partitions the very
analytes under measurement, so the headspace you sample is not the headspace the product has.
Worse for this specific study, warmth accelerates thiol oxidation during the 50 min the vial
sits on the tray, which corrupts the primary endpoint. **Extract at 30 degC.** Recover the lost
sensitivity through fibre choice, salt, a 2 cm fibre and MS/MS rather than through heat.

**Trap 2: fibre choice.** Use **DVB/CAR/PDMS 50/30 um, 2 cm**, not CAR/PDMS. CAR/PDMS has the
better carbon micropore affinity for methanethiol and the C2-C4 volatiles specifically, and if
methanethiol were the only target it would win. But the panel spans methanethiol (RI 705) to
sotolon and difurfuryl disulfide (RI ~2210), and CAR/PDMS retains the late, larger, less volatile
analytes poorly. The triple phase covers the whole range in one extraction, which matters here
because vessel volume is the binding constraint — a second extraction on a second fibre would
cost a second aliquot. Run a CAR/PDMS cross-check during method validation only, on the
methanethiol/DMDS pair, to confirm the triple phase is not underselling the light sulfur window.

**Conditions to hand to the lab.**

| parameter | setting |
|---|---|
| sample | 10.0 mL into a 20 mL amber vial |
| salt | 3.0 g NaCl (pre-weighed into vial, ~30% w/v — salts out thiols, suppresses enzymatic and radical chemistry) |
| acid | H3PO4 to pH 2.5 (fixes protonation state, halts CGA-lactone hydrolysis in the shared aliquot) |
| chelator | 50 uL 1 mM EDTA (metal-catalysed thiol oxidation is the dominant artefact route — non-negotiable) |
| headspace | 10 mL, i.e. 1:1, identical in every vial |
| capping | crimp under an argon stream; PTFE/silicone septa, single-pierce |
| equilibration | 20 min at 30 degC, 250 rpm agitation |
| extraction | 30 min at 30 degC |
| desorption | 250 degC, 3 min, splitless, 0.75 mm SPME liner |
| fibre conditioning | 5 min at 260 degC between samples; blank injection every 10 runs |
| column | DB-WAX UI 30 m x 0.25 mm x 0.25 um (polar — resolves thiols from the hydrocarbon background; UI deactivation matters for sulfur peak shape) |
| carrier | helium 1.2 mL/min constant flow |
| oven | 35 degC (4 min), 5 degC/min to 150 degC, 8 degC/min to 240 degC, hold 12 min |
| MS | EI 70 eV, source 230 degC, full scan m/z 33-300 for identification PLUS timed SIM in 5 windows for quantitation |
| S-analytes | MRM on a triple quadrupole where available — the ng/L thiol targets against this matrix are not reliably quantifiable in single-quad SIM |

**The ng/L-against-a-huge-matrix problem.** 2-Furfurylthiol has an odour threshold near 0.01
ug/L and sits in a matrix containing furfural and furfuryl alcohol at four to five orders of
magnitude higher concentration, eluting nearby on a WAX phase. Three mitigations, in order of
preference: (1) MS/MS rather than SIM, which buys selectivity that no chromatographic tuning
will; (2) standard addition on a pooled matrix for the calibration, because a solvent-based
calibration curve will be wrong — SPME response is matrix-suppressed and the suppression is not
constant across arms if TDS differs; (3) deuterated FFT-d2 co-eluting, which corrects fibre
competition and any oxidation occurring between capping and extraction.

**Derivatisation (V5) is a contingency, not a default.** If validation cannot reach 5 ng/L for
FFT, derivatise with PFBBr to the PFB-thioether and detect by GC-NCI-MS, which reaches ~1 ng/L.
Two cautions the contract lab must acknowledge in writing: PFBBr derivatisation measures FREE
thiol only, and the alkaline conditions it requires actively drive thiol-to-disulfide conversion
during the reaction. It therefore cannot replace the V2/V3 pair — it can only substitute for V2,
and must be run with a matched TCEP-reduced arm to preserve the index.

---

## 3. DISSOLVED OXYGEN — THE ASSAY THAT VALIDATES THE PACKAGING CLAIM

This is the assay whose difficulty is entirely in the sampling, not in the measurement.

**Excluded methods and why.** A Clark electrode consumes oxygen as it measures and needs the
sample decanted into a cell. Winkler titration needs a filled, air-free bottle and multiple
reagent additions. Both require transferring an anoxic liquid through air to reach the sensor,
and the transfer entrains more oxygen than the sample contains — at <1% headspace O2 the
measurement artefact exceeds the quantity being measured. Any method requiring decanting is
disqualified on principle here.

**Specified method.** A luminescent optical oxygen sensor spot (PSt3-class, 0-100% air
saturation) is bonded to the INNER wall of each vessel before filling, and interrogated through
the glass wall by a fibre-optic polymer probe held against the outside. Nothing is opened,
nothing is removed, no air is admitted.

Consequences worth stating plainly, because they reshape the trial:

1. DO stops being a single destructive endpoint and becomes a **continuous ingress trajectory**
   measured on every vessel at every timepoint, including the vessels reserved for later
   destructive sampling.
2. A second spot in the headspace (P2) gives headspace O2 on the same read-out. The pair
   separates a bad flush at seal (both high from t=0) from closure ingress over time (headspace
   rises first, dissolved follows).
3. Every vessel carries its own oxygen provenance, so a vessel that leaked can be excluded from
   the sensory arm on evidence rather than suspicion.

Two-point calibration per batch of spots: 0% in sodium sulfite solution, 100% in air-saturated
water, temperature-compensated from a co-located Pt100. Verify the calibration on three sacrificial
vessels per production lot of spots.

---

## 4. PROCESS CONTROLS — SEPARATING A FAILED BATCH FROM A FAILED TREATMENT

Every batch must clear these gates BEFORE its vessels are admitted to the study. A batch failing
any gate is discarded whole and re-brewed; it never enters the dataset, and it never reaches the
sensory panel. This is what the 15% shot contingency is for.

| control | measurement | admit if | rationale |
|---|---|---|---|
| Dose | balance, 0.01 g | 18.0 +/- 0.2 g | extraction consistency |
| Shot time | timer from pump start | 27 +/- 3 s | channelling detector |
| Beverage mass | balance | 40 +/- 1.0 g | ratio control |
| TDS (N7) | refractometer, filtered, 20 degC, x0.85 | 8.0-11.0%, and within 0.5% absolute of session median | extraction consistency |
| Extraction yield (N8) | computed | 18-22%, within 1.0% absolute of session median | extraction consistency |
| Caffeine (N3) | HPLC-DAD | within 8% of session median across arms | **the arm-blind check — caffeine is oxidatively and thermally inert over 48 h, so any between-arm difference is a brewing artefact, not a treatment effect** |
| Plate surface temperature | logged thermocouple, 1 Hz, whole run | within -20 to +2 degC for 100% of contact time; NO excursion below -3 degC | below -3 degC the shot freezes solid within the plate length (film Fourier number ~8, so the liquid takes the wall temperature almost instantly) |
| Chill-exit temperature | in-line probe at outlet | +2 to +4 degC, the useful setpoint window | the window is only ~5 K wide and passive conduction cannot hold it |
| Active control health | controller log | no loss-of-control event >5 s | passive choke free-falls to -130 degC at idle |
| Headspace O2 at seal (P2) | optical spot, read at t=0 before storage | inert arms <1.0%; air arms 19-21% | **the treatment-delivery check — an inert arm above 1% did not receive its treatment** |
| Cold-surface condensation | visual + surface temp | no surface below 90.2 K anywhere accessible | below 90.2 K the rig condenses oxygen-enriched liquid air onto a counter bearing coffee oil, sugar and paper |
| Ventilation | O2 room monitor | >=19.5% O2, >=2 ACH running | LN2 asphyxiation control |
| Clean cycle | duty-cycle log | food-contact path cleaned and sanitised within the 4 h clock | an open permanently-cold surface cannot meet this — the duty cycle is what makes it possible |

**Go/no-go decision rule.** Admit a batch only if every row above passes. Record the reason for
every rejection; a pattern of rejections concentrated in one arm is itself a finding about the
device, and must be reported even though those batches are excluded from the efficacy analysis.

---

## 5. REPLICATE STRUCTURE — KEEP THESE DISTINCT

- **Batch (biological) replicates: n = 3.** Three independent brew sessions on three separate
  days, each with its own grind calibration, its own device warm-up and its own flush. This is
  the replicate that carries the error term for all treatment inference. n = 3 is the unit of
  analysis; the statistical model treats batch as a random effect.
- **Analytical replicates: n = 2-3.** Duplicate or triplicate extractions/injections from a
  single opened vessel. These estimate instrument precision ONLY. **They must never be pooled
  with batch replicates or used to inflate degrees of freedom** — doing so is pseudoreplication
  and would make the trial appear to detect differences it cannot.
- Report both variance components separately: if analytical CV is 8% and total CV is 15%, the
  batch-to-batch term dominates and more brewing days, not more injections, is the way to
  improve the trial.

---

## 6. DESTRUCTIVE SAMPLING AND THE VESSEL LEDGER

Each vessel, once opened, is consumed: its atmosphere is destroyed, so it cannot be resealed and
revisited. **One vessel is therefore required per arm, per timepoint, per batch replicate.**
This is the single constraint that drives the coffee budget.

The one exception is the optical oxygen and CO2 spots (P1, P2, P3-primary), which are read
through the glass without opening. Those run on every vessel at every timepoint, including
vessels not yet due for destructive sampling.

| item | vessels |
|---|---|
| 4 arms x 6 timepoints (0,2,6,12,24,48 h) x 3 batches | 72 |
| Fresh unchilled reference, t=0, 3 batches | 3 |
| Pooled QC reservoir | 3 |
| Matrix blanks (water through each device path) | 3 |
| **CORE TOTAL (<= 48 h)** | **81** |
| Conditional 72 h arm — ONLY under a variance | 12 |
| Conditional peroxide value (P8), t=0 and t=48 | 24 |
| **MAXIMUM TOTAL** | **117** |

Vessel format: 125 mL amber glass serum bottle, 105 mL fill, 20 mL headspace (16%), butyl rubber
septum, crimp seal. **Headspace fraction must be identical across all arms** — an unequal
headspace changes the oxygen inventory available to the product and would confound the very
comparison the trial exists to make.

Routine destructive draw is 91 mL of the 105 mL fill, leaving 14 mL of reserve for repeat
injections and archive.

**Shot budget.**

| item | shots |
|---|---|
| Liquid into vessels (105 mL fill / 40 g shot) | 228 |
| Device and line hold-up purge (150 mL per arm per batch) | 45 |
| Grinder warm-up and dial-in (6 per session x 3) | 18 |
| In-line process-control shots | 36 |
| Subtotal, core | 304 |
| Contingency at 15% (failed go/no-go batches, reruns) | 45 |
| **CORE TOTAL** | **349** |
| Conditional 72 h arm | 32 |
| Conditional peroxide value | 63 |
| **MAXIMUM TOTAL** | **444** |

At 18 g dose: **6.3 kg** of roasted coffee for the core design, **8.0 kg** if both conditional
arms run. Single-origin, single roast lot, single grind calibration, rested 7-14 days
post-roast, with the same lot reserved for the sensory track.

---

## 7. THE 48 HOUR CEILING — AN EXPLICIT CONSTRAINT ON THE SCHEDULE

The core schedule stops at 48 h. This is not an analytical choice.

Espresso at pH ~5.15 and aw ~0.99 held under inert gas or vacuum is reduced-oxygen packaging of
a temperature-controlled-for-safety food with no intrinsic barrier and no lethality step.
Non-proteolytic *C. botulinum* grows at 3.0-3.3 degC — below normal cafe refrigeration. The
realistic ceiling is **48 h at <=4 degC, WITH a HACCP plan and almost certainly a variance**.

The 72 h timepoint is therefore specified but held in reserve. It runs ONLY if the safety track
obtains a written variance waiving the 48 h ceiling. If no variance is granted, the 72 h vessels
are never filled, and no 72 h claim may be made from this trial. The analytical track must not
generate 72 h data that a product claim could later be hung on without that variance in hand.

Note independently that Phase 0 puts practical shelf life for fresh-shot character at 6-12 h,
well inside the safety ceiling. The 24 and 48 h timepoints exist to characterise decay, not
because the product is expected to be good there.

---

## 8. SAMPLE HANDLING BETWEEN COLLECTION AND ANALYSIS

- Vessels stored upright at 3.0 +/- 0.5 degC in a logged, alarmed refrigerator, in the dark.
- On opening: pierce the septum with the argon-purged sampling needle; do not remove the crimp.
  Draw all aliquots through the septum under a gentle argon counter-flow.
- **Thiol aliquots (V1/V2/V3): quench immediately.** EDTA and acid go into the vial before the
  sample. Cap under argon. On the autosampler tray within 30 min, tray held at 10 degC. No
  sample waits more than 4 h at tray temperature.
- **Lactone aliquot (N2): acidify to pH 2.5-3.0 at the moment of opening.** CGA lactones
  hydrolyse back to CQAs at a pH- and temperature-dependent rate, so an un-quenched aliquot
  reports a handling artefact that is indistinguishable from a storage effect. A 3-CQL spiked
  handling control runs in every sequence to quantify residual handling hydrolysis; report
  lactones as a lactone:CQA ratio, never as an absolute.
- HPLC aliquots: 0.45 um PVDF, -80 degC, analysed within 14 days.
- Microbiology (M1): aseptic draw, plated within 1 h, never frozen.
- Never freeze a sample destined for volatile analysis — ice crystal growth ruptures the
  colloid and shifts the headspace partition irreversibly.

---

## 9. BLINDING AND RUN ORDER

- **Analyst blinding.** Vessels carry a random 4-digit code applied by a coordinator who
  performs no analysis. The code maps to arm and timepoint in a sealed key held outside the lab.
  Analysts see only the code.
- Blinding is imperfect where it cannot be helped: an analyst reading a headspace O2 spot sees
  the atmosphere directly. Accept it, and assign O2 spot reading to a different person from
  the one integrating the thiol chromatograms.
- **Randomised run order.** Randomise injection order across arm and timepoint within each
  analytical batch, and re-randomise per sequence. This is what de-confounds instrument drift
  from treatment — a sequence run in arm order would render a drifting fibre or a fouling source
  perfectly collinear with the treatment effect and produce a completely spurious result.
- Block by batch replicate so that a whole brew day cannot align with a whole instrument day.
- **Integration is blinded and locked.** Integration parameters are fixed during method
  validation and applied unchanged; manual re-integration requires a second analyst's
  countersignature and a logged reason.

---

## 10. QC SAMPLES AND ACCEPTANCE CRITERIA

| QC | frequency | acceptance |
|---|---|---|
| Solvent/fibre blank | every 10 injections and after any high-concentration sample | target analytes < LOQ; carryover <1% of preceding sample |
| Matrix blank (water through device) | 1 per device per batch | no target analyte above LOQ; catches septum, tubing and phthalate contributions |
| Pooled QC (aliquots of one homogenised pool) | every 10 injections | RSD across the full sequence <=15% for major analytes, <=25% for thiols |
| Matrix spike (mid-level, all targets) | 1 per sequence | recovery 70-130%, thiols 60-140% |
| 3-CQL handling control | every HPLC sequence | quantifies handling hydrolysis; flag if >5% converts |
| Calibration | standard addition on pooled matrix, 6 levels | r2 >= 0.99; back-calculated levels within 15% (20% at LOQ) |
| CCV (mid-level check) | start, every 10, end | within 15% of nominal |
| ISTD response | every injection | within 50-150% of sequence median, else re-inject |
| Optical O2 spot check | 3 sacrificial vessels per spot lot | within 0.05 mg/L of a Winkler reference at 0% and at saturation |
| System suitability | start of each sequence | FFT S/N >= 10 at LOQ; DB-WAX resolution of FFT from furfuryl alcohol >= 1.5 |

**Sequence rejection.** A sequence failing pooled-QC RSD or bracketing CCV is rejected whole and
re-run from the archived aliquots; individual samples are not cherry-picked out of a failed
sequence.

**Study-level acceptance.** The trial is analysable if >=80% of planned vessels clear the
process-control gates, all three batch replicates are present for every arm, and the pooled QC
RSD criterion is met in >=90% of sequences.

---

## 11. WHAT THE ANALYTICAL TRACK OWES THE SENSORY TRACK

1. **A batch-admission verdict before any tasting.** Headspace O2 at seal, extraction-consistency
   markers, and APC are reported to the sensory coordinator as a single go/no-go per vessel. A
   vessel that failed its flush must never reach a panellist, because it would be scored as a
   treatment effect when it is a delivery failure.
2. **The oxidation index as the mechanistic covariate.** When the panel does or does not
   discriminate, this index is the number that explains why. Sensory discrimination should be
   modelled against it, not against elapsed time.
3. **Two known confounds the sensory design must neutralise.** Crema cannot survive any version
   of this process and must be regenerated at service, identically across all arms including the
   comparator — otherwise the panel discriminates on foam, not flavour. And only ~25% of
   dissolved CO2 survives transit, with the collected liquid undersaturated so it will not
   re-effervesce; the CO2 measurements (P3) give the dose that regeneration must add back, and
   that dose must be matched across arms.
4. **A colour warning.** If dE*ab exceeds 2 between arms at any timepoint, the difference is
   visible and the panel must use opaque cups and red lighting.
5. **A sediment warning.** Fines >20 um settle within ~1.2 h. Every arm, including the
   comparator, must be re-agitated by an identical documented protocol immediately before
   pouring, or sediment becomes a visible cue.
