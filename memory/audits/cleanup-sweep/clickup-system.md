# Cleanup sweep: company/workstreams/clickup-system

Scope: `company/workstreams/clickup-system` (390 raw grep hits in 51 files, `refs` and `node_modules` excluded). Paths below are relative to that folder unless stated. Read-only pass.

## 1. Summary

| verdict | count (lines unless noted) |
|---|---|
| DELETE | 5 lines + 1 whole file (kb/from-build-out-2026-09-28.md, after merge) |
| REWRITE | 27 lines |
| KEEP | 14 lines |
| HOLD-RAW | 31 files under exports/ (about 300 hits) |
| HOLD-PROFILE / HOLD-V7 / REPORT | 0 files (Business Strategies Notebook hits sit only inside exports/, so they are covered by HOLD-RAW and flagged HOLD-V7 there) |

## 2. Per-line table (outside exports/)

Replacement text uses no em dashes. "[OOS]" rows: the Josephine / Event Co item is out of scope and is erased from working context.

| path:line | term | snippet | verdict | reason | proposed replacement |
|---|---|---|---|---|---|
| audit/00-workspace.md:59 | Josephine | `Josephine Pitch PunchList \| CHANNEL \| PUBLIC \| Dominic` | DELETE | out-of-scope initiative channel row | n/a |
| audit/00-workspace.md:71 | Josephine | `The Josephine \| CHANNEL \| PUBLIC \| Brandon` | DELETE | out-of-scope channel row | n/a |
| audit/00-workspace.md:79 | Josephine | `"Josephine Pitch PunchList" / "The Josephine" / "Programming Ideation" / ... are named for specific initiatives` | REWRITE | drop the two Josephine names | `**"Programming Ideation" / "Programming Pitch" / "Event Team Personas" / "Sprint 0 Redcar Response"** are named for specific initiatives/projects (deal or project code names) rather than general team chat.` |
| audit/technology.md:20 | Event Co / Josephine | `split into "Sŏn Home Base" and "Event Co - The Josephine" (a second, unrelated Claude Project...)` | REWRITE | out-of-scope sub-tree | Replace the clause with `split into "Sŏn Home Base" and a second page tree unrelated to Sŏn (out of scope, not catalogued here)` |
| audit/technology.md:21 | Master Pointer Index, Replacement Queue | `"Sŏn — Master Pointer Index & Inventory" ... "Profile Replacement Queue"` | REWRITE | stale pointers; these Box/ClickUp mechanisms are retired | Replace with `**"Sŏn Master Pointer Index & Inventory"** (retired pointer doc, superseded by the repo `profiles/` master copies); pages: "How This Works," "Consolidated Project Custom Instructions," and "Migration & Review Tracker (Temporary)."` (drops the Replacement Queue page) |
| audit/technology.md:55 | Event Co / Josephine | `3. Is "Event Co - The Josephine" a second, active Claude Project ...?` | DELETE | out-of-scope question | n/a (renumber later questions) |
| audit/events.md:4 | Pullman Market | `... GFN Coffee, Pullman Market, Douglas Kuehn III` | REWRITE | Pullman lead in the sponsor list is carried-in Pullman material, not a bio credential | Remove `Pullman Market, ` and change "13 sub-subtasks" to "12 sub-subtasks" |
| audit/founding-son.md:50 | Airtable | `single-word tasks (Gmail, Airtable, StoryDoc...)` | KEEP | verbatim ClickUp task name in an audit record; not a data source | |
| audit/founding-son.md:61 | Airtable | `Gmail, Airtable, AirTable, ClickUp, Access Removal` | KEEP | verbatim task names | |
| audit/founding-son.md:70 | Airtable | same list | KEEP | verbatim task names | |
| DECISIONS.md:94 | Josephine | `#14: ... loose items (Josephine, "(Temporary)", "Investment Thesis Architect")` | REWRITE | working-context mention | `loose items ("(Temporary)", "Investment Thesis Architect", and one out-of-scope page)` |
| DECISIONS.md:129 | Airtable | `Gmail, Airtable, AirTable, ClickUp, Access Removal` | KEEP | verbatim task names | |
| blueprint/00-blueprint.md:87 | Master Pointer Index, Event Co | `Claude Project Review, Master Pointer Index, ... Event Co / (Temporary) / staging-for-Box left for Brandon` | REWRITE | stale pointer + out-of-scope page | Drop `Master Pointer Index, ` from the folder list and change the tail to `"(Temporary)" / staging-for-Box left for Brandon` |
| blueprint/00-blueprint.md:193 | Keychain | `stored locally in macOS Keychain (service clickup-api-token)` | REWRITE | Mac-only token path | `stored outside the repo: CLICKUP_API_TOKEN in cloud sessions (or the ClickUp connector), a local secret store on a Mac; never in chat/tasks/docs.` |
| blueprint/00-blueprint.md:200 | Airtable | `Gmail, Airtable, AirTable, ...` | KEEP | verbatim task names | |
| blueprint/00-blueprint.md:204 | Event Co / Josephine | `"Event Co – The Josephine", "(Temporary)" tracker, ...` | REWRITE | out-of-scope page | `"(Temporary)" tracker, "Investment Thesis Architect (staging for Box)".` |
| blueprint/02-workspace-structure.md:185 | Airtable | leftover admin task list | KEEP | verbatim task names | |
| blueprint/04-knowledge-docs.md:59 | Event Co / Josephine | `plus a second, unrelated business ("Event Co – The Josephine") nested under the same tree` | REWRITE | out-of-scope business | `plus a page tree unrelated to Sŏn (out of scope)` |
| blueprint/04-knowledge-docs.md:64 | Master Pointer Index, Replacement Queue | `every persona/role profile page, the Master Pointer Index & Inventory, the Profile Replacement Queue, ...` | REWRITE | stale pointers | `every persona/role profile page and the Claude System & Profile Methodology research (repo `profiles/` holds the master copies).` |
| blueprint/04-knowledge-docs.md:69 | Event Co / Josephine | `"Event Co – The Josephine" stays where Brandon decides ...` | DELETE | whole sentence about an out-of-scope business | n/a |
| blueprint/04-knowledge-docs.md:75 | Event Co / Josephine | `... "Event Co – The Josephine" (its own space, or stays parked here) — three open questions` | REWRITE | | Remove that item and say "two open questions" |
| blueprint/04-knowledge-docs.md:204 | Event Co / Josephine | `3. "Event Co – The Josephine" inside the Claude folder split ...` | DELETE | out-of-scope open item | n/a |
| blueprint/05-build-plan.md:5 | Keychain | `stored in macOS Keychain, service clickup-api-token` | REWRITE | Mac-only token path | `stored outside the repo (CLICKUP_API_TOKEN in cloud sessions; local secret store on a Mac)` |
| blueprint/05-build-plan.md:15 | Keychain | `store it locally in macOS Keychain (service clickup-api-token)` | REWRITE | Mac-only | `store it outside the repo (CLICKUP_API_TOKEN in cloud sessions, or use the ClickUp connector)` |
| blueprint/05-build-plan.md:17 | Master Pointer Index | export list `..., Claude Project Review, Master Pointer Index, Technology OS` | KEEP | historical record of a finished export (done 2026-09-16); doc name, not a live pointer | |
| runbooks/you-checklist.md:11 | Keychain | `token stored locally in macOS Keychain (service clickup-api-token)` | REWRITE | Mac-only | `token stored outside the repo (CLICKUP_API_TOKEN in cloud sessions).` |
| runbooks/you-checklist.md:57 | Event Co / Josephine | `Decide Event Co – The Josephine / "(Temporary)" / "staging for Box".` | REWRITE | | `Decide "(Temporary)" / "staging for Box".` |
| kb/clickup-knowledge-base.md:12-14 | Keychain | `Store it outside the repo. macOS Keychain works well: save/read commands` | REWRITE | Mac-only token path | `- **Store it outside the repo.** Cloud sessions: the ClickUp connector, or CLICKUP_API_TOKEN injected at runtime. On a Mac: any local secret store. The code reads the token at call time so it never lands in a file, a log, or a transcript. **[V]**` (drop the two `security` command bullets) |
| kb/clickup-knowledge-base.md:155 | Keychain | docstring `token from Keychain, never printed` | REWRITE | | `token from CLICKUP_API_TOKEN, never printed` (and align the sample code to read the env var first) |
| kb/from-build-out-2026-09-28.md (whole file; hits at :14, :157) | Keychain | file header says "Merge its unique points into clickup-knowledge-base.md, then delete this file" | DELETE | near-duplicate of the KB file (diff is the header plus one table); merge confirmed unnecessary except the trailing "Code / Meaning / Fix" table, then delete | n/a |
| kb/cu.py:5 | Keychain | `2. macOS Keychain item "clickup-api-token" (Brandon's Mac)` | KEEP | already env var first; Mac fallback is labelled. But the file is byte-identical to scripts/cu.py (see section 4) | |
| scripts/cu.py:5 | Keychain | same | KEEP | same reason | |
| scripts/export_baseline.py:2 and :14-15 | Keychain, Master Pointer Index | docstring says token from Keychain; token read only via `security`; DOCS list includes "Master Pointer Index" | REWRITE | Mac-only, no env var path; one-shot script already run 2026-09-16 | Docstring: `Token comes from CLICKUP_API_TOKEN (or the local secret store on a Mac), never printed.`; read the env var first like cu.py; remove `"Master Pointer Index"` from DOCS. Alternative: DELETE the script (owner call). |
| scripts/meeting_transcript.py:10-12 | Keychain, `clickup-api-token` | `Tokens come from the macOS Keychain ... security add-generic-password` | REWRITE | Mac-only | `Tokens come from CLICKUP_API_TOKEN and ASSEMBLYAI_API_KEY environment variables (or the local secret store on a Mac) and are never printed.` (code at the cu import already supports env var for ClickUp) |
| logs/2026-10-04.md:3 | Keychain | `Needs an AssemblyAI key in Keychain (service assemblyai-api-token)` | KEEP | dated log of what happened; leave as record | |
| research/00-digest.md:35 | Event Co / Josephine | `a second business ("Event Co – The Josephine")` | REWRITE | | `a page tree unrelated to Sŏn` |
| research/00-digest.md:114 | Josephine | `per-initiative channels (Josephine, Programming)` | REWRITE | | `per-initiative channels (Programming)` |
| research/00-digest.md:139 | Airtable | `single-word admin tasks (Gmail, Airtable...)` | KEEP | verbatim task names | |
| research/00-digest.md:151 | Event Co / Josephine | `Is "Event Co – The Josephine" a separate business that needs its own space/workspace?` | REWRITE | | Delete that sentence; keep `Claude folder: split personas from compliance references?` |
| research/07-classification.md:43 | Airtable | `Tool migrations (Box, Airtable, ClickUp billing)` | KEEP | historical label examples | |
| research/07-classification.md:45 | Airtable | `Gmail/Airtable/Access Removal single-word tasks` | KEEP | verbatim task names | |
| research/08-opp-clickup-features.md:117 | Josephine | `per-initiative channels (Josephine, Programming)` | REWRITE | | `per-initiative channels (Programming)` |
| research/11-opp-knowledge-governance.md:13 | Josephine | `a second business ("The Josephine")` | REWRITE | | `a page tree unrelated to Sŏn` |
| research/12-opportunity-shortlist.md:130 | Airtable | `Gmail/Airtable tasks` | KEEP | verbatim task names | |

