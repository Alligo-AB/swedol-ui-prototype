---
name: eco-banner-notification
description: Use when building a page-wide banner notification at the top of the page (maintenance/outage/campaign) or a rich My Pages dashboard banner — Size Small/Large, Emphasis Strong/Weak/Weaker per status, and Promotion (Dark/Light/Strong/Weak) for brand campaigns.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Notification – Banner (ECO Design System)

**Figma:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=13377-41997
**Figma – component guide:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=23432-270125

> **2026-09 update:** Banner was restructured in Figma. `System Extra Strong` (the old centered, solid-color admin-impersonation variant) no longer exists as its own tier — it's merged into the top of the regular emphasis ladder (`Strong`, solid-color background). A new `Weaker` emphasis tier was added below `Weak`. A new `Size` property was added: `Small` (the existing 1-size banner) and `Large` (new — a richer, icon+heading+body+buttons banner, exclusive to signed-in/My Pages contexts). `E-Com Action` was renamed/restructured to **`Promotion`** with emphasis `Dark`/`Light`/`Strong`/`Weak`.

### Used when
- Page-wide messages affecting the whole page or system (maintenance, outage, campaign)
- The message should stay visible until the user closes it or the state changes — does **not** disappear automatically
- Placed at the very top of the page, **above** all page content (`Small`), or at the top of the My Pages dashboard after sign-in (`Large`)

### NOT used when
- Feedback on a specific action → use **Toast** (short-lived) or **Inline** (contextual)
- The message is for a single form field → use `form-helper--error`
- Blocks the action and requires confirmation → use **Modal**

---

### Size

| Size | Used for |
|---|---|
| **Small** | The general-purpose 1-size banner — system status, outages, maintenance, warnings, standard promotions. Can appear on any page, logged in or not. |
| **Large** | A richer banner with a big icon, heading, body copy, action buttons, and an optional text link. **Exclusive to My Pages** — appears at the top of the dashboard after sign-in, directed at a specific signed-in customer or customer group. `Small` variants may also target a specific signed-in customer/group, but `Large` is only available in signed-in mode. |

Both sizes take the full width of their container (`width: 100%`). No fixed width is set.

#### Small — layout per breakpoint

| Property | Desktop (`md:` 769px+) | Mobile/Tablet (`xs`/`sm` ≤768px) |
|---|---|---|
| Height | `48px` (`min-height`) | `40px` (`min-height`) |
| Padding | `12px` all sides | `8px` all sides |
| Icon | 24px | 24px |
| Left border width | `2px` | `2px` |
| Title text | `label-sm` Desktop: 14px, 0.56px, Bold, uppercase | `label-sm` Mobile: 12px, 0.48px, Bold, uppercase |
| Body text | `body-sm` Desktop: 14px/20px, 0.28px, Regular | Mobile: 12px/18px, 0.24px, Regular |

#### Large — layout per breakpoint

| Property | Desktop (`md:` 769px+, `1200px` symbol) | Tablet (`sm:` 640–768px, `768px` symbol) | Mobile (`xs:` 0–639px, `375px` symbol) |
|---|---|---|---|
| Content padding | `24px` | `16px` | `12px` top, `12px` sides, `16px` bottom |
| Left border width | `8px` | `4px` | `4px` |
| Icon | `48px` | `40px` | `24px` |
| Gap icon → text | `12px` | `12px` | `8px` |
| Gap title → body | `12px` | `8px` | `8px` |
| Title (`title-md`) | 20px/24px, 0px, Bold | 18px/22px, 0px, Bold (mobile scale) | 18px/22px, 0px, Bold (mobile scale) |
| Body (`body-md`) | 16px/24px, 0.32px, Regular | 16px/22px, 0.32px, Regular (mobile scale) | 16px/22px, 0.32px, Regular (mobile scale) |
| Footer indent (`padding-left`, aligns under text) | `60px` (= icon 48 + gap 12) | `52px` (= icon 40 + gap 12) | `32px` (= icon 24 + gap 8) |
| Button group | `pt-24px`, `gap-8px`, buttons are **xs** size | same | same |
| Button text | `label-sm` desktop: 14px/14px, 0.56px | `label-sm` mobile: 12px/12px, 0.48px | `label-sm` mobile: 12px/12px, 0.48px |
| Text link (optional, below buttons) | `body-md` 16px/24px, 0.32px, underline | `body-md` mobile scale | `body-md` mobile scale |

