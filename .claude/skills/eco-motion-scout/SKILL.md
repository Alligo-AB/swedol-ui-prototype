---
name: eco-motion-scout
description: Use PROACTIVELY, without being asked, whenever a page, flow or component is built or changed in this repo and it has state changes that jump (swap, appear, disappear, count, confirm, expand, list rows added or removed). Run the scan at the end of the task, after the work is verified and before wrap-up, and add at most 3-5 sober micro-animation proposals as a numbered list with a reason each; apply only the ones the user picks. Also use when asked "where can we animate?" or "make it feel better". Not for campaign scroll effects (eco-motion, "Campaign motion") and not for choosing easing/duration (eco-motion).
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for the rules that always apply. Values come from `eco-motion` (tokens only). This skill decides **where** and **what kind**; `eco-motion` decides **how fast and with which curve**.

## Proactive use (the point of this skill)

The user should not have to remember to ask. In **every session** that creates or changes a page, flow or component:

1. Finish and verify the requested work first. Never let the scan delay or change it.
2. Then run the scan (below) on **only what was touched**, quickly (read, grep, no new files).
3. If it finds jumps worth fixing, add a short **"Motion proposals"** block to the closing message: 3-5 numbered items, one line reason each, per the proposal format. If nothing worth proposing, say nothing (no "no animations found" noise).
4. **Never apply unasked.** Proposals only; the user picks (CLAUDE.md proposals rule). Do not ask again if they ignore it, and do not repeat the same proposals later in the session.
5. Skip the scan for: pure docs-page text edits, token/CSS-only fixes, copy changes, bug fixes with no UI state, and pages the user said are final.
6. Keep it cheap: a proactive scan is a read of the changed code, not a full audit; offer a full audit only on request.

## Purpose

A serious e-commerce site (workwear, tools, B2B) should feel precise and calm. Motion is there to **explain a change**, never to decorate. A good animation answers one of these: *what just changed?*, *where did it go?*, *did my action work?*, *what is related to what?*

Reference that set the manner: the Radmärkning link on `cart.html` (2026-11-26). The label folds away, the pencil turns out and the × turns in, 150–200 ms, `ease-standard`. Small, one idea, state driven by `aria-expanded`, off under reduced motion. Every proposal should feel like a sibling of that.

## The ECO manner (what every animation must have)

1. **One idea per animation.** One thing changes meaning (swap, reveal, confirm, count). Never fade + slide + scale + colour all at once. Two properties at most, three only for a swap (opacity + rotate + scale, as in the cart icon).
2. **Small and short.** Distance ≤ 25 % of the view and almost always ≤ 16 px; `duration-fast-3` / `fast-4` for state changes, `duration-medium-1…3` for surfaces that enter (drawers, panels). Nothing above `duration-medium-4` in a product flow; `slow-*` only for empty/loading states.
3. **Tokens only.** `var(--duration-…)` and `var(--ease-…)`. Hover/swap/collapse = `ease-standard`; enter = `ease-decelerate-emphasized` (or `-generic` when lighter); exit = `ease-accelerate-generic` and shorter than the enter.
4. **State drives it, not script.** Prefer CSS driven by an attribute that already exists (`aria-expanded`, `aria-pressed`, `[hidden]`→`.is-open`, `:has()`, `:focus-visible`). Script only to set the state or to count. Never an animation that exists only in JS timing.
5. **Animate cheap properties.** `opacity`, `transform`, and `grid-template-rows/columns` 0fr↔1fr for height/width collapse (the Collapsible and cart-row pattern). Never animate `height: auto`, `top/left`, `box-shadow` size on long lists, or `filter` on big areas.
6. **Never in the way.** Content readable and controls clickable at once. No waiting, no blocking, no animation before an action can be taken. Interruptible: a second click mid-animation just reverses it. Focus is never lost or delayed by an animation.
7. **`prefers-reduced-motion: reduce` = off** for movement (`transition: none`, final state at once). A pure colour/opacity change may stay if short. Always include the media query, every time.
8. **Same thing, same motion.** If the pattern exists below, reuse it. Do not invent a second way to expand a row, show a toast or swap an icon.
9. **Honest.** No fake progress, fake scarcity or "thinking" delays. A count-up ends on the real number. A loader appears only when something really loads.

## Where it must NOT go

