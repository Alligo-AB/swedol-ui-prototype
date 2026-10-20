---
name: eco-motion
description: Use when animating or transitioning something — easing curves (decelerate/accelerate/standard) and duration tokens (fast/medium/slow) per the ECO Design System. Also scroll effects on campaign pages (scroll-reveal, text fill, count-up, parallax, smooth scroll, grain) as user-picked proposals with conditions.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Motion – Easing & Duration (ECO Design System)

Animation conveys functionality, intent, and relationships. Use these tokens to create coherent, realistic transitions.

> These principles apply as guidelines. They can vary at the component level but should always be followed as closely as possible to ensure consistency.

### Three basic concepts

| Concept | Explanation |
|---|---|
| **Timing** | How long an action takes. Always choose it deliberately. |
| **Spacing** | The gap between frames in a moving object. Varied spacing produces smooth transitions. |
| **Ease** | The combination of timing and spacing. Controls how a motion flows – objects should accelerate and decelerate smoothly. |

---

### Easing tokens

Choose easing based on how a transition moves relative to the screen:

- **Small change, short distance** → fast fade
- **Medium change, medium distance** → medium fade
- **Large change, long distance** → slow fade

| Token | Curve | Type | Description | Used for |
|---|---|---|---|---|
| `ease-decelerate-generic` | `cubic-bezier(.16,.38,.58,1)` | Ease Out – Generic | Starts fast, brakes gradually. Less emphasized variant. | onClick, enter selected states. Form elements, Tabs, Toggled buttons, Tooltip. |
| `ease-decelerate-emphasized` | `cubic-bezier(.16,0,.16,1)` | Ease Out – Emphasized ★ | More pronounced braking. Default choice for bringing elements in from off-screen. | Drawers (all variants), Main/Account menu, Product menu, Notifications. |
| `ease-accelerate-generic` | `cubic-bezier(.36,.09,1,.58)` | Ease In – Generic | Starts slow, speeds up. Like an object falling. | Removing elements from the screen (exit animations). |
| `ease-standard` | `cubic-bezier(.35,0,.35,1)` | Ease InOut – Standard | Starts slow, speeds up, brakes. All-round easing. | Hover states (the majority). Button, Product Card, Text Link, Breadcrumb, Collapsible, Overflow menu, Form elements, Tab bar, Drawer Link. |

> Doc pages with `data-subnav="tabs"` (the Tooltip draft) jump to a section with `ease-decelerate-generic` and durations one step faster than the default (fast-3 / fast-4 / medium-2 / slow-1 by distance); other doc pages keep `ease-decelerate-emphasized`. Scroll animations must scroll with `behavior: 'instant'` per frame, otherwise `html { scroll-behavior: smooth }` stretches them.

> ★ `ease-decelerate-emphasized` is the first choice for enter animations. `ease-decelerate-generic` is used when a lighter emphasis is wanted.

```css
/* Example: Element sliding in from off-screen (drawer) */
.drawer {
  transition: transform var(--duration-medium-3) var(--ease-decelerate-emphasized);
}

/* Example: Hover state on a button */
.btn {
  transition: background-color var(--duration-fast-4) var(--ease-standard);
}

/* Example: Element leaving the screen */
.toast-exit {
  transition: opacity var(--duration-fast-3) var(--ease-accelerate-generic);
}
```

---

### Duration tokens

Duration is split into three groups — **Fast**, **Medium**, and **Slow** — with four steps each.

> Use tokens per the distance and fade principles below. For vertical movement, any duration within the right group can be used.

#### Fast (50–200ms) – Small, quick interactions

| Token | Value | Used for |
|---|---|---|
| `duration-fast-1` | 50ms | Micro-interactions, immediate feedback |
| `duration-fast-2` | 100ms | Fast hover transitions, focus indicators |
| `duration-fast-3` | 150ms | Standard hover, fast exit animations |
| `duration-fast-4` | 200ms | Light enter animations, short state changes |

#### Medium (250–400ms) – Medium-sized interactions

| Token | Value | Used for |
|---|---|---|
| `duration-medium-1` | 250ms | Dropdowns, tooltips, shorter slide-ins |
| `duration-medium-2` | 300ms | Standard for most UI transitions |
| `duration-medium-3` | 350ms | Drawers, panels, medium-sized surfaces |
| `duration-medium-4` | 400ms | Complex component transitions |

#### Slow (450–600ms) – Large, heavier motion

