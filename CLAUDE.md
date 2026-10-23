# Project – Design Guidelines for Claude Code

## Tech stack
- **HTML + Vanilla JS**
- **Tailwind CSS** for all styling

---

## Precedence over other design skills

The ECO Design System (this file, `tokens.json` via `eco-tokens`, and the `eco-*` component skills) always wins over any other installed design or styling skill (e.g. `design-taste-frontend`, `redesign-existing-projects`, `impeccable`, `frontend-design`, `ui-ux-pro-max`). Such skills may inform *composition* (layout, hierarchy, flow) but never replace ECO's stack, tokens, breakpoints, typography, or motion — for example a default of React/Next.js, a `768px` mobile breakpoint, off-black/off-white instead of the ECO colors, or fonts and easing outside the tokens. If a skill's rule conflicts with an ECO rule, follow ECO and mention the conflict instead of blending the two. See also `prototype-guide` (core principle).

Two design skills are installed globally for other projects (see "Why this section exists" below). Their rules here:

- **`design-taste-frontend`: do not invoke in this repo on your own initiative — only when the user asks for it by name.** It is written for landing pages and portfolios, and its own scope section excludes dashboards and data tables, which much of this repo is. Even when named, use it for suggestions only (composition and content, presented as proposals, see below), never for styling.
- **`redesign-existing-projects`: may be used without being asked, but only as a quality checklist**, never as a restyling tool. Use only these parts: *Interactivity and States* (hover/active/focus/loading/empty/error states, dead links, current-page indication), *Strategic Omissions* (skip link, back navigation, form validation, 404), *Code Quality* (semantic HTML, alt text, z-index scale, dead code), and the *alignment* points under *Layout* (buttons bottom-aligned in card groups, shared elements aligned across columns, consistent vertical rhythm, optical alignment). **Ignore** *Typography*, *Color and Surfaces*, *Component Patterns*, *Iconography*, *Upgrade Techniques*, the remaining *Layout* points (symmetry, three-column cards, doubling whitespace, sidebar), and the "Font swap first" step in *Fix Priority*. Fix gaps only with ECO components and tokens.

A vague request like "make the page nicer" is handled with `prototype-guide` and the `eco-*` skills; the `redesign-existing-projects` checklist above may be added on top. Everything in the list below still applies to both skills.

**Design-skill suggestions are proposals: the person writing the prompt chooses which ones are applied.** Both skills are welcome to suggest improvements, including content and structure ones (shortening text, merging or removing duplicate CTAs, trimming a section, reordering blocks, copy fixes). Present them as a numbered list with a short reason each, and mark the ones that change content or remove something, so the user can answer e.g. "do 1, 3 and 4". Apply nothing from such a list until the user has picked; "yes" or "go ahead" on the whole list counts as picking all of it. Never apply a suggestion on your own just because a skill recommends it. Suggestions that are void here (list below) are not proposed at all.

**Suggestions from other design skills that are void here** (each one has an ECO counterpart that wins):
- Font swaps (Inter → Geist, Outfit, etc.) → `eco-typography`
- Replacing pill badges, accordion/FAQ or modals with "more modern" patterns → `eco-badge`, `eco-collapsible`, `eco-modal-ecom`
- No pure black/white, a single accent, tinted shadows, varied border-radius → `eco-colors`, `eco-elevation`, tokens
- Glassmorphism → `eco-colors`, `eco-elevation` (still void; motion effects, grain and smooth scroll below are not)
- Swapping the icon library or simplifying the shared footer/header partials
- React/Next.js, Tailwind v4, or a `768px` mobile breakpoint → this file (HTML + vanilla JS + Tailwind, `md` = 769px)

**Motion effects (scroll-reveal, text fill on scroll, count-up numbers, timers and countdowns to a campaign start/end, dark/light section transitions, parallax, smooth scroll with Lenis, grain) are not void; they are proposals, by page type:**

| Page | Does Claude propose the effect? |
|---|---|
| Campaign / landing page | Yes, actively, as a numbered proposal with a short reason (e.g. focus on the CTA, conversion). Claude also suggests other fitting modern campaign techniques here, not only the ones listed |
| Regular public page | Only if the user asks |
| Logged-in page (My Pages), forms, tables | No. Effects disturb the workflow |

