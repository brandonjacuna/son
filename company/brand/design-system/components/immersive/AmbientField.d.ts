import * as React from "react";

/**
 * A slow-moving flat-color ground within the palette that keeps a section
 * subtly alive. No gradient, no texture overlay, ever. Optional module: the
 * 선 glyph at large scale in slow motion, gated behind --son-glyph-motion
 * (off = module absent). Static under reduced
 * motion. Immersive surfaces only.
 */
export interface AmbientFieldProps extends React.HTMLAttributes<HTMLDivElement> {
  /** Daypart theme for the field (sets data-theme). */
  theme?: "morning" | "dosi" | "dinner" | "luxe";
  /** Render the animated large-glyph module (still gated by --son-glyph-motion). Default false. */
  glyph?: boolean;
  /** Drift period in seconds. Default 48. */
  speed?: number;
  children?: React.ReactNode;
}

export function AmbientField(props: AmbientFieldProps): React.JSX.Element;
