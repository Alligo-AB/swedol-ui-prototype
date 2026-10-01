---
name: eco-radio
description: Use when building or reviewing radio buttons — a list of two or more mutually exclusive options where exactly one can be chosen. Sizes (Large/Small), all states (enabled/hover/focus/selected/selected hover/selected focus/disabled/disabled selected), label + optional hint message.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Radio button (ECO Design System)

**Figma:** `❖ Form Elements` → Radio Button (node `1548:70504`, all states × sizes × breakpoints) · usage info frame `12137:385322`.

Always implement radios with a native `<input type="radio">` + CSS — never `<img>`, SVG files, or `<div>` imitations. Native radios give grouping, arrow-key navigation and form submission for free.

### When to use
- Presenting **two or more mutually exclusive options** where the user must pick exactly one.
- **Preselect a default option** in every group. It removes confusion and gives users a clear suggestion.
- Prefer **vertical** layouts — easier to scan. Horizontal layouts obscure the link between radio and label.
- The **whole label is clickable** (wrap input + text in `<label>`), not just the circle.
- Not for toggling between two views/filters in the same surface (→ `eco-segment-control`), not for multi-select (→ `eco-checkbox`).

### Size model
Only **Large** and **Small** exist. Sizes do **not** change per breakpoint; only the label type style does (see below).

| Size | Total area | Visible circle | Margin | Dot | Focus ring |
|---|---|---|---|---|---|
| **Large** | 24×24px | 16px | `4px` (`--dimension-spacing-space-4`) | 6px | 2px, offset 2px |
| **Small** | 20×20px | 14px | `3px` | 6px | 2px, offset 2px |

Focus ring (2px) + offset (2px) = 4px → fills the Large margin exactly, same model as `eco-checkbox`. Gap between circle and label: `var(--dimension-spacing-space-8, 8px)`. Gap between label row and hint message: `var(--dimension-spacing-space-4, 4px)`.

### Label & message typography (`eco-typography`)
| Size | Label | Breakpoint behaviour |
|---|---|---|
| **Large** | `body-md` — 16px/22px, 0.32px | Mobile-first value; follow `eco-typography` if it changes at `md:` (769px) |
| **Small** | `body-sm` — 14px/20px, 0.28px | Same on all breakpoints |
| Hint message (both) | `body-sm` — 14px/20px, `var(--color-text-tertiary)` | — |

Font: `Breuer Condensed`, `font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1`.

> **Flag for design (do not silently change):** the Figma radio frames show Large desktop label as 17px/24px and body-sm letter-spacing 0.36px, while `tokens.json`/`eco-typography` have `body-md` 16px/22px and `body-sm` 0.28px (no desktop override). This skill follows `tokens.json`. Confirm with design whether the desktop radio label really differs.

### States

| State | Fill | Border (1px, `var(--border-brd-1)` width) | Dot | Other |
|---|---|---|---|---|
| **Enabled** | `--color-surface-raised-primary` | `--color-border-input-control-default` | — | |
| **Hover** | `--color-surface-opacity-black-05` | `--color-border-hover` | — | `cursor: pointer` |
| **Focus** (`:focus-visible`) | as Enabled | as Enabled | — | outline `2px solid var(--color-border-focus)`, offset 2px |
| **Selected** | `--color-surface-raised-primary` | `--color-border-selected` | `--color-surface-100` | |
| **Selected Hover** | `--color-surface-opacity-black-05` | `--color-border-selected-hover` | `--color-surface-100` | |
| **Selected Focus** | as Selected | as Selected | as Selected | same focus ring |
| **Disabled** | `--color-surface-disabled` | `--color-border-disabled` | — | `cursor: not-allowed`, label `--color-text-disabled` |
| **Disabled Selected** | `--color-surface-disabled` | none visible (border = fill colour, keeps 16px size) | `--color-surface-50` | `cursor: not-allowed`, label `--color-text-disabled` |

Focus color is `var(--color-border-focus)` (`#455efb`) — this matches the Figma radio focus ring, unlike checkbox (see flag in `eco-checkbox`).