Proposals follow the rule above: nothing is applied until the user picks. Once picked, the effect is built under the conditions in `eco-motion` ("Campaign motion"): ECO easing/duration tokens only, `prefers-reduced-motion` turns it off, xs/sm checked separately, nothing hides content or blocks CTAs and forms. A campaign page is still a public page (copy of `template.html`); campaign motion is an add-on, not a new page type. 3D scenes, pinned scenes and extra libraries are out of scope until a concrete project needs them (ask first).

If a suggestion from any design skill has no matching token or `eco-*` skill, ask before implementing it (same as rule 7 in Quality control).

### Identity is fixed, solutions are open

Two layers, so ECO protects the brands without blocking good ideas:

1. **Identity: always ECO, no exceptions without asking.** Colors, typefaces, foundations (spacing, elevation, breakpoints, motion tokens) and components. They are how the brands **Swedol** and **Tools** are shown correctly (Tools has its own brand primitives, see `eco-colors` and `foundations/colors.html`). Never replace or tint them.
2. **Solutions: open to proposals.** Layout, composition, flow, effects, campaign techniques, new patterns, copy structure and improvements nobody has thought of yet are welcome. Claude should speak up when it sees a better way, even if no rule mentions it.

How to read a rule here: a rule that says "never" protects identity (layer 1). A rule about *how* something is built (layer 2) is a default, not a ban. If an idea fits neither a token nor a skill, it is not refused: Claude proposes it as a numbered item with a short reason and what it would need (a new token, a new pattern in a skill), and the user picks (same as the proposals rule above and rule 7 in Quality control). If a rule seems to block a good idea, say so and propose changing the rule, instead of silently following or breaking it. A picked idea that proves itself is added to the matching skill and to this file.

### Why this section exists (read this if you wonder later)

`design-taste-frontend` and `redesign-existing-projects` (from the `Leonxlnx/taste-skill` repo) were installed globally on 2026-09-19 for projects that do *not* use ECO. Their descriptions are broad ("upgrades existing websites"), so they can trigger on almost any request to change a page here, and their rules contradict ECO (fonts, colors, badges, accordions, breakpoints). This repo is protected by the text in this section (precedence rule, per-skill usage rules, the list of void suggestions, the ask-first rule). It is guidance, not a lock: `CLAUDE.md` is always loaded, but an instruction can still be missed. There is deliberately **no hard block** for now. The two skills are treated differently on purpose: `design-taste-frontend` is for landing pages and portfolios, so it is only used on request; `redesign-existing-projects` is mostly a generic quality audit (states, accessibility, alignment), so its ECO-neutral parts are allowed and its styling parts are not. Content and structure suggestions from either skill (e.g. shorter text) are welcome, but only as proposals: the person writing the prompt picks which ones are applied (see the proposals rule above). This was added after a test on `mypages/users.html`, where the skill proposed to do some content changes (removing a CTA, trimming copy, removing an accordion) directly.

**Test first:** ask for something vague like "make this page nicer". Expected: `design-taste-frontend` is not invoked, and if `redesign-existing-projects` is used it only produces checklist-type fixes (missing states, focus, alt text, alignment), not new fonts, colors, badges or layouts. If `design-taste-frontend` is invoked on its own, or `redesign-existing-projects` restyles things, add a hard block to `.claude/settings.json` (`Skill(name)` and `Skill(name *)` under `permissions.deny`; syntax from the Claude Code skills docs, not tested in this repo) or tighten the wording above.

A newly installed design skill should be added to the list of examples in the paragraph above.

---

## Before you build a new page

**Never start from an existing, finished page as the starting point** for a new prototype page — always copy the right template:

| Page type | Starting point | Characteristics |
|---|---|---|
| **Logged-out/public page** | Copy of `template.html` (repo root) | No login required. `body` background: `background-primary` (white). |
| **Logged-in page ("My Pages")** | Copy of `mypages/mypages-template.html` | Requires login, shows the account-nav tabs. `body` background: `background-secondary` (grey) — this is intentional, see rule 7 in the Badge section about `body` background. |

Both templates carry only the page frame (header, footer, menu, drawers, breadcrumb) plus links to the shared component CSS; page-specific content CSS (user cards, stat cards, upload, tooltips, pagination, collapsibles …) was removed in 2026-10 and lives in each page or in the component's skill. Both templates already have the header/footer/main menu wired up via shared partials (`mypages/partials/`) and every design token in place — never start from scratch, and never copy another page's finished content wholesale, since page-specific CSS/JS hacks that don't belong on the new page will come along with it.

See `index.html` (repo root) for the full sitemap — it's a page overview that links to every page in the prototype and tags each one as "new"/"updated"/"in progress"/"archive" per page type.

