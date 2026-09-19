---
name: eco-colors
description: Use when choosing or reviewing colors/design tokens — text, icon, background, surface, border, and status colors per the ECO Design System.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Colors – Semantic Tokens (ECO Design System)

All tokens have the `color/` prefix in Figma. Values are always sourced from `var(--color-[token])`, never hardcoded hex — see `tokens.json` in the `eco-tokens` skill for the actual hex values.

### Accent

| Token | CSS variable | Description |
|---|---|---|
| `accent-default` | `var(--color-accent-default)` | Primary accent color (lime yellow). Used in Accent buttons. |
| `accent-light` | `var(--color-accent-light)` | Light accent color. Background for accent highlights. |
| `accent-dark` | `var(--color-accent-dark)` | Dark accent color. Hover state for accent. |

```html
<!-- Example: Accent button -->
<button style="background:var(--color-accent-default); color:var(--color-text-action-accent);">Buy now</button>
```

### Text

| Token | CSS variable | Description |
|---|---|---|
| `text-primary` | `var(--color-text-primary)` | Primary text. Headings and main content. |
| `text-primary-inverted` | `var(--color-text-primary-inverted)` | Primary text on a dark/black background. |
| `text-secondary` | `var(--color-text-secondary)` | High emphasis on a light background. Secondary content – reduces cognitive load next to text-primary. |
| `text-secondary-inverted` | `var(--color-text-secondary-inverted)` | Secondary text on a dark background. |
| `text-tertiary` | `var(--color-text-tertiary)` | Medium emphasis and hint text on a white background. |
| `text-tertiary-inverted` | `var(--color-text-tertiary-inverted)` | Tertiary text on a dark background. |
| `text-disabled` | `var(--color-text-disabled)` | Disabled text. |
| `text-price-customer` | `var(--color-text-price-customer)` | Customer price (logged in). |
| `text-price-guest` | `var(--color-text-price-guest)` | Guest price (not logged in). |
| `text-price-on-black` | `var(--color-text-price-on-black)` | Price shown on a black background. |
| `text-action-primary` | `var(--color-text-action-primary)` | Primary link/clickable text (on light background). |
| `text-action-primary-hover` | `var(--color-text-action-primary-hover)` | Hover for primary link (on light background). |
| `text-action-primary-inverted` | `var(--color-text-action-primary-inverted)` | Primary link on dark background. |
| `text-action-primary-inverted-hover` | `var(--color-text-action-primary-inverted-hover)` | Hover for primary link on dark background. |
| `text-action-secondary` | `var(--color-text-action-secondary)` | Secondary link color. Used together with text-secondary. |
| `text-action-secondary-hover` | `var(--color-text-action-secondary-hover)` | Hover for secondary link. |
| `text-action-tertiary` | `var(--color-text-action-tertiary)` | Tertiary link color. Used together with text-tertiary. |
| `text-action-tertiary-hover` | `var(--color-text-action-tertiary-hover)` | Hover for tertiary link. |
| `text-action-accent` | `var(--color-text-action-accent)` | Text on an accent-colored surface. |
| `text-success` | `var(--color-text-success)` | Status text – success. |
| `text-danger-default` | `var(--color-text-danger-default)` | Status text – error/danger. |
| `text-information-default` | `var(--color-text-information-default)` | Status text – information. |

```html
<!-- Example: Text colors -->
<p style="color:var(--color-text-primary);">Primary text</p>
<p style="color:var(--color-text-secondary);">Secondary text</p>
<span style="color:var(--color-text-danger-default);">Error message</span>
<a href="#" style="color:var(--color-text-action-primary);">Link</a>
```

### Icon

| Token | CSS variable | Description |
|---|---|---|
| `icon-primary` | `var(--color-icon-primary)` | Primary icon color. Default for icons on a light background. |
| `icon-inverted` | `var(--color-icon-inverted)` | Icon on a dark background. |

### Background

| Token | CSS variable | Description |
|---|---|---|
| `background-primary` | `var(--color-background-primary)` | Primary page background. |
| `background-secondary` | `var(--color-background-secondary)` | Secondary background. Panels, cards, sidebars. |

### Surface – Neutral levels

Used to build up contrast in the grayscale. The number indicates approximate opacity/darkness (02 = lightest, 100 = black).

| Token | CSS variable | Description |
|---|---|---|
| `surface-02` | `var(--color-surface-02)` | Very light surface. Navigation hover. |
| `surface-05` | `var(--color-surface-05)` | Light gray surface. |
| `surface-10` | `var(--color-surface-10)` | Disabled background, borders. |
| `surface-15` | `var(--color-surface-15)` | Soft separator. |
| `surface-20` | `var(--color-surface-20)` | Weaker border-selected. |
| `surface-40` | `var(--color-surface-40)` | Disabled text/icon. |
| `surface-50` | `var(--color-surface-50)` | Medium gray surface. |
| `surface-60` | `var(--color-surface-60)` | Dark surface. |
| `surface-80` | `var(--color-surface-80)` | Darker surface. |
| `surface-90` | `var(--color-surface-90)` | Near-black surface. |
| `surface-100` | `var(--color-surface-100)` | Black surface. |
| `surface-raised-primary` | `var(--color-surface-raised-primary)` | Raised surface, primary (cards, modals). |
| `surface-raised-secondary` | `var(--color-surface-raised-secondary)` | Raised surface, secondary. |
| `surface-disabled` | `var(--color-surface-disabled)` | Background for disabled elements. |
| `surface-navigation-hover` | `var(--color-surface-navigation-hover)` | Navigation hover background. |

