# Graph Report - hairline-button-group-24873c  (2026-10-20)

## Corpus Check
- 131 files · ~1,554,979 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1058 nodes · 1886 edges · 88 communities (63 shown, 12 thin omitted)
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 98 edges (avg confidence: 0.83)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `a348cec6`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- components/css/button-group.css
- eco-add-component skill
- tabs.js
- Persona 2 – Lars, senior snickare och arbetsledare (kundtyp *Effektivitet och säkerhet*)
- docnav.js
- Three-page component doc structure (Examples / Specifications / Code)
- build.py
- eco-button skill
- Public page template (Regular Page)
- notifications.js
- kernel.js
- doc-kit.js
- docs.css
- hairline/README.md
- notif.py
- compose-helpers.py
- CLAUDE.md (project design guidelines)
- eco-doc-page skill (docs page structure)
- js/range.js
- Radio component
- generate-tokens.py
- button-pair.js
- Design review: implementation vs. Figma + ECO
- List Item (ECO Design System)
- Tabs (ECO Design System)
- attach
- Table (ECO Design System) — first version
- Menu – Dropdown & Exposed Dropdown (ECO Design System)
- Role Tier Card component
- eco-card-animation/SKILL.md
- Divider (ECO Design System)
- Switch (ECO Design System)
- Text Area (ECO Design System)
- Adding a component to the design system
- Pill Segment Control (ECO Design System)
- Radio button (ECO Design System)
- tooltip.js
- Old ECO Libraries Web Page (Storybook)
- bc.py
- hero_switch.py
- hero_switch_iso.py
- toc.js
- Old ECO DS start page (gamla startsidan)
- gen_button.py
- radio.js
- card-check.mjs
- Pagination component
- switch.js
- Feature comparison with role tiers page
- Modal component
- link_large
- hero_button_iso.py
- gen_links_guide.py
- gen_notifications.py
- make-eco.mjs
- Feedback: Do not change table structure
- upload-jira-images.sh
- eco-collapsible skill
- btn_group
- run
- eco-badge skill
- patterns-overview.html docs page
- sel
- Toast docs page (old source)
- Welcome email (Valkommen till Swedol)
- tokens/_test.html (unused placeholder)
- eco-pill-segment-control skill
- button-group.js
- select.js
- eco-radio skill
- input.js
- checkbox.js
- hairline/range.js
- Resources overview page
- Icon picker (ECO Design System)

## God Nodes (most connected - your core abstractions)
1. `input.css` - 39 edges
2. `select.css` - 37 edges
3. `badge.css` - 35 edges
4. `tabs.css` - 32 edges
5. `button.css` - 30 edges
6. `divider.css` - 30 edges
7. `Three-page component doc structure (Examples / Specifications / Code)` - 24 edges
8. `docs.css` - 22 edges
9. `CLAUDE.md (project design guidelines)` - 21 edges
10. `eco-doc-page skill (docs page structure)` - 21 edges

## Surprising Connections (you probably didn't know these)
- `Recensioner page` --semantically_similar_to--> `Recensioner backup 1`  [INFERRED] [semantically similar]
  reviews.html → reviews_backup_1.html
- `Recensioner page` --semantically_similar_to--> `Recensioner backup 2`  [INFERRED] [semantically similar]
  reviews.html → reviews_backup_2.html
- `Sticky CTA example page` --semantically_similar_to--> `Public page template (Regular Page)`  [INFERRED] [semantically similar]
  sticky-cta-example.html → template.html
- `Feature comparison page (permission levels)` --semantically_similar_to--> `Feature comparison with role tiers page`  [INFERRED] [semantically similar]
  feature-comparison.html → feature-comparison-roles.html
