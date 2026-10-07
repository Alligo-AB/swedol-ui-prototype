---
name: eco-toast-ecom
description: Use when building an e-commerce toast — e.g. "product added to cart" (Add to cart variant with product image) or "added to wishlist" (Informational variant, black background).
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

> **Buttons and ×:** buttons and the close button follow `eco-button` (see `notifications-guide`, "Buttons and the close button"): `btn btn--primary|secondary|blank` with `<span class="btn__label">`, always 32px (XSmall from 769px, Small below), and the × is `icon-btn icon-btn--close` (`icon-btn--close-inverted` on dark/solid surfaces). Live CSS: `eco-design-system/notifications.css`.

## Notification – E-Com Toast (ECO Design System)

**Figma:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=13377-22983

### Used when
- An e-commerce action is confirmed without blocking the page: product added to cart, product added to wishlist
- Short-lived feedback directly tied to a product interaction

### NOT used when
- System errors or status messages → use **System Toast** (with a status color)
- The action requires confirmation → use **E-Com Modal**

---

### Two variants

| Variant | Background | Usage |
|---|---|---|
| **Add to cart** | `var(--color-surface-raised-primary)` white | Product added to cart — shows a product image + two CTA buttons |
| **Informational** | `var(--color-surface-100)` black | Short-lived info, e.g. "added to wishlist" — text + optional link |

> Position, animation, and auto-hide follow **the same rules as System Toast** (including the `--toast-in-*` / `--toast-out-*` motion overrides) (slides in from the right, `var(--ease-decelerate-emphasized)` in and `var(--ease-accelerate-generic)` out, `var(--duration-medium-2)`, auto-hide 4000ms, `position: fixed`). Default `autoHide` in `showEcomToast` is `4000` (same as System Toast), `0` = stays until closed. The playground on `eco-design-system/components/toast-ecom.html` has the same Auto-hide On/Off + `eco-range` "Auto-hide time" (2–10 s) as `toast.html`. Like `toast.html`, it links from the playground and the code block to the Motion section (`#motion`).
>
> **Emphasis: None.** The component set exposes only `Breakpoint` and `Variant` — there's no status/emphasis property here (unlike Banner/Inline/Toast). Usage guidance: "Add to cart" confirms a product was added and surfaces immediate shopping next steps (choose accessories, go to cart); "Informational" shows short e-commerce info that needs little or no interaction (e.g. added to wishlist).

---

### Width and padding per breakpoint

> **2026-10 Figma update:** the tablet breakpoint (Figma `Small`, 640–768px) now has the **wide card (440px) and 24px padding** like desktop; only the buttons stay mobile-sized. Text is `17/24` at every breakpoint. The Add to cart secondary button is **Blank** (no frame).

| | Desktop (`md:` 769px+) | Tablet (`sm:` 640–768px) | Mobile (`xs:` below 640px) |
|---|---|---|---|
| **Add to cart** width | `440px` | `440px` | `375px` |
| **Informational** width | `375px` | `375px` | `375px` |
| Padding | `24px` | `24px` | `16px` |
| Width on xs | | | **the whole viewport width** (flush with the top, left and right edges; enters from the top and leaves upward, as the System Toast) |
| Buttons | XSmall (label-sm 14/14, 0.56px, padding 6px) | Small (label-md 14/14, 0.42px, padding 4px) | Small |

---

### Add to cart — Anatomy

```
[Product image 40×40px]  [Product name Bold] body text Regular   [✕ close]

[Choose accessories  ] [Go to cart                          ]
```

- Product image: `40×40px`, `object-fit: contain`
- Gap image–text: `16px`
- **Product name**: Bold, `body-md` 16px/18px, `var(--color-text-primary)`
- **Body text**: Regular, `body-md` 17px/24px, `0.32px`, `var(--color-text-primary)`
- **Close button**: `close` icon 20px, `padding: 2px`, black
- **Buttons** (`pt-16px` below the text, `gap: 8px`; Blank keeps its own width, Primary is fluid with `flex: 1`):
  - Blank ("Choose accessories"): no frame, transparent (was Secondary before the 2026-10 Figma update)
  - Primary ("Go to cart"): `background: var(--color-surface-100)`, white text
  - Desktop: `label-sm` 14px, 0.56px / Tablet+Mobile: `label-md` 14px, 0.42px
  - Desktop button padding: `6px` / Tablet+Mobile: `4px`
- **Shadow**: `elevation-b-80` = `var(--shadow-elevation-b-80)`

---

### Informational — Anatomy

```
[Product name Bold] body text Regular         [View]  [✕]
```

