---
name: eco-checkbox
description: Use when building or reviewing checkboxes — light mode (standard and the detailed table icon variant) and dark mode, including all states (enabled/hover/focus/selected/indeterminate/disabled).
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Checkbox Styling (ECO Design System)

Checkboxes follow the ECO Design System spec: total area **24×24px**, visible box **16×16px**.

### Size model
- Visible box: `16px × 16px` (`appearance: none`, custom border)
- Margin: `4px` on all sides → total area 24×24px
- Focus ring: `outline: 2px`, `outline-offset: 2px` → exactly fills the margin (2px gap + 2px ring = 4px)

### States

| State | Visual rule |
|---|---|
| Enabled | 1.5px solid `var(--color-surface-100)` border, white background |
| Hover | border-width: 2px |
| Focus | Blue focus ring `#0052CC` **(deviates from `border-focus` = `var(--color-border-focus)` used in every other form component — not changed here, confirm with design before either value is used)**, 2px, offset 2px |
| Selected | Black fill `var(--color-border-selected)`, white checkmark (SVG) |
| Indeterminate | Black fill `var(--color-surface-100)`, white dash (SVG) |
| Disabled | Border `var(--color-surface-15)`, white background, `cursor: not-allowed` |
| Disabled Selected | Fill `var(--color-border-input-default)`, border `var(--color-border-input-default)` |
| Disabled label | Text `var(--color-text-disabled)` via `:has(input:disabled) span` |

### HTML structure
```html
<label class="form-checkbox-item">
  <input type="checkbox" />
  <span>Label</span>
</label>
```

### CSS template
```css
.form-checkbox-item { display: flex; align-items: center; gap: 8px; cursor: pointer; }
.form-checkbox-item input[type="checkbox"] {
  appearance: none; width: 16px; height: 16px;
  border: 1.5px solid var(--color-surface-100); background: var(--color-surface-raised-primary);
  cursor: pointer; flex-shrink: 0; margin: 4px;
}
.form-checkbox-item input[type="checkbox"]:hover { border-width: 2px; }
.form-checkbox-item input[type="checkbox"]:focus-visible { outline: 2px solid #0052CC; outline-offset: 2px; } /* deviates from var(--color-border-focus) — see flag above */
.form-checkbox-item input[type="checkbox"]:checked { background-color: var(--color-surface-100); border-color: var(--color-surface-100); /* + SVG checkmark */ }
.form-checkbox-item input[type="checkbox"]:indeterminate { background-color: var(--color-surface-100); border-color: var(--color-surface-100); /* + SVG dash */ }
.form-checkbox-item input[type="checkbox"]:disabled { border-color: var(--color-border-disabled); cursor: not-allowed; }
.form-checkbox-item input[type="checkbox"]:disabled:checked { background-color: var(--color-surface-40); border-color: var(--color-surface-40); }
.form-checkbox-item:has(input:disabled) { cursor: not-allowed; }
.form-checkbox-item:has(input:disabled) span { color: var(--color-text-disabled); }
```

---

## Checkbox Styling (ECO Design System)

Figma reference: `node-id=6408-8453`

Always implement checkboxes with `<input type="checkbox">` + CSS — never with `<img>` or SVG files.

### States

| State | Background | Border | Checkmark |
|---|---|---|---|
| **Default (unchecked)** | `--color-background-primary` | `1.5px solid --color-border-selected` | — |
| **Checked** | `--color-surface-100` (black) | `--color-border-selected` | White (`stroke="white"`) |
| **Hover (unchecked)** | — | `2px solid --color-border-selected` | — |
| **Hover (checked)** | `--color-text-disabled` (var(--color-text-disabled)) | `--color-text-disabled` (var(--color-text-disabled)) | White |
| **Disabled unchecked** | `--color-background-primary` | `--color-border-disabled` (var(--color-surface-15)) | — |
| **Disabled checked** | `--color-surface-disabled` (var(--color-surface-disabled)) | none (matches background) | Gray (`stroke="var(--color-surface-40)"`) |
| **Indeterminate** | `--color-surface-100` (black) | `--color-border-selected` | White horizontal line |

> **NOTE:** `disabled:checked` = light gray background (var(--color-surface-disabled)) + gray checkmark (var(--color-surface-40)).
> **Not** a dark gray background + white checkmark — that's the hover-selected style.

### Check icons in tables

Tables use the same `<input type="checkbox">` + CSS with the `.check-icon` class:

```html
<!-- Active permission -->
<td class="check-icon"><input type="checkbox" checked disabled /></td>

<!-- No permission -->
<td class="check-icon"><input type="checkbox" disabled /></td>
```

---

## Checkbox – Dark Mode (ECO Design System)

**Figma:** `❖ Form Elements` → COMPONENT_SET `Checkbox/Dark` (node `22256:676`)

> Always use the dark-mode variant of Checkbox when the component sits on a dark background (`surface-100` var(--color-surface-100), `surface-80` var(--color-surface-80), or similar). **Never** mix the light-mode variant onto a dark surface.

### Variant properties

| Property | Values |
|---|---|
| `Color Mode` | `Dark` |
| `Version` | `Desktop`, `Mobile` |
| `State` | `Enabled`, `Hover`, `Focus`, `Selected`, `Selected Hover`, `Selected Focus`, `indeterminate`, `Disabled`, `Disabled Selected`, `Inline Menu`, `Inline Menu Hover`, `Inline Menu Selected`, `Inline Menu Selected Hover`, `Inline Menu indeterminate`, `Inline Menu indeterminate Hover` |
| `Size` | `Large`, `Small` |

