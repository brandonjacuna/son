> **RETIRED, 2026-07-23 (G3, ruled by Brandon).** The immersive motion
> register this component embeds was retired at the track build
> (`tokens/motion-immersive.css` replaced by `tokens/motion-track.css`,
> 2026-07-22); the token layer no longer supports it. This prompt doc
> describes pre-retirement behavior and is superseded in full. The
> component remains in the generated bundle only until the next external
> regeneration drops it (the compiler is not in this repo; see
> `docs/track-scratch.md` item 14). Do not build new surfaces on it.

# DaypartTakeover

The signature interstitial between chapters. Rolls the timestamp forward (06:30 to 12:45) and cross-fades every semantic token (surface, text, accent, glyph, border) from the outgoing data-theme to the incoming one over --son-imm-takeover with --son-imm-ease. The clock is the transition.

- The daypart spine is morning, dosi, dinner, luxe.
- auto plays once when 55% visible; pass progress (0..1) to scrub it from a ScrollTrigger instead.
- Under prefers-reduced-motion the takeover hard-cuts (no roll, no fade).
