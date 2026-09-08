---
name: prototype-guide
description: Use BEFORE and DURING work on any new prototype, page, product/service page, UI/UX flow, or functionality for Swedol — whether the task starts from a Figma prototype, a loose brainstorm/spec, or a one-line brief like "make a nice page"/"design X"/"build functionality for Y". This is the entry point that ties general web-design quality (hierarchy, layout, copy, interaction, micro-animation, structured critique) to the ECO Design System rules in CLAUDE.md and the component skills. Read this BEFORE choosing a starting point/template and BEFORE building individual components.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.
>
> This is the enriched version (2026-09-04), written in English at the user's request — every other skill in this repo is written in Swedish, so don't take that as a pattern to copy for new skills unless asked. The previous (Swedish) version is preserved unchanged for reference in [`SKILL.backup-2026-09-04.md`](./SKILL.backup-2026-09-04.md) in this same folder — it is not loaded as a skill, it's just kept for history.
>
> This version deliberately draws on five external design skills (web-design-guidelines / web-interface-guidelines, frontend-design, design-critique, landing-page-guide-v2, emil-design-eng) — but only the parts that are **stack-agnostic and don't conflict with ECO's fixed tokens**. Where a source pushes a specific aesthetic direction (maximalist gradients, non-Inter display fonts at 4–6rem, urgency/scarcity CTAs, React/ShadCN component code) it was deliberately left out — see Guardrails.

## Purpose

This skill is the **entry point** for all creative work in this repo — prototypes, pages, product/service pages, UI, UX flows, and functionality for Swedol, regardless of whether the assignment arrives as a finished Figma prototype, a loose brainstorm, or a written spec. It doesn't replace the component skills (`button`, `input`, `section`, etc.) — it **routes into them**: it provides the same kind of general design quality that dedicated skills for web-design review, distinctive visual direction, structured design critique, and micro-interaction polish usually provide — but **entirely expressed through ECO Design System's own tokens, components, and rules**, never invented freely.

**Core principle:** general design judgment is allowed to drive *composition* (what goes where, how much air, what draws the eye, what flow a user goes through, whether/when something should move) — but **never the values** (color, spacing, shadow, radius, typeface, easing, duration). Values always come from a skill or token that already exists in this repo. When general design advice conflicts with a stated ECO decision, ECO always wins (see Guardrails).

---

## Workflow

### 0. Understand the task — and which starting point you have

Is this a new page, a new section on an existing page, a new UI flow (e.g. a drawer/modal flow), or pure functionality (JS logic with no new visual surface)? That determines whether step 2 (template) is relevant.

Then determine **which of the three modes** the assignment starts in — it shapes the rest of step 0:

| Mode | Signs | Do this before moving to step 1 |
|---|---|---|
| **A. A Figma prototype exists** | You've been given a Figma link or finished screens to implement | Load the `figma-design-to-code` skill (mandatory before calling `get_design_context`). Read layout, content, and flow off Figma — but map **every** color/spacing/typography/shadow to the matching ECO token instead of copying Figma's raw values. If Figma diverges from ECO (a different blue, a different radius): flag the divergence to the user, don't guess which one wins. See "Figma is the design system" below — this is different from Guardrail 6's treatment of Mobbin-style inspiration. |
| **B. Loose brainstorm/idea** | The task is a sentence like "make a nice page for X" with no detailed spec | Run the mini-brief below before sketching anything. Unclear scope → ask, don't build on a guess (see Guardrail 5). |
| **C. Written spec/requirements** | You've been given text with requirements, user stories, or similar | Break the spec down into screens/sections/components before coding. If the spec describes a pattern that doesn't exist in ECO (e.g. "a filterable table with saved views") — flag it per step 3 before building a one-off solution. |

