import * as React from "react";

/**
 * A row of tabs marked by a single hairline rule beneath the active label.
 *
 * @startingPoint section="Navigation" subtitle="Hairline tab row" viewport="700x120"
 */
export interface TabItem {
  id: string;
  label: React.ReactNode;
}

export interface TabsProps extends Omit<React.HTMLAttributes<HTMLDivElement>, "onChange"> {
  items: TabItem[];
  /** Controlled active tab id. */
  value?: string;
  /** Uncontrolled initial tab id. */
  defaultValue?: string;
  /** Fires with the newly selected tab id. */
  onChange?: (id: string) => void;
}

export function Tabs(props: TabsProps): React.JSX.Element;