> `Selected Hover` only exists for `Version=Desktop Large` and `Version=Mobile Large`.

### Semantic tokens (dark mode)

Every fill and stroke is bound to variables from the ECO Design System collection `Semantic: Design Tokens`.

| Element | State | Token | Hex |
|---|---|---|---|
| Checkbox box fill | Enabled / Hover / Focus / Disabled | `color/surface-opacity-white-0` | transparent |
| Checkbox box fill | Selected / Selected Focus / indeterminate | `color/border-action-2` | `var(--color-border-action-2)` |
| Checkbox box fill | Selected Hover | `color/surface-40` | `var(--color-surface-40)` |
| Checkbox box fill | Disabled Selected | `color/surface-60` | `var(--color-surface-60)` |
| Checkbox box stroke | Enabled / Hover / Focus / Selected | `color/border-action-2` | `var(--color-border-action-2)` |
| Checkbox box stroke | Disabled / Disabled Selected | `color/surface-60` | `var(--color-surface-60)` |
| Checkmark | Selected / Selected Focus | `color/surface-100` | `var(--color-border-selected)` |
| Checkmark | Selected Hover | `color/border-action-2` | `var(--color-border-action-2)` |
| Indeterminate dash | indeterminate | `color/surface-100` | `var(--color-surface-100)` |
| Arrow icon (Inline Menu) | All states | `color/icon-inverted` | `var(--color-icon-inverted)` |
| Label text | Enabled → indeterminate / Inline Menu | `color/text-primary-inverted` | `var(--color-text-primary-inverted)` |
| Label text | Disabled / Disabled Selected | `color/text-disabled` | `var(--color-text-disabled)` |
| Message text | Enabled → indeterminate / Inline Menu | `color/text-tertiary-inverted` | `var(--color-text-tertiary-inverted)` |
| Message text | Disabled / Disabled Selected | `color/text-disabled` | `var(--color-text-disabled)` |

### CSS template

```css
/* Wrapper */
.form-checkbox-item--dark { display: flex; align-items: center; gap: 8px; cursor: pointer; }

/* Checkbox box */
.form-checkbox-item--dark input[type="checkbox"] {
  appearance: none;
  width: 16px;
  height: 16px;
  border: 1.5px solid var(--color-border-action-2);      /* border-action-2 */
  background: transparent;          /* surface-opacity-white-0 */
  cursor: pointer;
  flex-shrink: 0;
  margin: 4px;
}

/* Hover — thicker border */
.form-checkbox-item--dark input[type="checkbox"]:hover { border-width: 2px; }

/* Selected */
.form-checkbox-item--dark input[type="checkbox"]:checked {
  background-color: var(--color-surface-action-2);        /* border-action-2 */
  border-color: var(--color-text-primary-inverted);
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 16 16' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M3 8l3.5 3.5L13 5' stroke='%23000000' stroke-width='1.5' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E");
}

/* Selected Hover */
.form-checkbox-item--dark input[type="checkbox"]:checked:hover {
  background-color: var(--color-surface-40);        /* surface-40 */
  border-color: var(--color-text-disabled);
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 16 16' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M3 8l3.5 3.5L13 5' stroke='%23ffffff' stroke-width='1.5' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E");
}

/* Focus */
.form-checkbox-item--dark input[type="checkbox"]:focus-visible {
  outline: 2px solid var(--color-border-focus);       /* border-focus */
  outline-offset: 2px;
}

/* Disabled */
.form-checkbox-item--dark input[type="checkbox"]:disabled {
  border-color: var(--color-surface-60);            /* surface-60 */
  cursor: not-allowed;
}

/* Disabled Selected */
.form-checkbox-item--dark input[type="checkbox"]:disabled:checked {
  background-color: var(--color-surface-60);        /* surface-60 */
  border-color: var(--color-surface-60);
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 16 16' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M3 8l3.5 3.5L13 5' stroke='%23939595' stroke-width='1.5' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E");
}

/* Label text */
.form-checkbox-item--dark span {
  color: var(--color-text-primary-inverted);                   /* text-primary-inverted */
  font-family: 'Breuer Condensed', sans-serif;
}

/* Disabled label */
.form-checkbox-item--dark:has(input:disabled) { cursor: not-allowed; }
.form-checkbox-item--dark:has(input:disabled) span { color: var(--color-text-disabled); /* text-disabled */ }
```

### HTML example

```html
<!-- Enabled -->
<label class="form-checkbox-item form-checkbox-item--dark">
  <input type="checkbox" />
  <span>Label</span>
</label>

<!-- Selected -->
<label class="form-checkbox-item form-checkbox-item--dark">
  <input type="checkbox" checked />
  <span>Label</span>
</label>

<!-- Disabled Selected -->
<label class="form-checkbox-item form-checkbox-item--dark">
  <input type="checkbox" checked disabled />
  <span>Label</span>
</label>
```

### Rules

1. **IMPORTANT:** Always use `.form-checkbox-item--dark` on a dark background – never `.form-checkbox-item` (light mode).
2. **IMPORTANT:** Never hardcode hex colors – always use CSS variables when the project has a token system: `var(--color-border-action-2)`, `var(--color-surface-60)`, etc.
3. The checkmark icon is always implemented as an inline SVG `background-image` or `<input type="checkbox">` + CSS – never as an `<img>` or external SVG file.
4. The focus ring (`var(--color-border-focus)`, `outline-offset: 2px`) must **always** show on keyboard navigation (`:focus-visible`).
5. `Disabled Selected` state: gray box (`var(--color-surface-60)`) + gray checkmark (`var(--color-surface-40)`) – **not** a dark background with a white checkmark (that's the hover-selected style).

---
