# FullBleedSection

Edge-to-edge section that breaks the page margin; the dark registers (dinner, luxe) are the hero grounds. Immersive surfaces only: the page root must carry data-surface="immersive" so the --son-imm-* register resolves.

- theme binds a daypart (data-theme); ground picks the surface token (primary | secondary | inverse).
- Uses 100vw + negative margin, so it bleeds out of any centered column.
- Content sits inside the 10% page margin (--son-margin-page).
