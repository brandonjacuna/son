# Cleanup sweep: other paths

Paths: company/workstreams/build-out, company/workstreams/nerve, company/brand, memory, prompts, .claude, CLAUDE.md, scripts. 135 raw hits. Read-only audit.

## 1. Summary

| verdict | count |
|---|---|
| KEEP | 101 |
| REWRITE | 25 |
| HOLD-BRAND | 8 |
| HOLD-V7 | 1 |
| DELETE | 0 |
| HOLD-RAW / HOLD-PROFILE / REPORT | 0 (none in these paths) |

No hits for Jun Shim, Sanctuary or Pullman outside rule text, and none for Home Folder, Master Pointer Index, or 2ky45bmy-16833. Replacement Queue and /sync-profiles appear only in memory/briefs and memory/audits.

## 2. Per-line: REWRITE

| path:line | term | snippet | verdict | reason | proposed replacement |
|---|---|---|---|---|---|
| company/workstreams/build-out/scripts/watch.py:18 | son-build | `"User-Agent": "Mozilla/5.0 (son-build watcher)"` | REWRITE | Cosmetic header string only. No repo slug, path, or logic reads it. | `headers={"User-Agent": "Mozilla/5.0 (son watcher)"}` (only edit; no workflow change needed) |
| company/workstreams/nerve/scripts/common.py:17 | son-nerve | `USER_AGENT = "son-nerve/0.1 (Austin hospitality research; human-scale use)"` | REWRITE | Header string only; no other code reads it. `son-nerve` is the retired repo name. | `USER_AGENT = "son-nerve-digest/0.1 (Austin hospitality research; human-scale use)"` (or `"son/0.1 (nerve digest; Austin hospitality research; human-scale use)"`) |
| company/workstreams/nerve/CLAUDE.md:1 | son-nerve | `# son-nerve` | REWRITE | Old repo name. | `# Nerve` |
| company/workstreams/nerve/CLAUDE.md:8 | Airtable | `- **No Airtable.** We have moved off it.` | REWRITE | Airtable retired; state the figures source instead. | `- **Figures.** Financial figures come only from the current Investor Review workbook in Box (Sŏn / 02. Capital Raise).` |
| company/workstreams/nerve/BRIEF.md:1 | son-nerve | `# son-nerve: Build Brief for the Weekly Industry Digest` | REWRITE | Old repo name. | `# Nerve: Build Brief for the Weekly Industry Digest` |
| company/workstreams/nerve/BRIEF.md:14 | Airtable | `- **No Airtable.** We have moved off it.` | REWRITE | Same as nerve/CLAUDE.md:8. | Same replacement as nerve/CLAUDE.md:8. |
| company/workstreams/build-out/README.md:1 | son-build | `# son-build` | REWRITE | Old repo name. | `# Build-out` |
| company/workstreams/build-out/README.md:11 | son-build | `cd son-build && git init ... gh repo create son-build ...` | REWRITE | The standalone-repo setup (lines 5 to 17) no longer applies. Replace the block. | Replace lines 5 to 17 with: `Setup lives in the root CLAUDE.md. Cloud sessions use the ClickUp and Box connectors (claude.ai Settings > Connectors). Local sessions (Claude Desktop, Code tab, open the son repo) are where Blender and FreeCAD get driven. Paste KICKOFF.md into the first session.` |
| company/workstreams/build-out/README.md:13 | son-build | `pick son-build, create an environment` | REWRITE | Covered by the block replacement. | See README.md:11. |
| company/workstreams/build-out/README.md:15 | son-build | `open the son-build folder` | REWRITE | Covered by the block replacement. | See README.md:11. |
| company/workstreams/build-out/CLAUDE.md:7 | son-build | `the repo root in the standalone son-build repo, company/workstreams/build-out/ in the unified son repo` | REWRITE | Old repo name. | `Paths in this file are relative to the build-out root, company/workstreams/build-out/ in the son repo. .claude/ sits at the repo root.` |
| company/workstreams/build-out/KICKOFF.md:1 | son-build | `the repo root for a standalone son-build repo, ... in the unified son repo` | REWRITE | Old repo name. | `Paste everything below the line into the first Claude Code session that has the build-out files in place (cloud is fine). Paths are relative to the build-out root, company/workstreams/build-out/.` |
| company/workstreams/build-out/KICKOFF.md:21 | Event Co | `Never read or import the "Event Co" section of that doc (parent page 2ky45bmy-28253) or the profile pages.` | REWRITE | Names the out-of-scope section and its page ID. Fence by allowlist instead. | `Import only the pages listed above. Read no other page of that doc.` |
| company/workstreams/build-out/HANDOFF.md:1 | son-build | `# HANDOFF: son-build into the unified son repo` | REWRITE | Old name. Migration is done; DELETE of the whole file is an option once Brandon confirms (build-out CLAUDE.md pointers section and KICKOFF.md:5 reference it, so drop those pointers too). | `# HANDOFF: build-out workspace into the son repo` |
| company/workstreams/build-out/HANDOFF.md:3 | son-build | `Source: the son-build construction-mode workspace, built in the Sŏn Home Base project ...` | REWRITE | Old name. | `Source: the construction-mode workspace, built 2026-09-28 (foundation) and extended the same day (Tobin Ellis bar knowledge base).` |
| company/workstreams/build-out/HANDOFF.md:41 | Event Co | `...the ClickUp "Claude Project Review" doc also holds an out-of-scope "Event Co" section. KICKOFF step 4 now imports only nine named Sŏn pages and forbids that section.` | REWRITE | Keeps an out-of-scope name in working context. | `5. **Exclusion scrub.** Every file was searched for the out-of-scope names in the Sŏn scope rules. None were present before or after. KICKOFF step 4 imports only nine named Sŏn pages.` |
| company/workstreams/build-out/HANDOFF.md:49 | son-build | `\| son-build path \| Unified son repo path \| Action \|` | REWRITE | Old name. | `\| Old workspace path \| son repo path \| Action \|` |
| company/workstreams/build-out/HANDOFF.md:66 | son-build | `If son-build was ever pushed as its own GitHub repo, import with history (...)` | REWRITE | Old name. | `If the workspace exists as its own GitHub repo, import with history (for example git subtree add --prefix=company/workstreams/build-out <url> main), then move .claude/ and .github/ up. Otherwise unzip and commit.` |
| company/workstreams/build-out/HANDOFF.md:180 | son-build | `Import the son-build construction workspace into this repo.` | REWRITE | Old name. | `Import the construction workspace into this repo.` |
| company/workstreams/build-out/research/raw/2026-09-28-construction-mode-blueprint.md:9 | Keychain | `The Keychain-based cu.py works only on the Mac.` | REWRITE | Mac-only token path. | `The Mac-only cu.py token path does not work in cloud; cloud sessions use the ClickUp connector or CLICKUP_API_TOKEN.` |
| .claude/hooks/guard.py:5 | son-build | `- standalone son-build repo: PHASE.yaml at the repo root` | REWRITE | Docstring only, no code change. Edits under .claude go by pull request. | `- standalone layout: PHASE.yaml at the repo root` |
| company/brand/design-system/AUDIT.md:98 | Airtable | `true figures stay in Airtable/the briefing.` | REWRITE | Airtable retired; figures source rule. | `true figures stay in the Investor Review workbook in Box (Sŏn / 02. Capital Raise).` |
| company/brand/design-system/guidelines-deck/deck.css:2 | experiential | `SŎN — Brand and Experiential Guidelines` (comment) | REWRITE | Pointer/label text; also has an em dash. | `SŎN: Brand Guidelines Deck` |
| company/brand/design-system/uploads/Design System Guidelines.md:7 | experiential | `# This file governs all AI-assisted design for the Sŏn brand and experiential guidelines deck.` | REWRITE | Pointer treats experiential guidelines as canon. | `# This file governs all AI-assisted design for the Sŏn brand guidelines deck.` |
| prompts/scheduled/weekly-tech-digest.md:10 | Airtable | `(3) Stack watch still lists Airtable; Airtable is retired as a Sŏn tool (keep only if tracking it as a vendor is still useful).` | REWRITE | Owner decision: Airtable stays as a watched vendor. Remove the open review item. | Delete item (3) from the review-items sentence (keep (1) and (2)). Optionally append to line 23: `Airtable (watched as a vendor only; not a Sŏn tool)`. |

