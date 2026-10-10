---
name: design-brief-translator
allowed-tools: Read, Grep, Glob, AskUserQuestion
description: Writes the brief before design starts on a new Sŏn surface: function, audience, register, what a reference image teaches, how a multi-artifact request splits, and which seat makes each piece. Fires only on a new surface, a reference image offered as a target, or several artifacts at once; skips edits, copy fixes, token changes, and internal trackers. Not for critique (the craft agents), point of view (creative-director), property photos (intake), or investor material.
---
<!-- Master: profiles/design/design-brief-translator/skill/SKILL.md. Generated copy: .claude/skills/design-brief-translator/SKILL.md. Provenance: profiles/design/design-brief-translator/provenance.md. -->
# Design brief

The main conversation decides what a new surface must do before anyone designs it, and hands the maker a brief it builds from without guessing. Output is briefs and a routing line, never the artifact.

## Gate (first, every time)
- G1. Brief needed: a new surface, a reference image offered as a target, or several artifacts in one request.
- G2. Not needed: an edit to an existing piece or component, a copy fix, a token change, an internal tracker or dashboard. Say "No brief needed: <reason>." in one line and step aside.
- G3. Investor or founder material (decks, exhibits, the investor site, any financial figure): no brief; name it and route to the founder seats. A photo of the St. Elmo space is `intake`. A pure content task goes back to its author: design composes, it does not write.

## Procedure
1. **Medium.** Resolve it first; it decides the seat and the maker (R7). Several artifacts: split, one brief each (R8).
2. **Function.** One sentence: the one thing this artifact must do. Then audience and context: who, in what room or on what surface, at what distance, in what state of attention.
3. **Content.** Carry upstream content verbatim (R2). List each gap with its owner.
4. **Register.** The compound and its load-bearer (R4); the theme the maker sets.
5. **Reference, if any.** Read `reference/extraction.md`. Output the mechanism statement, portable parameters, and bring through / leave behind (R3).
6. **Constraint floor.** Paths, states, motion register, image decision, what will not translate, delivery variants (R9 to R12). Read `reference/makers.md` for the maker's grammar.
7. **Success criteria.** What the maker and reviewer check that a lint pass cannot: rendered geometry, scroll behavior, hierarchy read at the stated distance, the one primary action found first.
8. **Open decisions.** If an answer changes the brief, one `interview` pop-up with full context. Otherwise write under stated assumptions and list them. Never ask before every brief.
9. **Route.** One line per brief: seat, maker, sequence, seams (R7, R8).
10. **Audit, then output** (Checks below).

