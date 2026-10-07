import * as React from "react";

/**
 * The chapter-marker system: eyebrow plus kicker plus display statement,
 * landing with a per-line --son-imm-stagger. Instant under reduced motion.
 * Immersive surfaces only.
 */
export interface SectionHeaderProps extends React.HTMLAttributes<HTMLElement> {
  /** Uppercase chapter marker, e.g. "02 · The space". */
  eyebrow?: string;
  /** Short lead line above the statement. */
  kicker?: string;
  /** The display statement. */
  children?: React.ReactNode;
}

export function SectionHeader(props: SectionHeaderProps): React.JSX.Element;
