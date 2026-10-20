# Graph Report - swedol-ui-prototype  (2026-09-19)

## Corpus Check
- Large corpus: 202 files · ~710,555 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder.

## Summary
- 228 nodes · 377 edges · 14 communities (12 shown, 2 thin omitted)
- Extraction: 85% EXTRACTED · 15% INFERRED · 0% AMBIGUOUS · INFERRED: 55 edges (avg confidence: 0.84)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Button & Breadcrumb Specs
- Links & Action Components
- CLAUDE.md Guidelines & Skills Index
- Page Templates & Public Pages
- Badge Component
- Token Showcase & Reviews Filters
- My Pages Users Page
- Motion & Elevation Tokens
- Input, Drawer & Form Patterns
- Token Generation Script
- Links Guide Skills
- Tooltip, Elevation & Motion Skills
- README & Deployment
- Data Table Structure Rule

## God Nodes (most connected - your core abstractions)
1. `index.html site overview (sitemap)` - 17 edges
2. `Shared header partial` - 17 edges
3. `Users page (Användare)` - 17 edges
4. `mypages-template.html (logged-in page template)` - 15 edges
5. `Reviews page (Recensioner)` - 14 edges
6. `template.html (public page template)` - 13 edges
7. `Shared footer partial` - 13 edges
8. `Shared account-nav drawer partial` - 13 edges
9. `Shared main menu partial` - 12 edges
10. `Component library skills index` - 11 edges

## Surprising Connections (you probably didn't know these)
- `Column settings drawer (Inställningar för Kolumner)` --semantically_similar_to--> `Filter and sort drawer (Filtrera och sortera; produkter/företaget)`  [INFERRED] [semantically similar]
  mypages/users.html → reviews.html
- `Reviews page backup 1` --semantically_similar_to--> `Reviews page (Recensioner)`  [INFERRED] [semantically similar]
  reviews_backup_1.html → reviews.html
- `Reviews page backup 2` --semantically_similar_to--> `Reviews page (Recensioner)`  [INFERRED] [semantically similar]
  reviews_backup_2.html → reviews.html
- `Feature comparison page (earlier version)` --semantically_similar_to--> `Feature comparison roles page (Jamfor behorighetsnivåer)`  [INFERRED] [semantically similar]
  feature-comparison.html → feature-comparison-roles.html
- `Feature comparison roles page (backup)` --semantically_similar_to--> `Feature comparison roles page (Jamfor behorighetsnivåer)`  [INFERRED] [semantically similar]
  feature-comparison-roles_backup.html → feature-comparison-roles.html

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Banner, Inline and Modal notification family** — _claude_skills_eco_banner_notification_skill_banner_notification, _claude_skills_eco_inline_notification_skill_inline_notification, _claude_skills_eco_modal_ecom_skill_modal_ecom [INFERRED 0.85]
- **Keyboard-only focus ring pattern (body.keyboard-nav)** — _claude_skills_eco_button_skill_focus_outline_method, _claude_skills_eco_input_skill_focus_ring_absolute, _claude_skills_eco_segment_control_skill_focus_inherits_button [INFERRED 0.85]
- **Action, Inline and Tile link family** — _claude_skills_eco_action_link_skill_action_link, _claude_skills_eco_inline_link_skill_inline_link, _claude_skills_eco_tile_link_skill_tile_link [INFERRED 0.85]
- **Notification component skills routed by notifications-guide** — claude_skills_notifications_guide_skill, claude_skills_eco_toast_system_skill, claude_skills_eco_toast_ecom_skill, claude_skills_eco_banner_notification_skill, claude_skills_eco_inline_notification_skill, claude_skills_eco_modal_ecom_skill [EXTRACTED 0.95]
- **Link types routed by links-guide** — claude_skills_links_guide_skill, claude_skills_eco_inline_link_skill, claude_skills_eco_action_link_skill, claude_skills_eco_tile_link_skill [EXTRACTED 0.95]
- **Pages using role tier cards** — feature_comparison_roles, feature_comparison_roles_backup, e_handelspartner, claude_skills_eco_role_tier_card_skill [INFERRED 0.85]
- **Shared page shell partials (header, main menu, footer, account-nav drawer)** — mypages_partials_header, mypages_partials_main_menu, mypages_partials_footer, mypages_partials_account_nav_drawer [EXTRACTED 1.00]
- **Users page drawer set (add, columns, balance, upload)** — mypages_users_add_user_drawer, mypages_users_column_settings_drawer, mypages_users_balance_settings_drawer, mypages_users_upload_users_drawer [EXTRACTED 1.00]
- **ECO token showcase pages** — tokens_buttons, tokens_checkboxes, tokens_colors, tokens_spacing_elevation, tokens_typography [EXTRACTED 1.00]

## Communities (14 total, 2 thin omitted)

### Community 0 - "Button & Breadcrumb Specs"
Cohesion: 0.07
Nodes (33): Promotion uses brand-scoped accent tokens, Bordered box crumb with slash separator, Button, Button keyboard-nav focus outline method, Button hover white 20% overlay, Button sizes lg/md/sm/xs desktop vs mobile, System button variant, Button variants Primary/Secondary/Blank/Destructive/Accent/System (+25 more)

### Community 1 - "Links & Action Components"
Cohesion: 0.08
Nodes (28): Action Link, Action Link icons never underlined on hover, Action Link Text Primary Inverted variant, Action Link sizes Large/Medium/Small, Breadcrumb Active (last, current page) state, Breadcrumb, Breadcrumb built-in spacing zeroes following section top padding, Breadcrumb uses --px-page not --px-full (+20 more)

