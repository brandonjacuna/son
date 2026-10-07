# Sŏn Learning Studio

This repo is where Sŏn's education and training modules are identified, ideated, designed, drafted, and parked until the operation's tools and workflows are set. It produces tool-neutral module source packages. It does not lock in any operational tool or workflow.

Read this file, then `canon/standing-rules.md`, before any task.

## The bar

Sŏn's goal is to be considered one of the absolute best restaurants in the country. Brandon has worked for restaurants of that caliber, and they built Sŏn's points of view. Hold every module, gate, and design choice to what a program must be to produce and sustain that standard, not what a good restaurant does. His lineage houses are still never reconstructed; his experience comes from him directly. `framework/system-design.md` governs how the module system works.

## The one idea that makes this work

A module has two kinds of content:

1. **Durable content.** The craft, the judgment, the why, the standard. True no matter which POS, reservation system, or LMS Sŏn runs. Written fully now.
2. **Bindings.** Anything that depends on a tool or workflow that is not set yet: the button path in the POS, the exact opening sequence, the station layout, the allergen matrix. Never written as fact. Always a placeholder: `{{bind:tool.pos.allergen_flag}}`, declared in the module's `bindings.yaml`.

A module whose durable content is complete and whose only gaps are declared bindings is **parked**. Parked is the target state for now. When tools and workflows are set, fill the bindings (`/bind`), render through an adapter (`/render`), and the module ships. See `framework/bindings.md`.

## Where things live (and where they do not)

| Thing | Home | Rule |
|---|---|---|
| Module source packages | this repo, `modules/` | Source of truth for module content. Versioned by git. |
| Module catalog and status | this repo, `catalog/catalog.yaml` | One row per module. Mirrored by `/status` to the ClickUp list Module Catalog `1400400000001424`. |
| Profiles (the specialist seats) | repo `profiles/` (phase 3 rebuilds the profile system) | Never edited here. Never committed. |
| Frozen releases | Box folder `421837487417` | Approved module packages exported as snapshots. |
| Published modules | Trainual (current plan) | Rendered from source by an adapter. Never edited in Trainual first. |
| Financial figures | Investor Review workbook, Box (Sŏn / 02. Capital Raise) | Never generated, estimated, or recalled. Read the current workbook or leave a `fact.*` binding. Operational figures (pars, labor targets, pay, schedules, counts) are unbound until a source is chosen (Airtable retired). |
| Brand facts | Brand Guidelines (canon line pending phase 1 session B), Box file `2281626080747` | Read from Box. Never hard-coded here. Anything not confirmed by Brandon stays a `brand.*` binding. |
| Strategy | Box, Sŏn Investor White Paper Sept 2026, file `2466517057642` | Read from Box. Carries figures; never carry a value. |
| Full resource map | `canon/pointers.md` | Lists the IDs this studio uses. |

Internal sources are read from Box, never from ClickUp documents. ClickUp holds tracking only: tasks, lists, and the module catalog mirror. The Sŏn Operating System is an active project that has not begun; do not consider it. (Brandon, 2026-09-28.)

## Lifecycle

`identified -> concept -> designed -> drafted -> reviewed -> parked -> bound -> rendered -> published -> measured` (plus `retired`). Exit criteria for each stage are in `framework/lifecycle.md`. Do not advance a module past a stage whose exit criteria are unmet.

## Which seat does what

Profiles are listed in `profiles/manifest.yaml` with their Box IDs and the stages they own. Load only the profiles the current stage needs. The routing in brief:

- **Identify:** Instructional Designer (is instruction even the lever), Hospitality Operations Realist (is this a tempo or system problem), Frontline Advocate (what the floor says it needs).
- **Ideate:** Curriculum & Program Architect (where it sits in the program), Hospitality Craft Educator (what the craft actually is), Learner Advocate.
- **Design:** Instructional Designer, Assessment & Competency Designer, Practice and Simulation Designer, plus HighScope and TBRI where the module touches active learning or correction.
- **Draft:** Educational Materials Author and Editor.
- **Review:** the panel in `framework/review-panels.md`, chosen by module type.
- **Render:** the adapter, plus the Design Translating Team whenever a prompt goes to an AI design or video tool.