Note: the Airtable KEEPs are task names in the old workspace. If the owner wants Airtable gone from every file, they can be reworded to "tool-account tasks"; none of them cite Airtable as a figure source.

Not hit by the regex but worth knowing: no Jun, June Shim, Sanctuary, experiential, Home Folder, sync-profiles, old repo names or Business Strategies Notebook outside exports/.

## 3. HOLD-RAW (exports/, per file: terms and counts)

All paths under `exports/`. Owner decides delete vs archive folder. Terms and counts:

| file | terms (count) |
|---|---|
| 2026-09-16-baseline/REPORT.json | Master Pointer Index (3) |
| 2026-09-16-baseline/VERIFY.md | Keychain (1) |
| 2026-09-16-baseline/docs/2ky45bmy-16833.json | Airtable 19, Josephine 16, 2ky45bmy-16833 9, Master Pointer Index 6, Home Folder 3, Replacement Queue 3, Pullman 2, 2ky45bmy-11873 2, Business Strategies Notebook 1 |
| 2026-09-16-baseline/docs/Sŏn_Master_Pointer_Index_Inventory.md | same profile as above (Airtable 19, Josephine 16, MPI 6, 16833 x3, Home Folder 3, Replacement Queue 3, Pullman 2, 11873 x2, BSN 1) |
| 2026-09-16-baseline/docs/2ky45bmy-16873.json | Josephine 15, experiential 12 + Experiential 7, Jun 11, Airtable 5, Pullman 3, Event Co 1, 11873 1, BSN 1 |
| 2026-09-16-baseline/docs/Claude_Project_Review.md | identical profile to 16873.json (Josephine 15, experiential 19, Jun 11, Airtable 5, Pullman 3, Event Co 1, 11873 1, BSN 1) |
| 2026-09-16-baseline/docs/2ky45bmy-17093.json | Airtable 15 |
| 2026-09-16-baseline/docs/Technology_OS_Build_Hub.md | Airtable 15 |
| 2026-09-16-baseline/docs/2ky45bmy-17233.json | Airtable 2, experiential 1 |
| 2026-09-16-baseline/docs/Scaling_People_Translation_Program.md | Airtable 2, experiential 1 |
| 2026-09-16-baseline/docs/2ky45bmy-17253.json | Airtable 5, experiential 6 |
| 2026-09-16-baseline/docs/Sŏn_Operating_System.md | Airtable 5, experiential 6 |
| 2026-09-16-baseline/docs/_index.json | Pullman 5, MPI 1, 16833 1, Josephine 1, Experiential 1 |
| 2026-09-16-baseline/tasks/founding-punch-list.json | Airtable 72, Jun 31, Josephine 16, experiential 6, Experiential 3, BSN 3, Home Folder 3, MPI 3, Pullman 1 |
| 2026-09-16-baseline/tasks/carryover-register.json | Airtable 9 |
| 2026-09-16-baseline/tasks/saas-catalog.json | Airtable 4, Event Co 3 |
| 2026-09-16-baseline/tasks/saas-map.json | Airtable 4, Event Co 1 |
| 2026-09-16-baseline/tasks/capture-901313751988.json | Pullman 1 |
| docs-map-2026-09-17.json | Pullman 5, MPI 1, 16833 1, Josephine 1, Experiential 1 |
| investor-build-report-2026-09-19.md | Josephine 1 (line 29, "Nothing related to The Josephine was touched") |
| previews/c-classification.md | Airtable 14, Jun 1, Josephine 1 |
| previews/deleted-scaling-people-translation-program.json | Airtable 15 |
| previews/followups-to-move.json | Airtable 2, Jun 2, BSN 1 |
| previews/followups-moved.json | Airtable 1, Jun 1 |
| previews/a-investor-migration.md | Airtable 1, Jun 1 |
| previews/saas-duplicates.md | Airtable 1 |