- My Pages, forms and tables: **no** scroll effects, reveals, parallax or count-up (CLAUDE.md). Only functional state feedback (rows 1–9 below), at `fast-*`, never delaying input.
- Anything the user does many times in a row (typing, table sorting, stepper clicks in a long list): keep to `fast-2…3` or no motion; repetition turns charm into friction.
- Error messages and validation: no bounce or shake. Fade/expand in, nothing more.
- Text the user is reading. No moving text blocks, no marquee.
- Price. A price may change calmly (see 9) but never flashes, rolls or pulses (the earlier "price roll" was removed on purpose).

## Catalogue of approved patterns

Each row: the situation, the motion, tokens, and where it already exists (reuse the code, do not copy a new variant).

| # | Situation (state change that jumps) | Motion | Tokens | Exists in |
|---|---|---|---|---|
| 1 | **Icon or label swap** on one control (edit→close, favourite off→on, show→hide, copy→done) | Outgoing icon turns −90° and scales .5 + fades; incoming turns in from +90°; label folds with `grid 1fr→0fr` | `fast-4` transform, `fast-3` opacity, `ease-standard` | cart Radmärkning (`.cm-lbl`, `.cm-ic`) |
| 2 | **Expand / collapse in place** (form under a row, details, filter group, "Visa detaljer") | `grid-template-rows 0fr→1fr` + content fade, `visibility` hidden when closed | `fast-4…medium-1`, `ease-standard` | eco-collapsible, cart row form, mini cart "Visa detaljer" |
| 3 | **Surface enters** (drawer, panel, modal, toast, sticky bar) | Slide/fade in from its own edge; exit shorter and faster | `medium-3` enter / `fast-3` exit, `decelerate-emphasized` / `accelerate-generic` | drawers, sticky add-to-cart, toasts |
| 4 | **Row added / removed** in a list (cart line, address, user) | Added: fade + 8 px up. Removed: fade, then collapse the row (`grid 1fr→0fr`) so neighbours close the gap instead of jumping | `fast-4` + `fast-4` | *proposal, not built* |
| 5 | **Confirm after action** (added to cart, saved, copied) | Button label/icon swaps once (pattern 1) for ~1.6 s, then back; toast does the sentence | `fast-3`, `ease-standard` | sticky bar "Tillagd ✓" |
| 6 | **Badge / counter changes** (cart count, filter count, number of results) | The number crossfades up/down 4 px (old out, new in), badge itself does not scale or bounce | `fast-3`, `ease-standard` | *proposal, not built* |
| 7 | **Selected state moves** (tabs, segment control, chosen variant, selected card frame) | A shared indicator slides to the new place, or the frame fades in/out; never both | `medium-1`, `ease-decelerate-generic` | pill segment control; tabs underline |
| 8 | **Content swaps behind a choice** (colour/variant changes image and text) | The image crossfades (new fades in over old); text swaps at once. No slide | `fast-4`…`medium-1`, `ease-standard` | PDP "Fler alternativ" (check) |
| 9 | **A value changes** (total, price after a code, stock text) | Colour tint of the value for ~600 ms (`surface-…` highlight fades out) or text crossfade. No count-up inside a transaction | `medium-2`, `ease-standard` | *proposal, not built* |
| 10 | **Hover / press / focus** on anything clickable | Colour, border or surface fade; press = 1 px or no movement; focus ring appears at once (no delay) | `fast-2…3`, `ease-standard` | every ECO component |
| 11 | **Empty and loading** (empty cart, search with no result, skeleton) | Slow fade of the message; skeleton as a still grey block with a very slow, soft opacity pulse, only after 400 ms of real waiting | `slow-3`, `ease-standard` | *proposal, not built* |
| 12 | **Scroll-to / jump to** (link to the size row, "Välj variant", back to top) | Smooth scroll that lands exactly under the sticky header, then a short highlight of the target (`border` or surface fades out) so the eye finds it | `medium-2`, `decelerate-generic` | `#varianter` scroll (highlight *proposal*) |
| 13 | **Progress and thresholds** (free-shipping bar, step progress, upload) | Bar width animates to the new value with `transform: scaleX`; text changes at the threshold with pattern 6 | `medium-2`, `ease-standard` | cart free-shipping bar (check) |
| 14 | **Validation message appears** | Message expands (pattern 2) and the field border colour fades; focus stays where it was | `fast-4` | *proposal, not built* |
| 15 | **Gallery / carousel** next-previous | Paged scroll-snap (native); controls slide in 16 px from their own side on hover | existing | gallery, carousels |

