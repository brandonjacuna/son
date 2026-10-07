import * as React from "react";

/** A single hairline rule, optionally centered around an eyebrow label. */
export interface DividerProps extends React.HTMLAttributes<HTMLElement> {
  /** Optional centered uppercase label between two rules. */
  label?: string;
  /** Vertical margin: sm (16) · md (32) · lg (48). Default md. */
  spacing?: "sm" | "md" | "lg";
}

export function Divider(props: DividerProps): React.JSX.Element;
