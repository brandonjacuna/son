# 03 Son design system
source: company/brand/design-system: docs/codified-patterns.md, browser-support.md, handoff.md, structure-motion-decision.md, adherence/*, .stylelintrc.json, eslint.config.mjs, readme.md | read: full text | verified: yes (read this build)

## Rows
| id | kind | row | quote | locator |
|---|---|---|---|---|
| 03.1 | rule | Gated surface: delete gate classes from root (or disable JS), read top to bottom, operate every control; fix by making the failing state the stylesheet default | "any content that vanishes, any control that dies, any frozen frame" | patterns §1 |
| 03.2 | anti | Reject per-frame scripts keeping two things in sync (scroll-handler pins, scroll-keyed clip-paths); use stacking, sticky geometry, observers | "Never realize it as a per-frame script" | patterns §2 |
| 03.3 | cue | Reduced-motion block zeroing duration only -> late appearance; zero delay too (spacing.css kill is duration only) | "ships staggered invisibility" | patterns §3 |
| 03.4 | rule | Focus can land in un-entered content: arm it at once; floor scrub fields at entered text | "Nothing focusable is ever invisible." | patterns §3 |
| 03.5 | rule | Submit or live swap freezes block size and answers in place | "An interior swap never moves the document under the reader." | patterns §4 |
| 03.6 | rule | Linked values are adjacent tokens, pairing named in the comment; split encodings are drift | "they will drift apart" | patterns §5 |
| 03.7 | cue | Probe reads oddly -> suspect the probe: ring while focused, the fill that paints, fontFamily is cascade not rendered face | "the unfocused measurement is of nothing" | patterns §7 |
| 03.8 | model | Four blocking checks in `npm run lint`; geometry and scroll need `npm run shoot / scrollframes / timeframes` | "What they do NOT cover: rendered geometry, scroll behavior, and visual judgment" | readme.md |
| 03.9 | cue | Check blind spots: JSX px rule skips numeric values; 13 files on a px debt register; copy check skips JSX; track check is static -> read by eye | "numeric style values (`fontSize: 14`) pass unflagged" | eslint.config.mjs |
| 03.10 | rule | Dark panels, html, body, main gain no stacking-context property; var() there counts as a violation | "content drowns under the glyph, silently" | check-track.mjs |
| 03.11 | decision | Tested cells are supported; the rest is "unverified", not broken. Desktop Safari untested | "unverified, not broken" | browser-support.md |
| 03.12 | model | Feedback register (state change) vs narrative register (must carry load static cannot); conversion surfaces feedback only | "Narrative motion never touches the ask." | motion-decision §4-5 |

## Tensions
- Frame cites `docs/motion-spec.md`; it was superseded 2026-07-20 by `structure-motion-decision.md`.
- Frame calls inertia damping scrolljacking; the system ships Lenis smoothing, a bounded pin, and scrub.
- Names: package.json says "Future Nostalgia Hospitality Group"; tokens and ESLint use daypart codes (morning, dosi, dinner, luxe).

## Not usable
- handoff.md tasks; motion-spec.md timings (superseded); track panel map (retired investor page).
