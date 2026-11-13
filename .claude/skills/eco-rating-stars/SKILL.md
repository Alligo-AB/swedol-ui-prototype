---
name: eco-rating-stars
description: Use when showing a product's or a review's rating as five stars — optionally with the score ("4.4 / 5"), a link with the number of reviews and an info icon. Sizes Small/Medium/Large/XLarge. Read-only: not for letting the user set a rating (no input component exists yet) and not for the rating bars/histogram on the reviews page.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Rating Stars (ECO Design System)

**Figma:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=891-32372 (component set, checked 2026-11-11). **CSS:** `components/css/rating-stars.css`. **Docs page:** none yet (ask before adding one). **First use:** `pdp.html` (Top info).

Shows a rating the user reads, never one the user sets. Five stars; a filled star is yellow, an unfilled star is grey.

### When to use
- A product's average rating (PDP, product card, variant row) or the rating of one review.
- With the review-count link when the user can go on to the reviews.

### Not to use
- To let the user choose a rating: no input component exists. Ask first.
- For the distribution of ratings (the bars on `reviews.html`): that is a page-local pattern.
- As decoration without a real rating behind it.

### Parts (left to right, all but the stars optional)

| Part | Class | Content |
|---|---|---|
| Score | `rating-stars__score` + `rating-stars__score-max` | `4.4` in `text-primary`, ` / 5` in `text-disabled` |
| Stars | `rating-stars__stars` > 5 × `rating-stars__star` | inline SVG, the Figma drawing; unfilled adds `rating-stars__star--empty` |
| Review count | `inline-link rating-stars__count` | the number only (`200`), `text-action-tertiary`, underlined |
| Info icon | `icon icon--xs` (`info`, 14px) | inside `rating-stars__meta` together with the count, 4px gap |

### Size model

| Size | Class | Star | Space after score and stars | Row gap when it wraps |
|---|---|---|---|---|
| Small | `rating-stars--sm` | 12px | `space-4` | 0 below 769px, `space-2` from 769px |
| Medium (default) | – | 16px | `space-8` | `space-2` |
| Large | `rating-stars--lg` | 20px | `space-8` | `space-2` |
| XLarge | `rating-stars--xl` | 24px | `space-8` | `space-2` |

1px between the stars at every size. The star size does not change with the breakpoint; the text does (below). Figma has XLarge only for 769px and up.

`rating-stars--sm-mobile` (add it to Medium, Large or XLarge): the component is Small below 769px and the chosen size from 769px. The PDP Top info uses it (Small on mobile, Medium on desktop).

### Typography (see `eco-typography`; switches at 769px, never at 640px)

| Part | Size | Style | Mobile | Desktop |
|---|---|---|---|---|
| Score | Medium, Large | title-sm | 16/18 | 16/18 |
| Score | XLarge | title-lg | 20/24 | 24/28 |
| Score | Small | label-sm, uppercase | 12/12, 0.48px | 14/14, 0.56px |
| Review count | Medium, Large, XLarge | body-md | 16/22, 0.32px | 17/24, 0.32px |
| Review count | Small | body-sm | 14/20, 0.36px | 14/20, 0.36px |

Score weight is 600 in CSS (Figma Bold; CSS = Figma − 100).

### States

The component itself has no states. The review-count link has the Inline Link states (`eco-inline-link`: hover, focus-visible, visited); only its color (`text-action-tertiary`) and size are set here.

### HTML structure

