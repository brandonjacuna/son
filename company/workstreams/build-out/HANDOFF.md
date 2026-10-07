# HANDOFF: build-out workspace into the son repo

Prepared 2026-10-07 for Brandon John Acuña-Cardona. Source: the construction-mode workspace, built 2026-09-28 (foundation) and extended the same day (Tobin Ellis bar knowledge base).
Destination: `company/workstreams/build-out/` in the unified `son` repo, per the rebuild plan decision 1 (company/ vs founders/ boundary).

---

## 1. Current state

| Item | State |
|---|---|
| Build-out phase | **P0-concept.** `lease_signed: false`. `gate_log` empty. Site candidate 207 E St. Elmo Rd, Austin, not leased. |
| Repo status | Delivered as a zip on 2026-09-28. There is no record that it was published to GitHub or that KICKOFF.md was run. Treat it as never run. |
| Plan tier | Claude Max 5x (confirmed). |
| Equipment records | None yet. Schema, template, and validator are in place. |
| Models | None yet. `models/src/` is empty. |
| Knowledge base | `kb/bar/tobin-ellis/` public layer: principles, dimensions, a 25-point Sŏn bar review checklist, 66-topic book map (27 Priority A). Book notes: 0 of 66. No other kb files yet. |
| Research | `research/raw/` holds the 2026-09-28 construction-mode blueprint (restored from the chat report) and the Tobin Ellis source scan. |
| ClickUp | Nothing created. Property Capture list (901327291277) is allowlisted. Nine pages (eight distinct Sŏn build-out guides: exhaust, fire suppression, plumbing and grease, flooring, HVAC and acoustics, electrical and lighting, outdoor pit, bar millwork) found in the ClickUp doc "Claude Project Review" and listed by page ID in KICKOFF step 4; not yet imported. |
| Box | Nothing created. Target folder `Sŏn / 04. Property and Build-Out` (420132927884). |

### What was tested (2026-10-07, both layouts)
- `tests/guard_selftest.py`: 17 of 17 guard decisions correct in the standalone layout and in the unified layout (`.claude/` at root, build-out under `company/workstreams/build-out/`).
- Unlock and advance: refused without the phrase, refused when skipping a phase, advanced one step with the phrase, wrote the gate log, committed, closed the window. Worked when run from inside `company/workstreams/build-out/` with no project variable set.
- Session-start and prompt banners show the build-out phase and root in both layouts.
- Writes outside the build-out root (for example under `founders/`) are not affected by phase rules.
- Workflow YAML parses. Equipment validator passes and fails correctly.

### Not tested
- Hooks wired into a live Claude Code session (scripts were fed sample events directly). KICKOFF steps 1 and 2 test this.
- `scripts/setup_cloud.sh` package installs on a cloud environment.
- Watcher fetches from GitHub runners. From the build sandbox, 4 of 10 watched sites (NAFEM, HostMilano, INTERNORGA, Tales of the Cocktail) refused scripted requests with HTTP 403; they may refuse runners too.

---

## 2. Changes made in this handoff
1. **Layout-aware hooks and scripts.** `guard.py`, `prompt_hook.py`, `session_start.sh`, and `advance_phase.py` now find the build-out root automatically: `$SON_BUILD_DIR` if set, else the repo root, else `company/workstreams/build-out/`. `.claude/` and the unlock file stay at the repo root.
2. **Workflows** carry a `defaults.run.working-directory` line set to `.`; change it to `company/workstreams/build-out` in the unified repo.
3. **Name.** Brandon John Acuña-Cardona added to CLAUDE.md and README, with the rule that legal documents such as leases and contracts use Brandon John Acuña, and permit or license applications get asked.
4. **Canon.** The cuisine descriptor was removed from the build-out CLAUDE.md, and one monitoring tag was made neutral, per rebuild plan decision 5. The Seoul Food trade show and Korea as an equipment-import market stay, since they are sourcing facts, not brand canon.
5. **Exclusion scrub.** Every file was searched for the out-of-scope names in the Sŏn scope rules. None were present before or after. KICKOFF step 4 imports only nine named Sŏn pages.
6. **Restored and added files:** `research/raw/2026-09-28-construction-mode-blueprint.md` (existed only as a chat report), `tests/guard_selftest.py`, `.gitkeep` files for `models/src/` and `tests/profiles/`, decisions/open.md items 8 and 9.
7. **KICKOFF.md** rewritten: paths relative to the build-out root, the full nine-page ClickUp seed list with exclusions, a rule to drop dollar figures from imported guides (figures come only from the Investor Review workbook), and a bar checklist step.

