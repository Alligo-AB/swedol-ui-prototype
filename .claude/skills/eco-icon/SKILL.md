---
name: eco-icon
description: Use when showing an icon (Material Symbols Outlined or Fill, or a custom SVG icon: customized symbol, brand, social, logo), choosing an icon size or color, naming or adding an icon, or looking up an icon name in the icon library. Not for choosing an icon name in a form field (use eco-icon-picker) and not for pictures or illustrations.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, breakpoints and the quality checklist.

## Icon (ECO Design System)

Figma (file ECO Design System): Icon Documentation `3886:157988`, Icon Library `262:10207`, Icon Library design `3914:166380`, Icon Item Container `3914:166984`, Add icons to our system `3912:166091`.
Docs: `eco-design-system/components/icon.html` (Examples) + `icon-specifications.html` + `icon-code.html` + `icon-library.html` (search and copy every icon) + `icon-add.html` (how to add one). Built by `eco-design-system/gen/gen_icon.py`.

## Two sources

| Source | Markup | Names |
|---|---|---|
| Material Symbols (font) | `<span class="icon icon--md" aria-hidden="true">search</span>` | Material Symbols name. Outline = Fill 0, Weight 300, Grade 0. Fill = `icon--fill` (Fill 1). |
| Custom icon (inline SVG, 24 grid) | `<svg class="icon icon--md" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">…</svg>` | Ends with `_custom` (customized symbol), `_brand` (Swedol / Tools), `_social`, `_logo`. |

Link `/components/css/icon.css` (one file, tokens only). Never set `font-size` on a font icon: use a size class so the optical size follows.

## Sizes

| Class | px | Optical size | Use |
|---|---|---|---|
| `icon--xxs` | 12 | 20 | Extra size: badges and components with restricted space (Figma) |
| `icon--xs` | 14 | 20 | Extra size: same as 12 (Figma) |
| `icon--sm` | 20 | 20 | Inside controls (default in buttons, inputs, list items) |
| `icon--md` | 24 | 24 | Stand-alone icon (default of `.icon`) |
| `icon--lg` | 40 | 40 | Tiles, empty states, the library |
| `icon--xl` | 48 | 48 | Prominent, rare |

Figma guidance (`24755:7811`): standard sizes 20, 24, 40, 48; 12 and 14 reserved for badges and components with restricted space. Examples for the standard sizes are ours. Same on every breakpoint. Material Symbols settings in Figma: Outlined Fill 0, Weight 300, Grade 0, optical sizes 20, 24, 40, 48 plus 12 and 14; Fill: Fill 1, Weight 300, Grade 0, optical sizes 20, 24, 40, 48.

## Color

`icon-primary` (default) on light, `icon-inverted` (`icon--inverted`) on dark, `icon--inherit` inside a button or link. No status colors exist for icons.

## Library and naming

- Names: underscore between words, lowercase, Material name as shipped; `_custom`, `_logo`, `_brand`, `_social` for the rest.
- Library page categories: Material Symbols (Outlined only; Fill is for developers, as the active state, and is not listed) and Custom icons (Customized symbols, Brand, Social, Logo). Data: `components/icon-library/icon-library-data.js` (generated, never by hand: `python3 gen_icon.py data` from `gen/icons-material.txt` and `gen/icons-custom.txt`); script `components/js/icon-library.js`.
- Icon item (library): button, copy icon 20px hidden until hover/focus, icon 40px, name body-sm, hover white + `shadow-elevation-b-60` + `surface-navigation-hover` name bar, focus ring `border-focus`.

## Forward and back arrows (2026-11-03, rule for every component)

With a text label the direction icon is a **chevron** (`chevron_right` forward, `chevron_left` back), on links, buttons and menu rows alike. Without text it is an **arrow**: `arrow_right_alt` (forward) and `arrow_left_alt` (back). Never `arrow_forward` or `arrow_back`. Same rule in Action Link, Button and cards.

| Case | Icon |
|---|---|
| A link with a text label ("Till Gesto", "View all products") | `chevron_right`, trailing (default) |
| No text, only a mark on a clickable card (article card): the only signal that the card leads on | `arrow_right_alt`, inside an `.action-link` (an icon button does not give an even left edge) |
| A single link that closes a section, or a campaign link where the signal should be stronger | `arrow_right_alt`, trailing, sparingly |
| Button, link or menu row with a text label | trailing `chevron_right` (forward), leading `chevron_left` (back) |
| Forward or back with no text (icon only) | `arrow_right_alt` / `arrow_left_alt` |
| Download | `file_download`, leading (unchanged) |

Never mix chevron and arrow in one group of cards or links. A decorative arrow is `aria-hidden="true"`; on a card where the whole card is the link, the link takes its name from the headline (`aria-labelledby`).

## Rules

0. **Reserved:** `verified_500_custom`, `assignment_turned_in_500_custom` and `history_500_custom` are only for the Product & Discount badges (`eco-badge`). Never use them elsewhere. The library marks them Reserved. The Material Symbols in the library are the ones in use on the site.
1. Decorative icon: `aria-hidden="true"`. Icon with meaning and no label: name the control that holds it (`aria-label`).
2. Outline for the normal state, Fill for the active state.
3. Same icon for the same meaning everywhere. Never decorate without meaning.
4. Never a color that is not a token. Never scale with transform or your own width/height: use a size class.
5. An icon-only button gets a Tooltip (`eco-tooltip`) and a Button size that matches (`eco-button`).

## Flags (for design)

- Fixed in Figma 2026-11-01 (library data rebuilt): `linkedin_social`, `sell_percent_custom`, `favourite_placed_custom`, style suffixes removed from Fill names, `docs_add_on`, `more_horiz`, `compare_arrows_inverted` removed. Still open: Material outline `favourite` (Material: `favorite`), `return_shipment_custom_1`.
- Service icons without `_brand` (for example `hose_crimping`, `calibration`) could not be exported (no visible layers); only the `_brand` versions are in the library.
- Brand icons have no per-brand (Swedol / Tools) split yet. Social icons use `currentColor`, not the networks’ brand colors.
- Figma shows a Sprout link on the Add-an-icon text; the docs link to the ECO file instead.
