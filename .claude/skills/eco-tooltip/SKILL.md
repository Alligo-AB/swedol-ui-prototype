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
| **Small** | `8px 12px` | 14px, Regular | 20px | 0.28px |
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

### CSS template

```css
.tooltip-wrap {
  position: relative;
  display: inline-flex;
}

.tooltip {
  position: absolute;
  z-index: 300;
  background: rgba(0,0,0,0.9);
  color: var(--color-text-primary-inverted);
  font-family: 'Breuer Condensed', Arial, sans-serif;
  font-size: 14px;        /* Small */
  font-weight: 400;
  line-height: 20px;
  letter-spacing: 0.28px;
  white-space: nowrap;
  pointer-events: none;
  opacity: 0;
  transition: opacity 100ms cubic-bezier(.35,0,.35,1); /* duration-fast-2, ease-standard */
  box-shadow: var(--shadow-elevation-b-40);
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
}

/* Beak — shared base for all positions */
.tooltip::before {
  content: '';
  position: absolute;
  width: 0;
  height: 0;
  border-left: 6.35px solid transparent;
  border-right: 6.35px solid transparent;
}

.tooltip-wrap:hover .tooltip { opacity: 1; }

/* Bottom — tooltip below, beak points up */
.tooltip--bottom {
  top: calc(100% + 8px);
  left: 50%;
  transform: translateX(-50%);
  padding: 8px 12px;
}
.tooltip--bottom::before {
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%);
  border-bottom: 6px solid rgba(0,0,0,0.9);
}

/* Top — tooltip above, beak points down */
.tooltip--top {
  bottom: calc(100% + 8px);
  left: 50%;
  transform: translateX(-50%);
  padding: 8px 12px;
}
.tooltip--top::before {
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  border-top: 6px solid rgba(0,0,0,0.9);
}
```

---
