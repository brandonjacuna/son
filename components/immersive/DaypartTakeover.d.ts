import * as React from "react";

/**
 * The full-screen interstitial between chapters — the signature component.
 * Rolls the timestamp forward and cross-fades every semantic token (surface,
 * text, accent, glyph, border) from the outgoing data-theme to the incoming
 * one over --son-imm-takeover with --son-imm-ease. The clock is the
 * transition. The daypart spine is morning, dosi, dinner, luxe. Hard-cuts
 * under prefers-reduced-motion. Immersive surfaces only.
 */
export interface DaypartTakeoverProps extends React.HTMLAttributes<HTMLDivElement> {
  /** Outgoing daypart theme. */
  from?: "morning" | "dosi" | "dinner" | "luxe";
  /** Incoming daypart theme. */
  to?: "morning" | "dosi" | "dinner" | "luxe";
  /** Clock start, "HH:MM". */
  fromTime?: string;
  /** Clock end, "HH:MM". */
  toTime?: string;
  /** Play once when scrolled into view. Default true. */
  auto?: boolean;
  /** External scrub 0..1 — overrides auto. */
  progress?: number;
  /** Quiet eyebrow under the clock, e.g. the incoming daypart's name. */
  label?: string;
  /** Fires when the takeover lands on the incoming theme. */
  onComplete?: () => void;
}

export function DaypartTakeover(props: DaypartTakeoverProps): React.JSX.Element;
