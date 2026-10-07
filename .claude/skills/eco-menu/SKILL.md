---
name: eco-menu
description: Use when building or reviewing a menu surface — the dropdown list that opens from a button/action (Dropdown menu) or from a Select field (Exposed dropdown menu). Base Item (Select / Multi Select, Enabled/Hover/Selected), Menu Item Divider (Middle-inset/Full-width/No), sizes, scrollbar and elevation. Not for the closed select field itself (use eco-select) and not for page navigation.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, breakpoints, and the quality checklist that always applies on top of this spec.

## Menu – Dropdown & Exposed Dropdown (ECO Design System)

Figma (file `42MgqJjV9vfplwQnrUB62r`): info `3516:126503`, Base Item `2723:85186`, Menu Item Divider `2728:86374`, Menu variants `2724:88966`.

### When to use / not to use

Dropdown menu and exposed dropdown menu are both just **Menu**: they differ only in the element that opens the menu surface.

- **Dropdown menu:** opened by a button, action or other control. A temporary surface that shows a list of choices.
- **Exposed dropdown menu:** the same menu opened by a **Select field** (`eco-select`). The chosen option is shown in the field above the list.
- The row content is the **List Item** component (`eco-list-item`: leading, label, trailing). `.menu__item` below is the row container and keeps the Select / Multi Select check; put a `.list-item` inside it when a row needs a leading element or trailing text.
- Not for: the closed field (`eco-select`), page/site navigation (header menu, drawer), or 2–5 always-visible options (`eco-radio`).

---

### Size model

Two sizes. Both change at `md` (769px), `sm` (640–768px) looks like mobile.

| Size | Desktop (`md:`, 769px+) | Mobile / Tablet (below 769px) | Text | Check icon |
|---|---|---|---|---|
| **Large** | row 48px | row 40px | desktop `body-md` 17/24, mobile `body-md` 16/22 | 24px desktop, 20px mobile |
| **Small** | row 40px | row 32px | `body-sm` 14/20 | 20px |

- Row padding: `16px` left and right (`--dimension-spacing-space-16`). Gap between label and icon: `8px`.
- The divider (1px) is **inside** the row height, at the bottom edge.
- Menu width: set by the opener (Figma example 408px). Never fixed in the component.
- **Scrolling:** Figma shows 14 rows (Large desktop 672px, Small desktop 560px) with a vertical scrollbar. `max-height = 14 rows`; more rows scroll.
- **Multi Select** is defined in Figma for **Large, desktop** only. It is also available for Small and mobile (derived: same row heights and the same 20px icon as the Select variant on those sizes).

### Typography

`body-md` (Large) and `body-sm` (Small), see `eco-typography`. `font-family: 'Breuer Condensed'`, `font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1`, weight 400 (same as `eco-select`).

### Variants

| Axis | Values |
|---|---|
| Size | Large, Small |
| Divider | **Middle-inset** (16px each side, default), **Full-width** (edge to edge), **No** |
| Variant (Base Item) | **Select** (one choice), **Multi Select** (any number) |
| State (Base Item) | Enabled, Hover, Selected |
| Scrollbar | shown when rows exceed 14 |

### States (Base Item)

| State | Select | Multi Select |
|---|---|---|
| **Enabled** | Fill `surface-raised-primary`, text `text-primary`, no icon | Same, plus an outline `circle` icon, `text-action-tertiary` |
| **Hover** | Fill `surface-navigation-hover`, no icon | Fill `surface-navigation-hover`, outline `check_circle` in `text-action-tertiary` (preview of the choice) |
| **Focus** (derived) | Keyboard focus (`:focus-visible`): 2px `border-focus` ring inside the row (`outline-offset: -2px`), the row's divider is hidden so it does not cross the ring | Same |
| **Selected** | Fill `surface-raised-primary`, outline `check_circle` in `text-action-primary` | Same as Select |
| **Disabled Selected** (Figma, all 4 sizes) | Text `text-disabled`, check `text-disabled`, no hover fill, `cursor: not-allowed` | Derived: same, check in `text-disabled` |
| **Disabled** (derived, not selected) | Text `text-disabled`, no icon | Derived: text and circle in `text-disabled` |

Icons: Material Symbols Outlined, weight 300, `FILL 0`.

### Container

