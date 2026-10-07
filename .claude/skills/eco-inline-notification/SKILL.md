---
name: eco-inline-notification
description: Use when building an inline notification that should stay in page context until the user acts or the state changes — not short-lived feedback (use toast-system for that).
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

> **Buttons and ×:** buttons and the close button follow `eco-button` (see `notifications-guide`, "Buttons and the close button"): `btn btn--primary|secondary|blank` with `<span class="btn__label">`, always 32px (XSmall from 769px, Small below), and the × is `icon-btn icon-btn--close` (`icon-btn--close-inverted` on dark/solid surfaces). Live CSS: `eco-design-system/notifications.css`.

> **Close (×) motion:** the × fades the inline notification out and collapses its height (no empty gap). Recommended: `--ease-accelerate-generic`, `--duration-fast-3`, collapse on; override with `--n-close-ease`, `--n-close-duration` or `data-n-close="fade"`. Details in `notifications-guide` ("Motion when a Banner or Inline closes"). The markup builder (`ECO_N.html`) takes `closable: false` to leave the × out.

> **Custom icon (Informational only):** the author may replace the default `info` icon with another from the gallery. The author enters the Google Material Symbols name; it renders as **Outlined, Fill 0, Weight 300, Grade 0** (`font-variation-settings: 'FILL' 0, 'wght' 300, 'GRAD' 0`, class `icon-outline`); the default status icons stay filled. See `notifications-guide`.

## Notification – System Inline (ECO Design System)

**Figma:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=13377-35659

### Used when
- Feedback or status information belongs directly to a specific section, form, or content block on the page
- The message should stay visible until the user acts or the state changes (does **not** disappear automatically)
- Contextual information that doesn't block the rest of the interface

### NOT used when
- A short-lived response to a user action → use **Toast** instead
- The action requires confirmation → use **Modal**
- The message is for a single form field → use `form-helper--error`

---

### Sizes

| Size | Height | Padding | Icon |
|---|---|---|---|
| **Large** | 48px | `12px` all sides | 24px |
| **Small** | 32px (one line) | `4px` container padding, `2px` extra on the left of the header, icon and text `2px` down (see below) | 20px |

> **Small** has no Actionable variant in Figma, and Weak Small exists only for Informational and Warning.

> Renamed from `Medium` to `Large` in the 2026-09 Figma update — same dimensions, name only. Update any code/class names still using `Medium`/`inline-notification--medium` to `Large`.

---

### Usage guidance per status

| Status | Usage guidance | Action |
|---|---|---|
| **Information** | Helper messages, non-blocking input field guidance, system status tooltips. Product stock availability, minimum order quantity warnings, delivery speed estimates, etc. Always paired with an icon for visual guidance. | Task-specific inline link if any. Supports embedded action links for inventory updates. |
| **Success** | Confirms inline form submission success, password changed, or settings saved. | Often auto-fades or features a quiet confirmation action. |
| **Warning** | Alerts the user about sub-optimal inputs (e.g. weak password, non-standard shipping details). | Dismissible by the user if a quiet "Close" action is provided. |
| **Error** | Failed form validations, payment authorization issues, or critical missing fields. | Requires action directly related to rectifying the error to proceed. |

