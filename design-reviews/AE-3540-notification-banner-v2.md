# Design re-review: Notification Banner (AE-3540), round 2

**Reviewed:** [Storybook UAT, Components / Notification Banner](https://test-acceptance--67b6063b450f52d85d87d37f.chromatic.com/?path=/docs/components-notification-banner--docs) (Playground, All Variants, Mobile width, Tablet width), 2026-11-19  
**Previous review:** Jira comment of 2026-10-30. Ids below refer to it.  
**Figma:** [Notification / Banner, 13377:41997](https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=13377-41997); wrapped text: [24748:63988](https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=24748-63988)  
**Design decisions since round 1:** Q1 Background, left border and shadow fill the width. The page container keeps the content within 1200 px (the type area). Q2 Promotion has no close button. Q3 Closing is animated as on [eco-designsystem.com, Banner](https://eco-designsystem.com/eco-design-system/components/banner.html). Q5 Button roles follow Figma.  
**Method:** same as round 1. Computed styles at 375, 639, 640, 768, 769, 1024, 1232, 1281 and 1800 px. Real keyboard (Tab, Return) and mouse hover.

**Updated 2026-11-20:** Figma re-checked. F2, F3, F4, F5 and F7 are fixed.

Thanks for the work. 27 of 37 points are fixed and 5 are partly fixed. Two new points (N1, N2) were found, and one question (Q4) is for you.

## Status

| Id | Point | Status |
|---|---|---|
| C1 | Large follows viewport, not `version` | ✅ Fixed |
| C2 | Blank label on Warning Strong Large | ✅ Fixed |
| C3 | Filled status icons | ✅ Fixed |
| C4 | Close button 24 px, banner heights | ✅ Fixed |
| MA1 | Small body text on mobile | ✅ Fixed |
| MA2 | Top alignment when text wraps | ✅ Fixed |
| MA3 | Promotion title size | ✅ Fixed |
| MA4 | Promotion link case | ✅ Fixed |
| MA5 | Promotion mobile height | ✅ Fixed |
| MA6 | Promotion Light | ✅ Fixed |
| MA7 | Large spacing | ✅ Fixed |
| MA8 | Large actions configurable | 🟡 Partly, see below |
| MA9 | Storybook coverage | 🟡 Partly, see below |
| MA10 | Focus ring | ✅ Fixed |
| MI1 | Button label letter-spacing | ❌ Not fixed |
| MI2 | Close hover on Strong | ✅ Fixed |
| MI3 | Promotion dash bold | ✅ Fixed |
| MI4 | Tokens for shadow and motion | 🟡 Partly, see below |
| W1 | Focus after closing | 🟡 Confirm on a page |
| W2 | Large title is a heading | ✅ Fixed |
| W3 | Region and close names | ✅ Fixed |
| W4 | Live role | ✅ Fixed |
| W5 | Focus ring on blue surface | ✅ Solved in code (design note below) |
| W6, W7 | Warning icon and inverted hover contrast | ➖ Design system owners |
| W8 | Hover and focus states in Figma | ❌ Not drawn |
| Q1 | Full width | ✅ Fixed (page container constrains the content) |
| Q2 | Promotion close button | ✅ Removed |
| Q3 | Close animation | 🟡 Fade ✅, height collapse missing |
| Q4 | `--color-color-*` names | ❓ Question to developers |
| Q5 | Button roles vs ticket | ✅ Follow Figma (implementation matches) |
| F1 | Extra blue edge, Figma | ✅ Fixed |
| F2 | Tablet Large border token, Figma | ✅ Fixed (2026-11-20) |
| F3 | Second, smaller link, Figma | ✅ Fixed (2026-11-20) |
| F4 | Body link off-scale, Figma | ✅ Fixed (2026-11-20) |
| F5 | Promotion desktop link 18/16, Figma | ✅ Fixed (2026-11-20) |
| F6 | Icon layer names, Figma | ✅ Fixed |
| F7 | Promotion close button, Figma | ✅ Fixed (2026-11-20) |

## Still open: developers

### MA8 – Inline link in the body does not render (Major)
**Deviation:** `bodyLinkLabel` exists in Controls, but no link appears in the body text.  
**Should be:** an underlined inline link inside the body, as "adressboken" in Figma `23557:161876`.  
**Currently:** with `bodyLinkLabel: "adressboken"` the body renders plain text with no `<a>`. The rest of MA8 is done: buttons can be none, one or two, labels are editable, and links can be shown without buttons.  
**Suggestion:** render `bodyLinkLabel` as an Inline Link at the end of the body, or allow rich text in `body`.

### MA9 – Mobile and Tablet width stories render at desktop width (Minor)
**Deviation:** the new stories set `version`, which no longer changes layout after C1, and set no viewport.  
**Should be:** the stories show the banner at 375 and 768 px.  
**Currently:** `parameters.viewport.defaultViewport` is empty, so the banner renders at full canvas width. All Variants now shows 12 Small, 12 Large and 4 Promotion banners ✅.  
**Suggestion:** set `parameters.viewport.defaultViewport` (or `globals.viewport`) per story, and remove the `version` control, which has no effect.

### MI1 – Button labels have no letter-spacing (Minor, unchanged)
**Deviation:** Large banner button labels have no tracking.  
**Should be:** 0.56 px desktop, 0.48 px mobile (`label-sm`, Figma `23559:44268`).  
**Currently:** `letter-spacing: normal` at 640 and 1232 px. The `.btn .btn-val` rule sets no `letter-spacing`.  
**Suggestion:** add the tracking in the shared `.btn-val` rule.

### MI4 – Motion values are still literals (Minor)
**Deviation:** the shadow now uses `var(--shadow-elevation-b-20)` ✅, but the link transition uses Tailwind `duration-150` with a written-out easing.  
**Should be:** ECO duration and easing tokens (`eco-motion`).  
**Currently:** `.notification-banner__link { transition-duration: 0.15s; … }`.  
**Suggestion:** use the platform's ECO motion tokens.

### Q3 – Close animation has no height collapse (Major)
**Deviation:** the banner fades out, then disappears at once, so the content below jumps up.  
**Should be:** fade and height collapse together, `--ease-accelerate-generic` (`cubic-bezier(.36,.09,1,.58)`) over `--duration-fast-3` (150 ms). Under `prefers-reduced-motion` the banner is removed without animation. This is the reference on eco-designsystem.com (`notifications.js` and `notifications.css`, rule `.is-collapsing`).  
**Currently:** `transition: transform 0.15s, opacity 0.15s` with the right easing ✅. Height stays 48 px until removal, and an element below jumps 48 px at about 200 ms. No `prefers-reduced-motion` rule for the banner was found in the stylesheets.  
**Suggestion:** pin the height, then animate `height`, `padding` and `margin` to 0 together with `opacity`. Skip the animation under reduced motion.

### N1 – Large: space above links when there are no buttons is 16 px (Major, new)
**Deviation:** with buttons hidden and links shown, the footer top padding drops from 24 to 16 px.  
**Should be:** 24 px between body and action area at every breakpoint (Figma Action Group `pt-[24px]`, `eco-banner-notification`).  
**Currently:** `showSecondaryButton: false; showBlankButton: false; showLinks: true` gives `padding-top: 16px` on `.notification-banner-large__footer` at 1232 px.  
**Suggestion:** keep 24 px whatever the footer contains.

### N2 – Emphasis options ignore the size (Minor, new)
**Deviation:** options that do not exist for a size fall back to Weak without warning.  
**Should be:** status banners offer Strong, Weak and Weaker. Promotion offers Strong, Weak, Dark and Light.  
**Currently:** Small with `Dark` or `Light` renders Weak. Promotion with `Weaker` renders Weak.  
**Suggestion:** limit the options by `size` in the argTypes, and in the component's prop type.

### Q4 – Token names `--color-color-*` (question)
**Deviation:** the CSS variables are named `--color-color-*`, for example `--color-color-surface-information-default`. ECO names them `--color-*` (`--color-surface-information-default`).  
**Currently:** unchanged since round 1. The values match `tokens.json`.  
**Question:** is the doubled `color-` prefix intended (a platform naming convention), or a side effect of the token build? If it is not intended, the names should follow ECO, so tokens can be searched and shared under the same names in design and code.

### W1 – Focus after closing (to confirm on a page)
**Deviation:** none in Storybook. After Return on close, focus lands on the story's "Show again" button.  
**Should be:** focus moves to a logical nearby element on a real page.  
**Currently:** cannot tell if the component or the story moves the focus.  
**Suggestion:** confirm the component sets focus itself, not only the story.

## Still open: design

### W5 – Focus ring on blue (note)
**Currently:** the implementation draws the ring in `#E2F1FF` on Informational Strong, about 4.2:1 (calculated), so it passes. ECO still has only one focus token (`#455EFB`), about 1.0:1 on `#0066FF`. Design decides whether ECO gets an inverted focus token. Rings on the other Strong surfaces were not measured.

### W6, W7 – Contrast in ECO (unchanged, design system owners)
Warning icon 1.52–1.67:1 and inverted link hover about 3.5:1, as in round 1.

### W8 – No hover or focus states in Figma (unchanged)
The component set still has only Enabled frames.

## Figma file

No Figma points remain open.

### Fixed in Figma since round 2 (2026-11-20)
- **F2:** `23557:161877` now uses `border-information-weaker`, like the other breakpoints.
- **F3:** `23559:44268` now shows one link, 17/24.
- **F4:** "adressboken" in `23557:161877` uses the text style `body-md--underline`, bound to the body-md variables, so it renders 16/22 on tablet.
- **F5:** `13377:42264` link "Till kampanjen" is now 17/24.
- **F7:** `13377:42264`, `42200`, `42204` and `42208` have no close button.

## ✅ Matches design and ECO (round 2)

- **Small, all 12 combinations:** background, left border, filled icon and its colour, text, link, close icon colour, shadow `elevation-b-20`.
- **Small layout:** 48/40 px high, padding 12/16 and 8/16 px, switches exactly between 768 and 769 px.
- **Small type:** title 14/14, 0.56 px and 12/12, 0.48 px. Body 14/20, 0.36 px and 12/18, 0.24 px.
- **Small close button:** 24 x 24 px with 2 px padding.
- **Small wrapped text:** icon, text, link and close button are top-aligned, matching Figma `24748:63988`.
- **Large breakpoints, now by viewport:** bar 8/4/4 px, icon 48/40/24 px, padding 24, 16 and 12/12/16 px, gaps and footer indent 60/52/32 px. Switches at 639/640 and 768/769 px. `version` has no effect.
- **Large, all 12 colours:** filled status icons (leaf outline), heading colours, buttons (Warning Strong Blank is black), links, close icon.
- **Large type and headings:** `h2` by default with a `titleLevel` control. Title 20/24 and 18/22 px, body 17/24 and 16/22 px.
- **Large actions:** none, one or two buttons, editable labels, links on their own.
- **Promotion:** Strong, Weak, Dark and Light colours. Desktop 48 px with title 18/18, 0.18 px, bold dash, link "Till kampanjen" in sentence case 17/24 px, centred. Mobile 32 px, title 14/16, link 14/16, title left and link right. No close button.
- **Focus and hover:** ring 2 px solid, 2 px offset. Close hover on Strong is `rgba(255,255,255,0.2)`.
- **Accessibility props:** `closeLabel`, `regionLabel`, `liveRole` (renders `role="alert"`). Default region name includes the title.
- **Full width (Q1):** background, left border and shadow fill the width. The content is not constrained by the component; the page container does this (design decision).
- **Button roles (Q5):** Figma applies, not the ticket's "primary/secondary". The implementation matches: Secondary + Blank on Weak and Weaker, Primary Inverted + Blank on Strong, black Blank on Warning Strong.

## Not tested

- Focus ring colour on Weak, Weaker and the other Strong surfaces.
- `prefers-reduced-motion` behaviour: could not be emulated, only the stylesheets were searched.
- Tools brand, real pages, screen reader, 200% zoom.
- Figma `23559:44082` layer names (F6 was checked on `23559:44268`).
