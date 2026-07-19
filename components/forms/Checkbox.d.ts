import * as React from "react";

/** A square hairline checkbox with an inline label. */
export interface CheckboxProps extends Omit<React.InputHTMLAttributes<HTMLInputElement>, "type"> {
  /** Inline label to the right of the box. */
  label?: React.ReactNode;
  /** Error message below the control — border weight plus text, never color alone. */
  error?: string;
}

export function Checkbox(props: CheckboxProps): React.JSX.Element;