**Component CSS and JS (shared, one source):** every component's CSS lives in `components/css/<name>.css` (button, input, select, textarea, checkbox, radio, switch, list-item, divider, menu, collapsible, tooltip, pagination, inline-link, action-link, tile-link, breadcrumb, pill-segment-control, role-tier, table, section, badge, range, button-group, tabs) and its behaviour JS in `components/js/` (`select-menu.js`, `collapsible.js`, `pagination.js`, `range.js`, `pill-segment-control.js`, `tooltip.js`, `tabs.js`; the icon picker in `components/icon-picker/`). The Specifications measurement figure (blueprint style) is `components/css/measure.css` + `components/js/measure.js` (skill `eco-doc-page`, section Measurements). Layout spacing `space-md` / `space-lg` (breakpoint-adaptive) is `components/css/spacing.css`, used as `var(--dimension-spacing-space-md)`; never hand-write its per-breakpoint pixel values (skill `eco-spacing`). Notifications use `eco-design-system/notifications.css` + `notifications.js` (a button inside a notification is always 32px, scoped in that file). The templates already link them. In a new page: `<link rel="stylesheet" href="/components/css/<name>.css">` for each component used, root-absolute, never a copy of the rules in the page. The ECO docs pages in `eco-design-system/` link the same files, so docs and product cannot drift. Changing a component means editing that file.

**Hero banner (2026-10-22):** a pattern in the Patterns group (`components/hero-banner-widget*.html`: Design / Usage / Reference and Examples / Storyblok), with a second link **Hero banner widget** under the Storyblok widget group that points to its Storyblok tab, built by `eco-design-system/gen/gen_hero_banner_widget.py` with the custom page set of `build.py`. Measurements, colors, logos and graphics come from the Figma links the user gives, not from the Supernova text (see `eco-doc-page`).

**Docs categories:** the ECO docs rail (`eco-design-system/docnav.js`, `NAV`) has four categories: Foundations, Components, Tokens (one page, no panel) and Resources (`resources-overview.html` + `resources/`: Libraries Web/Design, Getting help, User guides for developers and stakeholders; see `eco-doc-page`). New link-card block `.ds-linkcard` is in `docs.css`.

**Foundations in the new structure (2026-10-22):** Colors is the first migrated Foundation: `eco-design-system/foundations/colors.html` (Overview), `colors-primitives.html` and `colors-tokens.html`, same frame as a component page but with its own tabs (a foundation needs no Specifications/Code tab; may be one page), built by `gen/gen_colors.py`, shared script `color-kit.js`, rules in `eco-doc-page` ("Foundations in the new structure"). **Layout is the second (2026-10-22):** `foundations/layout.html` (Grid), `layout-breakpoints.html`, `layout-spacing.html` (the old Spacing page, moved in) and `layout-tokens.html`, built by `gen/gen_layout.py`, shared script `layout-kit.js`; the Foundations nav shows one item **Layout** instead of Spacing. Typography, elevation and motion are still single pages.

**Framed docs layout (2026-10-23, proof of concept applied to every docs page with the navigation):** from 961px the content is a white panel (`body`) on a grey surround (`html`, `--color-surface-02`, the table-header grey), with a 1px `--color-border-primary` border and 16px radius on all four sides, 16px gap around it. The rail is grey too (hover `--color-surface-05`); the footer is moved out of `body` onto the grey. The overlay (hover) panel has no shadow and a drawn right edge; an absolutely placed inverse-corner piece (`.dn::after`) carries the panel's rounded corner out with it at the top of the page. Switched on by `docnav.js` (`html.ds-frame`), styled in `docnav.css`; below 961px nothing changes. Pages without `docnav.js` (typography, elevation, motion) keep the old look until they are migrated.

**Tokens page (2026-10-23):** `eco-design-system/tokens.html`, its own rail category **Tokens** (`NAV.tokens` in `docnav.js` with `direct: true`: the rail item links straight to the page, no Secondary navigation panel, in the mobile drawer a plain row). It lists every token of `alligo-design-tokens` (the eight `dist/css/base/*.css` files, parsed live in the page) plus the motion tokens of `docs.css`, as a table (preview, token, value, category badge, copy `var(--…)`) from 1024px (lg) and as one card per token below it (one column below 769px, two columns 769–1023px, the md range). Search box and a **Filters** button that opens a right-hand drawer at every width (page-local `.tk-drawer`, built like the drawers on `mypages/users.html`: header and footer padding 24px top/bottom and 32px left/right from 769px, 16px and 24px below, content 0/32/32 and 0/24/24, `--shadow-elevation-drawer-right`; 16px of air around it on desktop for this docs site only, full screen on mobile); the choices are List Items (`eco-list-item`, check box + label, count as trailing text tertiary), in the drawer they apply at once and the button only closes. A category with `direct: true` needs no `groups`.

