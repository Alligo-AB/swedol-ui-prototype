---
name: eco-tile-link
description: Use when building a graphical/prominent link presented as a card or button — brand logos, icon+label tiles. Does not replace regular buttons or in-text link types.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Tile Link (ECO Design System)

**Figma:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=1671-53188

Used as a **card or button** when the link needs to be presented graphically and prominently — e.g. brand logos as a link group, or icons with text. Should **not** replace regular buttons or in-text link types.

---

### Variants

| Variant | Content | Placement |
|---|---|---|
| **Brand** | Brand logo (image) | Horizontal |
| **Label + Icon** | Material Symbol (24px/20px) + text label | Vertical or Horizontal |
| **Label Only** | Text label with no icon | Horizontal |

### Sizes

| Size | Type | Description |
|---|---|---|
| **Large** | All variants | Larger surface, clearer hierarchy |
| **Small** | Label + Icon, Label Only | Compact surface |

### Background colors

| Color | Background | Enabled border | Hover border |
|---|---|---|---|
| **White** | `var(--color-border-action-2)` (`surface-action-2`) | `var(--color-border-primary)` (`border-primary`) | `var(--color-border-hover)` (`border-hover`) |
| **Grey** | `var(--color-border-secondary)` (`surface-raised-secondary`) | `var(--color-border-primary)` (`border-primary`) | `var(--color-border-hover)` (`border-hover`) |
| **Black** | `var(--color-border-action-1)` (`surface-action-1`) | `var(--color-border-action-1)` (`border-action-1`) | `var(--color-border-action-1)` + white 20% overlay |

---

### States

| State | Border | Text color | Background |
|---|---|---|---|
| **Enabled** | `1px solid border-primary` (var(--color-border-primary)) | `text-primary` (var(--color-text-primary)) | Per color variant |
| **Hover** | `1px solid border-hover` (var(--color-border-hover)) | `text-action-primary-hover` (var(--color-text-action-primary-hover)) | Per color variant |
| **Hover – Black** | `1px solid border-action-1` (`var(--color-border-action-1)`) | Icon/text stays white | `linear-gradient(var(--color-surface-opacity-white-20), var(--color-surface-opacity-white-20)), linear-gradient(var(--color-surface-100),var(--color-surface-100))` |

> The border is implemented as an absolutely positioned element (`inset: 0`) inside the tile link — not as a `border` directly on the container element. This means the border doesn't affect the layout's dimensions.

---

### Dimensions per variant and breakpoint

#### Brand

| Version | Height | Padding (horizontal) | Logo |
|---|---|---|---|
| **Desktop Large** | 112px | `px-48px` | 48×99px |
| **Mobile Large** | 80px | `px-32px` | 24×50px |

#### Label + Icon — Desktop (`769px+`)

| Size | Placement | Padding | Icon | Gap |
|---|---|---|---|---|
| **Large** | Vertical | `px-16px py-10px` | 24px | `gap: 4px` |
| **Large** | Horizontal | `px-16px py-8px` | 20px | `gap: 8px` |
| **Small** | Vertical | `px-16px py-8px` | 24px | `gap: 4px` |
| **Small** | Horizontal | `px-16px py-6px` | 20px | `gap: 8px` |

#### Label + Icon — Mobile (`≤768px`)

| Size | Placement | Padding | Icon | Gap |
|---|---|---|---|---|
| **Large** | Vertical | `px-16px py-9px` | 24px | `gap: 4px` |
| **Large** | Horizontal | `px-16px py-9px` | 20px | `gap: 4px` |
| **Small** | Vertical | `px-8px py-6px` | 24px | `gap: 4px` |
| **Small** | Horizontal | `px-8px py-6px` | 20px | `gap: 4px` |

#### Label Only — Desktop (`769px+`)

| Size | Padding |
|---|---|
| **Large** | `px-16px py-8px` |
| **Small** | `px-16px py-6px` |

#### Label Only — Mobile (`≤768px`)

| Size | Padding |
|---|---|
| **Large** | `px-16px py-9px` |
| **Small** | `px-8px py-6px` |

---

### Typography

| Size | Token | Desktop | Mobile | `font-feature-settings` |
|---|---|---|---|---|
| **Large** | `body-md` | 16px / 24px / 0.32px | 16px / 22px / 0.32px | `'ss02' 1, 'ss03' 1, 'ss06' 1` |
| **Small** | `body-sm` | 14px / 20px / 0.28px | 14px / 20px / 0.28px | `'ss02' 1, 'ss03' 1, 'ss06' 1` |

Text color Enabled: `text-primary` (var(--color-text-action-primary)). Text color Hover: `text-action-primary-hover` (var(--color-text-action-primary-hover)). Font: Breuer Condensed Regular.

---

### CSS template

