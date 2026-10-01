# Graph Report - swedol-ui-prototype  (2026-09-30)

## Corpus Check
- 43 files · ~716,848 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 267 nodes · 417 edges · 16 communities (15 shown, 1 thin omitted)
- Extraction: 87% EXTRACTED · 13% INFERRED · 0% AMBIGUOUS · INFERRED: 55 edges (avg confidence: 0.84)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `0c3d744e`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- ECO semantic color tokens
- Section
- Component library skills index
- index.html site overview (sitemap)
- System Inline Notification
- ECO Design System tokens (alligo-design-tokens CSS + styles.css)
- Users page (Användare)
- Segment Control
- Design review: implementation vs. Figma + ECO
- generate-tokens.py
- links-guide skill
- eco-tooltip skill
- README.md
- Adding a component to the design system
- Radio button (ECO Design System)
- compose-helpers.py

## God Nodes (most connected - your core abstractions)
1. `index.html site overview (sitemap)` - 17 edges
2. `Shared header partial` - 17 edges
3. `Users page (Användare)` - 17 edges
4. `mypages-template.html (logged-in page template)` - 15 edges
5. `Reviews page (Recensioner)` - 14 edges
6. `Shared account-nav drawer partial` - 13 edges
7. `Shared footer partial` - 13 edges
8. `template.html (public page template)` - 13 edges
9. `Shared main menu partial` - 12 edges
10. `Component library skills index` - 11 edges

## Surprising Connections (you probably didn't know these)
- `Reviews page backup 1` --semantically_similar_to--> `Reviews page (Recensioner)`  [INFERRED] [semantically similar]
  reviews_backup_1.html → reviews.html
- `Reviews page backup 2` --semantically_similar_to--> `Reviews page (Recensioner)`  [INFERRED] [semantically similar]
  reviews_backup_2.html → reviews.html
- `Column settings drawer (Inställningar för Kolumner)` --semantically_similar_to--> `Filter and sort drawer (Filtrera och sortera; produkter/företaget)`  [INFERRED] [semantically similar]
  mypages/users.html → reviews.html
- `Feature comparison page (earlier version)` --semantically_similar_to--> `Feature comparison roles page (Jamfor behorighetsnivåer)`  [INFERRED] [semantically similar]
  feature-comparison.html → feature-comparison-roles.html
- `Feature comparison roles page (backup)` --semantically_similar_to--> `Feature comparison roles page (Jamfor behorighetsnivåer)`  [INFERRED] [semantically similar]
  feature-comparison-roles_backup.html → feature-comparison-roles.html

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Link types routed by links-guide** — claude_skills_links_guide_skill, claude_skills_eco_inline_link_skill, claude_skills_eco_action_link_skill, claude_skills_eco_tile_link_skill [EXTRACTED 0.95]
- **Notification component skills routed by notifications-guide** — claude_skills_notifications_guide_skill, claude_skills_eco_toast_system_skill, claude_skills_eco_toast_ecom_skill, claude_skills_eco_banner_notification_skill, claude_skills_eco_inline_notification_skill, claude_skills_eco_modal_ecom_skill [EXTRACTED 0.95]
- **ECO token showcase pages** — tokens_buttons, tokens_checkboxes, tokens_colors, tokens_spacing_elevation, tokens_typography [EXTRACTED 1.00]
- **Shared page shell partials (header, main menu, footer, account-nav drawer)** — mypages_partials_header, mypages_partials_main_menu, mypages_partials_footer, mypages_partials_account_nav_drawer [EXTRACTED 1.00]
- **Users page drawer set (add, columns, balance, upload)** — mypages_users_add_user_drawer, mypages_users_column_settings_drawer, mypages_users_balance_settings_drawer, mypages_users_upload_users_drawer [EXTRACTED 1.00]
- **Keyboard-only focus ring pattern (body.keyboard-nav)** — _claude_skills_eco_button_skill_focus_outline_method, _claude_skills_eco_input_skill_focus_ring_absolute, _claude_skills_eco_segment_control_skill_focus_inherits_button [INFERRED 0.85]
- **Action, Inline and Tile link family** — _claude_skills_eco_action_link_skill_action_link, _claude_skills_eco_inline_link_skill_inline_link, _claude_skills_eco_tile_link_skill_tile_link [INFERRED 0.85]
- **Banner, Inline and Modal notification family** — _claude_skills_eco_banner_notification_skill_banner_notification, _claude_skills_eco_inline_notification_skill_inline_notification, _claude_skills_eco_modal_ecom_skill_modal_ecom [INFERRED 0.85]
- **Pages using role tier cards** — feature_comparison_roles, feature_comparison_roles_backup, e_handelspartner, claude_skills_eco_role_tier_card_skill [INFERRED 0.85]

