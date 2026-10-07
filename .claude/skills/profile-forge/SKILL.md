---
name: profile-forge
description: Build a new specialist profile (subagent) when a recurring need has no good owner. Four stages with hard token budgets. Research targets the role's judgment, not a survey of its field.
---
# Profile forge

Use when the same kind of question has come up three or more times, or when a safety-critical area has no owner.

## Stage 1: Frame (delegate to a Haiku subagent, about 2k tokens out)
List the role's 5 to 8 highest-stakes decisions at Sŏn, and the failure modes a senior practitioner would catch that an amateur would miss. No field overview.

## Stage 2: Evidence (Sonnet, at most 8 web searches)
For each decision, find only: the governing rule (code section or manufacturer install requirement) and one practitioner heuristic. Save to `research/raw/YYYY-MM-DD-profile-<role>.md` with sources.

## Stage 3: Distill (Opus; Fable via /deep only for ventilation-fire, codes-permitting, or structural/gas work)
Write `.claude/agents/<role>.md` under 120 lines using `.claude/templates/agent.md`:
decision checklist, red flags, "ask before assuming" list, output format, model line.
Long reference material goes into `kb/<trade>.md`, not the agent file.

## Stage 4: Test (Haiku)
Write 3 scenarios in `tests/profiles/<role>.md` with the catch each should produce. Run the new agent on each. Pass means it catches all three. Fix and rerun once; if it still fails, report to Brandon.

## Model line
Pick the cheapest model that passes the tests. Default haiku for extraction roles, sonnet for design roles, opus only for code or safety interpretation.
