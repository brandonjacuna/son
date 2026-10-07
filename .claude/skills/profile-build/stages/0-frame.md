# Stage 0: Frame (Fable subagent, then Brandon)

1. Create `profiles/_builds/<slug>/` with an empty `BUILD.md` (header: slug, mode, date, orchestrator model) and `extract/`.
2. Spawn one Fable subagent (`model: fable`) with this brief, filled in:
   - "Read `.claude/skills/profile-build/templates/frame.md` and `.claude/skills/profile-build/stages/0-frame.md` (the container rubric below). Read `.claude/skills/profile-build/templates/tests.md` too. Write `profiles/_builds/<slug>/00-frame.md` and `00-tests.md` (3 to 5 tests) for <seat>, mode <mode>. Inputs: <the brief or Brandon's words>; old material: <paths> (read only headings, the scope, decision_rules, and interfaces sections, and up to 10 KB of worked examples for test candidates; never whole files); neighbors: the `description:` lines of `.claude/agents/*.md` and <named old profiles' scope sections>. 6 KB maximum (8 KB in rebuild or merge mode). Return the path and the open questions only."
3. Ask Brandon each open question as a pop-up, plus one fixed question: "What do you NOT want this seat to do?" Record answers under "Brandon's answers" with the date.
4. Stop if an open question that changes scope is unanswered. After the last edit to the frame (answers, added rules), re-read `00-tests.md` and align any expected catch that the frame now contradicts. Tests never change after stage 3 starts.
5. First build of a cluster only: spawn one Sonnet worker to compare the old profiles' project_block and interaction_guide against root CLAUDE.md and return any rule CLAUDE.md does not carry (1 KB). Log each gap with the `thread` skill for Brandon; never add it to CLAUDE.md yourself.

## Container rubric (the core design call)
| The seat... | Container |
|---|---|
| judges, reviews, diagnoses, or decides, and its value is an independent conclusion (can run blind, in parallel, on its own model) | **agent** in `.claude/agents/` |
| shapes how the main conversation writes or works: a voice, a format, a step-by-step procedure Brandon walks through | **skill** (a mode); no separate context |
| does a procedure in the main conversation AND its output needs an independent check | **both**: a skill for the procedure, an agent for the review (for example a translation skill plus a reviewing agent) |
| is only reference knowledge (a platform grammar, a code table, a glossary) | not a seat: a `reference/` file or a `kb/` page owned by an existing seat |

## Red-team intensity
- light: concept and ideation seats, low-stakes creative modes.
- standard: default.
- harsh: legal, compliance, finance, and anything touching employees (hiring, pay, discipline, training that becomes a gate).

## Tests are written here, not later
Each test names the catch the seat must produce and the failure a generalist shows. A test with no expected catch is not a test. Rebuilds: take candidates from the old profile's worked examples and the workstream's real requests.
