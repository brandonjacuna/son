# Standing rules

These apply to every employee-facing surface this studio produces. They mirror the rules baked into the Learning & Development, People & Culture, and Scaling People profiles. `scripts/lint.py` enforces the ones a machine can check. The rest are on the reviewer.

## Language

| Rule | Checked by lint |
|---|---|
| The person we serve is the **customer**, never "guest." | Error |
| No em dashes. Use a comma, a colon, or restructure the sentence. | Error |
| No daypart code names (Good Energy, Dosi, Luxx, or Sŏn used as a daypart name). They are internal and never appear on any surface, including training. | Error for Good Energy, Dosi, Luxx. Reviewer checks Sŏn-as-daypart. |
| No performed conviction: "we believe," "we hope," "our goal is." Declarative over aspirational. | Error |
| "Stage" in the unpaid-kitchen-trial sense is written as "paid practical." | Warning (rule carried from the Hospitality Operations Realist profile; confirm with Brandon) |
| Sentence case for headings and titles. | Reviewer |
| Profanity is spoken only. It never appears in writing without Brandon's explicit per-piece override. | Error on a short list; reviewer for the rest |

## Facts

| Rule | Checked by lint |
|---|---|
| Figures (prices, wages, costs, covers, percentages) come from Airtable only. Write a `fact.*` binding instead of a number. | Warning on any currency amount or percentage outside a binding |
| Brand facts (positioning, naming, service philosophy, lexicon) defer to the Brand and Experiential Guidelines in Box, file `2281626080747`. Cite the section or bind with `brand.*`. | Reviewer |
| Tool and workflow specifics are bindings until the tool or workflow is set. | Reviewer, plus `/park-module` check |
| Back-of-house station specifics, recipes, and menu execution are chef-gated. Bind with `chef.*`. | Reviewer |
| Practices from Brandon's lineage (Coqodaq, Alinea, Gracious) are never reconstructed. Flag for Brandon. | Warning when those names appear in `modules/` |

## Scope

- Sŏn only. No other portfolio concepts are named or planned for.
- Externally certified content (for example food handler or alcohol seller-server certification) is referenced, not re-taught as a substitute for the certification.

## Design prompts

Any prompt written for an AI design or video tool (Claude Design, Canva, Firefly, Adobe Express, Midjourney, Synthesia scene direction, or similar) runs through the Design Translating Team before it is used. See `adapters/synthesia.md`.
