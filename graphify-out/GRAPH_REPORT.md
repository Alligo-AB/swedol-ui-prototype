# Graph Report - swedol-ui-prototype  (2026-10-14)

## Corpus Check
- 101 files · ~977,797 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 648 nodes · 916 edges · 68 communities (42 shown, 10 thin omitted)
- Extraction: 92% EXTRACTED · 8% INFERRED · 0% AMBIGUOUS · INFERRED: 69 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `8389e1de`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Shared header partial
- Section
- Component library skills index
- eco-doc-page skill
- notifications.js
- doc-kit.js
- docnav.js
- Design review: implementation vs. Figma + ECO
- generate-tokens.py
- System Inline Notification
- List Item (ECO Design System)
- Menu – Dropdown & Exposed Dropdown (ECO Design System)
- attach
- Table (ECO Design System) — first version
- build.py
- Divider (ECO Design System)
- Switch (ECO Design System)
- Tabs (ECO Design System)
- Text Area (ECO Design System)
- Adding a component to the design system
- Pill Segment Control (ECO Design System)
- Radio button (ECO Design System)
- tabs.js
- Checkbox
- notif.py
- compose-helpers.py
- tooltip.js
- gen_button.py
- link_large
- Icon picker (ECO Design System)
- Range (ECO Design System)
- btn_group
- select-menu.js
- toc.js
- upload-jira-images.sh
- pill-segment-control.js
- init
- run
- watch
- Duration tokens fast/medium/slow
- tokens/_test.html (unused placeholder)
- old_js
- gen_links_guide.py
- Action Link
- Role Card / Tier Card pair
- gen/README.md
- ECO semantic color tokens
- Section padding per breakpoint first vs other
- Button
- Breadcrumb
- gen_notifications.py
- toolbar

## God Nodes (most connected - your core abstractions)
1. `eco-doc-page skill` - 24 edges
2. `Shared header partial` - 17 edges
3. `Users page (Användare)` - 17 edges
4. `index.html site overview (sitemap)` - 16 edges
5. `mypages-template.html (logged-in page template)` - 15 edges
6. `Reviews page (Recensioner)` - 14 edges
7. `Shared account-nav drawer partial` - 13 edges
8. `Shared footer partial` - 13 edges
9. `template.html (public page template)` - 13 edges
10. `List Item (ECO Design System)` - 12 edges

## Surprising Connections (you probably didn't know these)
- `Reviews page backup 1` --semantically_similar_to--> `Reviews page (Recensioner)`  [INFERRED] [semantically similar]
  reviews_backup_1.html → reviews.html
- `Reviews page backup 2` --semantically_similar_to--> `Reviews page (Recensioner)`  [INFERRED] [semantically similar]
  reviews_backup_2.html → reviews.html
- `Feature comparison page (earlier version)` --semantically_similar_to--> `Feature comparison roles page (Jamfor behorighetsnivåer)`  [INFERRED] [semantically similar]
  feature-comparison.html → feature-comparison-roles.html
- `Feature comparison roles page (backup)` --semantically_similar_to--> `Feature comparison roles page (Jamfor behorighetsnivåer)`  [INFERRED] [semantically similar]
  feature-comparison-roles_backup.html → feature-comparison-roles.html
- `Column settings drawer (Inställningar för Kolumner)` --semantically_similar_to--> `Filter and sort drawer (Filtrera och sortera; produkter/företaget)`  [INFERRED] [semantically similar]
  mypages/users.html → reviews.html

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Link types routed by links-guide** — claude_skills_links_guide_skill, claude_skills_eco_inline_link_skill, claude_skills_eco_action_link_skill, claude_skills_eco_tile_link_skill [EXTRACTED 0.95]
- **Notification component skills routed by notifications-guide** — claude_skills_notifications_guide_skill, claude_skills_eco_toast_system_skill, claude_skills_eco_toast_ecom_skill, claude_skills_eco_banner_notification_skill, claude_skills_eco_inline_notification_skill, claude_skills_eco_modal_ecom_skill [EXTRACTED 0.95]
- **Shared page shell partials (header, main menu, footer, account-nav drawer)** — mypages_partials_header, mypages_partials_main_menu, mypages_partials_footer, mypages_partials_account_nav_drawer [EXTRACTED 1.00]
- **Users page drawer set (add, columns, balance, upload)** — mypages_users_add_user_drawer, mypages_users_column_settings_drawer, mypages_users_balance_settings_drawer, mypages_users_upload_users_drawer [EXTRACTED 1.00]
- **Design system hub and its overview pages** — eco_design_system_overview, eco_design_system_components_overview, eco_design_system_foundations_overview [INFERRED 0.85]
- **Action, Inline and Tile link family** — _claude_skills_eco_action_link_skill_action_link, _claude_skills_eco_inline_link_skill_inline_link, _claude_skills_eco_tile_link_skill_tile_link [INFERRED 0.85]
- **Banner, Inline and Modal notification family** — _claude_skills_eco_banner_notification_skill_banner_notification, _claude_skills_eco_inline_notification_skill_inline_notification, _claude_skills_eco_modal_ecom_skill_modal_ecom [INFERRED 0.85]
- **Pages using role tier cards** — feature_comparison_roles, feature_comparison_roles_backup, e_handelspartner, claude_skills_eco_role_tier_card_skill [INFERRED 0.85]