## Communities (16 total, 1 thin omitted)

### Community 0 - "ECO semantic color tokens"
Cohesion: 0.07
Nodes (32): Banner Promotion variant, Promotion uses brand-scoped accent tokens, Bordered box crumb with slash separator, Button, Button hover white 20% overlay, Button sizes lg/md/sm/xs desktop vs mobile, System button variant, Button variants Primary/Secondary/Blank/Destructive/Accent/System (+24 more)

### Community 1 - "Section"
Cohesion: 0.08
Nodes (28): Action Link, Action Link icons never underlined on hover, Action Link Text Primary Inverted variant, Action Link sizes Large/Medium/Small, Breadcrumb Active (last, current page) state, Breadcrumb, Breadcrumb built-in spacing zeroes following section top padding, Breadcrumb uses --px-page not --px-full (+20 more)

### Community 2 - "Component library skills index"
Cohesion: 0.12
Nodes (29): CLAUDE.md project design guidelines, ECO breakpoints and mobile-first approach (xs/sm/md/lg/xl), graphify knowledge graph usage rules, Quality control checklist before delivery, Component library skills index, eco-banner-notification skill, eco-colors skill, eco-inline-notification skill (+21 more)

### Community 3 - "index.html site overview (sitemap)"
Cohesion: 0.20
Nodes (29): Page templates: template.html and mypages-template.html, eco-role-tier-card skill (role/tier card component), alligo-design-tokens npm package (CDN-loaded CSS variables), E-handelspartner page, Welcome email (Valkommen till Swedol), Feature comparison page (earlier version), Feature comparison roles page (Jamfor behorighetsnivåer), Feature comparison roles page (backup) (+21 more)

### Community 4 - "System Inline Notification"
Cohesion: 0.09
Nodes (26): Badge/Basic (.badge-basic), Badge color-meaning mapping for lifecycle status, Badge emphasis Strong/Weak/Weaker, Badge letter case parameter, Badge vs Tag vs counter bubble distinction, Badge states Neutral Grey/Dark and Alert Info/Success/Warning/Danger, Banner Notification, Banner emphasis Strong/Weak/Weaker (+18 more)

### Community 5 - "ECO Design System tokens (alligo-design-tokens CSS + styles.css)"
Cohesion: 0.21
Nodes (15): Row action buttons with tooltips, Filter and sort drawer (Filtrera och sortera; produkter/företaget), Reviews sidebar filters (collapsible + checkboxes), ECO Design System tokens (alligo-design-tokens CSS + styles.css), Tokens: Buttons page, Button variants and sizes showcase, Tokens: Checkboxes page, Checkbox light and dark mode showcase (+7 more)

### Community 6 - "Users page (Användare)"
Cohesion: 0.17
Nodes (16): Feedback: Do not change table structure, Rule: never alter data-table structure (COLS order, column visibility JS), mypages/memory/MEMORY.md index, Rule: do not change data table structure in frontend, Contact info section (Hur man kontaktar oss), Users page (Användare), Add user drawer (Lägg till ny användare), Balance settings drawer (Inställningar för saldo) (+8 more)

