import * as React from "react";

/**
 * A horizontal moving label row, used sparingly, sentence case — for a
 * single repeated-label moment if needed. Static single row under reduced
 * motion. Immersive surfaces only.
 */
export interface MarqueeProps extends React.HTMLAttributes<HTMLDivElement> {
  /** The repeated label, sentence case. */
  label: string;
  /** Separator between repeats. Default the 선 glyph. */
  separator?: string;
  /** Seconds per loop. Default 36. */
  duration?: number;
}

export function Marquee(props: MarqueeProps): React.JSX.Element;