| Token | Value | Used for |
|---|---|---|
| `duration-slow-1` | 450ms | Large enter animations, page transitions |
| `duration-slow-2` | 500ms | Hero elements, full-width animations |
| `duration-slow-3` | 550ms | Empty states, loading phases |
| `duration-slow-4` | 600ms | The longest allowed duration – use sparingly |

---

### Distances – distance drives duration

The distance of the motion determines which duration group to use.

| Distance | Share of viewport | Duration group | Description |
|---|---|---|---|
| **Short** | ≤ 25% of the view | Fast | Covers a small part of the screen. Use fast tokens. |
| **Medium** | 26–50% of the view | Medium | Half the screen. Use medium tokens. |
| **Long** | 51–100% of the view | Slow | All or most of the screen. Use slow tokens. |

---

### Fades – opacity and color transitions

Fades are a refined way to transition between colors and/or opacity levels.

| Type | Duration group | Description | Components |
|---|---|---|---|
| **Fast fade** | Fast | Standard small-scale interactions. | Buttons, list items, form elements |
| **Medium fade** | Medium | Medium-sized interactions. Elements lifted off the surface. | Cards, elevated surfaces |
| **Slow fade** | Slow | Important state changes. | Empty states, loading phases |

---

### Combination rule: distance + fade

| Scenario | Distance | Fade | Easing |
|---|---|---|---|
| Button hover | Short | Fast fade | `ease-standard` |
| Dropdown opens | Short–Medium | Fast–Medium fade | `ease-decelerate-generic` (Select menu: 8px move + fade, `duration-medium-1`) |
| Drawer slides in | Medium–Long | Medium fade | `ease-decelerate-emphasized` |
| Modal appears | Medium | Medium fade | `ease-decelerate-emphasized` |
| Element disappears | Any | Fast fade | `ease-accelerate-generic` (Select menu closing: fade + 8px move, `duration-fast-2`) |
| Banner / Inline notification closes (×) | Short | Fast fade (`fast-3`) + height collapse | `ease-accelerate-generic` |
| Loading/empty state | — | Slow fade | `ease-standard` |

```css
/* CSS custom properties for the whole project */
:root {
  /* Easing */
  --ease-decelerate-generic:    cubic-bezier(.16,.38,.58,1);
  --ease-decelerate-emphasized: cubic-bezier(.16,0,.16,1);
  --ease-accelerate-generic:    cubic-bezier(.36,.09,1,.58);
  --ease-standard:              cubic-bezier(.35,0,.35,1);

  /* Duration */
  --duration-fast-1:   50ms;
  --duration-fast-2:   100ms;
  --duration-fast-3:   150ms;
  --duration-fast-4:   200ms;
  --duration-medium-1: 250ms;
  --duration-medium-2: 300ms;
  --duration-medium-3: 350ms;
  --duration-medium-4: 400ms;
  --duration-slow-1:   450ms;
  --duration-slow-2:   500ms;
  --duration-slow-3:   550ms;
  --duration-slow-4:   600ms;
}
```

---


### Campaign motion (scroll effects, proposals only)

Scroll-reveal, text fill on scroll (grey → black), count-up numbers, timers and countdowns, dark/light section transitions, parallax, smooth scroll (Lenis) and grain are allowed, but **only as a proposal the user picks** (see `CLAUDE.md`, motion table by page type: campaign/landing pages yes, regular public pages only on request, My Pages/forms/tables no). They must serve a purpose (focus on the CTA, conversion), never decoration alone.

Conditions, every time:

