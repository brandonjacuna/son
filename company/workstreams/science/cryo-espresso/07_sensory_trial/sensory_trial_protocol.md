# Sensory Efficacy Trial — Cryo-Plate Espresso Batching

**Scope note.** This protocol tests the *corrected* configuration from Phase 0 — thermal break,
enclosed stainless flow path, food-contact surface held between −20 and +2 °C, active setpoint
control, duty-cycled cleaning, ≥2 ACH ventilation with low-level extract, O₂ monitoring. It does
**not** test the open-film device as originally drawn, which carries three independent safety
vetoes. All held arms are capped at ≤48 h at ≤4 °C under a HACCP plan; the sensory windows below
(4 h, 8 h) sit well inside that cap.

---

## 1. What this trial is actually for

The user asked to "prove the quality of product and impact of this process." Phase 0 has already
made the honest answer uncomfortable: **chilling rate explains at most 3.3 % of predicted quality
variance**, and the cryo-plate beats a plain 10 s plate heat exchanger by **at most 1.05 percentage
points** of marker retention anywhere in an 840-cell comparator matrix — against a credible band
~62 pp wide. Oxygen exclusion is worth **+40 pp** of 2-furfurylthiol retention at 24 h.

So the trial that matters is not "is batched coffee good?" It is: **is the cryogenic hardware
buying anything a €4,000 plate heat exchanger does not already buy?** Phase 0 predicts *no*. A
trial designed to detect a difference will fail to find one and prove nothing. The trial must be
designed so that *finding nothing* is a **positive, publishable, capital-decision-grade result** —
which means the primary contrast is an **equivalence test**, not a difference test.

Anyone who runs cryo-batched-vs-four-hour-thermos and reports a win has proved only that hot
holding destroys coffee. That comparison is retained here **solely as a panel-validity gate**.

---

## 2. Arm set

Six arms (`trial_arms.csv`). All batched arms are held at 4 °C and evaluated at 4 h, with an 8 h
sub-arm to locate the service window.

| Code | Arm | Role |
|---|---|---|
| `FRESH` | Fresh shot, served <30 s | Upper anchor; defines scale ceiling |
| `CRYO` | Cryo-plate (corrected config) + inert flush | Test article |
| `PHE` | Closed plate HX + inert flush | **Active comparator — the decision hinges here** |
| `PHE_AIR` | Closed plate HX, ambient air headspace | Isolates the oxygen effect |
| `AMB` | Passive ambient cooling + inert flush | Chilling-rate floor |
| `HOTHOLD` | 80 °C thermos, 4 h | **Positive control only** |

`AMB` is the arm most people leave out and it is the one that closes the argument. If passive
cooling under inert flush is also equivalent to `CRYO`, then the entire chilling-rate axis is
inert and no chiller capital of any kind is justified — the money goes to gas.

## 3. Hypotheses

Full matrix in `hypotheses_matrix.csv`. The load-bearing ones:

1. **`CRYO` vs `PHE`, both inert, 4 °C, 4 h — EQUIVALENCE.** H₀: d′ ≥ 1.0. H₁: d′ < 1.0. Declaring equivalence kills the cryo capital request. This is the primary endpoint.
2. **`PHE`+inert vs `PHE`+air — DIFFERENCE, one-sided.** Expected large. If this is *not* significant the panel is insensitive to the one variable Phase 0 says dominates, and the equivalence result in (1) becomes uninterpretable. It is a co-primary and a sensitivity check in one.
3. **`FRESH` vs `HOTHOLD` — GATE.** Must clear p < 0.01 or nothing else is analysed.
4. **Treatment × matrix interaction.** Determines commercial scope: parity in milk is plausible where parity neat is not.

Analysis order is fixed in advance: gate (3) → co-primary (2) → primary (1) → secondary. This
ordering is a gatekeeping procedure and controls family-wise error for the confirmatory family
without further adjustment.

---

## 4. Discrimination power — the trial's cost driver

Psychometric functions computed under the Thurstonian model and validated against 2 M-draw Monte
Carlo (agreement to 3–4 decimals). Sample sizes use the **exact binomial**, not the normal
approximation. Tables: `sample_size_difference.csv`, `sample_size_similarity.csv`.

**Difference mode** (α = 0.05, one-sided):

| d′ | p_c triangle | n (80 %) | n (90 %) | p_c tetrad | n (80 %) | n (90 %) |
|---|---|---|---|---|---|---|
| 0.5 | 0.356 | 2825 | 3881 | 0.378 | 752 | 1029 |
| 1.0 | 0.418 | 215 | 296 | 0.494 | **65** | 89 |
| 1.5 | 0.507 | 57 | 78 | 0.641 | 20 | 25 |
| 2.0 | 0.605 | 23 | 34 | 0.778 | 9 | 13 |

The tetrad has the same 1/3 guessing rate but a steeper psychometric function, and needs roughly
**one third the assessments** of the triangle at matched d′. **Use the tetrad.** There is no
defensible reason to run a triangle test here; it triples the cost for the same information.

**Similarity/equivalence mode** — this is the number that decides the trial's affordability. To
conclude d′ < 1.0 at 80 % power:

