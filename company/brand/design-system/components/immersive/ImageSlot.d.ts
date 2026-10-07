import * as React from "react";

/**
 * Image container with three sanctioned ratios (full-bleed, portrait ≈3:4,
 * landscape ≈16:9) and a required intentional empty state: a flat daypart
 * ground with a small set caption. Never a gray box, never a placeholder
 * texture, never an AI or stock image. Immersive surfaces only.
 */
export interface ImageSlotProps extends React.HTMLAttributes<HTMLElement> {
  /** Sanctioned ratio. Default "landscape". */
  ratio?: "full-bleed" | "portrait" | "landscape";
  /** Real photography only (found light; no stock, no AI). */
  src?: string;
  alt?: string;
  /** Recessive caption over a filled slot. */
  caption?: string;
  /** Set caption for the intentional empty state. */
  emptyCaption?: string;
  /** Daypart theme for the empty-state ground. */
  theme?: "morning" | "dosi" | "dinner" | "luxe";
}

export function ImageSlot(props: ImageSlotProps): React.JSX.Element;
