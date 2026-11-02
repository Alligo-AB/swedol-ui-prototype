# Design review: Notification Banner (AE-3540)

**Reviewed:** [Storybook UAT, Components / Notification Banner](https://test-acceptance--67b6063b450f52d85d87d37f.chromatic.com/?path=/docs/components-notification-banner--docs) (stories Playground and All Variants)  
**Figma:** [Notification / Banner, node 13377:41997](https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=13377-41997). The component set holds all breakpoints: XLarge-Large-Medium, Small and XSmall.  
**Prototype:** not run. Behaviour references come from the ECO skills.  
**Source of truth:** Figma for visuals, ECO Design System for tokens and rules, Jira ticket for scope.  
**Method:** computed styles measured in the story iframe at exact widths: 320, 375, 639, 640, 700, 768, 769, 1023, 1024, 1232, 1280, 1281 and 1800 px. Hover, Tab and Return were tested with real mouse and keyboard input. WCAG 2.2 AA, as the ticket asks.

Every deviation below should be fixed. The levels set the order of the work.

## 🔴 Critical

### C1 – Large banner layout follows the `version` prop, not the viewport
**Deviation:** Large gets its bar, icon and padding from `version`, while its type follows the viewport, so the two can disagree and the component is not responsive by itself.  
**Should be:** Figma Large frames by breakpoint, switching between 768 and 769 px and between 639 and 640 px. The ticket's Definition of Done says "Responsive behaviour follows the approved designs".  
**Currently:**

| `version` @ viewport | Bar | Icon | Padding | Title |
|---|---|---|---|---|
| Desktop @ 768 px | 8 px | 48 px | 24 px | 18 px |
| Mobile @ 1232 px | 4 px | 24 px | 12/12/16 px | 20 px |
| Tablet @ 1232 px | 4 px | 40 px | 16 px | 20 px |
| Tablet @ 639 px | 4 px | 40 px | 16 px | 18 px |

**Suggestion:** drive `.notification-banner-large` with the same responsive classes as Small and remove `version`. On Small, `version` already has no effect on layout, so the control is misleading there too.

### C2 – Blank button label is white on Warning Strong Large (WCAG 1.4.3)
**Deviation:** "VÄLJ TILLBEHÖR" uses Blank Inverted on the yellow surface and is close to unreadable.  
**Should be:** black label, `text-action-primary` (Figma `23559:44082`, standard Blank on Warning).  
**Currently:** `rgb(255,255,255)` on `#FAC000`, contrast 1.67:1 (4.5:1 required).  
**Suggestion:** use `btn-blank` instead of `btn-blank-inverted` when status is Warning and emphasis is Strong. Keep Blank Inverted on the other Strong statuses (Figma `23559:44268`). Measured here: Informational, Success and Error Strong correctly use it.

### C3 – Status icons render as outline instead of filled
**Deviation:** `info`, `check_circle`, `warning` and `error` show as outlines on every Small banner and every Large banner except the default leaf.  
**Should be:** `Material/Fill/300/*`, i.e. `'FILL' 1` (Figma `13377:42164`, `23433:265908`, `23559:44268`, `23559:44082`). The Large Informational leaf stays outline, as drawn (`23557:161876`).  
**Currently:** `font-variation-settings: "FILL" 0, "GRAD" 0, "wght" 300`, also on elements with class `material-symbols-filled`.  
**Suggestion:** make `.material-symbols-filled` set `'FILL' 1` with enough specificity, and apply it to Large status icons. Confirm a custom `icon` still renders Outline.

### C4 – Close button is 32 px instead of 24 px, which makes banners too tall
**Deviation:** the close button uses `btn-xs` with 5 px padding and a 1 px border, and this sets the height of Small and Promotion banners.  
**Should be:** 24 px button with 2 px padding and a 20 px icon (Figma button base `p-[2px]`, ECO `.icon-btn--close`). The story's own description also says 1200 x 48 and 768 x 40.  
**Currently:**

| Banner | Should be | Currently |
|---|---|---|
| Small, 769 px and up | 48 px | 56 px |
| Small, up to 768 px | 40 px | 48 px |
| Promotion, 769 px and up | 48 px | 56 px |
| Close button, all banners | 24 x 24 px | 32 x 32 px |

**Suggestion:** add a close variant of the Blank button with `padding: 2px` and no reserved border space, and use it in all three banner types. It still meets WCAG 2.5.8 at 24 x 24 px.

## 🟠 Major

### MA1 – Small body text does not scale down on mobile
**Deviation:** supporting text stays at desktop size up to 768 px, so it is larger than its own 12 px title.  
**Should be:** 12/18 px, 0.24 px letter-spacing (Figma `13377:42182`, ECO `eco-banner-notification`).  
**Currently:** 14/20 px, 0.36 px at every width. The story description says no body class matches 12 px.  
**Suggestion:** add a scoped mobile rule or a shared `body-xs` style instead of accepting the deviation. Raise it with design if a new shared style is preferred.

### MA2 – Small banner content is centred when text wraps
**Deviation:** icon, link and close button drift to the vertical middle of a multi-line banner.  
**Should be:** all top-aligned, `items-start` (Figma Main Content), with 2 px extra top on text and link.  
**Currently:** with long text at 375 px, in a banner 116 px high: icon top 46 px, link top 48 px, close top 42 px, text top 8 px. Class `items-center`.  
**Suggestion:** use `items-start` on `.notification-banner` and add `pt-[2px]` to text and link.

### MA3 – Promotion title is the wrong size on desktop
**Deviation:** the title is smaller, with wider tracking, than the design.  
**Should be:** `label-md` desktop 18/18 px, 0.18 px (Figma `13377:42264`, ECO `eco-banner-notification`).  
**Currently:** 16/16 px, 0.48 px at 769 px and up.  
**Suggestion:** check the `.label-md` definition or the responsive scope around it, since the mobile value is correct. Check other uses of `label-md` for the same error.

### MA4 – Promotion link is forced to uppercase
**Deviation:** the link inherits `text-transform: uppercase` from the parent paragraph. The default text "LOGGA UT" hides this.  
**Should be:** "Till kampanjen", in the case the author writes (Figma `13377:42264`, `13377:42214`, ECO: links never force uppercase).  
**Currently:** `linkLabel: "Till kampanjen"` renders "TILL KAMPANJEN" at every measured width.  
**Suggestion:** move `uppercase` from the `<p>` to the title span. Change the Promotion story's default link to "Till kampanjen".

### MA5 – Promotion mobile is 36 px high instead of 32 px
**Deviation:** line heights differ from the design, which adds 4 px.  
**Suggestion:** set the link and title line height to 16 px on mobile.

| Element, up to 768 px | Should be (Figma `13377:42214`) | Currently |
|---|---|---|
| Banner height | 32 px | 36 px |
| Title line height | 16 px | 14 px |
| Link line height | 16 px | 20 px |

### MA6 – Promotion emphasis Light is missing
**Deviation:** there is no Light option. `emphasis: Light` falls back to Weak and shows the pale accent colour, and white is only reached through `Weaker`, a name Figma does not use for Promotion.  
**Should be:** Strong, Weak, Dark and Light (Figma `13377:42204`, white surface).  
**Currently:** control options are Strong, Weak, Weaker and Dark. `Light` renders `rgb(244,246,204)`.  
**Suggestion:** add `Light` for Promotion, and limit the emphasis options by size so Dark and Light are not offered on status banners.

### MA7 – Large banner spacing differs from the design
**Deviation:** four spaces in Large differ from Figma.  
**Suggestion:** apply the values in the table. The gaps are `gap-2`, `gap-3` and `pt-2` in the Large template.

| Space | Should be (Figma `23557:161876/7/8`) | Currently |
|---|---|---|
| Title to body, 769 px and up | 12 px | 8 px |
| Icon to text, up to 639 px | 8 px | 12 px |
| Text block top offset | 2 px | 0 px |
| Buttons to text link | 0 px | 8 px |

### MA8 – Large actions cannot be configured
**Deviation:** button labels are fixed and the buttons cannot be hidden, and only one link is possible. The body cannot contain an inline link.  
**Should be:** the ticket says "Content and action labels must be configurable". Figma has an optional action section and an underlined link in the body ("adressboken").  
**Currently:** Controls offer `title`, `showTitle`, `body`, `linkLabel`, `showLink`, `closeButton` and `icon`. "GÅ TILL VARUKORGEN" and "VÄLJ TILLBEHÖR" always render.  
**Suggestion:** add props for primary and secondary labels, show/hide for each and the action section, and allow several links and rich text in the body.

### MA9 – Storybook coverage is incomplete
**Deviation:** All Variants shows only Small, and Large and Promotion need manual changes in Playground.  
**Should be:** the ticket requires stories or controls for all statuses, emphasis and Promotion variants, and supported responsive configurations.  
**Currently:** 12 Small combinations. No Large, no Promotion and no mobile view.  
**Suggestion:** add Large and Promotion to All Variants, plus viewport stories for 375 and 768 px.

### MA10 – Focus ring does not follow ECO (WCAG 1.4.11)
**Deviation:** the focus ring uses a browser-style rounded outline in another colour.  
**Should be:** `outline: 2px solid var(--color-border-focus); outline-offset: 2px` (`eco-button`).  
**Currently:** `rgb(229,151,0) auto 1px`, offset 0. Contrast is 2.0:1 on Informational Strong and 1.44:1 on Warning Strong (calculated from the measured colours, 3:1 required).  
**Suggestion:** apply the ECO focus rule. Note W5 first: the ECO token also fails on the blue surface, so that one case needs a decision from design.

## 🟢 Minor

### MI1 – Button labels have no letter-spacing
**Deviation:** `.btn-val` has no tracking. The likely source is the shared Button, so other components may have the same error.  
**Should be:** 0.56 px desktop, 0.48 px mobile (`label-sm`, Figma button labels).  
**Currently:** `letter-spacing: normal` at all widths.  
**Suggestion:** add the tracking in the shared `.btn-val` rule.

### MI2 – Close button hover is too weak on Strong
**Deviation:** the hover uses a dark tint on a solid colour, so it barely shows.  
**Should be:** `var(--color-surface-opacity-white-20)` (ECO `.icon-btn--close-inverted`).  
**Currently:** `rgba(0,0,0,0.05)`, measured on Informational Strong.  
**Suggestion:** use the inverted close variant where Figma has white close icons.

### MI3 – Promotion dash is not bold
**Deviation:** the dash between title and link is regular weight.  
**Should be:** part of the bold title "Title -" (Figma `13377:42264`).  
**Currently:** weight 400, 16/24 px, in its own span.  
**Suggestion:** render the dash in the title span on desktop.

### MI4 – Tokens are bypassed in shadow and motion
**Deviation:** values are written out where ECO has tokens. The rendered shadow is correct.  
**Should be:** `var(--shadow-elevation-b-20)` and the ECO easing and duration tokens (`eco-elevation`, `eco-motion`).  
**Currently:** `shadow-[0_1px_3px_...,0_0_1px_...]`, `duration-150`, `ease-[cubic-bezier(.35,0,.35,1)]`.  
**Suggestion:** replace them with the tokens, or add the tokens to the platform if they are missing (see Q4).

## ♿ WCAG

Standard: WCAG 2.2 AA, per the ticket.

**Group 1: implementation fails. Developers fix.**

- W: see C2 (1.4.3 contrast) and MA10 (1.4.11 focus indicator).

### W1 – Focus is lost after closing (2.4.3 Focus Order, A)
**Deviation:** pressing Return on the close button removes the banner and focus falls to the top of the document.  
**Should be:** focus moves to a logical nearby element.  
**Currently:** `document.activeElement` is `BODY`.  
**Suggestion:** move focus to the next focusable element or the banner's container in the page.

### W2 – Large title is not a heading (1.3.1 Info and Relationships, A)
**Deviation:** the visual heading of Large is a paragraph.  
**Should be:** a real heading, with a level the consumer can set.  
**Currently:** `<p class="title-md">`.  
**Suggestion:** render a heading element with a configurable level, keeping the `title-md` style.

### W3 – Region and button names are generic (2.4.6 Headings and Labels, AA)
**Deviation:** the label gives only the status, and the close name is English beside Swedish content.  
**Should be:** a descriptive, translated name.  
**Currently:** `role="region" aria-label="Informational"`, `aria-label="Close"`. Promotion uses `aria-label="Promotion"`.  
**Suggestion:** make both labels translatable props. Include the banner's title in the close name if possible.

### W4 – Status is not announced (4.1.3 Status Messages, AA)
**Deviation:** a banner added after page load would not be announced to assistive technology.  
**Should be:** `role="status"` for general messages and `role="alert"` for urgent errors, when inserted dynamically.  
**Currently:** only `role="region"`. Dynamic insertion cannot be tested in Storybook.  
**Suggestion:** add a prop for the live role, and confirm the use on real pages.

**Group 2: design or ECO conflicts with WCAG. Developers must not deviate from ECO; for the design system owners.**

### W5 – ECO focus token is invisible on the blue surface (1.4.11, AA)
**Deviation:** the ring token nearly matches the Informational Strong background.  
**Should be:** at least 3:1 against the surface.  
**Currently:** `--color-border-focus` `#455EFB` on `#0066FF` is about 1.0:1 (calculated).  
**Suggestion:** ECO needs an inverted focus token for Strong surfaces.

### W6 – Warning icon has low contrast (1.4.11, AA)
**Deviation:** the warning colours are too close to each other. This conveys status, though the text carries the meaning too.  
**Should be:** 3:1 for meaningful graphics.  
**Currently:** calculated from the measured colours: `#FFF5C2` on `#FAC000` (Strong) and `#FAC000` on `#FFF5C2` (Weak) 1.52:1, `#FAC000` on white (Weaker) 1.67:1.  
**Suggestion:** design reviews the warning icon colour in ECO.

### W7 – Inverted link hover is below text contrast (1.4.3, AA)
**Deviation:** the hover state of the inverted link loses contrast on blue.  
**Should be:** 4.5:1.  
**Currently:** `rgba(255,255,255,0.78)` on `#0066FF`, about 3.5:1 (calculated).  
**Suggestion:** design reviews the `text-action-primary-inverted-hover` token.

**Group 3: design gap. Design adds the state, then developers implement it.**

### W8 – Banner states are not drawn in Figma (2.4.7, AA)
**Deviation:** the component set has no hover or focus frames for close, link or buttons on each surface.  
**Should be:** focus and hover drawn at least for Strong surfaces.  
**Currently:** only the Enabled state is present in the set.  
**Suggestion:** add the state frames, including the Promotion link hover.

**Measured and passing:** Tab order is logical (buttons, link, close). Return closes the banner. No horizontal overflow at 320 px. Close button target is 32 x 32 px now and will be 24 x 24 px after C4, which passes 2.5.8. Text passes on all status colours: white on Strong blue 4.84:1, green 4.67:1, red 5.31:1 (calculated). Status icons are `aria-hidden`.

## ❓ To confirm

### Q1 – Should banners stop at 1200 px?
**Deviation:** Small and Large stop at 1200 px on wider screens.  
**Should be:** unclear. Figma frames are drawn 1200 px wide, while `eco-banner-notification` says full container width, and "Header top" placement suggests full width.  
**Currently:** `md:max-w-[1200px]`, 1200 px wide at an 1800 px viewport.  
**Suggestion:** design decides. If full width, remove the max-width and constrain the content instead.

### Q2 – Should Promotion have a close button?
**Deviation:** three sources disagree.  
**Should be:** unclear. The ticket says Promotion has no close control. Figma has one on desktop and none on mobile. `eco-banner-notification` says one was added on mobile in 2026-10, pending confirmation.  
**Currently:** matches Figma: shown from 769 px, hidden below.  
**Suggestion:** design decides, then update the ticket or the skill.

### Q3 – Should closing be animated?
**Deviation:** the banner disappears at once. Figma shows no motion and the ticket does not ask for it.  
**Should be:** ECO recommends a fade and height collapse with `--ease-accelerate-generic` and `--duration-fast-3` (`notifications-guide`).  
**Currently:** removed within 40 ms of the click.  
**Suggestion:** add it if it is in scope.

### Q4 – Are the platform token names intended?
**Deviation:** variables are named `--color-color-*` where ECO has `--color-*`.  
**Should be:** `tokens.json` names, for example `--color-surface-information-default`.  
**Currently:** `--color-color-surface-information-default`. Values match.  
**Suggestion:** confirm whether this is a platform decision.

### Q5 – Does the ticket's "primary/secondary" wording match Figma?
**Deviation:** the ticket says primary and secondary buttons on Large. Figma has Secondary + Blank on Weak and Weaker, and Primary Inverted + Blank on Strong.  
**Should be:** Figma, unless the ticket is meant to change it.  
**Currently:** the implementation follows Figma, apart from C2.  
**Suggestion:** –

## 📐 Issues in the Figma file itself (for design, not developers)

### F1 – Extra blue edge on Large banners
**Deviation:** the Large wrapper has `border-l-2` in `surface-information-default` in addition to the left bar, also on Success and Warning.  
**Should be:** only the left bar, 8 or 4 px, in the status colour.  
**Currently:** `23559:44269` (Success) and `23559:44083` (Warning) both carry the blue border in the generated code. The XSmall Informational frame `23557:161878` has it too.  
**Suggestion:** remove the border from the Big Notification Banner component.

### F2 – Tablet Large uses another edge colour
**Deviation:** the Small breakpoint uses `border-information-weak`, the others `border-information-weaker`.  
**Should be:** `-weaker` at every breakpoint (`eco-banner-notification`).  
**Currently:** `23557:161877` uses `#D0E9FF`.  
**Suggestion:** align the frame.

### F3 – Strong Large frames show a second, smaller link
**Deviation:** `23559:44268` (Success Strong) shows two "Text link" items, the second smaller. Weak frames show one.  
**Should be:** one consistent pattern.  
**Currently:** visible in the frame's render. Informational and Error Strong look the same in the overview.  
**Suggestion:** decide on one or several links, then align the frames.

### F4 – Hardcoded body link on tablet and mobile Large
**Deviation:** "adressboken" is 17/24 px inside 16/22 px body text.  
**Should be:** 16/22 px, `body-md` mobile.  
**Currently:** `23557:161877`, `23557:161878`.  
**Suggestion:** apply the `body-md--underline` style.

### F5 – Promotion desktop link is off the type scale
**Deviation:** the link is 18/16 px, a pair that is not in the ECO tokens.  
**Should be:** `body-md` 17/24 px, 0.32 px (`eco-banner-notification`). The implementation already uses this.  
**Currently:** `13377:42264`.  
**Suggestion:** apply the text style.

### F6 – Icon layers keep old names
**Deviation:** layer names do not match the icon, for example `nest_eco_leaf` holding a warning icon.  
**Should be:** a name that matches the icon.  
**Currently:** `23559:44082`, `23559:44268`.  
**Suggestion:** rename the layers to avoid wrong handoff.

## ✅ Matches design and ECO

- Small, all 12 status and emphasis combinations: background, left border colour, icon colour, text, link and close icon colour.
- Small breakpoint switch: padding and title size change exactly between 768 and 769 px.
- Small: 2 px left border, 12/16 px padding from 769 px and 8/16 px below, 8 px gap, 24 px icon.
- Small type: title 14/14 px, 0.56 px and 12/12 px, 0.48 px, uppercase. Desktop body 14/20 px, 0.36 px. Link 14/20 px, 0.36 px, underlined, hover removes the underline.
- Shadow values on Small and Promotion, equal to `elevation-b-20`.
- Large at the matching `version`: bar 8/4/4 px, icon 48/40/24 px, padding 24, 16 and 12/12/16 px, footer top 24 px and indent 60/52/32 px, buttons 32 px high.
- Large type: title 20/24 and 18/22 px, body 17/24 and 16/22 px, 0.32 px.
- Large Strong, measured on desktop: Primary Inverted + Blank Inverted on Informational, Success and Error; black link and close on Warning; white on the others.
- Promotion colours: Strong `#C7D300`, Weak `#F4F6CC`, Dark `#000000`.
- Promotion layout: centred on desktop; on mobile the title sits left and the link right, 14 px, 0.42 and 0.36 px.
- Controls work: `showTitle`, `showLink`, `closeButton`, custom `icon`, and close by mouse and keyboard.
- Font weight: title 600 and link 700 render the same Bold face, since only weights 400 and 700 are loaded.

## Not tested

- Tools brand. Only the Swedol accent was seen.
- Real pages, placement under a header or breadcrumb, and dismissal persistence. Storybook only.
- Screen reader output, 200% text zoom (1.4.4) and text spacing (1.4.12).
- `prefers-reduced-motion`. The only motion seen was the 150 ms link colour transition.
- Colours for all Large statuses at tablet and mobile widths. They were measured at desktop width.
- Hover on every surface: hover was measured on Informational Strong Small only. Active and disabled states.
- Whether the whole Promotion banner is clickable, as `eco-banner-notification` describes.
- `font-feature-settings`. It has no visible effect per `eco-typography`, so it is not a finding.
- No comparison images are included. Every finding has measured values.
