# Project – Design Guidelines for Claude Code

## Tech stack
- **HTML + Vanilla JS**
- **Tailwind CSS** for all styling

---

## Precedence over other design skills

The ECO Design System (this file, `tokens.json` via `eco-tokens`, and the `eco-*` component skills) always wins over any other installed design or styling skill (e.g. `design-taste-frontend`, `redesign-existing-projects`, `impeccable`, `frontend-design`, `ui-ux-pro-max`). Such skills may inform *composition* (layout, hierarchy, flow) but never replace ECO's stack, tokens, breakpoints, typography, or motion — for example a default of React/Next.js, a `768px` mobile breakpoint, off-black/off-white instead of the ECO colors, or fonts and easing outside the tokens. If a skill's rule conflicts with an ECO rule, follow ECO and mention the conflict instead of blending the two. See also `prototype-guide` (core principle).

Two design skills are installed globally for other projects (see "Why this section exists" below). Their rules here:

- **`design-taste-frontend`: do not invoke in this repo on your own initiative — only when the user asks for it by name.** It is written for landing pages and portfolios, and its own scope section excludes dashboards and data tables, which much of this repo is. Even when named, use it for composition ideas only.
- **`redesign-existing-projects`: may be used without being asked, but only as a quality checklist**, never as a restyling tool. Use only these parts: *Interactivity and States* (hover/active/focus/loading/empty/error states, dead links, current-page indication), *Strategic Omissions* (skip link, back navigation, form validation, 404), *Code Quality* (semantic HTML, alt text, z-index scale, dead code), and the *alignment* points under *Layout* (buttons bottom-aligned in card groups, shared elements aligned across columns, consistent vertical rhythm, optical alignment). **Ignore** *Typography*, *Color and Surfaces*, *Component Patterns*, *Iconography*, *Upgrade Techniques*, the remaining *Layout* points (symmetry, three-column cards, doubling whitespace, sidebar), and the "Font swap first" step in *Fix Priority*. Fix gaps only with ECO components and tokens.

A vague request like "make the page nicer" is handled with `prototype-guide` and the `eco-*` skills; the `redesign-existing-projects` checklist above may be added on top. Everything in the list below still applies to both skills.

**Suggestions from other design skills that are void here** (each one has an ECO counterpart that wins):
- Font swaps (Inter → Geist, Outfit, etc.) → `eco-typography`
- Replacing pill badges, accordion/FAQ or modals with "more modern" patterns → `eco-badge`, `eco-collapsible`, `eco-modal-ecom`
- No pure black/white, a single accent, tinted shadows, varied border-radius → `eco-colors`, `eco-elevation`, tokens
- Grain, glassmorphism, parallax, inertia scrolling, other motion → `eco-motion`
- Swapping the icon library or simplifying the shared footer/header partials
- React/Next.js, Tailwind v4, or a `768px` mobile breakpoint → this file (HTML + vanilla JS + Tailwind, `md` = 769px)

If a suggestion from any design skill has no matching token or `eco-*` skill, ask before implementing it (same as rule 7 in Quality control).

### Why this section exists (read this if you wonder later)

`design-taste-frontend` and `redesign-existing-projects` (from the `Leonxlnx/taste-skill` repo) were installed globally on 2026-09-19 for projects that do *not* use ECO. Their descriptions are broad ("upgrades existing websites"), so they can trigger on almost any request to change a page here, and their rules contradict ECO (fonts, colors, badges, accordions, breakpoints). This repo is protected by the text in this section (precedence rule, per-skill usage rules, the list of void suggestions, the ask-first rule). It is guidance, not a lock: `CLAUDE.md` is always loaded, but an instruction can still be missed. There is deliberately **no hard block** for now. The two skills are treated differently on purpose: `design-taste-frontend` is for landing pages and portfolios, so it is only used on request; `redesign-existing-projects` is mostly a generic quality audit (states, accessibility, alignment), so its ECO-neutral parts are allowed and its styling parts are not.

