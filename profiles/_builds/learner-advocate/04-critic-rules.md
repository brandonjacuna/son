lens: rules
| row id | severity | flag | evidence (quote the row, 20 words max) | proposed edit |
|---|---|---|---|---|
| front matter | major | `model: haiku` against CLAUDE.md model policy: Haiku is for searching, inventorying, extraction, mechanical edits. This seat judges harm and escalates on employee-adjacent matters. Failure path: weak read misses C15 (file on a person), which touches employees | "model: haiku" | Set sonnet |
| R11 | minor | Escalation rule is explicitly inferred with no source (the agent file says so). Not a rule violation; but "open at ship" for Brandon must be a recorded decision path, not a decision made by the seat | "list it once under 'open at ship' for Brandon to decide" | Keep; confirm Brandon agrees at readback |
| R9 / C-rows | minor | R9 bars framework names to the team, yet agent.md names tbri and "stereotype-threat" internally. Internal use only, so allowed | "no framework names" | none; ensure generated lean copy never emits them in output text |

Checked, clean: no em dashes or en dashes; no "guest"; no "we believe/hope/our goal"; no profanity; no Josephine, Sanctuary, former partners; no Airtable; no figures; Korean terms limited to dish and ingredient names (matches brand decision 2026-10-07 as cited, not opened by me); C15 and R7 keep training signals developmental. A6 treats contested research as non-fact, so no lineage practice asserted. Files checked: agent.md, provenance.md, reference/*.md (dash/guest/retired-name grep).
