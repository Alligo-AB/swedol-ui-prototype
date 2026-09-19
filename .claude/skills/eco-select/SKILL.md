---
name: eco-select
description: Use when building or reviewing select fields/dropdowns — sizes, states, and the dropdown arrow per the ECO Design System.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Select – Sizes & States (ECO Design System)

Select is used to let the user choose one option from a list. The component's size and states follow the same system as input fields.

> All select fields share: `font-family: 'Breuer Condensed', sans-serif`, `font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1`, `border-radius: 0` (sharp corners), `appearance: none` (hides the native arrow), and a custom dropdown arrow (24px, Material Symbols `arrow_drop_down`).

---

### Sizes per breakpoint

#### Desktop (`md:`, 769px+)

| Size | Height | Padding | Arrow icon | Label | Select text |
|---|---|---|---|---|---|
| **Large** | 48px | `8px` vert, `12px` horiz | 24px | `label-md`: 16px/16px, 0.48px, Bold, uppercase | `body-md`: 16px/24px, 0.32px, Regular |
| **Small** | 40px | `8px` all sides | 24px | `label-sm`: 14px/14px, 0.56px, Bold, uppercase | `body-sm`: 14px/20px, 0.28px, Regular |
| **XSmall** | 32px | `8px` all sides | 24px | `label-sm`: 14px/14px, 0.56px, Bold, uppercase | `body-sm`: 14px/20px, 0.28px, Regular |

#### Mobile / Tablet (`xs`/`sm`, 0–768px)

| Size | Height | Padding | Arrow icon | Label | Select text |
|---|---|---|---|---|---|
| **Large** | 40px | `8px` all sides | 24px | `label-md` (mobile): 14px/14px, 0.42px, Bold, uppercase | `body-md` (mobile): 16px/22px, 0.32px, Regular |
| **Small** | 32px | `8px` all sides | 24px | `label-sm` (mobile): 12px/12px, 0.48px, Bold, uppercase | `body-sm`: 14px/20px, 0.28px, Regular |

> The dropdown arrow is positioned absolutely: `right: 12px`, `top: 50%`, `transform: translateY(-50%)`. The right padding on the select must be at least `40px` to leave room for the arrow.

---

### States

Every state must be implemented each time a select field is created.

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

#### 3. Active (an option selected)
| Property | Value |
|---|---|
| Border | `1px solid var(--color-border-selected)` → `#000000` |
| Background | `var(--color-surface-raised-primary)` → `#ffffff` |
| Select text | `var(--color-text-primary)` → `#000000` |

> **Active state for select** cannot be detected with `:not(:placeholder-shown)`. Use JS to add the `.is-active` class on `.form-select-wrap` when a non-default option is selected: `select.addEventListener('change', e => wrap.classList.toggle('is-active', e.target.selectedIndex !== 0))`.

#### 4. Focus (keyboard focus)
| Property | Value |
|---|---|
| Border (select box) | `1px solid var(--color-border-input-default)` → `#939595` |
| Focus ring (outer) | `2px solid var(--color-border-focus)` → `#455efb`, `inset: -3px` |
| Background | `var(--color-surface-raised-primary)` → `#ffffff` |

> The focus ring is shown **only** on keyboard navigation (Tab). Implemented via `body.keyboard-nav .input-wrap:focus-within::after { opacity: 1; }`. Clicking opens the dropdown without a ring.

#### 5. Error
| Property | Value |
|---|---|
| Border | `1px solid var(--color-border-danger-default)` → `#d90000` |
| Background | `var(--color-surface-raised-primary)` → `#ffffff` |
| Message | `var(--color-text-danger-default)` → `#d90000` + 20px error icon (`error`, filled) to the left |

#### 6. Success
| Property | Value |
|---|---|
| Border | `1px solid var(--color-border-success-default)` → `#248616` |
| Background | `var(--color-surface-raised-primary)` → `#ffffff` |
| Message | `var(--color-text-success)` → `#248616` |

#### 7. Disabled
| Property | Value |
|---|---|
| Border | `1px solid var(--color-border-disabled)` → `#dad9d7` |
| Background | `var(--color-surface-raised-secondary)` → `#f6f6f6` |
| Select text | `var(--color-text-disabled)` → `#939595` |
| Cursor | `not-allowed` |

---

### Hint/message text (all sizes)
- `body-sm`: 14px/20px, letter-spacing 0.28px, Regular
- `font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1`
- Left icon on error: 20px Material Symbols `error` (filled, wght 300)

---

### CSS template (Desktop Large – all states)

```css
/* Wrapper — handles the focus ring and arrow icon */
.form-select-wrap {
  position: relative;
}

/* Focus ring (see input section — same mechanism) */
.input-wrap.form-select-wrap::after {
  content: '';
  position: absolute;
  inset: -3px;
  border: 2px solid var(--color-border-focus);
  pointer-events: none;
  opacity: 0;
  transition: opacity var(--duration-fast-2) var(--ease-standard);
}
body.keyboard-nav .input-wrap.form-select-wrap:focus-within::after { opacity: 1; }

/* Select */
.form-select {
  height: 48px;                   /* Desktop Large */
  padding: 8px 40px 8px 12px;     /* extra right padding for the arrow */
  border: 1px solid var(--color-border-input-default);
  background: var(--color-surface-raised-primary);
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 16px;                /* body-md */
  font-weight: 400;
  line-height: 24px;
  letter-spacing: 0.32px;
  color: var(--color-text-primary);
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
  appearance: none;
  cursor: pointer;
  width: 100%;
  box-sizing: border-box;
  outline: none;
  transition: border-color var(--duration-fast-3) var(--ease-standard);
}

/* Dropdown arrow */
.form-select-arrow {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  pointer-events: none;
  width: 24px;
  height: 24px;
}

/* Hover */
.form-select:hover { border-color: var(--color-border-dark); }

/* Active (an option selected) — toggled via JS */
.form-select-wrap.is-active .form-select { border-color: var(--color-border-selected); }

/* Focus (cursor in the field) */
.form-select:focus { border-color: var(--color-border-selected); }

/* Error */
.form-select--error { border-color: var(--color-border-danger-default) !important; }

/* Success */
.form-select--success { border-color: var(--color-border-success-default) !important; }

/* Disabled */
.form-select:disabled {
  background: var(--color-surface-raised-secondary);
  border-color: var(--color-border-disabled);
  color: var(--color-text-disabled);
  cursor: not-allowed;
}
```

---
