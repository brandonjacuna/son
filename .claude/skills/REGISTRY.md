# Skill registry

One owner per trigger. Before adding a skill or command, check its triggers against this table. A new skill whose triggers overlap a row is merged into that row's owner or rejected. Account-provided skills (synced from claude.ai) are listed so nothing in the repo duplicates them.

## Project skills (`.claude/skills/`)
| Owner | Triggers | Scope | Notes |
|---|---|---|---|
| `session-close` | close, wrap up, end the session, context-rot cue | Every session | The only way to end a session that changed anything |
| `thread` | a tangent mid-task: "also", "side note", "what about", "remind me" | Every session | Logs to `memory/threads.md` |
| `chat-handoff` | a package from an old chat in `imports/` | Every session | Not for build-out photos or spec sheets (`intake`) |
| `interview` | any decision or clarification as pop-ups | Every session | Not a selection among design directions on a named piece (`creative-director`) |
| `skill-scanner` | scan, audit, or vet a skill before adoption | Every session | Vendored, see its `SOURCE.md` |
| `red-team` | red team, poke holes, stress test, what breaks, what am I missing; before a draft goes to ClickUp for review; profile-build stage 4 | Every session | Three intensities with a stakes floor (light, standard, harsh). Workers `red-team-critic`, `red-team-merger`, `red-team-judge` in `.claude/agents/`. Replaces the profile-build interim critics (`profile-critic` retired 2026-10-09). Design record in its `SOURCE.md` |
| `profile-build` | build, rebuild, revise, slim, or merge a specialist profile (`/profile-build <slug> [mode]`) | Profiles | User-invoked. Replaces learning-studio `build-profile` and `validate-profile` (salvaged, inert) and `profile-forge` (retired 2026-10-07, M3); final approval after the session B test rebuild |
| `materials-author-editor` | draft the module, write this in library voice, edit or redline a peer draft, update the template, style guide, or forbidden list | Learning studio | Generated from `profiles/learning-and-development/materials-author-editor/skill/`; drafts in the session, the `materials-author-editor` agent reviews cold. Not for brand, investor, or founder copy |
| `hospitality-craft-educator` | walk a service scenario, elicit the craft, build the service standard, next scenario, continue the elicitation | Learning studio | Generated from `profiles/learning-and-development/hospitality-craft-educator/skill/`; staged elicitation with Brandon by pop-up, transcripts to `company/workstreams/learning-studio/research/elicitation/`. Takes precedence over `interview` while a round runs; the agent of the same name turns transcripts into craft |
| `design-brief-translator` | a new Sŏn surface, a reference image offered as a target, or several artifacts in one request, before design starts; skips edits, copy fixes, token changes, internal trackers, investor and founder material | Design | Generated from `profiles/design/design-brief-translator/skill/`; writes the brief and the route to the craft seat, never the artifact. A reference image for a brand surface goes here, not `intake`; property photos stay `intake`. Not for critique (the craft agents) or point of view (`creative-director`) |
| `creative-director` | direct this, which direction, pick one, push this further, it feels safe, each with a named Sŏn surface; is it done, only when a piece is named | Design | Generated from `profiles/design/creative-director/skill/`; frames problems, selects, kills, recommends done, makes nothing. Takes the selection among design directions from `interview`. Not for briefs (`design-brief-translator`), failure review (`red-team`), or copy |
| `intake` | build-out photo, sketch, markup, spec sheet, contract, design idea | Build-out | Not a reference image for a brand surface (`design-brief-translator`) |
| `equipment-record` | equipment YAML from a spec sheet or model number | Build-out | |
| `book-ingest` | reading notes from a reference book | Build-out kb | |
| `consolidate` | merge raw research notes into the kb | Build-out kb | |

## Project commands (`.claude/commands/`)
| Owner | Trigger | Notes |
|---|---|---|
| `/capture` | file an idea to a ClickUp capture list | Allowed in every phase |
| `/deep` | escalate one hard problem to Fable | |
| `/sandbox` | start a build-out design sandbox | Build-out only (creates P0 notes). For any other experiment or system change, create `sandbox/<name>` from `main` by hand |
| `/promote` | promote a build-out sandbox design to `main` | Build-out only. Other sandboxes land through `session-close` |
| `/gate`, `/lease-signed` | build-out phase changes | Brandon only |

## Account-provided (claude.ai sync; do not vendor)
| Owner | Triggers | Why not in the repo |
|---|---|---|
| `anthropic-skills:docx`, `xlsx`, `pdf`, `pptx` | Word, Excel, PDF, PowerPoint files | License forbids copies outside Anthropic's services (decision 2026-10-07) |
| `anthropic-skills:skill-creator` | create, edit, or eval a skill | Already in every session; a repo copy would be a second owner (decision 2026-10-07) |
| `anthropic-skills:docs` | shareable documents (Claude Docs) | Review copies still go to ClickUp per CLAUDE.md routing |
| `artifact-design` | a claude.ai artifact's page contract | Account skill. For a Sŏn surface, `design-brief-translator` decides whether an artifact is the right medium and writes its brief |
| Others in the sync (browser, computer-use, deep-research, google-workspace, morning, mcp-builder, import-memory) | as listed by the harness | Unused by Sŏn work so far; candidates for the monthly `/skill-doctor` prune |

## Vetting gate (every external skill, before it enters the repo)
1. Approved in `memory/skills-plan.md` (Brandon). Unapproved items stop here.
2. License allows a copy. If not, register the account or plugin copy above instead.
3. Read SKILL.md and every reference and script in full.
4. Run `python3 -I .claude/skills/skill-scanner/scripts/scan_skill.py <dir>` and judge each finding (documenting a pattern is not performing it).
5. List hooks, MCP servers, scripts, and network calls. Reject anything that writes outside its own folder or touches `memory/`, any CLAUDE.md, `.claude/settings.json`, or `.claude/hooks/`.
6. No trigger overlap with a row above.
7. Copy to `.claude/skills/<name>/` with `SOURCE.md` (repo, commit, date, license, scanner verdict, local edits). Rare workflows get `disable-model-invocation: true`.
8. Test on a `sandbox/<name>` branch; run `/skill-doctor`; merge only on Brandon's word.

## Hygiene
Run `/skill-doctor` monthly (headless: `claude -p "/skill-doctor"`). Baseline: `memory/audits/2026-10-07-skill-doctor-baseline.md`. Usage counts are per machine, so cloud containers always show "never"; judge pruning on purpose, not on those counts.
