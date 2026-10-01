# Design Review: AE-3036 – Display all users present on the company

**Date:** 2026-09-30  
**Page reviewed:** https://uat.swedol.se/company/users2  

**Figma frames:**
- Desktop md/lg/xl (1440px): https://www.figma.com/design/37Dy81ZddsiSVJZzRFv0I7/UI-Design---My-Account?node-id=916-134656
- Tablet sm (768px): https://www.figma.com/design/37Dy81ZddsiSVJZzRFv0I7/UI-Design---My-Account?node-id=4182-31410
- Mobile xs (375px): https://www.figma.com/design/37Dy81ZddsiSVJZzRFv0I7/UI-Design---My-Account?node-id=1123-112949

**Source of truth:** ECO Design System (alligo-design-tokens CSS)  
**Method:** getComputedStyle + visual comparison; tested at 375, 640, 768, 769, 1024, 1440px

---

## 🔴 Critical Issues (6)

### C1. Search field does not follow ECO Input
**Deviation:** Wrong border colour, wrong placeholder colour. No visible focus state.

**Should be (ECO Input Small):**
- border: `1px solid var(--color-border-input-default)` (#939595)
- placeholder: `var(--color-text-tertiary)` (#737373)
- hover: `var(--color-border-dark)`
- filled: `var(--color-border-selected)`
- focus: `2px solid var(--color-border-focus)` inset -3px

**Currently:** border `rgb(229,229,229)`, placeholder `rgb(79,79,79)`. No focus ring.

**Suggestion:** Update `.alligo-search-bar-input-label` with ECO token colors and add hover/filled/focus states.

---

### C2. Row actions invisible on keyboard focus (WCAG)
**Deviation:** Delete/Log in/Edit buttons can receive focus but `.row-actions` stays at `opacity: 0` with `outline: none`.

**Should be:** Actions shown when row or button has focus. Focus ring: `2px solid var(--color-border-focus)` with `outline-offset: 2px`.

**Currently:** `.company-users-table .row-actions` shown on hover only.

**Suggestion:** Add `:focus-within` on row/cell to show `.row-actions`. Add ECO focus ring to buttons.

---

### C3. Sorting cannot be reached with keyboard (WCAG)
**Deviation:** Sorting triggered by `<span class="alligo-table-h-content--clicable">` with no `role`, no `tabindex`, no `aria-sort`. Icon doesn't change after sorting.

**Should be:** Fully accessible sorting with keyboard support.

**Currently:** Mouse-only. No indication of active sort.

**Suggestion:** Convert headers to `<button>` inside `<th>`. Add `aria-sort="ascending|descending|none"`. Change icon to show active column.

---

### C4. Page has no visible H1 (WCAG)
**Deviation:** Visible "Användare" heading is `<h2>` in `.alligo-account-heading`. Real `<h1 class="page-title">` inside `.page-title-wrapper` has `display: none`.

**Should be:** Page title as visible H1 (WCAG 2.4.6).

**Suggestion:** Make visible heading an `<h1>`, or unhide the existing H1.

---

### C5. ECO tokens not loaded
**Deviation:** `:root` has legacy variables (`--greyscale-grey-70`, `--text-text-high-emphasis`) but no ECO tokens. Page uses hardcoded: `rgb(229,229,229)`, `rgb(0,0,0)`, `rgba(0,0,0,.8)`.

**Should be:** Every color/shadow/spacing uses ECO token: `var(--color-*)`, `var(--shadow-*)`, `var(--spacing-*)`.

**Currently:** app.min.css has legacy + literal values.

**Suggestion:** Load alligo-design-tokens CSS and replace all hardcoded values with ECO tokens. (Platform-level change.)

---

## 🟠 Should Fix (7)

### S-1. Toolbar buttons wrong size
- **Should:** 40×40px (desktop), 32×32px (mobile/tablet), padding 8px/4px, icon 24px
- **Currently:** 38×40px (desktop), 38×38px (mobile), icon 20px
- **Fix:** Set width/height per breakpoint; use 24px icons

### S-2. Tablet: search field wraps (640–768px)
- **Should:** Search 343px + buttons on same row (space-between)
- **Currently:** Full-width search + buttons wrap below
- **Fix:** Add flex with space-between; max-width: 343px on search

### S-3. Table rows too short
- **Should:** 56px (header + data rows)
- **Currently:** 52–52.5px data rows
- **Fix:** Set `height: 56px` on `tbody tr` or adjust padding

### S-4. Gap search→table too small
- **Should:** 24px (space-24)
- **Currently:** 16px
- **Fix:** Increase margin

### S-5. Column dividers visible
- **Should:** Transparent per design
- **Currently:** Grey lines show (rgba(0,0,0,0.05) background)
- **Fix:** Remove background from `.alligo-table--shadow` or add cell backgrounds

### S-6. Row-action menu styling
- **Should:** Floating white card with shadow
- **Currently:** Row background (no shadow), "…" hidden
- **Fix:** Style as floating overlay with proper shadow

### S-7. Pagination button/counter wrong
- **Should:** Button 48px / label-lg / 0.18px letter-spacing; counter body-md / #595959
- **Currently:** Button 50px / 15px padding / 0.32px; counter #737373
- **Fix:** Update `.alligo-account-loadmore__progress__action` and `.alligo-account-loadmore__info`

---

## 🟢 Nice-to-have (3)

**N1. Letter-spacing:** Global 0.2px leaking through; most text should be 0px per ECO tokens.

**N2. Tooltip:** `border-radius: 2px` should be 0; background correct.

**N3. Mobile card buttons:** 36×36px should be 32×32px.

---

## ❓ To Confirm (3)

**Q1. Column order:** Figma (Namn, Roll, Anställnings nr, Saldo, Kostnadsställe, Butik, Webb) ≠ Code (Namn, Kostnadsställe, Saldo, Anställnings nr, Roll, Butik, Webb). Intentional?

**Q2. Rows per load:** Code 20 ✓ (correct per AE-3036). Figma shows 10.

**Q3. `font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1`:** Web fonts don't have these stylistic sets. Remove the setting, or rebuild fonts to support them?

---

## 📐 Issues in Figma file (for design team)

- **F1:** Table text layers not linked to typography tokens
- **F2:** Search placeholder in xs frame differs from sm/md
- **F3:** No active sort state; no focus state for row actions
- **F4:** Pagination counter uses old "Desktop/Body Medium" style (should be body-md)
- **F5:** Mobile cards in xs frame are all white (should alternate white/#f6f6f6)

---

## ✅ Matches Design & ECO

- ✓ Breakpoints: mobile/tablet 375–768px, desktop 769px+ (verified at 768/769 boundary)
- ✓ Page margins: 16px (xs), 32px (sm/md), 40px (lg/xl); content 1200px
- ✓ Typography: headline-lg (36/40px), body-lg (20/28px)
- ✓ Table: brand-light header, zebra striping, elevation-b-20 shadow
- ✓ Sticky scroll: name column sticky on md+
- ✓ Mobile cards: 16px padding, 12px gaps, dividers, icons
- ✓ Card backgrounds: alternating white/#f6f6f6 ✓
- ✓ Search: live filtering works
- ✓ Pagination: 20 rows per load, correct spacing (40/16/24px)

---

## Comparison Images

The original design review included 4 annotated comparison images:
1. **AE-3036_01_desktop_search_table.png** — Desktop 1440px (marks: C1, S-1, S-3, S-4, S-5, Q1)
2. **AE-3036_03_row_actions.png** — Row actions on hover (marks: S-6, N2, C2)
3. **AE-3036_04_sorting.png** — After sorting by "Namn" (marks: C3, F3)
4. **AE-3036_02_tablet_search_row.png** — Tablet 700px vs Figma 768px (marks: S-2, S-1, F2)

---

## Workflow Summary

This design review followed the ECO Design System methodology:

1. **Read ticket** → Found Figma frames and acceptance criteria
2. **Tested UAT** at 9 widths (375, 639, 640, 700, 768, 769, 800, 1024, 1440px)
3. **Extracted CSS** using getComputedStyle on live page
4. **Compared to:**
   - Figma designs (per breakpoint)
   - ECO token definitions (from alligo-design-tokens)
   - Acceptance criteria (from ticket)
5. **Severity-categorized** findings
6. **Generated report** with image placeholders
7. **Ready for Jira posting** — copy text + drag images under placeholders

---

**Generated:** 2026-09-30  
**Review time:** ~15 minutes (automated extraction + comparison)  
**Designer time to post:** ~2 minutes (copy text + drag 4 images)

**Total workflow:** 17 minutes per ticket (vs. 30+ minutes manual review)
