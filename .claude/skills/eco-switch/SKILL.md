---
name: eco-switch
description: Use when building or reviewing a switch (toggle switch) — an immediate on/off control for a single binary setting. Sizes (Large/Small/X-Small), light and dark mode, all states (enabled/hover/focus/disabled × off/on), label. Not for choosing between options (use eco-radio) or multi-select/form submission (use eco-checkbox).
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Switch (ECO Design System)

**Figma:** `❖ Form Elements` → Toggle Switch (node `278:9676`, Size × State × Switch × Breakpoint × Mode) · usage info frame `12137:385340`.

Always implement a switch with a native `<input type="checkbox" role="switch">` + CSS — never `<img>`, SVG files, or `<div>` imitations. Native input gives keyboard (Space), label click and form state for free.

### When to use
- Control a feature or option that can be turned **on or off**. If a physical switch would work for the action, a switch is probably the right component.
- Visualise the selection of **binary states**, for example "On" / "Off".
- A switch acts **immediately** (no Save button needed). If the choice is only applied on form submit, use `eco-checkbox`.
- Not for picking one of several options (→ `eco-radio`), not for switching between two views/filters (→ `eco-pill-segment-control`), not for multi-select lists (→ `eco-checkbox`).

### Size model
Switch size does not scale with the breakpoint; only the label type style does (see below).

| Size | Track | Thumb | Thumb inset | Thumb travel | Track radius | Gap to label |
|---|---|---|---|---|---|---|
| **Large** | 48×24px | 20px | 2px | 24px | 999px (pill) | `--dimension-spacing-space-8` |
| **Small** | 48×24px | 20px | 2px | 24px | 999px | `--dimension-spacing-space-8` |
| **X-Small** | 32×16px | 12px | 2px | 16px | 999px | `--dimension-spacing-space-8` |

Focus ring: `2px` + `2px` offset around the track (same ring model as `eco-checkbox`/`eco-radio`).

### Label typography (`eco-typography`)
| Size | Label | Breakpoint behaviour |
|---|---|---|
| **Large** | `body-md` — 16px/22px, 0.32px | 17px/24px from `md:` (769px) |
| **Small** | `body-sm` — 14px/20px, 0.36px | Same on all breakpoints |
| **X-Small** | `body-sm` — 14px/20px, 0.36px | Same on all breakpoints |

Font: `Breuer Condensed`, `font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1`. `sm` (640–768px) uses the mobile value.

### States

Light mode:

| State | Off track | On track | Thumb | Other |
|---|---|---|---|---|
| **Enabled** | `--color-surface-20` | `--color-surface-success-default` | `--color-surface-raised-primary` + `--shadow-elevation-input-control-switch` | `cursor: pointer` |
| **Hover** | `--color-surface-15` | `#71b790` (no token, see flag) | as Enabled | |
| **Focus** (`:focus-visible`) | as Enabled | as Enabled | as Enabled | outline `2px solid var(--color-border-focus)`, offset 2px |
| **Disabled** | `--color-surface-disabled` | `rgba(36,134,22,.5)` (see flag) | `--color-surface-raised-primary`, no shadow | `cursor: not-allowed`, label `--color-text-disabled` |

Dark mode (`.form-switch-item--dark`, label `--color-text-primary-inverted`; On track and focus ring are identical to light):

| State | Off track | Thumb |
|---|---|---|
| **Enabled** | `--color-surface-60` | `--color-surface-raised-primary` + shadow |
| **Hover** | `--color-surface-50` | as Enabled |
| **Focus** | as Enabled | as Enabled |
| **Disabled** | `--color-surface-80` | `--color-surface-40`, no shadow; label `--color-text-disabled`; On track `rgba(36,134,22,.5)` |

### HTML structure
```html
<label class="form-switch-item">
  <input type="checkbox" role="switch" checked />
  <span>Email notifications</span>
</label>

<label class="form-switch-item form-switch-item--sm">
  <input type="checkbox" role="switch" />
  <span>Small</span>
</label>

<label class="form-switch-item form-switch-item--xs">
  <input type="checkbox" role="switch" disabled />
  <span>X-Small, disabled</span>
</label>

<!-- dark surface -->
<label class="form-switch-item form-switch-item--dark">
  <input type="checkbox" role="switch" />
  <span>Dark mode</span>
</label>
```
The label is always visible text; the **whole label is clickable** (wrap input + text in `<label>`). A switch without visible label needs `aria-label` on the input.

### CSS

Link the shared stylesheet. Never copy its rules into a page, and never write a parallel version:

```html
<link rel="stylesheet" href="/components/css/switch.css">
```

`components/css/switch.css` is the single source for this component. The docs page `eco-design-system/components/switch.html` links the same file and prints it in its Code section. Mobile-first, desktop from 769px, `var(--…)` only. The `[data-state="…"]` selectors in it are only for the docs pages' forced-state demos and do nothing elsewhere. To change the component, edit that file.

### Rules
1. **Never hardcode hex/px colours** — use `var(--color-…)` from `tokens.json` (`eco-tokens`, rule 6 in CLAUDE.md). The only literals are the two flagged below.
2. Native `<input type="checkbox" role="switch">` inside a `<label>`; never a `<div>`/`<button>` imitation. Test: label click toggles, Space toggles, Tab reaches it, disabled is not focusable.
3. A switch applies its change **immediately**; do not pair it with a Save/Submit button for the same setting.
4. Label describes the setting (state is shown by the switch), never "On"/"Off" text changing with state.
5. Focus ring must show on keyboard navigation (`:focus-visible`), for both off and on.
6. Dark variant only on dark surfaces — never combine `--dark` with a light page background.
7. Test all states at `xs` (~375px), `sm` (~700px) and `md`/`lg` (≥1024px); label size changes at 769px (`md`), never at `sm` (CLAUDE.md quality control 1 + 5).

### Flags for design
- **Hover On track `#71b790`** and **Disabled On track `rgba(36,134,22,0.5)`** are baked into the Figma SVGs (not variable-bound) and have no token. Values are sampled from the Figma render; hover is not a clean tint of `--color-surface-success-default`. Ask design for tokens.
- **Label size inconsistencies in Figma:** desktop Large uses 17px/24px (matches `body-md` desktop override); some desktop Small/X-Small variants default to 16px/22px in code while their widths imply 14px. This skill uses `body-sm` for Small and X-Small at all breakpoints. Confirm with design.
- **Motion:** Figma specifies no thumb animation. Transition uses `--duration-fast-3` + `--ease-standard` (hover/form-element default in `eco-motion`). Confirm.
- Dark On hover and focus ring colours were not variable-bound in dark frames; assumed identical to light.
