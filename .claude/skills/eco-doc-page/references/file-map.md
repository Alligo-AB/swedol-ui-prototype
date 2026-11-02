# Docs site file map

```
eco-design-system/
  eyebrow.css              one definition of the eyebrow label style (also used by the root index.html)
  docs.css                 shared styles for every doc page (only file with doc-page CSS). Imports components/css/spacing.css, so every doc page has var(--dimension-spacing-space-md / -lg) (eco-spacing); defines --ds-accent (#E94E19, the ECO DS documentation accent, not in the token package)
  subnav.js                stuck-state hairline + active-section marker for the sticky nav, smooth jump for chips and the side list
  toc.js                   split pages: builds the chip row (below 1024px) and the sticky Contents list (from 1024px) from the headings
  tokens-loader.js         ECO.watch(): load tokens.json and re-render when it changes
  index.html            hub: entry points, summary + live illustration per page
  foundations/colors.html, colors-primitives.html, colors-tokens.html   the first migrated Foundation (2026-10-22): Overview / Primitive colors / Semantic tokens, built by `gen/gen_colors.py`; reference for foundation pages (see "Foundations in the new structure")
  tokens.html   the Tokens category (2026-10-23): one page, no Secondary navigation (`NAV.tokens` has `direct: true` in `docnav.js`); every token of `alligo-design-tokens` parsed live from the package CSS, table from 1024px / cards below it (1 column below 769px, 2 columns in md), search + Filters modal (`ECO_N.openModal`)
  foundations/layout.html, layout-breakpoints.html, layout-spacing.html, layout-tokens.html   the second migrated Foundation (2026-10-22): Grid / Breakpoints / Spacing / Tokens, built by `gen/gen_layout.py` (see "Foundations in the new structure"); replaces the old `foundations/spacing.html` (kept in `gen/old-source/spacing.html`)
  layout-kit.js            shared by the four Layout pages: breakpoint list, scaled grid figure, package reader (global LAYOUT)
  color-kit.js             shared by the three Colors pages: swatch card, Cards / Table switch, primitives read from the token package (global COLORKIT)
  foundations/<name>.html  typography, spacing, elevation, motion …
  components/tooltip.html, tooltip-specifications.html, tooltip-code.html   reference implementation for component pages (three pages, see "Split component pages")
  components/checkbox*.html, input*.html …   the Form components (checkbox, input, textarea, radio, select, switch, tabs, segment-control, range, icon-picker), converted to three pages 2026-10-12: reference for the form-control playground, toggles, states matrix and card treatment
  components/button*.html, button-group*.html   the Actions components (button, button-group), converted to three pages 2026-10-13: reference for a component with variants, sizes, content options and a badge, and for the dark-surface variants
  components/notifications.html (hub) + toast / toast-ecom / modal / banner / inline, each as .html / -specifications.html / -code.html   the Notifications, converted to the three pages 2026-10-13: hub + five type sets like Badge, reference for fixed overlays (modal preview), live motion (toast, banner, inline) and measurement with a status edge
  components/menu*.html, list-item*.html, divider*.html, links-guide.html (hub) + inline-link / action-link / tile-link, each as .html / -specifications.html / -code.html   Menus, lists and dividers and Links, converted to the three pages 2026-10-13 (hub + three types for Links, like Badge and Notifications)
  components/section*.html, collapsible*.html   Layout and content (section, collapsible), converted to three pages 2026-10-14: reference for a layout block with no states (Section) and for a row with live motion (Collapsible)
  components/breadcrumb.html (hub) + breadcrumb-base*.html + breadcrumb-bar*.html   Breadcrumb, converted to the hub + two type sets 2026-10-19 (Badge pattern; see "Breadcrumb is converted")
  components/role-tier-card*.html   the one Draft: three pages like every component, converted 2026-10-15 (see "Drafts" below)
  foundations/docs-table.html   the table of the documentation pages, internal docs pattern, linked only from the root index.html section ECO docs – internal (2026-10-28): one page (see "Drafts" below)
  resources-overview.html + resources/*.html   the third rail category **Resources** (icon `menu_book`, added 2026-10-18; structure from the old Supernova site): hub + Libraries (web, design), Help (getting-help), User guides (introduction-for-developers, introduction-for-stakeholders). One page each, built like a component page without the primary tab bar: `.ds-doc data-subnav="tabs"` wrapper, `section[id]` + `.ds-prose`, `.ds-sep` dividers, `toc.js` (Contents list with link icons, secondary tabs below 1024px). Generated once from a script; edit the HTML directly now. New blocks in docs.css: `.ds-linkcard` (tool card: dark tile with icon + title + line; `--row` variant). The page list lives in `docnav.js` (`NAV.resources`, helper `r()`); footer links (Storybook, Figma, Slack) in the same file. Brand logos are not used: icon tiles stand in (add logos to `images/` if wanted)
  (the component CSS/JS of the form and action components is in the repo-root components/css/ and components/js/, linked by these pages and by prototypes)
  notifications.css, notifications.js   the real component CSS + runtime shared by the notification pages (Code sections print their `@section` blocks live); doc-kit.js = shared page helpers (DK)
```