## Communities (68 total, 10 thin omitted)

### Community 0 - "Shared header partial"
Cohesion: 0.10
Nodes (51): Page templates: template.html and mypages-template.html, eco-role-tier-card skill (role/tier card component), alligo-design-tokens npm package (CDN-loaded CSS variables), E-handelspartner page, Welcome email (Valkommen till Swedol), Feature comparison page (earlier version), Feature comparison roles page (Jamfor behorighetsnivåer), Feature comparison roles page (backup) (+43 more)

### Community 1 - "Section"
Cohesion: 0.29
Nodes (8): Breadcrumb uses --px-page not --px-full, Hide the whole pagination once all items loaded, Pagination has no bottom padding of its own, Pagination (load more), My Pages page-title section spacing, Page Divider, Use --px-full not --px-page for divider/section, Section

### Community 2 - "Component library skills index"
Cohesion: 0.07
Nodes (41): CLAUDE.md project design guidelines, ECO breakpoints and mobile-first approach (xs/sm/md/lg/xl), graphify knowledge graph usage rules, Quality control checklist before delivery, Component library skills index, eco-action-link skill, eco-banner-notification skill, eco-colors skill (+33 more)

### Community 3 - "eco-doc-page skill"
Cohesion: 0.08
Nodes (29): eco-doc-page skill, Building blocks in `docs.css`, Component pages, Contents list (sticky side TOC), Controls in a playground are the real components, doc-kit.js (DK helpers), docs.css (shared doc-page styles), Foundation pages (+21 more)

### Community 4 - "notifications.js"
Cohesion: 0.22
Nodes (24): B(), banner(), button(), closeBtn(), e(), ecom(), el(), ic() (+16 more)

### Community 5 - "doc-kit.js"
Cohesion: 0.13
Nodes (22): block(), bp(), callouts(), draw(), node(), clear(), codeBox(), esc() (+14 more)

### Community 6 - "docnav.js"
Cohesion: 0.11
Nodes (30): build(), close(), closeDrawer(), closeSearch(), cubic(), esc(), fill(), fold() (+22 more)

### Community 7 - "Design review: implementation vs. Figma + ECO"
Cohesion: 0.14
Nodes (13): 1. Before you start — ask, don't guess, 2. Read the design, 3. Measure the implementation, 4. WCAG check (separate section in the report), 5. Verify before you report, 6. Severity, 7. Report structure, 8. Comparison images (optional) (+5 more)

### Community 8 - "generate-tokens.py"
Cohesion: 0.36
Nodes (13): extract_declarations(), fallback_value(), main(), normalize_typography_value(), parse_colors(), parse_radius_border(), parse_shadows(), parse_spacing() (+5 more)

### Community 9 - "System Inline Notification"
Cohesion: 0.06
Nodes (38): Badge/Basic (.badge-basic), Badge color-meaning mapping for lifecycle status, Badge emphasis Strong/Weak/Weaker, Badge letter case parameter, Badge vs Tag vs counter bubble distinction, Badge states Neutral Grey/Dark and Alert Info/Success/Warning/Danger, Banner Notification, Banner emphasis Strong/Weak/Weaker (+30 more)

### Community 10 - "List Item (ECO Design System)"
Cohesion: 0.15
Nodes (12): Axes, CSS, Flags (for design), HTML structure, List Item (ECO Design System), Rules, Size model, States (+4 more)

### Community 11 - "Menu – Dropdown & Exposed Dropdown (ECO Design System)"
Cohesion: 0.17
Nodes (11): Container, CSS, Flags (for design), HTML structure, Menu – Dropdown & Exposed Dropdown (ECO Design System), Rules, Size model, States (Base Item) (+3 more)

### Community 12 - "attach"
Cohesion: 0.35
Nodes (11): attach(), close(), group(), open(), pick(), render(), show(), loadData() (+3 more)

