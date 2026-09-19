---
name: eco-badge
description: Use when building a non-interactive status or label indicator (Badge) — e.g. "New", "Updated", "Archive", a role name. Not to be confused with Tag (interactive filtering) or the cart counter's `.badge` class.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Badge (ECO Design System)

**Figma – guidelines:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=4752-241948
**Figma – all variants:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=6098-342317

Badge is a **non-interactive** status or label indicator — readable but never clickable. Don't confuse it with **Tag** (interactive, used for filtering/sorting/grouping) or with `.breadcrumb-item` (interactive navigation).

### Used when
- Status indication (e.g. "Latest", "Archive", "In progress", a role name like "Administrator").
- Counts, featured/highlighted content, or information requiring immediate attention.
- Should **not** rely on color alone to convey meaning — combine with text and/or an icon.

### NOT used when
- The element should be clickable/filterable → use **Tag** instead.
- It's a counter bubble on an icon (e.g. cart) → that's a different, already-existing component in this project: `.badge`/`.badge--white` (circular counter, see `site-header__right`). Name clash — Badge/Basic below has been given the class name `.badge-basic` to avoid colliding.

---

### Variants

Badge/Basic comes in **6 States** × **3 Emphasis** × **3 Sizes** (Large/Medium/Small, Small is Desktop-only) × an optional icon. Beyond Basic there's also Dot (dot only, no text), Number-Icon, and e-com-specific Product/Discount/Purchase badges (used only in e-commerce context, not in this project).

#### States (color)

| State | Purpose |
|---|---|
| **Neutral Grey** | Neutral status with no alert meaning (grey). |
| **Neutral Dark** | Neutral status, high contrast (black). |
| **Alert Info** | Informational — default alert color, most flexible. |
| **Alert Success** | Positive feedback/successful status. |
| **Alert Warning** | Warning, requires attention. |
| **Alert Danger** | Negative feedback/error. |

#### Emphasis (color strength) — formula per state

| Emphasis | Background | Border | Text color |
|---|---|---|---|
| **Strong** | `surface-{state}-default` (Neutral Grey: `surface-50` `var(--color-surface-50)` · Neutral Dark: `surface-100` black) | none | `text-primary-inverted` (white) |
| **Weak** | `surface-{state}-weak` (Neutral Grey: `surface-20` `var(--color-surface-20)` · Neutral Dark: `surface-100` black — identical to Strong) | none | `text-{state}-default` (Neutral Grey: `text-primary` black · Neutral Dark: `text-primary-inverted` white) |
| **Weaker** | `surface-{state}-weaker` (Neutral Grey: `surface-05` `var(--color-surface-05)` · Neutral Dark: `surface-100` black — identical to Strong/Weak) | `1px solid border-{state}-weak` (Neutral Grey: `border-primary` var(--color-border-primary) · Neutral Dark: `border-dark` `var(--color-border-dark)`) | Same as Weak |

> Neutral Dark always has a black background regardless of emphasis choice — the only difference is that Weaker gets a `border-dark` edge. `{state}` in the formula above refers to the alert name in lowercase (`information`, `success`, `warning`, `danger`) for the four Alert variants.

**Verified examples (Alert Info, Medium, Desktop):**

| Emphasis | Background | Border | Text |
|---|---|---|---|
| Strong | `surface-information-default` `var(--color-surface-information-default)` | – | `text-primary-inverted` white |
| Weak | `surface-information-weak` `var(--color-surface-information-weak)` | – | `text-information-default` |
| Weaker | `surface-information-weaker` `var(--color-surface-information-weaker)` | `1px solid border-information-weak` `var(--color-border-information-weak)` | `text-information-default` |

`Alert Success`/`Warning`/`Danger` follow exactly the same formula with their respective status color's `-default`/`-weak`/`-weaker` tokens (see the Colors section above).

---

### Sizes

| Size | Padding (Desktop) | Padding (Mobile) | Font (Desktop) | Font (Mobile) | Availability |
|---|---|---|---|---|---|
| **Large** | `6px 8px` | `5px 6px` | `label-lg--badge`: 14px/14px, 0.56px | 14px/14px, 0.48px | Desktop + Mobile |
| **Medium** | `4px 5px` | `4px 5px` | `label-lg--badge`: 14px/14px, 0.56px | same | Desktop + Mobile |
| **Small** | `3px 5px` | – | `label-sm--badge`: 12px/12px, 0.48px | – | **Desktop only** |

- Icon (optional): `14px`, `gap: 4px` between icon and text.
- Font-weight: **Medium (500)** — deliberately deviates from the project's usual 700, since this is the actual Figma spec for Badge/Basic.
- `font-feature-settings`: `'ss02' 1, 'ss03' 1` (Large/Small) — the Medium size also has `'ss06' 1`.

---

### Letter Case (parameter)

The badge text's case is its own, selectable parameter — not hardcoded. Two modes:

| Letter Case | Font-weight | `text-transform` | Used when |
|---|---|---|---|
| **Sentence Case** (default) | 500 (Medium) | None (`New`, `Updated`) | Status labels — most cases. |
| **Upper Case** | 700 (Bold) | `uppercase` (`NEW`, `LOGGED IN`) | Fixed classification/category labels where uppercase adds extra visual weight — matches the buttons'/label components' uppercase convention. |

> Choose Sentence Case as the default. Upper Case isn't "wrong" just because Sentence Case happens to fit the content — it's a deliberate style switch, not a bug fix.

---

### CSS template

