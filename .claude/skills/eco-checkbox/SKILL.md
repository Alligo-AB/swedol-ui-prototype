---
name: eco-checkbox
description: Use when building or reviewing checkboxes — light mode (standard and the detailed table icon variant) and dark mode, including all states (enabled/hover/focus/selected/indeterminate/disabled), plus the tile variants used on PDP and in filtering (Color swatch, Image, Number).
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
| Enabled | `1px solid var(--color-border-input-control-default)`, fill `var(--color-surface-raised-primary)` |
| Hover | fill `var(--color-surface-raised-secondary)`, border `var(--color-border-hover)` (still 1px) |
| Focus | Enabled look + ring `var(--color-border-focus)`, 2px, offset 2px (matches Figma) |
| Selected | Fill and border `var(--color-surface-100)`, white checkmark (SVG) |
| Selected Hover | Fill and border `var(--color-surface-50)`, white checkmark |
| Selected Focus | Selected look + focus ring |
| Indeterminate | Same as Selected, white dash (SVG). Hover = Selected Hover. Focus = Selected Focus. |
| Disabled | Border `var(--color-border-disabled)`, fill `var(--color-surface-disabled)`, `cursor: not-allowed` |
| Disabled Selected | Fill and border `var(--color-surface-disabled)`, grey checkmark `#939595` (= `text-disabled`) |
| Disabled Indeterminate | Fill and border `var(--color-surface-disabled)`, grey dash `#939595` |
| Disabled label | Text `var(--color-text-disabled)` via `:has(input:disabled) span` |

> Updated from Figma (2026-10-03): the enabled border is now the grey `border-input-control-default` at **1px** and hover no longer thickens the border (it changes fill and border color). Dark mode is unchanged (1px white border, **2px on hover**). Disabled Indeterminate and Inline Menu Disabled / Disabled Selected / Disabled Indeterminate were added later (all sizes and modes). Dark disabled mixed: fill and border `surface-60`, dash `surface-40`.

### Sizes and Inline Menu (Figma `Checkbox`, node `1548:53635`, file `42MgqJjV9vfplwQnrUB62r`)

Figma properties: `Mode` (Light/Dark), `Size` (Large/Small), `Breakpoint` (XLarge-Large-Medium / Small-XSmall), `State`. The Breakpoint axis (XLarge-Large-Medium = Desktop, 769px+; Small-XSmall = Mobile/Tablet, below 769px) leaves the box, area, gap and Small label unchanged; only the Large label differs: Mobile 16/22, Desktop 17/24 (`body-md`).

| Size | Area | Box | Margin | Gap | Label |
|---|---|---|---|---|---|
| Large (default) | 24×24px | 16×16px | 4px | 8px | `body-md`: 16/22, from `md:` 17/24, 0.32px |
| Small (`.form-checkbox-item--sm`) | 20×20px | 14×14px | 3px | 4px | `body-sm`: 14/20, 0.36px |

- Small focus ring: `outline-offset: 1px` (1px + 2px = 3px margin). Checkmark `background-size: 12px`.
- Selected Hover exists for both sizes and looks the same (updated in Figma).
- **Inline Menu** (all sizes, light and dark): box + 24×24px dropdown arrow (`.cb-arrow`, fill `icon-primary`, dark `icon-inverted`), no label (add `aria-label`), gap 8px Large / 4px Small. States: Enabled, Hover, Focus, Selected, Selected Hover, Selected Focus, Mixed, Mixed Hover, Mixed Focus, Disabled, Disabled Selected, Disabled Mixed. The arrow is `text-disabled` (`#939595`) when disabled, light and dark (`:has(input:disabled) .cb-arrow`).
- Every state is defined in Figma for both sizes, both modes and the inline menu.
- Live reference with all of this: `eco-design-system/components/checkbox.html` (it links `components/css/checkbox.css`, the single CSS source).

```html
<label class="form-checkbox-item form-checkbox-item--sm"><input type="checkbox" /><span>Label</span></label>
<label class="form-checkbox-item"><input type="checkbox" aria-label="Select all" />
  <svg class="cb-arrow" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 10l5 5 5-5z"/></svg></label>
```

### Tiles: Color swatch, Image, Number (PDP and filtering)

Figma: Checkbox Color Swatch `4650:209393`, Checkbox Image / Number `14460:597851`. Used first and foremost on product pages (PDP) and in filtering, where the choice is a color or a picture instead of a text label. Native `<input type="checkbox">` visually hidden over a `.form-checkbox-tile__box`; **no visible label, so `aria-label` is required**; several can be chosen. Live reference: the **Tiles** section of `eco-design-system/components/checkbox.html` (its `#cb-css` block is the canonical CSS).

