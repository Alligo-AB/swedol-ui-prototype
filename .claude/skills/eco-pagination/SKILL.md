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
| Top spacing to the content above | `24px` xs → `32px` sm → `40px` md/lg |
| Bottom spacing | **None of its own** — see rule 1 |

### Typography & colors

| Element | Token | Color |
|---|---|---|
| Counter text ("Showing X of Y …") | `body-md`: 16px/22px, 0.32px, Regular | `surface-60` (`var(--color-surface-60)`) |
| Progress bar — track | — | `surface-10` (`var(--color-surface-10)`) |
| Progress bar — fill | — | `surface-100` (`var(--color-surface-100)`) |
| Button | **Secondary**, size **md** (see Button Styling above) | border/text `border-action-1` / `text-action-primary` |

---

### CSS template

```css
.pagination {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 24px;
  width: 190px;
  max-width: 100%;
  margin: 24px auto 0; /* xs: top 24px */
}
.pagination[hidden] { display: none; }
@media (min-width: 640px) { .pagination { margin-top: 32px; } } /* sm */
@media (min-width: 769px) { .pagination { margin-top: 40px; } } /* md + lg/xl */

.pagination__info { display: flex; flex-direction: column; align-items: center; gap: 16px; width: 100%; }

.pagination__count {
  font-family: 'Breuer Condensed', Arial, sans-serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 22px;
  letter-spacing: 0.32px;
  color: var(--color-surface-60);
  text-align: center;
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
}

.pagination__progress { width: 100%; height: 2px; background: var(--color-surface-10); position: relative; }
.pagination__progress-bar {
  position: absolute;
  inset: 0;
  width: 0%; /* set via JS: (visible / total) * 100% */
  background: var(--color-surface-100);
  transition: width var(--duration-medium-2) var(--ease-standard);
}

.pagination__btn {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: transparent;
  border: 1px solid var(--color-border-action-1);
  cursor: pointer;
  padding: 8px;                    /* xs–sm: md button mobile */
  font-family: 'Breuer Condensed', Arial, sans-serif;
  font-weight: 700;
  text-transform: uppercase;
  white-space: nowrap;
  font-size: 16px;
  line-height: 16px;
  letter-spacing: 0.32px;
  color: var(--color-text-action-primary);
  font-feature-settings: 'ss02' 1, 'ss03' 1;
  transition: background var(--duration-fast-3) var(--ease-standard);
}
.pagination__btn:hover { background: var(--color-surface-opacity-black-05); }
@media (min-width: 769px) {
  .pagination__btn { padding: 12px; font-size: 18px; line-height: 18px; letter-spacing: 0.18px; } /* md+: md button desktop */
}
```

### HTML example

```html
<div class="pagination" id="pagination-products">
  <div class="pagination__info">
    <p class="pagination__count">Showing <span id="products-pagination-count">4</span> of 6 reviews</p>
    <div class="pagination__progress">
      <div class="pagination__progress-bar" id="products-pagination-bar" style="width:66.6667%"></div>
    </div>
  </div>
  <button type="button" class="pagination__btn" onclick="showMore('products', this)">Show more reviews</button>
</div>
```

```js
function updatePagination(key, visible, total) {
  document.getElementById(key + '-pagination-count').textContent = visible;
  document.getElementById(key + '-pagination-bar').style.width = (total ? (visible / total) * 100 : 0) + '%';
  document.getElementById('pagination-' + key).hidden = visible >= total; // nothing more to load
}
```

### Rules

1. **IMPORTANT — No bottom padding of its own:** The component is always placed as the last element in a `.section` (see the Section component above). The section's own bottom padding (40/48/64/80px per breakpoint) already provides the right amount of air below — **never** add `padding-bottom`/`margin-bottom` to the pagination component itself, that would double the spacing. Only the top spacing (24/32/40/40) belongs to the component.
2. The progress bar's fill width is always computed dynamically as `(visible / total) * 100%` via JS — never hardcode a fixed percentage beyond the initial server-rendered value.
3. **Hide the whole component** (the `hidden` attribute on the outer wrapper, not just the button) once every item is already loaded. Hiding just the button leaves a misleading counter/progress bar behind.
4. The button is always **Secondary, size md**, at the full width of the component's 190px container — never Primary or another size/variant.
5. The component's width (`190px`, `max-width: 100%`) is fixed and centered regardless of how wide the parent section is — never stretch it to the section's full width.

---
