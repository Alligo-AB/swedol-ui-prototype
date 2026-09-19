---
name: eco-elevation
description: Use when choosing shadow/elevation for cards, modals, drawers, tooltips, or other raised surfaces — Shadow Bottom/Top, Designated Level (drawers), and component-specific shadows.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Elevation & Shadows (ECO Design System)

Shadows express the degree of elevation between surfaces – the bigger and softer the shadow, the higher the elevation.

### Basic concepts

| Concept | Definition |
|---|---|
| **Elevation** | The distance between two elements along the z-axis. |
| **Surface** | The lowest visible container that components, text, etc. are placed on. Corresponds to `background-primary` (`var(--color-background-primary)`). |
| **Background** | The application's background color – the surface everything rests on below the surface level. |

### Choosing the right elevation

- **Increase elevation for prioritized actions.** Users notice elements that appear closer — lift what you want them to focus on.
- **Small, sharp shadow** = the surface sits close to the background (low elevation).
- **Large, soft shadow** = the surface sits far from the background (high elevation).
- **Mimic real lighting conditions** – choose the elevation level that feels natural for the component's function.
- **Use sparingly.** Excessive elevation distracts and hurts the user experience.

The ECO Design System has **4 categories** of elevation:

| Category | Prefix | Description |
|---|---|---|
| Shadow Bottom | `elevation-b-*` | Light source from above. Most common. |
| Shadow Top | `elevation-t-*` | Light source from below. Used sparingly. |
| Designated Level | `elevation-drawer-*` | Global components on a separate layer (navigation, drawers). |
| Component Specific | `elevation-*` | Exclusive to specific components. |

---

### Shadow Bottom (`elevation-b-*`)

Simulates a light source from above. The shadow falls downward. **Most common** throughout the UI.

Each level consists of two layers: a soft main shadow + a sharp contour shadow (`0px 0px 1px 0px rgba(0,0,0,0.05)`).

| Token | CSS `box-shadow` | Level | Used for |
|---|---|---|---|
| `elevation-b-20` | `var(--shadow-elevation-b-20)` | 20% | Variant Tables (PDP/PLP), Data tables |
| `elevation-b-40` | `var(--shadow-elevation-b-40)` | 40% | Tooltip |
| `elevation-b-60` | `var(--shadow-elevation-b-60)` | 60% | Overflow menu, Notification |
| `elevation-b-80` | `var(--shadow-elevation-b-80)` | 80% | Site header, Menu, Dropdowns, Exposed Dropdowns |
| `elevation-b-100` | `var(--shadow-elevation-b-100)` | 100% | Modals |

```css
/* Example: Card with elevation-b-20 */
.card {
  box-shadow: var(--shadow-elevation-b-20);
}

/* Example: Modal with elevation-b-100 */
.modal {
  box-shadow: var(--shadow-elevation-b-100);
}
```

---

### Shadow Top (`elevation-t-*`)

Simulates a light source from below. The shadow falls upward. **Used sparingly.**

| Token | CSS `box-shadow` | Level |
|---|---|---|
| `elevation-t-20` | `var(--shadow-elevation-t-20)` | 20% |
| `elevation-t-40` | `var(--shadow-elevation-t-40)` | 40% |
| `elevation-t-60` | `var(--shadow-elevation-t-60)` | 60% |
| `elevation-t-80` | `var(--shadow-elevation-t-80)` | 80% |
| `elevation-t-100` | `var(--shadow-elevation-t-100)` | 100% |

---

### Designated Level – Drawers & Navigation

Intended for essential global components (navigation menu, drawers) that must sit on a separate layer and rarely be obstructed by other elements.

| Token | CSS `box-shadow` | Description |
|---|---|---|
| `elevation-drawer-left` | `var(--shadow-elevation-drawer-left)` | Drawer from the left – shadow on the right side |
| `elevation-drawer-right` | `var(--shadow-elevation-drawer-right)` | Drawer from the right – shadow on the left side |
| `elevation-drawer-left-menu-sublevel` | `var(--shadow-elevation-drawer-left-menu-sublevel)` | Inline drawer, sub-menu levels (level 2+) |

```css
/* Drawer from the left */
.drawer-left {
  box-shadow: var(--shadow-elevation-drawer-left);
}

/* Drawer from the right */
.drawer-right {
  box-shadow: var(--shadow-elevation-drawer-right);
}
```

---

### Component Specific

Shadows used only for specific components. Detailed in each component's own description.

| Token | CSS `box-shadow` | Used for |
|---|---|---|
| `elevation-input_control-switch` | `var(--shadow-elevation-input-control-switch)` | Toggle switch – indicates a raised level |
| `elevation-table-overflow-right` | `var(--shadow-elevation-table-overflow-right)` | Table overflow, right – shadow inside a table where content exceeds the width |
| `elevation-table-overflow-left` | `var(--shadow-elevation-table-overflow-left)` | Table overflow, left – shadow inside a table where content exceeds the width |

---

### Elevation rules