- `Feature comparison with role tiers page` --semantically_similar_to--> `Feature comparison roles (backup)`  [INFERRED] [semantically similar]
  feature-comparison-roles.html → feature-comparison-roles_backup.html

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Notification component skills governed by notifications-guide** — claude_skills_eco_banner_notification_skill, claude_skills_eco_inline_notification_skill, claude_skills_eco_modal_ecom_skill, claude_skills_notifications_guide_skill [EXTRACTED 0.85]
- **ECO Resources section pages** — eco_design_system_resources_overview, eco_design_system_resources_design, eco_design_system_resources_web, eco_design_system_resources_getting_help, eco_design_system_resources_introduction_for_developers, eco_design_system_resources_introduction_for_stakeholders [EXTRACTED 0.95]
- **ECO Resources section pages** — eco_design_system_resources_overview, eco_design_system_resources_design, eco_design_system_resources_web, eco_design_system_resources_getting_help, eco_design_system_resources_introduction_for_developers, eco_design_system_resources_introduction_for_stakeholders [EXTRACTED 0.95]
- **Hairline figure pages (button, switch, radio) in clean and ECO variants** — hairline_hairline_button_pair, hairline_hairline_switch, hairline_hairline_radio, hairline_hairline_button_pair_eco, hairline_hairline_switch_eco, hairline_hairline_radio_eco [EXTRACTED 0.95]
- **Hairline figure pages (button, switch, radio) in clean and ECO variants** — hairline_hairline_button_pair, hairline_hairline_switch, hairline_hairline_radio, hairline_hairline_button_pair_eco, hairline_hairline_switch_eco, hairline_hairline_radio_eco [EXTRACTED 0.95]
- **menu docs page set** — eco_design_system_components_menu, eco_design_system_components_menu_specifications [EXTRACTED 0.95]
- **menu docs page set** — eco_design_system_components_menu, eco_design_system_components_menu_specifications [EXTRACTED 0.95]
- **modal docs page set** — eco_design_system_components_modal, eco_design_system_components_modal_specifications, eco_design_system_components_modal_code [EXTRACTED 0.95]
- **modal docs page set** — eco_design_system_components_modal, eco_design_system_components_modal_specifications, eco_design_system_components_modal_code [EXTRACTED 0.95]
- **pagination docs page set** — eco_design_system_components_pagination, eco_design_system_components_pagination_specifications, eco_design_system_components_pagination_code [EXTRACTED 0.95]
- **pagination docs page set** — eco_design_system_components_pagination, eco_design_system_components_pagination_specifications, eco_design_system_components_pagination_code [EXTRACTED 0.95]
- **Pill segment control three-page doc set** — eco_design_system_components_segment_control, eco_design_system_components_segment_control_specifications, eco_design_system_components_segment_control_code [EXTRACTED 0.95]
- **Pill segment control three-page doc set** — eco_design_system_components_segment_control, eco_design_system_components_segment_control_specifications, eco_design_system_components_segment_control_code [EXTRACTED 0.95]
- **Select three-page doc set** — eco_design_system_components_select, eco_design_system_components_select_specifications, eco_design_system_components_select_code [EXTRACTED 0.95]
- **Select three-page doc set** — eco_design_system_components_select, eco_design_system_components_select_specifications, eco_design_system_components_select_code [EXTRACTED 0.95]
- **Switch three-page doc set** — eco_design_system_components_switch, eco_design_system_components_switch_specifications, eco_design_system_components_switch_code [EXTRACTED 0.95]
- **Switch three-page doc set** — eco_design_system_components_switch, eco_design_system_components_switch_specifications, eco_design_system_components_switch_code [EXTRACTED 0.95]
- **Badge doc page sets (5 types x 3 pages)** — eco_design_system_components_badge_basic_code, eco_design_system_components_badge_basic_specifications, eco_design_system_components_badge_basic, eco_design_system_components_badge_dot_code, eco_design_system_components_badge_dot_specifications, eco_design_system_components_badge_dot, eco_design_system_components_badge_number_code, eco_design_system_components_badge_number_specifications, eco_design_system_components_badge_number [EXTRACTED 1.00]
- **Badge doc page sets (5 types x 3 pages)** — eco_design_system_components_badge_basic_code, eco_design_system_components_badge_basic_specifications, eco_design_system_components_badge_basic, eco_design_system_components_badge_dot_code, eco_design_system_components_badge_dot_specifications, eco_design_system_components_badge_dot, eco_design_system_components_badge_number_code, eco_design_system_components_badge_number_specifications, eco_design_system_components_badge_number [EXTRACTED 1.00]
- **ECO component skills** — claude_skills_eco_breadcrumb_skill, claude_skills_eco_list_item_skill, claude_skills_eco_menu_skill, claude_skills_eco_modal_ecom_skill, claude_skills_eco_pagination_skill, claude_skills_eco_select_skill, claude_skills_eco_tabs_skill [EXTRACTED 1.00]
- **ECO component skills** — claude_skills_eco_breadcrumb_skill, claude_skills_eco_list_item_skill, claude_skills_eco_menu_skill, claude_skills_eco_modal_ecom_skill, claude_skills_eco_pagination_skill, claude_skills_eco_select_skill, claude_skills_eco_tabs_skill [EXTRACTED 1.00]
- **Link types decided by links-guide** — c_inline_link_concept, c_action_link, c_tile_link, eco_design_system_components_links_guide [EXTRACTED 1.00]
- **Link types decided by links-guide** — c_inline_link_concept, c_action_link, c_tile_link, eco_design_system_components_links_guide [EXTRACTED 1.00]
- **Notification component family** — claude_skills_notifications_guide_skill, claude_skills_eco_toast_system_skill, claude_skills_eco_toast_ecom_skill, claude_skills_eco_banner_notification_skill, claude_skills_eco_inline_notification_skill, claude_skills_eco_modal_ecom_skill [EXTRACTED 1.00]
- **Old Resources & Help pages sharing one layout** — old_ds_page_structures_category_sources_help_resources_and_help_help_getting_help_overview, old_ds_page_structures_category_sources_help_resources_and_help_libraries_design, old_ds_page_structures_category_sources_help_resources_and_help_libraries_web [EXTRACTED 1.00]
- **Old Resources & Help pages sharing one layout** — old_ds_page_structures_category_sources_help_resources_and_help_help_getting_help_overview, old_ds_page_structures_category_sources_help_resources_and_help_libraries_design, old_ds_page_structures_category_sources_help_resources_and_help_libraries_web [EXTRACTED 1.00]
- **Customer personas for design feedback** — docs_personas_fa_jobbet_gjort, docs_personas_effektivitet_och_sakerhet, docs_personas_trygghet_och_inkopsstyrning, docs_personas_readme [EXTRACTED 1.00]
- **Customer personas for design feedback** — docs_personas_fa_jobbet_gjort, docs_personas_effektivitet_och_sakerhet, docs_personas_trygghet_och_inkopsstyrning, docs_personas_readme [EXTRACTED 1.00]
- **Shared page frame partials (header, footer, main menu, account nav drawer)** — mypages_partials_header, mypages_partials_footer, mypages_partials_main_menu, mypages_partials_account_nav_drawer [EXTRACTED 1.00]
- **Shared page frame partials (header, footer, main menu, account nav drawer)** — mypages_partials_header, mypages_partials_footer, mypages_partials_main_menu, mypages_partials_account_nav_drawer [EXTRACTED 1.00]
- **Specifications pages sharing measure.css/js blueprint figures** — eco_design_system_components_divider_specifications, eco_design_system_components_icon_picker_specifications, eco_design_system_components_inline_link_specifications, eco_design_system_components_inline_specifications, eco_design_system_components_input_specifications, eco_design_system_components_list_item_specifications, c_measure_js [EXTRACTED 1.00]
- **Specifications pages sharing measure.css/js blueprint figures** — eco_design_system_components_divider_specifications, eco_design_system_components_icon_picker_specifications, eco_design_system_components_inline_link_specifications, eco_design_system_components_inline_specifications, eco_design_system_components_input_specifications, eco_design_system_components_list_item_specifications, c_measure_js [EXTRACTED 1.00]
- **banner three-page doc set** — eco_design_system_components_banner, eco_design_system_components_banner_specifications, eco_design_system_components_banner_code [EXTRACTED 1.00]
- **banner three-page doc set** — eco_design_system_components_banner, eco_design_system_components_banner_specifications, eco_design_system_components_banner_code [EXTRACTED 1.00]
- **button three-page doc set** — eco_design_system_components_button, eco_design_system_components_button_specifications, eco_design_system_components_button_code [EXTRACTED 1.00]
- **button three-page doc set** — eco_design_system_components_button, eco_design_system_components_button_specifications, eco_design_system_components_button_code [EXTRACTED 1.00]
- **checkbox three-page doc set** — eco_design_system_components_checkbox, eco_design_system_components_checkbox_specifications, eco_design_system_components_checkbox_code [EXTRACTED 1.00]
- **checkbox three-page doc set** — eco_design_system_components_checkbox, eco_design_system_components_checkbox_specifications, eco_design_system_components_checkbox_code [EXTRACTED 1.00]
- **Foundational token skills** — claude_skills_eco_tokens_skill, claude_skills_eco_typography_skill, claude_skills_eco_spacing_skill, claude_skills_eco_colors_skill, claude_skills_eco_elevation_skill [EXTRACTED 1.00]
- **Docs intro page design references** — docs_intro_ref_cards_pick_a_category, docs_intro_ref_gamla_startsidan_old_eco_start_page, docs_intro_ref_hero_dark_hero [INFERRED 0.75]
- **Docs intro page design references** — docs_intro_ref_cards_pick_a_category, docs_intro_ref_gamla_startsidan_old_eco_start_page, docs_intro_ref_hero_dark_hero [INFERRED 0.75]
- **Form selection controls and their boundaries** — claude_skills_eco_radio_skill, claude_skills_eco_switch_skill, claude_skills_eco_pill_segment_control_skill, claude_skills_eco_checkbox_skill, claude_skills_eco_tabs_skill [INFERRED 0.85]
- **Old form control docs pages** — eco_design_system_gen_old_source_input, eco_design_system_gen_old_source_textarea, eco_design_system_gen_old_source_select, eco_design_system_gen_old_source_radio, eco_design_system_gen_old_source_switch [INFERRED 0.85]
- **Old form control docs pages** — eco_design_system_gen_old_source_input, eco_design_system_gen_old_source_textarea, eco_design_system_gen_old_source_select, eco_design_system_gen_old_source_radio, eco_design_system_gen_old_source_switch [INFERRED 0.85]
- **Old notification docs pages** — eco_design_system_gen_old_source_inline, eco_design_system_gen_old_source_modal, eco_design_system_gen_old_source_notifications, eco_design_system_gen_old_source_toast_ecom [INFERRED 0.85]
- **Old notification docs pages** — eco_design_system_gen_old_source_inline, eco_design_system_gen_old_source_modal, eco_design_system_gen_old_source_notifications, eco_design_system_gen_old_source_toast_ecom [INFERRED 0.85]
- **Recensioner page and backups** — reviews, reviews_backup_1, reviews_backup_2 [INFERRED 0.85]
- **Recensioner page and backups** — reviews, reviews_backup_1, reviews_backup_2 [INFERRED 0.85]
- **Three-page doc sets in this chunk** — eco_design_system_components_toast, eco_design_system_components_toast_specifications, eco_design_system_components_tooltip, eco_design_system_components_tooltip_code, eco_design_system_components_tooltip_specifications [INFERRED 0.85]
- **Three-page doc sets in this chunk** — eco_design_system_components_toast, eco_design_system_components_toast_specifications, eco_design_system_components_tooltip, eco_design_system_components_tooltip_code, eco_design_system_components_tooltip_specifications [INFERRED 0.85]
- **Användare page versions** — mypages_users, mypages_users_v1, mypages_users_dashboard [INFERRED 0.85]
- **Användare page versions** — mypages_users, mypages_users_v1, mypages_users_dashboard [INFERRED 0.85]

