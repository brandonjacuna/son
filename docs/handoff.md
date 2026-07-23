# Handoff — ownership, tags, and the standing state

Written 2026-07-23, HEAD at the close of the handoff session. Reader:
Dominic, who builds and hosts on Vercel and has none of this context.
Start at the repo readme's "Start here" section; this document is the
ownership record. The build-session record is `docs/build-state.md`; the
rules that graduated from the build are `docs/codified-patterns.md`; the
tested browser boundary is `docs/browser-support.md`.

## What ships

`track/` is the site: a scroll-driven single page (eleven panels, a
drawn 선 still layer, a pinned band, a form, a scrubbed coda). It is
static — serve the repo root and open `track/index.html`; there is no
build step. `site/` is the v3 fallback (below), not the ship.

## Dominic — tasks, not notes

1. **Provision the POST endpoint.** The form in `track/index.html`
   carries a marked INTEGRATION POINT: set `data-endpoint` on
   `.ask-form`. Today a valid submit shows the confirmation and logs a
   console warning instead of sending; the persistence flag
   (`son-ask-confirmed`) is success-gated, so it is never written until
   a real endpoint returns success. The five validation strings and the
   client behavior are settled — the server side is yours.
2. **Deduplicate by email, server-side, on that endpoint** (build-spec
   §6). The client deliberately does not attempt it: a browser cannot
   promise uniqueness, so the guarantee lives with you.
3. **Run the external regeneration, dropping the retired immersive
   components.** The compiler is not in this repo. Its artifacts
   (`_ds_bundle.js`, `_ds_manifest.json`, `_adherence.oxlintrc.json`,
   the `.d.ts` files) are snapshots, established non-authoritative
   2026-07-23 (see the readme's Index section). The regeneration should:
   drop the nine retired immersive components (their prompt docs carry
   supersession banners) and with them the GSAP dependency; regenerate
   the `.d.ts` files to declare the DOM/event passthrough the components
   actually implement (found at the ESLint migration — the current
   `.d.ts` under-declare); and rebuild the bundle, which is stale (one
   manifest path was hand-patched to fix a 404, and one bundle string
   will diverge if the address sweep executes before regeneration).
4. **Deploy.** Vercel, static. Before ship, run the first checks in
   `docs/browser-support.md` — desktop Safari was never tested and is
   the highest-risk untested surface; the wipe (P6→P7), the re-reveal
   (P9→P10), the pin under real trackpad momentum, and the coda scrub
   against toolbar dynamics are the four things to look at. `npm install
   && npm run lint` must be clean before any deploy; every check blocks.

## Open, and Brandon's

1. **Founder portraits** — the reserved P8 frames are standing and
   ship empty until real Section-10 photography exists (the system
   ships no images by doctrine).
2. **Verify-pending facts in the copy** (docs/copy.md): the accolade
   source, Dominic's credentials and years, counsel's word on the
   disclaimer, and the two-business-day promise. None ship unverified.
3. **The motion-registers canon amendment into the Brand Guidelines**
   (standing since R1). The two-register motion system is ratified and
   built; the Brand Guidelines document has not yet absorbed it.

## The two tags — why both exist, and why neither gets deleted

- **`v3-fallback`** is the document-form build, frozen in `site/`. It
  is canon-clean and shippable: no scroll dependency, no driver, no
  pin. After the freeze it received exactly one change class (the
  retirement migration: the carried ease value and the reduced-motion
  delay kill). It exists so that there is always a shippable site if
  the track's scroll dependency ever fails a surface the boundary
  document did not cover. Known residual: it carries the ch-measure
  class the track fixed for Firefox (stale-ch), unfixed — awareness,
  not a ship blocker, because it is the fallback.
- **`v4-track`** is what ships — the scrub-led build this whole record
  describes.

Delete `v3-fallback` and the only no-dependency fallback and the frozen
document-form reference go with it. Delete `v4-track` and the ship goes.
Neither is redundant with the other; they are different answers to
different failure modes. The merge to production is Brandon's call.

## The address sweep (EXECUTED 2026-07-23, ruled)

The site (`site/`, `track/`) was already clean. External-capable
carriers now hold the city-only form: the guidelines deck (both
variants, seven sites each including the zip note-row), slide 01, the
deck template, the two immersive card docs, and the `styles.css` header
comment. The good-energy confirmation line dropped the location
outright (demo copy, not voice copy — "The walk-up. We'll have it
warm."), and the matching `_ds_bundle.js` string was hand-patched per
precedent. Internal records KEEP the real address by ruling:
`readme.md`, `docs/content-architecture.md` (the historical record of
this exact problem), `refs/`, `uploads/`. Do not "fix" those.

## The standing doors (named, unspent)

Recorded where they live; listed here so nobody rediscovers them:

- **The couplet door** (build-spec §7 amendment 3): if P3's composed
  couplet under-holds in the hand, the staged argument is the locked
  one-panel couplet strophe — never Subhead, never Lead Light.
- **The phone-only still-size override** (type-decision, judgment
  register 10): if the phone coda's crop cost ever reads too high.
- **Body 16 → 17** (the watch item): reopens on evidence only.
- **The skip-link door** (scratch 3j): reopens if the keyboard stop
  count ever grows past seven.
- **Chrome focus nuance** (scratch 3i): scrolling down with focus in
  the revealed bar re-hides it; revisit only if a real keyboard session
  minds.
- **The reduced-motion mid-session toggle** keeps load-time gating
  (recorded limitation).