- Background: `var(--color-surface-100)`
- Border: `1px solid var(--color-border-secondary)` (`border-secondary`) — subtle edge on the black surface
- All text elements: `color: var(--color-text-primary-inverted)` (`text-primary-inverted`)
- **Text**: Bold product name (16/18) + Regular description, `body-md` 17px/24px at every breakpoint; the link wraps after the text with `8px` row / `12px` column gap
- **"View" link** (optional): underlined, `body-md` Regular (17/24 desktop and tablet, 16/22 mobile), `var(--color-text-primary-inverted)`
- **Close button**: `close` icon 20px, `padding: 2px`, white
- Gap text–link–close: `12px`
- **Shadow**: `elevation-b-80`

---

### CSS template

```css
/* Shared base */
.ecom-toast {
  position: relative;
  box-shadow: var(--shadow-elevation-b-80);
  width: 440px;        /* Add to cart desktop */
}

/* Add to cart */
.ecom-toast--cart {
  background: var(--color-surface-raised-primary);
  padding: 24px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

/* Informational */
.ecom-toast--info {
  background: var(--color-surface-100);
  border: 1px solid var(--color-border-secondary);
  padding: 24px;
  display: flex;
  align-items: flex-start;
  gap: 12px;
  width: 375px;
}

/* Mobile (below 640px); tablet keeps the wide card and 24px padding */
@media (max-width: 639px) {
  .ecom-toast--cart { padding: 16px; width: 375px; }
  .ecom-toast--info { padding: 16px; }
}

/* --- Add to cart header --- */
.ecom-toast__header {
  display: flex;
  gap: 12px;
  align-items: flex-start;
  width: 100%;
}

.ecom-toast__image-text {
  display: flex;
  gap: 16px;
  align-items: flex-start;
  flex: 1;
}

.ecom-toast__img {
  width: 40px;
  height: 40px;
  object-fit: contain;
  flex-shrink: 0;
}

.ecom-toast__product-text {
  flex: 1;
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 16px;
  color: var(--color-text-primary);
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
}

.ecom-toast__product-name {
  font-weight: 600;
  line-height: 18px;
  font-feature-settings: 'ss02' 1, 'ss03' 1;
}

.ecom-toast__product-desc {
  font-weight: 400;
  line-height: 24px;
  letter-spacing: 0.32px;
}

/* --- Add to cart footer --- */
.ecom-toast__footer {
  display: flex;
  gap: 8px;
  align-items: center;
  padding-top: 16px;
  width: 100%;
}




/* --- Informational content --- */
.ecom-toast__info-content {
  flex: 1;
}

.ecom-toast__info-text {
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 16px;
  color: var(--color-text-primary-inverted);
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
}

.ecom-toast__info-name {
  font-weight: 600;
  line-height: 18px;
  font-feature-settings: 'ss02' 1, 'ss03' 1;
}

.ecom-toast__info-desc {
  font-weight: 400;
  line-height: 24px;
  letter-spacing: 0.32px;
}


.ecom-toast__info-link {
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 24px;
  letter-spacing: 0.32px;
  color: var(--color-text-primary-inverted);
  text-decoration: underline;
  cursor: pointer;
  white-space: nowrap;
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
}




/* Buttons and ×: eco-button classes (.btn, .icon-btn.icon-btn--close); live CSS in eco-design-system/notifications.css */
.ecom-toast__footer .btn--primary { flex: 1; } /* Primary fills the row; the Blank button keeps its own width */
.ecom-toast--info .inline-link { color: var(--color-text-action-primary-inverted); } /* Inline Link, inverted */
```

### HTML example

**Add to cart:**
```html
<div class="ecom-toast ecom-toast--cart">
  <div class="ecom-toast__header">
    <div class="ecom-toast__image-text">
      <img class="ecom-toast__img" src="product.jpg" alt="Product name" />
      <p class="ecom-toast__product-text">
        <span class="ecom-toast__product-name">Carpenter Soul work pants stretch black</span>
        <span class="ecom-toast__product-desc"> has been added to the cart.</span>
      </p>
    </div>
    <button type="button" class="icon-btn icon-btn--close" aria-label="Close"><span class="btn__icon" aria-hidden="true">close</span></button>
  </div>
  <div class="ecom-toast__footer">
    <button type="button" class="btn btn--secondary"><span class="btn__label">Choose accessories</span></button>
    <button type="button" class="btn btn--primary"><span class="btn__label">Go to cart</span></button>
  </div>
</div>
```

**Informational:**
```html
<div class="ecom-toast ecom-toast--info">
  <div class="ecom-toast__info-content">
    <p class="ecom-toast__info-text">
      <span class="ecom-toast__info-name">Belt stretch black</span>
      <span class="ecom-toast__info-desc"> added to your wishlist.</span>
    </p>
    <a class="ecom-toast__info-link" href="#">View</a>
  </div>
  <button type="button" class="icon-btn icon-btn--close icon-btn--close-inverted" aria-label="Close"><span class="btn__icon" aria-hidden="true">close</span></button>
</div>
```

---
