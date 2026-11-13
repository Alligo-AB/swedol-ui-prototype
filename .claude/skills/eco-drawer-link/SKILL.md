---
name: eco-drawer-link
description: Use when a row on the page opens a drawer — Boxed (a label, an optional Action link beside it and a white framed row that shows the chosen value, e.g. the size on a product page) or Plain (one full-width row with icon, uppercase label and chevron between two lines, e.g. "Produktinformation", "Behöver du hjälp?"). States enabled/hover/focus. Not for the drawer itself (see the Drawers rule in CLAUDE.md), not for content that expands in place (use eco-collapsible), not for a dropdown list (use eco-select) and not for a link that goes to another page (see links-guide).
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Drawer Link (ECO Design System)

**Figma** (file `42MgqJjV9vfplwQnrUB62r`, checked 2026-11-12): component set `3245:111390` (Breakpoint × State × Boxed).
**CSS:** `components/css/drawer-link.css`. **JS:** none (the page opens its drawer). **Docs page:** none yet (ask before adding one). **First use:** `pdp.html` (Action section, size).

A Drawer Link is the row the user presses to open a drawer. The chevron tells that something opens to the side. The drawer itself is built by the Drawers rule in `CLAUDE.md` (reference `mypages/users.html`).

### When to use
- **Boxed:** the user makes a choice in a drawer and the row shows the current choice (size, color, store).
- **Plain:** the row opens a drawer with more content (product information, specifications, help).

### Not to use
- The content should open in place, below the row → `eco-collapsible`.
- A short list of options that opens under the field → `eco-select`.
- The row goes to another page → `links-guide` (Action link or Tile link).
- Rows inside a menu or a list surface → `eco-menu`, `eco-list-item`.

### Size model

| Variant | Part | Below 769px | From 769px |
|---|---|---|---|
| Boxed | Row height (border included) | 40px | 48px |
| Boxed | Row padding | `space-8` top/bottom and right, `space-16` left | 11px top/bottom (`space-12` − 1px border), `space-8` right, `space-16` left |
| Boxed | Gap label row → row | `space-8` | `space-8` |
| Boxed | Chevron | 20px | 24px |
| Plain | Row height (lines included) | 74px (72px + two 1px lines) | 74px |
| Plain | Padding | 22px top/bottom, 0 left/right | `space-24` top/bottom, `space-4` left/right |
| Plain | Icon and chevron | 20px | 24px |
| Plain | Gap icon → label | `space-8` | `space-8` |

### Typography (see `eco-typography`; switches at 769px, never at 640px)

| Part | Style | Mobile | Desktop |
|---|---|---|---|
| Boxed label | label-md, uppercase | 14/14, 0.42px | 16/16, 0.48px |
| Boxed link | Action link Small (`eco-action-link`), `text-secondary` | 14/20 | 14/20 |
| Boxed value | body-md | 16/22, 0.32px | 17/24, 0.32px |
| Plain label | label-lg, uppercase | 16/16, 0.32px | 18/18, 0.18px |

Label weight is 600 in CSS (Figma Bold; CSS = Figma − 100).

### States

| Variant | State | Background | Border | Text |
|---|---|---|---|---|
| Boxed row | Enabled | `surface-00` | 1px `border-primary` | value `text-primary` |
| Boxed row | Hover | `surface-00` | 1px `border-hover` | value `text-tertiary` |
| Plain | Enabled | none | 1px `border-primary` above and below | `text-primary` |
| Plain | Hover | `surface-navigation-hover` | unchanged | `text-primary` |
| Both | Focus (keyboard) | – | 2px `border-focus` outline, 2px offset | – |

Transition: `duration-fast-3` / `ease-standard` on color (hover), as on the action link.

### HTML structure

```html
<link rel="stylesheet" href="/components/css/drawer-link.css">

<!-- Boxed -->
<div class="drawer-link">
  <div class="drawer-link__head">
    <span class="drawer-link__label" id="size-label">Storlek</span>
    <!-- optional -->
    <a href="#" class="action-link action-link--small drawer-link__link">
      <span class="action-link__icon" aria-hidden="true">straighten</span>
      <span class="action-link__label">Storleksguide</span>
      <span class="action-link__icon" aria-hidden="true">chevron_right</span>
    </a>
  </div>
  <button type="button" class="drawer-link__row" aria-labelledby="size-label size-value" aria-haspopup="dialog">
    <span class="drawer-link__value" id="size-value">C44 - 275072599-44</span>
    <span class="icon icon--sm" aria-hidden="true">chevron_right</span>
  </button>
</div>

<!-- Plain: the element itself is the row -->
<button type="button" class="drawer-link drawer-link--plain" aria-haspopup="dialog">
  <span class="drawer-link__lead">
    <span class="icon icon--sm" aria-hidden="true">support_agent</span>
    <span class="drawer-link__title">Behöver du hjälp?</span>
  </span>
  <span class="icon icon--sm" aria-hidden="true">chevron_right</span>
</button>
```

- The row is a `<button type="button">` when it opens a drawer on the page. The page's own script opens the drawer.
- Stacked Plain rows share one line between them (the CSS removes the doubled line).
- The leading icon on a Plain row is optional.
- Needs `components/css/icon.css` and, for the Boxed link, `action-link.css`. Both templates link all files.
- The link beside the label follows the arrow rule in `eco-icon`: with a text label the trailing icon is a chevron; a link that opens a new tab has `open_in_new` instead (as on the PDP size guide).

### Rules

1. **Link the shared stylesheet**, never copy its rules into a page.
2. **Only for opening a drawer.** If nothing opens to the side, it is another component (see Not to use).
3. **`<button>` for the row**, never a `<div>` with a click handler; `aria-haspopup="dialog"`, and on a Boxed row `aria-labelledby` naming label and value so a screen reader says "Storlek C44 …".
4. **Always the trailing `chevron_right`**, `aria-hidden`. Never an arrow, never a down chevron (that is a select or a collapsible).
5. **A long value is cut with an ellipsis** on one line; the row never grows in height.
6. **Tokens only.** The literals are the 22px Plain padding and the 28px content height on mobile (Figma, no token), each with a comment in the CSS.
7. **Visible keyboard focus** (`:focus-visible`); never `outline: none`.
8. **The drawer** follows the Drawers rule in `CLAUDE.md`; return focus to the row when the drawer closes.
9. **Breakpoint test:** check at ~375px, ~700px (must look like mobile) and 1024px+ with `getComputedStyle`/`offsetHeight`: row height, text size, chevron size.

### Flags for design

- **Focus state:** not in Figma (only Enabled and Hover). The CSS uses the 2px `border-focus` outline with 2px offset, as on List Item.
- **Hover value color:** Figma binds the primitive `text/medium-emphasis` (#737373); the CSS uses the semantic token with the same value, `text-tertiary`.
- **Plain row on mobile:** the 22px padding has no spacing token.
- **Stacked Plain rows:** Figma shows one row at a time, with a line above and below. Sharing one line between stacked rows is an assumption.
- **Trailing icon of the Boxed link:** the component shows `chevron_right`, the PDP instance `open_in_new`. Both are allowed here (see HTML structure).
- **Disabled state:** not in Figma, not built.
