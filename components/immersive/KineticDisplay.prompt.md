> **RETIRED, 2026-07-23 (G3, ruled by Brandon).** The immersive motion
> register this component embeds was retired at the track build
> (`tokens/motion-immersive.css` replaced by `tokens/motion-track.css`,
> 2026-07-22); the token layer no longer supports it. This prompt doc
> describes pre-retirement behavior and is superseded in full. The
> component remains in the generated bundle only until the next external
> regeneration drops it (the compiler is not in this repo; see
> `docs/track-scratch.md` item 14). Do not build new surfaces on it.

# KineticDisplay

Large GT Sectra Display type, sentence case, entering and settling as its own beat over --son-imm-settle with --son-imm-ease. The large-text-as-event mechanism.

- Settles once when 40% visible, or pass progress (0..1) to scrub it.
- size: display | headline (the fluid clamp tokens).
- Under prefers-reduced-motion the tokens collapse and the text is simply there.