### Community 2 - "CLAUDE.md Guidelines & Skills Index"
Cohesion: 0.12
Nodes (29): CLAUDE.md project design guidelines, ECO breakpoints and mobile-first approach (xs/sm/md/lg/xl), graphify knowledge graph usage rules, Quality control checklist before delivery, Component library skills index, eco-banner-notification skill, eco-colors skill, eco-inline-notification skill (+21 more)

### Community 3 - "Page Templates & Public Pages"
Cohesion: 0.20
Nodes (29): Page templates: template.html and mypages-template.html, eco-role-tier-card skill (role/tier card component), alligo-design-tokens npm package (CDN-loaded CSS variables), E-handelspartner page, Welcome email (Valkommen till Swedol), Feature comparison page (earlier version), Feature comparison roles page (Jamfor behorighetsnivåer), Feature comparison roles page (backup) (+21 more)

### Community 4 - "Badge Component"
Cohesion: 0.09
Nodes (27): Badge/Basic (.badge-basic), Badge color-meaning mapping for lifecycle status, Badge emphasis Strong/Weak/Weaker, Badge letter case parameter, Badge vs Tag vs counter bubble distinction, Badge states Neutral Grey/Dark and Alert Info/Success/Warning/Danger, Banner Notification, Banner emphasis Strong/Weak/Weaker (+19 more)

### Community 5 - "Token Showcase & Reviews Filters"
Cohesion: 0.21
Nodes (15): Row action buttons with tooltips, Filter and sort drawer (Filtrera och sortera; produkter/företaget), Reviews sidebar filters (collapsible + checkboxes), ECO Design System tokens (alligo-design-tokens CSS + styles.css), Tokens: Buttons page, Button variants and sizes showcase, Tokens: Checkboxes page, Checkbox light and dark mode showcase (+7 more)

### Community 6 - "My Pages Users Page"
Cohesion: 0.21
Nodes (14): Feedback: Do not change table structure, Rule: never alter data-table structure (COLS order, column visibility JS), Contact info section (Hur man kontaktar oss), Users page (Användare), Add user drawer (Lägg till ny användare), Balance settings drawer (Inställningar för saldo), BankID signing flow, Column settings drawer (Inställningar för Kolumner) (+6 more)

### Community 7 - "Motion & Elevation Tokens"
Cohesion: 0.17
Nodes (12): Component-specific elevation tokens, Distance + fade + easing combination table, Distance drives duration group, Duration tokens fast/medium/slow, Fades fast/medium/slow, Motion easing and duration, Pagination progress bar, Segment Control fluid width only at xs (+4 more)

### Community 8 - "Input, Drawer & Form Patterns"
Cohesion: 0.18
Nodes (12): Designated Level elevation-drawer-*, Drawer conventions, Drawer mobile base styling at max-width 768px, Input focus ring is absolute inset -3px, keyboard-only, Input Field, Label above input, hint/message below pattern, Input sizes per breakpoint, Input states enabled/hover/active/focus/error/success/disabled (+4 more)

### Community 9 - "Token Generation Script"
Cohesion: 0.45
Nodes (10): extract_declarations(), main(), parse_colors(), parse_props(), parse_radius_border(), parse_shadows(), parse_spacing(), parse_typography() (+2 more)

### Community 10 - "Links Guide Skills"
Cohesion: 0.29
Nodes (7): eco-action-link skill, eco-inline-link skill, eco-tile-link skill, links-guide skill, Action Link (standalone, optional icons), Inline Link (in body text, always underlined), Tile Link (graphical/prominent)

### Community 11 - "Tooltip, Elevation & Motion Skills"
Cohesion: 0.40
Nodes (5): eco-elevation skill, eco-motion skill, eco-tooltip skill, Tooltip hover-only interaction (never on focus), Tooltip positions, sizes and beak

## Ambiguous Edges - Review These
- `Border color tokens` → `Tile Link background colors White/Grey/Black`  [AMBIGUOUS]
  .claude/skills/eco-tile-link/SKILL.md · relation: conceptually_related_to

## Knowledge Gaps
- **46 isolated node(s):** `Action Link sizes Large/Medium/Small`, `Action Link Text Primary Inverted variant`, `Badge letter case parameter`, `Breadcrumb Active (last, current page) state`, `Checkbox 24x24 size model` (+41 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 68 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Border color tokens` and `Tile Link background colors White/Grey/Black`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `Component library skills index` connect `CLAUDE.md Guidelines & Skills Index` to `Tooltip, Elevation & Motion Skills`, `Links Guide Skills`, `Page Templates & Public Pages`?**
  _High betweenness centrality (0.064) - this node is a cross-community bridge._
- **Why does `ECO semantic color tokens` connect `Button & Breadcrumb Specs` to `Badge Component`?**
  _High betweenness centrality (0.061) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Shared header partial` (e.g. with `Shared account-nav drawer partial` and `Shared main menu partial`) actually correct?**
  _`Shared header partial` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `Users page (Användare)` (e.g. with `mypages-template.html (logged-in page template)` and `Users dashboard page (Användare with stat cards)`) actually correct?**
  _`Users page (Användare)` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `mypages-template.html (logged-in page template)` (e.g. with `Address book page (Adressbok)` and `My Pages dashboard test page`) actually correct?**
  _`mypages-template.html (logged-in page template)` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `Reviews page (Recensioner)` (e.g. with `template.html (public page template)` and `Reviews page backup 1`) actually correct?**
  _`Reviews page (Recensioner)` has 3 INFERRED edges - model-reasoned connections that need verification._