| Tile | Desktop | Mobile | Inside | Enabled border |
|---|---|---|---|---|
| Color swatch (`.form-checkbox-tile`) | 24×24px | 24×24px | 16px swatch (`--swatch` = product color), 2px padding | 1px `border-secondary` |
| Image (`--image`) | 48×48px | 40×40px | image, `object-fit: contain`, 6px from the edge | 1px `border-primary` |
| Number (`--number`, a `<button>`, "+10") | 48×48px | 40×40px | `label-md` 16/16, 0.48px, Bold, uppercase, `text-primary` | 1px `border-secondary` |

States (all tiles, fill `surface-raised-primary`): **Hover** 1px `border-hover`; **Selected** 2px `border-selected`; **Selected Hover** 2px `border-selected-hover` (the 2px frame is a 1px border plus `box-shadow: inset 0 0 0 1px`, so the size never changes); **Focus** ring `border-focus` 2px, offset 2px. Number only has Enabled and Hover. Disabled is not defined in Figma for tiles.

> **Filter list row:** on filter pages a color tile sits in a row with its name (`body-md`, `text-primary`) and the number of products (`body-md`, `text-tertiary`, right-aligned); the whole row is the click target (`.form-checkbox-tile--row` on the same label, 48px min height, 8px between tile and name). A group has a header (title + chevron), the list, a "Show more" action and a 1px `border-primary` divider before the next group (for example "Size").

> **Product color library:** Figma node `13395:185062` (Product color filter swatches) has 26 colors: Yellow, White, Beige, Black, Blue, Bronze, Brown, Gold, Green, Grey, Oak, Orange, Pink, Purple, Red, Silver, Teak, Pattern, Dark, Multi color, Black mirror, Clear, Matte, Mirror lens, Semi shiny, Transparent. Most are a glossy angular gradient (`conic-gradient`) per color, a few are linear gradients, Pattern is a checker. The live values are the `COLORS` list in the page script (product data, not design tokens). A color row is the name (`alt-label-lg` style, Medium, uppercase, `text-tertiary`) + a 16px swatch + the hex value from product data, with a 1px `border-primary` divider below.

> **One at a time on a PDP:** on a product page only one tile can be chosen (for example the image variants of one product). Then use `<input type="radio" name="…">` inside the same `.form-checkbox-tile` markup (the CSS works for both). Use `type="checkbox"` when several can be chosen, as in filtering. Show the chosen option's name next to the group so it is not conveyed by the picture alone.

> Flag: in Figma the mobile Color Swatch has a 20×18px swatch box in the selected states (16px in Enabled); the page uses 16px for every state and breakpoint. The tile colors in examples are product data, not design tokens.

```html
<label class="form-checkbox-tile">
  <input type="checkbox" aria-label="Blue" />
  <span class="form-checkbox-tile__box"><span class="form-checkbox-tile__swatch" style="--swatch: #0066ff"></span></span>
</label>
<label class="form-checkbox-tile form-checkbox-tile--image">
  <input type="checkbox" aria-label="Yellow / black" />
  <span class="form-checkbox-tile__box"><img src="/images/product-skaljacka-gul-svart.webp" alt="" /></span>
</label>
<button type="button" class="form-checkbox-tile form-checkbox-tile--number" aria-label="Show 10 more colors">
  <span class="form-checkbox-tile__box">+10</span>
</button>
```

### HTML structure
```html
<label class="form-checkbox-item">
  <input type="checkbox" />
  <span>Label</span>
</label>
```

### CSS

Link the shared stylesheet. Never copy its rules into a page, and never write a parallel version:

```html
<link rel="stylesheet" href="/components/css/checkbox.css">
```

`components/css/checkbox.css` is the single source for this component. The docs page `eco-design-system/components/checkbox.html` links the same file and prints it in its Code section. Mobile-first, desktop from 769px, `var(--…)` only. The `[data-state="…"]` selectors in it are only for the docs pages' forced-state demos and do nothing elsewhere. To change the component, edit that file.

---

## Checkbox Styling (ECO Design System)

Figma reference: `node-id=6408-8453`

Always implement checkboxes with `<input type="checkbox">` + CSS — never with `<img>` or SVG files.

### States

| State | Background | Border | Checkmark |
|---|---|---|---|
| **Default (unchecked)** | `--color-surface-raised-primary` | `1px solid --color-border-input-control-default` | — |
| **Checked** | `--color-surface-100` (black) | `--color-surface-100` | White (`stroke="white"`) |
| **Hover (unchecked)** | `--color-surface-raised-secondary` | `1px solid --color-border-hover` | — |
| **Hover (checked)** | `--color-surface-50` | `--color-surface-50` | White |
| **Disabled unchecked** | `--color-surface-disabled` | `--color-border-disabled` | — |
| **Disabled checked** | `--color-surface-disabled` | none (matches background) | Gray (`#939595` = `--color-text-disabled`) |
| **Indeterminate** | `--color-surface-100` (black) | `--color-surface-100` | White horizontal line |
| **Disabled indeterminate** | `--color-surface-disabled` | `--color-surface-disabled` | Gray line (`#939595`) |

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

> `Selected Hover` exists for Large and Small (Figma updated).

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
