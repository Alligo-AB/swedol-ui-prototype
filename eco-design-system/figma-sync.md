# Figma sync list (code ahead of Figma)

Values that exist in the prototype code but not yet in the ECO Figma library or in `alligo-design-tokens`.
Every item here must be added in Figma (and then the token package) so design and code use the same names and values.
When an item is done in Figma and the package, tick it, and remove the provisional line from `components/css/premium.css`.

Rule: Claude never adds a new value without a token. If a provisional value is needed, it goes into `premium.css` **and** onto this list in the same change.

Started 2026-10-27 (premium extras for the docs start page hero).

## 1. Tokens to add (Figma variables, then the token package)

| # | Token (code name) | Value | Figma collection / type | Used for | Status |
|---|---|---|---|---|---|
| 1 | `--duration-loop-slow` | `90s` | Motion → Duration (number, ms: 90000) | Endless decorative loops: marquee, the scrolling column grid in the hero. Always `linear`, always with a pause button. Never for transitions. | [ ] Figma [ ] package |
| 2 | `--color-surface-opacity-black-80` | `rgba(0,0,0,0.8)` | Color → Surface → Opacity (next to Black 50) | Scrim behind inverted text over moving imagery or video. | [ ] Figma [ ] package |
| 3 | `--blur-edge` | `12px` | Effects → Blur (new group; Figma "Background blur" effect style) | Edge softening at the top and bottom of a decorative moving background. Not for glass panels. | [ ] Figma [ ] package |
| 4 | `--opacity-grain` | `0.05` | Effects → Opacity (number, 5%) or a "Grain" effect/fill style | Static noise layer over a dark hero. | [ ] Figma [ ] package |


Check in Figma: are values 1–4 right? If you change one, tell Claude and it updates `premium.css`.

## 2. Text style to add

| # | Style | Proposed size (desktop / mobile) | Status |
|---|---|---|---|
| 5 | `display-xl` | Desktop 84/76, mobile 48/44, letter-spacing 0.48px, weight and uppercase as `display-lg`. | [x] Figma (2026-10-27) [ ] `tokens.json` / package (the user adds it) [x] `eco-typography` (marked provisional) |

Use only for the start page hero and campaign heroes. In code it is the class `.display-xl` in `components/css/premium.css` until `tokens.json` has it.

## 3. Patterns to document in Figma (no new token, but needs a Figma example)

| # | Pattern | What to draw in Figma | Status |
|---|---|---|---|
| 6 | Premium hero | One frame per breakpoint (xs 375, sm 700, md 1024, xl 1440): moving column grid, black-80 scrim, top/bottom vignette, edge blur bands (`space-120` high, md+ only), grain, centred content, scroll cue and pause button. | [ ] |
| 7 | Hero scroll-out | Prototype note: content opacity 1 to 0 and moves up `space-48` while the hero scrolls away (md+). | [ ] |
| 8 | Pointer parallax | Prototype note: background moves at most `space-16` against the cursor (md+, mouse only), smoothed with `duration-slow-4` / `ease-decelerate-emphasized`. | [ ] |

## 4. Decided against (do not add)

- Rounded tiles or cards. ECO is sharp-cornered. Decided 2026-10-27.
- Glass panels (frosted cards, headers or buttons over content). Still void.

## Where the rules live in code

- `CLAUDE.md`, section "Premium extras"
- `.claude/skills/eco-motion/SKILL.md`, Campaign motion rules 8 and 11
- `.claude/skills/eco-colors/SKILL.md`, opacity table (black-80, marked provisional)
- `components/css/premium.css`, the provisional tokens and the `.fx-edge-blur` / `.fx-grain` classes
- Reference page: `eco-design-system/index.html` (hero)
