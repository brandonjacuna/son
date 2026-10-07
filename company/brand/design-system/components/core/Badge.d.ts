import * as React from "react";

/** Small category label in the eyebrow register. Recessive by default. */
export interface BadgeProps extends React.HTMLAttributes<HTMLSpanElement> {
  /** outline (hairline) · accent (theme accent rule) · solid (inverse fill). */
  variant?: "outline" | "accent" | "solid";
  children?: React.ReactNode;
}

export function Badge(props: BadgeProps): React.JSX.Element;
