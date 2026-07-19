import * as React from "react";

/**
 * The repeatable "request the briefing" call — a quiet hairline button that
 * appears at several beats, all pointing to one gated form. Uses the UI
 * motion register (a control, not a narrative element).
 */
export interface SeededCTAProps extends React.AnchorHTMLAttributes<HTMLAnchorElement> {
  /** The one gated form. Default "#briefing". */
  href?: string;
  /** Button copy. Default "Request the briefing". */
  children?: React.ReactNode;
  /** Quiet fine-print line under the button. */
  note?: string;
}

export function SeededCTA(props: SeededCTAProps): React.JSX.Element;
