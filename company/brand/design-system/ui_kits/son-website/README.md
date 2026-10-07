# Sŏn — Reservation Website (UI kit)

A type-forward recreation of the Sŏn dinner-register site and reservation flow.

## Screens
- **Home** — wordmark lock-up, the single most important line, the four dayparts as a quiet index.
- **Reserve** — profile lookup at initiation ("We may already have your record"), daypart tabs, date, party, seating. No tipping screen, no upsell, no forced account creation.
- **Confirmed** — functional confirmation in the brand voice. Not congratulatory. No celebration.

## Register
Wrapped in `data-theme="dinner"` — Plum Ink ground, Bone text. Every primitive
(`Button`, `Input`, `Select`, `Tabs`, `Checkbox`, `Card`, `Divider`, `Badge`,
`Wordmark`) resolves its color from the theme, so the same components serve the
other dayparts by changing the `data-theme` value.

## Files
- `index.html` — mounts the app, loads the compiled `_ds_bundle.js`.
- `app.jsx` — screens + a small view state machine (`home → reserve → confirmed`).

## Notes / corners cut
- Date entry is a plain field, not a calendar.
- Imagery is intentionally absent — the dinner register is type-forward, and the
  brand prohibits stock and AI imagery. Drop real Section-10 photography in to extend.