```html
<link rel="stylesheet" href="/components/css/rating-stars.css">

<div class="rating-stars">
  <span class="rating-stars__score">4.4 <span class="rating-stars__score-max">/ 5</span></span>
  <span class="rating-stars__stars" role="img" aria-label="Betyg 4,4 av 5">
    <svg class="rating-stars__star" viewBox="0 0 16 16" aria-hidden="true"><path d="M3.02959 16L4.89941 9.88791L0 6.39528H6.08284L8 0L9.91716 6.39528H16L11.1006 9.88791L12.9704 16L8 12.2242L3.02959 16Z"/></svg>
    <svg class="rating-stars__star" viewBox="0 0 16 16" aria-hidden="true"><path d="M3.02959 16L4.89941 9.88791L0 6.39528H6.08284L8 0L9.91716 6.39528H16L11.1006 9.88791L12.9704 16L8 12.2242L3.02959 16Z"/></svg>
    <svg class="rating-stars__star" viewBox="0 0 16 16" aria-hidden="true"><path d="M3.02959 16L4.89941 9.88791L0 6.39528H6.08284L8 0L9.91716 6.39528H16L11.1006 9.88791L12.9704 16L8 12.2242L3.02959 16Z"/></svg>
    <svg class="rating-stars__star" viewBox="0 0 16 16" aria-hidden="true"><path d="M3.02959 16L4.89941 9.88791L0 6.39528H6.08284L8 0L9.91716 6.39528H16L11.1006 9.88791L12.9704 16L8 12.2242L3.02959 16Z"/></svg>
    <svg class="rating-stars__star rating-stars__star--empty" viewBox="0 0 16 16" aria-hidden="true"><path d="M3.02959 16L4.89941 9.88791L0 6.39528H6.08284L8 0L9.91716 6.39528H16L11.1006 9.88791L12.9704 16L8 12.2242L3.02959 16Z"/></svg>
  </span>
  <span class="rating-stars__meta">
    <a href="#reviews" class="inline-link rating-stars__count" aria-label="200 recensioner">200</a>
    <span class="icon icon--xs" aria-hidden="true">info</span>
  </span>
</div>
```

Stars only: keep just `rating-stars__stars`. Without the info icon the count may sit directly in `.rating-stars` (no `__meta` wrapper needed). The one star path is used at every size (the SVG scales; Figma's 12, 16, 20 and 24px drawings are the same shape).

### CSS

Link the shared stylesheet; never copy its rules into a page and never write a parallel version (the older `.stars` / `.star-icon` in `reviews.html` is page-local and predates this component). The info icon needs `components/css/icon.css`, the count needs `inline-link.css`; both templates link all three.

### Rules

1. **Always the Figma star** (inline SVG path above), never the Material `star` glyph: the shapes differ.
2. **Whole stars only.** Figma has a filled and an unfilled star, no half star. Round the score to the nearest whole number for the stars and show the exact score as text or in the label.
3. **Always a text alternative:** `role="img"` and `aria-label="Betyg 4,4 av 5"` on `rating-stars__stars`; every `<svg>` has `aria-hidden="true"`.
4. **The count is a link** (`<a>`, `inline-link`) that goes to the reviews; give it an `aria-label` with the unit ("200 recensioner"), since the visible text is only the number.
5. **Tokens only:** `--color-surface-warning-default` (filled), `--color-surface-10` (unfilled), `--color-text-disabled` (` / 5`), `--color-text-action-tertiary` (count). Never a hex value.
6. **Sizes are the four above.** Never set `--rs-size` or a width on the stars in a page.
7. **Read-only.** No hover state, no `cursor: pointer` on the stars, no click handler.
8. **Breakpoint test:** check at ~375px, ~700px (must look like mobile) and 1024px+ with `getComputedStyle` (star size, text size).

### Flags for design

- **title-sm:** Figma binds the score (Medium, Large) to title-sm = 17/20 on desktop, and the mobile frames hard-code 17/20; `tokens.json` has title-sm 16/18 at every width. The CSS follows `tokens.json` (16/18).
- **Small score on mobile:** the Figma mobile frame hard-codes 14/14; the CSS follows label-sm (12/12 below 769px).
- **" / 5" color on mobile Small:** Figma has `#999` there and `text-disabled` (#939595) everywhere else; the CSS uses `text-disabled` at every size.
- **Info icon:** Figma shows it but not what it does. It is built as a plain icon. If it should explain something it becomes an icon button with `data-tooltip` (`eco-tooltip`): ask first.
- **Half stars:** not in Figma (4.4 shows four filled stars).
- **Star sizes 12/16/20/24px** have no token; they are the Figma sizes, like the icon sizes in `eco-icon`.
