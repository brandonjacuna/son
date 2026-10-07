# Sŏn Build: construction-mode workspace

This is the build-out workspace of Brandon John Acuña-Cardona, operator and PM of Sŏn, a fine dining restaurant built around live-fire cooking in Austin, TX. It covers equipment layout and installs, bar and kitchen design, MEP (mechanical, electrical, plumbing) coordination, lighting, audio, networking, storage, water, codes and permitting, and small-batch prototyping.

Brandon is not a licensed design professional. Everything produced here is **design intent**. Stamped permit drawings come from a licensed architect and MEP engineer.

Paths in this file are relative to the build-out root: the repo root in the standalone son-build repo, `company/workstreams/build-out/` in the unified son repo. `.claude/` always sits at the repo root.

## 1. Phase rule (read PHASE.yaml first, every session)
- The current phase lives in `PHASE.yaml`. Hooks enforce it; do not try to work around them.
- **Until `lease_signed: true`, all work is P0 concept work** and is written under `phases/P0-concept/`, `models/`, `equipment/`, `research/`, `kb/`, `decisions/`, `intake/`.
- Later phase folders are locked. Never edit `PHASE.yaml` or run `scripts/advance_phase.py` yourself. Only the `/lease-signed` or `/gate` flow, started by Brandon, can advance a phase.
- Label every concept output "CONCEPT / NOT FOR CONSTRUCTION".

## 2. Where things live
| Thing | Location |
|---|---|
| Design work, research, knowledge | This repo (system of record) |
| Real tasks with an owner and a date, and captured ideas | ClickUp (see §5) |
| Binary evidence: lease, contracts, spec sheet PDFs, manuals, stamped drawings, quotes | Box `Sŏn / 04. Property and Build-Out` (folder 420132927884). Repo stores Box file ID + SHA1 only |
| Equipment facts | `equipment/<slug>.yaml`, validated against `equipment/schema.json` |
| Canonical geometry | `models/src/` (build123d .py, .kcl, .ifc). Exports in `models/exports/` are regenerated, never hand-edited |
| Code facts | `codes/register.yaml`. Every fact is tagged with its code family (UPC/UMC, not IPC/IMC, in Austin) |

## 3. Working rules
- **Intake before design.** Any photo, sketch, markup, or vague idea goes through the `intake` then `interview` skills. Ask one question at a time with AskUserQuestion. Put the key tradeoff in the option label. Never model on an unconfirmed dimension.
- **Dimensions trace to a source.** A dimension is either `verified` (spec sheet on file) or `estimated` (say so on the drawing). Never invent a spec.
- **Sandboxes are branches.** Ideation happens on `sandbox/<topic>-<n>`. `main` holds canonical P0 designs only. Promote with `/promote`.
- **Research is stored.** Raw notes go to `research/raw/YYYY-MM-DD-<topic>.md` with sources. `/consolidate` merges them into `kb/`.
- **Define jargon.** Brandon is not an engineer. The first time a technical term appears in an answer, define it in one short sentence.
- **Decisions are recorded.** Open questions go to `decisions/open.md`. Settled ones become `decisions/NNNN-<slug>.md`.

## 4. Model routing (be strict)
| Work | Model |
|---|---|
| Classifying files, OCR, pulling specs into YAML, diffs, file moves, schema fixes | haiku (subagent) |
| Default: design work, modeling scripts, schedules, research summaries, interviews | sonnet (session default) |
| Code interpretation, live-fire ventilation, cross-trade clash review, routine gate reviews | opus (subagent) |
| Lease-signed gate, first full layout at the real site, safety-critical new profiles, a problem Opus failed twice | Fable, **only** via `/deep`. Never auto-escalate |

Token hygiene: delegate reading-heavy work to subagents and ask them for summaries of 200 words or fewer. Use plan mode before multi-file model changes. Enable CAD MCP servers only for the task that needs them. `/clear` between unrelated tasks.

## 5. ClickUp boundary
- P0: create nothing except (a) ideas filed to a capture list in `clickup/allowlist.yaml`, or (b) a real, committed action Brandon confirms. A hook asks before any other ClickUp write.
- Never delete in ClickUp. Follow `clickup/knowledge-base.md` safety rules. Verify every write by reading it back.
- At P1, `/lease-signed` builds the construction space from `clickup/space-blueprint.md`.

## 6. Writing rules (all output)
- No em dashes. Use commas, colons, or restructure.
- Restaurant patrons are "customers," never "guests."
- Declarative, not aspirational. No "we believe," "we hope," "our goal is."
- Profanity never appears in written output.
- Name: Brandon John Acuña-Cardona in all work. Legal documents such as leases and contracts use Brandon John Acuña. Ask which to use on permit and license applications.
- Sŏn brand canon is under cleanup: do not add cultural tie-ins or experiential brand material to build-out work. Equipment sourcing from any market is fine.

## 7. Environments
- **Cloud (Claude Code on the web, Ubuntu):** research, monitoring, headless geometry (build123d, IfcOpenShell, ezdxf), exports, docs.
- **Local (Claude Desktop Code tab on Brandon's Mac):** anything that drives a GUI app over MCP (Blender + Bonsai, FreeCAD, later SketchUp). Same repo, same branches.
- If a task needs a GUI tool and this is a cloud session, say so and stop; do not fake a render.

## 8. Pointers
Bar work: read `kb/bar/tobin-ellis/` first. Skills: `.claude/skills/`. Agents: `.claude/agents/`. Commands: `/intake /sandbox /promote /capture /consolidate /deep /gate /lease-signed`. Architecture: `decisions/0001-architecture.md`. Research behind it: `research/raw/2026-09-28-construction-mode-blueprint.md`. Migration state: `HANDOFF.md`.
