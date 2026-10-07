---
name: eco-pagination
description: Use when building a "load more" pattern for progressively loading more results into a list (reviews, products, order history) — not numbered page navigation.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Pagination (ECO Design System)

**Figma:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=11614-537671

Pagination is used to let the user load more results into a list (reviews, products, order history, etc.) without a page load — a "load more" pattern, not numbered page navigation. The component is narrow and centered (`190px`, `max-width: 100%`) and placed as the last element in a `.section`/list, regardless of how wide the parent is.

### Used when
- A list is too long to show in full right away and more items should be loaded progressively.
- The total item count is known upfront (needed for the counter text + progress bar).

### NOT used when
- Every item is already shown (hide the whole component, see rule 3).
- The page requires traditional numbered page navigation (1, 2, 3 …) — that's a different pattern.

---

### Anatomy

```
Showing [X] of [Y] [unit]
[▬▬▬▬▬▬▬▬░░░░░░]              ← progress bar, 2px
[      SHOW MORE RESULTS       ]  ← Secondary button, md, full width of the component
```

### Dimensions

| Property | Value |
|---|---|
| Total width | `190px` (`max-width: 100%`, centered) |
| Gap: info block → button | `24px` |
| Gap: counter text → progress bar | `16px` |
| Progress bar height | `2px` |
| Top spacing to the content above | `24px` xs → `32px` sm → `40px` md/lg/xl (`space-24` / `space-32` / `space-40`). This is **page spacing**, which follows the 5 ECO breakpoints (Figma and `eco-spacing`), so it steps at 640px. It is not the `space-md` token (that is 48px at lg). The component itself (text, button) still keeps Mobile Base Styling until 769px. |
| Bottom spacing | **None of its own** — see rule 1 |

### Typography & colors

| Element | Token | Color |
|---|---|---|
| Counter text ("Showing X of Y …") | `body-md`: 17px/24px (mobile 16px/22px), 0.32px, Regular | `surface-60` (`var(--color-surface-60)`) |
| Progress bar — track | — | `surface-10` (`var(--color-surface-10)`) |
| Progress bar — fill | — | `surface-100` (`var(--color-surface-100)`) |
| Button | **`eco-button` Secondary, size Medium** (`btn btn--secondary btn--md`), 40px high on mobile/tablet, 48px from 769px, label-lg 16px/18px. Figma matches Medium exactly (padding 8/12, label-lg). No own button class. | border/text `border-action-1` / `text-action-primary` |

---

### CSS

Link the shared stylesheet. Never copy its rules into a page, and never write a parallel version:

```html
<link rel="stylesheet" href="/components/css/button.css">
<link rel="stylesheet" href="/components/css/pagination.css">
<script src="/components/js/pagination.js"></script>
```

`components/css/pagination.css` is the single source for this component and `components/js/pagination.js` its behavior. Mobile-first, desktop from 769px, `var(--…)` only. To change the component, edit that file.

### HTML example

```html
<div class="pagination" id="pagination-products">
  <div class="pagination__info">
    <p class="pagination__count">Showing <span id="products-pagination-count">4</span> of 6 reviews</p>
    <div class="pagination__progress">
      <div class="pagination__progress-bar" id="products-pagination-bar" style="width:66.6667%"></div>
    </div>
  </div>
  <button type="button" class="btn btn--secondary btn--md" onclick="showMore('products', this)"><span class="btn__label">Show more reviews</span></button>
</div>
```

The counter and progress bar are updated with `updatePagination(key, visible, total)` from `components/js/pagination.js`.

### Rules

1. **IMPORTANT — No bottom padding of its own:** The component is always placed as the last element in a `.section` (see the Section component above). The section's own bottom padding (40/48/64/80px per breakpoint) already provides the right amount of air below — **never** add `padding-bottom`/`margin-bottom` to the pagination component itself, that would double the spacing. Only the top spacing (24/32/40/40) belongs to the component.
2. The progress bar's fill width is always computed dynamically as `(visible / total) * 100%` via JS — never hardcode a fixed percentage beyond the initial server-rendered value.
3. **Hide the whole component** (the `hidden` attribute on the outer wrapper, not just the button) once every item is already loaded. Hiding just the button leaves a misleading counter/progress bar behind.
4. The button is always the `eco-button` **Secondary, Medium** (`btn btn--secondary btn--md`), at the full width of the component's 190px container (`.pagination .btn { width: 100% }`) — never Primary, another size/variant or a separate button class. Link `/components/css/button.css` together with `pagination.css`.
5. The component's width (`190px`, `max-width: 100%`) is fixed and centered regardless of how wide the parent section is — never stretch it to the section's full width.

---
