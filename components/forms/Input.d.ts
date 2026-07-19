import * as React from "react";

/**
 * A hairline text field with an eyebrow label and a specific error line.
 *
 * @startingPoint section="Forms" subtitle="Text field, select, checkbox, switch" viewport="700x300"
 */
export interface InputProps extends Omit<React.InputHTMLAttributes<HTMLInputElement>, "size"> {
  /** Eyebrow-cased label above the field. */
  label?: string;
  /** Error message — name the specific problem, do not apologize. */
  error?: string;
  /** Quiet helper text below the field. */
  hint?: string;
}

export function Input(props: InputProps): React.JSX.Element;
