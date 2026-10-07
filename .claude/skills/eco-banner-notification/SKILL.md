---
name: eco-banner-notification
description: Use when building a page-wide banner notification at the top of the page (maintenance/outage/campaign) or a rich My Pages dashboard banner — Size Small/Large, Emphasis Strong/Weak/Weaker per status, and Promotion (Dark/Light/Strong/Weak) for brand campaigns.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

> **Buttons and ×:** buttons and the close button follow `eco-button` (see `notifications-guide`, "Buttons and the close button"): `btn btn--primary|secondary|blank` with `<span class="btn__label">`, always 32px (XSmall from 769px, Small below), and the × is `icon-btn icon-btn--close` (`icon-btn--close-inverted` on dark/solid surfaces). Live CSS: `eco-design-system/notifications.css`.

> **Close (×) motion:** the × fades the banner out and collapses its height (no empty gap). Recommended: `--ease-accelerate-generic`, `--duration-fast-3`, collapse on; override with `--n-close-ease`, `--n-close-duration` or `data-n-close="fade"`. Details in `notifications-guide` ("Motion when a Banner or Inline closes"). The markup builder (`ECO_N.html`) takes `closable: false` to leave the × out.

> **Custom icon (Informational only):** the author may replace the default `info` icon with another from the gallery. The author enters the Google Material Symbols name; it renders as **Outlined, Fill 0, Weight 300, Grade 0** (`font-variation-settings: 'FILL' 0, 'wght' 300, 'GRAD' 0`, class `icon-outline`); the default status icons stay filled. See `notifications-guide`.

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
| **Large** | A richer banner with a big icon, heading, body copy, action buttons **or** inline links. **Exclusive to My Pages** — appears at the top of the dashboard after sign-in, directed at a specific signed-in customer or customer group. `Small` variants may also target a specific signed-in customer/group, but `Large` is only available in signed-in mode. |

**Inline link (Small, status banners):** optional, set by the banner's author. One or more Inline Links of the Small Bold type (`body-sm` 14/20, 0.36px, weight 600, `inline-link--small inline-link--bold`) sit on the right of the text, before the ×, with an 8px gap, `padding-top: 2px`, at every breakpoint (Figma `13377:42164`, `13377:42182`). The label is whatever the author writes (Figma shows "LOGGA UT"): the link never forces uppercase. Text Primary on Weak/Weaker, Text Primary Inverted on Strong. Markup: `<div class="banner-notification__links"><a href="#" class="inline-link inline-link--small inline-link--bold">Log out</a></div>` inside `.banner-notification__content`, after the text.

Both sizes take the full width of their container (`width: 100%`). No fixed width is set.

#### Small — layout per breakpoint

| Property | Desktop (`md:` 769px+) | Mobile/Tablet (`xs`/`sm` ≤768px) |
|---|---|---|
| Height | `48px` (`min-height`) | `40px` (`min-height`) |
| Padding | `12px` top/bottom, `16px` left/right | `8px` top/bottom, `16px` left/right |
| Icon | 24px | 24px |
| Left border width | `2px` | `2px` |
| Title text | `label-sm` Desktop: 14px, 0.56px, Bold, uppercase | `label-sm` Mobile: 12px, 0.48px, Bold, uppercase |
| Body text | `body-sm` Desktop: 14px/20px, 0.36px, Regular | Mobile: 12px/18px, 0.24px, Regular |

#### Large — layout per breakpoint

