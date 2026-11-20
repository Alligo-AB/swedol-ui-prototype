---
name: eco-icon-button-compact
description: Use when an icon-only action sits where a regular icon button is too big — product card (compare, favourite), table row, input field, list row (edit, close, clear, location, scan). Frameless, as big as its icon (Small 20px, Large 24px), states Enabled/Hover/Selected/Selected hover. `components/css/icon-button-compact.css`. Not for the 40/48px icon button of eco-button (`btn--icon`), a text link with an icon (use eco-action-link) or a text label button.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, breakpoints, and the quality checklist.

## Compact Icon Button (ECO Design System)

Figma: section "Compact Icon Button" `23990:132193` (renamed from "Icon Button" 2026-11-15 so it does not clash with `btn--icon` of `eco-button`). Nine sets, each `Version=All`, State × Size (Enabled, Hover, Selected, Selected Hover × Small, Large): `compare`, `add_card_favourite`, `add_favourite_to_list`, `list_selected`, `edit`, `location_on`, `cancel_filled`, `qr_code_scanner`, `close`. Named `Compact Icon Button/<icon>`.

CSS: `components/css/icon-button-compact.css` (linked by both templates). No docs page yet (ask before adding).

## When to use / not to use

- **Use** for an icon-only action on a small surface: compare and favourite on a product card, edit/close/clear/location/scan inside an input or list row.
- **Not** for the regular icon button (40px, 48px from 769px, padding, Blank/Primary… variants) → `eco-button` (`btn--icon`).
- **Not** for a link with a text label → `eco-action-link`. **Not** for a two-view switch → `eco-pill-segment-control`.

## Anatomy and sizes

`<button type="button" class="icon-btn-compact" aria-label="…"><span class="icon icon--sm" aria-hidden="true">favorite</span></button>`

| Size | Icon class | Button size |
|---|---|---|
| Small | `icon--sm` | 20 × 20 px |
| Large | `icon--md` | 24 × 24 px |

No padding, border or background of its own, same on every breakpoint. Icons are Material Symbols Outlined (Fill for the selected state), custom icons (`compare_added_custom`) as in `eco-icon`. Always an `aria-label`; add `data-tooltip` (see `eco-tooltip`) since there is no text.

## States

| State | Look |
|---|---|
| Enabled | icon `--color-text-action-primary` |
| Hover | icon `--color-text-action-primary-hover` |
| Hover, `icon-btn-compact--fill-hover` (favourite) | icon solid, colour stays primary |
| Selected (`aria-pressed="true"` or `.is-on`) | icon solid, primary |
| Selected hover | icon solid, `--color-text-action-primary-hover` |
| Focus (`:focus-visible`) | 2px `--color-border-focus` ring, 2px gap |

`close` (Figma `11916:387404`, Blank / Blank Inverted) has no selected state and uses `icon-btn-compact--surface-hover`: 2px padding (24px box), a `surface-opacity-black-05` surface on hover, icon stays `icon-primary`; `icon-btn-compact--inverted` for dark surfaces (`icon-inverted`, `surface-opacity-white-20`). Decided 2026-11-15: kept in this component rather than `btn--icon btn--xs` (which is 32px in code, 24px in Figma).

Toggles (2026-11-15, Figma `20819:110498`, `12378:513956`): favourite, compare, `add_favourite_to_list` (selected shows the solid `edit` icon as `icon-btn-compact__on`, enabled shows `favorite` as `__off`; hover fills the heart) and `edit` (hover and selected solid, selected hover grey; Figma hover keeps the primary colour). Compare uses an SVG as `__on`. A toggle sets `aria-pressed`; the page script flips it. A background behind the button (the product card puts it on 50% `surface-00` over the picture) is page-local, never in the component.

## Open flags (for design)

- Figma compare Hover (Large) uses `icon/disabled` grey, Small has no solid colour; the code uses `text-action-primary-hover` for all hover.
- Selected compare is the custom `compare_added_custom` icon in Figma; the card still shows the same `compare_arrows` in every state (the card has no compare toggle yet).
- The hit area equals the icon (20px, below the 24px minimum for pointer targets); Figma has no larger area.
