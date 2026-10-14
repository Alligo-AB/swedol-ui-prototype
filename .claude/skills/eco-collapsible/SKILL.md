---
name: eco-collapsible
description: Use when building a row-based expandable component/accordion, e.g. an "FAQ" section or a filter group — header (title, descriptive text, icons, toggle switch, number badge, chevron) + animated content. Sizes Large/Small, Boxed, Dark, Disabled.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Collapsible / Accordion (ECO Design System)

A row-based expandable component. A click on the header opens or closes the content with an animated `max-height` transition. Used for FAQ sections and filter groups. Documentation: three pages, `eco-design-system/components/collapsible.html` (+ `-specifications`, `-code`).

**Figma** (checked 2026-10-14): Base / Collapsible `535:15947` (axes Breakpoint, State, Theme, Size, Boxed; the description says the header is a building block, and that expansion state and content are coordinated by the composed pattern), Collapsible & Collapsible open `3375:138321` (closed/open examples: checkboxes, FAQ text, footer link; the content is free, not limited to these), Support + Visa mer `8657:125202`, boxed setup `23386:26225`.

### Anatomy

```
.collapsible-wrap                              ← one row, 1px line under it (+ --open --small --boxed --dark --disabled)
  <button class="collapsible-item">            ← header (recommended; the old <div onclick> still works)
    .collapsible-item__left
      .ms                                      ← optional leading icon
      .collapsible-item__text                  ← optional, when there is a descriptive or helper text
        .collapsible-item__line
          .collapsible-item__label             ← title ("Title:")
          .collapsible-item__info              ← optional descriptive text, regular weight
        .collapsible-item__helper              ← optional helper text, body-sm
      .ms                                      ← optional trailing icon
    .collapsible-item__end
      .form-switch-item (--xs on Small)        ← optional toggle switch
      .badge-number (--md Large, --sm Small)   ← optional number badge
      .collapsible-item__chevron               ← "expand_more", rotates 180° when open
  .collapsible-item__content                   ← must follow the header; max-height animated by JS
    (.collapsible-item__body)                  ← inside a boxed row
```

### Sizes and values

| | Large | Small |
|---|---|---|
| Header | min-height 72px, padding 24px top/bottom | min-height 56px, padding 16px top/bottom |
| Title | `title-md` 18/22 → 20/24 (769px), weight 600 | `title-sm` 16/18 |
| Descriptive text | regular, 18/24 → 20/24 | `body-md` 16/22 → 17/24 |
| Icons, chevron | 24px | 20px |
| Switch | 48×24 (default) | 32×16 (`form-switch-item--xs`) |
| Number badge | `badge-number--md` (20px desktop, 18px mobile) | `badge-number--sm` (16px desktop, 14px mobile) |
| Gaps | icon–text 8px, title–descriptive 2px, text–right group 16px | same |

Helper text: `body-sm` 14/20, 0.36px, `text-tertiary`. Open row: 32px extra space below the content. Content: `body-md` 16/22 → 17/24, `text-primary`, 12px between paragraphs (changed 2026-10-14 from body-lg grey 18/24 → 20/28, to follow Figma: user decision "följ Figma").

### Boxed (Small only)

`collapsible-wrap--small collapsible-wrap--boxed`: 1px `border-primary` frame, header padding 16px on all sides. Open: header `surface-02` with a 1px line under it, body (`collapsible-item__body`) `background-primary`, padding 16px, gap 12px, no extra space below.

### Theme and states

| | Text, icons, chevron | Other |
|---|---|---|
| Light enabled | `text-primary` | line `border-primary` |
| Light hover (whole header) | `text-action-primary-hover` (also the icons) | |
| Dark (`--dark`) | `text-action-primary-inverted`, hover `text-action-primary-inverted-hover` | line `border-dark`, number badge `surface-raised-primary` with `text-primary` |
| Disabled (`--disabled` + `disabled`) | `text-disabled`, no hover, no click | number badge `surface-disabled` |

Figma defines Disabled once, under Theme Dark, with `text-disabled`; the CSS applies it to both themes. The dark content text (`text-primary-inverted`) is not specified in Figma. Transition: `color` with `duration-fast-3` and `ease-standard`. All transitions are off with `prefers-reduced-motion`.

### Content patterns (Figma)

Checkbox list: `collapsible-item__list` (gap/padding from `space-24`/`space-8`) with `collapsible-item__row` (checkbox + `collapsible-item__count`, 16/22 tertiary). Support block: `collapsible-item__support` with `collapsible-item__note` (body-sm tertiary), `collapsible-item__more` ("Show more", text-only, body-md bold, underlined on hover; Figma uses an Action Link without icon, the Action Link component always has an icon) and optionally a Secondary XSmall button.

### Rules

1. **Bottom line between rows** — every `.collapsible-wrap` has `border-bottom: 1px solid var(--color-border-primary)` as a separator against the next row.
2. **The last row in a list that closes out a section hides its bottom line** — conditioned on the list's PARENT being the section's last child (`section > *:last-child .collapsible-wrap:last-child`), not for a boxed row.
3. **`min-height`, not `height`, on `.collapsible-item`** — the header must be able to grow if the title wraps.
4. **The `max-height` animation is handled by JS** — `toggleCollapsible()` sets `content.style.maxHeight` to `scrollHeight` (open) or `null` (close).
5. **Header is a `<button>`** with `aria-expanded` and `aria-controls` (the script keeps `aria-expanded` in sync). Closed content is `visibility: hidden` after the close animation, so it is not read or focused.
6. **A switch inside an opening header is a control inside a control.** Figma shows both together; build a row with a switch **without a chevron** (header as `div`), or move the switch out. A click on `.form-switch-item`, a link or `[data-collapsible-ignore]` inside the header does not toggle the row.
7. **Boxed is Small only.** Large + boxed does not exist in Figma.
8. The old `<div class="collapsible-item" onclick>` markup keeps working (same classes).

### CSS and JS

Link the shared files. Never copy their rules into a page, and never write a parallel version:

```html
<link rel="stylesheet" href="/components/css/collapsible.css">
<script src="/components/js/collapsible.js"></script>
```

A switch needs `switch.css`, a number `badge.css`, checkboxes `checkbox.css`. Mobile-first, desktop from 769px, `var(--…)` only.

### HTML example

```html
<div class="collapsible-wrap">
  <button type="button" class="collapsible-item" onclick="toggleCollapsible(this)" aria-expanded="false" aria-controls="faq-1">
    <span class="collapsible-item__left">
      <span class="collapsible-item__label">What does it cost to set up a custom webshop?</span>
    </span>
    <span class="collapsible-item__end">
      <span class="collapsible-item__chevron"><span class="ms" aria-hidden="true">expand_more</span></span>
    </span>
  </button>
  <div class="collapsible-item__content" id="faq-1"><p>It depends on the scope and which features you need.</p></div>
</div>
```

### Motion

Open/close uses `--co-ease` / `--co-duration` (fallback: `ease-standard`, `duration-fast-4`, the recommended values) on `.collapsible-wrap`, its chevron and its content. The docs page has a Motion section (`DK.motion`, prefix `co`) to compare other tokens live. Set the vars on a wrapper to override.

### Open points (also on the documentation page)

- `max-height` is set once when the row opens; if the text wraps differently after a resize while open, the height is not updated.
- Figma shows the switch and the chevron in one header (see rule 6).
- Dark content text and the Disabled-on-light theme are not defined in Figma.