**Figma is the design system — not an outside inspiration source.** Unlike a Mobbin screenshot, a Figma prototype in this org *is* ECO — everything in it should, in principle, already trace back to a token or a component skill. So when you hit something in Figma that has no match in `CLAUDE.md` or any component skill (a color, a spacing value, an entire component pattern), the likely explanation isn't "this is a one-off style choice" — it's that ECO/CLAUDE.md simply hasn't caught up with Figma yet. Don't silently treat it as a free value (that would violate Guardrail 1), and don't silently treat it as disposable either. Instead, stop and ask the user directly which of these it is:
- **A permanent addition** — the token/component should be documented in `CLAUDE.md` and, if it's a component, given its own skill under `.claude/skills/` (per the existing rule on growing the skills index), so every future page can reuse it.
- **A snowflake** — a deliberate one-off for this specific screen that shouldn't become a reusable system pattern, and can be implemented inline this one time without a new token/skill.

Only proceed with implementation once you know which one it is — building it as if it were already an established token either overstates what exists in the system, or under-serves a genuinely new piece of ECO that other pages will need next.

**Mini-brief for mode B (brainstorm):** when the task is loosely worded, gather this by asking the user, not guessing:
- **Page type**: public/logged-out or logged-in ("My Pages")? Determines the template in step 2.
- **Purpose & audience**: what should the visitor be able to do or understand, and who are they (B2B buyer, workshop staff, administrator, etc.)?
- **Content that already exists**: product data, copy, images — never build on Lorem Ipsum or invented products/prices if real content exists or can be requested.
- **Scope/sections**: which blocks should be included? Use the structural checklist in step 3b as a prompt, not a requirement to fill every row.

**Inspiration references (e.g. Mobbin or similar pattern libraries):** these require a login and can't be fetched live by Claude. Instead, ask the user to share screenshots or links to specific examples when inspiration is needed. Analyze the references at the **pattern/structure level** — information architecture, flow, what content is prioritized, how one step leads to the next — never at the pixel level. Color, typeface, spacing, radius, and shadow in a reference are **never** copied; they're always replaced by ECO tokens. A reference is allowed to inspire *what* a surface does, never *how it looks*.

### 1. Ground yourself in what Swedol actually is

Before composing anything: what's the product/service, who's the audience (professional B2B customer, workshop, reseller, admin), and what's the page's one job? Build with the actual content — real product names, categories, and prices where they exist, otherwise clearly-marked placeholder content you ask about. A Swedol page should feel like a tool for a professional, not a consumer e-commerce storefront or a SaaS marketing pitch.

This repo's real page categories (see `index.html` sitemap) are **Templates**, **My Pages / user management**, **Comparison & marketing**, **Components & testing**, and **Email** — not a general e-commerce catalog. Most work here is account/self-service flows and comparison/marketing surfaces, not conversion-funnel landing pages. Keep that in mind before reaching for hard-sell patterns (see step 3b) — they fit the "Comparison & marketing" category far more often than "My Pages".

### 2. Choose the right starting point (for new pages)

**Never** copy an existing, finished page. Always start from:

| Page type | Starting point |
|---|---|
| Logged-out/public page | Copy of `template.html` (repo root) |
| Logged-in page ("My Pages") | Copy of `mypages/mypages-template.html` |

See `CLAUDE.md` → "Innan du bygger en ny sida" for the full rule and why.

### 3. Map out which components/patterns are needed

Go through the intended interface piece by piece and match every part against the skills index in `CLAUDE.md` (buttons → `button`, form fields → `input`/`select`/`checkbox`, notices → `notifications-guide`, links → `links-guide`, spacing → `spacing`, color → `colors`, shadow → `elevation`, animation → `motion`, etc.). Load and read every relevant skill before coding that part.

**A pattern is missing entirely** (it exists in Figma or the brief but has no skill)? Flag it to the user and ask before you either (a) build a one-off solution inline using existing tokens, or (b) create a new skill under `.claude/skills/` — per the rule in `CLAUDE.md`. Never guess a new component style into existence. This is the same permanent-vs-snowflake question from step 0's "Figma is the design system" note — ask it there the moment you spot the gap, don't wait until you're mid-build. This also includes micro-interaction patterns raised in step 6 below (e.g. a press-feedback scale on buttons) that aren't yet defined by a component skill — flag them the same way rather than inventing a transform value inline.

#### 3b. Structural checklist for product/service/marketing pages (a prompt, not a requirement)

