---
name: eco-input
description: Use when building or reviewing text input fields — sizes (Large/Small/XSmall), all states (enabled/hover/active/focus/error/success/disabled), and label/hint patterns per the ECO Design System.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Input Fields – Sizes & States (ECO Design System)

Input fields are used to enter free text, numbers, or other data. They can be combined with icons, hint text, and error messages.

> All input fields share: `font-family: 'Breuer Condensed', sans-serif`, `font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1`, and `border-radius: 0` (sharp corners).

---

### Sizes per breakpoint

#### Desktop (`md:`, 769px+)

| Size | Height | Padding | Icon | Label | Input text |
|---|---|---|---|---|---|
| **Large** | 48px | `var(--dimension-spacing-space-12, 12px)` horiz, `var(--dimension-spacing-space-8, 8px)` vert | 24px | `label-md`: 16px/16px, 0.48px, Bold, uppercase | `body-md`: 16px/24px, 0.32px, Regular |
| **Small** | 40px | `var(--dimension-spacing-space-8, 8px)` all sides | 20px | `label-sm`: 14px/14px, 0.56px, Bold, uppercase | `body-sm`: 14px/20px, 0.28px, Regular |
| **XSmall** | 32px | `var(--dimension-spacing-space-8, 8px)` all sides | 20px | `label-sm`: 14px/14px, 0.56px, Bold, uppercase | `body-sm`: 14px/20px, 0.28px, Regular |

#### Mobile / Tablet (`xs`/`sm`, 0–768px)

| Size | Height | Padding | Icon | Label | Input text |
|---|---|---|---|---|---|
| **Large** | 40px | `var(--dimension-spacing-space-8, 8px)` all sides | 24px | `label-md` (mobile): 14px/14px, 0.42px, Bold, uppercase | `body-md` (mobile): 16px/22px, 0.32px, Regular |
| **Small** | 32px | `var(--dimension-spacing-space-8, 8px)` all sides | 20px | `label-sm` (mobile): 12px/12px, 0.48px, Bold, uppercase | `body-sm`: 14px/20px, 0.28px, Regular |

> **Rule of thumb:** Desktop Large = 48px (standard forms), Desktop Small = 40px (compact surfaces), Mobile Large = 40px (standard forms on mobile). Always choose the size that fits the breakpoint.

**Hint/message text** (below the input field, all sizes):
- `body-sm`: 14px/20px, letter-spacing 0.28px, Regular
- Left icon: 20px (Material Symbols Outlined, wght 300)

---

### States

Every state must be implemented each time an input field is created. States control border, background, text color, and helper text.

#### 1. Enabled (default)
| Property | Value |
|---|---|
| Border | `1px solid var(--color-border-input-default)` → `#939595` |
| Background | `var(--color-surface-raised-primary)` → `#ffffff` |
| Placeholder text | `var(--color-text-tertiary)` → `#737373` |
| Hint/message | `var(--color-text-tertiary)` → `#737373` |

#### 2. Hover
| Property | Value |
|---|---|
| Border | `1px solid var(--color-border-dark)` → `#333333` |
| Background | `var(--color-surface-raised-primary)` → `#ffffff` |
| Placeholder text | `var(--color-text-tertiary)` → `#737373` |
| Hint/message | `var(--color-text-tertiary)` → `#737373` |

#### 3. Active (filled in / focus with a value)
| Property | Value |
|---|---|
| Border | `1px solid var(--color-border-selected)` → `#000000` |
| Background | `var(--color-surface-raised-primary)` → `#ffffff` |
| Input text | `var(--color-text-primary)` → `#000000` |
| Clear icon | Shown (cancel icon, filled, 20px) + divider `1px, var(--color-border-tertiary)` |
| Hint/message | `var(--color-text-tertiary)` → `#737373` |

#### 4. Focus (keyboard focus, no ring on select)
| Property | Value |
|---|---|
| Border (input box) | `1px solid var(--color-border-input-default)` → `#939595` |
| Focus ring (outer) | `2px solid var(--color-border-focus)` → `#455efb`, `inset: -3px` (offset outside) |
| Background | `var(--color-surface-raised-primary)` → `#ffffff` |
| Placeholder text | `var(--color-text-tertiary)` → `#737373` |

> The focus ring is placed as an absolute element `inset: -3px` outside the input box – not as an `outline` on the input element itself.

#### 5. Error
| Property | Value |
|---|---|
| Border | `1px solid var(--color-border-danger-default)` → `#d90000` |
| Background | `var(--color-surface-raised-primary)` → `#ffffff` |
| Input text | `var(--color-text-primary)` → `#000000` |
| Message | `var(--color-text-danger-default)` → `#d90000` + 20px error icon to the left of the text |

