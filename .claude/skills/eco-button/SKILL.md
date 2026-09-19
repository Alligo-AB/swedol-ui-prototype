---
name: eco-button
description: Use when building, changing, or reviewing buttons (`<button>`, CTAs) in swedol-ui-prototype — all variants (Primary/Secondary/Blank/Destructive/Accent/System), sizes, and states (hover/focus/disabled) per the ECO Design System.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Button Styling (ECO Design System)

**Figma:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=2007-68126

### Variants

| Variant | Background | Text | Border |
|---|---|---|---|
| **Primary** | `var(--color-surface-action-1)` | `var(--color-text-primary-inverted)` | — |
| **Primary Inverted** | `var(--color-surface-action-2)` | `var(--color-text-primary)` | — |
| **Secondary** | transparent | `var(--color-text-primary)` | `1px solid var(--color-border-action-1)` |
| **Secondary Inverted** | transparent | `var(--color-text-primary-inverted)` | `1px solid var(--color-border-action-2)` |
| **Blank** | transparent | `var(--color-text-primary)` | — |
| **Blank Inverted** | transparent | `var(--color-text-primary-inverted)` | — |
| **Destructive** | `var(--color-surface-danger-default)` | `var(--color-text-primary-inverted)` | — |
| **Accent** | `var(--color-accent-default)` | `var(--color-text-action-accent)` | — |
| **System** | transparent | `var(--color-text-primary)` | `1px solid var(--color-border-action-3)` = `border-action-3` |
| **System Selected** | `var(--color-surface-opacity-black-12)` | `var(--color-text-primary)` | `1px solid var(--color-border-action-3)` = `border-action-3` |
| **Disabled** (all variants) | `var(--color-surface-disabled)` | `var(--color-text-disabled)` | — |
| **Disabled Blank** | transparent | `var(--color-text-disabled)` | — |

> **System** is used for buttons that act at the system level (e.g. filter, sort, tool selection). Differs from Secondary via the subtle, semi-transparent border (`border-action-3`) instead of solid black.
> **System Selected** is the active/selected state of System — same border, but with a `rgba(0,0,0,0.12)` background marking the selected state.

### Sizes — Desktop (`min-width: 769px` / breakpoint `lg-md`)

| Size | Height | Padding (button) | Inner padding (text) | Font |
|---|---|---|---|---|
| **lg** | 56px | `16px` | `px-8px py-3px` | label-lg: 18px Bold, 0.18px spacing |
| **md** | 48px | `12px` | `px-8px py-3px` | label-lg: 18px Bold, 0.18px spacing |
| **sm** | 40px | `8px` | `px-8px py-4px` | label-md: 16px Bold, 0.48px spacing |
| **xs** | 32px | `6px` | `px-4px py-3px` | label-sm: 14px Bold, 0.56px spacing |

### Sizes — Mobile (default / breakpoint `sm-xs`)

| Size | Height | Padding (button) | Font |
|---|---|---|---|
| **lg** | 48px | `12px` | label-lg: 16px Bold, 0.32px spacing |
| **md** | 40px | `8px` | label-lg: 16px Bold, 0.32px spacing |
| **sm** | 32px | `6px` | label-md: 14px Bold, 0.48px spacing |
| **xs** | 32px | `6px` | label-sm: 14px Bold, 0.56px spacing |

### States

