---
name: eco-list-item
description: Use when building or reviewing the content of one row in a list surface (List Item) — optional leading element (icon, check box, radio, color swatch, swatch frame, image), label (regular/bold) and optional trailing element (icon, secondary or tertiary text, check box, radio, switch), plus optional overline and supporting text. Used inside Menu, Overflow menu, List Picker, Drawer link and Filter sections. Not for the row container (height, divider, hover, focus: use eco-menu) and not for a standalone checkbox/radio (use eco-checkbox / eco-radio).
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, breakpoints, and the quality checklist that always applies on top of this spec.

## List Item (ECO Design System)

Figma (file `42MgqJjV9vfplwQnrUB62r`): info `14965:36405`, List Item Content (all variants) `3140:104687`, Base/List Item `3137:104383`.
Docs page: `eco-design-system/components/list-item.html` (it links `components/css/list-item.css`, the single CSS source).

### When to use / not to use

- A List Item is the **content** of a row: `[leading] [label] … [trailing]`. It is used inside **Menu**, **Overflow menu**, **List Picker**, **Drawer link** and **Filter sections in drawer content**. Concrete usage is documented on those components.
- The **container owns** row height, padding, divider, hover, focus and the selected fill (see `eco-menu`). The List Item never draws them.
- Not for: a standalone form control (`eco-checkbox`, `eco-radio`), page navigation links (`links-guide`), tabular data (`eco-table`), or rich cards.

### Axes

| Axis | Values |
|---|---|
| Size | **Large** (default), **Small** |
| Breakpoint | Desktop (769px+), Mobile/Tablet (below 769px). Large changes, Small does not |
| Leading | None, **Icon**, **Check box**, **Radio button**, **Color swatch**, **Color swatch + frame**, **Image** |
| Label | Regular, **Bold**, None |
| Trailing | None, **Icon**, **Text secondary**, **Text tertiary**, **Check box**, **Radio button**, **Switch** |
| Overline | None, shown (above the label) |
| Supporting text | None, 1 line, 2 lines (below the label, clipped after 2) |

Mapping to the Figma variant names: `Leading=Regular Label` = no leading + regular label; `Bold Label` = bold label + trailing text secondary; `Check Box` / `Radio Button` / `Icon` = that leading + label (Icon in Figma is icon only); `Color Swatch` = swatch without label; `Color Swatch + Label` = frame + label; `Image Swatch` = image without label. We keep Leading, Label and Trailing as three free axes so every Figma combination can be built.

### Size model

| Breakpoint · size | Text | Trailing icon | Check box / radio area |
|---|---|---|---|
| Desktop · Large | `body-md` 17/24, 0.32px | 24px | 24px (16px box + 4px margin) |
| Mobile · Large | `body-md` 16/22, 0.32px | 20px | 24px |
| Small (both) | `body-sm` 14/20, 0.36px | 20px | 20px (14px box + 3px margin) |

- Gap between leading, label and trailing: `8px` (`--dimension-spacing-space-8`). Leading and label stay together (`.list-item__fill`), the trailing element sits at the far end.
- Leading sizes: icon **20px**, check/radio as above, swatch **16px**, swatch frame **24px** (1px frame, 16px swatch inside), image **48px** (`object-fit: cover`).
- Row height comes from the tallest part (image 48px) plus the container padding.

### Text parts (overline, label, supporting text)

Wrap the text parts in `.list-item__text` (a column). Total one to three lines.

| Part | Style | Color |
|---|---|---|
| Overline | `alt-label-sm`, uppercase, 12/12 mobile, 14/14 desktop, weight 500 (as `eco-typography` documents) | `text-tertiary` |
| Label | `body-md` / `body-sm` | `text-primary` |
| Supporting text | `body-sm` 14/20 on both sizes, `-webkit-line-clamp: 2` | `text-tertiary` |

Leading and trailing elements stay vertically centered. The **container row needs vertical padding** for rows taller than one line (`.menu__item` has none today).

### Trailing controls

Check box and radio: same parts as leading (`.list-item__check`, `.list-item__radio`), placed after `.list-item__fill`. **Switch** (`.list-item__switch`): Large 48×24px track with 20px thumb, Small 32×16px with 12px thumb (X-Small of `eco-switch`); off `surface-20`, on `surface-success-default`, thumb `surface-raised-primary` + `shadow-elevation-input-control-switch`; disabled track `surface-disabled`. All three are **presentational** (`aria-hidden`): state comes from `aria-selected` on the row or item. No hover, focus, motion or dark mode on the trailing switch: the container and the row's own role (`option`, `menuitemcheckbox`, `switch`) handle that.

### Typography

`body-md` (Large) and `body-sm` (Small), see `eco-typography`. `font-family: 'Breuer Condensed'`, `font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1`, weight 400; **Bold label** weight 700. Trailing text uses the same style as the label.

### States

The item has no hover or focus of its own. It reflects two things, set on the row or the item with ARIA attributes:

| State | Check box | Radio | Swatch frame | Text / icons |
|---|---|---|---|---|
| **Enabled** | 1px `border-input-control-default`, fill `surface-raised-primary` | same, circle | 1px `border-secondary` | label `text-primary`, trailing text `text-secondary` / `text-tertiary`, icons `icon-primary` |
| **Selected** (`aria-selected="true"`) | fill and border `surface-100`, white check | border `border-selected`, 6px dot `surface-100` | 2px `border-selected` (1px border + 1px inset shadow, size unchanged) | unchanged |
| **Disabled** (`aria-disabled="true"`) | fill `surface-disabled`, border `border-disabled` | same | unchanged | label, trailing text and icons `text-disabled` |

