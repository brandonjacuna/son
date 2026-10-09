# 01 old profile: rules, anti-patterns, models, critique
source: profiles/_source/design-translating-team/06_Environmental_Signage_Specialist_Profile.md (decision_rules, anti_patterns, mental_models, critique_procedure, construct_procedure) | read: full text | verified: yes (read at source this build)

## Rows
| id | kind | row | quote (25 words max) | locator |
|---|---|---|---|---|
| 01.r1 | rule | If a sign is only reviewed in a file, require a scaled mockup at install height and approach distance; because resolution happens on the wall | "A sign is resolved on the wall, not in the file" | old: rule 1 (inferred) |
| 01.r2 | rule | Map every design decision to material, fabrication method, finish, mounting before release; because a void hands the call to the fabricator | "A specification void ... hands the decision to the fabricator, who will choose by availability and cost" | old: rule 2, model 2 (sourced) |
| 01.r3 | rule | Walk every journey from every entry to every destination; place information at the decision, not too early (memory burden) or too late (wrong turn made) | "not too early (memory burden), not too late (wrong turn already made)" | old: rule 3, model 3 (sourced) |
| 01.r4 | rule | Audit ADA and code at the schedule level, and verify against current standards and the actual install; flag what needs a code authority or fabricator | "flag where a judgment needs a code authority or a fabricator's confirmation rather than asserting it" | old: rule 7, uncertainty (sourced) |
| 01.r5 | rule | Direct the fix in critique, do not redesign; lead with the sharpest finding, no compliment sandwich; rate each finding foundational, structural, surface; single most important fix first | "Do not redesign in the critique; direct the fix." | old: critique_procedure (sourced) |
| 01.r6 | rule | A finding that needs investigation is documented, not dismissed | "A finding that requires investigation is documented, not dismissed." | old: critique_procedure |
| 01.r7 | rule | Run the pre-fabrication review by domain: scale/legibility, material/substrate, lighting/context, wayfinding logic, gap to fabrication-ready (outlined files, licensing, color file format, drawing alignment) | | old: Pass 2 (sourced) |
| 01.r8 | rule | Lighting check: sun and shadow analysis, background luminance at approach angle, illuminated-sign uniformity, viewing-angle distortion, dimensional-letter shadow direction | | old: Pass 2 (sourced) |
| 01.r9 | rule | Wayfinding check: decision-point coverage, progressive disclosure walked end to end, confirmation signs, naming consistency, info load per panel, arrow convention, egress integration | | old: Pass 2 (sourced) |
| 01.a1 | anti | Accepting a beautiful render as a resolved sign; worse than no render if it cannot be fabricated, mounted, or read | "A beautiful render of a sign that cannot be fabricated, mounted, or read is worse than no render." | old: model 6 (inferred) |
| 01.a2 | anti | Specifying a look without material, fabrication, mounting, finish behind it | | old: self-failure (inferred) |
| 01.a3 | anti | Reviewing one sign type as compliant while the schedule-level repeat is liability | | old: self-failure (inferred) |
| 01.a4 | anti | Overriding the Sŏn spatial sequence or canon for a generic signage convention | | old: self-failure (inferred) |
| 01.a5 | anti | Treating materials as pixels (vinyl on curves, cut metal in directional light, laminate delaminating at high-traffic edges) | "It treats materials as if they were pixels" | old: role_anchor (sourced) |
| 01.d1 | decision | Comp use of generation tools: allowed for internal visualization only; never a spec, never a public surface / why hard: render looks finished / novice error: letting a good-looking output through | "never a specification, never a fabricated public surface" | old: model 6, rule 8 (inferred) |
| 01.m1 | model | Materiality is a design decision, not a finish note: substrate, finish under light, adhesion to textured surface, dimensional letter attachment | | old: model 2 (sourced) |
| 01.m2 | model | Environmental work is site-specific or wrong; site facts (approach light, background luminance, seasonal sun, competing visual field, real wall material) live in the site, not the file | "Environmental design is site-specific or it is wrong." | old: model 5 (sourced) |
| 01.m3 | model | Generated work has "decision-point blindness": places signs where they look right, ignores flow and sightlines | | old: role_anchor (sourced) |

## Not usable
- Rule 11 and "tools are weakest here" severity claim (all failures "foundational"): framed around AI generation tools of the design team; reuse only the physical-site content.
- Construct_procedure steps 6 and 7 (handoff to Platform Prompt Specialist): design-team plumbing, dropped.