| β-risk | truth d′ = 0 (Phase 0's expectation) | truth d′ = 0.5 (conservative) |
|---|---|---|
| 0.05 | 68 tetrads | 123 tetrads |
| 0.10 | 49 | 93 |
| 0.20 | 35 | 63 |

**State this plainly: equivalence is not free, and the cost explodes if the true difference is not
exactly zero.** At the conservative planning assumption the tetrad needs 123 assessments where the
same claim by triangle test needs 402. Under replication, responses from one assessor are
correlated; with an over-dispersion γ ≈ 0.20 (`replicate_overdispersion.csv`), 4 replicates per
assessor inflate the required assessment count by a factor of 1.6.

**Recommended plan** (`panel_size_plan.csv`), tetrad, β-risk 0.10, conservative d′ = 0.5 truth:
**149 inflated assessments = 38 assessors × 4 replicates.** At β-risk 0.05 it becomes 50 assessors
× 4.

**Feasibility verdict — read this before budgeting.** A café cannot run 38–50 trained assessors ×
4 replicates in-house. Three ways out, in order of preference:

1. **Central-location test (CLT), recommended.** Recruit 60–80 espresso drinkers (not trained
   assessors) at a single site over 2–3 days; each performs 2 tetrads. 120–160 assessments covers
   β-risk 0.05 at the conservative assumption. Tetrad requires no training — only "group these
   four into two pairs" — which is exactly why it suits a naive-consumer CLT. Cost is roughly one
   week of a technician's time plus incentives.
2. **Reduce the arm set.** Drop `AMB` and the 8 h sub-arms from the discrimination phase; run
   `CRYO` vs `PHE` only, in one matrix (milk, if the commercial case is milk-led). Roughly halves
   the panel-hours.
3. **Accept β-risk 0.20 and say so.** 76 assessments = 38 assessors × 2 replicates. This is an
   honest budget trial, but the equivalence claim is materially weaker and a skeptic is entitled
   to say so. Do not report it as "no difference."

Do **not** run an underpowered difference test and report "no significant difference." That is the
failure mode this whole design exists to prevent.

---

## 5. Trained-panel descriptive analysis

**Lexicon** — 20 attributes across appearance, aroma, taste, mouthfeel, aftertaste
(`attribute_lexicon.csv`), each with definition, 0–10 line-scale anchors, and a physical reference
standard. The Phase-0-critical ones: crema volume and persistence, CO₂ prickle (only ~25 % of
dissolved CO₂ survives transit and the liquid will not re-effervesce), sediment visibility (fines
>20 µm settle within ~1.2 h — inside the service hour), and oxidised/cardboard, which is the
primary marker for the oxygen contrast.

**Panel.** 14 assessors (recruit 16 for attrition), 3 replicates. Power to detect a 1.0-point
pairwise difference on the 0–10 scale, residual SD 1.2, Bonferroni over 15 pairs: 0.80 at n = 14;
0.71 at n = 12; 0.60 at n = 10. **12 is not enough** — the commonly cited "10–12 assessors" is
below the bar for a 6-arm design.

**Training.** 40 h over 5 weeks: 8 h lexicon generation by consensus on the real product set, 16 h
reference-standard anchoring and scale use, 8 h matrix-specific practice (milk and iced dull and
shift attributes), 8 h performance qualification. Qualify each assessor on discrimination (F-test
on blind duplicates), repeatability (assessor × replicate MSE), and agreement with panel consensus;
retrain or drop anyone failing two of three.

**Model.** Mixed model per attribute:

```
y ~ treatment + matrix + treatment:matrix + (1|assessor) + (1|session)
      + (1|assessor:treatment) + (1|assessor:matrix)
```

Fixed: treatment, matrix, interaction. Random: assessor, session, assessor × treatment (the scale-
usage interaction that inflates Type I error if omitted). REML, Kenward–Roger denominator df.
Multiple comparisons: Tukey HSD within attribute across treatments; across the 20 attributes,
Benjamini–Hochberg FDR at 0.05 for the exploratory family, while the four confirmatory contrasts
in §3 keep their pre-registered gatekeeping order. Report effect sizes with CIs, not just p-values
— for the equivalence framing a CI that sits inside the equivalence band is the result.

**Consumer acceptance.** n = 120 completed (recruit 140), screener: drinks espresso-based beverages
≥3×/week, no dairy allergy, not employed in coffee trade or market research. 9-point hedonic for
overall liking, plus liking of aroma, flavour, mouthfeel, aftertaste. **5-point JAR** on the three
attributes most at risk: strength, bitterness, sourness. **Penalty analysis** (mean drop per JAR
category × % respondents in category); flag any attribute where >20 % of consumers are off-JAR and
the mean drop exceeds 1.0 hedonic point. Because the commercial use is milk-led, run **preference
on the milk matrix specifically** — paired preference `CRYO` vs `PHE` in flat white, with a
no-preference option and a Thurstonian analysis, and treat the milk result as the commercially
binding one.

**Temporal.** TDS (temporal dominance of sensations) on neat espresso and flat white, 90 s capture,
attribute set restricted to 8 terms (bitter, sour, sweet, roasty, stale/cardboard, astringent,
body, metallic). Staling manifests in the finish before the attack, so an attack-only static rating
will miss it. Supplement with time-intensity on **lingering bitterness** and **stale finish** as a
continuous trace. Analyse via dominance-rate curves with the chance and significance bands, and
compare arms on area-under-curve for the stale-finish attribute.

---

## 6. Serving and blinding

**Matrices.** Every arm is served in three matrices: neat espresso (30 mL), 6 oz flat white
(30 mL espresso + 150 mL steamed whole milk at 60 °C), iced americano (30 mL espresso + 150 mL
water over 100 g ice). A difference invisible in milk may be obvious neat; the commercial case may
only require parity in milk, so the matrix × treatment interaction is a primary endpoint, not a
nuisance term.

**Temperature matching — the easiest thing to botch.** A cold-batched shot reheated is not
thermally or chemically identical to a fresh one, and if serving temperature differs by more than
~2 °C the panel discriminates on temperature rather than on flavour, which invalidates every
contrast. Rules:

- All hot-served samples arrive in the booth at **65 ± 1.5 °C** neat, **62 ± 1.5 °C** in milk, verified per cup with a fast thermocouple; any cup outside band is discarded, not served.
- Batched arms are brought up by **inline sous-vide/thermoblock reheat to 65 °C with ≤20 s dwell**, never by microwave (hot-spotting) and never by holding at temperature.
- `FRESH` is pulled directly into a **pre-warmed cup at 65 °C** and rested to the same 20 s dwell as the reheated arms, so every arm shares an identical thermal history in the final 20 s. `HOTHOLD` is decanted from the thermos and trimmed to the same band.
- Iced arms: all served at **4 ± 1 °C** with ice mass matched to ±5 g and served within 60 s of build to equalise melt dilution.
- Booth ambient 22 ± 1 °C, cups on a warming plate held at serving temperature until the moment of presentation.

**Dilution matching.** All arms brewed from one homogenised bulk extraction per session where
possible, or from a single grind/dose/yield recipe (18.0 g dose, 36.0 g yield, ±0.3 g) with TDS
measured by refractometer per batch. Any arm deviating >2 % relative TDS from the session mean is
re-made. Frost dilution is negligible (−0.14 % relative, >10× below the ~5 % strength JND), so it
needs no correction — but reheat evaporation does, so reheat is closed-vessel.

**Crema — the unblinding problem, addressed directly.** Phase 0 is unambiguous: crema cannot
survive any version of this process and must be regenerated at service. Regenerated crema does not
match native crema in volume or persistence, so crema is an **obvious visual cue that would unblind
the entire panel**. Two-tier solution:

- **Tier 1, blinded discrimination and hedonics (primary).** Serve every arm — `FRESH` included — in **opaque black lidded cups with black straws**, under **red/amber booth lighting** (sodium or filtered LED, ~590 nm), crema **removed from all arms** by a standardised 10 s skim. This equalises the visual channel completely. **The validity cost is real and must be stated in the report:** removing crema from the fresh reference removes part of what makes a fresh shot good — mouthfeel contribution, aroma retention under the foam layer, and visual pleasure. Tier-1 results therefore answer "do these liquids differ in flavour?", not "do these drinks differ as products."
- **Tier 2, unblinded appearance panel (secondary).** A separate short session in clear glassware under full-spectrum 6500 K light, crema intact as it would be served, rating crema volume/persistence, sediment visibility and colour only. No flavour attributes. This is where the honest appearance penalty of batching is quantified.

Report both tiers. Tier 1 alone overstates parity; Tier 2 alone confounds appearance with flavour.

**Codes and order.** Three-digit blind codes drawn without replacement from 100–999, unique per
arm × matrix × replicate so no code recurs across sessions (54 codes in the DA design, 800 rows in
the tetrad design). Presentation order follows a **Williams design** for 6 treatments — verified
position-balanced (every arm has mean position exactly 3.50 in every session) and carryover-
balanced (all 30 ordered pairs appear exactly once). Each of the 6 sequences is used by 2 of the
12 assessors per session; sequence-to-assessor assignment and matrix-block order are randomised
(seed 4711, reproducible). Files: `serving_design_DA.csv`, `serving_design_tetrad.csv`.

**Palate cleansing.** 60 s enforced inter-sample interval; room-temperature filtered water plus
unsalted water cracker between samples, 90 s and a mandatory second cracker between milk samples
(milk fat coats and carries over hardest). Expectorate; no swallowing except in the aftertaste
sessions, which are scheduled last and limited to 6 samples/session on caffeine grounds
(6 × 30 mL espresso ≈ 380 mg caffeine — do not exceed).

**Booths.** ISO 8589-compliant: individual positive-pressure booths, odour-free HVAC, no ambient
coffee aroma (critical — a café's own aroma load will mask the orthonasal contrasts; run sessions
before opening or in an off-site space), 22 ± 1 °C, 50–60 % RH, digital data capture at the booth,
no communication between assessors. Sessions ≤45 min, max 2 sessions/day, ≥90 min apart.
