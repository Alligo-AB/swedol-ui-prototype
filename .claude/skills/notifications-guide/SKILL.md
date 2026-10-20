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
| **Success** | Success Default (Green) — `var(--color-surface-success-default)` / `var(--color-text-success-default)` |
| **Warning** | Warning Default (Yellow) — `var(--color-surface-warning-default)` / `var(--color-border-warning-default)` (no dedicated `text-warning` token — pair with `text-primary` for contrast) |
| **Error** | Danger Default (Red) — `var(--color-surface-danger-default)` / `var(--color-text-danger-default)` |
| **Promotion** | Brand Specific — the concept brand's own `accent-default`/`accent-light` token (lime on Swedol), or Neutral (black/white) |
| **E-Com** | Brand (black/white), no status color |

Emphasis levels available per component are documented in that component's own skill — they differ (e.g. Banner supports Strong/Weak/Weaker plus a Large size for status colors; Inline and Toast support Strong/Weak only; E-Com Toast and Modal have no emphasis/status concept at all).

---

### Choosing the emphasis

> **Source (2026-10-13):** design guidance given by the team, **not in Figma** (Figma defines the tiers, not when to pick which). It agrees with the older ECO Banner guidance ("Strong only for what is urgent, Weaker for general information and offers") and with how Carbon, Adobe Spectrum, SAP Fiori and Material treat routine confirmations. Inline is not covered by it: the Inline rule below is a recommendation.

**Weak is the default. Strong is used sparingly.** Status says *what* (color and icon), emphasis says *how loud*. Choose in this order: 1) the **component** by disruption and origin (the decision matrix above), 2) the **status** by meaning (the status table), 3) the **emphasis**. **The status does not decide the emphasis; the consequence does.** An Error does not have to be Strong, and a Warning can be Strong if the consequence is serious.

| Component | Default | Strong only when |
|---|---|---|
| **Toast** | **Weak**: normal feedback, "Saved", "Copied", "Could not save – try again" | Exceptionally, when the feedback needs extra visual attention. **Never for a critical interruption or anything the user must notice or act on:** use a Banner, or an Inline notification near the content. |
| **Banner** | **Weak** (Weaker for general information and offers) | Critical outages, a blocked main flow, risk of data loss, or anything that needs immediate attention. |
| **Inline** | **Weak** | The same as Banner, when it blocks a central flow in that area (recommendation). |

**Weak, for a warning or an error:** an ordinary one that can be handled locally: a failed action that can be tried again, or something the user must correct.
**Strong:** a critical outage, a blocked main flow, risk of data loss, or anything that needs immediate attention.

**A toast disappears.** If the message must be noticed, must stay, or needs an action, it does not belong in a toast: show it as a Banner or near the affected content. For critical or blocking information choose a persistent notification type; do not make a temporary toast louder.

**Ask, in this order, and take the first yes:**
1. Is it normal feedback on something the user just did, including "Could not save – try again"? → **Toast, Weak.**
2. Must the user notice it, act on it, or be able to read it again? → **not a toast.** An Inline notification near the content, or a Banner.
3. Is it general information or an offer? → **Banner, Weaker.**
4. Is it an ordinary warning or error that can be handled locally? → **Weak.**
5. Is it a critical outage, a blocked main flow, risk of data loss, or does it need immediate attention? → **Strong** (a Banner; a Toast only exceptionally).

**Rules**
- **Set the emphasis on purpose** and keep the same situation at the same emphasis across the product.
- **One loud message at a time.** Never stack Strong banners. Campaigns use the Promotion banner, not a higher emphasis.
- **Emphasis is never the only signal.** The icon and the text always carry the status (WCAG 1.4.1).
- Inline Small · Weak is only defined for Informational and Warning (see `eco-inline-notification`).

Examples: "Copied to clipboard", "Saved" → Toast, Success, Weak. "Could not save – try again" → Toast, Error, Weak. "Upload failed" with Retry → Toast, Error, Weak, Actionable. "Free shipping on this order" → Banner, Informational, Weaker. "The shop is down for maintenance" → Banner, Warning or Error, Strong. "You are acting as Anna" → Banner, Informational, Strong (existing ECO use).

