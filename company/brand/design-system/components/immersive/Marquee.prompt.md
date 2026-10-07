> **RETIRED, 2026-07-23 (G3, ruled by Brandon).** The immersive motion
> register this component embeds was retired at the track build
> (`tokens/motion-immersive.css` replaced by `tokens/motion-track.css`,
> 2026-07-22); the token layer no longer supports it. This prompt doc
> describes pre-retirement behavior and is superseded in full. The
> component remains in the generated bundle only until the next external
> regeneration drops it (the compiler is not in this repo; see
> `docs/track-scratch.md` item 14). Do not build new surfaces on it.

# Marquee

A horizontal moving label row, used sparingly, sentence case, for a single repeated-label moment. Separated by the 선 glyph by default.

- One per page at most; it is an accent, not a pattern.
- Static single row under prefers-reduced-motion.