```css
/* Tile Link — wrapper (gives the correct display behavior) */
.tile-link {
  display: inline-flex;
  position: relative;
  cursor: pointer;
  text-decoration: none;
}

/* Inner tile (the border's container) */
.tile-link__inner {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--color-surface-raised-primary);           /* White — default */
  transition: border-color 150ms cubic-bezier(.35,0,.35,1);
}

/* Vertical placement */
.tile-link--vertical .tile-link__inner { flex-direction: column; gap: 4px; }

/* Horizontal placement */
.tile-link--horizontal .tile-link__inner { flex-direction: row; }

/* Border (absolute, doesn't affect layout) */
.tile-link__inner::before {
  content: '';
  position: absolute;
  inset: 0;
  border: 1px solid var(--color-border-primary);    /* border-primary — Enabled */
  pointer-events: none;
  transition: border-color 150ms cubic-bezier(.35,0,.35,1);
}

/* Hover */
.tile-link:hover .tile-link__inner::before { border-color: var(--color-border-hover); /* border-hover */ }

/* Background variants */
.tile-link--grey .tile-link__inner  { background: var(--color-surface-05); }
.tile-link--black .tile-link__inner { background: var(--color-surface-100); }
.tile-link--black .tile-link__inner::before { border-color: var(--color-text-primary); }

/* Hover Black — white 20% overlay */
.tile-link--black:hover .tile-link__inner {
  background-image: linear-gradient(90deg, var(--color-surface-opacity-white-20), var(--color-surface-opacity-white-20)),
                    linear-gradient(90deg, var(--color-surface-100), var(--color-surface-100));
}

/* Label */
.tile-link__label {
  font-family: 'Breuer Condensed', Arial, sans-serif;
  font-weight: 400;
  color: var(--color-text-primary);                /* text-primary */
  white-space: nowrap;
  text-align: center;
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;

  /* Large desktop */
  font-size: 16px;
  line-height: 24px;
  letter-spacing: 0.32px;
}
.tile-link--small .tile-link__label { font-size: 14px; line-height: 20px; letter-spacing: 0.28px; }

/* Hover — label color */
.tile-link:hover .tile-link__label { color: var(--color-text-action-primary-hover); /* text-action-primary-hover */ }

/* Black variant — label is always white */
.tile-link--black .tile-link__label { color: var(--color-text-primary-inverted); }
.tile-link--black:hover .tile-link__label { color: var(--color-text-primary-inverted); }

/* Icon */
.tile-link__icon {
  font-size: 24px;               /* Large Vertical */
  color: var(--color-text-primary);
}
.tile-link--horizontal .tile-link__icon { font-size: 20px; }
.tile-link--small.tile-link--vertical .tile-link__icon { font-size: 24px; }
.tile-link:hover .tile-link__icon { color: var(--color-text-action-primary-hover); }
.tile-link--black .tile-link__icon,
.tile-link--black:hover .tile-link__icon { color: var(--color-text-primary-inverted); }

/* Sizes — Desktop */
.tile-link--large.tile-link--vertical  .tile-link__inner { padding: 10px 16px; }
.tile-link--small.tile-link--vertical  .tile-link__inner { padding: 8px 16px; }
.tile-link--large.tile-link--horizontal .tile-link__inner { padding: 8px 16px; gap: 8px; }
.tile-link--small.tile-link--horizontal .tile-link__inner { padding: 6px 16px; gap: 8px; }

/* Mobile */
@media (max-width: 768px) {
  .tile-link__label { line-height: 22px; }     /* body-md mobile: 22px */

  .tile-link--large.tile-link--vertical  .tile-link__inner { padding: 9px 16px; }
  .tile-link--small.tile-link--vertical  .tile-link__inner { padding: 6px 8px; }
  .tile-link--large.tile-link--horizontal .tile-link__inner { padding: 9px 16px; gap: 4px; }
  .tile-link--small.tile-link--horizontal .tile-link__inner { padding: 6px 8px;  gap: 4px; }
}

/* Brand variant */
.tile-link--brand.tile-link--large .tile-link__inner {
  height: 112px;
  padding: 0 48px;
}

@media (max-width: 768px) {
  .tile-link--brand.tile-link--large .tile-link__inner {
    height: 80px;
    padding: 0 32px;
  }
}
```

### HTML example

```html
<!-- Label + Icon, Large, Vertical, White -->
<a href="#" class="tile-link tile-link--large tile-link--vertical tile-link--white">
  <div class="tile-link__inner">
    <span class="material-symbols-outlined tile-link__icon">bolt</span>
    <span class="tile-link__label">Generator</span>
  </div>
</a>

<!-- Label + Icon, Small, Horizontal, Grey -->
<a href="#" class="tile-link tile-link--small tile-link--horizontal tile-link--grey">
  <div class="tile-link__inner">
    <span class="material-symbols-outlined tile-link__icon">search</span>
    <span class="tile-link__label">Search</span>
  </div>
</a>

<!-- Label Only, Large, White -->
<a href="#" class="tile-link tile-link--large tile-link--horizontal tile-link--white">
  <div class="tile-link__inner">
    <span class="tile-link__label">Generator</span>
  </div>
</a>

<!-- Brand, Large, White -->
<a href="#" class="tile-link tile-link--brand tile-link--large tile-link--white">
  <div class="tile-link__inner">
    <img src="brand-logo.svg" alt="Björnkläder" style="height:48px;" />
  </div>
</a>

<!-- Brand, Large, Black -->
<a href="#" class="tile-link tile-link--brand tile-link--large tile-link--black">
  <div class="tile-link__inner">
    <img src="brand-logo-white.svg" alt="Björnkläder" style="height:48px;" />
  </div>
</a>
```

---
