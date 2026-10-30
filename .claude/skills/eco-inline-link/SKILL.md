---
name: eco-inline-link
description: Use when building a link inside a sentence or text block — always underlined in the enabled state, never with an icon.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Inline Link (ECO Design System)

**Figma:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=1671-52629

Figma description (2026-10-13): "An underlined text link that flows within body copy, lists, and UI text. The underline is its affordance — never paired with icons." Used **inside body copy, lists and UI text** (sentences and text blocks). Underlined in the Enabled state — the underline is **removed** on hover, replaced by a color change. **Never** combined with icons.

An inline link inherits the typography of its surrounding context and signals interactivity through an underline and state changes. It is the default way to link from running text, footers, legal copy and helper text. One line: an underlined text element that navigates to a destination while flowing inline with surrounding content.

**States:** Enabled (Default: underlined; Reverse: not underlined) and Hover (reduced contrast: color shift and underline removal; Reverse: underline appears). **No Disabled state:** avoid disabled links entirely; remove the link or render plain text (a disabled `<a>` has no standard semantics).

**Sizing rule:** an inline link matches the size, line height and letter spacing of its surrounding text (body-xl / body-lg / body-md / body-sm) and follows the Desktop or Mobile base styles of that text. The link has the same style as its surrounding text (size, line height, letter spacing, weight, italic). Never make a link larger or bolder than its text for emphasis; Medium, Bold and Italic only follow text that has that style. A link that stands apart from other content matches the page's default body copy size.

### Difference from Action Link

| Property | Inline Link | Action Link |
|---|---|---|
| Placement | In body text | Standalone |
| Underline | Enabled: yes. Hover: no (removed) | Enabled: no. Hover: yes (added) |
| Icons | Never | Always at least one (leading, trailing or both) |
| `display` | `inline` | `inline-flex` |

---

### Sizes

> XLarge (`body-xl` 24/32) is also used for the intro text of the doc pages (`.ds-lead`).

#### Desktop (`md:`, 769px+)

| Size | Typography token | Font-size | Line-height | Letter-spacing | Weight |
|---|---|---|---|---|---|
| **XLarge** (`inline-link--xlarge`) | `body-xl` | 24px | 32px | 0 | 400 |
| **Large** | `body-lg` | 20px | 28px | 0.18px | 400 |
| **Medium** | `body-md` | 17px | 24px | 0.32px | 400 |
| **Small** | `body-sm` | 14px | 20px | 0.36px | 400 |
| **Small Bold** (`inline-link--small-bold`, kept) | `body-sm` | 14px | 20px | 0.36px | Weight 600 (Bold): same as `inline-link--small inline-link--bold` |

#### Mobile / Tablet (`xs`/`sm`, ≤768px)

| Size | Font-size | Line-height | Letter-spacing |
|---|---|---|---|
| **XLarge** | 20px | 26px | 0 |
| **Large** | 18px | 24px | 0.18px |
| **Medium** | 16px | 22px | 0.32px |
| **Small / Small Bold** | 14px | 20px | 0.36px |

---

### Color variants

| Variant | Enabled color | Hover color |
|---|---|---|
| **Text Primary** | `var(--color-text-action-primary)` (`text-action-primary`) | `var(--color-text-action-primary-hover)` (`text-action-primary-hover`) |
| **Text Secondary** | `var(--color-text-action-secondary)` (`text-secondary`) | `var(--color-text-action-secondary-hover)` (`text-action-secondary-hover`) |
| **Text Tertiary** | `var(--color-text-action-tertiary)` (`text-tertiary`) | `var(--color-text-action-tertiary-hover)` (`text-action-tertiary-hover`) |
| **Text Primary Inverted** | `var(--color-text-action-primary-inverted)` (`text-primary-inverted`) | `var(--color-text-action-primary-inverted-hover)` (`text-action-primary-inverted-hover`) |

---

### States

| State | Underline | Text color |
|---|---|---|
| **Enabled** | `text-decoration: underline` | Per variant above |
| **Hover** | `text-decoration: none` (removed) | Per variant above |
| **Enabled Accordion Link** | `text-decoration: underline` | Same as Text Primary |
| **Hover Accordion Link** | `text-decoration: none` | Same as Text Primary hover |

> Transition: `color` with `duration-fast-3` (150ms) and `ease-standard`. `text-decoration` is not transitioned.
>
> **Focus (2026-10-13):** `body.keyboard-nav .inline-link:focus-visible` has a 2px `border-focus` ring, offset 2px, the same as Action link and Tile link. **Docs (2026-10-29):** `.inline-link[data-state="focus"]` (also `.action-link`, `.tile-link`) forces the ring for the docs only: State Focus in each playground, a Focus row in each states matrix, and a forced example under Behavior > Focus. The Code tab hides that selector via `DK.printCss`.

---

### font-feature-settings

| Size | Value |
|---|---|
| Large (`body-lg`) | `'ss02' 1, 'ss03' 1` |
| Medium (`body-md`) | `'ss02' 1, 'ss03' 1, 'ss06' 1` |
| Small / Small Bold (`body-sm`) | `'ss02' 1, 'ss03' 1, 'ss06' 1` |

