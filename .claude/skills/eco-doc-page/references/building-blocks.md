# Building blocks, spacing and cards

## Contents

- Building blocks in `docs.css`
- Spacing and card treatment
- Cards on component pages

## Building blocks in `docs.css`

| Need | Use |
|---|---|
| Swatch card (chip, name, value, description, copy button) | `.ds-swatch` + `.ds-grid` (4 cols desktop), `.ds-grid--feature` for few large items |
| Ordered scale | `.ds-ramp` |
| Matched sets across variants | `.ds-status` (columns of rows) |
| Hub card with illustration | `.ds-cards` > `a.ds-card` (`.ds-card__visual`, `__body`, `__title`, `__desc`, `__meta`, status as `.badge-basic`, Medium) |
| Not-yet-built hub entry | `div.ds-card.ds-card--soon` + `<span class="badge-basic badge-basic--neutral-grey badge-basic--weak">Soon</span>`, `aria-disabled="true"` |
| Do / Don't figure | `.ds-figs` (2-column grid) with `figure.ds-fig.ds-fig--do` / `.ds-fig--dont`: `.ds-fig__stage` holds a live mini example built from real components (never a screenshot), `figcaption.ds-fig__cap` has a `.ds-fig__ic` (`check_circle` / `cancel`) and one short sentence. Green / red 4px bar on top as `.ds-rule`. A figure that is neither do nor don't is a plain `figure.ds-fig` (no bar, caption without icon); a lone figure goes in `.ds-figs.ds-figs--one` (full width). Page-local classes only for the demo's own layout (reference: the Overview section of `components/tooltip.html`). |
| Running text on a component page (Overview, When to use …) | Put `.ds-prose` on the `.ds-inner` that holds the text. Spacing then follows the Typography article (`foundations/typography.html`), text in Body Large (18/24 mobile, 20/28 desktop): paragraph gap 20px / 16px, above a heading 32px / 24px, heading to text 12px / 8px; a sub-heading straight under its group heading gets only the heading-to-text gap. After a figure (`.ds-figs` with its caption) the next heading or paragraph starts 32px below on mobile and 48px from 769px (`space-32` / `space-48`). Heading levels inside the text block: `.ds-h2` (a further main topic, e.g. Overview then Positioning), `.ds-h3.ds-group` (group heading under an h2: When to use, Alignment), `.ds-h3` (sub-heading under a group heading). Never set paragraph, heading or list margins by hand on such a page. |
| Monospace | Only for code: printed code and CSS (`.ds-code pre`), class names, attribute names and inline `code`. Token names, style names and other labels stay in Breuer (body-sm 14/20 for small labels). |
| Overlays in examples | The sticky on-page nav (`.ds-subnav`) has `z-index: 10`. Anything inside an example must stay below it: `docs.css` sets `--tooltip-z: 9` for tooltips, and a preview of a fixed overlay (modal, toast) is made static with `z-index: auto` (a flex item honors `z-index` even when `position: static`; see `.modal-preview .modal` in `components/modal.html`). Check a new example by scrolling it under the nav. |
| Text sizes | Every font-size / line-height pair on a doc page is a real pair from `tokens.json` (`eco-typography`): mobile and desktop value of one style, e.g. body-md 16/22 → 17/24, body-lg 18/24 → 20/28. Never a mix (17/28 is no style). Check a new rule against the table before writing it, and re-check after. |
| Bullet list in body text | `ul.ds-bullets`: same size, line height, letter-spacing and color as `.ds-desc` (body-lg: 18/24 mobile, 20/28 from 769px), round 8px bullets, 8px between items, as `.ty-list` in the Typography article. A list is never smaller than the text around it. Lists inside a card (`.ds-rule`) follow the card's text size but use the same round 8px bullet (changed 2026-10-14; they had a square 6px one). |
| Mini illustration | `.mini-*` classes (built from tokens). Add a new `.mini-x` in `docs.css` when a new page needs one. |
| Sub-heading / helper text | `.ds-h3`, `.ds-desc` |
| Option group (Mode, Size, Breakpoint …) | `.btn-group` (shared `components/css/button-group.css`, see `eco-button`): a joined group of System buttons, buttons with `aria-pressed`, inside `.ds-toolbar` (page-wide) or `.ds-field` (in `.ds-controls`). **Max 4 options with short labels (the whole group must fit the controls panel on one row), never wrapped.** More options: a `select.form-select.form-select--sm` (`eco-select`) with the same `data-pg` (`DK.seg` and `wireSeg` handle both) |
| Example surface | `.ds-stage` (`--dark` for a dark surface, `--center` to center one example), `.ds-stage__cap` for a small caption (uppercase label-md: 14/14 mobile, 16/16 from 769px; add `.ds-stage__cap--name` when the caption shows a style name and values: normal case, body-sm 14/20) |
| Playground (stage + controls) | `.ds-playground` > `.ds-stage` + `.ds-controls` |
| Icon name field (Material Symbols) | `data-icon-picker` on the input, script `../../components/icon-picker/icon-picker.js`. Spec and rules: `eco-icon-picker`. Never a plain text input. |
| Table (matrix, specs, tokens) | `.ds-table-wrap` > `.ds-table`, see `eco-docs-table`; `.ds-matrix` for a states matrix; `.ds-dot` for a color dot; `.ds-na` for a "not defined" cell |
| Copyable code block | `.ds-code` > `.ds-code__bar` (title + copy button) + `pre` |
| Divider between two white blocks (header → first section, section → section, last section → following block) | **Rule: when two neighbouring blocks are both white, put a divider between them; never when one is grey (the color change is the divider).** Always the inset divider `<div class="ds-sep"><hr class="divider" /></div>` (needs `components/css/divider.css`): same side margin as the sections, never full page width. It goes after the intro section (or after the chip row on pages with `.ds-subnav`), between sections. On pages with `.ds-doc` every divider (under the header and between sections) stops at the text column, not under the Contents list. Overview pages have no Contents list, so their divider runs margin to margin. The line under the primary tab bar (`.ds-tabs`) follows the same rule: it ends with the text column, not under the Contents list (`docs.css`). **A hub page (no tab bar: Badge, Notifications, Links guide, Breadcrumb) has no tab-bar line under the header, so it needs the `.ds-sep` after the intro section explicitly (added to `gen_breadcrumb.py` 2026-10-19; the older hubs still lack it).** Exactly one divider per boundary: never a `.ds-sep` plus a `.ds-divider`. (`.ds-divider`, full width, remains only for older chip-row pages.) |
| Copy control (every place that copies a token, class, value or code) | Always a Blank icon button: `<button type="button" class="mo-copy" aria-label="Copy …"><span class="mo-ic" aria-hidden="true">content_copy</span></button>`; on click the glyph becomes `check` for 1.2 s. Never a text "Copy" link. A token or value shown beside it is `.ds-copyname` > `.ds-copyname__text` + the button. Material Symbols is imported by `docs.css`. |
| Numbered anatomy (markers) | `.ds-fig__stage.ds-callout` holding `.ds-callout__art` (the component at 1×, with room beside or below it for an open tooltip) and `DK.callouts(stage, [{ n, el | box(), side, at, len }])` from `doc-kit.js`. Each part gets a marker as in the Figma "Marker" component: a 24px `.badge-number` (`components/css/badge.css`), a 1px line and a 3px dot on the part (`at: 'edge'` or `'center'`). Fill is `surface-100` (confirmed; Figma `annotation/marker-fill` is being changed to it). Legend: `ol.ds-bullets.ds-bullets--num`, one entry per part (bold name, one sentence). Reference: Overview → Anatomy in `components/tooltip.html`. Figma: Supernova-ECO-DS-Assets, nodes 1703:2207 (example) and 5516:31452 (Marker). |
| Anatomy diagram (8× scale) | `.ds-anatomy` > `.ds-anatomy__fig` + `.ds-anatomy__legend` |

