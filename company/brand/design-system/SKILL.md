---
name: son-design
description: Use this skill to generate well-branded interfaces and assets for Sŏn, the Korean fine-dining restaurant in Austin, TX (Future Nostalgia Hospitality Group) — either for production or throwaway prototypes/mocks. Contains essential design guidelines, colors, type, fonts, assets, and UI kit components for prototyping across the four dayparts (Good Energy, Dosi, Sŏn, late night).
user-invocable: true
---

Read the `readme.md` file within this skill, and explore the other available files.

If creating visual artifacts (slides, mocks, throwaway prototypes, etc), copy assets out and create static HTML files for the user to view. If working on production code, you can copy assets and read the rules here to become an expert in designing with this brand.

If the user invokes this skill without any other guidance, ask them what they want to build or design, ask some questions, and act as an expert designer who outputs HTML artifacts _or_ production code, depending on the need.

## Orientation

- **`readme.md`** is the design guide: the guiding cultural influences (they inform decisions, they do not veto them), content/voice rules, visual foundations, iconography, and the file manifest. Read it first.
- **`styles.css`** is the single global entry point — link it and you get every token, font-face, and base style. Components read tokens from it.
- **Tokens** live in `tokens/`. Daypart themes switch via `data-theme="morning|dosi|dinner|luxe"` on any ancestor; the unscoped default is the warm editorial register (Bone/Parchment).
- **Components** (`components/`) are React, exported under `window.SNDesignSystem_4d795d` once `_ds_bundle.js` is loaded. Each has a `.d.ts` and `.prompt.md`.
- **`templates/deck/`** is a runnable editorial deck (Section 14 rules) to start a presentation from.
- **`ui_kits/`** are full product recreations: `son-website` (reservation flow) and `good-energy` (morning standing order).

## Non-negotiables (do not violate)

- Eight colors, closed. No tints, shades, gradients, blue accents, or purple anything.
- Jade never appears in the dinner register. Never pair Jade with Aubergine/Plum Ink as the two dominant colors.
- Type: GT Sectra + GT Alpina only; Sandoll Myeongjo (or the flagged Nanum Myeongjo substitute) for the 선 glyph and Hangul dish names only. The 선 glyph is part of the logo and travels with it; it is not required on every surface. Never in Jade.
- Sentence case; UPPERCASE for eyebrows only. "Customer," never "guest." No em dashes, exclamation points, or emoji. Apply the six binary voice tests.
- 1px hairline borders, near-square corners, no drop shadows. Restraint over decoration.
- No AI-generated or stock imagery, ever. Real Section-10 photography only; otherwise stay type-forward or use a drop-in slot.

When in doubt, run the governing test: could this appear in a premium editorial publication — a monograph, a brand book — without embarrassment? If not, find what makes it wrong and remove it.
