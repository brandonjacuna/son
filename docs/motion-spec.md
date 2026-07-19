# Motion spec

Motion for the Sŏn investor site. It serves the downward funnel or it does not
ship. The structure decision settled the frame: restrained reveal on the
load-bearing beats, no pinned or scrubbed hero, because pinning produces a
section that reads as the end of the page and every exit before the ask is a
lost request. This document applies the earn test per beat, states what does
not move and why, and specifies mobile directly.

Companion inputs: `docs/design-language.md` (grounds, the 선 depth system, the
band, and the full session registers), `docs/structure-decision.md`,
`docs/reference-spec.md` (the extraction, used as reference not as defaults),
`refs/notes/mobile-measurements.md`, and the motion tokens in
`tokens/motion-immersive.css` and `tokens/spacing.css`.

Ma governs time as it governs space: stillness is specified, not left over.
When everything moves, nothing is emphasized.

## Model: timed reveal, not scrub

We are timed-reveal-led, not scrub-led. The reference primary is scrub-led
(Lenis lerp 0.10, per-frame transforms). We take the opposite pole, the one its
own secondaries take: timed on-enter reveals, nothing driven by scroll
position.

- No pin, no scrub, no parallax.
- No smooth-scroll library. Native scroll. We have nothing scrubbing that needs
  smoothing, and native scroll keeps the reader's control surface responsive
  and cannot lag on a phone.
- Only `transform` (translateY) and `opacity` animate. No layout-triggering
  properties.

The site's one narrative gesture is a settle: on enter, an element rises a
short distance and fades up to rest. Duration keyed to element size, ease-out.
Fires once at roughly 85% viewport height, never re-fires. In every
multi-element beat, one element leads or holds and the rest follow at an 80ms
stagger. Stillness is the emphasis.

Honest earn-test result, stated up front: no beat requires motion. The site
makes its whole case static, because it is a type and color site. The reveals
improve pacing and serve the downward flow; they are restrained emphasis, not
load-bearing. That is exactly what the settled frame sanctioned, and it means
the reduced-motion path loses nothing essential.

## The earn test per beat

| Beat | What moves | What holds still | Earn verdict |
| --- | --- | --- | --- |
| Hero | One load entrance: sentence settles (rise 16px, ~550ms), lock-up follows at +100ms; header fades only, no transform. Nothing on scroll. | The ground; the 선 in the lock-up; everything after the entrance. | Establishes the vocabulary and stays out of the way; the sentence is legible within ~300ms. No pin. |
| Moat | Each block settles on enter; the pull-lines (Display) settle larger and alone, isolated as the emphasis. | The oversized 선. It does not drift, does not parallax. It is the largest still thing on the site. | Motion stages the pull-lines so "memory business" lands. The still 선 is the memory that stays, the thing that does not walk out. Load-bearing as stillness. |
| Opportunity | Text column settles at 80ms stagger; the 선 field glyph settles at +120ms after the headline. | The peacock field once swapped. | The 선 arrives just after "where they meet," enacting the intersection. Earned. |
| Team | Two founder blocks settle, staggered so they read as two people. Headshots fade only, no rise, no scale. | The faces; the Parchment ground. | Real people resolve quietly; no ken-burns (scale is a vestibular trigger and a spectacle move). Stillness is the dignity, and it matches "no performed conviction." |
| Model | The one expressive motion. Headline settles first, then the band builds left-to-right (first light to last call) as a transform wipe, ~1000ms, labels landing per stripe. | The headline (the anchor) after it settles; the band after it completes. | Motion equals argument here: four returns across one footprint, the day sweeping a fixed space. The single beat where noticeable motion is justified. |
| Ask | Headline settles; the Bone form card settles once. Fields do not narrative-reveal. | The Aubergine ground; the form. | Form motion is feedback, not narrative. Adding excitement motion to conversion is performed conviction; the reader is already warm. Confirmation cross-fades (200ms), no celebration, no confetti. |
| Footer | Settle once, staggered: lock-up, location, then the bare 선, which lands last and holds. | Everything after. The site ends on a still glyph, mirroring the moat. | Quiet close, no further ask, minimal motion by design. |