**Test first:** ask for something vague like "make this page nicer". Expected: `design-taste-frontend` is not invoked, and if `redesign-existing-projects` is used it only produces checklist-type fixes (missing states, focus, alt text, alignment), not new fonts, colors, badges or layouts. If `design-taste-frontend` is invoked on its own, or `redesign-existing-projects` restyles things, add a hard block to `.claude/settings.json` (`Skill(name)` and `Skill(name *)` under `permissions.deny`; syntax from the Claude Code skills docs, not tested in this repo) or tighten the wording above.

A newly installed design skill should be added to the list of examples in the paragraph above.

---

## Before you build a new page

**Never start from an existing, finished page as the starting point** for a new prototype page — always copy the right template:

| Page type | Starting point | Characteristics |
|---|---|---|
| **Logged-out/public page** | Copy of `template.html` (repo root) | No login required. `body` background: `background-primary` (white). |
| **Logged-in page ("My Pages")** | Copy of `mypages/mypages-template.html` | Requires login, shows the account-nav tabs. `body` background: `background-secondary` (grey) — this is intentional, see rule 7 in the Badge section about `body` background. |

Both templates already have the header/footer/main menu wired up via shared partials (`mypages/partials/`) and every design token in place — never start from scratch, and never copy another page's finished content wholesale, since page-specific CSS/JS hacks that don't belong on the new page will come along with it.

See `index.html` (repo root) for the full sitemap — it's a page overview that links to every page in the prototype and tags each one as "new"/"updated"/"in progress"/"archive" per page type.

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

### Quality control — before delivery

**IMPORTANT:** Go through this list before reporting a new or changed page/component as done. Applies to every page in the project, not just individual features.

