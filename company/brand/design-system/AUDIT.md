# Sŏn correction + immersive extension pass · 2026-07-17

Prompt 1 of 2, items 1–13. Everything below is auditable against git-style before/after.

## Files changed

**Tokens:** `tokens/colors.css`, `tokens/base.css`, `tokens/typography.css`, `tokens/fonts.css`, `tokens/components.css`, `tokens/spacing.css`, `styles.css` · **new** `tokens/motion-immersive.css`
**Components (forms):** `Input.jsx/.d.ts`, `Select.jsx/.d.ts`, `Checkbox.jsx/.d.ts`, `Switch.jsx/.d.ts`, `forms.card.html`
**Specimens:** `guidelines/colors-special.html`, `colors-accents.html`, `colors-dark.html`, `colors-daypart.html`, `colors-surfaces.html`, `type-body.html`, `type-display.html`, `type-wordmark.html`, `type-korean.html`, `components/core/core.card.html`, `components/navigation/tabs.card.html`
**Slides:** `slides/02-section.html`, `04-content.html`, `05-callout.html`, `06-photo.html`, `07-menu.html` (01, 03 untouched)
**Template:** `templates/deck/index.html`
**UI kits:** `ui_kits/good-energy/index.html`, `ui_kits/son-website/index.html`
**Guidelines deck:** `Son Guidelines Deck.html` + `-print.html` (three stale strings only)
**Docs / enforcement:** `readme.md` · **new** `.stylelintrc.json`, `adherence/check-copy.mjs`, `thumbnail.html`
**New components:** `components/immersive/` — 9 × (`.jsx` + `.d.ts` + `.prompt.md` + `.card.html`)

## 1 · Token values, before → after