## Timing scale

Derived, keyed to element size, departing from the raw immersive tokens (which
were tuned to scrubbed reference panels). Ease-out throughout, `--son-imm-ease`
cubic-bezier(0.22, 1, 0.36, 1), the weighty settle curve.

| Class | Elements | Rise | Duration |
| --- | --- | --- | --- |
| Small | eyebrow, body, labels | 12px | 450ms |
| Medium | headline, subhead, form card | 16px | 600ms |
| Large | display sentence, pull-lines | 20 to 24px | 700ms |
| Band | the daypart band, once | per-stripe wipe | ~1000ms total, per stripe ~260ms staggered |

Stagger between siblings: 80ms. Trigger: IntersectionObserver on enter, once,
at roughly 85% viewport height, never re-firing.

Departures from the reference and the tokens, named:

- Reference is scrub-led; we are timed-reveal-led. No scrub, no pin.
- Immersive takeover 1400ms is unused. We have no chapter takeover; a takeover
  reads as a page end, the funnel's exit failure.
- Immersive settle 850ms compressed to 700ms for triggered reveals; 850 was
  tuned to scrubbed panels.
- Immersive lerp 0.08 and reference lerp 0.10 not applied; native scroll.
- The reference's "80ms stagger, unconfirmed" is adopted on our own judgment,
  not imported as measured.

## The feedback register

Distinct from narrative motion, from `tokens/spacing.css`: fast 100ms, standard
200ms, slow 400ms, with the standard, enter, and exit eases. It marks state
change and carries no meaning. It governs:

- Header hide on scroll. Hides on scroll-down past the hero, reveals on
  scroll-up (translateY, ~300ms, ease). A1 stays one small scroll-up away for
  the already-convinced reader.
- Field focus, hover, and validation. The 2px focus ring is the single 2px
  exception in the 1px-hairline system.
- The confirmation cross-fade, form to confirmation, 200ms. Functional, not
  congratulatory. No confetti.

## Reduced motion

A designed path, not a kill switch. Reduced is not none: keep what
communicates, drop what moves.

- Reveals become opacity-only, no translate.
- The daypart band appears complete, no wipe. Its claim, four labeled colors
  from first light to last call, is fully legible static, so nothing is lost.
- The hero appears complete, no entrance.
- The header still hides and reveals, but instantly.

The immersive register collapses to effectively zero inside
`[data-surface="immersive"]` per `tokens/motion-immersive.css`; the UI register
collapses via the global kill rule in `tokens/spacing.css`. Every JS consumer
of the immersive tokens must also gate on `prefers-reduced-motion`.

## Mobile, specified directly

Not derived from desktop. The reference's horizontal-scrub collapse is
irrelevant to us, because we have no horizontal axis to lose.

- Same timed-reveal model. Reduce rise to 8 to 10px; the hero may be fade-only.
- The daypart band stacks vertically (first light at the top, last call at the
  bottom) and wipes top-to-bottom, which reads as the day passing and pulls the
  eye down. The one motion climax serves the funnel better on the phone than on
  the desktop.
- Native scroll, no smooth-scroll library, so touch scrolling stays native and
  responsive.
- Touch targets at least 44 by 44px; focus-visible rings on tap-through; no
  hover-dependent motion, of which there is none.
- Header hide on scroll as on desktop; the mobile chrome is minimal, the Sŏn
  wordmark and "Request the briefing."

## Session registers

The motion-relevant entries live in full alongside the design entries in
`docs/design-language.md`, under "Session registers." In brief, excluded this
session: ambient 선 drift, scrubbing the band, smooth-scroll and inertia,
parallax, and the chapter takeover. Reconsidered and admitted: the band as the
one noticeable ~1s wipe, and narrative motion at all as restrained,
reduced-motion-safe emphasis. Each is argued there.