| Part | Token |
|---|---|
| Fill | `var(--color-surface-raised-primary)` |
| Shadow | `var(--shadow-elevation-b-80)` (Figma `elevation-b-80`: used by Menu, Dropdowns and Exposed Dropdowns) |
| Divider | `var(--color-border-secondary)`, 1px |
| Scrollbar width | 12px |
| Scrollbar track | `var(--color-surface-02)` with `var(--color-border-primary)` edge |
| Scrollbar handle | `var(--color-surface-30)` ("Used for vertical scrollbar handle"), 8px wide, 4px radius |

---

### HTML structure

```html
<!-- Dropdown menu (opened by a button) -->
<div class="menu">
  <ul class="menu__items" role="listbox" aria-label="Sort by">
    <li class="menu__item" role="option" tabindex="0" aria-selected="false">
      <span class="menu__item-label">Label text</span><span class="menu__item-icon" aria-hidden="true"></span>
    </li>
    <li class="menu__item" role="option" tabindex="0" aria-selected="true">
      <span class="menu__item-label">Label text</span><span class="menu__item-icon" aria-hidden="true"></span>
    </li>
  </ul>
</div>

<!-- Variants: .menu--sm  .menu--multi (+ aria-multiselectable="true" on the ul)  .menu--full  .menu--none -->
```

The icon span is always in the markup. CSS decides when to show it (Select: only when selected; Multi Select: always).

### CSS

Link the shared stylesheet. Never copy its rules into a page, and never write a parallel version:

```html
<link rel="stylesheet" href="/components/css/menu.css">
```

`components/css/menu.css` is the single source for this component. The docs page `eco-design-system/components/menu.html` links the same file and prints it in its Code section. Mobile-first, desktop from 769px, `var(--…)` only. The `[data-state="…"]` selectors in it are only for the docs pages' forced-state demos and do nothing elsewhere. To change the component, edit that file.

**Name clash:** `.menu__item`, `.menu__item-icon` and `.menu__item-label` are also used by the main-menu drawer (`mypages/partials/main-menu.html`, styled in the page templates). Do not link `menu.css` on a page that includes that partial until one of the two is renamed (see Flags).

---

### Rules

1. **Never hardcode design tokens** — every color, spacing and shadow is a `var(--…)` (see `eco-tokens`).
2. **Mobile-first, switch at `md` (769px)**, never `sm`. Verify with `getComputedStyle` at ~375px, ~700px and ~1024px+ (row 40/40/48 for Large).
3. **Use `eco-menu` for the open list.** `eco-select` opens a `.menu` instead of the browser's native list (script: `components/js/select-menu.js`). The native `<select>` stays in the markup as the form control.
4. **Always set roles:** `role="listbox"` on the list, `role="option"` and `aria-selected` on each row, `aria-multiselectable="true"` for Multi Select. Rows are focusable (`tabindex`), Up/Down move, Enter/Space choose, Esc closes the menu and returns focus to the opener.
5. **Disabled rows:** `aria-disabled="true"` and `tabindex="-1"`. Click and Enter are ignored, arrow keys skip them, no hover fill.
6. **Never rely on the icon alone** for the selected state: `aria-selected` always matches what is shown.
7. **Never add a fixed width**; the opener sets the width.
8. **Row content = List Item** (`eco-list-item`). Put `.list-item` inside `.menu__item` for leading/trailing elements; the menu keeps the 48/40/32 row heights, dividers, hover and focus.

### Flags (for design)
- **Class names:** the dropdown rows were renamed from `.menu__item…` to `.menu__item…` (2026-10) to avoid the clash with the main-menu drawer's `.menu__item…`, so `menu.css` is now linked in the page templates.

- **Tokens confirmed in Figma (updated):** hover fill = `surface-navigation-hover`; icons = `text-action-tertiary` (circle, hover preview check) and `text-action-primary` (selected check). Icons are bound to text-action tokens, there is no icon token with these values.
- **Disabled Selected** is defined in Figma for Select (all four sizes, `text-disabled` text and check). Derived from it: the plain Disabled row and Disabled in Multi Select.
- **Derived by us, not in Figma (confirm with design):** focus ring on a row (`border-focus`, 2px inset, same color as the other form components), Multi Select for Small and mobile (20px icon, same as Select on those sizes). Still undefined: Selected + Hover (kept as Selected with hover fill), max height / when the scrollbar appears (14 rows from the Figma example), menu width.
- **Figma body weight** is 500 in the variable export; the repo (and `eco-select`) use 400 for `body-md` / `body-sm`. Followed the repo.
- **Scrollbar:** Firefox only supports a thin native scrollbar (color only); the 12px track + 8px rounded handle is WebKit/Blink.
- **Handle radius 4px** has no token.
