# T1: Site hero direction

The hero as described has four things stacked on a film: wordmark, tagline, scroll cue, supporting copy. That is too many voices at once. Direction below.

## Hierarchy
1. **Film** is the hero. It carries the emotion.
2. **Wordmark** is the only fixed anchor. It identifies; it does not need help.
3. **Tagline or supporting copy, not both.** Pick one. If both stay, the tagline is one short line and the supporting copy moves below the fold, where it can be read at rest.
4. **Scroll cue** is a utility, not a feature. Quiet, small, one motion, and it disappears after the first scroll.

## Decisions
- **Keep:** wordmark over film, scroll cue.
- **Cut:** one of tagline or supporting copy. My recommendation: keep the tagline only if it says something specific and true about Sŏn; if it is generic ("a new kind of dining"), cut it and let the film and wordmark stand.
- **Change:** supporting copy to the first section after the hero.

## Wordmark over film
- Place the wordmark where the film is calmest; test over the brightest and darkest frames of the loop.
- Use a gentle overlay or gradient scrim only as needed to hold contrast (wordmark at least 3:1, text at 4.5:1). Do not add a drop shadow.
- Do not resize or recolor the wordmark outside the design-system rules.

## Film
- Slow, real footage from Sŏn or its food; no stock. Loop under 15 seconds, muted, with a poster frame for load and reduced-motion users (`prefers-reduced-motion` shows the still).
- No audio autoplay. Mobile crop must be checked separately.

## Copy
Declarative, short, "customer" not "guest," no em dashes, no performed conviction.

## Reject if
- Text covers faces or the plate in the film.
- More than one animation runs at the same time.
- The hero would work for any restaurant.

## Send back to Web UI
Cut to wordmark plus one line, mobile crop, contrast evidence over the worst frame, reduced-motion still. Return for one round of review.