| Property | Desktop (`md:` 769px+, `1200px` symbol) | Tablet (`sm:` 640–768px, `768px` symbol) | Mobile (`xs:` 0–639px, `375px` symbol) |
|---|---|---|---|
| Content padding | `24px` | `16px` | `12px` top, `12px` sides, `16px` bottom |
| Left border width | `8px` | `4px` | `4px` |
| Icon | `48px` | `40px` | `24px` |
| Gap icon → text | `12px` | `12px` | `8px` |
| Gap title → body | `12px` | `8px` | `8px` |
| Title (`title-md`) | 20px/24px, 0px, Bold | 18px/22px, 0px, Bold (mobile scale) | 18px/22px, 0px, Bold (mobile scale) |
| Body (`body-md`) | 17px/24px, 0.32px, Regular | 16px/22px, 0.32px, Regular (mobile scale) | 16px/22px, 0.32px, Regular (mobile scale) |
| Footer indent (`padding-left`, aligns under text) | `60px` (= icon 48 + gap 12) | `52px` (= icon 40 + gap 12) | `32px` (= icon 24 + gap 8) |
| Space body → action area | **`24px` at every breakpoint**, and only that: the footer's `padding-top: 24px` is the one space under the body, the container has **no** `gap` of its own (`gap: 0`) | same | same |
| Button group | `gap-8px`, buttons are 32px high (XSmall desktop, Small below) | same | same |
| Button text | `label-sm` desktop: 14px/14px, 0.56px | `label-sm` mobile: 12px/12px, 0.48px | `label-sm` mobile: 12px/12px, 0.48px |
| Inline links (instead of the buttons; `.banner-notification__links`, 8px / 16px gap) | `body-md` 17px/24px, 0.32px, underline | `body-md` mobile scale | `body-md` mobile scale |

> **Large** always shows a status icon (48/40/24px), a `title-md` heading, `body-md` body copy, and a `Notification / Section / Footer - Call to Action` action group (Secondary + Blank buttons, **or** inline links; no Primary button in Figma) — see Anatomy below. This is a heavier content contract than `Small`; don't use `Large` for a simple one-line status message.

---

### Variants

#### Emphasis — status banners (Informational / Success / Warning / Error)

Three tiers, same ladder for both `Small` and `Large` (only the left-border width and padding scale differ per Size — see tables above):

| Emphasis | Background | Left border | Other borders | Text color |
|---|---|---|---|---|
| **Strong** | `var(--color-surface-{status}-default)` (solid status color) | `var(--color-surface-{status}-weaker)` | none (`Large`: `1px solid var(--color-border-{status}-default)`, same tone as bg) | `var(--color-text-primary-inverted)` (white) |
| **Weak** | `var(--color-surface-{status}-weaker)` | `var(--color-surface-{status}-default)` | `1px solid var(--color-border-{status}-weaker)` (same tone as bg). Figma's tablet Large uses `border-{status}-weak` — likely a Figma inconsistency, `-weaker` used at every breakpoint. | `var(--color-text-primary)` (black) |
| **Weaker** | `var(--color-surface-raised-primary)` (white) | `var(--color-surface-{status}-default)` | none | `var(--color-text-primary)` (black) |

`{status}` = `information` / `success` / `warning` / `danger` (Error uses the `danger` token family).

> **Shadow (Figma 2026-10):** **every banner has `elevation-b-20` by default**: Small and Large, all emphasis tiers, and Promotion. Set it once on `.banner-notification`.

> **Strong is the old `System Extra Strong`.** The solid-color, white-text, high-priority treatment (e.g. admin impersonation — "Din roll är ADMINISTRATÖR och du agerar tillfälligt som [namn]") now lives at `Strong` emphasis, left-aligned like every other tier — it's no longer a separate centered variant. If you're migrating old markup that used a centered `.banner-notification--extra-strong` layout, switch it to the standard left-aligned `Strong` layout (see CSS template below); centering is no longer part of the spec.

#### Status + colors

