---
name: eco-badge
description: Use when building a non-interactive status, label, count or marker (Badge) — Basic ("New", "Archive", a role name), Dot, Number, and the e-commerce badges Product & Discount and Purchase Info (Good buy, Good to know). Five types, one page set each under components/badge.html. Not to be confused with Tag (interactive filtering) or the cart counter's `.badge` class.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Badge (ECO Design System)

**Figma – guidelines:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=4752-241948
**Figma – all variants:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=6098-342317
**Figma per type** (file 42MgqJjV9vfplwQnrUB62r): Basic `3912-157194`, Number `535-15785`, Dot `4763-292600`, Product & Discount `328-8378`, Good buy `459-19071`, Good to know `4518-196348`.

**Documentation:** a hub `eco-design-system/components/badge.html` (overview, usage, color, emphasis) and one three-page set per type: `badge-basic*.html`, `badge-dot*.html`, `badge-number*.html`, `badge-product-discount*.html`, `badge-purchase-info*.html` (each `.html`, `-specifications.html`, `-code.html`). All five types share `components/css/badge.css`. Each type page set has Anatomy (numbered markers), Variants, Accessibility, Related and References on the Examples page, and Design Tokens, Sizes (where the type has several), Measurements with a breakpoint toggle, States, Behavior and Accessibility Requirements on the Specifications page.

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

Badge/Basic comes in **6 States** × **3 Emphasis** × **3 Sizes** (Large/Medium/Small; Small looks like Medium below 769px) × an optional icon. The other types are Dot, Number, Product & Discount and Purchase Info (see the sections at the end). Product & Discount and Purchase Info are for e-commerce only.

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

| Size | Padding (Desktop) | Padding (Mobile) | Font (Desktop) | Font (Mobile) |
|---|---|---|---|---|
| **Large** | `6px 8px` | `5px 6px` | 14px/14px, 0.56px | 14px/14px, 0.48px |
| **Medium** | `4px 5px` | `3px 4px` | 14px/14px, 0.56px | **12px/12px**, 0.48px |
| **Small** | `3px 5px` | `3px 4px` (= Medium) | 12px/12px, 0.48px | 12px/12px, 0.48px |

Figma Badge/Basic (node `3912:157194`, checked 2026-10-12) has Small frames on mobile too, and the user confirmed that Small exists on mobile: Small is **not** hidden on mobile (the CSS used to hide it, and Medium used 14px on mobile). Small and Medium look the same on mobile.

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

### CSS

Link the shared stylesheet. Never copy its rules into a page, and never write a parallel version:

```html
<link rel="stylesheet" href="/components/css/badge.css">
```

`components/css/badge.css` is the single source for this component. It now includes `.badge-basic--danger` and a glyph icon (`<span class="badge-basic__icon" aria-hidden="true">info</span>`). Documentation page: `eco-design-system/components/badge.html`. Mobile-first, desktop from 769px, `var(--…)` only. To change the component, edit that file.

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
4. **Small is the same as Medium below 769px** (Figma has no separate mobile Small look) — on mobile use Medium or Large.
5. The icon (if used) is always `14px` with a `4px` gap to the text — never hardcode a different icon size in a badge.
6. **Letter Case is a deliberate parameter, not a mistake.** Sentence Case (default, weight 500) and Upper Case (weight 700 + `text-transform: uppercase`) are both valid — choose based on whether the label is a status (Sentence Case) or a fixed category (Upper Case adds extra visual weight).
7. **Color should reflect meaning, not be random.** Keep the mapping consistent within the same page/view (see "Color choice — common meanings" above) — don't mix, e.g., green for "New" in one place and blue for the same meaning elsewhere.

---

### Badge/Number (`.badge-number`)

Figma "Number", node `535:15785` (the older "Number-Icon", node `5516:31452`, is Large only). A round `surface-100` badge with `text-primary-inverted`, Breuer Condensed Bold (600), uppercase. Sizes (mobile-first, change at 769px):

