---
name: notifications-guide
description: Use BEFORE building a notification, to decide which status (Informational/Success/Warning/Error/Promotion/E-Com) and component type (Banner/Inline/Toast/E-Com Toast/Modal) fits the situation. Then read the skill for the specific component type (eco-banner-notification, eco-inline-notification, eco-toast-system, eco-toast-ecom, or eco-modal-ecom).
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Notification Component Guide (ECO Design System)

**Figma:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=23432-270125

An authoritative reference detailing implementation, behavior, status support, and color usage for the five notification components. Use this to preserve consistency across task-generated and system-generated states.

---

### When to use a notification

Notifications inform users of important status changes and updates. Transparency is a fundamental aspect of building user trust (Jakob Nielsen's first usability heuristic). Notifications should be relevant to the user and as minimally disruptive as possible. There are two primary use cases:

**Task-generated notifications** are triggered in response to a user action during a specific task. They provide direct, immediate feedback and should be placed in the region of the page where the user is working. Shown in **Toast**, **E-Com Toast**, or **Inline**.

**System-generated notifications** are triggered by:
- The application or system, independent of user action.
- Administrators using the backend notification service to push information to users.

They provide updates on background system status or out-of-context events that have finished. Shown in **Banner** (or a Notification panel).

Examples of when to send a system-generated notification: campaign/price-change info, scheduled system maintenance, campaigns that benefit the user, unpaid invoices.

### When NOT to use a notification

Limit notifications to only when necessary. Each notification should stay confined to the portion of the interface and workflow where it's relevant. Being interrupted creates a frustrating experience — frequent distractions lower productivity and lead to alert fatigue.

---

### Notification decision matrix

Choose the right notification component based on context, disruption level, and origin:

| Type | Disruption level | When to choose |
|---|---|---|
| **Banner** | Medium — top placement | Global/system or product-level messages, including promotional e-commerce campaigns and brand-specific communication. |
| **Inline** | Low — non-disruptive, embedded | Contextual task-generated feedback or a status response placed in the region of active work. |
| **Toast** | Low — slide-in transient feedback | Brief, transient confirmations or acknowledgements requiring minimal user interaction. |
| **E-Com Toast** | Low — transient e-commerce feedback | Add-to-cart confirmation or brief e-commerce information with minimal interaction. |
| **Modal** | High — fully blocking dialog | Crucial information requiring immediate attention or a decision before proceeding. |

Then read the skill for the chosen component type: `eco-banner-notification`, `eco-inline-notification`, `eco-toast-system`, `eco-toast-ecom`, or `eco-modal-ecom`.

---

### Status colors

| Status | Color role |
|---|---|
| **Informational** | Information Default (Blue) — `var(--color-surface-information-default)` / `var(--color-text-information-default)` |
| **Success** | Success Default (Green) — `var(--color-surface-success-default)` / `var(--color-text-success)` |
| **Warning** | Warning Default (Yellow) — `var(--color-surface-warning-default)` / `var(--color-border-warning-default)` (no dedicated `text-warning` token — pair with `text-primary` for contrast) |
| **Error** | Danger Default (Red) — `var(--color-surface-danger-default)` / `var(--color-text-danger-default)` |
| **Promotion** | Brand Specific — the concept brand's own `accent-default`/`accent-light` token (lime on Swedol), or Neutral (black/white) |
| **E-Com** | Brand (black/white), no status color |

Emphasis levels available per component are documented in that component's own skill — they differ (e.g. Banner supports Strong/Weak/Weaker plus a Large size for status colors; Inline and Toast support Strong/Weak only; E-Com Toast and Modal have no emphasis/status concept at all).

---

### The status icon

Icons are reserved for their corresponding alert color or specific intended e-com use. Do not use a reserved icon with a conflicting alert color — each has an established, universal meaning. Preferred icon variant: **Material Symbols Outlined, wght 300, Filled**.

| Status | Material Symbol |
|---|---|
| **Informational** | `info` |
| **Error** | `error` |
| **Success** | `check_circle` |
| **Warning** | `warning_amber` |

Any icon in the icon gallery is available for **E-Com Informational** and **Promotion** — those are not reserved to a single icon.

---

### Dismissing a modal or notification

A passive modal or notification stays on screen until it's dismissed. This can be done by:

| Method | Used in |
|---|---|
| **× (close icon)** | Toast, E-Com Toast, Inline, Banner, Modal |
| **Click outside the modal area** | Modal |
| **ESC key** | Modal |
| **Auto-dismiss** | Toast (Success, E-Com) |

> A Modal must **always** support all three: × in the header, ESC, and close on backdrop click.
> For a Banner, whether a dismiss (×) button is shown at all is generally decided by the banner's administrator/content owner, not fixed by the component.

---

### Critical design rules

- **Status icons must strictly correspond with their semantic colors.** Do not mix alert colors with unrelated icons.
- **Task-generated feedback must stay close to context.** Only use global banners or interrupting modals when absolutely unavoidable, to prevent alert fatigue and maintain user flow trust.

---
