import * as React from "react";

/** A held surface — hairline border, no shadow. Wraps grouped content. */
export interface CardProps extends React.HTMLAttributes<HTMLElement> {
  /** Element tag to render. Default "div". */
  as?: keyof React.JSX.IntrinsicElements;
  /** primary (default surface) or secondary (warm variation). */
  surface?: "primary" | "secondary";
  /** none · sm (16) · md (24) · lg (32). Default lg. */
  padding?: "none" | "sm" | "md" | "lg";
  children?: React.ReactNode;
}

export function Card(props: CardProps): React.JSX.Element;
