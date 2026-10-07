import * as React from "react";

/**
 * The Sŏn wordmark lock-up. Typographic, never drawn. 선 is part of the logo;
 * on this mark it is centered below the Latin word at a constant ratio.
 *
 * @startingPoint section="Brand" subtitle="Wordmark lock-up — vertical, latin, glyph" viewport="700x260"
 */
export interface WordmarkProps {
  /** Responsive architecture: full vertical lock-up, Latin alone, or 선 alone. */
  variant?: "lockup" | "latin" | "glyph";
  /** Latin wordmark size in px. The 선 glyph scales from this. Default 64. */
  size?: number;
  /** Override both Latin + glyph color. Defaults to theme text / glyph tokens. */
  color?: string;
  /** Override only the 선 glyph color. Never set this to Jade. */
  glyphColor?: string;
  /** Horizontal alignment of the stacked lock-up. Default "center". */
  align?: "left" | "center" | "right";
  className?: string;
  style?: React.CSSProperties;
}

export function Wordmark(props: WordmarkProps): React.JSX.Element;
