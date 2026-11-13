---
name: eco-picker-stepper
description: Use when the user sets a small whole number by stepping it up or down — the quantity beside "Lägg i varukorgen" on a product page, in a product card, a variant table row or the cart. A minus button, a value field (with an optional unit such as "st") and a plus button. Sizes Large/Medium/Small, states enabled/hover/focus/disabled. Not for a value on a scale (use eco-range), a free number field without steps (use eco-input) or choosing between named options (see selection-guide).
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Picker Stepper (ECO Design System)

**Figma** (file `42MgqJjV9vfplwQnrUB62r`, checked 2026-11-12): sizes `1612:111715`, value states `1609:63554`, button `1601:54900` (enabled) / `1602:54423` (disabled).
**CSS:** `components/css/picker-stepper.css`. **JS:** `components/js/picker-stepper.js`. **Docs page:** none yet (ask before adding one). **First use:** `pdp.html` (Action section).

### When to use
- A quantity the user changes in small steps: number of items to buy, to order, to return.
- Beside the button that acts on the quantity (add to cart); the two are the same height.

### Not to use
- A value on a scale with a minimum and a maximum the user drags to → `eco-range`.
- A number the user types without stepping (order number, measurement) → `eco-input`.
- A choice between named options → `selection-guide`.

### Size model

Every part is a square cell of the same size. The stepper is three cells wide.

| Size | Class | Cell below 769px | Cell from 769px | Unit shown |
|---|---|---|---|---|
| Large (default) | – | 40px | 48px | always |
| Medium | `picker-stepper--md` | 32px | 40px | from 769px only |
| Small | `picker-stepper--sm` | 32px | 32px | never |

Icons are 20px at every size. The cell border (1px) is inside the cell size.

**Same height as the button beside it** (`eco-button` rule 8): Large ↔ `btn--md` (40/48px), Medium ↔ `btn--sm` (32/40px), Small ↔ `btn--xs` (32px). Check with `offsetHeight`.

### Typography

| Part | Value | Note |
|---|---|---|
| Number | 16px/22px, 0.32px, `text-primary` | the same at every width (Figma), not body-md's 17/24 on desktop |
| Unit | 11px/11px, 0.33px (Large from 769px); 10px/10px, 0.3px (elsewhere) | **confirmed snowflake**, `SNOWFLAKES.md` no. 1: not a type style |

The unit sits at the bottom of the value cell, centred: 3px from the bottom edge on Large from 769px, `space-2` elsewhere.

### States

| Part | State | Background | Border | Content |
|---|---|---|---|---|
| Button | Enabled | `surface-00` | 1px `border-primary` | icon `icon-primary` |
| Button | Disabled | `surface-00` | 1px `border-disabled` | icon `text-disabled` |
| Button | Focus (keyboard) | – | 2px `border-focus` outline | – |
| Value | Enabled | `surface-00` | top and bottom 1px `border-primary` | `text-primary` |
| Value | Hover | `surface-00` | all four sides 1px `border-hover` | `text-primary` |
| Value | Focus | `surface-00` | top and bottom `border-secondary`, plus 2px `border-focus` outside the cell | `text-primary` |
| Value | Disabled | `surface-00` | top and bottom `border-disabled` | number and unit `text-disabled` |

The minus button is disabled when the value is at its minimum, the plus button when it is at its maximum; the script does this.

### HTML structure

```html
<link rel="stylesheet" href="/components/css/picker-stepper.css">
<script src="/components/js/picker-stepper.js" defer></script>

<div class="picker-stepper" role="group" aria-label="Antal">
  <button type="button" class="picker-stepper__btn" data-step="-1" aria-label="Minska antal" disabled>
    <span class="icon icon--sm" aria-hidden="true">remove</span>
  </button>
  <div class="picker-stepper__value">
    <input class="picker-stepper__input" type="text" inputmode="numeric" pattern="[0-9]*" value="1" min="1" aria-label="Antal, styck" autocomplete="off">
    <span class="picker-stepper__unit" aria-hidden="true">st</span>
  </div>
  <button type="button" class="picker-stepper__btn" data-step="1" aria-label="Öka antal">
    <span class="icon icon--sm" aria-hidden="true">add</span>
  </button>
</div>
```

- Limits are attributes on the input: `min` (default 1), `max` (default none), `step` (default 1).
- Leave the unit out when there is none. Medium and Small: keep it in the markup if you like, the CSS hides it where Figma has no unit.
- Whole stepper disabled: `disabled` on the input and on both buttons.
- Needs `components/css/icon.css` for the icons. Both templates link all files.

### Behaviour (`picker-stepper.js`)

Delegated, so steppers added later work. A click on a button changes the value by `step`, keeps it within `min`/`max`, enables or disables the buttons and fires a bubbling `change` event on the input. Typing a value and leaving the field clamps it the same way. Listen for `change` on the input (or on a parent) to react. `ECO_PICKER_STEPPER.init(root)` re-checks steppers you add with a value outside the limits.

### Rules

1. **Link the shared files**, never copy the rules into a page, never write a second stepper script.
2. **Three native controls:** two `<button type="button">` and one `<input>`. Never a `<div>` with a click handler.
3. **Every control has a name:** `aria-label` on both buttons and on the input (include the unit in words: "Antal, styck"); `role="group"` + `aria-label` on the wrapper. The visible unit is `aria-hidden`.
4. **`type="text"` + `inputmode="numeric"`**, not `type="number"`: no browser spin buttons, and the numeric keyboard on touch.
5. **Never block typing or paste** in the field; the value is clamped when the field loses focus.
6. **The button beside it has the same height** (see Size model).
7. **Tokens only.** The only literals are the cell sizes (component heights, like buttons), the 3px unit offset and the unit text size (snowflake).
8. **No animation:** the user presses these buttons many times (`eco-prototype-guide`, step 6).
9. **Breakpoint test:** check at ~375px, ~700px (must look like mobile) and 1024px+ with `getComputedStyle`/`offsetHeight`: cell size, unit visible or not.

### Flags for design

- **Border color differs between Figma files:** the ECO component has `border-primary`; the instance in the PDP file (`gAuhhKQVftqFTly8D9ACp0`, Action section) shows `border-input-default`. The CSS follows the ECO component.
- **Disabled icon:** Figma `#939595`. There is no `icon-disabled` token; the CSS uses `text-disabled` (same value).
- **Button hover:** Figma has no hover state for the buttons (only for the value cell). None is built.
- **Button focus:** not in Figma. The CSS uses the 2px `border-focus` outline other ECO controls use.
- **Number on desktop:** 16/22 in Figma, while body-md is 17/24 from 769px. The CSS follows Figma.
- **Minimum width:** the PDP instance sets a minimum width of 144px on the Large desktop stepper, which is its natural width (3 × 48px). No rule is needed.