All four statuses support **Strong / Weak** emphasis (no `Weaker` tier for Inline — that's a Banner-only concept).

---

### Variants

#### Emphasis
| Emphasis | Background | Left border | Other borders |
|---|---|---|---|
| **System Strong** | The status color's weak background (see table) | `2px solid [status color]` | `1px solid [status-color-weaker]` |
| **System Weak** | `var(--color-surface-raised-primary)` (`surface-raised-primary`) | `2px solid [status color]` | **none** (2026-09 Figma) |

#### Status + colors

| Status | Left border / Icon | Strong background | Right/top/bottom border | Material Symbol |
|---|---|---|---|---|
| **Informational** | `var(--color-border-information-default)` | `var(--color-surface-information-weaker)` (`surface-information-weaker`) | `var(--color-border-information-weaker)` | `info` |
| **Error** | `var(--color-border-danger-default)` | `var(--color-surface-danger-weaker)` (`surface-danger-weaker`) | `var(--color-border-danger-weaker)` | `error` |
| **Success** | `var(--color-text-success-default)` | `var(--color-surface-success-weaker)` (`surface-success-weaker`) | `var(--color-border-success-weaker)` | `check_circle` |
| **Warning** | `var(--color-border-warning-default)` | `var(--color-surface-warning-weaker)` (`surface-warning-weaker`) | `var(--color-border-warning-weaker)` | `warning` |

> **Informational · Weak** is white (`surface-raised-primary`) with the 2px blue left edge and no outline. As with any Informational notification, the author may replace the default `info` icon with a Google Material Symbols icon of their choice, shown as Outlined (Fill 0, Weight 300, Grade 0). There is no separate "Informational E-Com" variant: it is the same thing as Informational Weak.

#### Layout variants
| Variant | Content |
|---|---|
| **Default** | Status icon + [Title (optional) + body text] + Close button |
| **Actionable** | Same as Default + an action area below the text (indent `32px`) that holds **either buttons or inline links**, not both |

---

### Anatomy

```
[2px border] [Status icon] [TITLE (OPTIONAL): Body text.]   [✕ close 20px]
             [Secondary button] [Primary button]              ← Actionable
             [Inline link] [Inline link]                      ← Actionable, instead of the buttons
```

- **Left border**: `2px solid [status color]`, full height
- **Right/top/bottom border**: Strong only — `1px solid [status-color-weaker]` (`border-{status}-weaker`, same color as the Strong background). Weak has none.
  > `border-*-weaker` was added to `tokens.json` (2026-09) with provisional values equal to `surface-*-weaker`; also add them to the `:root` block of each page when tokens are refreshed.
- **Padding**: `12px` (Large) / `4px` (Small). **Small** (Figma `24000:263507`): the header has `padding-left: 2px` and the icon and text `margin-top: 2px`, so on one line the icon sits **6px** from the left edge, **4px** from the right (the × box is 24px), and **6px** from top and bottom: the content is vertically centered in 32px. With two or more lines the icon, text and × stay **top-aligned** (icon and text start 6px from the top, × 4px).
- **Icon**: Material Symbols Outlined, 24px (Large) / 20px (Small), color = status color
- **Gap** between icon and text: `8px`
- **Title** (optional): `label-sm` — 14px, Bold, uppercase, `var(--color-text-primary)`, `letter-spacing: 0.56px`
- **Body text**: `body-sm` — 14px/20px, Regular, `var(--color-text-primary)`, `letter-spacing: 0.36px`
- **Close button**: Blank xs, `close` icon 20px, `padding: 2px`
- **Shadow**: `elevation-b-20` = `var(--shadow-elevation-b-20)`

#### Actionable — Action Group
- Indent: `padding-left: 32px`
- Buttons: `gap: 8px`, `padding-top: 16px` from the text
- Button size: xs (height 32px)
- Inline links (instead of buttons): `body-sm` underlined, `.inline-notification__links`, `padding-top: 16px`, `8px` row / `16px` column gap

---

### CSS template

```css
/* Wrapper */
.inline-notification {
  display: flex;
  align-items: stretch;
  box-shadow: var(--shadow-elevation-b-20);
}

/* Base — left border + background */
.inline-notification__base {
  display: flex;
  align-items: center;
  overflow: hidden;
  position: relative;
  width: 100%;
}

.inline-notification__left-border {
  width: 2px;
  align-self: stretch;
  flex-shrink: 0;
}

/* Container with right/top/bottom border */
.inline-notification__container {
  flex: 1;
  /* the 1px outline is an inset shadow so it takes no room: padding stays a true 12px (Small 4px), height 48px (32px) */
  --edge: transparent;
  box-shadow: inset 0 1px 0 var(--edge), inset -1px 0 0 var(--edge), inset 0 -1px 0 var(--edge);
}

.inline-notification__inner {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 12px;        /* Large */
  width: 100%;
  box-sizing: border-box;
}

/* Small */
.inline-notification--small .inline-notification__inner {
  padding: 4px;
}
.inline-notification--small .inline-notification__header { padding-left: 2px; }
.inline-notification--small .inline-notification__icon,
.inline-notification--small .inline-notification__text { margin-top: 2px; padding-top: 0; }

.inline-notification__header {
  display: flex;
  gap: 8px;
  align-items: flex-start;
  width: 100%;
}

.inline-notification__icon {
  font-size: 24px;        /* Large */
  flex-shrink: 0;
  font-variation-settings: 'FILL' 1, 'wght' 300, 'GRAD' 0, 'opsz' 24;  /* Filled, wght 300: without this a plain Material Symbols span renders outline */
}
.inline-notification--small .inline-notification__icon {
  font-size: 20px;
}

.inline-notification__text {
  flex: 1;
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 14px;        /* body-sm */
  font-weight: 400;
  line-height: 20px;
  letter-spacing: 0.36px;
  color: var(--color-text-primary);
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
  padding-top: 2px;
}

.inline-notification__title {
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.56px;
  font-feature-settings: 'ss02' 1, 'ss03' 1;
}



/* Actionable — Action Group */
.inline-notification__actions {
  padding-left: 32px;
  width: 100%;
  box-sizing: border-box;
}

.inline-notification__btn-group {
  display: flex;
  gap: 8px;
  align-items: center;
  padding-top: 16px;
  width: 100%;
}

.inline-notification__link {
  padding-top: 8px;
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 14px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: 0.36px;
  color: var(--color-text-primary);
  text-decoration: underline;
  cursor: pointer;
}

/* Status — Informational */
.inline-notification--info.inline-notification--strong { background: var(--color-surface-information-weaker); }
.inline-notification--info .inline-notification__left-border { background: var(--color-surface-information-default); }
.inline-notification--info .inline-notification__container { --edge: var(--color-border-information-weaker); }
.inline-notification--info .inline-notification__icon { color: var(--color-surface-information-default); }

/* Status — Error */
.inline-notification--error.inline-notification--strong { background: var(--color-surface-danger-weaker); }
.inline-notification--error .inline-notification__left-border { background: var(--color-surface-danger-default); }
.inline-notification--error .inline-notification__container { --edge: var(--color-border-danger-weaker); }
.inline-notification--error .inline-notification__icon { color: var(--color-surface-danger-default); }

/* Status — Success */
.inline-notification--success.inline-notification--strong { background: var(--color-surface-success-weaker); }
.inline-notification--success .inline-notification__left-border { background: var(--color-surface-success-default); }
.inline-notification--success .inline-notification__container { --edge: var(--color-border-success-weaker); }
.inline-notification--success .inline-notification__icon { color: var(--color-surface-success-default); }

/* Status — Warning */
.inline-notification--warning.inline-notification--strong { background: var(--color-surface-warning-weaker); }
.inline-notification--warning .inline-notification__left-border { background: var(--color-surface-warning-default); }
.inline-notification--warning .inline-notification__container { --edge: var(--color-border-warning-weaker); }
.inline-notification--warning .inline-notification__icon { color: var(--color-surface-warning-default); }

/* Weak — white background, no right/top/bottom border */
.inline-notification--weak { background: var(--color-surface-raised-primary); }
.inline-notification--weak .inline-notification__container { --edge: transparent; }

/* Buttons and ×: eco-button classes (.btn, .icon-btn.icon-btn--close); live CSS in eco-design-system/notifications.css */
```

### HTML example (Default, Informational, System Strong, Large)

```html
<div class="inline-notification inline-notification--info inline-notification--strong">
  <div class="inline-notification__base">
    <div class="inline-notification__left-border"></div>
    <div class="inline-notification__container">
      <div class="inline-notification__inner">
        <div class="inline-notification__header">
          <span class="material-symbols-outlined inline-notification__icon">info</span>
          <p class="inline-notification__text">
            <span class="inline-notification__title">Title (optional):</span> Body text.
          </p>
          <button type="button" class="icon-btn icon-btn--close" aria-label="Close"><span class="btn__icon" aria-hidden="true">close</span></button>
        </div>
      </div>
    </div>
  </div>
</div>
```

---