```css
/* Badge/Basic — named .badge-basic to avoid colliding with the
   existing counter bubble `.badge` (cart/compare icons in the header). */
.badge-basic {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 4px 5px;                 /* Medium, default */
  font-family: 'Breuer Condensed', Arial, sans-serif;
  font-weight: 500;
  font-size: 14px;
  line-height: 14px;
  letter-spacing: 0.56px;
  white-space: nowrap;
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
}
.badge-basic__icon { width: 14px; height: 14px; flex-shrink: 0; }

/* Letter Case — Sentence Case is the default (already set above). Upper Case: */
.badge-basic--uppercase {
  font-weight: 700;
  text-transform: uppercase;
}

/* Sizes */
.badge-basic--large  { padding: 6px 8px; font-feature-settings: 'ss02' 1, 'ss03' 1; }
.badge-basic--small  { padding: 3px 5px; font-size: 12px; line-height: 12px; letter-spacing: 0.48px; font-feature-settings: 'ss02' 1, 'ss03' 1; }
@media (max-width: 768px) {
  .badge-basic--large { padding: 5px 6px; letter-spacing: 0.48px; }
  .badge-basic--small { display: none; } /* Small is Desktop-only */
}

/* Neutral */
.badge-basic--neutral-grey.badge-basic--strong  { background: var(--color-surface-50); color: var(--color-text-primary-inverted); }
.badge-basic--neutral-grey.badge-basic--weak    { background: var(--color-surface-20); color: var(--color-text-primary); }
.badge-basic--neutral-grey.badge-basic--weaker  { background: var(--color-surface-05); border: 1px solid var(--color-border-primary); color: var(--color-text-primary); }
.badge-basic--neutral-dark.badge-basic--strong,
.badge-basic--neutral-dark.badge-basic--weak    { background: var(--color-surface-100); color: var(--color-text-primary-inverted); }
.badge-basic--neutral-dark.badge-basic--weaker  { background: var(--color-surface-100); border: 1px solid var(--color-border-dark); color: var(--color-text-primary-inverted); }

/* Alert Info / Success (template for Danger — just swap the status name) */
.badge-basic--info.badge-basic--strong    { background: var(--color-surface-information-default); color: var(--color-text-primary-inverted); }
.badge-basic--info.badge-basic--weak      { background: var(--color-surface-information-weak); color: var(--color-text-information-default); }
.badge-basic--info.badge-basic--weaker    { background: var(--color-surface-information-weaker); border: 1px solid var(--color-border-information-weak); color: var(--color-text-information-default); }
.badge-basic--success.badge-basic--strong { background: var(--color-surface-success-default); color: var(--color-text-primary-inverted); }
.badge-basic--success.badge-basic--weak   { background: var(--color-surface-success-weak); color: var(--color-text-success); }
.badge-basic--success.badge-basic--weaker { background: var(--color-surface-success-weaker); border: 1px solid var(--color-border-success-weak); color: var(--color-text-success); }

/* Alert Warning — CLAUDE.md lacks a text-warning-default token (yellow text has
   poor contrast); use text-primary (black) at every emphasis level. */
.badge-basic--warning.badge-basic--strong { background: var(--color-surface-warning-default); color: var(--color-text-primary); }
.badge-basic--warning.badge-basic--weak   { background: var(--color-surface-warning-weak); color: var(--color-text-primary); }
.badge-basic--warning.badge-basic--weaker { background: var(--color-surface-warning-weaker); border: 1px solid var(--color-border-warning-weak); color: var(--color-text-primary); }
```

### Color choice — common meanings

Badge has no fixed rulebook for which status gets which color, but keep it consistent within a project. Recommended mapping for status labels of the "where is this page/component in its lifecycle" type:

| Meaning | State | Emphasis | Example |
|---|---|---|---|
| Newly created | Alert Success | Weak | `New` |
| Recently edited (existing page) | Alert Info | Weak | `Updated` |
| Ongoing/unfinished work | Alert Warning | Weak | `In progress` |
| Lower priority / outdated | Neutral Grey | Weaker | `Archive`, `Draft`, `Test` |
| Ready to hand off to development | Neutral Dark | Weaker | `Ready for development` |
| Fixed category (not a status) | Neutral Grey or Neutral Dark | Weaker/Strong | `Logged in`, `Logged out` — consider `--uppercase` here to visually distinguish category from status. |

### HTML example

```html
<!-- Neutral Grey, Weaker, Medium — default choice for status labels -->
<span class="badge-basic badge-basic--neutral-grey badge-basic--weaker">Latest</span>

<!-- Alert Success, Strong, with an icon -->
<span class="badge-basic badge-basic--info badge-basic--strong">
  <img class="badge-basic__icon" src="..." alt="" />
  Info
</span>
```

### Rules

1. **Badge ≠ Tag ≠ counter bubble.** Badge is always non-interactive (no `<button>`/`<a>`, no `cursor: pointer`, no hover state). Don't confuse it with the existing `.badge` class (the cart/compare counter in the header) — they're different components that happen to share a name in ECO's Figma file.
2. **Color must never be the sole carrier of meaning** — combine with text and/or a reserved icon (e.g. `info`/`check_circle`/`warning`/`error` for the respective Alert state, the same icon logic as Notifications).
3. **Neutral Dark always has a black background** regardless of the emphasis choice — only use it when high contrast/weight is intended, otherwise use Neutral Grey.
4. **Small size is intended for Desktop only** — use Medium or Large on mobile/tablet.
5. The icon (if used) is always `14px` with a `4px` gap to the text — never hardcode a different icon size in a badge.
6. **Letter Case is a deliberate parameter, not a mistake.** Sentence Case (default, weight 500) and Upper Case (weight 700 + `text-transform: uppercase`) are both valid — choose based on whether the label is a status (Sentence Case) or a fixed category (Upper Case adds extra visual weight).
7. **Color should reflect meaning, not be random.** Keep the mapping consistent within the same page/view (see "Color choice — common meanings" above) — don't mix, e.g., green for "New" in one place and blue for the same meaning elsewhere.

---