### Surface – Semantic status colors

| Token | CSS variable | Description |
|---|---|---|
| `surface-information-default` | `var(--color-surface-information-default)` | Information surface, strong. |
| `surface-information-weak` | `var(--color-surface-information-weak)` | Information surface, weak. |
| `surface-information-weaker` | `var(--color-surface-information-weaker)` | Information surface, very weak. Background for info messages. |
| `surface-success-default` | `var(--color-surface-success-default)` | Success surface, strong. |
| `surface-success-weak` | `var(--color-surface-success-weak)` | Success surface, weak. |
| `surface-success-weaker` | `var(--color-surface-success-weaker)` | Success surface, very weak. |
| `surface-warning-default` | `var(--color-surface-warning-default)` | Warning surface, strong. |
| `surface-warning-weak` | `var(--color-surface-warning-weak)` | Warning surface, weak. |
| `surface-warning-weaker` | `var(--color-surface-warning-weaker)` | Warning surface, very weak. |
| `surface-danger-default` | `var(--color-surface-danger-default)` | Danger surface, strong. |
| `surface-danger-weak` | `var(--color-surface-danger-weak)` | Danger surface, weak. |
| `surface-danger-weaker` | `var(--color-surface-danger-weaker)` | Danger surface, very weak. Background for error messages. |

```html
<!-- Example: Status messages -->
<div style="background:var(--color-surface-success-weaker); color:var(--color-text-success);">Order confirmed</div>
<div style="background:var(--color-surface-danger-weaker); color:var(--color-text-danger-default);">Something went wrong</div>
<div style="background:var(--color-surface-information-weaker); color:var(--color-text-information-default);">Fetching information...</div>
<div style="background:var(--color-surface-warning-weaker); color:var(--color-text-primary);">Low stock</div>
```

### Surface – Opacity levels

| Token | CSS variable | Description |
|---|---|---|
| `surface-opacity-black-05` | `var(--color-surface-opacity-black-05)` | Black at 5% opacity. |
| `surface-opacity-black-10` | `var(--color-surface-opacity-black-10)` | Black at 10% opacity. Subtle overlay. |
| `surface-opacity-black-20` | `var(--color-surface-opacity-black-20)` | Black at 20% opacity. |
| `surface-opacity-black-50` | `var(--color-surface-opacity-black-50)` | Black at 50% opacity. Modal background. |
| `surface-opacity-white-0` | `var(--color-surface-opacity-white-0)` | White, fully transparent. |
| `surface-opacity-white-20` | `var(--color-surface-opacity-white-20)` | White at 20% opacity. Subtle lightening on a dark background. |

### Border

| Token | CSS variable | Description |
|---|---|---|
| `border-primary` | `var(--color-border-primary)` | Standard border. Card separators. |
| `border-secondary` | `var(--color-border-secondary)` | Light border. Subtle separators. |
| `border-tertiary` | `var(--color-border-tertiary)` | Soft border. Disabled elements. |
| `border-dark` | `var(--color-border-dark)` | Dark border. Hover state. |
| `border-selected` | `var(--color-border-selected)` | Selected/active border. |
| `border-selected-hover` | `var(--color-border-selected-hover)` | Hover for selected border. |
| `border-selected-weaker` | `var(--color-border-selected-weaker)` | Weaker selected border. |
| `border-hover` | `var(--color-border-hover)` | Hover border. |
| `border-disabled` | `var(--color-border-disabled)` | Disabled border. |
| `border-input-default` | `var(--color-border-input-default)` | Input field, default. |
| `border-input-control-default` | `var(--color-border-input-control-default)` | Input controls (checkbox, radio), default. |
| `border-action-1` | `var(--color-border-action-1)` | Action button border, primary. |
| `border-action-2` | `var(--color-border-action-2)` | Action button border, inverted. |
| `border-action-3` | `var(--color-border-action-3)` | Action button border, subtle (10% black). |
| `border-focus` | `var(--color-border-focus)` | Focus ring (blue). Used with `inset: -2px`. |
| `border-information-default` | `var(--color-border-information-default)` | Information border, strong. |
| `border-information-weak` | `var(--color-border-information-weak)` | Information border, weak. |
| `border-success-default` | `var(--color-border-success-default)` | Success border, strong. |
| `border-success-weak` | `var(--color-border-success-weak)` | Success border, weak. |
| `border-warning-default` | `var(--color-border-warning-default)` | Warning border, strong. |
| `border-warning-weak` | `var(--color-border-warning-weak)` | Warning border, weak. |
| `border-danger-default` | `var(--color-border-danger-default)` | Danger border, strong. |
| `border-danger-weak` | `var(--color-border-danger-weak)` | Danger border, weak. |

```html
<!-- Example: Border usage -->
<input style="border: 1px solid var(--color-border-input-default);">
<input style="border: 2px solid var(--color-border-focus);"> <!-- focus -->
<div style="border: 1px solid var(--color-border-danger-default); background:var(--color-surface-danger-weaker);">Error message</div>
```

---