| Status | Strong background | Weak background | Weaker left-border / Strong left-border-accent | Icon | Material Symbol |
|---|---|---|---|---|---|
| **Informational** | `var(--color-surface-information-default)` | `var(--color-surface-information-weaker)` | `var(--color-surface-information-default)` / `var(--color-surface-information-weaker)` | `var(--color-text-information-default)` | `info` |
| **Error** | `var(--color-surface-danger-default)` | `var(--color-surface-danger-weaker)` | `var(--color-surface-danger-default)` / `var(--color-surface-danger-weaker)` | `var(--color-text-danger-default)` | `error` |
| **Success** | `var(--color-surface-success-default)` | `var(--color-surface-success-weaker)` | `var(--color-surface-success-default)` / `var(--color-surface-success-weaker)` | `var(--color-text-success-default)` | `check_circle` |
| **Warning** | `var(--color-surface-warning-default)` | `var(--color-surface-warning-weaker)` | `var(--color-surface-warning-default)` / `var(--color-surface-warning-weaker)` | `var(--color-border-warning-default)` (no dedicated `text-warning` token) | `warning` |

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
> **Desktop (769px+):** content centered: `Title -` (uppercase, `label-md` 18/18, 0.18px) + underlined `Till kampanjen`-style Inline Link (`body-md` 17/24, 0.32px), all in one line, `white-space: nowrap`; padding `12px` top/bottom and `8px` sides (plus room for the ×), height `48px`, × shown.
> **Mobile / tablet (below 769px, Figma Small-XSmall, 32px):** a different layout: padding `8px`, height `32px`, **title on the left** (`label-md` 14/16, 0.42px, uppercase, no trailing dash) and the **link on the right** (Inline Link `body-sm` 14/16, 0.36px, `white-space: nowrap`), 12px gap, **no ×** in Figma. The link is an Inline Link (`eco-inline-link`): underlined, underline removed on hover; on `Dark` it is Text Primary Inverted, on the brand-accent emphasis it keeps the surface text color (no hover token, confirm with design). Never uppercase. **The whole Promotion banner is clickable:** the link's `::after` is stretched over the banner (`position: absolute; inset: 0`, banner `position: relative`, × `z-index: 1` above it), and `.banner-notification--promotion:hover .inline-link` gives the link its hover (underline removed, hover color), so hovering anywhere shows the effect. Keyboard focus on the link draws the focus ring around the banner (`outline-offset: -4px`; confirm the offset with design).

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
                          [Secondary button] [Blank button]
                          [Inline link] [Inline link]   ← instead of the buttons
```

**Promotion (Small only):**
```
Desktop:  [      TITLE - Inline link (centered)      ]  [✕ close 20px]
Mobile:   [TITLE (left)                  Inline link]     ← no ×, 32px high
          ← whole background is the emphasis color →
```

- **Gap** icon–text: `12px` (Large desktop) / `8px` (Small). Gap title–link (Promotion): a space on desktop, `12px` on mobile
- **Close button**: Blank xs, `close`-icon 20px, `padding: 2px`
- **Shadow**: `elevation-b-20` = `var(--shadow-elevation-b-20)` on every banner (all sizes and tiers)

---

### CSS template

```css
/* ---------- Small (status banners) ---------- */
.banner-notification {
  display: flex;
  align-items: stretch;
  width: 100%;
  box-shadow: var(--shadow-elevation-b-20);  /* every banner */
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
  /* the 1px edge (Weak) is an inset shadow so it takes no room: padding stays 12px / 16px, height 48px (40px mobile) */
  --edge: transparent;
  box-shadow: inset 0 1px 0 var(--edge), inset -1px 0 0 var(--edge), inset 0 -1px 0 var(--edge);
}

.banner-notification__inner {
  display: flex;
  gap: 8px;
  align-items: flex-start;
  padding: 12px 16px;
  width: 100%;
  box-sizing: border-box;
}

@media (max-width: 768px) {
  .banner-notification__inner { padding: 8px 16px; }
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
  font-variation-settings: 'FILL' 1, 'wght' 300, 'GRAD' 0, 'opsz' 24;  /* Filled, wght 300: without this a plain Material Symbols span renders outline */
}

.banner-notification__text {
  flex: 1;
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 14px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: 0.36px;
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
}

