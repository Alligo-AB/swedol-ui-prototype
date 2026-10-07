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
| **Large** | 48px | `8px` vert, `12px` horiz | 24px | `label-md`: 16px/16px, 0.48px, Bold, uppercase | `body-md`: 17px/24px, 0.32px, Regular |
| **Small** | 40px | `8px` all sides | 24px | `label-sm`: 14px/14px, 0.56px, Bold, uppercase | `body-sm`: 14px/20px, 0.36px, Regular |
| **XSmall** | 32px | `8px` all sides | 24px | `label-sm`: 14px/14px, 0.56px, Bold, uppercase | `body-sm`: 14px/20px, 0.36px, Regular |

#### Mobile / Tablet (`xs`/`sm`, 0–768px)

| Size | Height | Padding | Arrow icon | Label | Select text |
|---|---|---|---|---|---|
| **Large** | 40px | `8px` all sides | 24px | `label-md` (mobile): 14px/14px, 0.42px, Bold, uppercase | `body-md` (mobile): 16px/22px, 0.32px, Regular |
| **Small** | 32px | `8px` all sides | 24px | `label-sm` (mobile): 12px/12px, 0.48px, Bold, uppercase | `body-sm`: 14px/20px, 0.36px, Regular |

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

#### 3. Active (the field is being used)
> **Decision (2026-10-07):** the selected border shows only while the select has focus or its menu is open (`:focus`, `[aria-expanded="true"]`, `[data-state="active"]` for docs demos). A chosen option alone keeps the default border.

| Property | Value |
|---|---|
| Border | `1px solid var(--color-border-selected)` → `#000000` |
| Background | `var(--color-surface-raised-primary)` → `#ffffff` |
| Select text | `var(--color-text-primary)` → `#000000` |

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
| Message | `var(--color-text-success-default)` → `#17730d` |

#### 7. Disabled
| Property | Value |
|---|---|
| Border | `1px solid var(--color-border-disabled)` → `#dad9d7` |
| Background | `var(--color-surface-raised-secondary)` → `#f6f6f6` |
| Select text | `var(--color-text-disabled)` → `#939595` |
| Cursor | `not-allowed` |

---

### Hint/message text (all sizes)
- `body-sm`: 14px/20px, letter-spacing 0.36px, Regular
- `font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1`
- Left icon on error: 20px Material Symbols `error` (filled, wght 300)

---

### Dropdown list

A select opens the ECO **Menu** (`eco-menu`, Exposed dropdown menu) instead of the browser's list. The native `<select>` stays in the markup as the form control (value, label, `disabled`, `:has()` active state, forms); a small script only replaces the popup.

| Field size | Menu size |
|---|---|
| Large | Large (`.menu`) |
| Small, XSmall | Small (`.menu--sm`) |

- The menu is appended to `.input-wrap`, `position: absolute`, `top: calc(100% + 4px)`, as wide as the field, `z-index: 10` (local, no token).
- **Placement:** opens below. If it does not fit and there is more room above, it opens upwards (`.menu--up`, `bottom: calc(100% + 4px)`); if it fits in neither direction the list height is capped and scrolls. Checked on open; window resize closes the menu.
- Rows come from the `<option>`s; the empty placeholder option is skipped; a disabled `<option>` becomes a disabled row (`aria-disabled`, skipped by arrow keys); the chosen row shows the check (`aria-selected="true"`).
- Click or Enter/Space/Arrow opens; Up/Down/Home/End move; Enter/Space choose and fire `change`; Escape closes and returns focus to the field; Tab or an outside click closes.
- CSS and script: `/components/css/menu.css`, `/components/css/select.css` and `<script src="/components/js/select-menu.js"></script>` (the docs page `select.html` links the same files). Add each once per page.
- Mobile: the same menu is used (no native picker), rows 40px Large / 32px Small.

---

> **CSS:** `components/css/select.css` is the live, tested stylesheet (mobile-first, desktop from 769px). Where the HTML below and the CSS differ, follow the CSS file.

### CSS

Link the shared stylesheet. Never copy its rules into a page, and never write a parallel version:

```html
<link rel="stylesheet" href="/components/css/select.css">
```

`components/css/select.css` is the single source for this component. The docs page `eco-design-system/components/select.html` links the same file and prints it in its Code section. Mobile-first, desktop from 769px, `var(--…)` only. The `[data-state="…"]` selectors in it are only for the docs pages' forced-state demos and do nothing elsewhere. To change the component, edit that file.

Also link `/components/css/menu.css` when the select opens a custom menu (eco-menu).

---
