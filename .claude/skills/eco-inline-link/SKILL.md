---
name: eco-inline-link
description: Use when building a link inside a sentence or text block — always underlined in the enabled state, never with an icon.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Inline Link (ECO Design System)

**Figma:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=1671-52629

Used **inside sentences and text blocks**. Underlined in the Enabled state — the underline is **removed** on hover, replaced by a color change. **Never** combined with icons.

### Difference from Action Link

| Property | Inline Link | Action Link |
|---|---|---|
| Placement | In body text | Standalone |
| Underline | Enabled: yes. Hover: no (removed) | Enabled: no. Hover: yes (added) |
| Icons | Never | Optional (left/right) |
| `display` | `inline` | `inline-flex` |

---

### Sizes

#### Desktop (`md:`, 769px+)

| Size | Typography token | Font-size | Line-height | Letter-spacing | Weight |
|---|---|---|---|---|---|
| **Large** | `body-lg` | 20px | 28px | 0.18px | 400 |
| **Medium** | `body-md` | 17px | 24px | 0.32px | 400 |
| **Small** | `body-sm` | 14px | 20px | 0.36px | 400 |
| **Small Bold** | `body-sm` | 14px | 20px | 0.36px | **700** |

#### Mobile / Tablet (`xs`/`sm`, ≤768px)

| Size | Font-size | Line-height | Letter-spacing |
|---|---|---|---|
| **Large** | 18px | 24px | 0.18px |
| **Medium** | 16px | 22px | 0.32px |
| **Small / Small Bold** | 14px | 20px | 0.36px |

---

### Color variants

| Variant | Enabled color | Hover color |
|---|---|---|
| **Text Primary** | `var(--color-text-action-primary)` (`text-action-primary`) | `var(--color-text-action-primary-hover)` (`text-action-primary-hover`) |
| **Text Secondary** | `var(--color-text-action-secondary)` (`text-secondary`) | `var(--color-text-action-secondary-hover)` (`text-action-secondary-hover`) |
| **Text Tertiary** | `var(--color-text-action-tertiary)` (`text-tertiary`) | `var(--color-text-action-tertiary-hover)` (`text-action-tertiary-hover`) |
| **Text Primary Inverted** | `var(--color-text-action-primary-inverted)` (`text-primary-inverted`) | `var(--color-text-action-primary-inverted-hover)` (`text-action-primary-inverted-hover`) |

---

### States

| State | Underline | Text color |
|---|---|---|
| **Enabled** | `text-decoration: underline` | Per variant above |
| **Hover** | `text-decoration: none` (removed) | Per variant above |
| **Enabled Accordion Link** | `text-decoration: underline` | Same as Text Primary |
| **Hover Accordion Link** | `text-decoration: none` | Same as Text Primary hover |

> Transition: `color` with `duration-fast-3` (150ms) and `ease-standard`. `text-decoration` is not transitioned.

---

### font-feature-settings

| Size | Value |
|---|---|
| Large (`body-lg`) | `'ss02' 1, 'ss03' 1` |
| Medium (`body-md`) | `'ss02' 1, 'ss03' 1, 'ss06' 1` |
| Small / Small Bold (`body-sm`) | `'ss02' 1, 'ss03' 1, 'ss06' 1` |

---

### CSS

Link the shared stylesheet. Never copy its rules into a page, and never write a parallel version:

```html
<link rel="stylesheet" href="/components/css/inline-link.css">
```

`components/css/inline-link.css` is the single source for this component. Mobile-first, desktop from 769px, `var(--…)` only. To change the component, edit that file.

### HTML example

```html
<!-- In body text — Text Primary, Medium -->
<p>Read more about our products on the
  <a href="#" class="inline-link inline-link--medium">product page</a>.
</p>

<!-- Text Secondary -->
<p>See <a href="#" class="inline-link inline-link--medium inline-link--secondary">full terms</a> for more info.</p>

<!-- Small Bold -->
<a href="#" class="inline-link inline-link--small-bold">Read more</a>

<!-- Inverted, in a dark context -->
<p style="color:var(--color-text-primary-inverted)">Contact us at
  <a href="mailto:info@example.com" class="inline-link inline-link--medium inline-link--inverted">info@example.com</a>.
</p>
```

---
