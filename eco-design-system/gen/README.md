# Generator for the three-page component docs

**The pages in `../components/` are the real files.** Edit them by hand like any other page. The generator is a **starting point for a new component**, not the source of the existing ones: it refuses to overwrite a page that exists (add `--force` only when you want to rebuild a page and lose its hand edits).

Builds `<name>.html`, `<name>-specifications.html` and `<name>-code.html` in `../components/`. Run from this folder:

```bash
cd eco-design-system/gen
python3 gen_checkbox.py            # skips pages that already exist
python3 gen_checkbox.py --force    # overwrites them
```

- `build.py`: the shared page frame (head, breadcrumb, intro, tabs, scripts) and helpers (`emit`, `section`, `table`, `rules`, `fig_pair`, `fig_one`, `ol_parts`, `toolbar`, `btn_group`, `old_js` …). Mirrors `components/tooltip*.html`.
- `gen_<name>.py`: one per Form component (2026-10-12), per Actions component (`gen_button.py`, `gen_button_group.py`, 2026-10-13) per Notification type (`gen_toast.py`, `gen_toast_ecom.py`, `gen_modal.py`, `gen_banner.py`, `gen_inline.py`, 2026-10-13), per Menus, lists and dividers component (`gen_menu.py`, `gen_list_item.py`, `gen_divider.py`) and per Link type (`gen_inline_link.py`, `gen_action_link.py`, `gen_tile_link.py`, 2026-10-13); per Status and navigation component (`gen_pagination.py`, 2026-10-19; Tooltip and Badge earlier, Breadcrumb has `gen_breadcrumb_*.py`), per Layout and content component (`gen_section.py`, `gen_collapsible.py`, 2026-10-14; `gen_role_tier_card.py` for the Draft Role tier card, 2026-10-15; the Docs table is a docs-only page in `foundations/` and is not generated); `gen_breadcrumb.py` (hub), `gen_breadcrumb_base.py` and `gen_breadcrumb_bar.py` (type sets, shared `bc.py`) were added 2026-10-19 for Breadcrumb; `gen_links_guide.py` builds the Links guide hub (one page, no tab bar, same emitter as `gen_notifications.py`), as it was when the pages were created (and the Do/Don't additions that followed). It may be behind the pages if they were edited by hand afterwards.
- `notif.py`: what the five notification sets share (the `pre_css` that loads `notifications.css` before `docs.css`, the scripts, the page-local style, playground field helpers, the `parent` hub for the breadcrumb). `gen_notifications.py` builds the hub `notifications.html` (one page, no tab bar), which is a different frame from the three-page sets.
- `old-source/`: the one-page versions the components had before. `old_js(name, start, end)` slices the old component builder (`field()`, `radio()`, `cb()` …) out of them, so builders are copied, not rewritten.

To convert another component: copy the nearest `gen_*.py`, change the texts and the script, put the old page in `old-source/` first (`git show <commit>:eco-design-system/components/<name>.html`), run it, then edit the result by hand. Rules: `.claude/skills/eco-doc-page/SKILL.md`.

`sel()` (a Small `eco-select` playground field) and `fig_one(..., stage_cls=)` (for example `ds-stage--dark`) are in `build.py`.

Optional keys of the component dict: `pre_css` (links placed **before** `docs.css`, for the Examples and Specifications pages, or the kinds in `pre_css_kinds`: used for `notifications.css`, so that the files `docs.css` imports win), `parent` (`(href, title)` of a hub: breadcrumb `Components / Notifications / Toast`), `head_extra` (raw `<link>` lines added to the head of the Examples page only, placed **before** the component CSS so the component files win: `notifications.css` has its own `.btn` base that shrinks every button to 32px if it comes after `button.css`), `css_before`, `css`, `head_js`, `body_js`, `select_menu`, `tooltip`.

Optional keys for a Storyblok tab (fourth page, `<slug>-storyblok.html`): `sb` (list of `(id, html)` sections, turns the tab on), `lead_sb` (second lead paragraph), `js_sb` (page script). Reference: `gen_collapsible.py` (`shot()` builds a screenshot with numbered `badge-number` markers in percent positions). One widget per tab: the tab documents only the widget of its own component; other widgets get their own tab on their own component page.

`gen_colors.py` (2026-10-22) builds the three Colors pages in `../foundations/` (Overview / Primitive colors / Semantic tokens) with the custom page set; keys `out`, `crumb_group`, `first_plain` of `build.py` were added for it. The shared script is `../color-kit.js`. Old page: `old-source/colors.html`.

`hero_switch.py` is not a page generator: it prints the blueprint SVG of the Switch header art (see `eco-doc-page`, section Header art).
`hero_switch_iso.py` (isometric version, same camera as the figure) and `build_switch_header_versions.py` (builds `components/switch-header-versions.html`, the three header layouts side by side) belong to the same header-art experiment.
`hero_switch_iso.py scene` prints the wide background scene (version 2b, figure included as a foreignObject).

`gen_hero_banner_widget.py` (2026-10-21) builds the four-tab Hero banner Storyblok widget docs with the custom page set `pages=[…]` (see `build.py` `PG()`); `hero_pins.py` holds the marker positions for the Storyblok screenshots.
`doc-kit.js` `DK.callouts`: `len` may be a function(rect) (used by `gen_hero_banner_widget.py` to put all badges of a figure in one column). `badge_list()` there renders legends with the round number badge.
