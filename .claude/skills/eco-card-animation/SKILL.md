---
name: eco-card-animation
description: Use when making an animated Hairline illustration (isometric line figure that answers the pointer) for a component and putting it on its card on the ECO overview pages — the whole procedure from concept to card, with the reusable files, the ECO colouring, the card integration, hover tour, archiving the old visual and the verification scripts. Not for the component pages themselves and not for static images.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack and the quality checklist. Everything lives in `hairline/` (read `hairline/README.md` too); the figure engine is the global skill `hairline-create` (never edit its kernel). Cards done: Button, Switch, Checkbox, Select, Input, Range, Textarea, Toast (System). References: **Button** (`hairline/button-pair.js`) and **Switch** (`hairline/switch.js`, the more complete one, copy from it). Press-and-pop springs for joined/segmented parts: `hairline/button-group.js` (selected part sinks, the former pick pops up, tint via `data-show` + CSS opacity transition).
> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack and the quality checklist. Everything lives in `hairline/` (read `hairline/README.md` too); the figure engine is the global skill `hairline-create` (never edit its kernel). Cards done: Button, Switch, Checkbox, Select, Input, Range, Textarea, Banner (close = banner slides off the page, content follows; no opacity allowed in figures). References: **Button** (`hairline/button-pair.js`) and **Switch** (`hairline/switch.js`, the more complete one, copy from it). Press-and-pop springs for joined/segmented parts: `hairline/button-group.js` (selected part sinks, the former pick pops up, tint via `data-show` + CSS opacity transition).

## When a figure in `hairline/` is changed (check this every time)

The figure file `hairline/<name>.js` is the one source: the card (`embed.js`) and the docs-page header (foreignObject in the scene, `data-flat`) both fetch it on page load, so a change shows in both after a reload. Then check the four places that do not follow by themselves, and say which one needs work:

1. **The header drawing holds the figure's numbers.** `eco-design-system/gen/hero_<name>_iso.py` has the camera constants (from `Cam` + `fit`), the slab, slot/button positions and sizes written out. If a change moves or resizes geometry, camera, scale or fit points, lines and dimensions no longer match: recompute the constants (kernel `proj`), rerun the generator and paste the SVG into the page header (and `gen/build_switch_header_versions.py` for the Switch comparison page). Colour, motion, height, cursor and behaviour changes usually need nothing.
2. **The bench pages are built copies.** `hairline/hairline-<name>.html` and `.eco.html` have the figure baked in: run `look.mjs` and `node hairline/make-eco.mjs <name>` again, or they show the old figure. They are not linked to the cards or headers.
3. **Colours live in two places.** Cards and docs pages: `hairline/hairline-card.css` (scoped `[data-hairline="<name>"]` when part names clash). The bench: `hairline/<name>.eco.css`. Change both. Scene-only colours (slab, opacities) are in `eco-design-system/doc-hero.css`.
4. **The header uses `data-flat`.** The figure's flat-slab branch (`stage.hasAttribute("data-flat")`) only runs in the header; a change to the slab can affect the header and not the card, or the reverse. Look at both.

Also: browser cache after a change; the kernel copy `hairline/kernel.js` has two patches (`tour(..., delay, pace)`); a faster hover tour per card: `data-travel="450" data-dwell="450"` on the card div (defaults 900/1200 ms).

## Procedure (one component)

1. **Ask first** (`AskUserQuestion`): a screenshot of the real component (states, sizes), the concept (offer 2–3 one-liners: object · what the pointer does · read-out · tour), and whether the drawn cursor rests visible above the component. The README's defaults: cursor visible at rest, black arrow.
2. **Read** `hairline/README.md`, the skill's `concepts.md`, `rules.md`, `look.md`, the kernel index (top of `kernel.js`) and a reference figure. Component spec from `.claude/skills/eco-<name>/SKILL.md` (colours, proportions, **timing**: the figure's motion copies the component's transition, e.g. Switch 150 ms `ease-standard`).
3. **Write `hairline/<name>.js`** (≤200 lines, in the shape of `switch.js`). Build + check from `hairline/`:
   `node ~/.claude/skills/hairline-create/look.mjs <name>.js --answer x,y,z --edge x,y,z --edge x,y,z` (world points; it prints the `?at=` screen points). Fix every failed line; read the sheet.
