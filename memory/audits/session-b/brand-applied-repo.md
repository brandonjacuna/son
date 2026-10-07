# Brand canon line applied to the repo design system

2026-10-07. Applies Brandon's approved brand canon line to `company/brand/design-system/`. Source map: `brand-canon-extraction.md` (this folder). Not committed. refs/, node_modules, uploads/ untouched.

## Changes by file

All paths relative to `company/brand/design-system/`.

| File | What changed | Decision |
|---|---|---|
| `readme.md` | Preface (59-60): 선 is part of the logo, appears where the logo appears, not required on every surface. Blockquote (68-69): "governed top-down by three Tier-1 frameworks with veto power" replaced by "informed by guiding cultural influences; no veto." Section "The three Tier-1 frameworks (always govern)" retitled "Guiding influences (inform, do not govern)" with an intro paragraph; Jaeyeonmi, Ma, Mahk descriptions kept; Jeong and Nunchi added as item 4. Preferred terms (144-146) replaced: Korean terms limited to Galbi, Dosirak, Banchan, Ganjang, Doenjang, Gochujang, 선; philosophy and craft terms marked internal; no-gloss rule removed. Type section: Sandoll Myeongjo limited to the 선 glyph and Hangul dish names. Backgrounds: pattern system marked reference only. Iconography: "primary mark" became "part of the logo, not mandated on every surface"; future marks and pattern system labeled "reference only, not canon (2026-10-07)". Font substitutions: "all Hangul" became "Hangul dish names." | 2, 3, 4, 5 |
| `SKILL.md` | Orientation line: Tier-1 frameworks became guiding influences (inform, do not veto). Non-negotiables: Korean face limited to glyph and dish names; "선 glyph is on every surface" replaced by "part of the logo, travels with it, not required on every surface; never in Jade." | 2, 3 |
| `guidelines-deck/Son Guidelines Deck.html` | Section 02 divider and authority slide rewritten: guiding influences that inform decisions, no veto, not Tier 1 (framework description slides kept). Section 07: headline, hierarchy row 1 (now "Guiding influences", unnumbered, no veto; tiers 2-6 kept so "Tier 6" and ClickUp numbering still match), row 4 ("선 mandate" became "wordmark and 선 glyph"). "The 선 mandate" slide became "The 선 glyph in the logo." Visual principle 03 "The mark is constant" became "The mark is consistent." Ecosystem sub line reworded. Typography: Korean face limited to glyph and dish names (three faces slide, Hangul deployment Rule 1); Hangul deployment headline, sub, and Rule 2 replaced (no-gloss rule dropped; dish and ingredient names only). Preferred terms slide: Korean column now Galbi, Banchan, Dosirak, Ganjang, Doenjang, Gochujang, 선; headline no longer "stand without translation." Deferred items row for Korean terminology rules updated. Downstream citations softened: "Ma governs" to "Ma informs it" (digital empty state), olfactory "governed by" to "informed by", 1B "frameworks cannot change" to "guiding influences inform it." Reference-only labels (21 total, existing `corner status s-held` / `status lg s-held` markup, text "Reference only, not canon (2026-10-07)"): section 13, 14, 15 dividers plus every content slide in those sections (14 slides); Pattern and texture; Iconography; Bird mark (label merged with Deferred); 7C tableware row (ceramic traditions). Nothing deleted. | 2, 3, 4, 5 |
| `guidelines-deck/Son Guidelines Deck-print.html` | Rebuilt as the edited deck plus its existing print script block, so it stays identical to the main deck (verified the twin matched before the edit). | same |
| `guidelines/type-korean.html` | Specimen meta "All Hangul, all contexts, one face" became "The 선 glyph and Hangul dish names only, one face." Tokens untouched. | 2 |
| `components/brand/Wordmark.d.ts` | Header comment: "선 is mandatory on every surface" became "선 is part of the logo." | 2 |
| `components/immersive/AmbientField.prompt.md`, `.jsx`, `.d.ts` | Removed "deliberate canon override (the readme fixes the glyph at constant scale)" wording; the large-glyph module is now described as an optional module behind `--son-glyph-motion`. Behavior unchanged. | 2 |
| `tokens/base.css` | Comment only on `.son-glyph`: "sole mandatory structural constant" became "part of the logo, not mandated on every surface." No token values changed. | 2 |

## Unchanged by decision
- "Korean fine dining restaurant", "Korean restraint", site hero and type-fit (decision 1).
- Onggi name and color (decision 6).
- All components still render 선 (Wordmark, AmbientField, Marquee, DaypartTakeover, Divider, Badge). Korean font tokens kept.

## Lint
- No lint rule enforced the glyph mandate, the no-gloss rule, or the preferred-terms list. `adherence/check-copy.mjs`, `eslint.config.mjs`, and `_adherence.oxlintrc.json` only reference the glyph as a declared component prop / token; nothing to remove.
- `node adherence/check-copy.mjs`: clean (50 files checked).
- `npx eslint`: not run; node_modules is absent (no npm install, per instruction).

## Left as is (flag)
- `_ds_bundle.js:749` still carries the old AmbientField "deliberate canon override" comment. Compiler-generated snapshot; updates at the next external regeneration.
- `AUDIT.md:87` repeats "deliberate canon override." Historical audit record, not canon.
- `docs/design-language.md:44-45` ("A Korean room that does not show its Korean mark in the opening...") is the hero crop rationale, tied to the hero (decision 1), not an every-surface mandate.
- Deck section 02 framework slides and Jeong/Nunchi slides keep their descriptions and Hangul labels, per decision 3. Sections 13-15 still cite Jaeyeonmi/Ma "governs" inside reference-only slides; left verbatim because those sections are now reference.
- Pre-existing em dashes in edited lines (deck ecosystem sub line, section number labels) left as they were.
