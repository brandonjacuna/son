# 02 old Platform Prompt Specialist
source: profiles/_source/design-translating-team/02_Platform_Prompt_Specialist_Profile.md | read: full text | verified: yes (read at source this build)

## Rows
| id | kind | row | quote | locator |
|---|---|---|---|---|
| 02.1 | model | Each unspecified visual decision is filled from training-data average; the prompt removes decisions, not describes better | "it is the removal of every decision the model would otherwise make on your behalf." | old: sourced |
| 02.2 | cue | "Modern / clean / premium / minimal" -> adjective abdication -> no better adjective -> name hex, radius, spacing step, font, proportion, or a reference | "The root cause of AI slop is the adjective." | old: sourced, cue 3 |
| 02.3 | rule | Rewrite every quality as a constraint the maker can honor or an anchor it can read; interpretation is where defaults enter | "A constraint the model can honor, or an anchor it can read, never a quality it must interpret." | old: sourced, rule 3 |
| 02.4 | anti | Bare negation ("don't use cream"): suppresses one behavior, supplies no replacement, so the model falls to another fixed default | "A negation suppresses a behavior without supplying a replacement, so the model falls back to another strong prior" | old: sourced, rule 4 |
| 02.5 | rule | To override a default, give a concrete alternative spec with exact values, or ask for several distinct directions first and commit to one | "asking the model to propose several distinct directions before building and then committing to one." | old: sourced, date-sensitive |
| 02.6 | cue | Register is cool, dense, or technical -> Claude's house style (warm cream, serif display, italic accents, terracotta) fights it -> override by spec | "reads right for hospitality and editorial and wrong for dense, technical, or cool registers" | old: sourced, date-sensitive |
| 02.7 | rule | If a token system applies, give the maker the actual tokens and constrain output to that dictionary; never describe a palette in words | "Do not describe a color system in words; paste the actual token block" | old: sourced, rule 5 |
| 02.8 | model | For Claude Code, map each visual decision to color, typography, spacing, shape, or structure, each with exact values and a semantic role | "map every visual decision to one of five categories, color, typography, spacing, shape, structure, each with exact values and semantic roles." | old: sourced |
| 02.9 | cue | Maker is Claude Code -> it reads structure, not taste -> Markdown, directory conventions, token-level specs | "Does not speak visual intuition." | old: sourced |
| 02.10 | rule | Name each element that will not translate reliably, with workaround or another maker; where behavior is uncertain, say so | "Name any element that will not render reliably on the target model and give the workaround or an alternative tool." | old: sourced, rule 7 |
| 02.11 | anti | Writer makes the design decision instead of encoding the one already made | "Making the design decision instead of prompting for the one already made." | old: sourced |
| 02.12 | rule | Do not assert brand facts in the prompt; take them from the canonical brand source | "Brand specifics are never yours to assert" | old: sourced, rule 9 |
| 02.13 | example | Dark, quiet cocktail menu screen: instead of "not cream," the prompt gives near-black background, aubergine surface, low-coverage brand accent, brand display face, 2px radius, and opens with a propose-three-then-build-one instruction. | | old: sourced, ex. 3 |

## Tensions
- Old rule 5 says paste the token block; the frame says hand the design system files by path, never a description. Same aim; path wins for Sŏn.
- Sŏn is hospitality, the register house style "reads right" for, so it can pass as on-brand. Source is silent; mark any claim inferred.

## Not usable
- Every per-platform grammar (Claude Design, Midjourney, v0, GPT-4o/DALL-E, Flux/SD): dropped by Brandon 2026-10-10; moves to kb/tools.
- Three-variant rule (frame: bloat); routing across image tools; "internal only" AI imagery (now never).
- v0 "what not to invent" and states list; Claude Design version/feature claims and "stop at roughly 80 percent": not grounded for Claude Code or date-sensitive.
- Role anchor, manifest, interfaces, interaction guide: no decision attached.