1. **Breakpoint check (most important)** — Verify that every new/changed component actually switches at `769px` (`md`), not at `640px` (`sm`) or some other guessed threshold. `sm` (640–768px) must **always** look like mobile (Mobile Base Styling) — never Desktop Base Styling. Never assume the CSS is correct just because it looks reasonable in the code: read the actual `getComputedStyle(...)` values (e.g. via `javascript_tool` in the Browser panel) at at least three widths — an `xs` (~375px), an `sm` (~700px), and an `md`/`lg` (~1024px+) — before calling it done.
2. **Reuse existing tokens/patterns** — Search the file for a component that already solves the same thing (button sizes, drawer chrome, collapsible, checkbox, etc.) before creating a new CSS class. Extend an existing class rather than building a parallel variant.
3. **CSS specificity when nesting** — When a new component is nested inside an existing one (e.g. an icon in a `.form-checkbox-item` label), check that no broader rule (e.g. `.form-checkbox-item span`) leaks through and disturbs the font/color of the nested element.
4. **Spacing duplication** — If several elements that already have their own margin/padding/border are stacked in a flex/grid container with `gap`, check that the gap isn't added on top of the elements' own spacing.
5. **Interaction at every breakpoint** — Test open/close, hover, checkbox/radio selection, etc. at both mobile and desktop width at minimum, not just one window size, before delivery.
6. **Never hardcode design tokens** — Color, spacing (fixed scale values), shadow, and border shorthand must always be written as `var(--...)` against `tokens.json` (see the `eco-tokens` skill), never as a literal hex/px. Every component skill under `.claude/skills/eco-*/SKILL.md` already follows this — keep the pattern when editing a skill. Exceptions require a visible comment explaining why (see e.g. `eco-checkbox`'s flagged non-standard focus color).
7. **Ask before inventing a value** — If a color, size, spacing, or pattern isn't covered by an existing token or skill under `.claude/skills/eco-*/SKILL.md`, ask before choosing a value yourself rather than guessing.

---


## Component library — skills index

> **Missing component?** If you (or Claude) come across a Figma component or pattern that is NOT in the table below: flag it and ask before creating a new skill under `.claude/skills/` — never add a new skill without checking first. Applies equally to new components and to larger changes to an existing one.

Every component in the ECO Design System is its own skill under `.claude/skills/<name>/SKILL.md`. They load automatically when needed — e.g. the button spec (`.claude/skills/eco-button/`) only loads when you're actually building a button — so keep this file thin and never put component-specific CSS templates back in here.

**Before you build anything new**

| Skill | Used when |
|---|---|
| `prototype-guide` | The starting point for ALL creative work — a new prototype, page, product/service page, UI/UX flow, or feature for Swedol, whether the assignment starts from a Figma prototype, a brainstorm, or a spec. Ties together general web-design quality (hierarchy, layout, micro-animation, structured critique) and inspiration references (e.g. Mobbin — structure, never style) with the ECO Design System rules, and routes into the right component skills below. Read this FIRST. |

**Foundational tokens**

| Skill | Used when |
|---|---|
| `eco-tokens` | **Read FIRST, before writing any CSS, color, spacing, shadow, or border value** — whether it's a new prototype or a change to an existing page. Contains `tokens.json`, the single source for `var(--...)` names and values. Never hardcode hex/px when a token exists — see rule 6 in Quality control. |
| `eco-typography` | Use when choosing or reviewing typography/text styles (Body, Alt-Label, Label, Title, Headline, Display) on Desktop vs. Mobile per the ECO Design System. |
| `eco-colors` | Use when choosing or reviewing colors/design tokens — text, icon, background, surface, border, and status colors per the ECO Design System. |
| `eco-spacing` | Use when setting margin, padding, or gap — the fixed Spacing Scale (space-0…space-120) and the breakpoint-adaptive space-sm/space-md/space-lg tokens. |
| `eco-elevation` | Use when choosing shadow/elevation for cards, modals, drawers, tooltips, or other raised surfaces — Shadow Bottom/Top, Designated Level (drawers), and component-specific shadows. |
| `eco-motion` | Use when animating or transitioning something — easing curves (decelerate/accelerate/standard) and duration tokens (fast/medium/slow) per the ECO Design System. |

**Form components**

| Skill | Used when |
|---|---|
| `eco-button` | Use when building, changing, or reviewing buttons (`<button>`, CTAs) in swedol-ui-prototype — all variants (Primary/Secondary/Blank/Destructive/Accent/System), sizes, and states (hover/focus/disabled) per the ECO Design System. |
| `eco-input` | Use when building or reviewing text input fields — sizes (Large/Small/XSmall), all states (enabled/hover/active/focus/error/success/disabled), and label/hint patterns per the ECO Design System. |
| `eco-select` | Use when building or reviewing select fields/dropdowns — sizes, states, and the dropdown arrow per the ECO Design System. |
| `eco-segment-control` | Use when building or reviewing a segmented control (pill toggle) for switching between two related views/filters in the same surface — sizes, the sliding-pill interaction, and states. Never replaces Tabs or Radio buttons. |
| `eco-checkbox` | Use when building or reviewing checkboxes — light mode (standard and the detailed table icon variant) and dark mode, including all states (enabled/hover/focus/selected/indeterminate/disabled). |

**Layout**

| Skill | Used when |
|---|---|
| `eco-section` | Use when building a new section/full-width block in a page layout, including My Pages page-title spacing (main-content/page-preamble) — padding per breakpoint, background (Surface Raised Primary/Secondary), page divider, and the zeroed-padding use case. |

**Notifications**

| Skill | Used when |
|---|---|
| `notifications-guide` | Use BEFORE building a notification, to decide which status (Informational/Success/Warning/Error/Promotion/E-Com) and component type (Banner/Inline/Toast/E-Com Toast/Modal) fits the situation. Then read the skill for the specific component type (eco-banner-notification, eco-inline-notification, eco-toast-system, eco-toast-ecom, or eco-modal-ecom). |
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
| `eco-tooltip` | Use when adding a tooltip to an icon button or other element with no visible text — shown on hover, never on keyboard focus. |
| `eco-collapsible` | Use when building a row-based expandable component/accordion, e.g. an "FAQ" section — header + animated content. |
| `eco-role-tier-card` | Use when building a role card/tier card pair that introduces two tiers within the same category (e.g. Standard/Administrator) side by side and links onward to a full comparison table. |
| `eco-badge` | Use when building a non-interactive status or label indicator (Badge) — e.g. "New", "Updated", "Archive", a role name. Not to be confused with Tag (interactive filtering) or the cart counter's `.badge` class. |
| `eco-breadcrumb` | Use when building breadcrumbs for page-hierarchy navigation — placed directly under the header as the first element in `.page`. |
| `eco-pagination` | Use when building a "load more" pattern for progressively loading more results into a list (reviews, products, order history) — not numbered page navigation. |

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
