import * as React from "react";

/**
 * Pinned, scroll-scrubbed chapter bound to a daypart theme. Vertical scroll
 * drives lateral travel of the inner track; direct children may carry
 * data-imm-rate (e.g. "1.3") to ride at different rates. Position-scrubbed,
 * never fade-in. Requires GSAP ScrollTrigger on the page; collapses to a
 * static readable stack under prefers-reduced-motion or without GSAP.
 * Immersive surfaces only.
 */
export interface ChapterProps extends React.HTMLAttributes<HTMLElement> {
  /** Daypart theme for this chapter (sets data-theme). */
  theme?: "morning" | "dosi" | "dinner" | "luxe";
  /** The chapter's clock marker, e.g. "06:30". */
  timeLabel?: string;
  /** Scrub on/off. Off renders the static stack. Default true. */
  scrub?: boolean;
  /** Scroll length as a multiple of viewport height. Default 2.5. */
  length?: number;
  children?: React.ReactNode;
}

export function Chapter(props: ChapterProps): React.JSX.Element;
