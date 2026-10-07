---
name: eco-divider
description: Use when separating content groups with a thin line (Divider) — horizontal between sections/list items, vertical between side-by-side items. Three colors (Border Primary/Secondary/Tertiary). Not for section boundaries that already have their own padding (see eco-section `.page-divider`) and not a replacement for whitespace, headings or labels.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, breakpoints, and the quality checklist that always applies on top of this spec.

## Divider (ECO Design System)

**Figma – guidelines:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=18282-2867
**Figma – component:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=894-27082

A divider is a **1px line** that creates visual separation between content, so users can scan and group information. It is decorative: it carries no content and no interaction.

### Used when
- Separating distinct content groups within a page or container, when spacing alone does not suffice.
- Organizing sections of a page or list (e.g. rows in a menu or settings list).
- Creating hierarchy where content lacks a clear separation.
- Separating form sections or interactive items such as menu items.
- Showing options: a divider with text (like "or") between alternative actions. *(Mentioned in Figma usage text, but the Figma component has no text variant — see Flags.)*

### NOT used when
- Whitespace alone separates the content well enough. Do not overuse: lines add visual clutter.
- The content is naturally grouped or related.
- It would be purely decorative. A divider must have a structural purpose.
- A heading or label already makes the grouping clear.
- The line is a **section boundary** between full-width blocks → use `.page-divider` (see `eco-section`), which adds the page margin and padding around the same 1px line.

---

### Variants

| Axis | Values |
|---|---|
| **Variant** (direction) | Horizontal · Vertical |
| **Color** | Border Primary (default) · Border Secondary · Border Tertiary |

6 combinations, all 1px thick. Divider has **no states** (no hover/focus/disabled) and **no breakpoint-specific values**: it looks the same on mobile and desktop.

| Color | Token | Value | Meaning |
|---|---|---|---|
| **Border Primary** (default) | `var(--color-border-primary)` | `#e5e5e5` | Default separation. |
| **Border Secondary** | `var(--color-border-secondary)` | `#f6f6f6` | Less prominent, but still present. Very low contrast: use on white only. |
| **Border Tertiary** | `var(--color-border-tertiary)` | `#dad9d7` | More prominent; for shorter/smaller separations, e.g. values placed side by side. |

### Size

| Variant | Thickness | Length |
|---|---|---|
| Horizontal | `1px` (height) | Fills the container (`width: 100%`). Figma shows 335px = a mobile content width, not a fixed value. |
| Vertical | `1px` (width) | Fills the height of the row (`align-self: stretch`). Figma shows 112px = an example height, not a fixed value. |

The thickness is a `1px` hairline; there is no spacing token for it. Never use a thicker line.

---

### HTML structure

Semantic first. A divider between list items or sections is a plain `<hr>`: it is announced as a separator by screen readers. A divider that is only visual, inside a component, is `aria-hidden`.

```html
<!-- Horizontal, default color -->
<hr class="divider" />

<!-- Horizontal, tertiary -->
<hr class="divider divider--tertiary" />

<!-- Vertical, between side-by-side items (inside a flex row) -->
<div class="flex-row">
  <span>Size</span>
  <span class="divider divider--vertical" role="separator" aria-orientation="vertical"></span>
  <span>Weight</span>
</div>

<!-- Purely visual line inside a component (hidden from assistive tech) -->
<span class="divider" aria-hidden="true"></span>
```

### CSS

Link the shared stylesheet. Never copy its rules into a page, and never write a parallel version:

```html
<link rel="stylesheet" href="/components/css/divider.css">
```

`components/css/divider.css` is the single source for this component. The docs page `eco-design-system/components/divider.html` links the same file and prints it in its Code section. Mobile-first, desktop from 769px, `var(--…)` only. The `[data-state="…"]` selectors in it are only for the docs pages' forced-state demos and do nothing elsewhere. To change the component, edit that file.

Spacing around a divider comes from the **parent** (`gap`, or padding on neighbours), never from margin on the divider: see `eco-spacing`.

---

### Rules

1. **Structural purpose only.** Add a divider only when whitespace does not separate enough. Never for decoration.
2. **Do not rely on color alone** for meaning. Border Secondary (`#f6f6f6`) is nearly invisible: if the line carries meaning, use Primary or Tertiary and make sure the content structure (headings, lists) also conveys the grouping.
3. **Semantics.** Use `<hr>` (or `role="separator"` with `aria-orientation="vertical"`) when the line separates content for all users. Use `aria-hidden="true"` when it is only visual and the structure already explains the grouping.
4. **Always 1px, color tokens only.** Never hardcode a hex: `var(--color-border-primary|secondary|tertiary)`. Never a thicker line, dashed or dotted style.
5. **No margin on the divider.** Set the space above and below from the parent (`gap`) so spacing does not stack with neighbours (CLAUDE.md quality rule 4).
6. **Full-width section boundary** → `.page-divider` in `eco-section`, not `.divider`.
7. **Do not overuse.** Several dividers in a row is a sign that spacing or a heading would be clearer.
8. **Test line** (CLAUDE.md quality rule 1): the divider has no breakpoint values, but check with `getComputedStyle` at ~375px, ~700px and ~1024px that thickness is `1px` and the color matches the table above.

### Flags

> **Flag for design — text divider.** The Figma usage text says dividers "with text (like 'or')" can show options. The Figma component set (node 894-27082) has only the six line variants, no text variant. Not built; ask before inventing one (CLAUDE.md quality rule 7).

> **Flag for design — existing `.page-divider__line`.** `eco-section` already has a 1px `var(--color-border-primary)` line for page sections. It matches Divider Horizontal / Border Primary. Kept as is (it adds page padding); `.divider` is for lines inside a container.
