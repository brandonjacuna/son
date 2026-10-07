> **RETIRED, 2026-07-23 (G3, ruled by Brandon).** The immersive motion
> register this component embeds was retired at the track build
> (`tokens/motion-immersive.css` replaced by `tokens/motion-track.css`,
> 2026-07-22); the token layer no longer supports it. This prompt doc
> describes pre-retirement behavior and is superseded in full. The
> component remains in the generated bundle only until the next external
> regeneration drops it (the compiler is not in this repo; see
> `docs/track-scratch.md` item 14). Do not build new surfaces on it.

# AmbientField

A slow-moving flat-color ground that keeps a section subtly alive. One flat panel of the theme's secondary surface drifts over the primary surface. No gradient, no texture overlay, ever.

- glyph renders the 선 glyph at large scale in slow motion. This is an optional module, gated behind --son-glyph-motion: set it to off on any scope to remove the module without touching anything else.
- Static under prefers-reduced-motion.
