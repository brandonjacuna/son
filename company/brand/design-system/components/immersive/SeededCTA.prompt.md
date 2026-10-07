> **RETIRED, 2026-07-23 (G3, ruled by Brandon).** The immersive motion
> register this component embeds was retired at the track build
> (`tokens/motion-immersive.css` replaced by `tokens/motion-track.css`,
> 2026-07-22); the token layer no longer supports it. This prompt doc
> describes pre-retirement behavior and is superseded in full. The
> component remains in the generated bundle only until the next external
> regeneration drops it (the compiler is not in this repo; see
> `docs/track-scratch.md` item 14). Do not build new surfaces on it.

# SeededCTA

The repeatable "request the briefing" call: a quiet hairline button designed to appear at several beats of the narrative, all pointing to ONE gated form (default #briefing).

- It is a control, so it uses the UI motion register, not the immersive one.
- note prints one fine-print line under the button.
- Do not multiply destinations; every seed points at the same form.
