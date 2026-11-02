# Banner notification: CSS template

## Contents

- Small (status banners)
- Large (rich My Pages banner)
- Promotion (Small only)

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
/* Mobile (below 769px): 32px, title left, link and × right (× added 2026-10) */
.banner-notification--promotion {
  position: relative;
  align-items: center;
  width: 100%;
  min-height: 32px;
  padding: 4px 8px;            /* the 24px × plus 4px + 4px keeps 32px */
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
.banner-notification--promotion { gap: 8px; }   /* mobile: title, link and × in one row */

/* Desktop: 48px, centered "Title - Link", × shown */
@media (min-width: 769px) {
  .banner-notification--promotion { min-height: 48px; padding: 12px 48px; }
  .banner-notification__promo { display: block; text-align: center; }
  .banner-notification--promotion .banner-notification__title { display: inline; font-size: 18px; line-height: 18px; letter-spacing: 0.18px; }  /* label-md */
  .banner-notification--promotion .banner-notification__title::after { content: ' -'; }
  .banner-notification--promotion .inline-link { font-size: 17px; line-height: 24px; letter-spacing: 0.32px; }  /* body-md */
  .banner-notification--promotion { gap: 0; }
  .banner-notification--promotion .icon-btn { position: absolute; right: 16px; top: 50%; transform: translateY(-50%); }
}

/* Promotion emphasis colors */
.banner-notification--promotion.banner-notification--dark  { background: var(--color-surface-100); color: var(--color-text-primary-inverted); }
.banner-notification--promotion.banner-notification--light { background: var(--color-surface-raised-primary); color: var(--color-text-primary); }
.banner-notification--promotion.banner-notification--promo-strong { background: var(--color-accent-default); color: var(--color-text-action-accent); }
.banner-notification--promotion.banner-notification--promo-weak   { background: var(--color-accent-light); color: var(--color-text-action-primary); }

/* Buttons and ×: eco-button classes (.btn, .icon-btn.icon-btn--close); live CSS in eco-design-system/notifications.css */
```