### HTML structure
```html
<fieldset class="form-radio-group">
  <legend>Delivery method</legend>

  <label class="form-radio-item">
    <input type="radio" name="delivery" value="standard" checked />
    <span>Standard</span>
  </label>

  <!-- with hint message -->
  <div class="form-radio-field">
    <label class="form-radio-item">
      <input type="radio" name="delivery" value="express" />
      <span>Express</span>
    </label>
    <p class="form-radio-message">Delivered next business day</p>
  </div>

  <label class="form-radio-item form-radio-item--sm">
    <input type="radio" name="delivery" value="pickup" disabled />
    <span>Pick up</span>
  </label>
</fieldset>
```
Every radio in a group shares the same `name`; the group gets a `<fieldset>` + `<legend>` (style the legend with the surrounding form's label style, e.g. `eco-input` `label-md`).

### CSS template
```css
.form-radio-group { border: 0; margin: 0; padding: 0; display: flex; flex-direction: column; } /* vertical by default */

.form-radio-item {
  display: flex; align-items: center; gap: var(--dimension-spacing-space-8, 8px); cursor: pointer;
  font-family: 'Breuer Condensed', sans-serif; font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
  font-size: 16px; line-height: 22px; letter-spacing: 0.32px; /* body-md */
  color: var(--color-text-primary);
}
.form-radio-item--sm { font-size: 14px; line-height: 20px; letter-spacing: 0.28px; } /* body-sm */

.form-radio-item input[type="radio"] {
  appearance: none; flex-shrink: 0; cursor: pointer;
  width: 16px; height: 16px; margin: var(--dimension-spacing-space-4, 4px);   /* total area 24×24 */
  border: var(--border-brd-1-width, 1px) solid var(--color-border-input-control-default);
  border-radius: 50%;
  background-color: var(--color-surface-raised-primary);
  background-repeat: no-repeat; background-position: center;
}
.form-radio-item--sm input[type="radio"] { width: 14px; height: 14px; margin: 3px; }  /* total area 20×20 */

.form-radio-item input[type="radio"]:hover { background-color: var(--color-surface-opacity-black-05); border-color: var(--color-border-hover); }
.form-radio-item input[type="radio"]:focus-visible { outline: 2px solid var(--color-border-focus); outline-offset: 2px; }

/* Selected — dot is a 6px radial-gradient, no SVG/img */
.form-radio-item input[type="radio"]:checked {
  border-color: var(--color-border-selected);
  background-image: radial-gradient(circle, var(--color-surface-100) 0 3px, transparent 3.5px);
}
.form-radio-item input[type="radio"]:checked:hover { border-color: var(--color-border-selected-hover); }

/* Disabled */
.form-radio-item input[type="radio"]:disabled { background-color: var(--color-surface-disabled); border-color: var(--color-border-disabled); cursor: not-allowed; }
.form-radio-item input[type="radio"]:disabled:checked {
  border-color: var(--color-surface-disabled);
  background-image: radial-gradient(circle, var(--color-surface-50) 0 3px, transparent 3.5px);
}
.form-radio-item:has(input:disabled) { cursor: not-allowed; color: var(--color-text-disabled); }

/* Hint message (aligned to the left edge of the radio) */
.form-radio-field { display: flex; flex-direction: column; gap: var(--dimension-spacing-space-4, 4px); }
.form-radio-message { margin: 0; font-size: 14px; line-height: 20px; letter-spacing: 0.28px; color: var(--color-text-tertiary); }
.form-radio-field:has(input:disabled) .form-radio-message { color: var(--color-text-disabled); }
```
> `--border-brd-1-width` does not exist as a token (`--border-brd-1` is the full `width style color` shorthand, black). The `1px` fallback is intentional; only the colour changes per state. If a width-only token is added to `alligo-design-tokens`, switch to it.

### Rules
1. **Never hardcode hex/px colours** — every colour above is a `var(--color-…)` from `tokens.json` (`eco-tokens`, rule 6 in CLAUDE.md).
2. Always a `name` per group, always one option **preselected** unless the user must consciously choose (then say why in a comment).
3. Vertical stacking with `space-8`–`space-12` between items unless the design says otherwise; never horizontal for more than two short options.
4. Label click must select the radio (`<label>` wrapper). Test it.
5. Focus ring must show on keyboard navigation (`:focus-visible`), including for the selected radio.
6. Test all 8 states at `xs` (~375px), `sm` (~700px) and `md`/`lg` (≥1024px) before delivery (CLAUDE.md quality control 1 + 5).