When the task is a comparison, marketing, or campaign-style page (this repo's "Comparison & marketing" category) — or a product/service page more generally — use the list below to check nothing important was forgotten. Not every page needs all of them; match against the purpose from the step 0 mini-brief. This is adapted from a conversion-page framework, stripped of anything that isn't already an ECO pattern.

| Block | What it does | Built with |
|---|---|---|
| Header/logo | Placement and identity, always visible | Shared partial, already wired in the templates |
| Hero/value proposition | What the page is about, in under 2 seconds | `typography` scale (Display/Headline) |
| Primary CTA | One clear next step | `button` Primary — max one per surface |
| Supporting information/specs | Details a professional buyer actually needs | `typography` Body/Label, `section` |
| Trust signals | Reviews, customer logos, certifications — where relevant for B2B | `badge`, `role-tier-card`, or a plain section built from existing tokens |
| Related content/products | A natural continuation of the flow | `tile-link` or `action-link` |
| FAQ | Only if the content actually has recurring questions | `collapsible` |
| Secondary/closing CTA | A second chance further down a long page | `button`, never more dramatic than the primary one |
| Footer/contact | Shared partial | Already wired in the templates |

What this checklist deliberately does **not** carry over from its source material: oversized 4–6rem display type, gradient-mesh/glassmorphism backgrounds, urgency/scarcity CTAs (countdown timers, "limited spots"), animated counter effects, or a mandate that all of the above must appear on every page. Those are conversion-marketing defaults that conflict with ECO's typography scale, restrained motion tokens, and Swedol's professional B2B tone — see Guardrail 4.

### 4. Compose with general design quality — but our own building blocks

Use the checklist below (from classic web-design practice) as a lens, but solve every point with what already exists in the repo:

| Design principle | Solved with |
|---|---|
| Clear visual hierarchy (heading → support → CTA) | `typography` scale, not arbitrary font sizes |
| Consistent rhythm/air between blocks | `spacing` scale (space-0…space-120, space-sm/md/lg) and the `section` padding table |
| Contrast & readability | `colors` tokens (text/background/border pairs that are already contrast-safe) |
| Depth/layering where needed (cards, modals, drawers) | `elevation` skill — never a custom `box-shadow` value |
| Motion feels natural, not bouncy or too fast | `motion` skill's easing/duration tokens — see step 6 for *whether* something should animate at all |
| One clear primary call-to-action per view | `button` variants (Primary/Secondary/etc.), never more than one Primary per surface |
| Forms feel forgiving (states, error messages) | `input`/`select`/`checkbox` states + `inline-notification` for errors |
| Links signal the right weight | `links-guide` → Inline/Action/Tile |
| Statuses/labels are legible in one second | `badge` skill |
| The page feels whole, not a stack of loose blocks | `section`'s background rule (deliberately alternating white/grey) + Page Divider |
| The mobile experience isn't "squeezed desktop" | Mobile-first per the breakpoint table in `CLAUDE.md`, actually test at `xs`/`sm`/`md` |
| A distinct, deliberate composition — not a generic default | See the distinctiveness check below |

**Distinctiveness check (before coding the layout):** would you have landed on the exact same layout and emphasis for a completely different Swedol page with a different purpose? If yes — go back and let the actual content and purpose (steps 0–1) drive what's emphasized, in what order, and with how much air, within ECO's tokens. Distinctiveness comes from composition (what's emphasized, ordering, rhythm), never from inventing new colors/typefaces/shadows — those stay locked to ECO.

### 5. Copy is design content, not decoration

Words earn their place in a design for one reason: making it easier to understand and use. Bring the same intentionality to copy that you bring to spacing and color — before writing anything, ask what the page needs to say and how to say it in a way that helps someone navigate.

- **Write from the user's perspective.** Name things the way users understand them, not the way the system is built internally — a user manages *orders*, not *webhook payloads*.
- **Use active voice by default.** A CTA states exactly what happens: "Spara ändringar", not "Skicka". An action keeps its name through the whole flow — a button labeled "Publicera" produces a toast that says "Publicerat", not "Klart" or "Sparat".
- **Errors and empty states speak in the interface's voice**, not a person's — explain what happened and how to fix it, without apologizing or being vague. An empty state is an invitation to act, not just a description of absence.
- **Second person, not first person** ("din order", not "min order").
- This applies in Swedish, matching how existing Swedol pages already write: professional B2B tone, not marketing-department superlatives (already stated in step 9, repeated here because copy is part of composition, not an afterthought).

### 6. Micro-interaction & motion — decide *whether* and *why* before *how*

The `motion` skill gives you the allowed easing curves and duration tokens (`motion-ease-*`, `motion-duration-fast/medium/slow-*`). Before reaching for them, decide whether the animation should exist at all:

| How often does the user see this interaction? | Decision |
|---|---|
| Very often (keyboard shortcuts, a toggle used dozens of times/day) | No animation |
| Often (hover, list navigation) | Remove it or keep it extremely short (`motion-duration-fast-1`/`fast-2`) |
| Occasional, once or twice per session (modals, drawers, toasts) | Standard animation from `motion` |
| Rare/first-time (onboarding, confirmations) | Can allow slightly more noticeable motion — still within `motion`'s tokens, still the slow tier at most |

Every animation needs an answer to "why does this animate?" — spatial consistency (a drawer enters and exits from the same direction), state indication, preventing an abrupt jump, or feedback on a press. "It looks cool" isn't a reason if the user sees it often.

**Which token tier, concretely:** this repo's `motion` skill already ties duration to on-screen distance (short/medium/long → fast/medium/slow) and easing to interaction type (`motion-ease-standard` for hover, `motion-ease-decelerate-emphasized` for things entering from off-screen, `motion-ease-accelerate-generic` for things leaving). Use that mapping — do not reach for a duration or curve outside those tables just because a source pattern suggests a specific millisecond value (e.g. "180ms feels faster than 400ms"); pick the nearest existing `motion` token in the right tier instead of inventing a new number.

Practical rules that apply regardless of which duration/easing token is chosen:
- **Prefer CSS transitions over keyframes** for UI that can be triggered quickly/repeatedly (a toast that can appear multiple times, a toggle) — transitions can be interrupted and retargeted smoothly; keyframes restart from zero.
- **Never animate a keyboard-triggered action.**
- **Respect `prefers-reduced-motion`** — color/opacity transitions that aid comprehension may stay; movement/position animation should be removed.
- **Popovers anchored to a trigger should scale from that trigger, not from center** (`transform-origin` matching the trigger's position) — the exception is modals, which stay centered because they aren't anchored to a specific trigger. This is a placement decision, not a new value, and doesn't conflict with any existing token.
- **Don't invent a press-feedback scale value** (e.g. a button `:active` scale-down) even though it's a well-known polish pattern — no component skill currently defines one. If you notice buttons/cards feel unresponsive on press, flag it per step 3 as a possible gap in the `button`/`elevation` skills instead of adding an inline transform.

### 7. Functionality (JS)

Keep interaction logic vanilla JS, consistent with how existing pages already solve similar things (open/close patterns, form validation, state handling) — search the repo for a similar pattern before inventing a new one (see quality rule 2 in `CLAUDE.md`).

### 8. Implementation checklist (stack-agnostic)

Run through this list for new interactive surfaces — it complements CLAUDE.md's breakpoint checklist, it doesn't replace it:

**Accessibility**
- Icon-only buttons have `aria-label`; decorative icons have `aria-hidden="true"`
- Every form field has an associated `<label>` (or `aria-label`) — clickable label (`for`/wrapping control)
- `<button>` for actions, `<a>` for navigation — never a `<div>`/`<span>` with a click handler
- Visible focus state on every interactive element (`:focus-visible`), never `outline: none` without a replacement
- Async updates (validation, toasts) are announced with `aria-live="polite"`
- Heading hierarchy `<h1>`–`<h6>` in order, one `<h1>` per page

**Forms**
- Correct `type`/`inputmode` (email, tel, url, number) and meaningful `autocomplete`
- Never block paste
- Errors show inline next to the field, with focus moved to the first error on submit
- Submit button stays clickable until the request starts; a spinner shows during the request
- Warn before navigating away from unsaved changes

**Content & empty states**
- Text containers handle long content (`truncate`, `line-clamp`, `break-words`); flex children with text need `min-w-0` for truncation to actually work
- Never render broken UI for empty lists/strings — build an actual empty state
- Account for short, average, and very long user-generated/product content

**Touch & interaction**
- `touch-action: manipulation` on interactive surfaces (avoids the double-tap-zoom delay)
- `overscroll-behavior: contain` in modals/drawers/sheets
- Gestures (drag/swipe) always have a tap/click and keyboard alternative unless purely decorative

**Images & performance**
- `<img>` has explicit `width`/`height` (avoids layout shift)
- Below-the-fold images: `loading="lazy"`
- Large lists (50+ rows): consider virtualization or `content-visibility: auto`

**Locale**
- Dates/times and numbers/currency use `Intl.DateTimeFormat('sv-SE')`/`Intl.NumberFormat('sv-SE')` rather than hand-formatted strings — this repo's audience is Swedish, so don't hardcode a different locale either.

This is a supplement, not a full replacement for CLAUDE.md's breakpoint checklist — run both.

### 9. Structured self-critique before delivery

Before calling anything done, review your own result the way a design critic would. Answer each point concretely, not just yes/no — and rate severity where something falls short, so priority is clear:

**First impression (2 seconds)**
- What draws the eye first — is that the right thing?
- Is the page's purpose immediately clear?

**Usability**
- Can the user actually accomplish what the surface is for, without unnecessary steps?
- Is the next click obvious?

**Visual hierarchy**
- Is there a clear reading order?
- Is whitespace used to group things, not just to fill space?

**Consistency**
- Does the surface follow ECO tokens throughout, or did a one-off solution sneak in?
- Do similar elements behave the same way (same button type for the same kind of action, etc.)?

**Accessibility**
- Contrast, touch target size, readable text size — see the checklist in step 8.

**Copy**
- Short, concrete, in line with how existing Swedol pages write (Swedish, professional B2B tone — not marketing-department superlatives or invented content) — see step 5.

| Finding | Severity | Fix |
|---|---|---|
| [what you found] | 🔴 Critical / 🟡 Moderate / 🟢 Minor | [what you'll do about it] |

Anything 🔴 or 🟡 gets fixed before delivery, not just noted as "could be improved."

### 10. Run the quality checklist in CLAUDE.md

The five points under "Kvalitetskontroll — innan leverans" in `CLAUDE.md` (breakpoint check with actual `getComputedStyle` values, reusing tokens/patterns, CSS specificity when nesting, spacing duplication, interaction at every breakpoint) are mandatory and come **after** the design and critique pass above, not instead of it.

---

## Guardrails

1. **Never free values.** No hex color, px number for spacing/shadow, or custom easing curve that doesn't already exist as a token/skill — even if it "looks better," and even if it came from a Figma file or an inspiration reference. If no token fits: flag and ask, don't build silently.
2. **Never copy a finished page as a template.** See step 2.
3. **Never more than one new skill at a time without checking in.** This skill existing doesn't change the `CLAUDE.md` rule about asking before `.claude/skills/` grows.
4. **General "best practice" never beats a stated ECO design decision.** If a general web-design rule (e.g. "CTAs should be orange for attention," or a maximalist landing-page trend — oversized display type, gradient meshes, urgency/scarcity CTAs) collides with how the `button` skill defines variants, the `button` skill wins.
5. **Ask when scope is unclear.** "Make a nice landing page" with no further detail → ask which page type (public/logged-in), what purpose/audience, and which sections should be included, before building. This also applies when an inspiration reference (Figma or Mobbin-like) is ambiguous about what's structure and what's style.
6. **Inspiration references give structure, never style.** Color, typeface, spacing, radius, shadow, and easing in a Figma file or external reference are always replaced by ECO tokens — only flow/information architecture/content prioritization may inspire composition.
7. **A well-known polish pattern is not a license to invent a value.** Press-feedback scales, stagger timings, or any other micro-interaction detail from outside sources gets flagged as a possible gap per step 3, not added inline just because it's good practice elsewhere.