Need a block that does not exist? Add it to `docs.css` with the same conventions (tokens only, mobile-first, `md` = 769px) rather than writing page-local CSS.

## Spacing and card treatment

All values are mobile-first; the larger value applies from 769px (`md`).

| Between | Mobile | Desktop |
|---|---|---|
| `.ds-desc` and the block it introduces (`.ds-stage`, `.ds-table-wrap`, `.ds-playground`, `.ds-layers`, `.ds-ramp`, `.ds-grid`, `.ds-status`) | 12px | 16px |
| Block (or note under it) and the next `.ds-h3` | 32px | 48px |
| `.ds-h3` and the `.ds-desc` after it | 8px | 8px |
| Foundation pages (`data-ds="foundation"`): block and next `.ds-h3` | 56px | 56px |
| `.ds-h3` straight after a `.ds-desc` (section intro) | 0 | 0 |
| Block and the explanatory note under it: `<p class="ds-desc ds-note">` (body-md: 16/22 mobile, 17/24 desktop; changed from 8px to 16px 2026-10-14) | 16px | 16px |

**Cards on component pages** (`data-ds="component"`): `.ds-stage`, `.ds-controls`, `.ds-code`, `.ds-rule` have no 1px frame and use `var(--shadow-elevation-b-20)`, the same elevation as the dashboard stat cards. `.ds-controls` has 24px side padding; `.ds-code__bar` is 56px high with 24px side padding; the Do / Don't cards keep their 4px color bar on top. Tables (`.ds-table-wrap`) get the same treatment on every page type: see `eco-docs-table`.
