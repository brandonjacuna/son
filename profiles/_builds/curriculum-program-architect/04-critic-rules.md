lens: rules
| row id | severity | flag | evidence (quote the row, 20 words max) | proposed edit |
|---|---|---|---|---|
| front matter | minor | `model: sonnet` for a seat that makes system-shape judgments; CLAUDE.md model policy puts building/drafting on Opus, search/extraction on Sonnet or Haiku. Check against the policy before ship | "model: sonnet" | Confirm intent in the build; set opus if the seat drafts maps |
| C14 | minor | Figure "70-20-10" appears; used only as a rejected ratio, not asserted as fact. Acceptable; keep the "strike the number" framing | "A plan cites 70-20-10 to cut formal learning" | none |
| A7 | minor | Names page 08 and V7; correct as reference/background-only, matches CLAUDE.md. Provenance cites "decision 2026-10-07" which I did not open | "reference and background only" | none |

Checked, clean: no em dashes or en dashes; no "guest"; no "we believe/hope/our goal"; no profanity; no Josephine, Sanctuary, former partners; no Airtable or other retired tool; no financial figures; no lineage practice stated as fact (D1 states the evidence is reasoned, not proven); R11 keeps framework names (HighScope, TBRI) off team-facing output, though the names do appear in this internal agent file, which is permitted. Files checked: agent.md, provenance.md, reference/*.md (dash/guest/retired-name grep).
