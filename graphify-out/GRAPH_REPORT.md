# Graph Report - swedol-ui-prototype  (2026-09-04)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 126 nodes · 90 edges · 50 communities (11 shown, 39 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 14 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `2743d4ab`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- ECO Design System
- Cookie Banner (ECO Design System)
- Reviews Page
- Swedol – E-handelspartner
- Reviews Page (Backup 1)
- Compare Table Section
- Welcome Email Template
- Typography Skill
- showAddrToast
- applyFilter
- Kundunika priser och prislistor
- Address Book Page
- Site Header
- applyCompareFilterState
- measureCompareColumns
- Revisionslogg
- openMainMenuDrawer
- applyReviewFilter
- Search Bar Row 2
- Tooltip Skill
- BankID Signing Modal
- Compare Intro Section
- EHP Integration Grid
- Features Out of Box Grid
- Form Checkboxes
- Site Header Small (Mobile)
- Avtalspriser
- mypages/partials/footer.html
- GDPR-verktyg och dataexport
- Kampanjpriser
- Kundtjänst (chatt, e-post, telefon)
- mypages/partials/main-menu.html
- Onboarding och utbildning
- Råvarukoppling på priser
- SLA-garanti för svarstider
- Compare Card Grid
- toggleCategory
- toggleDetail
- 3D Secure Logo
- Swedol Store Borås
- Category: El & Belysning
- Category: Kläder & Skydd
- closeMainMenuDrawer
- toggleCollapsible
- updateBorder
- swedol-ui-prototype README
- showMoreReviews
- BankID Signing Modal
- Store Nav Row 3
- Delete Confirmation Modal

## God Nodes (most connected - your core abstractions)
1. `Reviews Page` - 7 edges
2. `Reviews Page (Backup 1)` - 5 edges
3. `Swedol – E-handelspartner` - 4 edges
4. `Compare Table Section` - 4 edges
5. `Notifications Guide Skill` - 4 edges
6. `Cookie Banner (ECO Design System)` - 4 edges
7. `Site Header` - 3 edges
8. `Action Link Skill` - 3 edges
9. `Links Guide Skill` - 3 edges
10. `Section Skill` - 3 edges

## Surprising Connections (you probably didn't know these)
- `Reviews Page` --references--> `Claude Code Design Guidelines`  [INFERRED]
  reviews.html → CLAUDE.md
- `Reviews Page (Backup 2)` --references--> `Site Header`  [EXTRACTED]
  reviews_backup_2.html → template.html
- `Cookie Banner (ECO Design System)` --semantically_similar_to--> `Cookie Banner`  [INFERRED] [semantically similar]
  mypages/cookie-banner_v1.html → mypages/cookie-banner.html
- `Welcome Email Template` --references--> `Email Hero Image`  [EXTRACTED]
  email/email.html → email/images/hero.jpg
- `Welcome Email Template` --references--> `Swedol Footer Logo`  [EXTRACTED]
  email/email.html → email/images/logo-footer.png

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Address Management Flow** — mypages_addressbook_openaddressdrawer, mypages_addressbook_renderaddresstable, mypages_addressbook_showaddrtoast [EXTRACTED 0.90]
- **Pricing and Contract Features** — feature_comparison_roles_backup_kundunika_priser, feature_comparison_roles_backup_avtalspriser, feature_comparison_roles_backup_kampanjpriser, feature_comparison_roles_backup_ravarukoppling [EXTRACTED 0.90]
- **Review Management Flow** — reviews_backup_2_switchreviewstab, reviews_backup_2_openfilterdrawer, reviews_backup_2_applyreviewfilter [EXTRACTED 0.90]
- **Review Management Flow** — reviews_switchreviewstab, reviews_openfilterdrawer, reviews_showmorereviews, reviews_clearreviewfilter [EXTRACTED 0.90]
- **Security and Compliance Features** — feature_comparison_roles_backup_sso_saml, feature_comparison_roles_backup_revisionslogg, feature_comparison_roles_backup_gdpr_verktyg [EXTRACTED 0.90]
- **Support and Services Features** — feature_comparison_roles_backup_kundansvarig, feature_comparison_roles_backup_onboarding, feature_comparison_roles_backup_kundtjanst, feature_comparison_roles_backup_sla_garanti [EXTRACTED 0.90]
- **Swedol Brand Assets** — email_images_logo_header_png, email_images_logo_footer_png, email_images_logo_header_svg, email_images_logo_footer_svg [EXTRACTED 0.90]
- **UI State Management** — feature_comparison_setview, feature_comparison_setfilter, feature_comparison_applyfilter [EXTRACTED 0.90]
- **Navigation Drawer Flow** — index_openmainmenudrawer, index_closemainmenudrawer, index_openproductpickerdrawer [EXTRACTED 0.95]
- **Review Management Flow** — reviews_backup_1_switchreviewstab, reviews_backup_1_openfilterdrawer, reviews_backup_1_applyreviewfilter, reviews_backup_1_showmorereviews [EXTRACTED 0.95]
- **Feature Comparison System** — e_handelspartner_setcompareview, e_handelspartner_gotocompareview, e_handelspartner_compare_table_section, e_handelspartner_role_tiers [EXTRACTED 1.00]
- **Cookie Consent Management** — mypages_cookie_banner_v1_html, mypages_cookie_banner_v1_submitconsent, mypages_cookie_banner_v1_toggleacc [EXTRACTED 1.00]
- **ECO Design System Components** — claude_skills_tile_link_skill, claude_skills_toast_ecom_skill, claude_skills_toast_system_skill, claude_skills_tooltip_skill, claude_skills_typography_skill [EXTRACTED 1.00]
- **Link System Components** — skills_links_guide_skill, skills_inline_link_skill, skills_action_link_skill [EXTRACTED 1.00]
- **Notification System Components** — skills_notifications_guide_skill, skills_inline_notification_skill, skills_banner_notification_skill, skills_modal_ecom_skill [EXTRACTED 1.00]
- **Global Navigation Elements** — impersonation_banner, e_handelspartner_html [INFERRED 0.70]
- **Global UI Patterns** — template_site_header, template_impersonation_banner, template_delete_modal [INFERRED 0.85]
- **B2B Integration Solutions** — e_handelspartner_ehp_integration_grid, e_handelspartner_fob_grid, e_handelspartner_compare_table_section [INFERRED 0.85]
- **Security Verification Pattern** — mypages_addressbook_openbillingbankidmodal, mypages_addressbook_html [INFERRED 0.85]
- **Form Element Components** — skills_input_skill, skills_select_skill, skills_checkbox_skill, skills_segment_control_skill [INFERRED 0.90]