#### 6. Success
| Property | Value |
|---|---|
| Border | `1px solid var(--color-border-success-default)` → `#248616` |
| Background | `var(--color-surface-raised-primary)` → `#ffffff` |
| Input text | `var(--color-text-primary)` → `#000000` |
| Message | `var(--color-text-success)` → `#248616` |

#### 7. Disabled
| Property | Value |
|---|---|
| Border | `1px solid var(--color-border-disabled)` → `#dad9d7` |
| Background | `var(--color-surface-raised-secondary)` → `#f6f6f6` |
| Placeholder text | `var(--color-text-disabled)` → `#939595` |
| Message | `var(--color-text-disabled)` → `#939595` |
| Cursor | `not-allowed` |

---

### Anatomy

```
[Label]                      ← label-md/sm, uppercase, text-primary
[Icon] [Input text...]  [✕|⊕] ← input box with optional left icon + right clear+divider+action
[Hint/error message]         ← body-sm, tertiary / danger / success
```

- **Label**: Always uppercase, Bold font. Placed above the input box with `gap: var(--dimension-spacing-space-4, 4px)`.
- **Left icon** (optional): Material Symbols Outlined, wght 300, 24px (Large) / 20px (Small/XSmall).
- **Right clear icon**: Shown only in the `Active` state. Icon size 20px (cancel, filled). Separated from other right-side icons by a 1px divider (`border-tertiary`, 16px tall).
- **Message**: Always `body-sm` (14px), shown below the input box with `gap: var(--dimension-spacing-space-4, 4px)`.

---

### CSS template (Desktop Large – all states)

```css
/* Wrapper */
.form-field {
  display: flex;
  flex-direction: column;
  gap: var(--dimension-spacing-space-4, 4px);
}

/* Label */
.form-label {
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 16px;          /* Desktop Large: label-md */
  font-weight: 700;
  line-height: 16px;
  letter-spacing: 0.48px;
  text-transform: uppercase;
  color: var(--color-text-primary);
  font-feature-settings: 'ss02' 1, 'ss03' 1;
}

/* Input wrapper (position: relative for the focus ring) */
.input-wrap { position: relative; }

/* Focus ring (absolute, outside) — animated with opacity */
.input-wrap::after {
  content: '';
  position: absolute;
  inset: -3px;
  border: 2px solid var(--color-border-focus);
  pointer-events: none;
  opacity: 0;
  transition: opacity var(--duration-fast-2) var(--ease-standard);
}
/* Ring only shows on keyboard navigation — body.keyboard-nav is set via JS */
body.keyboard-nav .input-wrap:focus-within::after { opacity: 1; }

/* Input */
.form-input {
  height: 48px;                  /* Desktop Large */
  padding: var(--dimension-spacing-space-8, 8px) var(--dimension-spacing-space-12, 12px);
  border: 1px solid var(--color-border-input-default);
  background: var(--color-surface-raised-primary);
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 16px;               /* body-md */
  font-weight: 400;
  line-height: 24px;
  letter-spacing: 0.32px;
  color: var(--color-text-primary);
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
  width: 100%;
  box-sizing: border-box;
  outline: none;
}

/* Placeholder */
.form-input::placeholder {
  color: var(--color-text-tertiary);
}

/* Hover */
.form-input:hover { border-color: var(--color-border-dark); }

/* Active (has a value — placeholder not shown) */
.form-input:not(:placeholder-shown) { border-color: var(--color-border-selected); }

/* Focus — inner border stays border-input-default; only the blue ring (::after) appears */
.form-input:focus { border-color: var(--color-border-input-default); }

/* Error */
.form-input--error { border-color: var(--color-border-danger-default); }

/* Success */
.form-input--success { border-color: var(--color-border-success-default); }

/* Disabled */
.form-input:disabled {
  background: var(--color-surface-raised-secondary);
  border-color: var(--color-border-disabled);
  color: var(--color-text-disabled);
  cursor: not-allowed;
}

/* Hint/message */
.form-helper {
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 14px;               /* body-sm */
  font-weight: 400;
  line-height: 20px;
  letter-spacing: 0.28px;
  color: var(--color-text-tertiary);
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
}
.form-helper--error   { color: var(--color-text-danger-default); display: flex; align-items: center; gap: var(--dimension-spacing-space-4, 4px); }
.form-helper--success { color: var(--color-text-success); }
.form-helper--disabled{ color: var(--color-text-disabled); }

/* Mobile Small override (32px) */
@media (max-width: 768px) {
  .form-input--sm {
    height: 32px;
    font-size: 14px;
    line-height: 20px;
    letter-spacing: 0.28px;
  }
  .form-label--sm {
    font-size: 12px;
    line-height: 12px;
    letter-spacing: 0.48px;
  }
}
```

---
