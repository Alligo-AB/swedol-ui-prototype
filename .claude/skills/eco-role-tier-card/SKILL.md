---
name: eco-role-tier-card
description: Use when building a role card/tier card pair that introduces two tiers within the same category (e.g. Standard/Administrator) side by side and links onward to a full comparison table.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Role Card / Tier Card (ECO Design System)

A card pair presenting two tiers within the same category (e.g. a base tier and an extended/administrative tier) side by side, linking onward to a detailed comparison table further down the page. Used on `feature-comparison-roles.html` (Standard/Administrator, Company Standard/Company Special) and `e-handelspartner.html` (Individual/Company, Small & medium business/Large business & group) to introduce that page's roles/account types before the full `.compare-table` comparison. The content (name, badge, description, feature strips) is adapted per page — the CSS classes and JS function (`goToCompareView()`) are identical and copied as-is.

### Anatomy

```
.role-tier-pair                                  ← grid, 2 cards side by side (md+)
  .role-tier                                      ← light card (base tier)
    .role-tier__info                              ← left half
      .role-tier__badge-row                       ← icon + .compare-badge
      .role-tier__name                            ← title-lg
      .role-tier__desc                             ← body-md
      .role-tier__link                             ← Action Link, "arrow_downward" icon
    .role-tier__features                           ← right half, stacked strips
      .role-tier__feature × 4                      ← body-sm, centered text
  .role-tier.role-tier--dark                       ← extended/administrative card
    (same substructure)
```

Several `.role-tier-pair` can be stacked one below another (one per category/tab to be introduced).

### Color variants

| Part | Light card (base tier) | `.role-tier--dark` (extended tier) |
|---|---|---|
| Card background | `surface-raised-primary` (`var(--color-surface-raised-primary)`) | `surface-100` (`var(--color-surface-100)`) |
| Card border | `border-primary` (`var(--color-border-primary)`) | `surface-90` (`var(--color-surface-90)`) |
| Title/icon | `text-primary` (`var(--color-text-primary)`) | `accent-default` (`var(--color-accent-default)`) |
| Description | `text-secondary` (`var(--color-text-secondary)`) | `text-secondary-inverted` (`var(--color-text-secondary-inverted)`) |
| Link | `text-action-primary` → hover `text-action-primary-hover` | `text-action-primary-inverted` → hover `text-action-primary-inverted-hover` |
| Feature strips | `surface-05` (`var(--color-surface-05)`) background, `border-primary` between | `surface-90` (`var(--color-surface-90)`) background, `rgba(255,255,255,.12)` between |

> This is the same "light vs. dark tier" pattern found on external SaaS pricing pages, but in the ECO Design System's own color tokens, sharp corners (`border-radius: 0`), and typography — not pill-shaped buttons or arbitrary colors.

### Typography

