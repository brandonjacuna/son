import * as React from "react";

/** A native select in the hairline field register. Error reads through border weight plus text, never color alone. */
export interface SelectProps extends React.SelectHTMLAttributes<HTMLSelectElement> {
  /** Eyebrow-cased label above the control. */
  label?: string;
  /** Error message — name the specific problem, do not apologize. */
  error?: string;
  /** Quiet helper text below the control. */
  hint?: string;
  children?: React.ReactNode;
}

export function Select(props: SelectProps): React.JSX.Element;
