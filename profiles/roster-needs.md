# Roster needs (phase 3, step 3)

Status: built-agent = lean agent exists; profile-only = long source in `profiles/_source/` (paths below relative to it); gap = no profile. Founder clusters are inventoried under `founders/`.

Only 1 company seat is rebuilt. Build-out has 2 built worker agents. profile-critic/extractor/grader/runner are builder tooling, not seats.

## 1. Seats by workstream

### Learning studio (29 seats in manifest.yaml; review panels in `framework/review-panels.md`)

| seat | what it decides | covered by | status |
|---|---|---|---|
| Curriculum & Program Architect | Program shape, sequence, dependencies, gate placement | learning-and-development/Curriculum & Program Architect.md | profile-only |
| Instructional Designer | How one module teaches; front-end gap check; medium; authoring template | learning-and-development/Instructional Designer.md | profile-only |
| Assessment & Competency Designer | Whether a gate validly reads readiness; signs gate specs | learning-and-development/Assessment & Competency Designer.md | profile-only |
| Educational Materials Author and Editor | The prose and the single library voice | learning-and-development/Educational Materials Author and Editor.md | profile-only |
| Learner Advocate | Built for the learner or for the designer | learning-and-development/Learner Advocate.md | profile-only |
| HighScope | Active participatory learning, plan-do-review | learning-and-development/HighScope.md | profile-only |
| TBRI | Felt safety in correction and feedback | learning-and-development/TBRI.md | profile-only |
| Hospitality Craft Educator | What the craft is as a teachable discipline; how tacit parts transmit | learning-and-development/Hospitality Craft Educator.md (95 KB) | profile-only |
| Practice and Simulation Designer | Which practice form transfers; consequence, feedback, fidelity, debrief | profiles/learning-and-development/practice-simulation-designer/agent.md; `.claude/agents/practice-simulation-designer.md` | built-agent |
| Hospitality Operations Realist | Survives a Friday at 8:15 with the real crew (core panel, every module) | scaling-people/Hospitality Operations Realist.md | profile-only |
| Frontline Advocate | What the hourly team needs and what lands (core panel) | people-and-culture/Frontline Advocate.md | profile-only |
| Emerging Leader Advocate | Leadership-track learners; LEA domain | people-and-culture/Emerging Leader Advocate.md | profile-only |
| Culture Implementer | Ritual and culture material survive a real floor; ORI, CUL | people-and-culture/Culture Implementer.md | profile-only |
| Values and Belonging Designer | Values and belonging design; ORI | people-and-culture/Values and Belonging Designer.md | profile-only |
| Performance and Feedback Systems Designer | Reviews and feedback systems; LEA | people-and-culture/Performance and Feedback Systems Designer.md | profile-only |
| HR Implementer | Administrability of HR-facing material; SAF, linked rows | people-and-culture/HR Implementer.md | profile-only |
| HR Systems Designer | HR systems; policy modules | people-and-culture/HR Systems Designer.md | profile-only |
| Culture Signal Designer | Whether culture took; CUL | people-and-culture/Culture Signal Designer.md | profile-only |
| Organizational Systems Architect | Advancement ladder, roles, unlock rules (only when structure changes) | scaling-people/Organizational Systems Architect.md | profile-only |
| People Systems Designer | Whether a people system produces its intended behavior | scaling-people/People Systems Designer.md | profile-only |
| Design Translating Team, 9 seats: Brief Translator, Platform Prompt, Brand Identity, Editorial Layout, Web UI, Environmental Signage, Image Campaign, Design Director, Creative Director | Brief, prompt, identity, layout, web, signage, image, routing, direction (render stage) | design-translating-team/01 to 09 | profile-only |

Chef sign-off (KIT) and founder gate are human seats.

### Build-out (blueprint section 5: 18 planned, 2 built)

| seat | what it decides | covered by | status |
|---|---|---|---|
| intake-triage | Classify, OCR, extract dimensions | `.claude/agents/intake-triage.md` | built-agent |
| equipment-librarian | Equipment YAML from spec sheets | `.claude/agents/equipment-librarian.md` | built-agent |
| bar-designer | Front/back bar, underbar, speed rails, ergonomics, glass flow; reads `kb/bar/tobin-ellis/` first | none | gap |
| kitchen-layout | Line flow, live-fire station, prep, dish, walk-in, clearances | none | gap |
| ventilation-fire | NFPA 96/UMC hoods, solid-fuel exhaust, make-up air, suppression | none | gap |
| plumbing-water | Indirect drains, floor sinks, grease interceptor, filtration | none | gap |
| electrical-power | Load schedules, circuits, NEMA, panel inputs | none | gap |
| lighting | Scenes, CCT, dimming, fixture schedules | none | gap |
| av-network | Audio zoning, POS/KDS network, Wi-Fi, low-voltage | none | gap |
| hvac-comfort | Dining comfort, pressurization against kitchen exhaust | none | gap |
| materials-finishes | NSF/food-zone materials, cleanable surfaces | none | gap |
| storage-shelving | Dry and cold storage capacity and systems | none | gap |
| codes-permitting | Austin code interpretation; APH, Austin Water, TABC, ADA/TAS | none | gap |
| fabrication-dfm | Fab packages, DFM, tolerances | none | gap |
| import-certification | UL/ETL/NSF/CSA status of foreign equipment | none | gap |
| innovation-scout | Feed and trade-show digestion | none | gap |
| clash-reviewer | Cross-trade conflicts in a layout | none | gap |
| kb-consolidator | Research to kb merges | `consolidate` skill (not a profile) | gap, deferrable |

Of the 16 unbuilt seats, only `bar-designer` is referenced by name elsewhere in build-out kb (`kb/bar/tobin-ellis/README.md`, line 29). The blueprint was researched, not decided; Brandon sets build order (brief, decisions list). No company profile covers any construction trade.

