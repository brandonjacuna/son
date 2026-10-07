# Cleanup allowlist

Every hit of the phase 1 cleanup terms that stays in the repo, and why. A sweep greps the terms in `memory/audits/cleanup-sweep/` (term list at the top of each report) and treats any hit not covered here as new work. Built 2026-10-07 (phase 1, session A). Classification detail per hit: `memory/audits/cleanup-sweep/*.md`.

## Repo-wide
- memory/decisions.md, memory/briefs/**, memory/audits/**, memory/plan.md, memory/state.md, memory/threads.md | all terms | they record the cleanup rules and open questions
- CLAUDE.md (root) | Pullman, experiential | scope rule itself
- nerve/data/** | Josephine House, Jun | public Austin inspection data and month names (Josephine House is an unrelated Clarksville restaurant; Brandon 2026-10-07)
- .claude/hooks/guard.py:5 | son-build | docstring comment; the file is protected and changes only after Brandon's unlock phrase


### Part: Allowlist part: clickup-build-nerve-brand-other

Format: path | term | reason

### KEEP

- company/workstreams/clickup-system/audit/founding-son.md:50,61,70 | Airtable | verbatim ClickUp task names in an audit record
- company/workstreams/clickup-system/DECISIONS.md:129 | Airtable | verbatim task names
- company/workstreams/clickup-system/blueprint/00-blueprint.md:200 | Airtable | verbatim task names
- company/workstreams/clickup-system/blueprint/02-workspace-structure.md:185 | Airtable | verbatim task names
- company/workstreams/clickup-system/research/00-digest.md:139 | Airtable | verbatim task names
- company/workstreams/clickup-system/research/07-classification.md:43,45 | Airtable | historical label examples and task names
- company/workstreams/clickup-system/research/12-opportunity-shortlist.md:130 | Airtable | verbatim task names
- company/workstreams/clickup-system/blueprint/05-build-plan.md:17 | Master Pointer Index | historical record of a finished export (2026-09-16)
- company/workstreams/clickup-system/audit/technology.md:21 | Master Pointer Index | names the retired pointer doc as retired, superseded by repo profiles/
- company/workstreams/clickup-system/scripts/cu.py:5 | Keychain | labelled secondary Mac fallback; CLICKUP_API_TOKEN is read first
- company/workstreams/clickup-system/scripts/export_baseline.py, scripts/meeting_transcript.py | Keychain (code, `security`) | env var read first; Mac keychain kept as secondary fallback in code
- company/workstreams/clickup-system/logs/ (dated logs, e.g. logs/2026-10-04.md:3) | Keychain | dated history, not edited
- company/workstreams/build-out/kb/bar/tobin-ellis/toc.yaml:70 | Experiential | book chapter topic, generic English
- company/workstreams/build-out/CLAUDE.md:54 | experiential | exclusion rule
- company/workstreams/nerve/scripts/build_digest.py:461 | Jun | month abbreviation
- company/workstreams/nerve/config/peers_sources.md:20 | Jun | month
- company/workstreams/nerve/data/digests/2026-09-28.md, 2026-09-28.section9.md | Jun | "Jun to Aug 2026" month range
- company/workstreams/nerve/data/store/current/atx_inspections.csv | Josephine | public City of Austin inspection data (Josephine House venue, Josephine St). Confirmed unrelated (Brandon, 2026-10-07).
- company/workstreams/nerve/data/store/current/tabc_licenses.csv | Josephine, Event Co | street name and "Event Collective LLC" (regex false positive), public licence data
- company/brand/design-system/readme.md:135, _ds_bundle.js:44, adherence/check-copy.mjs:25, uploads/Design System Guidelines.md:308 | experiential | copy-lint forbidden vocabulary
- memory/threads.md:7, memory/context.md:10, memory/plan.md:9 | Airtable, Jun, Josephine, Pullman, experiential | states or describes the rules / parked thread
- memory/decisions.md (lines 7, 9, 10, 11, 15) | various | append-only decision log
- memory/state.md:9 | son-nerve | live to-do to archive the retired repos; drop once archived
- memory/briefs/ (1-cleanup.md, 3-profiles.md, 5-workstreams.md) | various | briefs describing the cleanup
- memory/audits/ (2026-10-07-readiness.md, cleanup-sweep/*, cleanup-allowlist-parts/*) | various | audit records
- prompts/chat-handoff.md:9 | Pullman, Josephine, Sanctuary | instruction that strips these terms from old chats
- prompts/scheduled/weekly-tech-digest.md:23 | Airtable | watched vendor only (owner decision)
- CLAUDE.md:30,35 | Airtable, Pullman, Josephine, Sanctuary | the routing and exclusion rules

### HOLD-PROFILE

None.

### HOLD-V7

- memory/state.md:28 | Business Strategies Notebook, 2ky45bmy-11873 | open owner question: is the V7 notebook still canon

### HOLD-BRAND

- company/brand/design-system/guidelines-deck/Son Guidelines Deck.html (lines 6, 28, 1010) | experiential | title, h1, forbidden-lexicon sentence; brand session decides
- company/brand/design-system/guidelines-deck/Son Guidelines Deck-print.html (lines 6, 28, 1010) | experiential | print twin; change both together
- company/brand/design-system/uploads/Son Brand Guidelines v1 (1).md:78,663 | experiential | forbidden category and lexicon list

### REPORT

None.

### Part: Allowlist part: learning-studio

Date 2026-10-07. Path: company/workstreams/learning-studio. Format: `path | term | reason`.

### KEEP

- company/workstreams/learning-studio/research/ (position-paths/modules-service-food-menu.md, modules-house-compliance-systems.md, modules-leadership-admin-culinary.md; phase2-working/06-draft.md, 07-panel-architect-osa-realist.md, 12-back-of-house.md; module-discovery-2026-09.md, intake-2026-09.md, starting-structure-2026-09.md) | Airtable | rewritten text reads "unbound until a source is chosen (Airtable retired)" or "(source unbound; Airtable retired)"; the term is the retirement note, not a source
- company/workstreams/learning-studio/CLAUDE.md (2 lines), canon/standing-rules.md:21, canon/pointers.md (last paragraph), framework/lifecycle.md:13, framework/bindings.md:19 | Airtable | same retirement note
- company/workstreams/learning-studio/framework/system-design.md D26 (amended decision record, "Amended 2026-10-07 (Brandon)" line) | experiential | amendment text prescribed by Brandon; D26 original text untouched
- company/workstreams/learning-studio/_salvage/ (README.md, skills/identify/SKILL.md, skills/sync-profiles/SKILL.md) | Airtable, sync-profiles, Replacement Queue, Master Pointer Index, 2ky45bmy-16833, 2ky45bmy-11873 | salvaged tooling, inert until phase 5; README states the supersession

### HOLD-PROFILE

- company/workstreams/learning-studio/profile-builds/README.md | Replacement Queue | profile mechanics, phase 3
- company/workstreams/learning-studio/profile-builds/RUNBOOK.md | Airtable, sync-profiles, Replacement Queue | profile mechanics, phase 3 (only the son-learning-studio repo-name line was edited)
- company/workstreams/learning-studio/profile-builds/hospitality-craft-educator/ (01-corpus, 04-draft, 05-tagged, 06-revised, 06-validation) | Airtable, Replacement Queue | profile build stage files
- company/workstreams/learning-studio/profile-builds/practice-simulation-designer/ (04-draft, 05-tagged, 06-revised, 06-validation) | Airtable, Replacement Queue | profile build stage files
- company/workstreams/learning-studio/profiles/README.md | sync-profiles, 2ky45bmy-16833, Master Pointer Index, Replacement Queue | profile mechanics, phase 3
- company/workstreams/learning-studio/profiles/manifest.yaml | sync-profiles | profile mechanics, phase 3

### HOLD-V7

- company/workstreams/learning-studio/canon/pointers.md:12 | Business Strategies Notebook, 2ky45bmy-11873 | V7 canon status is an open owner question
- company/workstreams/learning-studio/profile-builds/hospitality-craft-educator/01-corpus.md, 04-draft.md, 05-tagged.md, 06-revised.md | Business Strategies Notebook, 2ky45bmy-11873 | V7 pointer inside profile files

### HOLD-BRAND

- company/workstreams/learning-studio/framework/skill-web-design-language.md (lines 3, 7, 9, 624) | Experiential | header note added; values stand until phase 1 session B re-sources them to the brand canon line

### REPORT

- company/workstreams/learning-studio/research/ (starting-structure-2026-09.md:599 and others) | Korean terms from the Brand Guidelines (Jaeyeonmi, Mahk, Hangul) | not canon pending brand review; no term hit, noted for the owner

### Part: Allowlist part: operations

Paths relative to `company/workstreams/operations/` unless noted. Grep scope: company/workstreams/operations, founders/operations-manual (no hits in founders/operations-manual).

### KEEP
- .gitignore:11 | .clickup_token | defensive ignore pattern that prevents committing a token
- output/s03/operating-system-page.md:817 | Airtable | verbatim white paper quote (WP p.21); retirement note added on line 819
- output/s03/operating-system-page.md:819 | Airtable | the added line "(Airtable is retired; financial figures come only from the Investor Review workbook.)" (verbatim quote with retirement note)
- output/s05/operating-system-page.md:260 | experiential | generic English word on a banned-vocabulary list
- RECONSIDERATION-PLAN.md:9 | experiential | "The experiential guidelines are a Box reference file only" (matches root CLAUDE.md scope rule)
- sources/extraction/** (all hits: Airtable, experiential, .clickup_token, son-operational-buildout, Pullman) | verbatim provenance, prior session records. Includes sources/extraction/s13/cu.py, which now reads CLICKUP_API_TOKEN first and keeps the old file path only as fallback (line 3).

### HOLD-PROFILE
- profiles/hospitality-operations-realist.md, profiles/organizational-systems-architect.md, profiles/people-systems-designer.md | Airtable, Business Strategies Notebook, 2ky45bmy-11873 | profile content, no edits
- profiles/learning-and-development/{educational-materials-author-and-editor,highscope,instructional-designer,learner-advocate,tbri}.md | Airtable, Business Strategies Notebook, 2ky45bmy-11873, experiential (generic pedagogy in highscope and instructional-designer) | profile content, no edits

### HOLD-V7
- CLAUDE.md:109 | Business Strategies Notebook, Airtable | ignore-instruction about V7 and retired tool; notebook canon status open
- CLAUDE.md:124 | Business Strategies Notebook, 2ky45bmy-11873 | Excluded list entry
- reference/standing-rules.md:77 | Business Strategies Notebook, 2ky45bmy-11873, Airtable | exclusion list; delete "Airtable," once V7 is ruled on
- reference/standing-rules.md:95 | 2ky45bmy-11873 | V7 notebook row

### HOLD-BRAND
(none)

### REPORT
- sources/son-investor-white-paper-sept-2026.pdf | Pullman, Airtable | investor document, no edits. Pullman sentence at about text line 102 ("He consulted at Pullman Market with the group behind Emmer and Rye"); Airtable at about line 876 ("The data layer is Airtable as the hub for everything that is not CRM"). Owner decides on a paper revision.
- sources/extraction/s05/white-paper.txt and sources/extraction/s01/record.md:53 | Pullman, Airtable | text copies of the same white paper content (also under KEEP as verbatim provenance)

### Part: Allowlist part: founders and profiles

### HOLD-PROFILE (phase 3 rewrites these)
- profiles/_source/** (35 files) and founders/profiles/_source/** (11 files) | Airtable, Sŏn Home Folder, Master Pointer Index, Business Strategies Notebook, 2ky45bmy-11873, Josephine | verbatim Box baseline. Phase 3 MUST cut the 17 Josephine lines in 12 files (the compliance 506(b) and Market Competitive Analyst profiles need a rewrite, not a strike) and replace Airtable as the figures source. See `memory/audits/cleanup-sweep/founders-profiles.md`.

### REPORT (investor material, never edited by a cleanup)
- founders/capital-raise/working-files/** | Airtable | August 2026 Airtable-era working files, marked superseded by README.md in that folder (Brandon, 2026-10-07)
- company/workstreams/operations/sources/son-investor-white-paper-sept-2026.pdf | Pullman, Airtable | Pullman appears once as a bio credential ("He consulted at Pullman Market with the group behind Emmer and Rye."), passed by Brandon 2026-10-07; Airtable named as the data hub, report only