## 3. Per-line: KEEP

| path:line | term | snippet | verdict | reason |
|---|---|---|---|---|
| memory/audits/2026-10-07-readiness.md (45 hits) | various | audit of the cleanup | KEEP | Records the rules. |
| memory/briefs/1-cleanup.md (11), 3-profiles.md:6,48,51,62 (4), 5-workstreams.md:14 (1) | various | retirement of Replacement Queue, /sync-profiles, no Airtable | KEEP | Describes the cleanup itself. |
| memory/decisions.md (5 hits) | various | decision log | KEEP | Append-only record. |
| memory/state.md:9 | son-nerve etc. | `Archive the old GitHub repos (son-learning-studio, son-operational-buildout, son-nerve; ...)` | KEEP | Live to-do that must name the retired repos. Drop once archived. |
| memory/plan.md:9 | Jun, Josephine, Pullman, experiential, Airtable | Phase 1 row | KEEP | Describes the cleanup. |
| memory/threads.md:7 | Airtable | `Future database tool (Airtable again or other)...` | KEEP | Parked thread. |
| memory/context.md:10 | Airtable | `Airtable is retired.` | KEEP | States the rule. |
| CLAUDE.md:30 | Airtable | `Never from memory, decks, or Airtable (retired).` | KEEP | Routing rule. |
| CLAUDE.md:35 | Josephine, Sanctuary, Pullman, Experiential | Scope and exclusions paragraph | KEEP | The exclusion rule itself; Pullman rule matches the owner decision. |
| prompts/chat-handoff.md:9 | Pullman, Josephine, Sanctuary | `Remove any reference to Pullman Market (except my bio line), The Josephine, Sanctuary...` | KEEP | Instruction that strips these terms from old chats. |
| prompts/scheduled/weekly-tech-digest.md:23 | Airtable | `Airtable (acquired by Bending Spoons, 2026)` | KEEP | Watched vendor (owner decision). |
| company/workstreams/build-out/CLAUDE.md:54 | experiential | `do not add cultural tie-ins or experiential brand material to build-out work` | KEEP | Exclusion rule. Optional tighten: `The Experiential Guidelines are a Box reference file only.` |
| company/workstreams/build-out/kb/bar/tobin-ellis/toc.yaml:70 | Experiential | `topic: "Experiential Nightlife Design"` | KEEP | Book chapter topic, generic English, not the Guidelines. |
| company/workstreams/nerve/scripts/build_digest.py:461 | Jun | comment `"Jun to Aug 2026"` | KEEP | Month. |
| company/workstreams/nerve/config/peers_sources.md:20 | Jun | `winners Jun 15, 2026 (Chicago)` | KEEP | Month. |
| company/workstreams/nerve/data/digests/2026-09-28.md:13,15,70,97,143,145,189 (7) | Jun | `Jun to Aug 2026` | KEEP | Month range. |
| company/workstreams/nerve/data/digests/2026-09-28.section9.md:3 | Jun | `Jun to Aug 2026` | KEEP | Month range. |
| company/workstreams/nerve/data/store/current/atx_inspections.csv:2109,3331,4550,6033,12988,15426,20109 (7) | Josephine | `Josephine House, 1601 Waterston Ave` | KEEP | City inspection record (public data). FLAG: owner to confirm Josephine House is unrelated to "The Josephine". If related, drop the venue from the store and the ingest. |
| same csv:12522,17914 (2) | Josephine | `Carpenter Hotel, 400 Josephine St` | KEEP | Street name in public data. |
| company/workstreams/nerve/data/store/current/tabc_licenses.csv:6704 | Event Co | `Event Collective LLC` | KEEP | False positive of the `Event Co` regex; public licence name. |
| same csv:8813 | Josephine | `408 Josephine Street` | KEEP | Street name in public licence data. |
| company/brand/design-system/readme.md:135 | experiential | Forbidden lexicon list | KEEP | Lint vocabulary, not guidance. |
| company/brand/design-system/_ds_bundle.js:44 | experiential | `LEXICON` regex | KEEP | Copy-lint code. |
| company/brand/design-system/adherence/check-copy.mjs:25 | experiential | `LEXICON` regex | KEEP | Copy-lint code. |
| company/brand/design-system/uploads/Design System Guidelines.md:308 | experiential | Forbidden word list | KEEP | Lint vocabulary. |