## Communities (50 total, 39 thin omitted)

### Community 0 - "ECO Design System"
Cohesion: 0.12
Nodes (23): ECO Design System, Action Link Skill, Badge Skill, Banner Notification Skill, Breadcrumb Skill, Button Skill, Checkbox Skill, Collapsible Skill (+15 more)

### Community 1 - "Cookie Banner (ECO Design System)"
Cohesion: 0.29
Nodes (7): Alligo Design Tokens, Cookie Banner, Cookie Banner (ECO Design System), submitConsent, toggleAcc, Dashboard Test Page, openAccountNavDrawer

### Community 2 - "Reviews Page"
Cohesion: 0.29
Nodes (7): Claude Code Design Guidelines, clearReviewFilter, Reviews Page, openFilterDrawer, openProductPickerDrawer, showMoreReviews, switchReviewsTab

### Community 3 - "Swedol – E-handelspartner"
Cohesion: 0.33
Nodes (5): Compare Accounts Table, Swedol – E-handelspartner, Impersonation Banner, Global Footer Partial, Global Header Partial

### Community 4 - "Reviews Page (Backup 1)"
Cohesion: 0.29
Nodes (7): Main Menu Partial, applyReviewFilter, Reviews Page (Backup 1), openFilterDrawer, openProductPickerDrawer, switchReviewsTab, Trustvoice

### Community 5 - "Compare Table Section"
Cohesion: 0.40
Nodes (6): Compare Table Section, goToCompareView, Role Tiers Section, setCompareView, toggleCompareGroup, toggleCompareRow

### Community 6 - "Welcome Email Template"
Cohesion: 0.33
Nodes (6): Welcome Email Template, Email Hero Image, Swedol Footer Logo, Footer Logo SVG, Swedol Header Logo, Header Logo SVG

### Community 7 - "Typography Skill"
Cohesion: 0.67
Nodes (4): Tile Link Skill, E-Com Toast Skill, System Toast Skill, Typography Skill

### Community 9 - "applyFilter"
Cohesion: 0.67
Nodes (3): applyFilter, setFilter, setView

### Community 10 - "Kundunika priser och prislistor"
Cohesion: 0.67
Nodes (3): Personlig kundansvarig, Kundunika priser och prislistor, toggleCompareRow

### Community 12 - "Site Header"
Cohesion: 0.67
Nodes (3): Reviews Page (Backup 2), Impersonation Banner, Site Header

## Knowledge Gaps
- **83 isolated node(s):** `clearReviewFilter`, `openFilterDrawer`, `openProductPickerDrawer`, `showMoreReviews`, `switchReviewsTab` (+78 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 88 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **39 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Reviews Page` connect `Reviews Page` to `ECO Design System`?**
  _High betweenness centrality (0.022) - this node is a cross-community bridge._
- **Why does `Site Header` connect `Site Header` to `ECO Design System`?**
  _High betweenness centrality (0.004) - this node is a cross-community bridge._
- **What connects `clearReviewFilter`, `openFilterDrawer`, `openProductPickerDrawer` to the rest of the system?**
  _83 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `ECO Design System` be split into smaller, more focused modules?**
  _Cohesion score 0.11857707509881422 - nodes in this community are weakly interconnected._