1. **Tokens only.** Easing and duration from this file. Reveal = fade + short move (≤ 25% of the view): `ease-decelerate-emphasized`, `duration-medium-3` to `duration-slow-2`. No custom curves or durations.
2. **`prefers-reduced-motion: reduce`** → effect off, content visible at once, no movement.
3. **Breakpoints.** Check xs (~375px), sm (~700px) and md+ (1024px+) separately. xs/sm may use a simpler version or none. Parallax is desktop-first and off on xs/sm.
4. **Never hide content or block action.** Content must be readable and CTAs/forms clickable without waiting for an animation. Without JS the content is visible.
5. **Play once** by default (`IntersectionObserver`, unobserve after it runs). Repeating on scroll up needs the user's okay.
6. **Count-up numbers** end on the real number, with the final value in the HTML for screen readers.
7. **Smooth scroll (Lenis)** is a proposal like the rest, with extra conditions: off under `prefers-reduced-motion` and on touch/xs/sm unless tested; keyboard scrolling, anchor links, Tab focus into view and find-in-page must still work; never on My Pages, forms or tables; the library is an extra dependency, so say so in the proposal and ask before adding it.
8. **Grain** is a proposal like the rest, with extra conditions: a static, low-opacity noise layer (`pointer-events: none`, no animation, never over text-heavy areas), text contrast must still pass on top of it, and there is no token for it yet, so ask for the opacity value before choosing one (rule 7 in Quality control).
9. **Timers and countdowns** (to a campaign start or end, or an elapsed-time counter) are proposals like the rest, with extra conditions: the date/time is **real** and comes from one visible source (never invented, never reset on reload to fake urgency); show the time zone; at zero the page changes state (e.g. "Campaign started", CTA swaps) instead of showing 00:00:00 or negative numbers; the full date is also given as plain text; screen readers get the date, not a ticking value (`aria-live` off or `role="timer"` only with `aria-live="off"`); numbers use tabular figures so the layout does not jump; reduced motion = no flip/slide animation, the value still updates.
10. **Still void:** glassmorphism, and made-up scarcity ("only 3 left" when it is not true). 3D scenes, pinned scroll scenes and other extra libraries: ask first.

#### Campaign techniques catalog (approved by the user 2026-10-17, deep-dived rows 5, 8, 9, 14)

A starting menu for campaign/landing pages. Claude picks the ones that fit, proposes them with a reason, and the user chooses. The list is open: Claude adds ideas that are not here. Colors, typefaces, components and tokens stay ECO (Swedol / Tools); only the technique is new.

| Technique | Good for | Notes |
|---|---|---|
| Scroll-reveal (fade + short move) | Focus, pacing of long pages | Rules 1–5 above |
| Text fill on scroll (grey → black) | Key message, headline | Two-tone headline in ECO text colors |
| Count-up numbers | Proof (customers, years, volume) | Rule 6 |
| Countdown / timer | Campaign start or end | Rule 9, real dates only |
| Sticky CTA (bar or button appears after the hero) | Conversion on long pages | One CTA, `eco-button` Primary. Shows only after the hero, hides while the page's own CTA is in view, never covers content, the cookie banner or the chat widget (reserve the space), respect the iOS bottom bar. Risk: covers content on small screens, feels pushy if always on |
| Scroll progress indicator | Long story pages | Thin line from tokens, decorative (`aria-hidden`) |
| Dark ↔ light section transitions | Rhythm, emphasis | ECO surface colors, gradient only between existing tokens |
| Parallax (image/background, subtle) | Hero or full-width image | Use sparingly (once per page). Desktop only, small offset, off on xs/sm and reduced motion. Risk: nausea for some users, heavy on mobile, larger images (load time), cropped motifs or horizontal scroll if built wrong, rarely a measurable conversion gain |
| Hero image/video with text overlay | First impression | Text sits on an ECO surface/overlay layer so contrast passes (test it, not just look); video muted, paused under reduced motion, static poster image fallback; separate crop for xs/sm/md+. Risk: text contrast over moving images, heavy video hurts load time and mobile data, autoplay may be blocked |
| Social proof strip (logos, rating, short quote) | Trust near the CTA | Real, approved content only |
| Product/offer cards with staggered reveal | Offer overview | Stagger from `duration-fast-*` steps, max a handful of items |
| Hover/press feedback on cards and tiles | Clickability | `ease-standard`, fast durations (existing rules) |
| Early-access / notify-me form before launch | Campaign before start | `eco-input` + `eco-button`, clear consent text |
| Exit or return prompt (a banner, not a blocking popup) | Recover leaving visitors. **Only on request, never proposed by default** | `eco-banner-notification` or `eco-inline-notification`; never a modal that traps the user. Once per visit, one-click close, keyboard reachable, never over the cookie banner or a form. Risk: exit intent only works on desktop, irritating in B2B, search engines penalise intrusive popups on mobile |

Not on the list on purpose: dark patterns (fake scarcity, hidden unsubscribe, forced opt-ins, blocking popups), autoplay with sound, and anything that makes content unreadable without JavaScript.

Reference studied 2026-10-17: unitedcarriers.com (campaign site: scroll-driven hero, grey → black headline fill, count-up, dark/light gradients). Used for ideas about structure only; not for style or libraries.

---

### Choosing motion in docs

Component docs pages that animate get a live **Motion** section (easing, duration, collapse, recommended default marked `*`, warnings for choices that clash with these rules). See `eco-doc-page`, "Motion section".
