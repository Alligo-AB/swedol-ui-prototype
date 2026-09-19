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
| `.collapsible-item__content` | `body-lg` | 18px/24px, 0px, weight 400 | 20px/28px, 0px, weight 400 |

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

### CSS template

```css
.collapsible-wrap {
  border-bottom: 1px solid var(--color-border-primary);
  transition: padding-bottom var(--duration-fast-4) var(--ease-standard);
}
/* The last collapsible-wrap in a list hides its bottom border WHEN
   the list is the section's last/only content (i.e. nothing — e.g.
   a CTA row — follows it in the same <section>) — otherwise a
   purposeless line would hang right above the section's own bottom
   padding. Conditioned on the list's PARENT (e.g. .ehp-faq) itself
   being the section's last child, so the border stays as normal if
   the list is followed by other content in the same section. */
section > *:last-child .collapsible-wrap:last-child { border-bottom: none; }

.collapsible-wrap--open { padding-bottom: 32px; }

.collapsible-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 24px 0;
  cursor: pointer;
  min-height: 72px;
  box-sizing: border-box;
}
.collapsible-item__left {
  display: flex;
  align-items: center;
  gap: 8px;
}
.collapsible-item__left .ms { color: var(--black); }

/* title-md (ECO Design System): mobile 18px/22px, desktop 20px/24px, 0px spacing, weight 600 */
.collapsible-item__label {
  font-size: 18px;
  font-weight: 600;
  line-height: 22px;
  letter-spacing: 0;
  color: var(--black);
  transition: color var(--duration-fast-3) var(--ease-standard);
}
.collapsible-item:hover .collapsible-item__label { color: var(--color-text-action-primary-hover); }
@media (min-width: 769px) {
  .collapsible-item__label { font-size: 20px; line-height: 24px; }
}

.collapsible-item__chevron .ms {
  color: var(--black);
  font-size: 24px;
  transition: transform var(--duration-fast-4) var(--ease-standard);
}
.collapsible-wrap--open .collapsible-item__chevron .ms { transform: rotate(180deg); }

/* body-lg (ECO Design System): mobile 18px/24px, desktop 20px/28px, 0px spacing, weight 400 */
.collapsible-item__content {
  max-height: 0;
  overflow: hidden;
  transition: max-height var(--duration-fast-4) var(--ease-standard);
  font-size: 18px;
  font-weight: 400;
  line-height: 24px;
  letter-spacing: 0;
  color: var(--color-text-tertiary);
}
@media (min-width: 769px) {
  .collapsible-item__content { font-size: 20px; line-height: 28px; }
}
```

```js
function toggleCollapsible(header) {
  const wrap = header.parentElement;
  const content = header.nextElementSibling;
  const isOpen = wrap.classList.contains('collapsible-wrap--open');
  wrap.classList.toggle('collapsible-wrap--open', !isOpen);
  content.style.maxHeight = isOpen ? null : content.scrollHeight + 'px';
}
```

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