The Jun counts in baseline docs and tasks need a per-line check by whoever acts: Claude_Project_Review.md / 2ky45bmy-16873.json hold "Jun" 11 times (likely "Jun" as a person's short name or a month; cannot assume). Flag: docs/2ky45bmy-16873.json is the Claude Project Review doc and contains the Pullman (3), Josephine (15) and Jun (11) content; it is the single largest out-of-scope carrier here. Items touching Business Strategies Notebook / 2ky45bmy-11873 (16833, 16873, Master Pointer Index Inventory, Claude_Project_Review.md, founding-punch-list.json, followups-to-move.json) are HOLD-V7: do not propose deletion on that basis alone.

## 4. Surprising

1. `kb/cu.py` and `scripts/cu.py` are byte-identical (diff clean). One copy should go (suggest keeping scripts/cu.py, which `meeting_transcript.py` imports).
2. `kb/from-build-out-2026-09-28.md` is an unprocessed merge leftover (its own header says merge then delete); it is a near-copy of `kb/clickup-knowledge-base.md`.
3. The Pullman exposure outside raw exports is one line (`audit/events.md:4`, "Pullman Market" as a sponsor lead). Inside exports, docs-map and _index.json each list five Pullman-titled pages (for example "Pullman Perks - Meeting 1", "Brandon x Ali- Pullman Market", "Concierge at Pullman"). Those are Pullman consulting material, not a bio credential; they should not survive as working context.
4. `exports/docs/2ky45bmy-16873.json` and `Claude_Project_Review.md` are duplicates of one doc (JSON and Markdown renderings), as are `2ky45bmy-16833.json` / `Sŏn_Master_Pointer_Index_Inventory.md`, `2ky45bmy-17093.json` / `Technology_OS_Build_Hub.md`, `2ky45bmy-17253.json` / `Sŏn_Operating_System.md`, `2ky45bmy-17233.json` / `Scaling_People_Translation_Program.md`. Deleting one rendering of each halves the raw surface.
5. `exports/` holds `Operating Agreement` and `Finance and Technology Seat` doc exports per `scripts/export_baseline.py` DOCS list, plus an Operating Agreement Pre-Counsel Brief (build-plan 0.2). If these landed under `exports/docs/`, they are founder-only material under `company/`. The grep did not hit them, so I did not open them; check `ls exports/2026-09-16-baseline/docs` and `exports/shell-pages` before the founder/company split.
6. No investor documents and no profile `_source` files are in this path, so no REPORT or HOLD-PROFILE rows apply.
