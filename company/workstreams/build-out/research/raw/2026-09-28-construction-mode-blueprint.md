# Construction-mode workspace: research blueprint (2026-09-28)

Restored 2026-10-07 from the research report produced in chat on 2026-09-28, so it travels with the repo. Edits on restore: plan tier recorded as confirmed (Max 5x); one cuisine-specific monitoring tag made neutral per the brand canon cleanup. Everything else is as researched. Facts marked "secondary" were not checked against a primary source.

This is the research record behind `decisions/0001-architecture.md`. It holds the parts not captured elsewhere: the software stack ranking, the handoff format strategy, the full profile roster, the trade-show calendar, the import rule, and the prototyping toolchain.

## 1. Key findings
1. **Cloud vs local is the central constraint.** A cloud environment setup script runs once, as root, on Ubuntu 24.04 before Claude Code launches, and the result is cached (re-run when the script or network allowlist changes, or about every seven days; not cached if setup takes over about five minutes). Every CAD MCP server found (SketchUp, Blender/Bonsai, FreeCAD) is a bridge from an add-on inside the running desktop app to a local MCP server. Those run only on the Mac. The cloud still does real geometry through headless Python (build123d, IfcOpenShell, ezdxf).
2. **Secrets are not available to the setup script.** Cloud environment variables are empty inside the setup script and only injected once the session runs (GitHub issue anthropics/claude-code #63541, May 2026). ClickUp and Box authentication happens at session time through connectors or a runtime environment secret. The Mac-only `cu.py` token path does not work in cloud; cloud sessions use the ClickUp connector or CLICKUP_API_TOKEN.
3. **Claude Code primitives used:** subagents with `model`, `tools`, `skills`, `memory`, `effort`, `background`, `isolation`, `maxTurns`, `omitClaudeMd` frontmatter; skills with progressive disclosure (only name and description stay resident); AskUserQuestion pop-ups with an automatic "Other"; Routines (launched April 14, 2026, research preview) for scheduled cloud sessions.
4. **Austin codes changed recently.** 2024 local amendments adopted April 10, 2025, effective July 10, 2025: 2024 IBC/IEBC, UPC, UMC, IECC, IFC with local amendments. Electrical: NEC 2023, effective September 11, 2023. Austin uses the Uniform codes for plumbing and mechanical, not IPC/IMC, so every code fact is tagged with its code family. Seeded into `codes/register.yaml`.
5. **Live fire sets the budget.** NFPA 96 solid-fuel provisions (carried into UMC Section 517) require a separate exhaust system for solid-fuel appliances, spark arresters ahead of grease filters, and filters at least 4 ft above the cooking surface. Site-built solid-fuel appliances need AHJ approval. This is the largest MEP cost and space driver and the first feasibility study to run against 207 E St. Elmo Rd.
6. **Existing landing zones.** ClickUp Property space (90136733959) with Property Capture (901327291277), plus Product Capture and Technology Capture lists. Box `Sŏn / 04. Property and Build-Out` (420132927884), empty at research time. The ClickUp doc "Claude Project Review" already holds Sŏn build-out compliance guides (see KICKOFF step 4 for the page list).

## 2. Software and connector stack (Mac, cost-ranked)
| Tool | Cost | Mac | Claude integration | Role | Verdict |
|---|---|---|---|---|---|
| build123d / CadQuery | Free | Yes, and cloud | build123d-mcp; plain Python | Parametric equipment envelopes, die walls, millwork, fab parts; STEP/STL/DXF | Core, now |
| IfcOpenShell + Blender/Bonsai | Free | Yes | Bonsai MCP (local); IfcOpenShell headless | Space model, equipment as IFC entities, rough-in points, IFC handoff | Core, now |
| FreeCAD 1.x | Free | Yes | neka-nat/freecad-mcp (local, includes FEM) | TechDraw sheets, FEM, sheet-metal unfold, DXF | Core, now |
| ezdxf | Free | Cloud | Direct scripting | DWG-compatible DXF plans and layers | Core, now |
| Zoo Design Studio (KCL) | Free tier | Yes | Text-based, versions in git; API | Rapid part ideation; STEP/STL | Optional, now |
| KCL CADalog web (Revalize) | Free manufacturer downloads | Web | None (manual download to `library/`) | Blocks, Revit families, spec sheets from 268 foodservice manufacturers | Core, now (account) |
| SketchUp Pro | $399/yr (secondary; Go $129/yr is web/iPad only) | Yes | Community MCP bridges; Ruby API | Fast visual layout play, LayOut sheets, DWG in/out | Later, when layout iteration is weekly |
| Fusion (personal) | Free | Yes | API | Fab parts | Avoid: non-commercial license, no DWG import. Apply for Fusion Startup only if the fabricator uses Fusion |
| Onshape | Free plan is public docs only | Web | REST API | Fab parts | Skip unless the fabricator uses it |
| Rhino 8 | $995 perpetual | Yes | Community MCP | Complex curved forms | Only for a curved custom bar |
| Revit | $3,005/yr | Windows only | n/a | n/a | Do not buy; architect and MEP use it, receive IFC + KCL families |
| AutoCAD LT Mac, Vectorworks, Archicad, Chief Architect | $500 to $3k+/yr | Yes | Weak | Drafting/BIM | Not justified for an operator-PM |
| AutoQuotes (AQ) | Dealer subscription | Web | None | Pricing and specs | Access through the foodservice dealer, post-lease |

Accounts now: GitHub (private), Claude Max 5x (confirmed), KCL web, Zoo, BIMobject, manufacturer portals (True, Hoshizaki, Hobart, Perlick, Krowne, Glastender), UpCodes free tier. Connect ClickUp and Box connectors at claude.ai.
Accounts later: SketchUp Pro, Fusion Startup (conditional), AQ via dealer.

Equipment data trust order: manufacturer spec sheet PDF (source of truth for dimensions and utilities), KCL blocks and families, BIMobject or manufacturer Revit families, manufacturer STEP.

## 3. Contractor handoff strategy
Brandon is not the design professional of record; Austin commercial permitting needs stamped drawings from a licensed architect and MEP engineer. Deliverables are design-intent packages:
- IFC 4 model: equipment as `IfcFurnishingElement` / `IfcFlowTerminal` with utility property sets.
- DXF/DWG plan layers with US National CAD Standard layer names (Q-EQPM, P-SANR, E-POWR): equipment plan, utility rough-in plan with heights, bar elevations.
- PDF sheet set with title block, version, phase, and "NOT FOR CONSTRUCTION: DESIGN INTENT."
- Equipment schedule (CSV/XLSX from `equipment/*.yaml`): item, qty, manufacturer, model, electrical, plumbing, gas, exhaust, remarks.
- Native files only on request.
Open: ask the first architect and GC what they draft in (decisions/open.md #3).

## 4. Intake workflow
1. Capture: chat attachments, Box `_Intake`, or `intake/inbox/` on the Mac.
2. Triage: Haiku `intake-triage` subagent classifies, transcribes annotations, lists visible dimensions; never interprets intent.
3. Clarify: `interview` skill, one AskUserQuestion per question, 2 to 4 options with the tradeoff in the label (descriptions sometimes do not render in Desktop), short headers, "Other" for dictation.
4. File: card linked to trade folder, equipment record, or sandbox. Unresolved items go to `decisions/open.md`, not ClickUp.
Community skill authors report AskUserQuestion limits of 1 to 4 questions per call, 2 to 4 options, and a 12-character header (secondary).

## 5. Profile roster (planned; 2 of 18 built)
| Profile | Model | Scope | Built |
|---|---|---|---|
| intake-triage | haiku | Classify, OCR, extract dimensions | yes |
| equipment-librarian | haiku | Equipment YAML from spec sheets | yes |
| bar-designer | sonnet | Front/back bar, underbar, speed rails, ergonomics, glass flow (reads kb/bar/tobin-ellis first) | no |
| kitchen-layout | sonnet | Line flow, live-fire station, prep, dish, walk-in, clearances | no |
| ventilation-fire | opus | NFPA 96/UMC hoods, solid-fuel separate exhaust, make-up air, suppression | no |
| plumbing-water | sonnet | Indirect drains, floor sinks, grease interceptor, filtration, ice machines | no |
| electrical-power | sonnet | Load schedules, circuits, NEMA configurations, panel inputs | no |
| lighting | sonnet | Scenes, CCT, dimming protocols, fixture schedules | no |
| av-network | sonnet | Audio zoning, POS/KDS network, Wi-Fi, low-voltage rough-in | no |
| hvac-comfort | sonnet | Dining comfort, pressurization against kitchen exhaust | no |
| materials-finishes | sonnet | NSF/food-zone materials, cleanable surfaces, stainless gauges | no |
| storage-shelving | haiku to sonnet | Shelving systems, dry and cold storage capacity | no |
| codes-permitting | opus | Austin code interpretation; APH, Austin Water, TABC, ADA/TAS matrices | no |
| fabrication-dfm | sonnet | Fab packages, DFM, tolerances, GD&T | no |
| import-certification | sonnet | UL/ETL/NSF/CSA status of foreign equipment | no |
| innovation-scout | haiku | Feed and trade-show digestion | no |
| clash-reviewer | opus | Cross-trade conflicts in a layout | no |
| kb-consolidator | sonnet | Research to kb merges (covered for now by the `consolidate` skill) | no |

Profile creation: `profile-forge` skill, four stages (Frame on Haiku, Evidence on Sonnet capped at 8 searches, Distill on Opus or Fable via /deep for safety-critical roles, Test on Haiku with 3 scenarios). Agent files stay under 120 lines; long reference goes to `kb/`.

## 6. Model routing (as researched)
API list prices reported for 2026 (secondary): Haiku 4.5 $1/$5, Sonnet $2/$10, Opus $5/$25, Fable 5.1 $10/$50 per million input/output tokens. Max 5x and 20x plans allow up to half of weekly usage on Fable at no extra cost (secondary). Routing table lives in the build-out `CLAUDE.md` section 4.
Token hygiene: `/clear` between unrelated tasks; subagent summaries of 200 words or fewer; MCP servers enabled per task; plan mode before multi-file modeling; root CLAUDE.md under 150 lines.

## 7. Codes, permitting, and monitoring
Register: `codes/register.yaml`. Process notes:
- In the City of Austin, food establishment plan review goes through Development Services; Austin Public Health runs the pre-opening inspection and issues the permit. Legacy APH guidance asks for 1/4 in = 1 ft plans showing kitchen, dining, restrooms, storage, bar and wait stations, plus a finish schedule.
- Austin Water sizes the grease interceptor in its approval letter during building plan review: minimum 500 gallons with a dishwasher; nothing under 100 gallons approved; do not buy before the approval letter; clean every 3 months or at 50% of the final compartment.
- TABC: Mixed Beverage permit plus Food and Beverage Certificate via AIMS. Timelines reported anywhere from 30 to 90+ days; long-lead item, confirm with TABC.
- Plan an early meeting with Austin Fire and the building official on the solid-fuel appliance, especially if any unit is site-built.
Monitoring: daily GitHub Action hashes watched pages (`monitoring/sources.yaml`) and opens an issue on change ($0); a weekly Sonnet Routine (planned) classifies diffs and proposes register or kb edits. Routine caps reported: Pro 5, Max 15, Team/Enterprise 25 runs per day (secondary).

## 8. Equipment and innovation monitoring
| Event | Next date | Location | Innovation program |
|---|---|---|---|
| NAFEM Show | Feb 11 to 13, 2027 | Orlando | Historically Innovation Station (unverified for 2027) |
| FOODEX Japan | Mar 9 to 12, 2027 | Tokyo Big Sight | n/a |
| INTERNORGA | Mar 12 to 16, 2027 | Hamburg | Future Award, Next Chef Award |
| HCJ (HOTERES / CATEREX / Food Service Equipment Show) | Mar 16 to 19, 2027 | Tokyo Big Sight | n/a |
| FHA-Food & Beverage | Apr 20 to 23, 2027 | Singapore EXPO | n/a |
| NRA Show | May 22 to 25, 2027 | Chicago | Kitchen Innovations Awards |
| Seoul Food (KOTRA) | June 8 to 11, 2027 | KINTEX, Goyang | Not the separate "Seoul Food & Hotel" |
| Bar Convent Brooklyn | June 8 to 9, 2027 | Industry City | CHILLED 100 Spirits Awards |
| Tales of the Cocktail | July 2027 (dates unpublished) | New Orleans | Spirited Awards |
| Bar Convent Berlin | Oct 12 to 14, 2026; 2027 unannounced | Messe Berlin | n/a |
| HostMilano | Oct 22 to 26, 2027 (biennial) | fieramilano Rho | SMART Label |

Pipeline (planned): weekly Action pulls trade press (FE&S, FER, Nation's Restaurant News, Restaurant Business, Imbibe, Punch) and award pages; a Haiku Routine dedupes and tags for relevance (live fire, bar, ice, dish, water, induction/charcoal hybrids, grill-table ventilation) into `monitoring/digests/<week>.md`; monthly Sonnet merge into `kb/equipment-landscape.md`. Anything to act on goes to a capture list, never a task list.

Import rule (`import-certification`): for equipment sold outside the US, record UL/ETL/CSA listing (needed for electrical inspection), NSF/ANSI or equivalent sanitation listing (health plan review), and voltage/frequency mismatch (230V/50Hz vs US 208/240V/60Hz). Default verdict "inspiration only" unless a US-listed variant or a field-evaluation path is documented.

## 9. Prototyping toolchain and validation
| Process | Hand-off files | Tool |
|---|---|---|
| CNC milling/routing | STEP (AP214/242) + PDF drawing with GD&T; DXF for 2D routing | build123d / FreeCAD; fabricator runs CAM |
| Laser / waterjet / plasma | DXF at 1:1, closed polylines, one layer per operation | ezdxf / FreeCAD |
| Sheet metal | STEP of folded part + DXF flat pattern + bend table (K-factor from fabricator) | FreeCAD SheetMetal |
| 3D printing | 3MF preferred, STL fallback | build123d / Zoo |
| Welding | PDF weldment drawing with AWS weld symbols + STEP | FreeCAD TechDraw |
| G-code | Never generated for the fabricator's machines | n/a |

Validation ladder: (1) CI checks: watertight solids, minimum wall, hole-to-edge, bend radius at least material thickness; (2) FEA in FreeCAD FEM for load-bearing parts; (3) `fabrication-dfm` review against the fabricator's capability sheet; (4) ASME Y14.5 GD&T on critical features only; (5) human sign-off. A June 2026 CADGenBench result supports incremental MCP modeling (build123d-mcp raised CAD validity from 88% to 100% in one test). Rule: render, measure, validate, then export.
Handoff from Claude Science: outputs enter `intake/` as a spec card; `fabrication-dfm` converts to a parametric build123d model; nothing goes to the fabricator without all five ladder steps.

## 10. ClickUp and Box boundaries
- P0: no task creation except capture-list ideas or a committed action Brandon confirms. At P1, `/lease-signed` builds the construction space from `clickup/space-blueprint.md`.
- Box holds binary evidence under `Sŏn / 04. Property and Build-Out/` with phase subfolders; the repo stores Box file ID + SHA1. Contractor packages publish to `…/Handoff/<date>-<package>/`.

## 11. Risks
- Community CAD MCP servers are unofficial and some expose arbitrary code execution (SketchUp Ruby eval, Blender/FreeCAD Python exec). Run locally only, pin versions, review before upgrading.
- Routines are a research preview; keep monitoring logic in Actions so it degrades gracefully.
- Model-generated geometry can be dimensionally wrong: every spec-sheet dimension traces to a PDF, and CI asserts envelopes against YAML.
- Code facts can be misapplied across code families (IMC vs UMC).
- Secondary-source figures (TABC timelines, model pricing, Routine caps, SketchUp pricing) need primary-source checks before reliance.
- The workspace produces design intent only; permit sets need licensed professionals.

## Sources (primary ones)
- Claude Code subagents: https://code.claude.com/docs/en/sub-agents
- Claude Code on the web quickstart: https://code.claude.com/docs/en/web-quickstart
- Setup script env var issue: https://github.com/anthropics/claude-code/issues/63541
- Austin building technical codes: https://www.austintexas.gov/page/building-technical-codes
- Austin Fire building code: https://www.austintexas.gov/fire/fire-building-code
- Austin Water grease trap criteria: https://www.austintexas.gov/water/grease-trap-sizing-design-criteria
- APH fixed food establishments: https://www.austintexas.gov/health/programs/fixed-food-establishments
- Texas Food Establishment Rules (25 TAC 228): https://www.dshs.texas.gov/sites/default/files/foodestablishments/pdf/GuidanceDocs/TFER-2021_TAC-228_August-2021.pdf
- UpCodes, solid-fuel cooking operations: https://up.codes/s/solid-fuel-cooking-operations
- KCL foodservice CAD: https://kclcad.com/
- FreeCAD MCP: https://github.com/neka-nat/freecad-mcp
- Bonsai MCP: https://mcpservers.org/servers/JotaDeRodriguez/Bonsai_mcp
- build123d MCP: https://github.com/pzfreo/build123d-mcp
- Zoo FAQ: https://zoo.dev/docs/faq
- Fable 5.1 announcement: https://www.anthropic.com/claude-fable-and-mythos-5-1
- NAFEM 2027: https://nafem.org/event/the-nafem-show-2027/
- HostMilano: https://host.fieramilano.it/en
- INTERNORGA: https://www.internorga.com/en/fair/about-internorga
- NRA Show: https://www.nationalrestaurantshow.com/home/why-attend/
- FOODEX Japan: https://foodex.jma.or.jp/en/
- Tales of the Cocktail Spirited Awards: https://talesofthecocktail.org/events/spirited-awards/