## Communities (88 total, 12 thin omitted)

### Community 0 - "components/css/button-group.css"
Cohesion: 0.12
Nodes (47): badge.css, button.css, divider.css, input.css, menu.css, radio.css, range.css, section.css (+39 more)

### Community 1 - "eco-add-component skill"
Cohesion: 0.14
Nodes (22): design-review skill, eco-action-link skill, eco-add-component skill, eco-colors skill, eco-divider skill, eco-section skill, Section padding per breakpoint, eco-spacing skill (+14 more)

### Community 2 - "tabs.js"
Cohesion: 0.08
Nodes (42): switch.css, textarea.css, tile-link.css, choose(), close(), holder(), leave(), openMenu() (+34 more)

### Community 3 - "Persona 2 – Lars, senior snickare och arbetsledare (kundtyp *Effektivitet och säkerhet*)"
Cohesion: 0.04
Nodes (44): Persona feedback protocol (severity, G-xx criteria), Acceptanskriterier (EOS), Behov i uppgiftsform, Exempel på granskning (mall), Frågor att ställa en prototyp som Lars, Kontext, Kort om Lars, Mål, smärtor och drivkrafter (översatt till gränssnittet) (+36 more)

### Community 4 - "docnav.js"
Cohesion: 0.10
Nodes (30): build(), close(), closeDrawer(), closeSearch(), cubic(), esc(), fill(), fold() (+22 more)