Hover and focus: drawn by the container row (`eco-menu`). Check box, radio and switch parts are **presentational** (`aria-hidden`). Who carries the state:

- **Inside a container row** (`role="option"`): `aria-selected` / `aria-disabled` on the row. The container handles click and keys.
- **Standalone item with a control**: the `.list-item` itself is `role="checkbox"`, `"radio"` or `"switch"` (switch wins over check, check over radio) with `tabindex="0"` and `aria-checked`. Component CSS gives it `cursor: pointer` and a 2px `border-focus` ring (offset 2px); nothing else.

Behavior for standalone items (script on the docs page, copy it with the markup): click, Space or Enter toggles `aria-checked`; a radio only selects, and clears the others inside its `role="radiogroup"`; in a group there is one tab stop (the checked radio, others `tabindex="-1"`) and Arrow keys move and select (wraps). `aria-disabled="true"` ignores clicks and keys, with `tabindex="-1"`. CSS reads both `aria-selected="true"` and `aria-checked="true"`.

### HTML structure

```html
<div class="list-item" aria-selected="false">
  <span class="list-item__fill">
    <span class="list-item__check" aria-hidden="true"></span>
    <span class="list-item__label">0 – 999 kr</span>
  </span>
  <span class="list-item__trail-text list-item__trail-text--tertiary">24</span>
</div>

<!-- Icon + label + trailing icon -->
<div class="list-item">
  <span class="list-item__fill">
    <span class="list-item__icon" aria-hidden="true">person</span>
    <span class="list-item__label">Label text</span>
  </span>
  <span class="list-item__trail-icon" aria-hidden="true">check_circle</span>
</div>

<!-- Inside a Menu row: the row sets padding, divider, hover, focus -->
<li class="menu__item" role="option" tabindex="0" aria-selected="true"><div class="list-item">…</div></li>
```

Other leading parts: `list-item__radio`, `list-item__swatch` (+ `style="--swatch: <color>"`), `list-item__swatch list-item__swatch--tile`, `<img class="list-item__image" alt="">`. Label bold: `list-item__label--bold`. Small: `list-item list-item--sm`. Swatch colors are product data, not design tokens.

### CSS

Link the shared stylesheet. Never copy its rules into a page, and never write a parallel version:

```html
<link rel="stylesheet" href="/components/css/list-item.css">
```

`components/css/list-item.css` is the single source for this component. The docs page `eco-design-system/components/list-item.html` links the same file and prints it in its Code section. Mobile-first, desktop from 769px, `var(--…)` only. The `[data-state="…"]` selectors in it are only for the docs pages' forced-state demos and do nothing elsewhere. To change the component, edit that file.

### Rules

1. **Never hardcode design tokens** — every color, spacing and border is a `var(--…)` (see `eco-tokens`). The 8px gap uses `--dimension-spacing-space-8`; the 20/16/48px element sizes are Figma sizes without a token.
2. **Mobile-first, switch at `md` (769px)**, never `sm`. Verify with `getComputedStyle` at ~375px, ~700px and ~1024px+ (Large label 16/22, 16/22, 17/24; trailing icon 20/20/24).
3. **The container owns the row.** Never add height, divider or hover styles to `.list-item` (focus ring and pointer only for a standalone item with a `role`); never put a real `<input>` inside an option row.
4. **State by attribute:** `aria-selected` (row in a container) or `aria-checked` (standalone `role` item), plus `aria-disabled`, on the `.list-item` or an ancestor. The visual (check, dot, frame, switch) must match the attribute. Keep `aria-checked` in sync when toggling.
5. **One leading type per list.** Do not mix check boxes with icons in the same list.
6. **Keep the label on one line**; use trailing text only for a short number or value.
7. When `eco-menu` rows are built from this component, keep the menu's 48/40/32px row heights and dividers.

### Flags (for design)

- **Weight:** Figma exports `body-md` / `body-sm` as 500; the repo (and `eco-menu`, `eco-select`) use 400. Followed the repo.
- **Trailing text is not bound to a token in Figma** (hard-coded 16/22 on both breakpoints, even in the desktop variant). We use `body-md` / `body-sm` like the label, so Desktop Large trailing text is 17/24, not 16/22. Small trailing text (14/20) is derived.
- **Icon colors** are not readable in the Figma export. We use `icon-primary` for leading and trailing icons (black, same as `text-action-primary`).
- **Leading icon is 20px** on Large desktop too (Figma), while the trailing check icon is 24px there.
- **Derived, not in Figma:** selected and disabled states, label with icon/radio/swatch (Figma icon-only and swatch-only variants have no label), Small trailing text. Check box / radio selected looks copy `eco-checkbox` / `eco-radio`.
- **Anatomy** is "TBA" in the Figma info frame; the "Anatomy & specs" section on the docs page is ours.
- **Added from Material Design 3, not in Figma (confirm with design):** overline, supporting text (max 2 lines, so up to 3 lines with overline), and check box / radio / switch as trailing control. Overline uses `alt-label-sm` (tokens say 12/12 mobile, weight 600; we followed the documented 500, as `eco-typography`). Small supporting text and the 32×16px Small switch are derived. Leading/trailing are centered, not top-aligned as M3 does for three-line items.
- **Switch literals:** the trailing switch reuses `eco-switch`; its flagged hover/disabled-on colors are not used here (no hover, no disabled-on).
- **Not added, ask before adding:** avatar or video as leading, a standalone clickable/selectable row (the interactive row is the container's job today).
