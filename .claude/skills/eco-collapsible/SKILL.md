---
name: eco-collapsible
description: Use when building a row-based expandable component/accordion, e.g. an "FAQ" section or a filter group — header (title, descriptive text, icons, toggle switch, number badge, chevron) + animated content. Sizes Large/Small, Boxed, Dark, Disabled.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Collapsible / Accordion (ECO Design System)

A row-based expandable component. A click on the header opens or closes the content with an animated `max-height` transition. Used for FAQ sections and filter groups. Documentation: three pages, `eco-design-system/components/collapsible.html` (+ `-specifications`, `-code`).

**Figma** (checked 2026-10-14): Base / Collapsible `535:15947` (axes Breakpoint, State, Theme, Size, Boxed; the description says the header is a building block, and that expansion state and content are coordinated by the composed pattern), Collapsible & Collapsible open `3375:138321` (closed/open examples: checkboxes, FAQ text, footer link; the content is free, not limited to these), Support + Visa mer `8657:125202`, boxed setup `23386:26225`.

### Anatomy

```
.collapsible-wrap                              ← one row, 1px line under it (+ --open --small --boxed --filled --divider-top --divider-bottom --no-divider-bottom --dark --disabled)
  <button class="collapsible-item">            ← header (recommended; the old <div onclick> still works)
    .collapsible-item__left
      .ms                                      ← optional leading icon
      .collapsible-item__text                  ← optional, when there is a descriptive or helper text
        .collapsible-item__line
          .collapsible-item__label             ← title ("Title:")
          .collapsible-item__info              ← optional descriptive text, regular weight
        .collapsible-item__helper              ← optional helper text, body-sm
      .ms                                      ← optional trailing icon
    .collapsible-item__end
      .form-switch-item (--xs on Small)        ← optional toggle switch
      .badge-number (--md Large, --sm Small)   ← optional number badge
      .collapsible-item__chevron               ← "expand_more", rotates 180° when open
  .collapsible-item__content                   ← must follow the header; max-height animated by JS
    (.collapsible-item__body)                  ← inside a boxed row
```

### Sizes and values

| | Large | Small |
|---|---|---|
| Header | min-height 72px, padding 24px top/bottom | min-height 56px, padding 16px top/bottom |
| Title | `title-md` 18/22 → 20/24 (769px), weight 600 | `title-sm` 16/18 |
| Descriptive text | regular, 18/24 → 20/24 | `body-md` 16/22 → 17/24 |
| Icons, chevron | 24px | 20px |
| Switch | 48×24 (default) | 32×16 (`form-switch-item--xs`) |
| Number badge | `badge-number--md` (20px desktop, 18px mobile) | `badge-number--sm` (16px desktop, 14px mobile) |
| Gaps | icon–text 8px, title–descriptive 2px, text–right group 16px | same |

Helper text: `body-sm` 14/20, 0.36px, `text-secondary` (hover `text-tertiary`, dark `text-primary-inverted`, disabled `text-disabled`). Open row: 32px extra space below the content. Content: `body-md` 16/22 → 17/24, `text-primary`, 12px between paragraphs (changed 2026-10-14 from body-lg grey 18/24 → 20/28, to follow Figma: user decision "följ Figma").

**Helper text:** with a `collapsible-item__helper` the header has two lines. Leading and trailing icons, switch, badge and chevron line up with the **title line** (24px high, header `align-items: flex-start`), not with the middle of the block. Without helper text everything is centered.

**Content gap:** the space from the bottom of the header text to the first line of the content is **24px in every size** (not boxed), whatever the header holds (`--co-content-gap`; Large: header padding 24px; Small: 16px + 8px margin on the first child). **A boxed row is the exception**: header padding + body padding = 48px Large, 32px Small. The checkbox list has no top padding of its own. Requested by the user 2026-10-14; Figma has 24px (FAQ, Large), 32px (checkbox list) and 33px (boxed).

### Boxed (Large and Small)