| Size | Desktop | Mobile | Label |
|---|---|---|---|
| **Large** (default) | 24 × 24px, padding `0 5px` | 20 × 20px | desktop 14/14, 0.56px · mobile 12/12, 0.48px |
| **Medium** (`--md`) | 20px high, padding `0 5px` | 18px high, padding `0 4px` | same |
| **Small** (`--sm`) | 16px high, padding `0 3px` | 14px high, padding `0 2px` | 10/10, no tracking |

`min-width` equals the height: round for one digit, wider for more. The check mark (`<span class="badge-number__icon" aria-hidden="true">done</span>`) exists on every size (Figma 2026-10-12): 20px Large, 14px Medium, 11px Small desktop / 10px mobile. Markup: `<span class="badge-number">1</span>`, `<span class="badge-number badge-number--md">1</span>`. Used for counts, steps, the docs' numbered legends (`ds-bullets--num`, Medium) and the anatomy markers (`DK.callouts`, which stay 24px: `.ds-callout__pin.badge-number` in `docs.css`, Figma Marker). **Open point:** Figma's Large mobile still carries the desktop 14/14 label and a 20px check mark in a 20px circle (we use 12/12 for the number, 20px for the check mark). Not a status badge and not the cart counter `.badge`.

### Badge/Dot (`.badge-dot`)

Figma "Dot", node `4763:292600`. A circle without text: Large 10px (default), Medium 8px (`--md`), Small 6px (`--sm`), the same at every breakpoint. Five states: Danger (default, `surface-danger-default`), `--warning`, `--success`, `--info` (`surface-*-default`) and `--neutral` (`surface-20`). Next to a text, or on the top right corner of an icon or a text; never alone, never stacked, not for critical alerts. The dot has no margin; the page positions it. Decorative: `aria-hidden="true"`, say the status in text.

### Badge/Product and Badge/Discount (`.badge-promo`) — e-commerce only

Figma node `328:8378`. Label Breuer Condensed Bold, uppercase, 14/14 + 0.56px desktop, 12/12 + 0.48px mobile; 4px gap; icon 14px.

| Class | Look | Padding desktop · mobile |
|---|---|---|
| `badge-promo` | Discount: `surface-danger-default`, white text (`30% rabatt`) | `4px 5px` · `4px 4px` |
| `badge-promo badge-promo--closing` | Closing sale: `surface-100`, white text (`Utförsäljning`), only with a Discount badge | same |
| `badge-promo badge-promo--product` | Product: `surface-05`, 1px `border-primary`, `text-primary`, icon + text | `4px 5px` · `3px 4px` (+ border) |

Product icons (Material Symbols): `verified` (Standardsortiment), `assignment_turned_in` (Avtalssortiment), `history` (`23 tidigare köp`; icon only shows `23`). `badge-promo-group` puts Discount and Closing sale side by side; `badge-promo-stack` stacks them (Discount on top, left-aligned). Icon-only badges need a label (`aria-label` or hidden text).

### Badge/Purchase Info (`.badge-purchase`) — e-commerce only

Figma "Good buy" `459:19071`, "Good to know" `4518:196348`. A label with a right-pointing beak, then a short explanation beside it (8px gap, vertically centered). `<div class="badge-purchase"><span class="badge-purchase__tag"><span class="badge-purchase__label">Bra köp</span><span class="badge-purchase__beak"></span></span><p class="badge-purchase__text">…</p></div>`. Good buy = `surface-danger-default` (Figma uses the primitive `system/dark_red`, same #d90000), Good to know (`badge-purchase--know`) = `surface-50`. Label: padding `4px 3px 4px 5px` desktop, `3px 4px` mobile; type like Product; beak 10 × 22px desktop, 8 × 18px mobile (`clip-path` triangle, as high as the label). Text: body-sm 14/20, `text-secondary`, 0.36px desktop / 0.28px mobile; links in it are underlined. Colour is set by `--badge-purchase-bg` on the wrapper.

### Guidelines from Figma (node `4752:241948`, summarised in the hub page)

Badge indicates status or count, read-only; Tag (TBA) is interactive. Do not rely on color alone; combine text, emphasis and icon. Alert colors have reserved icons (info, check_circle, error, warning). Neutral pairs with alert colors for contrast. Emphasis: Strong = darker, Weak = more saturated medium, Weaker = light; do not mix emphasis without a reason. Dots are indicators, not alerts, never standalone.