### Operations (Scaling People build-out)

Operations uses profiles as "reasoning lenses for considerations, never authorities" (its CLAUDE.md), with copies in `company/workstreams/operations/profiles/`.

| seat | what it decides | covered by | status |
|---|---|---|---|
| Hospitality Operations Realist | Does an org or operating design hold at tempo with an hourly crew | scaling-people/Hospitality Operations Realist.md | profile-only |
| Organizational Systems Architect | Structural soundness: code-bearing web, two-lead layer, progression | scaling-people/Organizational Systems Architect.md | profile-only |
| People Systems Designer | Hiring, team development, feedback as machinery | scaling-people/People Systems Designer.md | profile-only |
| HR Systems Designer | Handbook, conduct standards, policy set | people-and-culture/HR Systems Designer.md | profile-only |
| HR Implementer | Administrability and fair enforcement | people-and-culture/HR Implementer.md | profile-only |
| Performance and Feedback Systems Designer | The review an employee sits in | people-and-culture/Performance and Feedback Systems Designer.md | profile-only |
| Culture Implementer | Does designed culture survive a floor | people-and-culture/Culture Implementer.md | profile-only |
| Frontline Advocate | Hourly view of any policy or system | people-and-culture/Frontline Advocate.md | profile-only |
| Five L&D lens copies (Instructional Designer, Materials Author, TBRI, Learner Advocate, HighScope) | kept in operations/profiles | as above | profile-only |

### Nerve, clickup-system, science, brand

| workstream | seats named | covered by | status |
|---|---|---|---|
| nerve (weekly industry digest) | none; rules live in its CLAUDE.md | none needed | n/a |
| clickup-system (knowledge base, runbooks, Meetings Agent) | none; no profile or seat references found | none needed | n/a |
| science (espresso-chiller, matcha-sonication, cryo-espresso) | none named | none | n/a |
| brand (`company/brand/design-system`, code) | no profile references. Design is done in code; the Design Translator auto-trigger is an open decision for Brandon | design-translating-team (if kept) | profile-only, decision pending |

## 2. Retirement candidates (no company workstream needs them)

- Voice/Gladwell_Narrative_Voice_Profile.md: learning-studio CLAUDE.md line 95 says the House voice system is for investor and audience persuasion, not training. Move to `founders/` or retire.
- Voice/Graham_Clarity_Voice_Profile.md: same reason; only serves the House Voice.
- Voice/Vee_Conviction_Voice_Profile.md: same reason; conviction register also sits close to the "no performed conviction" standing rule.
- Voice/House_Voice_Brandon_Profile.md: braids the three pole voices; needed only if a persuasion workstream (investor, white paper) is kept. Not company-facing.
- narrative-and-structure/Narrative_Architect_Profile.md: shapes white paper, website, deck argument. No company workstream names it; investor/founder use only. Keep under `founders/` or retire.
- design-translating-team/10_Motion_Interaction_Specialist_Profile.md: not in the learning-studio manifest and brand is built in code; 46 KB. Retire unless brand takes motion work on.

Held: Design Translating Team 01 to 09 (auto-trigger decision open).

## 3. Gaps

1. All 16 unbuilt build-out seats (table above). Known first build: bar-designer (reads Tobin Ellis kb first; sonnet).
2. A chef-side reviewer for KIT modules: only a human sign-off exists, no profile.
3. Science, nerve, clickup-system, brand: none needed today.

## 4. Overlaps

- Hospitality Operations Realist, Culture Implementer, HR Implementer: all "does it survive a real floor." The boundary is written (the Realist tests the operating system, the others test culture and HR material), but the learning-studio core panel plus domain adds loads three floor-realists on one SAF/ORI module.
- People Systems Designer and HR Systems Designer: architecture versus its expression as handbook. Boundary written; pair is mostly sequential.
- Frontline Advocate, Emerging Leader Advocate, Learner Advocate: three receiving-end advocates for different learners; Frontline and Learner overlap on any hourly-staff module.
- Instructional Designer and HighScope: retention mechanics inside participatory structure.
- Hospitality Craft Educator and Practice and Simulation Designer: both choose how a craft transmits (SVC, BEV modules).
- Organizational Systems Architect and Curriculum & Program Architect: progression structure versus program sequence.
- Values and Belonging Designer, Culture Signal Designer, Culture Implementer: one culture topic, three seats (design, measure, reality-check).
- Design Director, Creative Director, Design Brief Translator: routing, direction, and briefing at the top of one team. Web UI Specialist and Motion Specialist share a stated line (state versus argument).
- Build-out: ventilation-fire and hvac-comfort (make-up air versus pressurization); kb-consolidator and the existing `consolidate` skill; clash-reviewer and every trade seat.
- Operations holds duplicate profile copies; one master is needed.

## 5. Summary counts

- Company profiles in `_source`: 35 (10 design-translating, 9 L&D, 8 people-and-culture, 3 scaling-people, 4 voice, 1 narrative); 1 of them (Practice and Simulation Designer) is rebuilt.
- Learning-studio seats: 29 (1 built-agent, 28 profile-only; 9 of them are the design team).
- Build-out seats: 18 (2 built-agent, 16 gap; 1 of the 16 deferrable).
- Operations seats: 8 distinct (all profile-only), plus 5 L&D lens copies.
- Nerve, clickup-system, science, brand: 0 seats required (brand tied to the open Design Translator decision).
- Distinct seats needed across workstreams: 29 + 16 = 45 (3 builds already done: 1 L&D agent, 2 build-out workers).
- Retirement candidates: 6. Gaps: 16 build-out plus 1 chef reviewer. Overlap clusters: 10.
