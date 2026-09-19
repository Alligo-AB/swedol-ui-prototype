---
name: eco-typography
description: Use when choosing or reviewing typography/text styles (Body, Alt-Label, Label, Title, Headline, Display) on Desktop vs. Mobile per the ECO Design System.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

> **Source:** Size/Line-height/Letter-spacing in the tables below are pulled from `tokens.json` (the `eco-tokens` skill), not hardcoded. Typography tokens have no CSS `var(--...)` in the package (JS values only, see `eco-tokens`) — the numbers here are the actual source to write CSS against, not a standalone copy.
>
> **Known discrepancies, not changed here — require confirmation before changing in code:**
> - **`display-lg` on mobile** is `66px/60px` in the live package (same as desktop) — the table below keeps `36px/34px` as the documented value since `66px` is likely an unintentional Supernova export bug (a 66px heading at 375px width would be broken). Confirm with design before either value is used.
> - **Font-weight** for Body (documented as 400) and Alt-Label (documented as 500) differs from `tokens.json` (500 and 600 respectively) — not changed here, flag for confirmation before changing the weight in code, since it affects already-built pages.

## Typography – Desktop Base Styling (ECO Design System)

Applies to **Desktop Small (`md:`, 769px+) and Desktop (`lg:`, 1024px+)**.
Font: `Breuer Condensed`, sans-serif. `font-feature-settings: 'ss02' 1, 'ss03' 1` applies to all styles.

### Body

| Token | Name | Size | Line-height | Letter-spacing | Weight | Paragraph-spacing |
|---|---|---|---|---|---|---|
| `body-sm` | Body Small | 14px | 20px | 0.28px | 400 | 12px |
| `body-md` | Body Medium | 16px | 22px | 0.32px | 400 | 16px |
| `body-lg` | Body Large | 20px | 28px | 0px | 400 | 20px |
| `body-xl` | Body XLarge | 24px | 32px | 0px | 400 | 24px |

> Body is used for longer text passages. `body-xl` suits shorter intro text.

### Alt-Label (alternative labels, uppercase)

| Token | Name | Size | Line-height | Letter-spacing | Weight |
|---|---|---|---|---|---|
| `alt-label-sm` | Alt-Label Small | 14px | 14px | 0.56px | 500 |
| `alt-label-md` | Alt-Label Medium | 16px | 16px | 0.64px | 500 |
| `alt-label-lg` | Alt-Label Large | 18px | 18px | 0.36px | 500 |

> Alt-Label: `text-transform: uppercase`. Used for labeling form fields and UI components.

### Label (bold labels, uppercase)

| Token | Name | Size | Line-height | Letter-spacing | Weight |
|---|---|---|---|---|---|
| `label-sm` | Label Small | 14px | 14px | 0.56px | 600 |
| `label-md` | Label Medium | 16px | 16px | 0.48px | 600 |
| `label-lg` | Label Large | 18px | 18px | 0.18px | 600 |

> Label: `text-transform: uppercase`. A bolder version of Alt-Label. Used in buttons, forms, and UI components.

### Title (headings, normal case)

| Token | Name | Size | Line-height | Letter-spacing | Weight |
|---|---|---|---|---|---|
| `title-sm` | Title Small | 16px | 22px | 0px | 600 |
| `title-md` | Title Medium | 20px | 24px | 0px | 600 |
| `title-lg` | Title Large | 24px | 28px | 0px | 600 |

> Title: shorter, medium-strength text. Used for secondary headings and smaller H-tags.

### Headline (primary headings, normal case)

| Token | Name | Size | Line-height | Letter-spacing | Weight |
|---|---|---|---|---|---|
| `headline-sm` | Headline Small | 28px | 32px | 0px | 600 |
| `headline-md` | Headline Medium | 32px | 36px | 0px | 600 |
| `headline-lg` | Headline Large | 36px | 40px | 0px | 600 |
| `headline-xl` | Headline XLarge | 46px | 48px | 0px | 600 |

> Headline: short, high-emphasis text. Primary text passages and important content regions. `headline-xl` suits H1 content (not in combination with `display-lg`).

### Display (campaign/hero, uppercase)

| Token | Name | Size | Line-height | Letter-spacing | Weight |
|---|---|---|---|---|---|
| `display-sm` | Display Small | 26px | 26px | 0px | 600 |
| `display-md` | Display Medium | 36px | 36px | 0px | 600 |
| `display-lg` | Display Large | 66px | 66px | 0px | 600 |

> Display: `text-transform: uppercase`. Reserved for hero banners, campaign headlines, and numerals. Use sparingly. `display-lg` = H1 on a page/article (never together with `headline-xl`).

### Modified Styles (modified variants)