.banner-notification__title {
  font-weight: 600;
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



/* Emphasis — Strong: solid status color, white text (this is the old
   "System Extra Strong" treatment, now just the top of the ladder) */
.banner-notification--strong.banner-notification--info    { background: var(--color-surface-information-default); }
.banner-notification--strong.banner-notification--error   { background: var(--color-surface-danger-default); }
.banner-notification--strong.banner-notification--success { background: var(--color-surface-success-default); }
.banner-notification--strong.banner-notification--warning { background: var(--color-surface-warning-default); }
.banner-notification--strong .banner-notification__text,
.banner-notification--strong .banner-notification__title,
.banner-notification--strong .banner-notification__icon { color: var(--color-text-primary-inverted); }

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

.banner-notification--weak.banner-notification--info    .banner-notification__left-border { background: var(--color-surface-information-default); }
.banner-notification--weak.banner-notification--error   .banner-notification__left-border { background: var(--color-surface-danger-default); }
.banner-notification--weak.banner-notification--success .banner-notification__left-border { background: var(--color-surface-success-default); }
.banner-notification--weak.banner-notification--warning .banner-notification__left-border { background: var(--color-surface-warning-default); }

.banner-notification--weak.banner-notification--info    .banner-notification__container { --edge: var(--color-border-information-weaker); }
.banner-notification--weak.banner-notification--error   .banner-notification__container { --edge: var(--color-border-danger-weaker); }
.banner-notification--weak.banner-notification--success .banner-notification__container { --edge: var(--color-border-success-weaker); }
.banner-notification--weak.banner-notification--warning .banner-notification__container { --edge: var(--color-border-warning-weaker); }
.banner-notification--weak.banner-notification--info    .banner-notification__icon { color: var(--color-text-information-default); }
.banner-notification--weak.banner-notification--error   .banner-notification__icon { color: var(--color-text-danger-default); }
.banner-notification--weak.banner-notification--success .banner-notification__icon { color: var(--color-text-success-default); }
.banner-notification--weak.banner-notification--warning .banner-notification__icon { color: var(--color-border-warning-default); }

/* Emphasis — Weaker: white background, colored left border only, no edge */
.banner-notification--weaker { background: var(--color-surface-raised-primary); box-shadow: var(--shadow-elevation-b-20); }

.banner-notification--weaker .banner-notification__text,
.banner-notification--weaker .banner-notification__title,
.banner-notification--weaker.banner-notification--info    .banner-notification__left-border { background: var(--color-surface-information-default); }
.banner-notification--weaker.banner-notification--error   .banner-notification__left-border { background: var(--color-surface-danger-default); }
.banner-notification--weaker.banner-notification--success .banner-notification__left-border { background: var(--color-surface-success-default); }
.banner-notification--weaker.banner-notification--warning .banner-notification__left-border { background: var(--color-surface-warning-default); }
.banner-notification--weaker.banner-notification--info    .banner-notification__icon { color: var(--color-text-information-default); }
.banner-notification--weaker.banner-notification--error   .banner-notification__icon { color: var(--color-text-danger-default); }
.banner-notification--weaker.banner-notification--success .banner-notification__icon { color: var(--color-text-success-default); }
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
  gap: 0;              /* the footer's 24px padding-top is the only space under the body */
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
  font-weight: 600;
  line-height: 24px;
  letter-spacing: 0px;
  font-feature-settings: 'ss02' 1, 'ss03' 1;
}
@media (max-width: 768px) {
  .banner-notification--large .banner-notification__heading { font-size: 18px; line-height: 22px; }
}