| State | Visual rule |
|---|---|
| **Enabled** | Base style per variant above |
| **Hover – Primary / Destructive / Accent** | `background-image: linear-gradient(90deg, var(--color-surface-opacity-white-20), var(--color-surface-opacity-white-20)), linear-gradient(90deg, [base color], [base color])` — white 20% overlay over the solid background color. |
| **Hover – Secondary** | `background: var(--color-surface-opacity-black-05)` — subtle dark overlay on a transparent background. |
| **Hover – Blank / icon buttons on a light background** | `background: var(--color-surface-opacity-black-05)` — same as Secondary hover. Used on `Blank` buttons and icon buttons on a white/light background. |
| **Focus** | The focus ring only shows **on keyboard navigation** (Tab). Same mechanism as form elements: `body.keyboard-nav button:focus::after { opacity: 1 }`. Ring: `border: 2px solid var(--color-border-focus)`, `inset: -3px`, `border-radius: 0`, `opacity: 0` by default with a transition. |
| **Disabled** | Bg `var(--color-surface-disabled)`, text `var(--color-text-disabled)`, `cursor: not-allowed` |

> The focus ring is implemented as a global `button::after` rule with `opacity: 0` by default. `body.keyboard-nav` is set via JS when the user presses Tab, and removed on `mousedown`/`touchstart`. **Never** use `:focus-visible` for buttons — always use the `body.keyboard-nav` pattern for consistent behavior with the form elements.

### Typography (all buttons)
- Font: `Breuer Condensed Bold`, sans-serif
- `text-transform: uppercase`
- `white-space: nowrap`
- `font-feature-settings: 'ss02' 1, 'ss03' 1` (for label-lg/md)

### CSS template (Primary)
```css
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  position: relative;
  border: none;
  cursor: pointer;
  font-family: 'Breuer Condensed', Arial, sans-serif;
  font-weight: 700;
  text-transform: uppercase;
  white-space: nowrap;
}

/* Sizes – Desktop */
.btn--lg { height: 56px; padding: 16px; font-size: 18px; letter-spacing: 0.18px; }
.btn--md { height: 48px; padding: 12px; font-size: 18px; letter-spacing: 0.18px; }
.btn--sm { height: 40px; padding: 8px;  font-size: 16px; letter-spacing: 0.48px; }
.btn--xs { height: 32px; padding: 6px;  font-size: 14px; letter-spacing: 0.56px; }

/* Sizes – Mobile (default, override with desktop: if needed) */
/* lg-mobile = 48px, md-mobile = 40px, sm/xs-mobile = 32px */

/* Variants */
.btn--primary           { background: var(--color-surface-action-1); color: var(--color-text-primary-inverted); }
.btn--secondary         { background: transparent; color: var(--color-text-primary); border: 1px solid var(--color-border-action-1); }
.btn--destructive       { background: var(--color-surface-danger-default); color: var(--color-text-primary-inverted); }
.btn--accent            { background: var(--color-accent-default); color: var(--color-text-action-accent); }
.btn--blank             { background: transparent; color: var(--color-text-primary); }

/* Hover */
.btn--primary:hover     { background-image: linear-gradient(90deg,var(--color-surface-opacity-white-20),var(--color-surface-opacity-white-20)), linear-gradient(90deg,var(--color-surface-action-1),var(--color-surface-action-1)); }
.btn--destructive:hover { background-image: linear-gradient(90deg,var(--color-surface-opacity-white-20),var(--color-surface-opacity-white-20)), linear-gradient(90deg,var(--color-surface-danger-default),var(--color-surface-danger-default)); }

/* Focus — the outline method, NOT ::after with inset.
   Reason: ::after with inset is positioned from the padding edge, not the border edge.
   Buttons with a border (e.g. Secondary 1px solid) lose the gap (inset -3px - 1px border - 2px ring = 0px gap).
   outline always measures from the outer border edge → a consistent 2px gap regardless of button variant. */
button { position: relative; outline: 2px solid transparent; outline-offset: 2px; transition: outline-color 100ms cubic-bezier(.35,0,.35,1); /* duration-fast-2, ease-standard */ }
body.keyboard-nav button:focus { outline-color: var(--color-border-focus); }

/* Disabled */
.btn:disabled, .btn--disabled { background: var(--color-surface-disabled); color: var(--color-text-disabled); cursor: not-allowed; border: none; }
.btn--blank:disabled           { background: transparent; }
```

---
