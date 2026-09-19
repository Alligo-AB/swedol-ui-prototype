---
name: eco-spacing
description: Use when setting margin, padding, or gap — the fixed Spacing Scale (space-0…space-120) and the breakpoint-adaptive space-sm/space-md/space-lg tokens.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Spacing (ECO Design System)

Spacing tokens create a predictable, harmonious spacing system. Tokens are applied to all margins, padding, and position coordinates — both horizontally and vertically.

> Most values are multiples of 8px. The values 1px, 2px, and 4px are used only for fine detail. 12px is a complement used when needed.

### Spacing Scale

| Token | Value | Usage |
|---|---|---|
| `space-0` | `var(--dimension-spacing-space-0, 0px)` | Zero out spacing |
| `space-1` | `var(--dimension-spacing-space-1, 1px)` | Fine detail – very small adjustments |
| `space-2` | `var(--dimension-spacing-space-2, 2px)` | Fine detail – borders, small adjustments |
| `space-4` | `var(--dimension-spacing-space-4, 4px)` | Fine detail – inner padding in tight components |
| `space-8` | `var(--dimension-spacing-space-8, 8px)` | Base unit. Inner padding, gap in tight layouts |
| `space-12` | `var(--dimension-spacing-space-12, 12px)` | Complement. Paragraph spacing, tight lists |
| `space-16` | `var(--dimension-spacing-space-16, 16px)` | Standard padding. Mobile page margin |
| `space-24` | `var(--dimension-spacing-space-24, 24px)` | Medium spacing. Gutter on desktop |
| `space-32` | `var(--dimension-spacing-space-32, 32px)` | Tablet/desktop margin. Section spacing |
| `space-40` | `var(--dimension-spacing-space-40, 40px)` | Desktop page margin (lg). Section spacing |
| `space-48` | `var(--dimension-spacing-space-48, 48px)` | Large section spacing |
| `space-56` | `var(--dimension-spacing-space-56, 56px)` | Component height, lg button on desktop |
| `space-64` | `var(--dimension-spacing-space-64, 64px)` | Large layout spacing |
| `space-72` | `var(--dimension-spacing-space-72, 72px)` | Large layout spacing |
| `space-80` | `var(--dimension-spacing-space-80, 80px)` | Hero sections, large vertical spacing |
| `space-112` | `var(--dimension-spacing-space-112, 112px)` | Extra-large layout spacing |
| `space-120` | `var(--dimension-spacing-space-120, 120px)` | Grid margin on desktop |

### Layout Vertical Whitespace (per breakpoint)

Beyond the flat Spacing Scale above, there's a semantic, **breakpoint-adaptive** scale (T-shirt sizes: sm/md/lg) for vertical spacing between elements in a layout — e.g. `gap` in a flex-column section (like `.compare-intro`) or `padding-top` in front of a closing CTA row (`.section-cta`). Unlike `space-24`/`space-48` etc. (fixed pixel values, the same at every breakpoint), `space-sm`/`space-md`/`space-lg` HERE change pixel value depending on breakpoint:

| Token | `breakpoint-xs` | `breakpoint-sm` | `breakpoint-md` | `breakpoint-lg` | `breakpoint-xl` |
|---|---|---|---|---|---|
| `space-lg` | 32px | 40px | 48px | 56px | 56px |
| `space-md` | 24px | 32px | 40px | 48px | 48px |

> Use `space-lg`/`space-md` (this table) for the air BETWEEN a section's own content blocks (e.g. heading → card grid → CTA buttons within the same section) — not `space-24`/`space-40` etc. (fixed Spacing Scale values above), which fit better for layout margins and gutters that should NOT vary as finely per breakpoint.

```css
/* Example: gap in a flex-column section, space-lg */
.hero {
  display: flex;
  flex-direction: column;
  gap: 32px;                              /* xs: space-lg */
}
@media (min-width: 640px) {
  .hero { gap: 40px; }                    /* sm: space-lg */
}
@media (min-width: 769px) {
  .hero { gap: 48px; }                    /* md: space-lg */
}
@media (min-width: 1024px) {
  .hero { gap: 56px; }                    /* lg: space-lg */
}
@media (min-width: 1281px) {
  .hero { gap: 56px; }                    /* xl: space-lg */
}
```

---

### How tokens are used

Spacing is applied by combining a **token** (size) with a **consumer class** (where the spacing should apply).

#### Consumer classes

**Margin**
| Class | CSS property |
|---|---|
| `mt-space` | `margin-top` |
| `mr-space` | `margin-right` |
| `mb-space` | `margin-bottom` |
| `ml-space` | `margin-left` |
| `mx-space` | `margin-left` + `margin-right` |
| `my-space` | `margin-top` + `margin-bottom` |

**Padding**
| Class | CSS property |
|---|---|
| `pt-space` | `padding-top` |
| `pr-space` | `padding-right` |
| `pb-space` | `padding-bottom` |
| `pl-space` | `padding-left` |
| `px-space` | `padding-left` + `padding-right` |
| `py-space` | `padding-top` + `padding-bottom` |

**Gap (layout spacing)**
| Class | CSS property |
|---|---|
| `gap-space` | `gap` (row + column) |
| `gap-x-space` | `column-gap` |
| `gap-y-space` | `row-gap` |

### Examples

```css
/* Padding: space-16 */
.card { padding: var(--dimension-spacing-space-16, 16px); }

/* Margin: space-24 vertical, space-8 horizontal */
.item { margin: var(--dimension-spacing-space-24, 24px) var(--dimension-spacing-space-8, 8px); }

/* Gap in grid: space-24 */
.grid { display: grid; gap: var(--dimension-spacing-space-24, 24px); }
```

```html
<!-- Typical combinations per breakpoint -->
<!-- xs: space-16 page margin, space-8 gap -->
<section style="padding: 0 var(--dimension-spacing-space-16, 16px);">
  <div style="display:grid; gap:var(--dimension-spacing-space-8, 8px);">...</div>
</section>

<!-- sm/md: space-32 page margin, space-16 gap -->
<section style="padding: 0 var(--dimension-spacing-space-32, 32px);">
  <div style="display:grid; gap:var(--dimension-spacing-space-16, 16px);">...</div>
</section>

<!-- lg: space-40 page margin, space-24 gap -->
<section style="padding: 0 var(--dimension-spacing-space-40, 40px);">
  <div style="display:grid; gap:var(--dimension-spacing-space-24, 24px);">...</div>
</section>
```

---
