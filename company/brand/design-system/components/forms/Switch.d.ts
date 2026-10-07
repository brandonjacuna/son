import * as React from "react";

/** A hairline toggle. On state uses the theme accent. Marks state, not importance. */
export interface SwitchProps extends Omit<React.InputHTMLAttributes<HTMLInputElement>, "type"> {
  /** Inline label to the right of the track. */
  label?: React.ReactNode;
  /** Error message below the control — border weight plus text, never color alone. */
  error?: string;
}

export function Switch(props: SwitchProps): React.JSX.Element;
