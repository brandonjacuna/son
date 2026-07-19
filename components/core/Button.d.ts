import * as React from "react";

/**
 * Button — the brand's action primitive in three registers.
 *
 * @startingPoint section="Core" subtitle="Primary, secondary, ghost · three sizes" viewport="700x160"
 */
export interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  /** primary (filled inverse) · secondary (hairline outline) · ghost (type only). */
  variant?: "primary" | "secondary" | "ghost";
  /** sm · md · lg. Default md. */
  size?: "sm" | "md" | "lg";
  fullWidth?: boolean;
  children?: React.ReactNode;
}

export function Button(props: ButtonProps): React.JSX.Element;
