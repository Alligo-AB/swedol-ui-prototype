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
- Not for toggling between two views/filters in the same surface (→ `eco-pill-segment-control`), not for multi-select (→ `eco-checkbox`).

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
| **Large** | `body-md` — 16px/22px, 0.32px | 17px/24px from `md:` (769px) |
| **Small** | `body-sm` — 14px/20px, 0.36px | Same on all breakpoints |
| Hint message (both) | `body-sm` — 14px/20px, `var(--color-text-tertiary)` | — |

Font: `Breuer Condensed`, `font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1`.

> Matches Figma and `tokens.json` (2026-10-02): `body-md` is 17/24 from `md:`, `body-sm` letter-spacing 0.36px.

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

### CSS

Link the shared stylesheet. Never copy its rules into a page, and never write a parallel version:

```html
<link rel="stylesheet" href="/components/css/radio.css">
```

`components/css/radio.css` is the single source for this component. The docs page `eco-design-system/components/radio.html` links the same file and prints it in its Code section. Mobile-first, desktop from 769px, `var(--…)` only. The `[data-state="…"]` selectors in it are only for the docs pages' forced-state demos and do nothing elsewhere. To change the component, edit that file.
> `--border-brd-1-width` does not exist as a token (`--border-brd-1` is the full `width style color` shorthand, black). The `1px` fallback is intentional; only the colour changes per state. If a width-only token is added to `alligo-design-tokens`, switch to it.

### Rules
1. **Never hardcode hex/px colours** — every colour above is a `var(--color-…)` from `tokens.json` (`eco-tokens`, rule 6 in CLAUDE.md).
2. Always a `name` per group, always one option **preselected** unless the user must consciously choose (then say why in a comment).
3. Vertical stacking with `space-8`–`space-12` between items unless the design says otherwise; never horizontal for more than two short options.
4. Label click must select the radio (`<label>` wrapper). Test it.
5. Focus ring must show on keyboard navigation (`:focus-visible`), including for the selected radio.
6. Test all 8 states at `xs` (~375px), `sm` (~700px) and `md`/`lg` (≥1024px) before delivery (CLAUDE.md quality control 1 + 5).