| Token | Base | Change | Usage |
|---|---|---|---|
| `label-lg--badge` | `label-sm` | 14px, 0.56px, 600, normal case | Badge component |
| `label-sm--badge` | `label-sm` | 12px, 0.48px, 600, normal case | Small badge |
| `label-lg--underline` | `label-lg` | + `text-decoration: underline` | Underlined label |

### CSS rule (Desktop Base)

```css
/* All typography styles share: */
font-family: 'Breuer Condensed', Arial, sans-serif;
font-style: normal;
font-feature-settings: 'ss02' 1, 'ss03' 1;

/* Alt-Label and Label add: */
text-transform: uppercase;

/* Display adds: */
text-transform: uppercase;
font-feature-settings: 'ss02' 1, 'ss03' 1; /* not 'ss06' */
```

---

## Typography – Mobile Base Styling (ECO Design System)

Applies to **Mobile (`xs`, 0–639px) and Tablet (`sm`, 640–768px)**.
Font: `Breuer Condensed`, sans-serif. `font-feature-settings: 'ss02' 1, 'ss03' 1` applies to all styles.

### Body

| Token | Name | Size | Line-height | Letter-spacing | Weight | Paragraph-spacing |
|---|---|---|---|---|---|---|
| `body-sm` | Body Small | 14px | 20px | 0.28px | 400 | 12px |
| `body-md` | Body Medium | 16px | 22px | 0.32px | 400 | 16px |
| `body-lg` | Body Large | 18px | 26px | 0px | 400 | 16px |
| `body-xl` | Body XLarge | 20px | 26px | 0px | 400 | — |

> Body is used for longer text passages. `body-xl` suits shorter intro text.

### Alt-Label (alternative labels, uppercase)

| Token | Name | Size | Line-height | Letter-spacing | Weight |
|---|---|---|---|---|---|
| `alt-label-sm` | Alt-Label Small | 12px | 12px | 0.48px | 500 |
| `alt-label-md` | Alt-Label Medium | 14px | 14px | 0.56px | 500 |
| `alt-label-lg` | Alt-Label Large | 16px | 16px | 0.32px | 500 |

> Alt-Label: `text-transform: uppercase`. Used for labeling form fields and UI components.

### Label (bold labels, uppercase)

| Token | Name | Size | Line-height | Letter-spacing | Weight |
|---|---|---|---|---|---|
| `label-sm` | Label Small | 12px | 12px | 0.48px | 600 |
| `label-md` | Label Medium | 14px | 14px | 0.42px | 600 |
| `label-lg` | Label Large | 16px | 16px | 0.32px | 600 |

> Label: `text-transform: uppercase`. A bolder version of Alt-Label. Used in buttons, forms, and UI components.

### Title (headings, normal case)

| Token | Name | Size | Line-height | Letter-spacing | Weight |
|---|---|---|---|---|---|
| `title-sm` | Title Small | 16px | 22px | 0px | 600 |
| `title-md` | Title Medium | 18px | 24px | 0px | 600 |
| `title-lg` | Title Large | 20px | 24px | 0px | 600 |

> Title: shorter, medium-strength text. Used for secondary headings and smaller H-tags.

### Headline (primary headings, normal case)

| Token | Name | Size | Line-height | Letter-spacing | Weight |
|---|---|---|---|---|---|
| `headline-sm` | Headline Small | 22px | 24px | 0px | 600 |
| `headline-md` | Headline Medium | 26px | 32px | 0px | 600 |
| `headline-lg` | Headline Large | 28px | 32px | 0px | 600 |
| `headline-xl` | Headline XLarge | 30px | 34px | 0px | 600 |

> Headline: short, high-emphasis text. Primary text passages and important content regions. `headline-xl` suits H1 content (not in combination with `display-lg`).

### Display (campaign/hero, uppercase)

| Token | Name | Size | Line-height | Letter-spacing | Weight |
|---|---|---|---|---|---|
| `display-sm` | Display Small | 22px | 22px | 0px | 600 |
| `display-md` | Display Medium | 28px | 28px | 0px | 600 |
| `display-lg` | Display Large | 36px | 34px | 0px | 600 |

> Display: `text-transform: uppercase`. Reserved for hero banners, campaign headlines, and numerals. Use sparingly. `display-lg` = H1 on a page/article (never together with `headline-xl`). NOTE: `display-lg` has a line-height (34px) lower than its font-size (36px) — intentional, for tight campaign text.

### CSS rule (Mobile Base)

```css
/* All typography styles share: */
font-family: 'Breuer Condensed', Arial, sans-serif;
font-style: normal;
font-feature-settings: 'ss02' 1, 'ss03' 1;

/* Alt-Label and Label add: */
text-transform: uppercase;

/* Display adds: */
text-transform: uppercase;
font-feature-settings: 'ss02' 1, 'ss03' 1; /* not 'ss06' */
```

---