| Token | Before | After |
|---|---|---|
| `--son-color-white` | `#FFFFFF` | **deleted** (grep found no consumers; nothing resolves to #FFFFFF) |
| `--son-color-gold-foil` | `#BC9A5C` | **deleted** — physical spec (Pantone 871C / Kurz Luxor 220) lives only in the colors-special card as a labeled stripe: "Physical only, no digital fill" |
| `--son-border-default` (base/editorial) | plum-ink 16% | plum-ink **22%** |
| `--son-border-default` (dinner) | bone 18% | bone **28%** |
| `--son-border-default` (luxe) | bone 18% | bone **28%** |
| `--son-border-default` (morning / dosi) | 38% / 34% | unchanged |
| `--son-text-display` | `clamp(3.5rem, 6vw, 6rem)` | `clamp(2.5rem, 2.5rem + 2.875vw, 6rem)` → 76.8px @1280 |
| `--son-text-headline` | `4.5rem` | `clamp(2rem, 2rem + 3.125vw, 4.5rem)` → 72px @1280 |
| `--son-text-section` | `2.5rem` | `clamp(1.5rem, 1.5rem + 1.25vw, 2.5rem)` → 40px @1280 |
| `--son-text-subhead` | `1.625rem` | `clamp(1.1875rem, 1.1875rem + 0.547vw, 1.625rem)` → 26px @1280 |
| `--son-font-korean` | `"Nanum Myeongjo", "GT Sectra Book", "Apple SD Gothic Neo", serif` | `"Sandoll Myeongjo", "Nanum Myeongjo", "Apple Myungjo", "Batang", serif` (Korean serif or generic serif only) |
| `--son-font-wordmark` | `"GT Sectra Book", "Cormorant Garamond", Georgia, serif` | `"GT Sectra Book", "GT Sectra Book Fallback", Georgia, serif` |
| `.son-eyebrow` color | `var(--son-text-secondary)` | `var(--son-text-primary)` (dosi eyebrow now Plum Ink on Parchment) |
| `--son-text-secondary` (all 5 scopes) | — | comment added: "large text only (>= 24px, or >= 18.66px bold) and non-text roles (border, icon, accent); never small or body text" |
| Focus (all controls) | mixed: 1px outlines, field box-shadow underline + `outline: none` | one spec: `outline: 2px solid var(--son-focus-ring); outline-offset: 2px` — the single 2px exception |
| GT Sectra Book `@font-face` | `font-display: swap` | `font-display: block` + new `GT Sectra Book Fallback` on Georgia: `size-adjust 100.44%, ascent-override 97.57%, descent-override 25.89%, line-gap-override 0%` (measured from GT-Sectra-Book.ttf: upm 1000, hhea 980/−260, avg lowercase advance 0.5041em vs Georgia 0.5019em) |
| Reduced motion (UI) | re-declared `--son-motion-* : 0ms` (manifest wrongly reported 0ms) | usage-level kill rule; manifest now reports **100/200/400ms** |
| **New immersive register** (`[data-surface="immersive"]` only) | — | `--son-imm-quick 450ms · settle 850ms · takeover 1400ms · stagger 80ms · ease cubic-bezier(0.22,1,0.36,1) · lerp 0.08 · --son-glyph-motion on`; collapses to nothing under reduced motion |

## 2 · Copy strings, before → after

Slides (and the same strings in `templates/deck/index.html`):
- 02: "02 — The Space" → "02 · The space"
- 02: "The room recedes so the experience comes forward." → "The room recedes. The table comes forward."
- 04: "Jeong — bond built through shared time" → "Jeong, the bond built through shared time"
- 04: "Nunchi — reading need before it is asked" → "Nunchi, reading need before it is asked"
- 04: "The step-back model holds a coverage position that permits observation without proximity. / The trigger for the next approach is attunement, not a timer." → "The server works from a step back, near enough to read the table, far enough to leave it alone. / The next approach comes from attention, not a timer."
- 04 kept: "Attention is the warmth, not the adjective.", "The server owns the table", "The floor manager owns the room"
- 05: figure "2,310 SF" → callout "One room, first light to last call." (132px → 104px to hold the sentence); kept "A converted residential bungalow. The facade does not announce itself as a restaurant."
- 06: "The fireplace, the room's gravitational center." → "The fireplace, the center of the room."
- 06: placeholder "Drop a photograph — Context A…" → "Drop a photograph. Context A…"
- 07: descriptors "Aged thirty days. Scored before the fire." and "Set in onggi clay. Three winters." → **removed**; names carry the slide
- 01, 03: untouched

Specimen labels (em dashes gone, exact renames as specified): Core / Forms / Navigation / Body / Display / Wordmark card names; the four color-card subtitles; plus `type-korean.html` flag line, `@startingPoint` subtitles and page `<title>`s in both ui kits, `Good Energy — morning order` → `Good Energy: morning order`, `Sŏn — reservation site` → `Sŏn: reservation site`.

readme.md, Content fundamentals:
- Removed examples: "Galbi / Aged thirty days. Scored before the fire." and "Scored before the fire. Table available tonight."
- Kept: plate/relationship line, confirmation example, in-space line.
- Added anchors: "What looks like a people business is a memory business." / "Only two things in a restaurant compound. The organization, and the customer. Everything else a good competitor copies in a season." / "One footprint. Coffee, lunch, dinner, late night, against one set of fixed costs."
- **OPEN DECISION flagged, not rewritten:** the "Preparation is stated as decision" guidance generates the removed clipped register — needs your call on menu voice.

Guidelines deck (both copies, stale strings only): the two menu-poetry examples removed from the voice table ("Galbi" stands alone; short-form → "Table available tonight."); "The room recedes so the experience comes forward." → new line; Interior/Patio SF rows → "Footprint: Figures live in the briefing."

## 3 · Forms state completion (item 7)

All four controls now express default / hover / focus / disabled / error. Disabled = opacity 0.45 + not-allowed (Input's treatment, now shared). Error = `--son-border-strong` border + message in `--son-text-fine` / `--son-text-primary` — border weight plus text, never color alone (Input previously mis-signaled error with Onggi color; removed). `Select` gained `error`/`hint` props (contract updated); `Checkbox`/`Switch` gained `error` (their boxes already ride `--son-border-strong`, so the message line carries the state). All error fields set `aria-invalid`.

## 4 · Manifest (item 8)

Root cause fixed at source: the reduced-motion blocks no longer re-declare tokens, so the regenerated manifest reports motion at 100/200/400ms (and the immersive register at 450/850/1400ms). `--son-font-korean` now leads with "Sandoll Myeongjo" — the compiler flags it as awaiting upload (correct: substitute pending; Nanum Myeongjo renders meanwhile).

## 5 · Enforcement (item 9)

- `.stylelintrc.json` (error severity): no raw hex / named colors / raw color functions; font-family allow-list; covers `.css` and `.html` (postcss-html); exemptions: `tokens/colors.css` primitives, gold-foil stripe.
- `adherence/check-copy.mjs` (`node adherence/check-copy.mjs`, exits 1 on violation): em dashes in specimen/slide copy **and** in printed `@dsCard`/`@template`/`@startingPoint` labels; forbidden lexicon (incl. "experience", "guest"); raw hex in CSS contexts; removed-token references; non-system font-families. Verified clean against the current tree.
- Scope notes: comments are stripped (not copy); `guidelines-deck/` is exempt as rendered documentation that quotes both sides of the voice rules; infra js and `uploads/` exempt.
- `_adherence.oxlintrc.json` is compiler-owned and regenerates from sources each turn: the removed tokens drop out automatically. Its JSX rule severity is set by the compiler (oxlint shares one severity per rule), so the **blocking** pass for canon-critical violations is the stylelint + checker pair above.

## 6 · New components (items 11–13) — `components/immersive/`, namespace `window.SNDesignSystem_4d795d`

All on corrected tokens, all with `.d.ts` contract + `.prompt.md` + `@dsCard` showcase, all with reduced-motion fallbacks; immersive register is scoped to `[data-surface="immersive"]` roots and never touches UI.

- **FullBleedSection** — `theme, ground (primary|secondary|inverse), as, minHeight, children`
- **Chapter** — `theme, timeLabel, scrub, length, children` (+ `data-imm-rate` on children); GSAP ScrollTrigger pin/scrub; static stack fallback
- **DaypartTakeover** (signature; item 13) — `from, to, fromTime, toTime, auto, progress, label, onComplete`; rolls the clock and cross-fades the full semantic register by layering outgoing/incoming `data-theme` grounds over `--son-imm-takeover`/`--son-imm-ease`; hard-cuts under reduced motion. Spine: morning → dosi → dinner → luxe.
- **AmbientField** — `theme, glyph, speed, children`; flat-color drift, no gradient/texture; large-glyph module gated by `--son-glyph-motion` (deliberate canon override, switchable off)
- **ImageSlot** — `ratio (full-bleed|portrait|landscape), src, alt, caption, emptyCaption, theme`; intentional empty state ("Photography to come. Found light, no stock, no AI."), never a gray box
- **KineticDisplay** — `as, size (display|headline), progress, children`; settles over `--son-imm-settle`
- **SectionHeader** — `eyebrow, kicker, children`; per-line `--son-imm-stagger`
- **SeededCTA** — `href (default #briefing), children (default "Request the briefing"), note`; one gated form, UI motion register
- **Marquee** — `label, separator (default 선), duration`; static single row under reduced motion

## Open items for you

1. **Menu voice** — the flagged readme decision (keep preparation-as-decision vs. the plainer live-site register).
2. **Sandoll Myeongjo** — upload the web files when licensed; the stack and sidebar banner are ready for them.
3. **Stale `2,310 SF`** — removed everywhere; true figures stay in Airtable/the briefing.
4. The compiler suggests converting the two ui-kit `@startingPoint` screens into `templates/` — say the word and I'll convert them.