`collapsible-wrap--boxed` (Large) or `collapsible-wrap--small collapsible-wrap--boxed` (Small): 1px `border-primary` frame, header padding on all sides = the size's vertical padding (**24px Large, 16px Small**; `--co-box-pad`). Figma only has Small boxed (`23350:159804`, `23350:159790`, `23386:26225`); Large boxed is the same rule, added on the user's request 2026-10-14. Open: no background of its own (**grey only with `--filled`**, user rule 2026-10-14: if grey is not chosen there is no grey, open or closed; Figma's boxed setup has a `surface-02` header), a 1px line under the header (inset shadow, no space), body (`collapsible-item__body`) `background-primary`, padding = `--co-box-pad` on all sides (24px Large, 16px Small, desktop and mobile; the user asked for 24px / 16px above the content text 2026-10-14), gap 12px, no extra space below.

### Filled (header background)

`collapsible-wrap--filled`: `background: var(--color-surface-raised-secondary)` on the **header only** (an add-on in the header part); the content sits on white (`background-primary`). The header gets 16px side padding and the content the same, so the text lines up (a boxed row keeps its own padding and its white body; a boxed row can be filled too). Requested by the user 2026-10-14 (color corrected from surface-02 to surface-raised-secondary); not in Figma. The content text starts 24px (Large) or 16px (Small) below the grey header (`--co-content-top`; not boxed, boxed has its body padding), because the grey box ends where the content starts. Only this color is supported; ask before adding others.

### Dividers

The line under the row is on by default (rows in a list share it); the line above is off. Each is switched on or off on its own: `collapsible-wrap--divider-top` (1px `border-primary` above), `collapsible-wrap--no-divider-bottom` (removes the line below). Dark: `border-dark`; disabled: `border-primary`. Not for a boxed row (the frame is the line). Figma's Large header has a line above and below; the repo default stays bottom only, so lists do not get double lines. The last row in a section still loses its bottom line (rule 2) unless it has `collapsible-wrap--divider-bottom` (forces the line on).

### Usage (from Supernova, Collapsible block, 2026-10-14)

- Use it to organize related content in a limited space (FAQ) and to hide complex or less important details so the user focuses on the key points first. It works on a white or a grey section; do not combine the grey Header background with a grey section.
- Do not use it to compare (all content must be visible), where people open and close a lot (open the most useful row from the start: `collapsible-wrap--open`, the **Open** switch in the Storyblok **Collapsible block**), for essential information, or nested.
- Best practices: short, descriptive titles; reduce clutter; few collapsibles per view; a clear purpose, never decoration; keep the content narrow enough (60–90 characters per line, Typography → Line length).
- Dividers: only where they add clarity. In a list: lines between rows only, none above the first or under the last. A section with one collapsible: top and bottom divider (`--divider-top` + `--divider-bottom`), but not on a colored section. With an optional headline above: no top divider. (The source caption of the headline example is labelled "Don't" although the image shows the correct solution; the docs show it as Do.) Storyblok context examples in Figma: file `QYaY33c8HK3xKVLcpnzlh6`, board `5060:131758`; frames checked 2026-10-14: `5072:26976` (grey group with Optional title, 8 rows, lines between), `5103:8811` (mobile card with icon rows), `5103:8090` (mobile grey group with title), `5430:40315` (two rows, line between, none top/bottom), `5446:42875` and `5446:42245` (rows with lines between), `5446:43512` (one collapsible: top + bottom), `5446:44259` (Optional title on grey: no dividers); Do/Don't assets in file `XiIY0vXqx3jQLsACy8sqfh`: `50:46`, `63:3266`, `55:18191`, `56:3245`, `59:2659`. The headline example (`59:2659`) has no dividers at all on the grey section. The Storyblok widget itself has its own Storyblok tab in Supernova, to be added.

### Theme and states

| | Text, icons, chevron | Other |
|---|---|---|
| Light enabled | `text-primary` | line `border-primary` |
| Light hover (whole header) | `text-action-primary-hover` (also the icons) | |
| Dark (`--dark`) | title `text-action-primary-inverted`, hover `text-action-primary-inverted-hover`; descriptive text follows the title (white, hover 78% white); helper text and content `text-primary-inverted` (Figma re-read 2026-10-14: on desktop hover the whole title line dims, the helper stays white) | line `border-dark`, number badge `surface-raised-primary` with `text-primary` |
| Disabled (`--disabled` + `disabled`) | everything `text-disabled` (title, descriptive text, helper text, icons), no hover, no click | line `border-primary` (also on Dark), number badge `surface-disabled` |

Dark + boxed or filled (not in Figma, added on the user's request 2026-10-14): frame `border-dark` on all sides; a filled header `surface-90` (the line under an open boxed header `border-dark`); body and content transparent, so they sit on the black surface with white text. Ask before changing these values.

Figma defines Disabled once, under Theme Dark, drawn with `text-disabled` and the light line; the CSS applies it to both themes. Figma shows the disabled helper text white at `body-md`; not followed, it stays `text-disabled`. The dark content text (`text-primary-inverted`) is not specified in Figma. Transition: `color` with `duration-fast-3` and `ease-standard`. All transitions are off with `prefers-reduced-motion`.

### Content patterns (Figma)

Checkbox list: `collapsible-item__list` (gap/padding from `space-24`/`space-8`) with `collapsible-item__row` (checkbox + `collapsible-item__count`, 16/22 tertiary). Support block: `collapsible-item__support` with `collapsible-item__note` (body-sm tertiary), `collapsible-item__more` ("Show more", text-only, body-md bold, underlined on hover; Figma uses an Action Link without icon, the Action Link component always has an icon) and optionally a Secondary XSmall button.

Filter list (Figma `UI – PLP/PDP 1.0`, file `gAuhhKQVftqFTly8D9ACp0`, frames `3753:534278`, `3753:534245`, `3753:534311`): Large rows in a drawer, the first row with `--divider-top`, a descriptive text for the current choice ("Sortering: Populärast"), a switch row without chevron ("Kampanj"), a trailing icon + number badge ("Avtalssortiment"), and an open row with a search field (`input-wrap` with `input-icon--lg`) 24px below the header and 32px above the checkbox list (`collapsible-item__content .input-wrap + .collapsible-item__list` has 32px top padding, measured in Figma), items 24px apart, counts right.

### Rules

1. **Bottom line between rows** — every `.collapsible-wrap` has `border-bottom: 1px solid var(--color-border-primary)` as a separator against the next row.
2. **The last row in a list that closes out a section hides its bottom line** — conditioned on the list's PARENT being the section's last child (`section > *:last-child .collapsible-wrap:last-child`), not for a boxed row.
3. **`min-height`, not `height`, on `.collapsible-item`** — the header must be able to grow if the title wraps.
4. **The `max-height` animation is handled by JS** — `toggleCollapsible()` sets `content.style.maxHeight` to `scrollHeight` (open) or `null` (close).
5. **Header is a `<button>`** with `aria-expanded` and `aria-controls` (the script keeps `aria-expanded` in sync). Closed content is `visibility: hidden` after the close animation, so it is not read or focused.
6. **A switch inside an opening header is a control inside a control.** Figma shows both together; build a row with a switch **without a chevron** (header as `div`), or move the switch out. A click on `.form-switch-item`, a link or `[data-collapsible-ignore]` inside the header does not toggle the row.
7. **Boxed exists in both sizes.** Large boxed is not in Figma (derived: padding 24px on all sides).
8. The old `<div class="collapsible-item" onclick>` markup keeps working (same classes).

### CSS and JS

Link the shared files. Never copy their rules into a page, and never write a parallel version:

```html
<link rel="stylesheet" href="/components/css/collapsible.css">
<script src="/components/js/collapsible.js"></script>
```

A switch needs `switch.css`, a number `badge.css`, checkboxes `checkbox.css`. Mobile-first, desktop from 769px, `var(--…)` only.

### HTML example

```html
<div class="collapsible-wrap">
  <button type="button" class="collapsible-item" onclick="toggleCollapsible(this)" aria-expanded="false" aria-controls="faq-1">
    <span class="collapsible-item__left">
      <span class="collapsible-item__label">What does it cost to set up a custom webshop?</span>
    </span>
    <span class="collapsible-item__end">
      <span class="collapsible-item__chevron"><span class="ms" aria-hidden="true">expand_more</span></span>
    </span>
  </button>
  <div class="collapsible-item__content" id="faq-1"><p>It depends on the scope and which features you need.</p></div>
</div>
```

### Motion

Open/close uses `--co-ease` / `--co-duration` (fallback: `ease-standard`, `duration-fast-4`, the recommended values) on `.collapsible-wrap`, its chevron and its content. The docs page has a Motion section (`DK.motion`, prefix `co`) to compare other tokens live. Set the vars on a wrapper to override.

### Storyblok

The Storyblok widget is the **Collapsible block** (technical name `collapsible`; items are **Collapsible item**). Documentation tab: `eco-design-system/components/collapsible-storyblok.html` (covers only the Collapsible block; other widgets are documented under their own components) (editor steps with annotated screenshots in `images/storyblok-collapsible-*.png`). Storyblok settings: item **Headline** (required), **Content** (Add Block), **Open** (off by default = `--open`), **Bottom Divider** (on by default), **Top Divider** (off by default = `--divider-top`); the container has an optional **Headline** and the section sets **Column Width Medium/Large** (col-10 / col-8 in the examples). Pro tip: use the section column width settings to make a group of collapsibles easier to digest.

### Open points (also on the documentation page)

- `max-height` is set once when the row opens; if the text wraps differently after a resize while open, the height is not updated.
- Figma shows the switch and the chevron in one header (see rule 6).
- Dark content text and the Disabled-on-light theme are not defined in Figma.