4. **ECO skin**: `hairline/<name>.eco.css` (copy `switch.eco.css`), then `node hairline/make-eco.mjs <name>` → `hairline-<name>.eco.html`. Colours only via tokens, only in CSS keyed on the figure's `data-part` attributes (the validator rejects colours/fills inside the figure page).
5. **Card**: `hairline/hairline-card.css` (colours for the card, keyed `[data-hairline="<name>"]` when a part name clashes with another figure, e.g. `ink` is black on Button, green on Switch). Then in `eco-design-system/components-overview.html` (ask first, README rule 1; also `index.html` has its own cards — ask which):
   - archive the old visual to `eco-design-system/card-visuals-archive/<component>.html` (markup + where it goes + how to switch back) and add a line to that folder's README;
   - replace the card's `ds-card__visual` with `<div class="ds-card__visual ds-card__visual--hairline" aria-hidden="true"><div data-hairline-card="<name>" data-play data-src="../hairline/<name>.js"></div></div>` (`data-play` runs the tour while the card is hovered or keyboard-focused, no play button; `kernel.js`, `embed.js`, `hairline-card.css` are already on the page);
   - centre it: the stage is 300 px wide, 5:4, `translateY(-16px)`; the figures' drawn extents differ, so add `.ds-card__visual--hairline [data-hairline-card="<name>"] { transform: translateY(Npx); }` in `hairline-card.css` until the content rows are centred (the check script prints them; Switch uses −5 px).
6. **Show it**: right after step 4, serve the repo (port ≠ 4173), `navigate` the built-in browser to `/hairline/hairline-<name>.eco` and `show_pane preview`, so the user sees it and can adjust at once (SendUserFile render does not work for it).
7. **Verify**: `npx serve . -l 4173` (if another session already holds 4173, serve on another port and run a copy of `card-check.mjs` with the port changed; the script is hardcoded to 4173 and its play-button step is a no-op now that cards use hover-`data-play`, so also hover the card with a real mouse and screenshot a few seconds of the tour) (repo root; `file://` does not work for cards), then `node hairline/tools/card-check.mjs <component> <outPrefix>` and read the PNGs: rest, hover, play (4 s into the tour). Plus the working routine in `CLAUDE.md` (mobile width, real mouse). State what was not tested.
8. **Sweep**: update `hairline/README.md` ("På korten"), this skill if something new was learned, the memory `project_hairline_card_animations.md`, and mention changed skills. Do not touch `index.html` unless asked.

## Reusable pieces (do not rewrite)

| File | What |
|---|---|
| `hairline/switch.js` | reference figure: recessed slots, thumbs, ghost-driven tour, component timing, cursor |
| `hairline/<name>.eco.css`, `hairline-card.css` | ECO colours from tokens, card stage |
| `hairline/embed.js` | mounts figures into cards (`data-hairline-card`, `data-src`, `data-play`); hovering/focusing the card runs `HL.tour(stage, stops, cb, 0)`, leaving stops it |
| `hairline/kernel.js` | copy of the skill's kernel with ONE patch: `tour(stage, stops, onStop, delay)` so the hover tour starts at once. Re-apply if the skill's kernel is updated |
| `hairline/make-eco.mjs <name>` | builds `hairline-<name>.eco.html` from the clean page + eco css |
| `hairline/tools/card-check.mjs` | Chrome check of a card: console, hover, play, content rows for centring |

## Techniques learned on Switch (reuse)