---

## 3. Landing map

| Old workspace path | son repo path | Action |
|---|---|---|
| `CLAUDE.md` | `company/workstreams/build-out/CLAUDE.md` | Move. Loads when Claude works in that folder. |
| `PHASE.yaml`, `phases/`, `models/`, `equipment/`, `library/`, `intake/`, `research/`, `kb/`, `codes/`, `monitoring/`, `decisions/`, `clickup/`, `scripts/`, `tests/`, `README.md`, `KICKOFF.md`, `HANDOFF.md` | `company/workstreams/build-out/...` | Move as is. Skills and commands use paths relative to this root. |
| `.claude/hooks/*` | `.claude/hooks/` | Move. Layout-aware. |
| `.claude/settings.json` | `.claude/settings.json` | Merge the `hooks` block only. Do not carry `"model": "sonnet"` unless the whole repo should default to Sonnet. |
| `.claude/agents/*` (2 agents) | `.claude/agents/` | Move. Check names against the P4 profile system. |
| `.claude/skills/*` (6 skills) | `.claude/skills/` | Move. Check names against P5 operating skills. |
| `.claude/commands/*` (6 commands) | `.claude/commands/` | Move. Check `/deep`, `/gate`, `/capture` against unified commands. |
| `.claude/templates/agent.md` | Fold into the P4 profile template | Merge. |
| `.github/workflows/watch.yml`, `validate.yml` | `.github/workflows/build-out-watch.yml`, `build-out-validate.yml` | Rename, set working directory to `company/workstreams/build-out`, add a `paths: [company/workstreams/build-out/**]` filter to the validate trigger. |
| `.gitattributes`, `.gitignore` | repo root | Merge lines. |
| `scripts/setup_cloud.sh` | Unified cloud environment setup script | Merge the package list (git-lfs, pyyaml, jsonschema, ezdxf, ifcopenshell, build123d). |
| `clickup/cu.py`, `clickup/knowledge-base.md` | Possibly shared at repo level | Decide (M2). |

Add one line to the unified root CLAUDE.md: "Build-out work lives in `company/workstreams/build-out/`. Its skills and commands use paths relative to that folder. Its phase lock is enforced by root hooks."

If the workspace exists as its own GitHub repo, import with history (for example `git subtree add --prefix=company/workstreams/build-out <url> main`), then move `.claude/` and `.github/` up. Otherwise unzip and commit.

---

## 4. Phase system

| Phase | Entry gate | Unlocks |
|---|---|---|
| P0 Concept (current) | default | Research, sandboxes, concept models, capture-list ideas |
| P1 Design | `/lease-signed`, executed lease in Box, Brandon types `LEASE SIGNED CONFIRMED` | `phases/P1-design/`, ClickUp construction space build, P0 to P1 promotion |
| P2 Permitting | Architect engaged, real plans in Box, `/gate P2-permitting` passed, Brandon types `GATE CONFIRMED` | Compliance matrices, permit tracking |
| P3 Construction | Permit issued, same gate pattern | RFIs, submittals, punch, change log |
| P4 Closeout | Certificate of occupancy, same gate pattern | As-builts, O&M to Box, warranty register |

Until `lease_signed: true`, all build-out work is concept work labeled "CONCEPT / NOT FOR CONSTRUCTION."

---

## 5. Guard hook rules

| Trigger | Rule | Result |
|---|---|---|
| Write/Edit into `phases/<later phase>/` | Phase is after the current one | Blocked |
| Write/Edit `PHASE.yaml` or `scripts/advance_phase.py` | No unlock window | Blocked |
| Write/Edit `.claude/hooks/`, `.claude/state/`, `.claude/settings.json` | No unlock window | Blocked (repo-wide in the unified repo, see M4) |
| Bash touching `PHASE.yaml`, `.claude/state`, `.claude/hooks`, `advance_phase` | Not a read-only command, no unlock window | Blocked |
| Bash naming a locked `phases/P*` folder | Not read-only | Blocked |
| ClickUp read tools | Any | Allowed |
| ClickUp create task on an allowlisted capture list | Any phase | Allowed |
| Any other ClickUp write (create, update, move, send, execute, attach) | Any phase | Asks Brandon |
| ClickUp delete or merge | Any | Blocked |
| Unlock window | Opens only when Brandon's typed prompt contains `LEASE SIGNED CONFIRMED`, `GATE CONFIRMED`, or `PHASE CONTROLS UNLOCK`; lasts 10 minutes; closed by a successful advance | |