Background: [Carbon](https://carbondesignsystem.com/components/notification/usage/), [Adobe Spectrum](https://spectrum.adobe.com/page/toast), [SAP Fiori](https://www.sap.com/design-system/fiori-design-web/v1-151/ui-elements/toast-web-component/usage), [Material](https://material.io/components/snackbars).

---

### The status icon

Icons are reserved for their corresponding alert color or specific intended e-com use. Do not use a reserved icon with a conflicting alert color — each has an established, universal meaning. Preferred icon variant: **Material Symbols Outlined, wght 300, Filled**. A plain `<span class="material-symbols-outlined">` renders **outline** (FILL 0) unless the CSS sets `font-variation-settings: 'FILL' 1, 'wght' 300, 'GRAD' 0, 'opsz' 24` (opsz 20 for 20px icons). Do this on the **default status icons** (info, check_circle, warning, error). **Exception, a user-chosen icon:** an **Informational** notification (Toast, Inline, Banner Small/Large, plus Informational E-Com) may let the author pick another icon from the gallery instead of the default `info`; the author enters the **Google Material Symbols name** (for example `local_shipping`), rendered as **Material Symbols Outlined with Fill 0, Weight 300, Grade 0** (outline), not the filled one. Success, Warning and Error always keep their reserved filled icon. Implemented as `.icon-outline` in `eco-design-system/notifications.css`. The × close icon is always outline.

| Status | Material Symbol |
|---|---|
| **Informational** | `info` |
| **Error** | `error` |
| **Success** | `check_circle` |
| **Warning** | `warning` |

Any icon in the icon gallery is available for **Informational** notifications (shown as outline, see above) and for **Promotion** — those are not reserved to a single icon. (An Inline "Informational E-Com" no longer exists: it was the same as Informational Weak.)

---

### Buttons and the close button

Buttons in notifications follow `eco-button` (classes `btn btn--primary|secondary|blank`, inverted variants on dark/solid surfaces such as Banner Strong): always 32px high, **XSmall from 769px, Small below** (label-sm 14/14 0.56px, label-md 14/14 0.42px). Label inside `<span class="btn__label">`.

The × is the `eco-button` **Close icon button**: `<button class="icon-btn icon-btn--close" aria-label="Close"><span class="btn__icon" aria-hidden="true">close</span></button>`, with `icon-btn--close-inverted` on dark or solid surfaces (Banner Strong, Promotion Dark, E-Com Toast Informational). Hover: `surface-opacity-black-05` (inverted: `surface-opacity-white-20`). The `.toast__close`/`.banner-notification__close` rules in the component skills are older; use the icon-btn classes. Live implementation: `eco-design-system/notifications.css`. The 32px is **scoped to the inside of a notification** (`:is(.toast, .ecom-toast, .modal, .banner-notification, .inline-notification) .btn`), so it also holds when `button.css` loads after `notifications.css` (as on the doc pages, where a bare `.btn` is Large) and a size class such as `btn--md` never changes a notification button.

### Links in notifications

Every link in a notification is an **Inline Link** (`eco-inline-link`): `<a|button class="inline-link inline-link--medium">` (`--small` in Inline notifications), underlined when enabled, underline removed on hover with the hover color, never with an icon. On dark and solid surfaces (Banner Strong, Promotion Dark, E-Com Toast Informational) it uses Text Primary Inverted (`text-action-primary-inverted` / `-hover`). Brand-accent Promotion banners (Strong, Weak) keep the surface's text color on hover, because no hover token exists for it (confirm with design). The action area of Toast, Inline and Banner Large holds **either buttons or inline links**. Live CSS: `eco-design-system/notifications.css`.

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

### Motion when a Banner or Inline closes

The × fades the notification out and collapses its height so no gap is left. Recommended (eco-motion, "Element disappears"): `--ease-accelerate-generic`, `--duration-fast-3` (150 ms), height collapse on. Set per page or wrapper with `--n-close-ease` / `--n-close-duration`; `data-n-close="fade"` on an ancestor turns the collapse off. Reduced motion: hidden at once. Slow durations (450 ms or more) and Decelerate easings are wrong for an exit. Live comparison and code: the **Motion** section on the Banner and Inline docs pages. Implemented in `eco-design-system/notifications.css` + `notifications.js` (`.is-closing`, `.is-collapsing`).

---

### Critical design rules

- **Status icons must strictly correspond with their semantic colors.** Do not mix alert colors with unrelated icons.
- **Task-generated feedback must stay close to context.** Only use global banners or interrupting modals when absolutely unavoidable, to prevent alert fatigue and maintain user flow trust.

---

**Live documentation (converted to the three-page structure 2026-10-13):** the hub `eco-design-system/components/notifications.html` (chooser, decision matrix, status and icon, emphasis guide, dismissing, demos; one page, no tab bar), and for each component three pages (Examples & Guidelines, Specifications, Code): `toast.html`, `toast-ecom.html`, `modal.html`, `banner.html`, `inline.html` (+ `-specifications.html`, `-code.html`). Generators: `eco-design-system/gen/gen_notifications.py`, `gen_toast.py`, `gen_toast_ecom.py`, `gen_modal.py`, `gen_banner.py`, `gen_inline.py`.