- **Recessed slot** in a slab: slab thicker than the slot depth `D` (PT 6, D 2); draw per slot, in this order: floor ring at `PT−D` (class `lo`, gets the colour), far-wall strip (`run(ring, q => !front(q))` at `PT` joined to the same at `PT−D` reversed; darker shade in CSS with `color-mix`), a floor-edge outline (`nf lo`, so an inked floor keeps an edge), the rim ring at `PT` (`nf`), the sunk part (thumb), then a **near lip** polygon (`fo`, the near run `PT`↔`PT−D`) plus the near rim line (`nf`) painted over it so the sunk part is hidden. Thumb foot `PT−D+0.6`; hover **sinks** the thumb top (it is fixed in the slot), never lifts it.
- **Parts that change colour by state**: set `data-part` (`track`/`ink`, `…-wall`) and `data-hover` in JS; all fills in CSS (`switch.eco.css`, `hairline-card.css`). Never `fill`/`style` in the figure.
- **Component timing instead of rule 08**: when the user asks for the component's feel, use a timed slide with `bezier(...)` and the component's duration (Switch: 150 ms, `bezier(.35,0,.35,1)`), tick-driven, `reducedMotion()` jumps. Say that it departs from rule 08.
- **Tour that presses**: the tour only calls `move(p, e)` (never `down`); the ghost has `e.pointerType === "ghost"`. Detect it, toggle after ~250 ms with no new ghost move (`gt`, `gdone` flag, tick keeps returning true meanwhile), and on the ghost's `leave` restore every state to its initial value so the lap ends at the rest pose.
- **Drawn cursor**: black arrow polygon (`dot`, `data-part="cursor"` filled black in CSS), springs follow the pointer, rests above the main part, sinks 2.5 px on press. Breaks skill rule 10 on the user's request; say so at hand-over.
- **Tried and rejected on Switch** (do not redo without being asked): a pointing-hand cursor (outlined, thick stamped outline, finger lines): looked clumsy, user went back to the arrow.
- **Sliding pill** (`hairline/pill.js`, Pill Segment Control): the thumb is a black `solid` whose `sil` gets `data-part="pill"`; labels are drawn twice, grey on the slot floor before the thumb and white on the thumb top after it, and `draw` shows whichever the thumb covers (`|s − i| < 0.5`); the inactive label's underline is a thin flat quad. Glyph set copied from `select.js`, pruned to the letters used (ALL/NEW) to stay under 200 lines.
- **Testing the hover tour**: the tour only runs while the real pointer is *off* the figure (pointer over the stage = `hand`). In Playwright hover the card body below the visual, not its centre.
- **Closing toast** (`hairline/toast.js`, copied from `toast-ecom.js`): floating panel + shadow path (`tshadow`), flat status strip, glyph text, close cross; a press closes it (out 150 ms accelerate, in 300 ms decelerate after `REOPEN`), the ghost's `leave` restores it. A tour needs at least three stops (two panel points and `null`s).
- **Open/close state (Modal, Select menu)**: the figure only toggles `data-open` on a group (`data-part="fade"`); the opacity transition (`--duration-medium-2`, `--ease-standard`, off under `prefers-reduced-motion`) lives in CSS (`modal.eco.css`, `hairline-card.css`). Geometry that sinks/rises goes on a spring (k 45, c 13.4); a closed figure sets `display:none` when `o < 0.02`. A press that closes something reopens it from the tick after a fixed time (Modal: 1100 ms), and the ghost's `leave` forces it open, so the tour lap ends at the rest pose. The drawn cursor follows the pointer over the whole stage (not only over parts), so a tour reads as a glide; keep the hit test on the target pose (`open` flag), not the faded one.
- **Tour stops must sit on a part**: `look.mjs` prints the `?at=` screen point for `--answer`; derive other stops from it (a wrong stop makes the ghost never hover anything). Test the hover tour with the mouse *outside* the stage (card body), a pointer over the stage pauses the tour.
- Range slider = one number in the figure's own units, three values moving one way; hover answers on a 240 px thumbnail are subtle, so `look.mjs` warns on item 3; that is accepted when the press is the big gesture.

- **Figure = the component itself, floating panel + replay (modelled on `modal.js`: glyph text via `label()`, cast shadow that follows the panel, raised buttons that sink on hover, press on a button closes and it reopens)** (`hairline/toast-ecom.js`, E-Com Toast; a first version with a product box and cart tray was rejected as "not like the component": draw the real component, visible at rest): press closes it, a pause later it slides back; timed tweens (`slide`, own duration/bezier per direction: in = decelerate-emphasized 300 ms, out = accelerate-generic 150 ms, set on each target change). A hidden part is `display:none` while closed; pick it only while its target is shown (rule 01). The ghost's `leave` resets.

## Also on the component page

The same figure can sit in the docs page header, fading into a technical drawing: see `eco-doc-page`, section "Header art" (`doc-hero.css`, `gen/hero_switch.py`). Switch is the only one so far.

## Open / always ask

Which cards on `index.html` too; Swedol accent colours; dark mode (ECO has none); a new `eco-*` skill or CLAUDE.md row for anything not covered. Answer in Swedish, short; ask before putting a component on a card.