## 4. Per-file summary: HOLD-*

| path | terms (count) | verdict | note |
|---|---|---|---|
| company/brand/design-system/guidelines-deck/Son Guidelines Deck.html | experiential (3: lines 6, 28, 1010) | HOLD-BRAND | Title `Brand and Experiential Guidelines`, h1 `Brand and experiential guidelines.`, forbidden-lexicon sentence. Decide in the brand session. |
| company/brand/design-system/guidelines-deck/Son Guidelines Deck-print.html | experiential (3: lines 6, 28, 1010) | HOLD-BRAND | Print twin; change both together. |
| company/brand/design-system/uploads/Son Brand Guidelines v1 (1).md | experiential (2: lines 78, 663) | HOLD-BRAND | `"Experiential platitude"` named forbidden category (78); forbidden lexicon list (663). |
| memory/state.md:28 | Business Strategies Notebook, 2ky45bmy-11873 | HOLD-V7 | Open question to owner: is the V7 notebook still canon. No deletion proposed. |

No HOLD-RAW, HOLD-PROFILE, or REPORT files in these paths.

## 5. Surprising / flags

1. Josephine House (nerve inspection CSV, 7 rows) shares a name with an out-of-scope former project. It is public City of Austin data and was kept, but the owner should confirm it is a different venue. No committed digest mentions it.
2. KICKOFF.md step 4 and HANDOFF.md:41 describe an "Event Co" section and parent page 2ky45bmy-28253 in the ClickUp doc "Claude Project Review". That ClickUp doc itself holds out-of-scope material; the repo only needs to stop naming it. The doc is outside this sweep.
3. watch.py needs only the one-line User-Agent change; it does not use the repo slug elsewhere. nerve common.py has the same shape (header only). Neither affects behavior.
4. The root guard hook blocks any shell command whose text mentions phase or hook controls (my first two shell attempts with such words in the command or heredoc were refused). Edits to .claude/hooks/guard.py (docstring only) go on a pull request as a system change.
5. memory/audits/cleanup-sweep did not exist before this run. No founder-only material found under company/ in these paths.
6. HANDOFF.md (migration record) and the README standalone-repo setup are mostly dead text. Consider deleting HANDOFF.md after Brandon confirms the migration is final.