1. **Always choose the lowest possible level** – use `elevation-b-20` as the default for card-like surfaces.
2. **Increase elevation for prioritized actions** – modals and critical overlays should always sit at `elevation-b-100`.
3. **Don't mix Bottom and Top** on the same component (exception: `elevation-input-control-switch`).
4. **Drawers and navigation** should always use `elevation-drawer-*`, never `elevation-b-*`.
5. **Component Specific tokens** are never used outside their intended component.
6. **Surface ≠ Background** – Surface (`background-primary: var(--color-background-primary)`) is the visible container; Background is the underlying page background. Elevation visually separates the two.
7. **Small/sharp shadow** signals a close surface (low level). **Large/soft shadow** signals high elevation – choose accordingly.
8. **Drawer overlay** – the background overlay behind an open drawer should have `background: var(--color-surface-opacity-black-20)`. Never use `surface-opacity-black-50` (50%) for drawers.
9. **Drawer shadow** – a drawer that opens from the right should always have `box-shadow: var(--shadow-elevation-drawer-right)`. A drawer from the left should have `box-shadow: var(--shadow-elevation-drawer-left)`. The shadow is applied directly to the drawer panel, not the overlay.
10. **Drawer width** – a standard drawer should always have `width: min(500px, 100%)`. This gives a fixed 500px width on larger screens and automatically fills the full width when the window/device is narrower than 500px. Never use separate media queries to set `width: 100%` or `width: 500px` on the drawer panel.
11. **Drawer header scroll shadow** – when the drawer content is scrolled down, the header should get a shadow to visually separate it from the content. Use `elevation-b-60` (`var(--shadow-elevation-b-60)`). The `.drawer-header--elevated` class is toggled via JS when `content.scrollTop > 0`. Transition: `var(--duration-fast-3) var(--ease-standard)`.

```css
.drawer-header {
  transition: box-shadow var(--duration-fast-3) var(--ease-standard);
}
.drawer-header--elevated {
  box-shadow: var(--shadow-elevation-b-60);
}
```

```js
content.addEventListener('scroll', () => {
  header.classList.toggle('drawer-header--elevated', content.scrollTop > 0);
});
```

12. **Drawer – responsive component sizes** – at `max-width: 768px` (xs + sm breakpoints), every component inside the drawer should use Mobile Base Styling. Apply the following `@media (max-width: 768px)` block to every drawer:

```css
@media (max-width: 768px) {
  /* Header */
  .drawer-header { padding: var(--dimension-spacing-space-16, 16px) var(--dimension-spacing-space-24, 24px); }
  .drawer-title {
    font-size: 22px;       /* display-sm Mobile */
    line-height: 22px;
  }

  /* Content & footer */
  .drawer-content { padding: 0 var(--dimension-spacing-space-24, 24px) var(--dimension-spacing-space-24, 24px); gap: var(--dimension-spacing-space-16, 16px); }
  .drawer-footer { padding: var(--dimension-spacing-space-16, 16px) var(--dimension-spacing-space-24, 24px); }

  /* Save button — mobile lg: padding 12px */
  .drawer-save-btn { padding: var(--dimension-spacing-space-12, 12px) var(--dimension-spacing-space-16, 16px); }

  /* Labels — label-md Mobile: 14px/14px, 0.42px */
  .form-label {
    font-size: 14px;
    line-height: 14px;
    letter-spacing: 0.42px;
  }

  /* Inputs & selects — Large Mobile: 40px, 8px padding, body-md mobile 16px/22px */
  .form-input,
  .form-select {
    height: 40px;
    padding: var(--dimension-spacing-space-8, 8px);
    line-height: 22px;
  }
  .form-select { padding-right: var(--dimension-spacing-space-40, 40px); }   /* keep room for the dropdown arrow */

  /* Checkbox text — body-md Mobile: 16px/22px */
  .form-checkbox-item span {
    font-size: 16px;
    line-height: 22px;
    letter-spacing: 0.32px;
  }

  /* form-row stacks vertically on mobile */
  .form-row { flex-direction: column; gap: var(--dimension-spacing-space-16, 16px); }
}
```

**Summary of Mobile Base Styling for drawer components:**

| Component | Desktop (`769px+`) | Mobile (`≤768px`) |
|---|---|---|
| Drawer title | `display-sm` 26px/26px | 22px/22px |
| Header padding | `24px 32px` | `16px 24px` |
| Content padding | `0 32px 32px`, gap 24px | `0 24px 24px`, gap 16px |
| Footer padding | `24px 32px` | `16px 24px` |
| Label (`label-md`) | 16px/16px, 0.48px | 14px/14px, 0.42px |
| Input / Select | 48px, padding `8px 12px`, line-height 24px | 40px, padding `8px`, line-height 22px |
| Checkbox text | `body-md` 16px/24px, 0.32px | 16px/22px, 0.32px |
| Save button | `padding: 16px` | `padding: 12px 16px` |
| form-row | `flex-direction: row` | `flex-direction: column`, gap 16px |

---