.banner-notification--large .banner-notification__body {
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 17px;          /* body-md desktop; 16px/22px below 769px */
  font-weight: 400;
  line-height: 24px;
  letter-spacing: 0.32px;
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
  margin-top: 12px;
}
@media (max-width: 768px) {
  .banner-notification--large .banner-notification__body { font-size: 16px; line-height: 22px; margin-top: 8px; }
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
/* Mobile (below 769px, Figma Small-XSmall): 32px, title left, link right, no × */
.banner-notification--promotion {
  position: relative;
  align-items: center;
  width: 100%;
  min-height: 32px;
  padding: 8px;
  box-sizing: border-box;
  box-shadow: var(--shadow-elevation-b-20);
}
.banner-notification__promo { display: flex; align-items: center; gap: 12px; width: 100%; margin: 0; }
.banner-notification--promotion .banner-notification__title {
  flex: 1;
  text-align: left;
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 14px;   /* label-md, mobile */
  font-weight: 600;
  line-height: 16px;
  letter-spacing: 0.42px;
  text-transform: uppercase;
}
.banner-notification--promotion .inline-link {   /* eco-inline-link, body-sm on mobile */
  flex-shrink: 0;
  white-space: nowrap;
  font-size: 14px;
  line-height: 16px;
  letter-spacing: 0.36px;
}
.banner-notification--promotion .icon-btn { display: none; }

/* Desktop: 48px, centered "Title - Link", × shown */
@media (min-width: 769px) {
  .banner-notification--promotion { min-height: 48px; padding: 12px 48px; }
  .banner-notification__promo { display: block; text-align: center; }
  .banner-notification--promotion .banner-notification__title { display: inline; font-size: 18px; line-height: 18px; letter-spacing: 0.18px; }  /* label-md */
  .banner-notification--promotion .banner-notification__title::after { content: ' -'; }
  .banner-notification--promotion .inline-link { font-size: 17px; line-height: 24px; letter-spacing: 0.32px; }  /* body-md */
  .banner-notification--promotion .icon-btn { display: inline-flex; position: absolute; right: 16px; top: 50%; transform: translateY(-50%); }
}

/* Promotion emphasis colors */
.banner-notification--promotion.banner-notification--dark  { background: var(--color-surface-100); color: var(--color-text-primary-inverted); }
.banner-notification--promotion.banner-notification--light { background: var(--color-surface-raised-primary); color: var(--color-text-primary); }
.banner-notification--promotion.banner-notification--promo-strong { background: var(--color-accent-default); color: var(--color-text-action-accent); }
.banner-notification--promotion.banner-notification--promo-weak   { background: var(--color-accent-light); color: var(--color-text-action-primary); }

/* Buttons and ×: eco-button classes (.btn, .icon-btn.icon-btn--close); live CSS in eco-design-system/notifications.css */
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
        <button type="button" class="icon-btn icon-btn--close" aria-label="Close"><span class="btn__icon" aria-hidden="true">close</span></button>
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
        <button type="button" class="icon-btn icon-btn--close icon-btn--close-inverted" aria-label="Close"><span class="btn__icon" aria-hidden="true">close</span></button>
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
        <button type="button" class="btn btn--secondary-inverted"><span class="btn__label">Go to cart</span></button>
        <button type="button" class="btn btn--blank-inverted"><span class="btn__label">Choose accessories</span></button>
      </div>
      <a href="#" class="banner-notification__link">Text link</a>
    </div>
  </div>
  <button type="button" class="icon-btn icon-btn--close icon-btn--close-inverted" aria-label="Close"><span class="btn__icon" aria-hidden="true">close</span></button>
</div>
```

### HTML example (Promotion, Strong, Accent)

```html
<div class="banner-notification banner-notification--promotion banner-notification--promo-strong">
  <p class="banner-notification__promo"><span class="banner-notification__title">Campaign title</span> <a href="#" class="inline-link inline-link--medium">View campaign</a></p>
  <button type="button" class="icon-btn icon-btn--close" aria-label="Close"><span class="btn__icon" aria-hidden="true">close</span></button>
</div>
```

---

---

### Placement and priority (Figma "Use Case Matrix", node 23586-56956)

Banners are configured by an administrator per banner. Settings per page type:

| Page | Banner size | Placement | Other settings (all pages) |
|---|---|---|---|
| **PDP** | Small | Beneath the breadcrumb | SNI code(s), customer ID(s), date from – to (yes/no) |
| **PLP** | Small | Beneath the breadcrumb | same |
| **My pages** | **Large** | In the context of the dashboard (on top of it) | same |
| **All pages** | Small | **Header top** (directly above the site header) or **Header bottom** (directly below it) | same |

**Priority** decides which banner shows when several match the same visitor and place (the creator labels each banner with one):
0. **Opt-out** (a specific company has chosen to see no banners at all): a company-level setting, not a banner. It **overrides every other level, alerts included**, so nothing is shown to that company's users. Confirm with product whether a critical outage alert should be able to break through.
1. **Alert** (Error / Warning / Success / Information)
2. **Customer specific** (customer ID)
3. **SNI** (code)
4. **Default**

The SNI level (3) is the industry-code level: **Norway and Finland use their own country's equivalent of SNI where one exists** (for example SN2007 in Norway, TOL 2008 in Finland), entered in the same field as the Swedish SNI code.

Only the highest-priority matching level counts: if the company has opted out, no banner is shown; otherwise the highest-priority matching banner is shown. Live demo of both rules: `eco-design-system/components/banner.html` (section "Placement and priority").