**Drawers (rule, 2026-10-23):** every drawer is built like the ones on `mypages/users.html`, at once and with these values. Desktop (769px+): header `24px 32px`, content `0 32px 32px` with `24px` gap, footer `24px 32px`; title `display-sm` 26/26 uppercase, close button 40px (`btn--sm btn--icon` Blank), footer button full width `btn--sm` (40px) primary, header gets `elevation-b-60` when the content scrolls, footer has `elevation-t-60`. Mobile/tablet (below 769px): header `16px 24px`, content `0 24px 24px` with `16px` gap, footer `16px 24px`; title 22/22, close `btn--md`, footer button `btn--lg` (48px). Panel 500px wide (max 100%), `--shadow-elevation-drawer-right`, sharp corners, `drawer-right` slides in with `ease-decelerate-emphasized` / `duration-medium-3`. On the docs site only, a drawer may float with 16px of air around it on desktop (reference: `tokens.html`). Lists inside use `eco-list-item`.

**Docs dividers:** when two neighbouring blocks on a docs page are both white (header and first section, two sections, last section and what follows), put a divider between them (the inset `.ds-sep` + `divider`, never full page width, exactly one line per boundary); when one of them is grey, the color change is the divider and no line is added. Details in `eco-doc-page`.

**Sticky tab bar (docs pages):** when a tab bar sticks to the top it gets 16px above the tabs and 16px of background below its line (`.is-stuck`: `padding-top: 16px` plus `box-shadow: 0 16px 0` in the surface colour; `margin-bottom` is reduced so the content does not move). Component pages: `.ds-subnav--tabs.is-stuck` in `docs.css`; `index.html` and `components-overview.html`: inline rule and script in the page. Details in `eco-doc-page`.

**Images:** all images live in one folder, `images/` in the repo root. Reference them as `/images/<file>` (root-absolute) in `mypages/` pages and all partials, since partials are injected into both root and `mypages/` pages. Never create a per-folder `images/` copy (no `mypages/images/`, `tokens/images/`). Exception: `email/images/`, separate on purpose for email HTML. Requires the server to run from the repo root (`npx serve .`).

---

## Breakpoints (ECO Design System)

The ECO Design System has **5 breakpoints** covering Mobile, Tablet, and Desktop.

| Token | Device | Width | Columns | Gutter | Margin |
|---|---|---|---|---|---|
| `breakpoint-xs` | Mobile | 0–639px *(min 375px)* | 4 | 8px | 16px |
| `breakpoint-sm` | Tablet | 640–768px | 8 | 16px | 32px |
| `breakpoint-md` | Desktop Small | 769–1023px | 12 | 24px | 32px |
| `breakpoint-lg` | Desktop | 1024–1280px | 12 | 24px | 40px |
| `breakpoint-xl` | Desktop XL | 1281px+ | 12 | 24px | ∞ |

> Mobile (`xs`) and Tablet (`sm`) use *Mobile Base Styling*.
> Desktop Small, Desktop, and Desktop XL use *Desktop Base Styling*.

### Tailwind config
```js
module.exports = {
  theme: {
    screens: {
      sm:  '640px',   // Tablet
      md:  '769px',   // Desktop Small
      lg:  '1024px',  // Desktop
      xl:  '1281px',  // Desktop XL
    },
  },
}
```

Live docs for the grid, the five breakpoints and the layout tokens: `eco-design-system/foundations/layout.html` and `layout-breakpoints.html` (skill `eco-doc-page`, section Layout).

### Approach: Mobile-first

**Always** write the mobile style first (no prefix), then build up with `sm:`, `md:`, `lg:`, `xl:`.

```html
<!-- Margin per breakpoint -->
<section class="px-[16px] sm:px-[32px] lg:px-[40px]">...</section>

<!-- Grid columns per breakpoint -->
<div class="grid grid-cols-4 sm:grid-cols-8 md:grid-cols-12 gap-[8px] sm:gap-[16px] md:gap-[24px]">...</div>

<!-- Visibility -->
<nav class="hidden md:block">...</nav>
<button class="block md:hidden">☰</button>
```

