# Project handoff package

Two independent research programmes, both investigating whether a batch-prepared beverage
can match or beat made-to-order preparation. Each is self-contained; they share no data.

**Status of everything in this package: modelling and design work. No bench measurements
have been made.** Every quantitative result is a first-principles calculation, a
literature-grounded calculation, or a task-time estimate. This is stated per claim in
`01_matcha_sonication/04_publication/matcha_claim_provenance.csv` and should be carried
into any downstream use.

---

## 01_matcha_sonication

**Question:** can probe sonication replace hand whisking for café matcha, and what does it
actually buy?

**Headline result — and it reverses the project's starting premise.** Sonication gives no
meaningful extraction uplift and therefore permits no reduction in powder dose. Matcha is
milled to 5–10 µm, so intraparticle equilibration takes ~0.07 s against ~25 min for a whole
leaf; the diffusion limit that ultrasound-assisted extraction exists to shorten has already
been removed by milling. What sonication does buy is complete deagglomeration (~450× stress
margin over agglomerate cohesive strength, against a whisk that sits *inside* that
distribution and leaves ~96% of clumps intact), near-zero thermal load, and cavitation that
strengthens as water cools — inverting the temperature dependence of every shear method.

Read in folder order:

| Folder | Contents |
|---|---|
| `01_core_analysis` | Energy regimes, the extraction-limit result, mechanism, efficacy assessment |
| `02_method_comparison` | Sonication vs. whisk / blender / rotor-stator; labor; texture and grit |
| `03_system_design` | Stirred keg → pulsed agitation → bottled concentrate → final spec |
| `04_publication` | Paper framing, figure arc, and the claim-by-claim provenance audit |

**Start with:** `04_publication/matcha_paper_framing.md` for the argument and what is
missing; `01_core_analysis/matcha_efficacy_assessment.md` for the physics.

**Final system (03):** cold sonication in-bottle → 750 mL glass → counter-integrated chill
→ shake → portioned pour spout. Modelled at CV ≈ 0.041 against ~0.18 for made-to-order
under service load. The highest-leverage single decision is the portioned pour spout, not
the sonicator.

**The one experiment that matters most:** laser-diffraction particle size distribution
across the four preparation methods. It converts the two central figures from predictions
into results. Nothing else on the list is close in value.

**Unmodelled throughout, and required before any food-contact use:** probe tip erosion into
an abrasive suspension (mass loss + ICP-MS for Ti/Al/V).

---

## 02_cryo_espresso

**Question:** can espresso be pulled in batch, chilled rapidly, and held without losing what
makes it fresh?

**Headline result:** oxygen exclusion, not chilling speed, governs retention. An LN₂
cryo-plate (1.5 s) and a plate heat exchanger (10 s) produce indistinguishable retention
curves; chilling rate explains ≤3.3% of predicted quality variance while hold atmosphere
dominates. The engineering effort belongs on headspace control, not on chilling hardware.
A second finding bounds the design space: any plate at −3 °C or below freezes the shot
solid within the plate.

| Folder | Contents |
|---|---|
| `01_feasibility` | Feasibility report, decision summary, pathway ranking |
| `02_thermal_physics` | Film cooling, freezing onset, boiling regimes, LN₂ consumption, frost |
| `03_chemistry_retention` | Volatile inventory, kinetics, retention and sensitivity analysis |
| `04_safety` | Nitrogen asphyxiation modelling, O₂ depletion, go/no-go conditions |
| `05_equipment_design` | Chiller sizing, BOM, system spec, fill-station layout |
| `06_test_program` | Staged gates, QC plan, assay panel, sampling schedule |
| `07_sensory_trial` | Trial design, tetrad/DA protocols, power analysis |

**Start with:** `01_feasibility/cryo_espresso_feasibility_report.md`.

**Read before any build:** `04_safety/safety_regulatory_constraint_memo.md`. The nitrogen
asphyxiation analysis is the gating constraint on the LN₂ pathway, and an unventilated room
breaches the OSHA 19.5% O₂ threshold within the study's own estimated boil-off range.

---

## Known open issues

A background reviewer raised ten findings against this corpus. Two touched deliverables and
**have been corrected in this package** (the copies here differ from the stored artifacts):

1. `matcha_efficacy_assessment.md` §1 quoted a Kolmogorov length of ~11 µm for the whisk
   case. That was a stale figure from a superseded temperature-independent model; the
   correct value at 80 °C is ~5 µm. The survival conclusion is unaffected — 45 µm
   agglomerates sit in the inertial subrange either way — and the text now explains why
   whisking is marginal in terms of applied stress rather than Kolmogorov scale.
2. `matcha_paper_framing.md` gave a claim breakdown that summed to 23 of 25, silently
   dropping the two literature-only claims. Corrected to 14 + 5 + 2 + 4 = 25.

The remaining eight are low-severity and concern figure-annotation overlap checks where the
rendered output was legible but the automated detector still reported flags. They do not
affect any numeric result. Several espresso-side artifacts also carry reviewer warnings
about citation provenance (specific author/DOI attributions that were not confirmed against
retrieved metadata in-session) and two internal inconsistencies in
`06_test_program/vessel_ledger.csv` (omits 24 conditional peroxide-value vessels; the
correct maximum of 117 appears in `qc_plan.md`) and `06_test_program/assay_panel.csv`
(row P8 `mL_consumed` is stale at 90 against a 105 mL fill). Verify citations independently
before publication.

---

## Reuse

Figures are 300 dpi PNG. Tabular data is CSV. Documents are Markdown. `build_scene.py`
(in `02_cryo_espresso/05_equipment_design`) generates the fill-station layout and is the
only executable file in the package.
