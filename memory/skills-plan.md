# External skills and plugins: plan

Approved by Brandon 2026-10-07 (see `memory/decisions.md`). Approved: all S tier; all A tier; Anthropic Operations, Human Resources, Legal, Design (test ad hoc); ClickUp official MCP; knowledge-ops, education rubrics, model tiering. Everything else below stays unapproved until Brandon says otherwise.

## How approved items get in (cloud sessions cannot run `/plugin`)
- **Skills:** vendor a copy into `.claude/skills/<name>/` after vetting, with `SOURCE.md` (repo URL, commit or version, date, scanner verdict, local edits). Editable, versioned, visible to cloud sessions. Rare workflows set to user-invoked only.
- **MCP servers:** add to the repo's `.mcp.json` (or the workstream's), version pinned, never `@latest`.
- **Mined items:** no install; the idea is written into our own skill, with the source credited in that skill's `SOURCE.md`.
- **Registry:** `.claude/skills/REGISTRY.md` maps trigger phrases to one owning skill. A new skill whose triggers overlap an existing row is merged or rejected.
- **Vetting gate:** read SKILL.md and references in full, run skill-scanner, list hooks, MCP servers, and scripts, reject anything that writes outside its folder or touches `memory/`, CLAUDE.md, or settings, test on a `sandbox/` branch, check `/skill-doctor` before merging.

## Install schedule
| Phase | Approved items |
|---|---|
| 2 Session basics | `/skill-doctor`, skill-scanner, skill-creator, document skills, handoff patterns (into session-close), the registry and vetting gate |
| 3 Profiles | Context Engineering patterns, writing-for-agents, writing-skills test method, model tiering, red-team lenses (into the red-team skill) |
| 5 Workstream builds | build123d-mcp (build-out, after lease work needs it), id-skills-for-claude and education rubrics (learning studio), cowork-sop-writer and knowledge-ops (operations); Anthropic Operations, HR, Legal, Design tested ad hoc as tasks call for them |
| 6 ClickUp layer | ClickUp official MCP (first check whether it is the same server as the existing ClickUp connector; design around daily call limits) |

Sources: Brandon's claude.ai plugin directory and the community research report (2026-10-07). Install = install a pinned, project-scoped copy after vetting. Mine = copy the idea into our own skill; do not install.

Rules for anything adopted: vet first (read SKILL.md and references, run the skill scanner, list hooks/MCP/scripts), project scope by default, pin versions, one owner per trigger verb (`.claude/skills/REGISTRY.md`), never a second memory or state store, rare workflows set to user-invoked only, `/skill-doctor` monthly prune.

## S tier: do first
| Skill | Category | Use | Phase |
|---|---|---|---|
| `/skill-doctor` (built into Claude Code) | Library hygiene | Built in | 2 |
| skill-scanner (Sentry, getsentry/skills) | Library hygiene | Install, user scope | 2 |
| Agent Skills for Context Engineering (muratcankoylan) | Profiles, token use | Mine | 3 |
| skill-creator (Anthropic) | Building our skills | Install | 2 |
| Document skills docx/xlsx/pdf/pptx (Anthropic) | Documents | Install | 2 |

## A tier: strong fit
| Skill | Category | Use | Phase |
|---|---|---|---|
| writing-for-agents (mattpocock/skills) | Profiles | Install editable copy of this one skill | 3 |
| writing-skills testing method (obra/superpowers) | Profiles, behavioral tests | Mine | 3 |
| Red-team lenses: questioning-frameworks (notmanas), stakes calibration (aaddrick/contrarian), three-concerns format (alirezarezvani executive-mentor) | Red team | Mine | 3 |
| Session-close patterns: verify real state, refused rationalizations, anti-shadowing rule (ostikwhy-blip, REMvisual) | Session basics | Mine | 2 |
| build123d-mcp (pzfreo) | CAD, fabrication | Install, pinned, build-out only | 5 |
| id-skills-for-claude (espialuso) | Training design | Install as reference files under kb-refresh | 5 |
| cowork-sop-writer (OneWave-AI) | SOPs | Install | 5 |

## B tier: useful, situational
| Skill | Category | Use | Phase |
|---|---|---|---|
| Operations, Human Resources, Legal, Design plugins (Anthropic) | Ops, people, contracts, design | Test one at a time | 5 |
| Brand Voice (Tribe AI) | Writing | Compare against House voice | 3 |
| humanizer (blader) | Writing | Install after review (has scripts) | 5 |
| the-elements-of-style SKILL.md (obra) | Writing | Copy SKILL.md only | 5 |
| literature-review (lingzhi227/agent-research-skills) | Research, science | Install, Sonnet subagent | 5 |
| knowledge-ops single owner and last-reviewed fields (alirezarezvani) | SOPs | Mine | 5 |
| Backwards design and rubrics (GarethManning/claude-education-skills) | Training design | Mine | 5 |
| Model tiering conventions (wshobson/agents) | Profiles | Mine | 3 |
| ClickUp official MCP | ClickUp | Check against the existing connector; mind daily call limits | 6 |

## C tier: later or only if needed
| Skill | Category | When |
|---|---|---|
| Blender MCP (ahujasid) | CAD | After build123d proves out; desktop only; telemetry off |
| FreeCAD robust MCP (spkane) | CAD | Only if FreeCAD becomes the main tool |
| VoltAgent subagents | Profiles | Format reference only |
| xlsx-toolkit audit checklist (borghei) | Finance | Before the model goes to investors |
| curriculum-designer interview flow (weihaoqu) | Training design | Idea only |
| skills-janitor | Library hygiene | Only if `/skill-doctor` is not enough |
| Marketing, Product Marketing (Anthropic, community) | Promotion | When Robert's promotion work starts |

## D tier: skip
Full superpowers plugin, full mattpocock plugin, c-level-skills plugin, wshobson bulk install, every handoff skill (each creates a second state store), every memory plugin, abogado-del-diablo, claude-office-skills, taazkareem ClickUp MCP, 3dp-mcp-server, build123d-claude-plugin, ai-restaurant-claude, claude-code-templates installer, Productivity plugin.

## Gaps to build ourselves
SCORM and Trainual export, Box workflows, the DuckDB market digest, restaurant back-of-house operations.