The guard catches mistakes; it is not a security boundary. A command that builds a path at runtime can slip past the string checks. Real protection for `PHASE.yaml` in the unified repo: branch protection on main plus a CODEOWNERS entry so any change to it needs Brandon's review.

---

## 6. Model routing (build-out)

| Work | Model |
|---|---|
| Classifying files, OCR, specs into YAML, diffs, file moves, schema fixes | Haiku (subagent) |
| Default design work, modeling scripts, schedules, research summaries, interviews | Sonnet (session default in build-out work) |
| Code interpretation, live-fire ventilation, cross-trade clash review, routine gate reviews | Opus (subagent) |
| Lease-signed gate, first full layout at the real site, safety-critical new profiles, a problem Opus failed twice | Fable, only through `/deep`; never auto-escalated |

Alignment with Brandon's standing rule (Fable for high-level thinking, strategy, and orchestrating agents only): consistent. In unified chat sessions, Claude says before doing non-Fable work so he can switch models; inside Claude Code the per-agent `model` line does that switching automatically.

---

## 7. Open decisions

### Build-out (from `decisions/open.md`)
1. Where the ClickUp construction space lives.
2. Box subfolders under `04. Property and Build-Out` (proposal: `_Intake`, `P0 Concept`, `P1 Design`, `Handoff`, `Spec Sheets`, `Reference`).
3. What the architect, MEP engineer, and GC draft in.
4. Live-fire unit: listed equipment or site-built.
5. When to buy SketchUp Pro.
6. Fabricator file formats and machine limits.
7. Product Capture and Technology Capture list IDs.
8. Bar task lighting color temperature (6000K vs 4000K).
9. Which duplicate plumbing / grease interceptor guide in ClickUp is current.

### Migration (new)
- **M1. ClickUp ask rule scope.** In the unified repo the guard asks before every non-capture ClickUp write, everywhere, including review drafts that rebuild plan decision 3 sends to ClickUp. Options: keep it repo-wide (safer, more prompts), or limit the ask to build-out work and keep delete/merge blocked repo-wide.
- **M2. Shared ClickUp tooling.** Keep `clickup/cu.py` and `knowledge-base.md` inside build-out, or promote them to a repo-level `tools/clickup/` for all areas.
- **M3. Profile creation.** `profile-forge` (four stages, token budgets) vs the P4 profile system pipeline. Recommendation: P4 is the master; feed profile-forge's stage design into P4 and retire the duplicate. **Resolved 2026-10-07 (Brandon):** profile-forge retired; its ideas live in the root `profile-build` skill.
- **M4. Settings protection.** The guard blocks edits to `.claude/settings.json` repo-wide without an unlock phrase. Keep, or scope to the hooks block.
- **M5. Command and skill names.** Resolve any collision between `/deep`, `/gate`, `/capture`, `/sandbox`, `/promote`, `/lease-signed` and the P5 operating skills (red-team, thread-log, session-close, task-tree, kb-refresh).
- **M6. Build-out kb location.** Keep at `company/workstreams/build-out/kb/` (works with current skill paths) or move to `company/kb/build-out/` (needs path edits in 3 skills and 2 commands).

---

## 8. Planned but not built

**Profiles:** 16 of 18 (bar-designer, kitchen-layout, ventilation-fire, plumbing-water, electrical-power, lighting, av-network, hvac-comfort, materials-finishes, storage-shelving, codes-permitting, fabrication-dfm, import-certification, innovation-scout, clash-reviewer, kb-consolidator). Roster with models and scope: blueprint section 5. `bar-designer` is referenced by the Tobin Ellis kb and should be first. The Sŏn Home Base section of the ClickUp review doc also holds design-side profiles (lighting designer, acoustic engineer, interior architect, industrial designer) worth reviewing in P4; they are not imported.

**Skills and commands:** export-handoff, code-check, a fabrication skill with the five-step validation ladder, `/digest`.

