# 04 Son design system
source: company/brand/design-system: readme.md, docs/codified-patterns.md, docs/content-architecture.md, Button/Card/Input/Wordmark/Chapter/ImageSlot .prompt.md | read: full text | verified: yes

## Rows
| id | kind | row | quote | locator |
|---|---|---|---|---|
| 04.1 | model | System answers rules; the page body (function, content, hierarchy, states) is the brief's | "rules and vocabulary, never one page's body" | codified, top |
| 04.2 | rule | Hand `styles.css` and `.prompt.md` paths; never hex, font, px; answered already | "consumers link one file" | readme, Index |
| 04.3 | anti | Never ask for tint, gradient, ninth color, or a reference's palette | "Never introduce a ninth color, a tint, a shade" | readme, Visual |
| 04.4 | cue | No register stated -> theme unchosen -> brief names it (`data-theme`); system never selects | "switch at the semantic tier via `data-theme`" | readme, Visual |
| 04.5 | decision | UI motion (state change) or track motion (narrative)? Brief states per surface | "keeping the registers separate is the point" | readme, Motion |
| 04.6 | rule | Brief lists states needed (error, confirmation, empty, reduced motion) and where a response renders | "never moves the document under the reader" | codified 4 |
| 04.7 | rule | Component docs give props, not purpose; brief names the one primary action | "Primary fills, secondary outlines in a hairline" | Button.prompt |
| 04.8 | cue | Lint passes -> geometry, scroll, visual judgment unchecked -> brief writes those acceptance criteria | "rendered geometry, scroll behavior, and visual judgment" | readme, Start |
| 04.9 | anti | Never route to immersive components; point at `track/`; source beats generated files | "Do not build new surfaces on them." | readme, Index |
| 04.10 | decision | Photo or type-forward? No images shipped, AI and stock banned; name a real photo source or type-only | "this system ships **no images**" | readme, Imagery |
| 04.11 | decision | Open decisions stay named gaps (menu voice, bleed element); maker never fills by default | "an open decision, not a builder's discretion" | content-arch, hero |
| 04.12 | rule | Check lease status before an address enters an external-surface brief | "no external surface names the address" | content-arch, Location |

## Tensions
- Readme company name differs from CLAUDE.md; two daypart codenames sit in `data-theme` tokens. Flag to Brandon in one line; never repeat in a brief.
- Pre-lease no-address rule (dated, investor site) vs verbatim address; check live.
- Card.prompt sample uses "Pyeong-sang", internal under the Korean canon line.
- Index still lists retired immersive components.

## Not usable
- content-architecture slots, affordances, word budgets: investor material.
- codified 2, 5, 6, 7: maker craft, no brief decision. Type table, timings: in tokens.
