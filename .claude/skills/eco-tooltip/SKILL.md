---
name: eco-tooltip
description: Use when adding a tooltip to an icon button or other element with no visible text — shown on hover, never on keyboard focus.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Tooltip (ECO Design System)

**Figma:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=316-14656

Tooltips show on hover over icon-only buttons and give a short label explaining the button's function. Used at **all** breakpoints.

---

### Sizes

| Size | Padding | Font | Line-height | Letter-spacing |
|---|---|---|---|---|
| **Small** | `8px 12px` | 14px, Regular | 20px | 0.36px |
| **Large** | `16px 24px` | 18px, Regular | 26px | 0.36px |

> Always use **Small** for icon buttons in toolbars and table rows.

---

### Appearance

| Property | Value |
|---|---|
| Background | `rgba(0,0,0,0.9)` (`surface-100` at 90% opacity) |
| Text color | `var(--color-text-primary-inverted)` (`text-primary-inverted`) |
| Font | `Breuer Condensed Regular` |
| `font-feature-settings` | `'ss02' 1, 'ss03' 1, 'ss06' 1` |
| `white-space` | `nowrap` |
| Shadow | `elevation-b-40`: `var(--shadow-elevation-b-40)` |
| Beak | CSS triangle, 6px tall, ~12.7px wide |

---

### Positions

| Type | Description | Beak direction |
|---|---|---|
| **Top** | Tooltip above the element | Beak points down (below the tooltip block) |
| **Bottom** | Tooltip below the element | Beak points up (above the tooltip block) |
| **Left** | Tooltip to the left | Beak points right (right side of the tooltip) |
| **Right** | Tooltip to the right | Beak points left (left side of the tooltip) |
| **Left side top/bottom** | Tooltip left-aligned with an offset | Beak at top/bottom |
| **Right side top/bottom** | Tooltip right-aligned with an offset | Beak at top/bottom |

> Choose the position based on where there's room. Default: **Bottom** for buttons in toolbars (room below), **Top** for buttons in table rows (room above).

---

### Interaction

- The tooltip shows on **hover** (CSS `opacity: 1` via `.tooltip-wrap:hover .tooltip`).
- Easing: `motion-ease-standard` (`cubic-bezier(.35,0,.35,1)`), `duration-fast-2` (`100ms`).
- Never visible on keyboard navigation (`:focus`) — hover only.
- `pointer-events: none` on the tooltip element so it doesn't interfere with mouse interaction.

---

### HTML structure

```html
<!-- Button with a Bottom tooltip -->
<div class="tooltip-wrap">
  <button class="action-btn" aria-label="Add user">
    <span class="ms">person_add</span>
  </button>
  <span class="tooltip tooltip--bottom">Add user</span>
</div>

<!-- Button with a Top tooltip -->
<div class="tooltip-wrap">
  <button class="btn-row-action" aria-label="Edit">
    <span class="ms">edit</span>
  </button>
  <span class="tooltip tooltip--top">Edit</span>
</div>
```

> `aria-label` on the button is mandatory and must have the same text as the tooltip content.

---

### CSS

Link the shared stylesheet. Never copy its rules into a page, and never write a parallel version:

```html
<link rel="stylesheet" href="/components/css/tooltip.css">
```

`components/css/tooltip.css` is the single source for this component. Mobile-first, desktop from 769px, `var(--…)` only. To change the component, edit that file.

---
