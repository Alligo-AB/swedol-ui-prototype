---
name: eco-motion
description: Use when animating or transitioning something — easing curves (decelerate/accelerate/standard) and duration tokens (fast/medium/slow) per the ECO Design System.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Motion – Easing & Duration (ECO Design System)

Animation conveys functionality, intent, and relationships. Use these tokens to create coherent, realistic transitions.

> These principles apply as guidelines. They can vary at the component level but should always be followed as closely as possible to ensure consistency.

### Three basic concepts

| Concept | Explanation |
|---|---|
| **Timing** | How long an action takes. Always choose it deliberately. |
| **Spacing** | The gap between frames in a moving object. Varied spacing produces smooth transitions. |
| **Ease** | The combination of timing and spacing. Controls how a motion flows – objects should accelerate and decelerate smoothly. |

---

### Easing tokens

Choose easing based on how a transition moves relative to the screen:

- **Small change, short distance** → fast fade
- **Medium change, medium distance** → medium fade
- **Large change, long distance** → slow fade

| Token | Curve | Type | Description | Used for |
|---|---|---|---|---|
| `motion-ease-decelerate-generic` | `cubic-bezier(.16,.38,.58,1)` | Ease Out – Generic | Starts fast, brakes gradually. Less emphasized variant. | onClick, enter selected states. Form elements, Tabs, Toggled buttons, Tooltip. |
| `motion-ease-decelerate-emphasized` | `cubic-bezier(.16,0,.16,1)` | Ease Out – Emphasized ★ | More pronounced braking. Default choice for bringing elements in from off-screen. | Drawers (all variants), Main/Account menu, Product menu, Notifications. |
| `motion-ease-accelerate-generic` | `cubic-bezier(.36,.09,1,.58)` | Ease In – Generic | Starts slow, speeds up. Like an object falling. | Removing elements from the screen (exit animations). |
| `motion-ease-standard` | `cubic-bezier(.35,0,.35,1)` | Ease InOut – Standard | Starts slow, speeds up, brakes. All-round easing. | Hover states (the majority). Button, Product Card, Text Link, Breadcrumb, Collapsible, Overflow menu, Form elements, Tab bar, Drawer Link. |

> ★ `motion-ease-decelerate-emphasized` is the first choice for enter animations. `motion-ease-decelerate-generic` is used when a lighter emphasis is wanted.

```css
/* Example: Element sliding in from off-screen (drawer) */
.drawer {
  transition: transform 350ms cubic-bezier(.16,0,.16,1);
}

/* Example: Hover state on a button */
.btn {
  transition: background-color 200ms cubic-bezier(.35,0,.35,1);
}

/* Example: Element leaving the screen */
.toast-exit {
  transition: opacity 150ms cubic-bezier(.36,.09,1,.58);
}
```

---

### Duration tokens

Duration is split into three groups — **Fast**, **Medium**, and **Slow** — with four steps each.

> Use tokens per the distance and fade principles below. For vertical movement, any duration within the right group can be used.

#### Fast (50–200ms) – Small, quick interactions

| Token | Value | Used for |
|---|---|---|
| `motion-duration-fast-1` | 50ms | Micro-interactions, immediate feedback |
| `motion-duration-fast-2` | 100ms | Fast hover transitions, focus indicators |
| `motion-duration-fast-3` | 150ms | Standard hover, fast exit animations |
| `motion-duration-fast-4` | 200ms | Light enter animations, short state changes |

#### Medium (250–400ms) – Medium-sized interactions

| Token | Value | Used for |
|---|---|---|
| `motion-duration-medium1` | 250ms | Dropdowns, tooltips, shorter slide-ins |
| `motion-duration-medium2` | 300ms | Standard for most UI transitions |
| `motion-duration-medium3` | 350ms | Drawers, panels, medium-sized surfaces |
| `motion-duration-medium4` | 400ms | Complex component transitions |

#### Slow (450–600ms) – Large, heavier motion

| Token | Value | Used for |
|---|---|---|
| `motion-duration-slow-1` | 450ms | Large enter animations, page transitions |
| `motion-duration-slow-2` | 500ms | Hero elements, full-width animations |
| `motion-duration-slow-3` | 550ms | Empty states, loading phases |
| `motion-duration-slow-4` | 600ms | The longest allowed duration – use sparingly |

---

### Distances – distance drives duration

The distance of the motion determines which duration group to use.

| Distance | Share of viewport | Duration group | Description |
|---|---|---|---|
| **Short** | ≤ 25% of the view | Fast | Covers a small part of the screen. Use fast tokens. |
| **Medium** | 26–50% of the view | Medium | Half the screen. Use medium tokens. |
| **Long** | 51–100% of the view | Slow | All or most of the screen. Use slow tokens. |

---

### Fades – opacity and color transitions

Fades are a refined way to transition between colors and/or opacity levels.

| Type | Duration group | Description | Components |
|---|---|---|---|
| **Fast fade** | Fast | Standard small-scale interactions. | Buttons, list items, form elements |
| **Medium fade** | Medium | Medium-sized interactions. Elements lifted off the surface. | Cards, elevated surfaces |
| **Slow fade** | Slow | Important state changes. | Empty states, loading phases |

---

### Combination rule: distance + fade

| Scenario | Distance | Fade | Easing |
|---|---|---|---|
| Button hover | Short | Fast fade | `motion-ease-standard` |
| Dropdown opens | Short–Medium | Fast–Medium fade | `motion-ease-decelerate-generic` |
| Drawer slides in | Medium–Long | Medium fade | `motion-ease-decelerate-emphasized` |
| Modal appears | Medium | Medium fade | `motion-ease-decelerate-emphasized` |
| Element disappears | Any | Fast fade | `motion-ease-accelerate-generic` |
| Loading/empty state | — | Slow fade | `motion-ease-standard` |

```css
/* CSS custom properties for the whole project */
:root {
  /* Easing */
  --ease-decelerate-generic:    cubic-bezier(.16,.38,.58,1);
  --ease-decelerate-emphasized: cubic-bezier(.16,0,.16,1);
  --ease-accelerate-generic:    cubic-bezier(.36,.09,1,.58);
  --ease-standard:              cubic-bezier(.35,0,.35,1);

  /* Duration */
  --duration-fast-1:   50ms;
  --duration-fast-2:   100ms;
  --duration-fast-3:   150ms;
  --duration-fast-4:   200ms;
  --duration-medium-1: 250ms;
  --duration-medium-2: 300ms;
  --duration-medium-3: 350ms;
  --duration-medium-4: 400ms;
  --duration-slow-1:   450ms;
  --duration-slow-2:   500ms;
  --duration-slow-3:   550ms;
  --duration-slow-4:   600ms;
}
```

---