### Rules

1. **Mobile-first** – mobile style with no prefix, then `sm:` → `md:` → `lg:` → `xl:`.
2. **Inline in HTML** – all styling with Tailwind classes directly in markup.
3. **Components** – buttons, typography, etc. change size at `md:` (Desktop Small). See the component sections below.

### Working routine (every task)

1. **Ask first** when a request can mean two things (for example Pill Segment Control vs button group).
2. **Verify before saying done:** mobile (~375px) and desktop (1200px), real mouse hover/click and keyboard (Tab), not only scripts. Check neighbours that share the file (other variants, other pages). State what was not tested.
3. **Sweep afterwards:** grep `.claude/skills/` and this file for old names or behaviour, update every affected skill and index row in the same turn, and name which ones changed.

### Quality control — before delivery

**IMPORTANT:** Go through this list before reporting a new or changed page/component as done. Applies to every page in the project, not just individual features.

1. **Breakpoint check (most important)** — Verify that every new/changed component actually switches at `769px` (`md`), not at `640px` (`sm`) or some other guessed threshold. `sm` (640–768px) must **always** look like mobile (Mobile Base Styling) — never Desktop Base Styling. Never assume the CSS is correct just because it looks reasonable in the code: read the actual `getComputedStyle(...)` values (e.g. via `javascript_tool` in the Browser panel) at at least three widths — an `xs` (~375px), an `sm` (~700px), and an `md`/`lg` (~1024px+) — before calling it done.
2. **Reuse existing tokens/patterns** — Check `components/css/` and `components/js/` first (link the shared file, do not rewrite it), then search the file for a component that already solves the same thing (button sizes, drawer chrome, collapsible, checkbox, etc.) before creating a new CSS class. Extend an existing class rather than building a parallel variant.
3. **CSS specificity when nesting** — When a new component is nested inside an existing one (e.g. an icon in a `.form-checkbox-item` label), check that no broader rule (e.g. `.form-checkbox-item span`) leaks through and disturbs the font/color of the nested element.
4. **Spacing duplication** — If several elements that already have their own margin/padding/border are stacked in a flex/grid container with `gap`, check that the gap isn't added on top of the elements' own spacing.
5. **Interaction at every breakpoint** — Test open/close, hover, checkbox/radio selection, etc. at both mobile and desktop width at minimum, not just one window size, before delivery.
6. **Never hardcode design tokens** — Color, spacing (fixed scale values), shadow, and border shorthand must always be written as `var(--...)` against `tokens.json` (see the `eco-tokens` skill), never as a literal hex/px. Every component skill under `.claude/skills/eco-*/SKILL.md` already follows this — keep the pattern when editing a skill. Exceptions require a visible comment explaining why (see e.g. `eco-checkbox`'s flagged non-standard focus color).
7. **Ask before inventing a value** — If a color, size, spacing, or pattern isn't covered by an existing token or skill under `.claude/skills/eco-*/SKILL.md`, ask before choosing a value yourself rather than guessing.
8. **Button label in a span** — every `.btn` label sits in `<span class="btn__label">` (also for buttons built in JS: `innerHTML`, change the text on the span, never `button.textContent`). Without it the 8px label inset is missing and the text sits too tight against the edge. See `eco-button`.
9. **Button beside a field = same height** — a button in the same row as an input/select uses the matching size: Input Large → `btn--md`, Small → `btn--sm`, XSmall → `btn--xs` (never `btn--lg` next to a Large input). Verify with `offsetHeight`. See `eco-button` rule 8 and `eco-input` rule 5.

---


## Component library — skills index

> **Missing component?** If you (or Claude) come across a Figma component or pattern that is NOT in the table below: flag it and ask before creating a new skill under `.claude/skills/` — never add a new skill without checking first. Applies equally to new components and to larger changes to an existing one.

Every component in the ECO Design System is its own skill under `.claude/skills/<name>/SKILL.md`. They load automatically when needed — e.g. the button spec (`.claude/skills/eco-button/`) only loads when you're actually building a button — so keep this file thin and never put component-specific CSS templates back in here.

**Before you build anything new**

| Skill | Used when |
|---|---|
| `prototype-guide` | The starting point for ALL creative work — a new prototype, page, product/service page, UI/UX flow, or feature for Swedol, whether the assignment starts from a Figma prototype, a brainstorm, or a spec. Ties together general web-design quality (hierarchy, layout, micro-animation, structured critique) and inspiration references (e.g. Mobbin — structure, never style) with the ECO Design System rules, and routes into the right component skills below. Read this FIRST. |

**Adding to the design system**

| Skill | Used when |
|---|---|
| `eco-add-component` | Use when adding a NEW component (a new `eco-*` skill from a Figma component) or substantially changing an existing one — Figma extraction → token mapping → skill template → CLAUDE.md index → verification checklist. Read this FIRST so every component skill keeps the same standard. |
| `eco-card-animation` | Use when making an animated Hairline illustration (isometric line figure answering the pointer) for a component and putting it on its card on the ECO overview pages: procedure from concept to card, reusable files in `hairline/` (`make-eco.mjs`, `tools/card-check.mjs`, `embed.js`, `hairline-card.css`), ECO colouring, hover-triggered tour (no play button), archiving the old card visual, verification. References: Button and Switch. |
| `eco-doc-page` | Use when building or changing a documentation/showcase page for the ECO Design System (foundations like colors, components like button/radio) in `eco-design-system/` — page structure, section order, shared `docs.css` classes, spacing and card rules, the component-page template (playground, variants, states matrix, specs, code, usage; reference: `components/checkbox.html`), and the split three-page structure every component page uses (Examples & Guidelines / Specifications / Code, tabs, sticky Contents list outside the 1200px content (with a link icon on every heading that copies its URL and shows a toast), white sections with dividers, on-page secondary tab bar via `data-subnav="tabs"`, `--ds-accent`; Measurements section; reference: `components/tooltip*.html`; an existing one-page component page is converted when you ask to update it; Form, Actions, Notifications, Menus, lists and dividers, Links and Layout and content (section, collapsible) components are converted, with the generator in `eco-design-system/gen/`; Role tier card is the one Draft and is converted too; the Docs table is a docs-only page in `foundations/` and stays one page), live-from-tokens rules, overview hub, registration in index.html. |

**Reviewing what developers built**

| Skill | Used when |
|---|---|
| `design-review` | Comparing a developer-built page/component (UAT/staging URL or code) against the Figma design (one frame per breakpoint) and the ECO rules, and producing a severity-grouped report for the developers — as a file and/or Jira comment, optionally with annotated Figma-vs-implementation images and a placement guide for where each image goes in the comment. |

**Foundational tokens**

| Skill | Used when |
|---|---|
| `eco-tokens` | **Read FIRST, before writing any CSS, color, spacing, shadow, or border value** — whether it's a new prototype or a change to an existing page. Contains `tokens.json`, the single source for `var(--...)` names and values. Never hardcode hex/px when a token exists — see rule 6 in Quality control. |
| `eco-typography` | Use when choosing or reviewing typography/text styles (Body, Alt-Label, Label, Title, Headline, Display) on Desktop vs. Mobile per the ECO Design System. |
| `eco-colors` | Use when choosing or reviewing colors/design tokens — text, icon, background, surface, border, and status colors per the ECO Design System. |
| `eco-spacing` | Use when setting margin, padding, or gap — the fixed Spacing Scale (space-0…space-120) and the breakpoint-adaptive space-md/space-lg tokens (`components/css/spacing.css`, `var(--dimension-spacing-space-md)`; no sm/xs/xl yet). |
| `eco-elevation` | Use when choosing shadow/elevation for cards, modals, drawers, tooltips, or other raised surfaces — Shadow Bottom/Top, Designated Level (drawers), and component-specific shadows. |
| `eco-motion` | Use when animating or transitioning something — easing curves (decelerate/accelerate/standard) and duration tokens (fast/medium/slow) per the ECO Design System. Also "Campaign motion": scroll-reveal, text fill, count-up, timers/countdowns and parallax as user-picked proposals (campaign pages yes, regular public pages on request, My Pages/forms/tables no), with conditions. |

**Actions**

| Skill | Used when |
|---|---|
| `eco-button` | Use when building, changing, or reviewing buttons (`<button>`, CTAs) and icon buttons in swedol-ui-prototype — all variants (Primary/Secondary/Blank/Destructive/Accent/System and the three Inverted ones), sizes (Large/Medium/Small/XSmall), content (label, icons, icon only, badge) and states (hover/focus/disabled) per the ECO Design System. Also the button group (joined toggle buttons, `components/css/button-group.css`): when a group does not fit its container, never change the button design, show an `eco-select` instead. Documentation is three pages (Examples & Guidelines / Specifications / Code), with when to use and avoid each variant, combining variants, label writing and state definitions. Not for links (use links-guide) or a switch between two views (use eco-pill-segment-control). |

**Form components**

| Skill | Used when |
|---|---|
| `eco-input` | Use when building or reviewing text input fields — sizes (Large/Small/XSmall), all states (enabled/hover/active/focus/error/success/disabled), and label/hint patterns per the ECO Design System. |
| `eco-icon-picker` | Use when a field must hold a Material Symbols icon name (icon for a banner, notification, menu item, tile or category) — click/Tab into it and a panel opens on top with instant search over all icons, Recent and Popular. One script, `components/icon-picker/icon-picker.js`, for prototypes, back-office forms and docs playgrounds alike. |
| `eco-textarea` | Use when building or reviewing a multi-line text area (comments, feedback, long free text) — label with optional word count, all states (enabled/hover/active/focus/error/success/disabled), resizer and message per the ECO Design System. Not for single-line text (use eco-input) or choosing from a list (use eco-select). |
| `eco-select` | Use when building or reviewing select fields/dropdowns — sizes, states, and the dropdown arrow per the ECO Design System. |
| `eco-pill-segment-control` | Use when building or reviewing a segmented control (pill toggle) for switching between two related views/filters in the same surface — sizes, the sliding-pill interaction, and states. Never replaces Tabs (`eco-tabs`) or Radio buttons (`eco-radio`). Not the framed button group (see `eco-button`). |
| `eco-checkbox` | Use when building or reviewing checkboxes — light mode (standard and the detailed table icon variant) and dark mode, including all states (enabled/hover/focus/selected/indeterminate/disabled) Also the tile variants for PDP and filtering (Color swatch, Image, Number). |
| `eco-switch` | Use when building or reviewing a switch (toggle switch) — an immediate on/off control for a single binary setting. Sizes (Large/Small/X-Small), light and dark mode, all states (enabled/hover/focus/disabled × off/on), label. Not for choosing between options (use eco-radio) or multi-select/form submission (use eco-checkbox). |
| `eco-radio` | Use when building or reviewing radio buttons — a list of two or more mutually exclusive options where exactly one can be chosen. Sizes (Large/Small), all states (enabled/hover/focus/selected/selected hover/selected focus/disabled/disabled selected), label + optional hint message. |
| `eco-range` | Use when the user picks one value from an ordered series of steps (easing, duration, size, a number between a minimum and a maximum) by dragging a thumb along a track, with the current value and optional tick labels. Native `<input type="range">` + `components/css/range.css` + `components/js/range.js`, for prototypes, back-office forms and docs playgrounds alike. Not for two or three named options (use eco-pill-segment-control / eco-radio), on/off (eco-switch) or typed numbers (eco-input). |

**Layout**

| Skill | Used when |
|---|---|
| `eco-section` | Use when building a new section/full-width block in a page layout, including My Pages page-title spacing (main-content/page-preamble) — padding per breakpoint, background (Surface Raised Primary/Secondary), page divider, and the zeroed-padding use case. |

**Notifications**

| Skill | Used when |
|---|---|
| `notifications-guide` | Use BEFORE building a notification, to decide which status (Informational/Success/Warning/Error/Promotion/E-Com), component type (Banner/Inline/Toast/E-Com Toast/Modal) and emphasis (Weak is the default, Strong sparingly; the "Choosing the emphasis" guide) fits the situation. Then read the skill for the specific component type (eco-banner-notification, eco-inline-notification, eco-toast-system, eco-toast-ecom, or eco-modal-ecom). |
| `eco-toast-system` | Use when building a system-generated Toast notification — short-lived, time-based feedback on a user action (save/send/delete) that slides in/out and auto-closes. |
| `eco-inline-notification` | Use when building an inline notification that should stay in page context until the user acts or the state changes — not short-lived feedback (use toast-system for that). |
| `eco-banner-notification` | Use when building a page-wide banner notification at the top of the page (maintenance/outage/campaign) or a rich My Pages dashboard banner — Size Small/Large, Emphasis Strong/Weak/Weaker per status, and Promotion (Dark/Light/Strong/Weak) for brand campaigns. |
| `eco-modal-ecom` | Use when building a modal (E-Com Modal) that requires confirmation or an active choice before the user can continue — not for short-lived feedback or status information in page context. |
| `eco-toast-ecom` | Use when building an e-commerce toast — e.g. "product added to cart" (Add to cart variant with product image) or "added to wishlist" (Informational variant, black background). |

**Links**

| Skill | Used when |
|---|---|
| `links-guide` | Use BEFORE building a link, to decide whether it should be an Inline Link (in body text), Action Link (standalone), or Tile Link (graphical/prominent). Then read the skill for the specific link type. |
| `eco-action-link` | Use when building a standalone clickable link with an optional left/right icon that is NOT in body text — e.g. "View all products →". |
| `eco-inline-link` | Use when building a link inside a sentence or text block — always underlined in the enabled state, never with an icon. |
| `eco-tile-link` | Use when building a graphical/prominent link presented as a card or button — brand logos, icon+label tiles. Does not replace regular buttons or in-text link types. |

**Other components**

| Skill | Used when |
|---|---|
| `eco-menu` | Use when building or reviewing a menu surface — the dropdown list that opens from a button/action (Dropdown menu) or from a Select field (Exposed dropdown menu). Base Item (Select / Multi Select, Enabled/Hover/Selected), Menu Item Divider (Middle-inset/Full-width/No), sizes, scrollbar and elevation. Not for the closed select field itself (use eco-select) and not for page navigation. |
| `eco-list-item` | Use when building or reviewing the content of one row in a list surface (List Item) — optional leading element (icon, check box, radio, color swatch, swatch frame, image), label (regular/bold) and optional trailing element (icon, secondary or tertiary text, check box, radio, switch), plus optional overline and supporting text. Used inside Menu, Overflow menu, List Picker, Drawer link and Filter sections. Not for the row container (height, divider, hover, focus: use eco-menu) and not for a standalone checkbox/radio (use eco-checkbox / eco-radio). |
| `eco-divider` | Use when separating content groups with a thin line (Divider) — horizontal between sections/list items, vertical between side-by-side items. Three colors (Border Primary/Secondary/Tertiary). Not for section boundaries that already have their own padding (see eco-section `.page-divider`) and not a replacement for whitespace, headings or labels. |
| `eco-tooltip` | Use when adding a tooltip to an icon button or other element with no visible text — shown on hover and on keyboard focus (`:focus-visible`), Esc hides it. Also the global `data-tooltip` tooltip (`components/js/tooltip.js`, use it for icon buttons and table rows; never write a tooltip script of your own) and the rules for when to use one and when not to (critical information, interactive content). |
| `eco-collapsible` | Use when building a row-based expandable component/accordion, e.g. an "FAQ" section or a filter group — header (title, descriptive text, icons, toggle switch, number badge, chevron) + animated content. Sizes Large/Small, Boxed, Dark, Disabled; checked against Figma 2026-10-14. |
| `eco-role-tier-card` | **Draft / experiment, not an official component** (Drafts group in the docs, three pages like every component). Use when building a role card/tier card pair that introduces two tiers within the same category (e.g. Standard/Administrator) side by side and links onward to a full comparison table. |
| `eco-badge` | Use when building a non-interactive status, label, count or marker (Badge): Basic, Dot, Number, and the e-commerce Product & Discount and Purchase Info. Five types, a hub page and one three-page set each. Not to be confused with Tag (interactive filtering) or the cart counter's `.badge` class. |
| `eco-docs-table` | **The table of the documentation pages, not a product component** (renamed from `eco-table` 2026-10-15; page `Docs table`, the Documentation group under Patterns, one page; a product table is planned). Use when building a data table (rows and columns of text, check icons or small controls) — row and header heights, cell padding, lines, header background, the soft inset shadow on the header's top edge and the card shadow. A first version: more variants and states (sorting, selection, sticky header, empty state) are added later. |
| `eco-breadcrumb` | Use when building breadcrumbs for page-hierarchy navigation — placed directly under the header as the first element in `.page`. |
| `eco-tabs` | Use when building or reviewing tabs — a tab bar of Primary or Secondary tab items that switches content in the same context, or serves as sub-navigation (e.g. the My Pages account nav), or navigates the sections of one long page (on-page navigation, `tab-bar--page`). Sizes (Large/Medium/Small), configurations (label, label + icon, icon only), states (enabled/hover/active), dot and number status, overflow. Not for sequential steps (use a stepper), not for a two-view toggle (use eco-pill-segment-control), not for choosing form values (use eco-radio / eco-select). |
| `eco-pagination` | Use when building a "load more" pattern for progressively loading more results into a list (reviews, products, order history) — not numbered page navigation. Documentation is three pages (Examples & Guidelines / Specifications / Code), checked against Figma 2026-10-19. |

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