Campaign/landing techniques (reveal on scroll, text fill, count-up, parallax, countdown) are **not** here; they are in `eco-motion` ("Campaign motion") and follow its page-type table.

## How to run a scan

1. **Pick the scope.** One page, one flow (e.g. cart → checkout) or one component. Ask only if it is unclear which.
2. **Read, then list every state change.** In the markup and script look for what *changes without a transition*:
   - `hidden`, `display:none` ↔ block, `.is-open`, `.active`, `aria-expanded`, `aria-pressed`, `aria-selected`, `disabled`
   - `textContent`, `innerHTML`, `.src` set from script (swaps, counters, prices)
   - `appendChild`, `remove()`, list re-renders (rows appearing/vanishing)
   - `scrollIntoView`, `location.hash`, `window.scrollTo`
   - toasts, modals, drawers that appear with no easing
   Grep example: `grep -nE "hidden|classList\.(add|remove|toggle)|textContent|innerHTML|\.remove\(\)|scrollTo|scrollIntoView" page.html`.
3. **Check what already moves.** Existing transitions on the same elements, and `prefers-reduced-motion` coverage. Missing reduced-motion on an existing animation is a finding too.
4. **Match each jump to a catalogue row.** No matching row → it is a new pattern: mark it "new pattern" and say what it would need (a row here, a token). Do not invent silently (CLAUDE.md rule 7).
5. **Drop the weak ones.** Keep a proposal only if it meets one of: explains a change, shows where something went, confirms an action, or removes a visual jump. Aim for the **3–7 best**, not every possible one.
6. **Present as a numbered list** (see format). Wait for the user to pick. "Do all" counts as picking all. Apply nothing before that (CLAUDE.md proposals rule).
7. **Build the picked ones** per `eco-motion` and the manner above, reusing the existing code. Add the reduced-motion rule each time.
8. **Verify** (below), then **sweep**: add the new pattern to the catalogue row "Exists in", and note it in `CLAUDE.md` if it is a new reusable pattern.

### Proposal format

```
Motion scan: cart.html (7 found, 4 proposed)

1. Row removed → row collapses, neighbours close the gap  [pattern 4]
   Why: today the list jumps and the eye loses its place.
   Motion: fade + grid 1fr→0fr, fast-4 / ease-standard.  Risk: none.
2. Cart count in the header crossfades  [pattern 6]
   Why: confirms that the add worked even when the toast is gone.
   ...
Not proposed: shake on error (void), price roll (removed 2026-11).
Changes content/behaviour: none.   Pick e.g. "1 and 3".
```

Mark any item that changes behaviour, content or timing of an action (e.g. a delay before deletion so an undo is possible).

## Verification (before "done")

1. **Real interaction**, not only script: click, hover and Tab, then click again mid-animation. It must reverse cleanly with no stuck state.
2. **Three widths:** xs (~375), sm (~700), md+ (1024+). Mobile may use a simpler version or none; sm behaves as mobile.
3. **Reduced motion:** emulate `prefers-reduced-motion: reduce`; the final state appears at once and nothing is lost (focus, text, label for screen readers).
4. **Screen reader and keyboard:** state change announced the same as before (`aria-expanded`, `aria-live` unchanged); `aria-label` still correct after a label folds away; focus ring visible during the motion.
5. **Cost:** only `opacity`/`transform`/grid fractions animate; no layout thrash; no animation on first paint.
6. **Neighbours:** the same component on other pages (mini cart, drawers) still behaves.
7. **Say what was not tested.**

## Honesty list (never)

Shake, bounce, wobble, elastic, pulse on a CTA, looping attention-grabbers, fake loading, motion that repeats on every scroll, animated gradients behind text, hover effects that move the click target, delays before an action, sound.

## Open flags

- No physics or spring tokens exist beyond the swipe constants (`eco-motion`, "Swipe physics"); patterns 4, 6, 9 and 11 are proposals until the user has tried one and we add it to `eco-motion` or a shared file in `components/`.
- A shared helper (e.g. a `.fx-swap` class in `components/css/`) for pattern 1 is not built; the cart uses page-local CSS. Propose moving it when a second page needs it (skill + `CLAUDE.md` + docs page: ask first).