> **Large** always shows a status icon (48/40/24px), a `title-md` heading, `body-md` body copy, and a `Notification / Section / Footer - Call to Action` action group (Primary + Secondary/Blank buttons, optional text link below) — see Anatomy below. This is a heavier content contract than `Small`; don't use `Large` for a simple one-line status message.

---

### Variants

#### Emphasis — status banners (Informational / Success / Warning / Error)

Three tiers, same ladder for both `Small` and `Large` (only the left-border width and padding scale differ per Size — see tables above):

| Emphasis | Background | Left border | Other borders | Text color |
|---|---|---|---|---|
| **Strong** | `var(--color-surface-{status}-default)` (solid status color) | `var(--color-surface-{status}-weaker)` | none | `var(--color-text-primary-inverted)` (white) |
| **Weak** | `var(--color-surface-{status}-weaker)` | `var(--color-surface-{status}-default)` | `Small`: `1px solid var(--color-surface-{status}-weaker)` (same tone as bg). `Large`: `1px solid var(--color-border-{status}-weak)` | `var(--color-text-primary)` (black) |
| **Weaker** | `var(--color-surface-raised-primary)` (white) | `var(--color-surface-{status}-default)` | none | `var(--color-text-primary)` (black) |

`{status}` = `information` / `success` / `warning` / `danger` (Error uses the `danger` token family).

> **Strong is the old `System Extra Strong`.** The solid-color, white-text, high-priority treatment (e.g. admin impersonation — "Din roll är ADMINISTRATÖR och du agerar tillfälligt som [namn]") now lives at `Strong` emphasis, left-aligned like every other tier — it's no longer a separate centered variant. If you're migrating old markup that used a centered `.banner-notification--extra-strong` layout, switch it to the standard left-aligned `Strong` layout (see CSS template below); centering is no longer part of the spec.

#### Status + colors

| Status | Strong background | Weak background | Weaker left-border / Strong left-border-accent | Icon | Material Symbol |
|---|---|---|---|---|---|
| **Informational** | `var(--color-surface-information-default)` | `var(--color-surface-information-weaker)` | `var(--color-surface-information-default)` / `var(--color-surface-information-weaker)` | `var(--color-text-information-default)` | `info` |
| **Error** | `var(--color-surface-danger-default)` | `var(--color-surface-danger-weaker)` | `var(--color-surface-danger-default)` / `var(--color-surface-danger-weaker)` | `var(--color-text-danger-default)` | `error` |
| **Success** | `var(--color-surface-success-default)` | `var(--color-surface-success-weaker)` | `var(--color-surface-success-default)` / `var(--color-surface-success-weaker)` | `var(--color-text-success)` | `check_circle` |
| **Warning** | `var(--color-surface-warning-default)` | `var(--color-surface-warning-weaker)` | `var(--color-surface-warning-default)` / `var(--color-surface-warning-weaker)` | `var(--color-border-warning-default)` (no dedicated `text-warning` token) | `warning_amber` |

#### Usage guidance per status

| Status | Usage guidance | Action | Sizes |
|---|---|---|---|
| **Informational** | Neutral guidance, minor site disruptions, planned site updates, background-status updates, or campaign price announcements. General e-commerce info like free-shipping eligibility or limited-time offers — generally paired with `Weaker` emphasis. | Supports an optional text link or CTA button targeting cart or promo pages. | Small, Large |
| **Success** | Confirms background process completions or system success states without requiring user action. | Auto-dismissible or persistent with a link. | Small, Large |
| **Warning** | Informs users of optimal actions or scheduled system-maintenance warnings. | Stays until dismissed or the maintenance window has passed. | Small, Large |
| **Error** | System-wide service outages, major disruptions, or unpaid invoices requiring user remediation. | Persistent until the blocking system problem is resolved. | Small, Large |