---

### CSS

Link the shared stylesheet. Never copy its rules into a page, and never write a parallel version:

```html
<link rel="stylesheet" href="/components/css/inline-link.css">
```

`components/css/inline-link.css` is the single source for this component. Mobile-first, desktop from 769px, `var(--…)` only. To change the component, edit that file.

### HTML example

```html
<!-- In body text — Text Primary, Medium -->
<p>Read more about our products on the
  <a href="#" class="inline-link inline-link--medium">product page</a>.
</p>

<!-- Text Secondary -->
<p>See <a href="#" class="inline-link inline-link--medium inline-link--secondary">full terms</a> for more info.</p>

<!-- Small Bold -->
<a href="#" class="inline-link inline-link--small-bold">Read more</a>

<!-- Inverted, in a dark context -->
<p style="color:var(--color-text-primary-inverted)">Contact us at
  <a href="mailto:info@example.com" class="inline-link inline-link--medium inline-link--inverted">info@example.com</a>.
</p>
```

---

---

### Modifiers: weight, italic, reverse underline

The variants are Breakpoint, State, Size (XLarge, Large, Medium, Small), Color (Primary, Secondary, Tertiary, Primary Inverted), Weight and Reverse. Figma weights are 100 higher than the CSS (see `eco-typography`).

| Modifier | Class | CSS |
|---|---|---|
| Weight Regular | (none) | `font-weight: 400` |
| Weight Medium | `inline-link--weight-medium` | `font-weight: 500` |
| Weight Bold | `inline-link--bold` | `font-weight: 600` |
| Italic | `inline-link--italic` | `font-style: italic` (the font ships an italic face for every weight) |
| Reverse underline | `inline-link--reverse` | no underline enabled, underline on hover |

The modifiers can be combined with any size and color. They make a link follow the text around it, never emphasize it. With the reverse underline, enabled has no underline and hover has the underline and `text-action-primary-hover`.

```html
<a href="#" class="inline-link inline-link--medium inline-link--weight-medium">Medium</a>
<a href="#" class="inline-link inline-link--small inline-link--bold">Bold</a>
<a href="#" class="inline-link inline-link--medium inline-link--italic">Italic</a>
<a href="#" class="inline-link inline-link--medium inline-link--reverse">Underline on hover only</a>
```

---

### Usage and content rules

**Use when:** linking from body copy, product descriptions or help text; secondary navigation in footers, text next to a breadcrumb and legal copy; one item in a list (related articles, policy documents); anchor links (table-of-contents entries); `mailto:` / `tel:` in copy.

**Do not use when:** the link is the primary action on the surface (Button); destinations are equal peers in a grid or scroller (Tile Link); the action manipulates the current page: expanding, opening a modal, revealing text (Button, Collapsible, Modal; **a link always navigates**); an icon-only trigger is needed (Icon button; a link with an icon is an Action Link).

**Best practices:** keep the underline on default links in running text (WCAG 1.4.1); link the meaningful phrase, never filler (“click here”, “read more” alone); keep the text short, a phrase not a sentence (typically 1 to 5 words; if it approaches a full line shorten the phrase, not the type size); Inverted on dark surfaces, never the default link on dark; the Medium, Bold and Italic modifiers only when the text around the link has that style; no icons; do not open new tabs by default, and if a link must (`target="_blank"`, a PDF) say so and add `rel="noopener"`.

**Writing link text:** describe the destination and make sense out of context; weave the link into the sentence (never “here” at the end); sentence case matching the copy, no trailing punctuation inside the link, mirror the real capitalization of a named page; never a raw URL as link text; no identical link texts for different destinations (“Read more about shipping” / “… returns”); name the exact action or document (verb for the stage of a quote or order).

**Accessibility:** `<a href>` only, never `href="#"` with a JS handler; accessible name is the visible text, extended with an `aria-label` that begins with the visible text (WCAG 2.5.3); new-tab and file links say so in the accessible name; inline links in text are exempt from the 24px target size (WCAG 2.5.8), standalone link lists need at least 24px effective height; text contrast at least 4.5:1 in every state, link versus body text at least 3:1 or the underline. **Open point (measured 2026-10-13):** Tertiary hover `#939595` is 3.0:1 on white and fails 4.5:1; `#737373` (Primary hover, Secondary hover, Tertiary) is 4.7:1 on white but 4.4:1 on `#f6f6f6`.

**Docs:** the text around a link in every example has the same size, line height and letter spacing as the link (`syncText()` in the page script copies them from the link, also under a forced breakpoint).

**Color rule (2026-10-13):** a link has the same color as the text around it: Primary (`text-action-primary`) in Primary text, Secondary (`text-secondary`, same value as `text-action-secondary`) in Secondary text, Tertiary (`text-tertiary`, same value as `text-action-tertiary`) in Tertiary text, Inverted on dark surfaces. The hover colors are `text-action-primary-hover`, `text-action-secondary-hover` and `text-action-tertiary-hover` (`text-action-primary-inverted-hover` for Inverted). There is no "Primary unless..." default: choose the color of the surrounding text.

