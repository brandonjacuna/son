import * as React from "react";

/**
 * Large GT Sectra Display type, sentence case, entering and settling as its
 * own beat over --son-imm-settle (or scrubbed). The large-text-as-event
 * mechanism. Instant under reduced motion. Immersive surfaces only.
 */
export interface KineticDisplayProps extends React.HTMLAttributes<HTMLElement> {
  /** Rendered element. Default "h2". */
  as?: keyof React.JSX.IntrinsicElements;
  /** Type scale. Default "display". */
  size?: "display" | "headline";
  /** External scrub 0..1 — overrides the settle-on-view beat. */
  progress?: number;
  children?: React.ReactNode;
}

export function KineticDisplay(props: KineticDisplayProps): React.JSX.Element;
