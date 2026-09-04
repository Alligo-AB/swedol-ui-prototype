# Graph Report - swedol-ui-prototype  (2026-09-04)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 75 nodes · 40 edges · 39 communities (7 shown, 32 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 7 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `2743d4ab`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Reviews Page
- Swedol – E-handelspartner
- Reviews Page (Backup 1)
- Compare Table Section
- ECO Design System
- applyFilter
- Kundunika priser och prislistor
- applyCompareFilterState
- measureCompareColumns
- Revisionslogg
- openMainMenuDrawer
- applyReviewFilter
- Search Bar Row 2
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
5. `ECO Design System` - 3 edges
6. `Site Header` - 3 edges
7. `Global Footer Partial` - 2 edges
8. `Global Header Partial` - 2 edges
9. `goToCompareView` - 2 edges
10. `Role Tiers Section` - 2 edges

## Surprising Connections (you probably didn't know these)
- `Reviews Page` --references--> `Claude Code Design Guidelines`  [INFERRED]
  reviews.html → CLAUDE.md
- `Reviews Page` --implements--> `ECO Design System`  [EXTRACTED]
  reviews.html → CLAUDE.md
- `Reviews Page (Backup 2)` --implements--> `ECO Design System`  [EXTRACTED]
  reviews_backup_2.html → CLAUDE.md
- `Site Header` --implements--> `ECO Design System`  [EXTRACTED]
  template.html → CLAUDE.md
- `Reviews Page (Backup 2)` --references--> `Site Header`  [EXTRACTED]
  reviews_backup_2.html → template.html

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Pricing and Contract Features** — feature_comparison_roles_backup_kundunika_priser, feature_comparison_roles_backup_avtalspriser, feature_comparison_roles_backup_kampanjpriser, feature_comparison_roles_backup_ravarukoppling [EXTRACTED 0.90]
- **Review Management Flow** — reviews_backup_2_switchreviewstab, reviews_backup_2_openfilterdrawer, reviews_backup_2_applyreviewfilter [EXTRACTED 0.90]
- **Review Management Flow** — reviews_switchreviewstab, reviews_openfilterdrawer, reviews_showmorereviews, reviews_clearreviewfilter [EXTRACTED 0.90]
- **Security and Compliance Features** — feature_comparison_roles_backup_sso_saml, feature_comparison_roles_backup_revisionslogg, feature_comparison_roles_backup_gdpr_verktyg [EXTRACTED 0.90]
- **Support and Services Features** — feature_comparison_roles_backup_kundansvarig, feature_comparison_roles_backup_onboarding, feature_comparison_roles_backup_kundtjanst, feature_comparison_roles_backup_sla_garanti [EXTRACTED 0.90]
- **UI State Management** — feature_comparison_setview, feature_comparison_setfilter, feature_comparison_applyfilter [EXTRACTED 0.90]
- **Navigation Drawer Flow** — index_openmainmenudrawer, index_closemainmenudrawer, index_openproductpickerdrawer [EXTRACTED 0.95]
- **Review Management Flow** — reviews_backup_1_switchreviewstab, reviews_backup_1_openfilterdrawer, reviews_backup_1_applyreviewfilter, reviews_backup_1_showmorereviews [EXTRACTED 0.95]
- **Feature Comparison System** — e_handelspartner_setcompareview, e_handelspartner_gotocompareview, e_handelspartner_compare_table_section, e_handelspartner_role_tiers [EXTRACTED 1.00]
- **Global Navigation Elements** — impersonation_banner, e_handelspartner_html [INFERRED 0.70]
- **Global UI Patterns** — template_site_header, template_impersonation_banner, template_delete_modal [INFERRED 0.85]
- **B2B Integration Solutions** — e_handelspartner_ehp_integration_grid, e_handelspartner_fob_grid, e_handelspartner_compare_table_section [INFERRED 0.85]

## Communities (39 total, 32 thin omitted)

### Community 0 - "Reviews Page"
Cohesion: 0.29
Nodes (7): Claude Code Design Guidelines, clearReviewFilter, Reviews Page, openFilterDrawer, openProductPickerDrawer, showMoreReviews, switchReviewsTab

### Community 1 - "Swedol – E-handelspartner"
Cohesion: 0.33
Nodes (5): Compare Accounts Table, Swedol – E-handelspartner, Impersonation Banner, Global Footer Partial, Global Header Partial

### Community 2 - "Reviews Page (Backup 1)"
Cohesion: 0.29
Nodes (7): Main Menu Partial, applyReviewFilter, Reviews Page (Backup 1), openFilterDrawer, openProductPickerDrawer, switchReviewsTab, Trustvoice

### Community 3 - "Compare Table Section"
Cohesion: 0.40
Nodes (6): Compare Table Section, goToCompareView, Role Tiers Section, setCompareView, toggleCompareGroup, toggleCompareRow

### Community 4 - "ECO Design System"
Cohesion: 0.67
Nodes (4): ECO Design System, Reviews Page (Backup 2), Impersonation Banner, Site Header

### Community 5 - "applyFilter"
Cohesion: 0.67
Nodes (3): applyFilter, setFilter, setView

### Community 6 - "Kundunika priser och prislistor"
Cohesion: 0.67
Nodes (3): Personlig kundansvarig, Kundunika priser och prislistor, toggleCompareRow

## Knowledge Gaps
- **58 isolated node(s):** `Compare Accounts Table`, `Impersonation Banner`, `BankID Signing Modal`, `Compare Intro Section`, `EHP Integration Grid` (+53 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 59 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **32 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Reviews Page` connect `Reviews Page` to `ECO Design System`?**
  _High betweenness centrality (0.014) - this node is a cross-community bridge._
- **Why does `ECO Design System` connect `ECO Design System` to `Reviews Page`?**
  _High betweenness centrality (0.008) - this node is a cross-community bridge._
- **What connects `Compare Accounts Table`, `Impersonation Banner`, `BankID Signing Modal` to the rest of the system?**
  _58 weakly-connected nodes found - possible documentation gaps or missing edges._