> Whether a dismiss (×) button is shown is generally decided by the banner's administrator/content owner, not hardcoded per status.
> **`Large`** variants of every status are exclusive to My Pages/signed-in mode (see Size table above) — `Small` variants may also target a specific signed-in customer/group, but only `Small` is available when the user isn't signed in.

#### Promotion (replaces the old "E-Com Action")

Used **only** for brand-driven campaign banners — not for system status. `Small` size only (no `Large` Promotion). No status icon system, no left border.

| Emphasis | Brand | Background | Text color | Used for |
|---|---|---|---|---|
| **Dark** | All | `var(--color-surface-100)` (black) | `var(--color-text-primary-inverted)` (white) | Neutral/brand-agnostic strong campaign banner. |
| **Light** | All | `var(--color-surface-raised-primary)` (white) | `var(--color-text-primary)` (black) | Neutral/brand-agnostic weak campaign banner. |
| **Strong** | Accent | `var(--color-accent-default)` (the concept brand's own accent — lime on Swedol) | `var(--color-text-action-accent)` (black on Swedol) | Strong commercial CTA in the brand's own accent color. |
| **Weak** | Accent | `var(--color-accent-light)` | `var(--color-text-action-primary)` (black) | Lighter version of the brand-accent banner. |

> **Brand Specific (Tools, Swedol, or Campaign Accent):** `Strong`/`Weak` always resolve through the concept brand's own `accent-default`/`accent-light` tokens — on Swedol that renders lime, on Tools it renders red. There is no separate "Tools" or "Swedol" emphasis option anymore; the same two tokens (`Strong`/`Weak`) automatically pick up the right brand color because `accent-default`/`accent-light` are themselves brand-scoped in `tokens.json`. Don't hardcode a brand-specific hex (e.g. `#cd1125`) for this — reference the accent tokens so the banner is correct on every concept brand's site.
> Content: centered, `Title -` (uppercase, `label-md`) + underlined `Till kampanjen`-style link (`body-md`), all in one line, `white-space: nowrap` on desktop.
> Padding: `12px` desktop / `8px` mobile (same as the `Small` status-banner padding table above). Height: `48px` desktop / `40px` mobile.

---

### Anatomy

**Small — Strong / Weak / Weaker (status banners):**
```
[2px border] [Status icon 24px] [TITLE (OPTIONAL): Body text...]   [✕ close 20px]
```
All three emphasis tiers share this same left-aligned anatomy — only background/border/text color change (see Emphasis table above).

**Large (any emphasis):**
```
[8px border] [Icon 48px] [Title — title-md]                        [✕ close 20px]
                          [Body text — body-md]
                          [Primary button] [Secondary/Blank button]
                          [Text link]
```

**Promotion (Small only):**
```
          [TITLE - Text link]                                      [✕ close 20px]
          ← whole background is the emphasis color, everything is centered →
```

- **Gap** icon–text: `12px` (Large desktop) / `8px` (Small). Gap title–link (Promotion): `4px`
- **Close button**: Blank xs, `close`-icon 20px, `padding: 2px`
- **Shadow**: `elevation-b-20` = `var(--shadow-elevation-b-20)`

---

### CSS template

```css
/* ---------- Small (status banners) ---------- */
.banner-notification {
  display: flex;
  align-items: stretch;
  width: 100%;
  box-shadow: var(--shadow-elevation-b-20);
}

.banner-notification__base {
  display: flex;
  align-items: center;
  width: 100%;
  overflow: hidden;
}

.banner-notification__left-border {
  width: 2px;
  align-self: stretch;
  flex-shrink: 0;
}

/* Weak's own edge — visually the same tone as the background, so it barely
   reads as a border; Weaker has no container border at all (see below). */
.banner-notification__container {
  flex: 1;
  border-width: 1px 1px 1px 0;
  border-style: solid;
}

.banner-notification__inner {
  display: flex;
  gap: 8px;
  align-items: flex-start;
  padding: 12px;
  width: 100%;
  box-sizing: border-box;
}

@media (max-width: 768px) {
  .banner-notification__inner { padding: 8px; }
}

.banner-notification__content {
  display: flex;
  gap: 8px;
  align-items: flex-start;
  flex: 1;
}

.banner-notification__icon {
  font-size: 24px;
  flex-shrink: 0;
  padding-top: 2px;
}

.banner-notification__text {
  flex: 1;
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 14px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: 0.28px;
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
}

.banner-notification__title {
  font-weight: 700;
  font-size: 14px;
  line-height: 14px;
  letter-spacing: 0.56px;
  text-transform: uppercase;
  font-feature-settings: 'ss02' 1, 'ss03' 1;
}

@media (max-width: 768px) {
  .banner-notification__text { font-size: 12px; line-height: 18px; letter-spacing: 0.24px; }
  .banner-notification__title { font-size: 12px; line-height: 12px; letter-spacing: 0.48px; }
}

.banner-notification__close {
  flex-shrink: 0;
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 2px;
  font-size: 20px;
}

/* Emphasis — Strong: solid status color, white text (this is the old
   "System Extra Strong" treatment, now just the top of the ladder) */
.banner-notification--strong.banner-notification--info    { background: var(--color-surface-information-default); }
.banner-notification--strong.banner-notification--error   { background: var(--color-surface-danger-default); }
.banner-notification--strong.banner-notification--success { background: var(--color-surface-success-default); }
.banner-notification--strong.banner-notification--warning { background: var(--color-surface-warning-default); }
.banner-notification--strong .banner-notification__text,
.banner-notification--strong .banner-notification__title,
.banner-notification--strong .banner-notification__icon,
.banner-notification--strong .banner-notification__close { color: var(--color-text-primary-inverted); }

.banner-notification--strong.banner-notification--info    .banner-notification__left-border { background: var(--color-surface-information-weaker); }
.banner-notification--strong.banner-notification--error   .banner-notification__left-border { background: var(--color-surface-danger-weaker); }
.banner-notification--strong.banner-notification--success .banner-notification__left-border { background: var(--color-surface-success-weaker); }
.banner-notification--strong.banner-notification--warning .banner-notification__left-border { background: var(--color-surface-warning-weaker); }

/* Emphasis — Weak: weaker-tinted background, colored left border + edge */
.banner-notification--weak.banner-notification--info    { background: var(--color-surface-information-weaker); }
.banner-notification--weak.banner-notification--error   { background: var(--color-surface-danger-weaker); }
.banner-notification--weak.banner-notification--success { background: var(--color-surface-success-weaker); }
.banner-notification--weak.banner-notification--warning { background: var(--color-surface-warning-weaker); }
.banner-notification--weak .banner-notification__text,
.banner-notification--weak .banner-notification__title,
.banner-notification--weak .banner-notification__close { color: var(--color-text-primary); }

.banner-notification--weak.banner-notification--info    .banner-notification__left-border { background: var(--color-surface-information-default); }
.banner-notification--weak.banner-notification--error   .banner-notification__left-border { background: var(--color-surface-danger-default); }
.banner-notification--weak.banner-notification--success .banner-notification__left-border { background: var(--color-surface-success-default); }
.banner-notification--weak.banner-notification--warning .banner-notification__left-border { background: var(--color-surface-warning-default); }

.banner-notification--weak.banner-notification--info    .banner-notification__container { border-color: var(--color-surface-information-weaker); }
.banner-notification--weak.banner-notification--error   .banner-notification__container { border-color: var(--color-surface-danger-weaker); }
.banner-notification--weak.banner-notification--success .banner-notification__container { border-color: var(--color-surface-success-weaker); }
.banner-notification--weak.banner-notification--warning .banner-notification__container { border-color: var(--color-surface-warning-weaker); }
.banner-notification--weak.banner-notification--info    .banner-notification__icon { color: var(--color-text-information-default); }
.banner-notification--weak.banner-notification--error   .banner-notification__icon { color: var(--color-text-danger-default); }
.banner-notification--weak.banner-notification--success .banner-notification__icon { color: var(--color-text-success); }
.banner-notification--weak.banner-notification--warning .banner-notification__icon { color: var(--color-border-warning-default); }

/* Emphasis — Weaker: white background, colored left border only, no edge */
.banner-notification--weaker { background: var(--color-surface-raised-primary); }
.banner-notification--weaker .banner-notification__container { border: none; }
.banner-notification--weaker .banner-notification__text,
.banner-notification--weaker .banner-notification__title,
.banner-notification--weaker .banner-notification__close { color: var(--color-text-primary); }
.banner-notification--weaker.banner-notification--info    .banner-notification__left-border { background: var(--color-surface-information-default); }
.banner-notification--weaker.banner-notification--error   .banner-notification__left-border { background: var(--color-surface-danger-default); }
.banner-notification--weaker.banner-notification--success .banner-notification__left-border { background: var(--color-surface-success-default); }
.banner-notification--weaker.banner-notification--warning .banner-notification__left-border { background: var(--color-surface-warning-default); }
.banner-notification--weaker.banner-notification--info    .banner-notification__icon { color: var(--color-text-information-default); }
.banner-notification--weaker.banner-notification--error   .banner-notification__icon { color: var(--color-text-danger-default); }
.banner-notification--weaker.banner-notification--success .banner-notification__icon { color: var(--color-text-success); }
.banner-notification--weaker.banner-notification--warning .banner-notification__icon { color: var(--color-border-warning-default); }

/* ---------- Large (rich My Pages banner) ---------- */
.banner-notification--large {
  display: flex;
  align-items: stretch;
  width: 100%;
  box-shadow: var(--shadow-elevation-b-20);
}
.banner-notification--large .banner-notification__left-border { width: 8px; }
@media (max-width: 1023px) {
  .banner-notification--large .banner-notification__left-border { width: 4px; }
}

.banner-notification--large .banner-notification__inner {
  gap: 12px;
  padding: 24px;
  flex-direction: column;
}
@media (max-width: 768px) {
  .banner-notification--large .banner-notification__inner { padding: 16px; }
}
@media (max-width: 639px) {
  .banner-notification--large .banner-notification__inner { padding: 12px 12px 16px; }
}

.banner-notification--large .banner-notification__icon-text {
  display: flex;
  gap: 12px;
  align-items: flex-start;
  width: 100%;
}
@media (max-width: 639px) {
  .banner-notification--large .banner-notification__icon-text { gap: 8px; }
}

.banner-notification--large .banner-notification__icon { font-size: 48px; padding-top: 0; }
@media (max-width: 768px) { .banner-notification--large .banner-notification__icon { font-size: 40px; } }
@media (max-width: 639px) { .banner-notification--large .banner-notification__icon { font-size: 24px; } }

.banner-notification--large .banner-notification__heading {
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 20px;
  font-weight: 700;
  line-height: 24px;
  letter-spacing: 0px;
  font-feature-settings: 'ss02' 1, 'ss03' 1;
}
@media (max-width: 768px) {
  .banner-notification--large .banner-notification__heading { font-size: 18px; line-height: 22px; }
}

.banner-notification--large .banner-notification__body {
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 24px;
  letter-spacing: 0.32px;
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
  margin-top: 12px;
}
@media (max-width: 768px) {
  .banner-notification--large .banner-notification__body { line-height: 22px; margin-top: 8px; }
}

.banner-notification--large .banner-notification__footer {
  padding-left: 60px;
  padding-top: 24px;
  width: 100%;
  box-sizing: border-box;
}
@media (max-width: 768px) { .banner-notification--large .banner-notification__footer { padding-left: 52px; } }
@media (max-width: 639px) { .banner-notification--large .banner-notification__footer { padding-left: 32px; } }

.banner-notification--large .banner-notification__btn-group {
  display: flex;
  gap: 8px;
  align-items: center;
}

.banner-notification--large .banner-notification__link {
  display: block;
  margin-top: 8px;
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 16px;
  line-height: 24px;
  letter-spacing: 0.32px;
  text-decoration: underline;
}
@media (max-width: 768px) {
  .banner-notification--large .banner-notification__link { font-size: 14px; line-height: 22px; letter-spacing: 0.42px; }
}

/* ---------- Promotion (Small only) ---------- */
.banner-notification--promotion {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 48px;
  padding: 8px;
  gap: 8px;
  box-sizing: border-box;
  box-shadow: var(--shadow-elevation-b-20);
}
@media (max-width: 768px) { .banner-notification--promotion { height: 40px; } }

.banner-notification--promotion .banner-notification__title {
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 18px;   /* label-md */
  font-weight: 700;
  line-height: 18px;
  letter-spacing: 0.18px;
  text-transform: uppercase;
  white-space: nowrap;
}

.banner-notification--promotion .banner-notification__link {
  font-size: 18px;   /* body-md */
  font-weight: 400;
  line-height: 18px;
  letter-spacing: 0.32px;
  text-decoration: underline;
  white-space: nowrap;
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
}

/* Promotion emphasis colors */
.banner-notification--promotion.banner-notification--dark  { background: var(--color-surface-100); color: var(--color-text-primary-inverted); }
.banner-notification--promotion.banner-notification--light { background: var(--color-surface-raised-primary); color: var(--color-text-primary); }
.banner-notification--promotion.banner-notification--promo-strong { background: var(--color-accent-default); color: var(--color-text-action-accent); }
.banner-notification--promotion.banner-notification--promo-weak   { background: var(--color-accent-light); color: var(--color-text-action-primary); }
```

### HTML example (Small, Informational, Weak)

```html
<div class="banner-notification banner-notification--info banner-notification--weak">
  <div class="banner-notification__base">
    <div class="banner-notification__left-border"></div>
    <div class="banner-notification__container">
      <div class="banner-notification__inner">
        <div class="banner-notification__content">
          <span class="material-symbols-outlined banner-notification__icon">info</span>
          <p class="banner-notification__text">
            <span class="banner-notification__title">Title (optional):</span> Body text.
          </p>
        </div>
        <button class="banner-notification__close" aria-label="Close">
          <span class="material-symbols-outlined">close</span>
        </button>
      </div>
    </div>
  </div>
</div>
```

### HTML example (Small, Informational, Strong — replaces the old "System Extra Strong")

```html
<div class="banner-notification banner-notification--info banner-notification--strong">
  <div class="banner-notification__base">
    <div class="banner-notification__left-border"></div>
    <div class="banner-notification__container">
      <div class="banner-notification__inner">
        <div class="banner-notification__content">
          <span class="material-symbols-outlined banner-notification__icon">info</span>
          <p class="banner-notification__text">
            Your role is <span class="banner-notification__title">Administrator</span>
            and you're temporarily acting as <strong>Alban Beluli</strong>.
          </p>
        </div>
        <button class="banner-notification__close" aria-label="Close">
          <span class="material-symbols-outlined">close</span>
        </button>
      </div>
    </div>
  </div>
</div>
```

### HTML example (Large, Informational, Strong — My Pages dashboard)

```html
<div class="banner-notification banner-notification--large banner-notification--info banner-notification--strong">
  <div class="banner-notification__left-border"></div>
  <div class="banner-notification__inner">
    <div class="banner-notification__icon-text">
      <span class="material-symbols-outlined banner-notification__icon">nest_eco_leaf</span>
      <div>
        <p class="banner-notification__heading">We've gone paperless with invoices</p>
        <p class="banner-notification__body">
          Invoices are always included as attachments with your delivery confirmation email. You can also download them from your order history. If you'd rather receive printed invoices, you can change this under "Invoice methods" in your
          <a href="#" class="banner-notification__link" style="display:inline; margin:0;">address book</a>.
        </p>
      </div>
    </div>
    <div class="banner-notification__footer">
      <div class="banner-notification__btn-group">
        <button class="btn btn--primary btn--xs">Go to cart</button>
        <button class="btn btn--blank btn--xs">Choose accessories</button>
      </div>
      <a href="#" class="banner-notification__link">Text link</a>
    </div>
  </div>
  <button class="banner-notification__close" aria-label="Close">
    <span class="material-symbols-outlined">close</span>
  </button>
</div>
```

### HTML example (Promotion, Strong, Accent)

```html
<div class="banner-notification banner-notification--promotion banner-notification--promo-strong">
  <p class="banner-notification__title">Campaign title - <a href="#" class="banner-notification__link">View campaign</a></p>
  <button class="banner-notification__close" aria-label="Close">
    <span class="material-symbols-outlined">close</span>
  </button>
</div>
```

---