### Community 5 - "Three-page component doc structure (Examples / Specifications / Code)"
Cohesion: 0.07
Nodes (37): ECO Badge component (non-interactive status/label/count marker), badge.css shared component CSS, Action link, components/css/collapsible.css, components/js/collapsible.js, components/css/divider.css, components/icon-picker/icon-picker.js, Inline link (+29 more)

### Community 6 - "build.py"
Cohesion: 0.07
Nodes (11): crumbs(), emit(), head(), intro(), old_js(), page(), Frame for the three-page component docs (reference: tooltip.html / tooltip-…, Slice of the old page's script: from the line containing `start` up to (not… (+3 more)

### Community 7 - "eco-button skill"
Cohesion: 0.21
Nodes (18): eco-banner-notification skill, eco-button skill, eco-inline-link skill, eco-inline-notification skill, eco-modal-ecom skill (E-Com Modal), eco-motion skill (easing, duration, campaign motion), eco-toast-ecom skill, Add to cart / Informational variants (+10 more)

### Community 8 - "Public page template (Regular Page)"
Cohesion: 0.10
Nodes (30): Site overview (index.html), alligo-design-tokens (unpkg CSS), styles.css (shared page styles), Adressbok page, Cookie Banner page, Cookie Banner page (v1), Min sida dashboard test page, My Pages template (logged-in) (+22 more)

### Community 9 - "notifications.js"
Cohesion: 0.18
Nodes (26): B(), banner(), button(), closeBtn(), e(), ecom(), el(), ic() (+18 more)

### Community 10 - "kernel.js"
Cohesion: 0.11
Nodes (19): css(), entry(), fade(), fit(), frame(), ghost(), hull(), inject() (+11 more)

### Community 11 - "doc-kit.js"
Cohesion: 0.13
Nodes (22): block(), bp(), callouts(), draw(), node(), clear(), codeBox(), esc() (+14 more)

### Community 12 - "docs.css"
Cohesion: 0.12
Nodes (25): action-link.css, inline-link.css, list-item.css, notifications.css, pagination.css, role-tier.css, docs.css, Divider (old docs page) (+17 more)

### Community 13 - "hairline/README.md"
Cohesion: 0.14
Nodes (15): Hairline card embed (embed.js, hairline-card.css, kernel.js), Hairline animated figure, Hairline button (first version, pill), Hairline button pair (clean page), Hairline button pair (ECO-styled page), Hairline radio (clean page), Hairline radio (ECO-styled page), Hairline switch (clean page) (+7 more)

### Community 14 - "notif.py"
Cohesion: 0.09
Nodes (10): esc_attr(), fig_one(), items: [(label_id, label, attr, buttons, extra)] -> ds-toolbar, table(), toolbar(), bp_toolbar(), fig_one_id(), Shared pieces of the five notification page sets (toast, toast-ecom, modal,… (+2 more)

### Community 15 - "compose-helpers.py"
Cohesion: 0.13
Nodes (15): box(), font(), panel(), Add a title strip above an image., sheet(), vbrace(), fig_pair(), AX() (+7 more)

### Community 16 - "CLAUDE.md (project design guidelines)"
Cohesion: 0.14
Nodes (15): Checkout leverans - tre forslag (page), CLAUDE.md (project design guidelines), eco-breadcrumb skill (Breadcrumb), eco-pagination skill (load more), eco-role-tier-card skill (Draft), prototype-guide skill (entry point for creative work), Design-skill suggestions are proposals, ECO breakpoints (xs/sm/md/lg/xl, md=769px) (+7 more)

### Community 17 - "eco-doc-page skill (docs page structure)"
Cohesion: 0.12
Nodes (17): eco-doc-page skill (docs page structure), Building blocks in `docs.css`, Component pages, Controls in a playground are the real components, Foundation pages, Hub (`overview.html`), Motion section, Page anatomy (in this order) (+9 more)

### Community 18 - "js/range.js"
Cohesion: 0.19
Nodes (13): pill-segment-control.css, init(), move(), init(), ECO Pill segment control component, ECO Toast component, ECO E-Com Toast component, Pill segment control: Code (+5 more)

### Community 19 - "Radio component"
Cohesion: 0.18
Nodes (14): components css menu stylesheet, components css radio stylesheet, components css range stylesheet, components/js/range.js, menu.html docs page, Menu component, menu-specifications.html docs page, radio-code.html docs page (+6 more)

### Community 20 - "generate-tokens.py"
Cohesion: 0.36
Nodes (13): extract_declarations(), fallback_value(), main(), normalize_typography_value(), parse_colors(), parse_radius_border(), parse_shadows(), parse_spacing() (+5 more)

### Community 21 - "button-pair.js"
Cohesion: 0.16
Nodes (10): ARROW, BOUNCE, BTN, DOWN, G, GW(), label(), mount() (+2 more)

### Community 22 - "Design review: implementation vs. Figma + ECO"
Cohesion: 0.15
Nodes (13): 1. Before you start — ask, don't guess, 2. Read the design, 3. Measure the implementation, 4. WCAG check (separate section in the report), 5. Verify before you report, 6. Severity, 7. Report structure, 8. Comparison images (optional) (+5 more)

### Community 23 - "List Item (ECO Design System)"
Cohesion: 0.17
Nodes (12): Axes, CSS, Flags (for design), HTML structure, List Item (ECO Design System), Rules, Size model, States (+4 more)

### Community 24 - "Tabs (ECO Design System)"
Cohesion: 0.13
Nodes (14): Anatomy, Choosing Primary or Secondary, Flags for design, HTML structure, On-page navigation (docs), On-page navigation (`tab-bar--page`), Rules, Size model (+6 more)

### Community 25 - "attach"
Cohesion: 0.35
Nodes (11): attach(), close(), group(), open(), pick(), render(), show(), loadData() (+3 more)

### Community 26 - "Table (ECO Design System) — first version"
Cohesion: 0.18
Nodes (10): CSS template, Dimensions, Flags, Header background, HTML structure, Rules, Surfaces and lines, Table (ECO Design System) — first version (+2 more)

### Community 27 - "Menu – Dropdown & Exposed Dropdown (ECO Design System)"
Cohesion: 0.18
Nodes (11): Container, CSS, Flags (for design), HTML structure, Menu – Dropdown & Exposed Dropdown (ECO Design System), Rules, Size model, States (Base Item) (+3 more)

### Community 28 - "Role Tier Card component"
Cohesion: 0.29
Nodes (9): components css role tier stylesheet, components css section stylesheet, role-tier-card.html docs page, role-tier-card-code.html docs page, Role Tier Card component, role-tier-card-specifications.html docs page, section-code.html docs page, Section component (+1 more)

### Community 29 - "eco-card-animation/SKILL.md"
Cohesion: 0.25
Nodes (6): Also on the component page, Open / always ask, Procedure (one component), Reusable pieces (do not rewrite), Techniques learned on Switch (reuse), Archived card visuals

### Community 30 - "Divider (ECO Design System)"
Cohesion: 0.22
Nodes (9): CSS, Divider (ECO Design System), Flags, HTML structure, NOT used when, Rules, Size, Used when (+1 more)

### Community 31 - "Switch (ECO Design System)"
Cohesion: 0.22
Nodes (9): CSS, Flags for design, HTML structure, Label typography (`eco-typography`), Rules, Size model, States, Switch (ECO Design System) (+1 more)

### Community 32 - "Text Area (ECO Design System)"
Cohesion: 0.22
Nodes (9): CSS, Flags, HTML structure, Rules, Size model, States, Text Area (ECO Design System), Typography (+1 more)

### Community 33 - "Adding a component to the design system"
Cohesion: 0.25
Nodes (8): 1. Gather inputs (ask if missing), 2. Extract from Figma (never from memory or guesswork), 3. Map every value to a token, 4. Write `.claude/skills/eco-<name>/SKILL.md`, 5. Register it, 6. Verify before reporting done, Adding a component to the design system, Don'ts

### Community 34 - "Pill Segment Control (ECO Design System)"
Cohesion: 0.25
Nodes (8): CSS template (Large, Primary/Pill — mobile-first), HTML and JS example, Interaction (sliding pill), Motion, Pill Segment Control (ECO Design System), Sizes, States, Variants

### Community 35 - "Radio button (ECO Design System)"
Cohesion: 0.25
Nodes (8): CSS, HTML structure, Label & message typography (`eco-typography`), Radio button (ECO Design System), Rules, Size model, States, When to use

### Community 36 - "tooltip.js"
Cohesion: 0.46
Nodes (6): alignSide(), globalTip(), needsFlip(), placeWrap(), safeTop(), show()

### Community 37 - "Old ECO Libraries Web Page (Storybook)"
Cohesion: 0.36
Nodes (8): ECO Slack channel as support and feedback route, Resources & Help page layout (left nav groups Libraries/Help/User Guides, hero, right TOC, link cards, prev/next, footer), Storybook docs playground pattern (live code, copy, property controls), Storybook Docs Canvas with Code Snippet and Controls Table, Storybook Alt Label Docs Page (Sidebar, Canvas, Controls), Old ECO Getting Help Overview Page, Old ECO Libraries Design Page (Figma), Old ECO Libraries Web Page (Storybook)

### Community 39 - "hero_switch.py"
Cohesion: 0.36
Nodes (4): call(), dim_h(), dim_v(), flat()

### Community 40 - "hero_switch_iso.py"
Cohesion: 0.43
Nodes (7): circ(), dim(), ext(), line(), P(), pill(), a, b: world coordinate range along `along`; off: world coordinate of the…

### Community 42 - "Old ECO DS start page (gamla startsidan)"
Cohesion: 0.38
Nodes (7): Docs page layout: left rail, sticky contents list, prev/next cards, footer, Storybook and Supernova documentation stack, Reference: dark category cards (Pick a category), Old ECO DS start page (gamla startsidan), Reference: dark centered hero with stats, Old ECO DS page: Introduction for Developers, Old ECO DS page: Introduction for Stakeholders

### Community 43 - "gen_button.py"
Cohesion: 0.33
Nodes (3): fig_cls(), pair_cls(), A figure whose stage has an extra class (dark surface).

### Community 44 - "radio.js"
Cohesion: 0.29
Nodes (4): ARROW, BX, DOT, mount()

### Community 45 - "card-check.mjs"
Cohesion: 0.29
Nodes (6): c, { chromium }, [comp, out = "/tmp/card"], errs, play, require

### Community 46 - "Pagination component"
Cohesion: 0.47
Nodes (6): components css pagination stylesheet, components/js/pagination.js, pagination.html docs page, pagination-code.html docs page, Pagination component, pagination-specifications.html docs page

### Community 47 - "switch.js"
Cohesion: 0.33
Nodes (3): ARROW, mount(), SW

### Community 48 - "Feature comparison with role tiers page"
Cohesion: 0.50
Nodes (5): Role tier comparison (Standard vs Administrator), Feature comparison page (permission levels), Feature comparison with role tiers page, Feature comparison roles (backup), Erbjudandedagar campaign page

### Community 49 - "Modal component"
Cohesion: 0.60
Nodes (4): modal-code.html docs page, Modal component, modal-specifications.html docs page, eco design system notifications css stylesheet

### Community 50 - "link_large"
Cohesion: 0.40
Nodes (5): link_large(), items: [(url, name, note)], refs(), three_pages(), parts_note()

### Community 51 - "hero_button_iso.py"
Cohesion: 0.70
Nodes (4): dim(), ext(), line(), P()

### Community 55 - "make-eco.mjs"
Cohesion: 0.40
Nodes (4): css, dir, eco, page

### Community 56 - "Feedback: Do not change table structure"
Cohesion: 0.50
Nodes (4): Feedback: Do not change table structure, Rule: never alter data-table structure (COLS order, column visibility JS), mypages/memory/MEMORY.md index, Rule: do not change data table structure in frontend

### Community 58 - "eco-collapsible skill"
Cohesion: 0.67
Nodes (3): eco-collapsible skill, components/css/collapsible.css, components/js/collapsible.js

### Community 59 - "btn_group"
Cohesion: 0.67
Nodes (3): bp_field(), btn_group(), buttons: [(value, text, pressed)]

### Community 79 - "eco-pill-segment-control skill"
Cohesion: 0.15
Nodes (15): eco-elevation skill, eco-pill-segment-control skill, Fluid width at xs only, Sliding pill thumb, Native input type=radio, eco-range skill, Flags, Native input type=range (+7 more)

### Community 80 - "button-group.js"
Cohesion: 0.18
Nodes (9): ARROW, BTN, DOWN, G, GW(), label(), mount(), SNAP (+1 more)

### Community 81 - "select.js"
Cohesion: 0.23
Nodes (9): ARROW, check(), flat(), G, GW(), label(), mount(), draw() (+1 more)

### Community 82 - "eco-radio skill"
Cohesion: 0.31
Nodes (10): eco-checkbox skill, eco-icon-picker skill, eco-input skill, eco-radio skill, eco-select skill (Select), eco-textarea skill, Single size, desktop-only Figma, components/css/checkbox.css (+2 more)

### Community 83 - "input.js"
Cohesion: 0.29
Nodes (8): ARROW, flat(), G, GW(), IBEAM, lay(), mount(), draw()

### Community 84 - "checkbox.js"
Cohesion: 0.22
Nodes (5): ARROW, BX, DASH, mount(), TICK

### Community 85 - "hairline/range.js"
Cohesion: 0.31
Nodes (7): ARROW, G, GW(), mount(), draw(), text(), VALUES

### Community 86 - "Resources overview page"
Cohesion: 0.48
Nodes (7): ECO docs Resources category, Resources: Design (Figma library), Resources: Getting help, Resources: Introduction for Developers, Resources: Introduction for Stakeholders, Resources overview page, Resources: Web (Storybook library)

### Community 87 - "Icon picker (ECO Design System)"
Cohesion: 0.40
Nodes (5): Behavior (same everywhere), Flags, Icon picker (ECO Design System), Rules, Use it

## Knowledge Gaps
- **292 isolated node(s):** `BTN`, `SNAP`, `DOWN`, `UP`, `ARROW` (+287 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 437 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **12 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `CLAUDE.md (project design guidelines)` connect `CLAUDE.md (project design guidelines)` to `eco-button skill`, `eco-doc-page skill (docs page structure)`, `eco-radio skill`, `Tabs (ECO Design System)`, `Table (ECO Design System) — first version`, `eco-card-animation/SKILL.md`?**
  _High betweenness centrality (0.029) - this node is a cross-community bridge._
- **Why does `eco-add-component skill` connect `eco-add-component skill` to `Adding a component to the design system`, `eco-button skill`, `eco-pill-segment-control skill`, `CLAUDE.md (project design guidelines)`, `eco-doc-page skill (docs page structure)`, `eco-radio skill`?**
  _High betweenness centrality (0.024) - this node is a cross-community bridge._
- **Why does `ECO Design System` connect `CLAUDE.md (project design guidelines)` to `Persona 2 – Lars, senior snickare och arbetsledare (kundtyp *Effektivitet och säkerhet*)`?**
  _High betweenness centrality (0.024) - this node is a cross-community bridge._
- **What connects `BTN`, `SNAP`, `DOWN` to the rest of the system?**
  _292 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `components/css/button-group.css` be split into smaller, more focused modules?**
  _Cohesion score 0.12006172839506173 - nodes in this community are weakly interconnected._
- **Should `eco-add-component skill` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._
- **Should `tabs.js` be split into smaller, more focused modules?**
  _Cohesion score 0.08295625942684766 - nodes in this community are weakly interconnected._