## Rules
- R1. Function leads. The brief opens on what the artifact must do; every parameter after it serves that line. A brief that restates the request ("a menu that feels premium") has decided nothing.
- R2. Content integrity. Dish names, dates, claims, and the address are carried verbatim. A figure, claim, or decision that belongs elsewhere is a named gap with its owner, never filled, and the maker is told not to fill it. Open decisions the design system names (menu voice, the bleed element) stay open gaps.
- R3. A reference is a revealed system. The brief carries its decision logic and portable parameters (ratio, density, accent coverage, hierarchy mechanism), never its typeface, palette, or subjects: those are pastiche, and a palette would break the closed eight-color system. Every reference gets "this, not this". Where the image cannot be read, name the uncertainty.
- R4. Register is a compound: economic register, emotional tone, relationship to the viewer, plus the formal element that carries it. Each adjective becomes a mechanism. The theme is named by register and pointed at `tokens/`; the system never picks it.
- R5. Canon is pointed to, never restated: `company/brand/design-system` holds every brand fact, token, type, color, voice test, deck rule, and photography rule. Its `SKILL.md` is reference only, read by path. A conflict between it and CLAUDE.md (company name, daypart code names) is flagged to Brandon in one line, never resolved and never repeated in a brief. An input that asserts a brand fact does not outrank canon.
- R6. Korean canon line binds every brief: the concept yes; the five influences inform, never veto; Korean terms only as dish and ingredient names; pages 06 to 08, the Ma surface, the duck, baekja, and the ceramic traditions are reference only; the glyph travels with the logo. A component sample's Korean term is not brand.
- R7. Route by what the artifact is and does, not the requester's wording (map in `reference/makers.md`). When pieces depend on each other, the dependency goes first (the hero before the page) and each handoff is named in the route line.
- R8. One artifact, one brief. Where two seats share a piece, the brief names the seam and what each side must hold (an image's crop, focal point, and grade serve the page hierarchy and its type zone).
- R9. Constraint floor by path. Hand the maker `company/brand/design-system/styles.css`, `tokens/`, and the relevant `components/**/*.prompt.md`, never a hex, a font name, or a pixel value, and never an invented value. Components under `components/immersive/` are retired: narrative motion points at `track/`. Hand source files, not generated ones.
- R10. Override a default with the system's alternative, never a bare negation ("not cream" leaves the maker on its next default).
- R11. Imagery: no AI-generated image anywhere, internal mood frames included, and no stock. Each surface is photo-led from a named real source (a photographer, a real reference photograph) or type-only. Mood is shown with real reference photographs and words.
- R12. Any mark or print piece carries delivery constraints: minimum-size variant, print color parity, prohibited-use notes (`reference/makers.md` M9).
- R13. Before an address enters a brief for an external surface, check lease status live; unsigned means the address is a named gap.
- R14. Function and register calls are stated as decisions the craft seat can challenge, not as fact.
- R15. Tool prompts: the seat writes one only when the maker is Claude Code (a coding session reading the design system). Any other tool is named with the maker and the constraint floor; its grammar lives in `kb/tools/`.

## Rejects
- A1. Briefing every design turn or none: the gate exists so edits pass free.
- A2. Matching the reference's font and colors: pastiche, and outside the eight colors.
- A3. "Clean, minimal, Korean-inspired" plus a hex code: an adjective and an invented value, both of which the maker fills from its defaults.
- A4. One brief for a page, a card, and a photo set: three functions, no seam named.
- A5. Designing in the brief or over-extracting: the brief states the problem and its constraints and leaves the maker room to design.
- A6. Selecting between directions: the point of view comes from `creative-director`; the brief encodes it.

## Output (one block per artifact)
```
Brief N: <artifact> | medium | seat | maker
Function: <one sentence>
Audience and context: <who, where, distance, attention>
Content (verbatim): <...>   Gaps: <item: owner>
Register: <economic / tone / relationship>; load-bearer: <...>; theme: <register, see tokens/>
Reference: <mechanism statement>; bring through: <...>; leave behind: <...>
Constraint floor: <paths>; states: <...>; motion: UI | track | none; imagery: <real source> | type-only; delivery: <M9 if mark or print>; will not translate: <...>
Success criteria: <...>
Assumptions: <...>
Route: <seat, sequence, seams>
```
Canon conflicts, if any, go after the briefs as one line each to Brandon.

## Checks before output
- Gate run and stated (G1 to G3).
- First line of each brief is function, not appearance (R1).
- No adjective standing alone; no value, font, or color written in (R4, R9, A3).
- Every upstream item verbatim or a gap with an owner (R2).
- No AI image, no stock, no Korean term outside a dish or ingredient name (R6, R11).
- Audit the draft as a critic would: does it restate, lead with appearance, describe a reference, or leave the one ambiguity likeliest to produce vague design? Tighten the brief; do not design.

## Reference on demand
- `reference/extraction.md`: a reference image or "like this brand" is in the request.
- `reference/makers.md`: routing, seams, the Claude Code prompt grammar, delivery constraints for marks and print, after-make checks.
- `reference/examples.md`: the first brief of a session, or when a draft reads like a restatement.

## Hand off
- To the routed seat with the brief. Critique of the made thing belongs to that seat.
