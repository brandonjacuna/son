---
name: <slug>
description: <what this mode does to the main conversation and the exact triggers. One owner per trigger: check .claude/skills/REGISTRY.md first.>
---
<!-- Master: profiles/<cluster>/<slug>/skill/SKILL.md. Generated copy: .claude/skills/<slug>/SKILL.md. -->
# <Mode name>

Use a skill (not an agent) when the seat shapes how the main conversation itself works or writes: a voice, a procedure Brandon steps through, a format. The main conversation keeps its context; this file loads only on trigger.

## Procedure
1. <step>

## Voice or format markers (voice modes only)
| marker | example | never |
|---|---|---|

## Checks before output
- <the 3 to 6 rules from the seat that catch most errors, by id>

## Reference on demand
- `reference/<file>.md`: <when to read it>

## Hand off
- To review: <the reviewing agent slug, if the profile is "both">
