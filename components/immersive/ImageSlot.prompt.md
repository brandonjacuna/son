> **RETIRED, 2026-07-23 (G3, ruled by Brandon).** The immersive motion
> register this component embeds was retired at the track build
> (`tokens/motion-immersive.css` replaced by `tokens/motion-track.css`,
> 2026-07-22); the token layer no longer supports it. This prompt doc
> describes pre-retirement behavior and is superseded in full. The
> component remains in the generated bundle only until the next external
> regeneration drops it (the compiler is not in this repo; see
> `docs/track-scratch.md` item 14). Do not build new surfaces on it.

# ImageSlot

Image container with three sanctioned ratios: full-bleed, portrait (3:4), landscape (16:9). The empty state is intentional: a flat daypart ground with a small set caption ("Photography to come. Found light, no stock, no AI."). Never a gray box, never a placeholder texture, never an AI or stock image.

- Real Section-10 photography only; found light; the brand prohibits stock and AI imagery on public surfaces.
- caption renders recessively over a filled slot.
