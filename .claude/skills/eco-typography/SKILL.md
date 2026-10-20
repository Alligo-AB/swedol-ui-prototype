---
name: eco-typography
description: Use when choosing or reviewing typography/text styles (Body, Alt-Label, Label, Title, Headline, Display) on Desktop vs. Mobile per the ECO Design System.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

> **Source:** Size/Line-height/Letter-spacing in the tables below are pulled from `tokens.json` (the `eco-tokens` skill), not hardcoded. Typography tokens have no CSS `var(--...)` in the package (JS values only, see `eco-tokens`) — the numbers here are the actual source to write CSS against, not a standalone copy.
>
> **Known discrepancies, not changed here — require confirmation before changing in code:**
> - **Resolved (tokens.json 2026-10-02, matches Figma):** `display-lg` mobile is now 36/34 (desktop 66/60), `body-md` desktop is 17/24, `body-sm` letter-spacing is 0.36px, `body-lg` has 0.18px letter-spacing. The tables below were regenerated from `tokens.json` (size, line-height, letter-spacing).
> - **Font-weight: Figma and CSS differ by 100 (confirmed by design).** Figma shows Breuer Condensed 100 higher than the CSS value: Figma Regular 500 / Medium 600 / Bold 700 = CSS Regular **400** / Medium **500** / Bold **600**. Write the CSS values (Body 400, Alt-Label 500, bold 600, never 700 copied from Figma). A weight in `tokens.json` or a Figma node that looks 100 too high for its role (Body 500, Alt-Label 600) is the Figma value, not a discrepancy to flag. The web font package only ships 300/400/500/700, so 600 renders with the 700 face.
> - **Stylistic sets (`ss02`/`ss03`/`ss06`) are not in the web fonts.** The `font-feature-settings` rules below match Figma, but the Breuer Condensed web font files in `alligo-design-tokens` (`dist/fonts/breuercondensed-*-webfont.woff`) only contain the OpenType features `frac`, `liga` and `sups` (checked 2026-09-28; the swedol.se UAT fonts are the same). In the browser the setting therefore has no visible effect, and glyphs cannot match Figma's alternates until the web fonts are rebuilt with the sets kept. Keep writing the declaration (it is harmless and correct once the fonts are fixed), but never report a missing or present `font-feature-settings` as a visible difference without comparing the rendered glyphs first.

## Typography – Desktop Base Styling (ECO Design System)

Applies to **Desktop Small (`md:`, 769px+) and Desktop (`lg:`, 1024px+)**.
Font: `Breuer Condensed`, sans-serif. `font-feature-settings: 'ss02' 1, 'ss03' 1` applies to all styles.

### Body

| Token | Name | Size | Line-height | Letter-spacing | Weight | Paragraph-spacing |
|---|---|---|---|---|---|---|
| `body-sm` | Body Small | 14px | 20px | 0.36px | 400 | 12px |
| `body-md` | Body Medium | 17px | 24px | 0.32px | 400 | 16px |
| `body-lg` | Body Large | 20px | 28px | 0.18px | 400 | 20px |
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
| `title-sm` | Title Small | 16px | 18px | 0px | 600 |
| `title-md` | Title Medium | 20px | 24px | 0px | 600 |
| `title-lg` | Title Large | 24px | 28px | 0px | 600 |

> Title: shorter, medium-strength text. Used for secondary headings and smaller H-tags.

### Headline (primary headings, normal case)

| Token | Name | Size | Line-height | Letter-spacing | Weight |
|---|---|---|---|---|---|
| `headline-sm` | Headline Small | 28px | 32px | 0px | 600 |
| `headline-md` | Headline Medium | 32px | 36px | 0px | 600 |
| `headline-lg` | Headline Large | 36px | 40px | 0px | 600 |
| `headline-xl` | Headline XLarge | 46px | 52px | 0px | 600 |

> Headline: short, high-emphasis text. Primary text passages and important content regions. `headline-xl` suits H1 content (not in combination with `display-lg`).

### Display (campaign/hero, uppercase)

| Token | Name | Size | Line-height | Letter-spacing | Weight |
|---|---|---|---|---|---|
| `display-sm` | Display Small | 26px | 26px | 0px | 600 |
| `display-md` | Display Medium | 36px | 36px | 0px | 600 |
| `display-lg` | Display Large | 66px | 60px | 0px | 600 |

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
| `body-sm` | Body Small | 14px | 20px | 0.36px | 400 | 12px |
| `body-md` | Body Medium | 16px | 22px | 0.32px | 400 | 16px |
| `body-lg` | Body Large | 18px | 24px | 0.18px | 400 | 16px |
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
| `title-sm` | Title Small | 16px | 18px | 0px | 600 |
| `title-md` | Title Medium | 18px | 22px | 0px | 600 |
| `title-lg` | Title Large | 20px | 24px | 0px | 600 |

> Title: shorter, medium-strength text. Used for secondary headings and smaller H-tags.

### Headline (primary headings, normal case)

| Token | Name | Size | Line-height | Letter-spacing | Weight |
|---|---|---|---|---|---|
| `headline-sm` | Headline Small | 22px | 24px | 0px | 600 |
| `headline-md` | Headline Medium | 26px | 28px | 0px | 600 |
| `headline-lg` | Headline Large | 28px | 32px | 0px | 600 |
| `headline-xl` | Headline XLarge | 30px | 36px | 0px | 600 |

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