**Geometry and exports:** parametric bar module library (build123d), IFC/DXF/PDF/equipment-schedule export pipeline, CI regeneration of exports from `models/src/`, CI geometry checks. `/promote` refers to export regeneration that does not exist yet.

**Local Mac setup:** Blender + Bonsai MCP, FreeCAD MCP, build123d-mcp, Git LFS; round-trip test cloud to branch to Mac render.

**Monitoring:** weekly code-change Routine (Sonnet), innovation feed Action plus Haiku digest Routine, monthly equipment-landscape merge. Replacement URLs or RSS feeds for the four sites that refuse scripted fetches.

**ClickUp and Box:** `clickup/build_space.py` (the space blueprint is a draft only), capture list IDs, Box subfolders including `_Intake` (the intake skill already points to it).

**Knowledge:** the nine ClickUp compliance guides (KICKOFF step 4), Tobin Ellis book notes (27 Priority A topics first), unmined Ellis interviews (Serves You Right #81, Shawn Soole, Hoshizaki booth parts 1 and 2), profile test scenarios in `tests/profiles/`.

**Verification debt:** every row in `codes/register.yaml` is `secondary` and must be checked against primary city and state sources before any compliance decision.

---

## 9. Red team

Scaled to stakes: light on concept tooling, harsh on compliance and the phase lock.

| Risk | Severity | Mitigation |
|---|---|---|
| Code register used for a real compliance call while still `secondary` | High | Verify each row at the source before P1; codes-permitting work runs on Opus with citations |
| Imported ClickUp guides may predate Austin's July 10, 2025 code change and cite old editions | High | KICKOFF step 4 flags conflicts against the register; treat guide code citations as unverified |
| Bar millwork guide carries budget figures that conflict with the figures rule | Medium | KICKOFF strips dollar figures on import |
| Phase lock bypassed by a runtime-built path | Medium | Branch protection and CODEOWNERS on `PHASE.yaml` |
| Unlock phrase opens the window if it appears in pasted text | Low | Phrases are distinctive; window is 10 minutes and closes on use |
| Tobin Ellis dimensions mostly come from Perlick training, not Ellis's book | Medium | Every row is tagged; the book overrides on ingest |
| Pricing, plan limits, and Routine caps are secondary-source | Low | Recheck before buying or relying |
| Community CAD MCP servers can execute arbitrary code | Medium | Local only, pinned versions, reviewed upgrades |
| ClickUp ask rule creates prompt fatigue repo-wide, leading to rubber-stamp approvals | Medium | Decide M1 |

---

## 10. Import prompt (paste into a Claude Code session on the son repo)

```
Import the construction workspace into this repo. The zip contents are in <path>.
Read <path>/HANDOFF.md first and follow its landing map (section 3) exactly.

1. Move build-out files to company/workstreams/build-out/. Move .claude/hooks, agents, skills, commands to the root .claude/, merging, never overwriting. List any name collision and ask me (one pop-up per collision) before resolving it.
2. Merge only the hooks block into the root .claude/settings.json. Do not add a default model.
3. Rename the two workflows with a build-out- prefix, set working-directory to company/workstreams/build-out, add a paths filter to validate.
4. Merge .gitattributes, .gitignore, and the setup_cloud.sh package list.
5. Add the one-line build-out pointer to the root CLAUDE.md.
6. Run python3 company/workstreams/build-out/tests/guard_selftest.py and python3 company/workstreams/build-out/scripts/validate_equipment.py. Report pass/fail only.
7. Commit on a branch named import/build-out and open a PR. Do not merge it.
8. Add the migration decisions M1 to M6 from HANDOFF section 7 to the repo's decision log as open items.
Use Opus for this; no Fable. No em dashes.
```

Then run `company/workstreams/build-out/KICKOFF.md` in a new session.

---

## 11. Package contents
79 files, including empty-folder placeholders. Root: CLAUDE.md, HANDOFF.md, KICKOFF.md, README.md, PHASE.yaml, .gitattributes, .gitignore. Folders: `.claude/` (3 hooks, settings, 2 agents, 6 commands, 6 skills, template), `.github/workflows/` (2), `clickup/` (4), `codes/`, `decisions/` (2), `equipment/` (schema, template), `kb/` (Tobin Ellis sub-KB, 7 files), `library/`, `models/`, `monitoring/`, `phases/` (P0 with 8 area folders, P1 to P4 locked), `research/raw/` (2), `scripts/` (4), `tests/` (guard self-test).