| Element | Token | Mobile | Desktop |
|---|---|---|---|
| `.role-tiers__eyebrow` | `label-sm` | 12px/12px, 0.48px, weight 600, uppercase | 14px/14px, 0.56px |
| `.role-tiers__title` / `.role-tier__group-title` | — (same scale as `.fob__title`) | 26px/30px, weight 700 | 36px/40px |
| `.role-tiers__desc` (the section's intro) | `body-lg` | 18px/24px, 0px | 20px/28px |
| `.role-tier__name` | `title-lg` | 20px/24px, 0px, weight 600 | 24px/28px |
| `.role-tier__desc` | `body-md` | 16px/22px, 0.32px | 16px/24px |
| `.role-tier__link` | Action Link, Medium, **Bold** variant | 16px/24px, 0.32px, weight 700, gap 6px, icon 24px | same |
| `.role-tier__feature` | `body-sm` | 14px/20px, 0.28px | same |

### Rules

1. **The link switches the active tab in the table BEFORE scrolling** — `.role-tier__link` calls a small wrapper function (e.g. `goToCompareView(event, view)`) that finds the right `.compare-view-btn[data-view="…"]` and reuses the table's own `setCompareView(view, btn)` — not its own separate copy of that logic — so the segment pill and visibility update identically to a normal tab click, before `scrollIntoView({behavior:'smooth'})` runs. `event.preventDefault()` is required so the browser's direct anchor jump doesn't "snap" mid-smooth-scroll.
2. **Feature strips must be grounded in the actual comparison table's rows** — pick 3–4 rows that are unique to/relevant for that specific role (not made-up content) so the card matches what the table actually shows once the user scrolls there.
3. **The card pair's order mirrors the tabs' order** in `.compare-view-toggle` — the first card pair belongs to the first tab, and so on.
4. **The link uses the Bold variant (700) and a 24px icon**, not Regular/20px like `.compare-intro__link` — the card's CTA needs to hold its own against the surrounding body text and read clearly as the primary clickable element, whereas `.compare-intro__link` sits alone in an emptier area and works fine with Regular.

### CSS template (the core)

```css
.role-tier-pair {
  display: grid;
  grid-template-columns: 1fr;
  gap: 24px;
}
@media (min-width: 769px) {
  .role-tier-pair { grid-template-columns: 1fr 1fr; }
}

.role-tier {
  display: flex;
  flex-direction: column;
  border: 1px solid var(--color-border-primary);
  background: var(--color-surface-raised-primary);
}
@media (min-width: 640px) {
  .role-tier { flex-direction: row; }
}
.role-tier--dark {
  background: var(--color-surface-100);
  border-color: var(--color-surface-90);
}

.role-tier__features {
  flex: 1 1 45%;
  display: flex;
  flex-direction: column;
  border-top: 1px solid var(--color-border-primary);
}
@media (min-width: 640px) {
  .role-tier__features { border-top: none; border-left: 1px solid var(--color-border-primary); }
}
.role-tier--dark .role-tier__features { border-color: rgba(255,255,255,0.12); }

.role-tier__feature {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 16px;
  min-height: 56px;
  background: var(--color-surface-05);
  font-size: 14px;
  line-height: 20px;
  letter-spacing: 0.28px;
  color: var(--color-text-primary);
}
.role-tier__feature + .role-tier__feature { border-top: 1px solid var(--color-border-primary); }
.role-tier--dark .role-tier__feature { background: var(--color-surface-90); color: var(--color-text-primary-inverted); }
.role-tier--dark .role-tier__feature + .role-tier__feature { border-top-color: rgba(255,255,255,0.12); }
```

```js
// Reuses the table's own setCompareView() — does NOT build a parallel
// copy of the tab logic.
function goToCompareView(event, view) {
  if (event) event.preventDefault();
  var btn = document.querySelector('.compare-view-btn[data-view="' + view + '"]');
  if (btn) setCompareView(view, btn);
  var target = document.getElementById('jamforelse');
  if (target) {
    // A plain scrollIntoView() doesn't account for the site's sticky
    // header (--header-top-h, the same CSS variable .compare-header-row/
    // .compare-group__header already use for their own sticky top
    // offset) — otherwise the section's top ends up hidden behind the header.
    var headerTopH = parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--header-top-h')) || 0;
    var targetY = target.getBoundingClientRect().top + window.scrollY - headerTopH;
    window.scrollTo({ top: targetY, behavior: 'smooth' });
  }
}
```

> **Always scroll to an `id`-anchored section with the `--header-top-h` offset, never with a plain `scrollIntoView()`** — on pages with a sticky site header, the header would otherwise hide the top of the section. `--header-top-h` is already set by the header's own JS and is the same variable `.compare-header-row`/`.compare-group__header` use for their sticky positioning, so reuse it instead of computing your own offset.

### Quick links in the intro (`.role-quicklinks`)

A compact row with ONE link per role, placed directly below `.compare-intro__desc` (before `.compare-card-grid`) — a quick "table of contents" showing exactly which roles/accounts the page compares, even before the visitor has scrolled past the hero. Complements (doesn't replace) the full `.role-tier-pair` cards further down: same roles, same `goToCompareView()` linking, but without a description or feature list — just a name + arrow.

```
.role-quicklinks                                 ← flex, wrap, centered, gap 8px
  .role-quicklink × 1 per role                    ← <a>, System button (xs, 32px)
    <span>Role name</span>
    <span class="ms">arrow_downward</span>
```

- **Size/variant**: built as the ECO Design System's **System** button variant (`border: 1px solid border-action-3`, transparent background) in **xs** size (32px tall, identical mobile/desktop) — deliberately the smallest, most discreet button type available, since this is a shortcut and NOT a primary CTA (those already exist in `.role-tier-pair` further down the page).
- **Hover**: `background: var(--color-surface-opacity-black-05)` + `border-color: var(--color-border-dark)` — same hover pattern as the Secondary button.
- **Link logic**: the same `goToCompareView(event, view)` as `.role-tier__link` — switches the active tab in `.compare-view-toggle` and scrolls (with the `--header-top-h` offset) to `#jamforelse`. NEVER build your own copy of the tab/scroll logic here.

```css
.role-quicklinks {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 8px;
  margin-top: 24px; /* space-24 — gap to .compare-intro__desc above */
}
.role-quicklink {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  height: 32px;
  padding: 6px 12px;
  box-sizing: border-box;
  border: 1px solid var(--color-border-action-3);
  background: transparent;
  color: var(--color-text-primary);
  text-decoration: none;
  cursor: pointer;
  white-space: nowrap;
  font-size: 14px;
  font-weight: 700;
  line-height: 14px;
  letter-spacing: 0.56px;
  text-transform: uppercase;
  transition: background var(--duration-fast-3) var(--ease-standard), border-color var(--duration-fast-3) var(--ease-standard);
}
.role-quicklink:hover {
  background: var(--color-surface-opacity-black-05);
  border-color: var(--color-border-dark);
}
.role-quicklink .ms { font-size: 16px; color: currentColor; }
```

---