### Community 13 - "Table (ECO Design System) — first version"
Cohesion: 0.18
Nodes (10): CSS template, Dimensions, Flags, Header background, HTML structure, Rules, Surfaces and lines, Table (ECO Design System) — first version (+2 more)

### Community 14 - "build.py"
Cohesion: 0.11
Nodes (9): crumbs(), emit(), head(), intro(), page(), Frame for the three-page component docs (reference: tooltip.html / tooltip-…, section(), sections() (+1 more)

### Community 15 - "Divider (ECO Design System)"
Cohesion: 0.20
Nodes (9): CSS, Divider (ECO Design System), Flags, HTML structure, NOT used when, Rules, Size, Used when (+1 more)

### Community 16 - "Switch (ECO Design System)"
Cohesion: 0.20
Nodes (9): CSS, Flags for design, HTML structure, Label typography (`eco-typography`), Rules, Size model, States, Switch (ECO Design System) (+1 more)

### Community 17 - "Tabs (ECO Design System)"
Cohesion: 0.18
Nodes (10): Anatomy, Flags for design, HTML structure, On-page navigation (docs), Rules, Size model, States, Tabs (ECO Design System) (+2 more)

### Community 18 - "Text Area (ECO Design System)"
Cohesion: 0.20
Nodes (9): CSS, Flags, HTML structure, Rules, Size model, States, Text Area (ECO Design System), Typography (+1 more)

### Community 19 - "Adding a component to the design system"
Cohesion: 0.22
Nodes (8): 1. Gather inputs (ask if missing), 2. Extract from Figma (never from memory or guesswork), 3. Map every value to a token, 4. Write `.claude/skills/eco-<name>/SKILL.md`, 5. Register it, 6. Verify before reporting done, Adding a component to the design system, Don'ts

### Community 20 - "Pill Segment Control (ECO Design System)"
Cohesion: 0.22
Nodes (8): CSS template (Large, Primary/Pill — mobile-first), HTML and JS example, Interaction (sliding pill), Motion, Pill Segment Control (ECO Design System), Sizes, States, Variants

### Community 21 - "Radio button (ECO Design System)"
Cohesion: 0.22
Nodes (8): CSS, HTML structure, Label & message typography (`eco-typography`), Radio button (ECO Design System), Rules, Size model, States, When to use

### Community 22 - "tabs.js"
Cohesion: 0.50
Nodes (8): arrive(), done(), end(), barKey(), current(), init(), place(), select()

### Community 23 - "Checkbox"
Cohesion: 0.29
Nodes (8): Checkbox, Checkbox dark mode (.form-checkbox-item--dark), Checkbox Disabled Selected gray box with gray checkmark, Checkbox light-mode focus ring deviates from border-focus, Checkbox 24x24 size model, Checkbox table check-icon variant (.check-icon), Border color tokens, Tile Link background colors White/Grey/Black

### Community 24 - "notif.py"
Cohesion: 0.11
Nodes (7): esc_attr(), fig_one(), table(), fig_one_id(), Shared pieces of the five notification page sets (toast, toast-ecom, modal,…, txt_field(), which()

### Community 25 - "compose-helpers.py"
Cohesion: 0.13
Nodes (15): box(), font(), panel(), Add a title strip above an image., sheet(), vbrace(), fig_pair(), AX() (+7 more)

### Community 26 - "tooltip.js"
Cohesion: 0.46
Nodes (6): alignSide(), globalTip(), needsFlip(), placeWrap(), safeTop(), show()

### Community 27 - "gen_button.py"
Cohesion: 0.33
Nodes (3): fig_cls(), pair_cls(), A figure whose stage has an extra class (dark surface).

### Community 28 - "link_large"
Cohesion: 0.40
Nodes (5): link_large(), items: [(url, name, note)], refs(), three_pages(), parts_note()

### Community 29 - "Icon picker (ECO Design System)"
Cohesion: 0.33
Nodes (5): Behavior (same everywhere), Flags, Icon picker (ECO Design System), Rules, Use it

### Community 30 - "Range (ECO Design System)"
Cohesion: 0.33
Nodes (5): Flags, Range (ECO Design System), Rules, States, Use it

### Community 31 - "btn_group"
Cohesion: 0.67
Nodes (3): bp_field(), btn_group(), buttons: [(value, text, pressed)]

### Community 32 - "select-menu.js"
Cohesion: 0.70
Nodes (4): choose(), close(), holder(), openMenu()

### Community 41 - "Duration tokens fast/medium/slow"
Cohesion: 0.25
Nodes (8): Button keyboard-nav focus outline method, Input focus ring is absolute inset -3px, keyboard-only, Distance + fade + easing combination table, Distance drives duration group, Duration tokens fast/medium/slow, Fades fast/medium/slow, Motion easing and duration, Pagination progress bar

### Community 46 - "old_js"
Cohesion: 0.33
Nodes (4): old_js(), Slice of the old page's script: from the line containing `start` up to (not…, A Small eco-select field for a playground (options: [(value, text)], cur = the…, sel()

### Community 49 - "Action Link"
Cohesion: 0.29
Nodes (7): Action Link, Action Link icons never underlined on hover, Action Link Text Primary Inverted variant, Action Link sizes Large/Medium/Small, Inline Link color variants Primary/Secondary/Tertiary/Inverted, Inline Link, Inline Link vs Action Link difference

### Community 50 - "Role Card / Tier Card pair"
Cohesion: 0.29
Nodes (7): Bordered box crumb with slash separator, System button variant, Feature strips must be grounded in comparison table rows, goToCompareView() switch-tab-then-scroll function, Scroll to anchored sections with --header-top-h offset, Role quicklinks (.role-quicklinks), Role Card / Tier Card pair

### Community 57 - "ECO semantic color tokens"
Cohesion: 0.25
Nodes (8): Banner Promotion variant, Promotion uses brand-scoped accent tokens, Accent color tokens accent-default/light/dark, ECO semantic color tokens, Never hardcode hex, use var(--color-*), Surface opacity tokens, Text color tokens, Role tier light vs dark card variants

### Community 58 - "Section padding per breakpoint first vs other"
Cohesion: 0.50
Nodes (5): Section padding per breakpoint first vs other, Spacing consumer classes mt-space, pt-space, gap-space, Layout Vertical Whitespace space-sm/md/lg, Spacing Scale space-0 to space-120, Spacing

### Community 59 - "Button"
Cohesion: 0.22
Nodes (9): Button, Button hover white 20% overlay, Button sizes lg/md/sm/xs desktop vs mobile, Button variants Primary/Secondary/Blank/Destructive/Accent/System, Modal buttons always 32px tall, Tile Link border is absolute ::before inset 0, Tile Link Black hover white 20% overlay, Tile Link (+1 more)

### Community 60 - "Breadcrumb"
Cohesion: 0.22
Nodes (8): Breadcrumb Active (last, current page) state, Breadcrumb, Breadcrumb built-in spacing zeroes following section top padding, Collapsible / Accordion, Hide last row bottom line when list closes a section, Collapsible header uses min-height not height, Easing tokens decelerate/accelerate/standard, Section zeroed-padding use cases

### Community 62 - "toolbar"
Cohesion: 0.67
Nodes (3): items: [(label_id, label, attr, buttons, extra)] -> ds-toolbar, toolbar(), bp_toolbar()

## Ambiguous Edges - Review These
- `Border color tokens` → `Tile Link background colors White/Grey/Black`  [AMBIGUOUS]
  .claude/skills/eco-tile-link/SKILL.md · relation: conceptually_related_to

## Knowledge Gaps
- **167 isolated node(s):** `1. Before you start — ask, don't guess`, `Prototype as a source (functionality)`, `Sweep systematically (do not sample)`, `4. WCAG check (separate section in the report)`, `5. Verify before you report` (+162 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 294 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **10 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Border color tokens` and `Tile Link background colors White/Grey/Black`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `ECO semantic color tokens` connect `ECO semantic color tokens` to `System Inline Notification`, `Checkbox`?**
  _High betweenness centrality (0.008) - this node is a cross-community bridge._
- **Why does `Component library skills index` connect `Component library skills index` to `Shared header partial`?**
  _High betweenness centrality (0.007) - this node is a cross-community bridge._
- **Why does `Accent color tokens accent-default/light/dark` connect `ECO semantic color tokens` to `Button`?**
  _High betweenness centrality (0.007) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Shared header partial` (e.g. with `Shared account-nav drawer partial` and `Shared main menu partial`) actually correct?**
  _`Shared header partial` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `Users page (Användare)` (e.g. with `mypages-template.html (logged-in page template)` and `Users dashboard page (Användare with stat cards)`) actually correct?**
  _`Users page (Användare)` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `mypages-template.html (logged-in page template)` (e.g. with `Address book page (Adressbok)` and `My Pages dashboard test page`) actually correct?**
  _`mypages-template.html (logged-in page template)` has 4 INFERRED edges - model-reasoned connections that need verification._