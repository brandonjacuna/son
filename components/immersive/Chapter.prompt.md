> **RETIRED, 2026-07-23 (G3, ruled by Brandon).** The immersive motion
> register this component embeds was retired at the track build
> (`tokens/motion-immersive.css` replaced by `tokens/motion-track.css`,
> 2026-07-22); the token layer no longer supports it. This prompt doc
> describes pre-retirement behavior and is superseded in full. The
> component remains in the generated bundle only until the next external
> regeneration drops it (the compiler is not in this repo; see
> `docs/track-scratch.md` item 14). Do not build new surfaces on it.

# Chapter

Pinned, scroll-scrubbed chapter bound to a daypart. Vertical scroll drives lateral travel of the inner track; direct children carry data-imm-rate ("1.25") to ride at different rates. Motion is position-scrubbed, never fade-in.

- Requires GSAP + ScrollTrigger loaded on the page (window.gsap / window.ScrollTrigger). Without them, or under prefers-reduced-motion, the chapter collapses to a static readable stack: same content, no pin.
- length is the scroll distance in viewport heights (default 2.5).
- timeLabel prints the chapter clock ("06:30") in the eyebrow voice.
