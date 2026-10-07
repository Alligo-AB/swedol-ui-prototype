---
name: eco-collapsible
description: Use when building a row-based expandable component/accordion, e.g. an "FAQ" section — header + animated content.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Collapsible / Accordion (ECO Design System)

A row-based expandable component — clicking the header toggles the content open/closed with an animated `max-height` transition. Used e.g. for "FAQ" sections.

### Anatomy

```
.collapsible-wrap                              ← one row, has a bottom line between rows
  .collapsible-item                            ← clickable header (onclick="toggleCollapsible(this)")
    .collapsible-item__left
      .collapsible-item__label                 ← title-md
    .collapsible-item__chevron                 ← "expand_more" icon, rotates 180° when open
  .collapsible-item__content                   ← body-lg, max-height animated via JS
```

Several `.collapsible-wrap` are stacked in a shared wrapper (e.g. `.ehp-faq`) to form a list.

### Typography

| Element | Token | Mobile | Desktop |
|---|---|---|---|
| `.collapsible-item__label` | `title-md` | 18px/22px, 0px, weight 600 | 20px/24px, 0px, weight 600 |
| `.collapsible-item__content` | `body-lg` | 18px/24px, 0.18px, weight 400 | 20px/28px, 0.18px, weight 400 |

`.collapsible-item__content` uses `color: var(--color-text-tertiary)` (`var(--color-text-tertiary)`).

### States

| State | Label color |
|---|---|
| **Enabled** | `text-primary` (`--black`, `var(--color-text-primary)`) |
| **Hover** (the whole `.collapsible-item`) | `text-action-primary-hover` (`var(--color-text-action-primary-hover)`) |

> Transition: `color` with `duration-fast-3` (150ms) and `ease-standard` — same mechanism as Inline/Action Link.

### Rules

1. **Bottom line between rows** — every `.collapsible-wrap` has `border-bottom: 1px solid var(--color-border-primary)` as a separator against the next row in the list.
2. **The last row in a list that closes out a section hides its bottom line** — if the `.collapsible-wrap` list is the section's last/only content block (i.e. nothing, e.g. a `.section-cta` row, follows the list in the same `<section>`), the last row's bottom line should **not** show. Otherwise a purposeless line is left hanging right above the section's own bottom padding. The rule is conditioned on the list's PARENT (e.g. `.ehp-faq`) itself being the section's last child — the border stays as normal if the list is followed by other content in the same section.
3. **`min-height`, not `height`, on `.collapsible-item`** — the header must be able to grow if the title wraps.
4. **The `max-height` animation is handled by JS**, not CSS — `toggleCollapsible()` sets `content.style.maxHeight` to `content.scrollHeight + 'px'` (open) or `null` (close), since CSS can't transition to/from `auto`.

### CSS

Link the shared stylesheet. Never copy its rules into a page, and never write a parallel version:

```html
<link rel="stylesheet" href="/components/css/collapsible.css">
<script src="/components/js/collapsible.js"></script>
```

`components/css/collapsible.css` is the single source for this component and `components/js/collapsible.js` its behavior. Mobile-first, desktop from 769px, `var(--…)` only. To change the component, edit that file.

### HTML example

```html
<div class="collapsible-wrap">
  <div class="collapsible-item" onclick="toggleCollapsible(this)">
    <div class="collapsible-item__left">
      <span class="collapsible-item__label">What does it cost to set up a custom webshop?</span>
    </div>
    <span class="collapsible-item__chevron"><span class="ms" aria-hidden="true">expand_more</span></span>
  </div>
  <div class="collapsible-item__content">It depends on the scope and which features you need. Contact your local sales representative and we'll work out a solution that fits your business and your budget together.</div>
</div>
```

---