A profile that says a call is founder-gated, chef-gated, or team-gated means exactly that. Mark it in the module's review log. Do not land it.

## Commands

These slash commands no longer exist in this folder. The tooling is salvaged and inert until phase 5: see `_salvage/README.md`.

| Command | Does |
|---|---|
| `/sync-profiles` | Profiles: repo `profiles/` (phase 3 rebuilds the profile system). |
| `/identify` | Intake a training need, run the front-end check, add it to the catalog. |
| `/ideate` | Turn an identified need into a concept brief with a program slot. |
| `/design-module` | Produce the module design: objectives, structure, practice, assessment, medium plan, bindings. |
| `/draft-module` | Write the source package from the design. |
| `/review-module` | Run the review panel and log findings. |
| `/park-module` | Verify exit criteria and mark the module parked. |
| `/bind` | Fill bindings, by module or by binding key across all modules. |
| `/render` | Render a bound module through an adapter (Trainual, Synthesia, print, live). |
| `/status` | Report the catalog, stage counts, open bindings, and modality variety, then mirror the catalog to ClickUp. |
| `/refresh-capabilities` | Re-research a platform (Trainual, Synthesia, H5P) and update its adapter. Platforms change fast. |
| `/build-profile` | Build a new specialist profile, stages 0 to 5 of the synthesis procedure. |
| `/validate-profile` | Stages 6 and 7 of the synthesis procedure. Run in a fresh session. |

## Designing for options, not defaults

Text plus video plus multiple choice teaches recognition, not performance. Every design considers at least three modalities per practice component from `framework/modality-library.md`, organized by the learning job (know, see, decide, do, hold, find, teach). Then check what the delivery platform can actually record in `adapters/trainual.md`. The governing fact: in Trainual only native tests and SCORM packages report completion or score; embedded interactions teach but leave no record. `python scripts/build_scorm.py` turns a module's scenarios into a tracked SCORM package with no extra tools.

## Studio rules every seat works under
Carried from the old profiles' shared blocks when the seats were rebuilt (Brandon, 2026-10-07). Seat-specific rules live in each seat.
- The target learner is about 22, six months in, often working in a second language, under service pressure. Every module passes a novice test against that learner.
- Why before how: onboarding and modules teach the reason before the procedure.
- Readiness gate: no one touches a table until demonstrably ready; sign-off is a competency conversation. Gate validity belongs to the Assessment and Competency Designer; sequencing to the Curriculum and Program Architect.
- Peer-authored modules: team members are paid to teach. Quality, voice, pedagogy, and assessment validity live in the template and style guide, not in the author; the studio keeps central coherence.
- Reviews run every 3 to 6 months: no surprises, feedback both ways.

## Hard rules

- Standing rules in `canon/standing-rules.md` apply to every file in `modules/`. Run `python scripts/lint.py` before any commit. The GitHub Action runs it too.
- Never write a tool-specific or workflow-specific step as fact. Bind it.
- Never write a figure (price, wage, cost, cover count, percentage of revenue). Read financial figures from the current Investor Review workbook at bind time; operational figures stay unbound until a source is chosen (Airtable retired). Otherwise leave a `fact.*` binding.
- Never assert a brand fact that is not in the Brand Guidelines. Where a module needs one, cite the canon page or bind it with `brand.*`.
- Never reconstruct a practice from Brandon's lineage (Coqodaq, Alinea, Gracious) as fact. Flag it for Brandon.
- Back-of-house station specifics, recipes, and menu execution are chef-gated. Bind them with `chef.*`.
- Never edit a profile here. Profiles: repo `profiles/` (phase 3 rebuilds the profile system).
- Never paste profile text into a module or commit it anywhere in this repo.
- Training content is written in the library voice held by the Educational Materials Author and Editor, against the Brand Guidelines Verbal Identity page. The House voice system is for investor- and audience-facing persuasion, not training.

## Connector hygiene

Enable only the connectors a session needs (usually Box plus ClickUp). Disable what the session does not use. The studio's `.mcp.json`, settings and slash commands are salvaged and inert until phase 5: see `_salvage/README.md`.

## Commit conventions

One module per commit where possible. Message format: `MOD-ID stage: what changed`, for example `FOH-003 drafted: scenarios and job aid`. Profile builds: `PROFILE name stage N: what changed`.
