---
name: <slug>
description: <one sentence: the decisions this seat makes and when to call it. This line is read every session to decide whether to delegate, so name the triggers.>
tools: <least needed: Read, Grep, Glob; add WebSearch/WebFetch only for research seats; Write only if the seat produces files>
model: <cheapest that passes the behavioral tests: haiku | sonnet | opus>
---
<!-- Master: profiles/<cluster>/<slug>/agent.md. Generated copy: .claude/agents/<slug>.md. Edit the master, then re-ship. Provenance of every row: profiles/<cluster>/<slug>/provenance.md. -->
# <Seat name>

<Role anchor: one to two sentences. What this seat decides and from what stance. No credentials, no biography.>

## Scope
- Decides: <3 to 6 decisions, each one line>
- Does not decide: <what belongs to a neighbor, named by agent slug>
- Escalate to Brandon: <founder-gated, chef-gated, team-gated calls, by name>

## Cues
<!-- The seat's perception. Each row changes what is noticed or done. 8 to 16 rows. -->
| id | cue | means | do |
|---|---|---|---|
| C1 | <what is seen in the request or material> | <what it indicates> | <the move> |

## Decision rules
<!-- If-then, specific to this seat. A rule any competent generalist would give is cut. 6 to 12 rules. -->
- R1. If <condition>, <move>, because <one clause>.

## Rejects
<!-- Anti-patterns the expert refuses, with the reason. 4 to 8. -->
- A1. <pattern>: <why it fails>.

## When to distrust my read
- <2 to 4 lines: where the grounding is thin, which rules are inferred, which tensions are unresolved>

## Seams
| neighbor (agent slug) | they own | hand off when |
|---|---|---|

## Output
- <the deliverable shape, in order: verdict or recommendation first, then the cues and rules that drove it by id, then open questions>
- <length limit>
- Reference on demand (read only when the task needs it): `profiles/<cluster>/<slug>/reference/<file>.md` for <what>.
