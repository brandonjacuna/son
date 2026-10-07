> **RETIRED, 2026-07-23 (G3, ruled by Brandon).** The immersive motion
> register this component embeds was retired at the track build
> (`tokens/motion-immersive.css` replaced by `tokens/motion-track.css`,
> 2026-07-22); the token layer no longer supports it. This prompt doc
> describes pre-retirement behavior and is superseded in full. The
> component remains in the generated bundle only until the next external
> regeneration drops it (the compiler is not in this repo; see
> `docs/track-scratch.md` item 14). Do not build new surfaces on it.

# FullBleedSection

Edge-to-edge section that breaks the page margin; the dark registers (dinner, luxe) are the hero grounds. Immersive surfaces only: the page root must carry data-surface="immersive" so the --son-imm-* register resolves.

- theme binds a daypart (data-theme); ground picks the surface token (primary | secondary | inverse).
- Uses 100vw + negative margin, so it bleeds out of any centered column.
- Content sits inside the 10% page margin (--son-margin-page).
