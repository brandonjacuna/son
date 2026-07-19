import * as React from "react";

/**
 * Edge-to-edge section that breaks the page margin. The dark registers
 * (dinner, luxe) are the hero grounds. Allowed only under
 * [data-surface="immersive"] roots.
 */
export interface FullBleedSectionProps extends React.HTMLAttributes<HTMLElement> {
  /** Daypart theme bound to this section (sets data-theme). */
  theme?: "morning" | "dosi" | "dinner" | "luxe";
  /** Surface token used as the ground. */
  ground?: "primary" | "secondary" | "inverse";
  /** Rendered element. Default "section". */
  as?: keyof React.JSX.IntrinsicElements;
  /** Minimum height. Default "100vh". */
  minHeight?: string;
  children?: React.ReactNode;
}

export function FullBleedSection(props: FullBleedSectionProps): React.JSX.Element;