### Community 7 - "Segment Control"
Cohesion: 0.08
Nodes (26): Button keyboard-nav focus outline method, Component-specific elevation tokens, Designated Level elevation-drawer-*, Drawer conventions, Drawer mobile base styling at max-width 768px, Input focus ring is absolute inset -3px, keyboard-only, Input Field, Label above input, hint/message below pattern (+18 more)

### Community 8 - "Design review: implementation vs. Figma + ECO"
Cohesion: 0.15
Nodes (12): 1. Before you start — ask, don't guess, 2. Read the design, 3. Measure the implementation, 4. WCAG check (separate section in the report), 5. Verify before you report, 6. Severity, 7. Report structure, 8. Comparison images (optional) (+4 more)

### Community 9 - "generate-tokens.py"
Cohesion: 0.45
Nodes (10): extract_declarations(), main(), parse_colors(), parse_props(), parse_radius_border(), parse_shadows(), parse_spacing(), parse_typography() (+2 more)

### Community 10 - "links-guide skill"
Cohesion: 0.29
Nodes (7): eco-action-link skill, eco-inline-link skill, eco-tile-link skill, links-guide skill, Action Link (standalone, optional icons), Inline Link (in body text, always underlined), Tile Link (graphical/prominent)

### Community 11 - "eco-tooltip skill"
Cohesion: 0.40
Nodes (5): eco-elevation skill, eco-motion skill, eco-tooltip skill, Tooltip hover-only interaction (never on focus), Tooltip positions, sizes and beak

### Community 13 - "Adding a component to the design system"
Cohesion: 0.22
Nodes (8): 1. Gather inputs (ask if missing), 2. Extract from Figma (never from memory or guesswork), 3. Map every value to a token, 4. Write `.claude/skills/eco-<name>/SKILL.md`, 5. Register it, 6. Verify before reporting done, Adding a component to the design system, Don'ts

### Community 14 - "Radio button (ECO Design System)"
Cohesion: 0.22
Nodes (8): CSS template, HTML structure, Label & message typography (`eco-typography`), Radio button (ECO Design System), Rules, Size model, States, When to use

### Community 15 - "compose-helpers.py"
Cohesion: 0.39
Nodes (6): box(), font(), panel(), Add a title strip above an image., sheet(), vbrace()

## Ambiguous Edges - Review These
- `Border color tokens` → `Tile Link background colors White/Grey/Black`  [AMBIGUOUS]
  .claude/skills/eco-tile-link/SKILL.md · relation: conceptually_related_to

## Knowledge Gaps
- **67 isolated node(s):** `1. Before you start — ask, don't guess`, `Prototype as a source (functionality)`, `3. Measure the implementation`, `4. WCAG check (separate section in the report)`, `5. Verify before you report` (+62 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 94 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Border color tokens` and `Tile Link background colors White/Grey/Black`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `Component library skills index` connect `Component library skills index` to `eco-tooltip skill`, `links-guide skill`, `index.html site overview (sitemap)`?**
  _High betweenness centrality (0.048) - this node is a cross-community bridge._
- **Why does `ECO semantic color tokens` connect `ECO semantic color tokens` to `System Inline Notification`?**
  _High betweenness centrality (0.045) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Shared header partial` (e.g. with `Shared account-nav drawer partial` and `Shared main menu partial`) actually correct?**
  _`Shared header partial` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `Users page (Användare)` (e.g. with `mypages-template.html (logged-in page template)` and `Users dashboard page (Användare with stat cards)`) actually correct?**
  _`Users page (Användare)` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `mypages-template.html (logged-in page template)` (e.g. with `Address book page (Adressbok)` and `My Pages dashboard test page`) actually correct?**
  _`mypages-template.html (logged-in page template)` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `Reviews page (Recensioner)` (e.g. with `template.html (public page template)` and `Reviews page backup 1`) actually correct?**
  _`Reviews page (Recensioner)` has 3 INFERRED edges - model-reasoned connections that need verification._