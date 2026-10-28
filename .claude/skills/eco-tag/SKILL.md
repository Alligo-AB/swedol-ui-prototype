---
name: eco-tag
description: Use when showing the active filters above a product list or search result — a tag is used ONLY for this. One Remove tag per chosen filter value (× removes it), Grey or White, Medium or Small, focus ring around the tag. Not for categories or labels on content, not for a status, count or marker (use eco-badge), not for choosing filter values (use eco-checkbox), not for actions (use eco-button / links-guide).
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, breakpoints, and the quality checklist.

## Tag (ECO Design System)

Figma: component set `326:7714` (Version Desktop/Mobile × Variant Grey/White × State Default/Remove × Size Medium/Small), info frame `17345:28457`. Read 2026-10-28.

Docs: `eco-design-system/components/tag.html` (+ `-specifications`, `-code`), built by `eco-design-system/gen/gen_tag.py`. Status **In progress** (flags below) — the eyebrow badge and the overview card badge change together.

## When to use / not to use

- **Only for active filters.** A tag shows one filter value the user has chosen, above the product list or search result. Remove is the normal state: the × removes that filter and the list updates at once. Default (no ×) only for a filter that cannot be removed from the tag.
- Row directly above the results, in the order chosen; label = the value name as in the filter ("Gloves", not "Category: Gloves"); a **Clear filters** link at the end from two active filters. Medium by default, Small in dense places (filter drawer). Grey on white, White on grey.
- **Not** for categories or labels on articles/products (text or a link), **not** for a status/count/marker (`eco-badge`), **not** for choosing filter values (`eco-checkbox`, incl. tiles), **not** for actions (`eco-button` / `links-guide`).

## Size model

| Size | State | Height | Padding (t r b l) | Gap label–× | × icon |
|---|---|---|---|---|---|
| Medium | Default | 32px | 9 12 9 12 | – | – |
| Medium | Remove | 32px fixed (`--dimension-spacing-space-32`, Figma updated 2026-10-28) | 8 8 8 12 | 6px below 769px, 8px from 769px | 16px |
| Small | Default | 24px | 5 8 5 8 | – | – |
| Small | Remove | 24px | 4 6 4 8 | 4px | 16px |

Only the Medium Remove gap changes per breakpoint (at `md` 769px, never `sm`).

## Typography

Label: Breuer Condensed 14/14, weight **600** (Figma Bold), letter-spacing **0.28px**, normal case, `ss02 ss03 ss06`, never wraps. Same on every breakpoint. No `eco-typography` style matches (see Flags).

## States

| State | Container | Label | Icon | Notes |
|---|---|---|---|---|
| Default, Grey | `--color-surface-opacity-black-10` | `--color-text-primary` | – | not interactive |
| Default, White | `--color-surface-action-2` | `--color-text-primary` | – | on grey surfaces |
| Remove, Grey | as Default | `--color-text-primary` | `close`, `--color-icon-primary` | × is a `<button>` |
| Remove, White | as Default | `--color-text-primary` | `close`, `--color-icon-primary` | × is a `<button>` |
| Focus (× has `:focus-visible`) | 2px `--color-border-focus` outline around the **whole tag**, offset 2px | `--color-text-primary` | no own ring | `.tag:has(.tag__remove:focus-visible)`; `[data-state="focus"]` forces it on docs pages. Not on mouse click |

Focus added 2026-10-28 on request (not drawn in Figma yet; same token/width/offset as other ECO components). No hover state exists in Figma.

## HTML structure

```html
<link rel="stylesheet" href="/components/css/tag.css">  <!-- both templates already link it -->

<span class="tag">Gloves</span>
<span class="tag tag--sm tag--white">Gloves</span>
<span class="tag tag--remove">Gloves
  <button type="button" class="tag__remove" aria-label="Remove Gloves"><span class="material-symbols-outlined" aria-hidden="true">close</span></button>
</span>
```

Classes: `tag` (Medium Grey), `tag--white`, `tag--sm`, `tag--remove`, `tag__remove`. A group: flex row, `flex-wrap: wrap`, `gap: var(--dimension-spacing-space-8)`. No shared JS: removing is page logic; move focus to the next ×, else the previous one.

## CSS

All rules live in `components/css/tag.css`; never copy them into a page. `.ds-tag` is the docs pages' status chip, not this component.

## Rules

1. Always link `components/css/tag.css`; tokens only (`var(--…)`), literal px only where commented in the file.
2. Never make the whole tag clickable or a link; only the × is a control, a native `<button type="button">`.
3. Always give the × `aria-label="Remove <label>"` and keep the focus ring around the tag (never `outline: none` on `.tag`); the icon is `aria-hidden`.
4. Grey on white surfaces, White on grey surfaces. One size per row.
5. Never use a tag for status (badge) or actions (button/link).
6. Verify at ~375, ~700 and ~1024px: the Medium Remove gap is 6px up to 768px and 8px from 769px.

## Flags (for design)

- **Typography:** 14/14 with 0.28px letter-spacing, normal case, matches no text style in `tokens.json` (Label Large mobile / Alt-Label Small are 14/14 with 0.56px, uppercase).
- **No spacing token** for 9px, 6px and 5px.
- Resolved 2026-10-28: Medium Remove now 32px (was 30px), White Remove no longer 80% opacity, × icon 16px in both sizes (was 14px in Medium).
- **Border:** Figma binds `border-secondary` to White with width 0; no border drawn.
- **Focus not in Figma yet:** built as ring around the whole tag (see States); add the variant in Figma. Hover is open.
