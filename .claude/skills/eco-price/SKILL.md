---
name: eco-price
description: Use when showing a price — on a product page, product card, small accessory card, mini cart, variant table or table card. Value with "exkl.moms", optional "Från", old price with info icon, campaign note and discount badge. Placements (page, card, card with stacked VAT, mini cart, table, compact) and price levels (not logged in, logged in, discount) by class. Not for a discount or status marker on its own (use eco-badge).
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Price (ECO Design System)

**Figma** (file `42MgqJjV9vfplwQnrUB62r`, checked 2026-11-13): Price `454:38091` (Product page, Card, Card w EPRED, Mini Cart × price level × breakpoint), Table price `303:17153`; small accessory card in the PDP file `gAuhhKQVftqFTly8D9ACp0` `2474:492811`.
**CSS:** `components/css/price.css`. **Docs page:** none yet (ask before adding). **First use:** `pdp.html` (price at the top, product cards, accessory cards, variant table and cards).

### When to use
Every price the user sees. Never write a page-local price rule: link `price.css` and pick the placement class.

### Not to use
- A discount or "Utförsäljning" marker on its own → `eco-badge` (Product & Discount). On the Product page it sits beside the old price in `.price__row`.

### Placement and price level (classes)

| Class | Placement | Value | "exkl.moms" | Old price |
|---|---|---|---|---|
| `price--page` | Product page | headline-lg 28/32, 36/40 from 769px | body-sm 14/20, 0.28px (0.36px from 769px), `text-secondary` | body-lg 18/24, 20/28 from 769px |
| `price--card` | Product card | title-md 18/22, 20/24 from 769px | body-sm 14/20, 0.36px, `text-tertiary`, same row | body-sm 14/20 |
| `price--card price--stack` | Card w EPRED | as card | under the price | as card |
| `price--mini` | Mini cart | body-md regular 16/22, 17/24 from 769px, one row, old price first | – | as value, strike |
| `price--table` | Variant table, table card | body-md bold 16/22, 17/24 from 769px, one row, old price first (card: value first) | – | body-sm 14/20, `text-secondary` |
| `price--compact` | Small accessory card | 14/20 bold, 0.28px | 12/20, 0.24px, `text-secondary` | 12/20 |

| Colour class | Price level | Value colour |
|---|---|---|
| none | Not logged in | `text-primary` |
| `price--customer` | Logged in (My account) | `text-price-customer` |
| `price--sale` | Discount | `text-price-guest` |

Bold is 600 in CSS (Figma 700). Old price: `text-tertiary`, struck through, info icon (`icon icon--sm`, `text-primary`). Campaign note ("Kampanj t.o.m …"): body-sm, `text-tertiary`.

### HTML structure

```html
<link rel="stylesheet" href="/components/css/price.css">

<!-- Card, logged in, with old price -->
<p class="price price--card price--customer">
  <span class="price__main"><span class="price__value">53,00 kr</span> <span class="price__vat">exkl.moms</span></span>
  <span class="price__extra">
    <span class="price__old"><s>63,00 kr</s><span class="icon icon--sm" aria-hidden="true">info</span></span>
    <span class="price__note">Kampanj t.o.m 2026-12-31</span>
  </span>
</p>

<!-- Table: old price first, value right-aligned in the cell -->
<span class="price price--table price--customer"><span class="price__old"><s>1 670,00 kr</s></span><span class="price__value">886,79 kr</span></span>
```

Optional "Från": `<span class="price__from">Från</span>` first in `.price__main`. Old price + discount badge side by side (Product page): `<span class="price__row">…old… <badge></span>` inside `.price__extra`.

### Rules
1. Link `price.css`; never copy its rules into a page and never write a page-local price style.
2. The price level is a colour class, never an inline colour. Prototype pages assume a logged-in customer: `price--customer` (PDP rule).
3. Update the value with `textContent` on `.price__value`, never rebuild the markup.
4. A wide, one-row price in a narrow card may get `flex-wrap: wrap` page-locally (as `.pv-card .price--table`); the base stays nowrap.
5. Tokens only. Breakpoint test at ~375px, ~700px (must look like mobile) and 1024px+ with `getComputedStyle`.

### Flags for design
- **Price level × placement:** Figma has more levels (My account with Old Price, My Account with Discount) and "Card w EPRED" layouts than are built; they are the same classes combined (`price--customer` + old price). "Card w EPRED" is `price--stack`.
- **Product page old price:** 20/28 desktop and 18/24 mobile are taken from the frames; the Figma code uses body-lg for mobile and literal 20/28 for desktop (no token).
- **Mini cart** and **Table price** at Small-XSmall in Figma wrap differently per variant; only the one-row version is built.
- **Not logged in on the PDP:** Figma shows black, the prototype uses customer teal for every price (PDP rule).
