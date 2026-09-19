---
name: eco-inline-notification
description: Use when building an inline notification that should stay in page context until the user acts or the state changes — not short-lived feedback (use toast-system for that).
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

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
| **Small** | 32px | `4px` all sides | 20px |

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
| **System Strong** | The status color's weak background (see table) | `2px solid [status color]` | `1px solid [status-color-weak]` |
| **System Weak** | `var(--color-surface-raised-primary)` (`surface-raised-primary`) | `2px solid [status color]` | `1px solid [status-color-weak]` |

#### Status + colors

| Status | Left border / Icon | Strong background | Right/top/bottom border | Material Symbol |
|---|---|---|---|---|
| **Informational** | `var(--color-border-information-default)` | `var(--color-surface-information-weaker)` (`surface-information-weaker`) | `var(--color-border-information-weak)` | `info` |
| **Error** | `var(--color-border-danger-default)` | `var(--color-surface-danger-weaker)` (`surface-danger-weaker`) | `var(--color-border-danger-weak)` | `error` |
| **Success** | `var(--color-text-success)` | `var(--color-surface-success-weaker)` (`surface-success-weaker`) | `var(--color-border-success-weak)` | `check_circle` |
| **Warning** | `var(--color-border-warning-default)` | `var(--color-surface-warning-weaker)` (`surface-warning-weaker`) | `var(--color-border-warning-weak)` | `warning` |
| **Informational E-Com** | `var(--color-border-information-default)` | — (always Weak, `var(--color-surface-raised-primary)`) | **none** | Optional (e.g. `local_shipping`) |

> **Informational E-Com** always has a white background (`surface-raised-primary`, `var(--color-surface-raised-primary)`) and **no** right/top/bottom border — just the 2px left blue one. The icon isn't reserved and is picked contextually from the gallery.

#### Layout variants
| Variant | Content |
|---|---|
| **Default** | Status icon + [Title (optional) + body text] + Close button |
| **Actionable** | Same as Default + buttons and/or a text link below the text (indent `32px`) |

---

### Anatomy

```
[2px border] [Status icon] [TITLE (OPTIONAL): Body text.]   [✕ close 20px]
             [Secondary button] [Primary button]              ← Actionable
             [Text link]                                      ← Actionable
```

- **Left border**: `2px solid [status color]`, full height
- **Right/top/bottom border**: `1px solid [status-color-weak]`
- **Padding**: `12px` (Large) / `4px` (Small)
- **Icon**: Material Symbols Outlined, 24px (Large) / 20px (Small), color = status color
- **Gap** between icon and text: `8px`
- **Title** (optional): `label-sm` — 14px, Bold, uppercase, `var(--color-text-primary)`, `letter-spacing: 0.56px`
- **Body text**: `body-sm` — 14px/20px, Regular, `var(--color-text-primary)`, `letter-spacing: 0.28px`
- **Close button**: Blank xs, `close` icon 20px, `padding: 2px`
- **Shadow**: `elevation-b-20` = `var(--shadow-elevation-b-20)`

#### Actionable — Action Group
- Indent: `padding-left: 32px`
- Buttons: `gap: 8px`, `padding-top: 16px` from the text
- Button size: xs (height 32px)
- Text link: `body-sm` underlined, `padding-top: 8px` below the buttons

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
  border-width: 1px 1px 1px 0;
  border-style: solid;
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

/* Header row: icon + text + close */
.inline-notification__header {
  display: flex;
  gap: 8px;
  align-items: flex-start;
  width: 100%;
}

.inline-notification__icon {
  font-size: 24px;        /* Large */
  flex-shrink: 0;
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
  letter-spacing: 0.28px;
  color: var(--color-text-primary);
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
  padding-top: 2px;
}

.inline-notification__title {
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.56px;
  font-feature-settings: 'ss02' 1, 'ss03' 1;
}

.inline-notification__close {
  flex-shrink: 0;
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 2px;
  font-size: 20px;
  color: var(--color-text-primary);
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
  letter-spacing: 0.28px;
  color: var(--color-text-primary);
  text-decoration: underline;
  cursor: pointer;
}

/* Status — Informational */
.inline-notification--info.inline-notification--strong { background: var(--color-surface-information-weaker); }
.inline-notification--info .inline-notification__left-border { background: var(--color-surface-information-default); }
.inline-notification--info .inline-notification__container { border-color: var(--color-border-information-weak); }
.inline-notification--info .inline-notification__icon { color: var(--color-surface-information-default); }

/* Status — Error */
.inline-notification--error.inline-notification--strong { background: var(--color-surface-danger-weaker); }
.inline-notification--error .inline-notification__left-border { background: var(--color-surface-danger-default); }
.inline-notification--error .inline-notification__container { border-color: var(--color-border-danger-weak); }
.inline-notification--error .inline-notification__icon { color: var(--color-surface-danger-default); }

/* Status — Success */
.inline-notification--success.inline-notification--strong { background: var(--color-surface-success-weaker); }
.inline-notification--success .inline-notification__left-border { background: var(--color-surface-success-default); }
.inline-notification--success .inline-notification__container { border-color: var(--color-border-success-weak); }
.inline-notification--success .inline-notification__icon { color: var(--color-surface-success-default); }

/* Status — Warning */
.inline-notification--warning.inline-notification--strong { background: var(--color-surface-warning-weaker); }
.inline-notification--warning .inline-notification__left-border { background: var(--color-surface-warning-default); }
.inline-notification--warning .inline-notification__container { border-color: var(--color-border-warning-weak); }
.inline-notification--warning .inline-notification__icon { color: var(--color-surface-warning-default); }

/* Weak — white background */
.inline-notification--weak { background: var(--color-surface-raised-primary); }

/* Informational E-Com — white background, no right/top/bottom border */
.inline-notification--ecom .inline-notification__container {
  border: none;
}
.inline-notification--ecom .inline-notification__left-border { background: var(--color-surface-information-default); }
.inline-notification--ecom .inline-notification__icon { color: var(--color-surface-information-default); }
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
          <button class="inline-notification__close" aria-label="Close">
            <span class="material-symbols-outlined">close</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</div>
```

---
