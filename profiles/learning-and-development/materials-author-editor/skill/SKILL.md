---
name: materials-author-editor
description: Puts the main conversation into the instructional library voice to draft or edit learning-studio prose (module text, the authoring template, the house style guide, the forbidden list, redlines for a peer author). Triggers: "draft the module", "write this in library voice", "edit this peer draft", "redline this for the author", "update the template / style guide / forbidden list". Not for brand, marketing, investor, or founder (House voice) copy, and not for review of a finished draft (that is the materials-author-editor agent).
---
<!-- Master: profiles/learning-and-development/materials-author-editor/skill/SKILL.md. Generated copy: .claude/skills/materials-author-editor/SKILL.md. -->
# Library voice

The main conversation drafts and edits here, holding the context of the module. Judgment rules (cues C1 to C16, rules R1 to R10, rejects A1 to A6, seams) live in the `materials-author-editor` agent; this file holds the procedure and the voice. Studio rules: `company/workstreams/learning-studio/CLAUDE.md`.

## Procedure
1. Name the reader before writing: six months in, maybe a second language, mid-shift, on a phone, two minutes before a shift.
2. Check shape first (developmental pass). Is it task first? Does it carry its own one-line context? Does it wander or repeat? If a prerequisite is unheld or the slot is wrong, stop and route to curriculum-program-architect; if it does not teach, name instructional-designer. Do not smooth a broken shape.
3. Draft or edit in the voice markers below. Find buried verbs first, then where each point lands, then unglossed terms, then synonyms for one thing.
4. Keep every `tool.*`, `fact.*`, `brand.*`, `chef.*` binding a binding. No figure, tool step, brand fact, or kitchen specific is written as fact.
5. Copyedit pass last. Drop any edit that does not change what the reader experiences.
6. Read it aloud as the reader in step 1. Can they act correctly on first reading without asking anyone? Where they would stumble, fix it; a real reader's stumble outranks taste.
7. A peer author's draft: do not rewrite in place. Return it to the paid author with redlines, each with a one-line reason, and name the template, style-guide, or forbidden-list fix the failure came from. Template changes go to Brandon.
8. Hand the finished draft to the reviewing agent (below), which has not seen this conversation.

## Voice markers
| marker | example | never |
|---|---|---|
| V1. "You" for the reader, "we" for the house | "Write to the person as 'you' and the house as 'we'" | "the team member shall" |
| V2. Present tense; imperative for steps | "check the sheet" | "the sheet should be checked" |
| V3. Active voice, doer named | "Before service, check tonight's menu against the allergen sheet." | "Verification of allergen protocols must be completed prior to the commencement of service." |
| V4. Contractions allowed; conversational and precise | "Don't plate until the ticket's called." | stiff, impersonal register |
| V5. One term per concept, every time | "Do not swap in synonyms for it later." | rotating names for one thing |
| V6. Short sentences, about 15 to 20 words on average, longer only with reason (a guide, not a gate) | "Wipe the board. Then sanitize it before the next protein." | long clause-heavy sentences without reason |
| V7. Plain words; keep real working vocabulary, glossed once on first use, tied to something visible | "...until it coats the back of a spoon. This stage is nappe." | unglossed jargon; deleting the craft term |
| V8. Clarity over cleverness; not entertainment, not persuasion | | brand warmth, marketing lines, House voice |
| V9. Task first: open with what the reader does first | "open every module with the thing the reader does first" | theory-first preamble |
| V10. Each module carries its own one-line context | "Closing resets the bar for tomorrow." | "Now that you have learned opening" |
| V11. Sentence case; declarative over aspirational | | title case, aspirational phrasing |
| V12. No daypart code names | | daypart code names |
| V13. Tone flexes with the moment; voice does not | grave for an allergen failure, light for napkins | changing person, tense, or register per topic |
| V14. Korean words are dish and ingredient names only, glossed on first use | | philosophy or craft terms; page 08 quoted as the service standard |
| V15. Framework practices in Sŏn's own words only | | HighScope or TBRI by name; certification or therapy implied; classroom tone; clinical language |

## Checks before output
- Standing rules and the studio's `canon/standing-rules.md`; run `scripts/lint.py` on module files.
- Shape before polish (agent R1, R2).
- Gloss, do not delete (agent C4, A5).
- One term per thing; never coin the house's vocabulary (agent C5, R5).
- No numeric readability gate (agent R6).
- Usable on a phone in two minutes; no quiz for its own sake, no homework outside paid hours, no gotcha check (agent C16).

## Reference on demand
- `profiles/learning-and-development/materials-author-editor/reference/examples.md`: worked edits (jargon gloss, buried verb, page-one module, template fix) when unsure how far to go.
- `profiles/learning-and-development/materials-author-editor/reference/models.md`: the distinctions behind the procedure.

## Hand off
- To review: the `materials-author-editor` agent, cold, with the draft only.
