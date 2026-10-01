---
name: design-review
description: Use when reviewing a page or component that developers have built (UAT/staging URL or code) against the original Figma design and the ECO Design System, to produce a severity-grouped deviation report for the developers — as a file and/or a Jira comment, optionally with annotated Figma-vs-implementation comparison images.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, breakpoints and the quality checklist. The ECO skills (`eco-tokens`, `eco-typography`, `eco-colors`, `eco-spacing`, the component skills) are the source of truth for design rules — not only what a single Figma frame happens to show.

# Design review: implementation vs. Figma + ECO

Goal: clear, verified feedback that developers can act on. Every item says what deviates, what it should be (Figma node or ECO token/skill), what the code does now, and a concrete fix.

## 1. Before you start — ask, don't guess

1. **Figma access.** Check that the Figma MCP tools are available (use ToolSearch). If not, ask for exported images.
2. **Figma frames, one per breakpoint.** Ask for a node link (`node-id` in the URL) for every breakpoint that has a design, even when the implementation is one responsive page. List the ECO breakpoints so the user can map them:

   | ECO breakpoint | Width | Styling |
   |---|---|---|
   | `xs` | 375–639px | Mobile Base |
   | `sm` | 640–768px | Mobile Base |
   | `md` | 769–1023px | Desktop Base |
   | `lg` | 1024–1280px | Desktop Base |
   | `xl` | 1281px+ | Desktop Base |

   If one frame covers several breakpoints, ask which width it is drawn at. Ask for state frames too (hover, error, empty, open menus). Breakpoints without a frame are checked against ECO rules only, and the report says so.
3. **Implementation.** URL of the running page and/or repo path. Ask whether it needs a login — the user logs in themselves; never type credentials.
4. **Jira.** The ticket link looks like `https://<site>.atlassian.net/browse/KEY-123`. Posting needs the Atlassian connector; without it, deliver a file the user pastes. Read the ticket's acceptance criteria — they are part of the review (e.g. WCAG, rows per load, sorting).
5. **Prototype.** Ask whether the page or component has a Claude Code prototype in this repo (a page under `mypages/` or the repo root; `index.html` lists them). If yes, get the path. If several versions exist (for example `users.html` and `users_V1.html`), ask which one matches the ticket. Do not assume the newest. See "Prototype as a source" in section 2.
6. **Report language and format.** Ask (default: English, Markdown for the new Jira editor).

## 2. Read the design

- Load `figma-design-to-code` before `get_design_context`. Large frames come back as sparse metadata — call `get_design_context` on the sub-layers (page title, toolbar, table, pagination, mobile card) instead.
- Note which values are bound to variables/text styles and which are hardcoded **in Figma itself**. Figma's own local deviations go in a separate "Issues in the Figma file" section so developers do not copy a wrong value.
- Also search the ECO library (`search_design_system`, file `42MgqJjV9vfplwQnrUB62r`) when a component's origin is unclear.

### Prototype as a source (functionality)

If a prototype exists, read its HTML/JS and run it in the browser. Use it as the reference for **behaviour and states** that Figma does not show: search and filter logic, sorting (including the sorted state), hover/focus/keyboard behaviour, empty, loading and error states, pagination, transitions. Compare each behaviour with the implementation and report differences under the normal levels.

Rules:
- **Figma wins for visuals** (spacing, size, colour, layout). The prototype is not a design source for those.
- **The Jira ticket wins for scope.** Prototype behaviour that the ticket does not ask for is not a deviation.
- The prototype uses ECO tokens and skills, so it can show the intended token or pattern when Figma is unclear. Say in the report that the value comes from the prototype.
- If the prototype and Figma disagree, do not pick one. List it under "To confirm" and name both.
- Behaviour the prototype has and Figma lacks (for example a sorted state) is a design gap: list it under "Issues in the Figma file".

## 3. Measure the implementation

- **Browser choice.** A page behind basic auth or a user login returns 401 in the built-in browser pane. Use Claude in Chrome (the user's own logged-in Chrome); if it is not connected, ask the user to install/sign in to the extension.
- **Read computed values, never guess from screenshots:** `getComputedStyle` for font size/weight/line-height/letter-spacing/`font-feature-settings`, colours, borders, padding, gaps, sizes, and `getBoundingClientRect` for spacing between elements.
- **Widths.** If the Chrome window cannot be made narrow enough, load the same URL in a same-origin `<iframe>` of exact width inside the page and measure inside it. Check at least 375 (`xs`), 700 (`sm`), 1024 (`lg`) and the desktop frame width, as CLAUDE.md requires. In addition, test the widths on either side of a breakpoint (639/640, 768/769, 1280/1281) whenever a value looks like it changes at the wrong width. The mobile→desktop switch must happen exactly between 768 and 769.
- **Tokens.** Check `:root` for ECO variables (`--color-*`, `--shadow-elevation-*`) and scan stylesheet rules for the page's selectors to see whether values use tokens, legacy variables or literals.
- **States and accessibility.** (Findings go in the WCAG section, see section 4.) Hover, keyboard focus (do hover-only menus appear on focus? is there a focus ring?), sortable headers (`<button>`, `aria-sort`, visible active sort), a visible `<h1>`, tooltips, empty/disabled states.
- **Acceptance criteria.** Test the behaviour the ticket asks for (search as you type, sorting, rows per load).
- **Clean up** any injected iframes or test elements afterwards.

## 4. WCAG check (separate section in the report)

Check the design (Figma) and the implementation against WCAG. Default: **WCAG 2.2, level AA**. If the Jira ticket names another version or level, use that. Ask when unsure.

Check at least:

| Area | Success criteria | How |
|---|---|---|
| Contrast | 1.4.3 text 4.5:1 (large text 3:1), 1.4.11 non-text 3:1 (input borders, icons, focus ring) | Compute the ratio from the computed colours (for both Figma tokens and live values). Report the ratio. |
| Keyboard | 2.1.1, 2.4.3, 2.4.7, 2.4.11 | Tab through the page. Everything interactive is reachable, in a logical order, with a visible focus that is not hidden. Hover-only content must also appear on focus. |
| Structure | 1.3.1, 2.4.6, 4.1.2 | One visible `<h1>`, correct heading levels, real `<button>`/`<a>`/`<label>` elements, name/role/state (`aria-sort`, `aria-expanded`, …). |
| Target size | 2.5.8 (min 24×24 CSS px) | Measure interactive elements. |
| Reflow and text | 1.4.10 (320px), 1.4.4 (200% zoom), 1.4.12 | Check at 320px and with enlarged text. No clipped or overlapping content. |
| Colour and hover | 1.4.1, 1.4.13 | Nothing conveyed by colour alone. Tooltips are dismissible, hoverable and persistent. |
| Forms and status | 3.3.1–3.3.3, 4.1.3 | Labels, errors that say what is wrong, status messages announced. |
| Motion | 2.3.3 / `prefers-reduced-motion` | Animations respect the setting. |
| Images and icons | 1.1.1 | Text alternatives, or hidden from assistive technology when decorative. |

Sort every finding into one of three groups:

1. **Implementation fails WCAG.** The design is fine, or the design does not say. Developers fix it. Level A/AA failures are Critical.
   - **Obvious failures stay in Critical.** Clear-cut implementation failures such as missing keyboard access, no visible focus, hover-only content or a missing `<h1>` are listed under Critical (with the criterion in the item, for example `WCAG 2.4.7`). They are not moved.
2. **Design or ECO conflicts with WCAG.** The design system itself does not meet a criterion (for example a token colour with too little contrast, a component smaller than 24px, a missing focus style). This may be intentional. Developers must **not** deviate from ECO for it. List it for the design system owners so it can be fixed in ECO later.
3. **Design gap.** Figma has no state that WCAG needs (focus, error, sorted, disabled). Design adds the state, then developers implement it.

Give each finding the criterion number and level (for example `2.4.7 Focus Visible (AA)`), the measured value, and the group. The WCAG section holds the audit: everything under groups 2 and 3, and the group 1 findings that are not obvious enough for Critical (for example contrast ratios, target size, reflow). For a group 1 finding already listed under Critical, do not repeat it; add a one-line reference (`W: see C2`) so the WCAG section is complete.

## 5. Verify before you report

Every claim of a *visible* difference must be checked by rendering or measuring it. A CSS value that differs from the spec is not automatically a visible deviation — for example, `font-feature-settings` has no effect because the web fonts do not contain the stylistic sets (see `eco-typography`). If unsure whether something is intentional, put it under "To confirm" and ask, instead of guessing.

## 6. Severity

Every deviation from the Figma design or ECO is a defect and should be fixed. The levels set the order of the work, not whether a deviation is fixed.

| Level | Meaning |
|---|---|
| 🔴 **Critical** | Breaks the design system / tokens, or is visibly wrong. Fix first. (Obvious WCAG failures also belong here, see section 4.) |
| 🟠 **Major** | Clear, visible deviation from the design (size, spacing, layout, colour). |
| 🟢 **Minor** | Small deviation from the design or a token (e.g. letter-spacing, radius, shadow). Lowest priority, but still fixed. |

Item ids: `C1…` Critical, `MA1…` Major, `MI1…` Minor, `W1…` WCAG, `Q1…` To confirm, `F1…` Figma file issues.
| ❓ **To confirm** | Possibly intentional, platform-level, or a design decision — needs an answer before it is a deviation. |

The user decides the final severity of platform-level items (e.g. missing ECO tokens).

## 7. Report structure

```
# Design review: <page> (<TICKET>)
Page reviewed / Figma frames (one link per breakpoint) / Prototype (path, if any) / Source of truth / Method
## 🔴 Critical        C1, C2 …
## 🟠 Major           MA1, MA2 …
## 🟢 Minor           MI1, MI2 …
## ♿ WCAG            W1, W2 …  (grouped: implementation fails / design or ECO conflicts / design gap)
## ❓ To confirm      Q1, Q2 …
## 📐 Issues in the Figma file itself (for design, not developers)   F1, F2 …
## ✅ Matches design and ECO
```

Each item: **Deviation**, **Should be** (Figma node or ECO token/skill), **Currently** (measured value), **Suggestion** (selector/file). Keep UI strings from the page in their original language.

Save the report where the user can find it (e.g. a folder on the Desktop), not only in a temp/scratchpad folder.

## 8. Comparison images (optional)

Use them where text alone may be misread: layout differences, spacing, hover menus, missing states.

- **Figma side:** `download_assets` on the relevant node at `defaultScale: 2`.
- **Implementation side:** automated export from the authenticated page is blocked (injecting libraries and passing upload tokens are refused). Ask the user for DevTools screenshots instead — give a table with file name, width and exactly what must be visible. DevTools: Cmd+Shift+M for the device toolbar (Swedish: "Växla enhetsverktygsfält"), Cmd+Shift+P → "Capture screenshot" ("Ta skärmbild").
- **Compose** with Pillow: Figma and implementation side by side or stacked, blue marks = design, red marks = deviation, short tags on the image (`C1`, `MA2`) and a legend with one line per tag under the image. Check each image visually for overlapping labels before delivering. Reusable drawing helpers (`box`, `vbrace`, `panel`, `sheet`, `save`) are in `compose-helpers.py` in this folder; import or copy them and write the per-image sections for the current ticket.

### Where images go in the Jira comment

1. Put each image **once**, directly under the **first** item in the comment that it shows.
2. Number images in the order they appear in the comment (Image 1, 2, …), not by file name.
3. Under each image, a caption: `Image N – <view, width>, Figma (top/left) vs UAT (bottom/right). Marks: <tags>.`
4. In every other item the image covers, add a last line: `See Image N.` (or `See Image 1 (desktop) and Image 4 (tablet).`).
5. **Write the report as if the images were already in place.** When the user inserts the images by hand, put a placeholder line where each image goes, then the caption, and the `See Image N.` references in the other items:

   ```
   > 📷 **INSERT IMAGE 1 HERE:** `<TICKET>_01_<short-name>.png` *(delete this line after inserting the image)*

   *Image 1 – Desktop 1440px, Figma (top) vs UAT (bottom). Marks: C1, MA1, MA3, MA4, MA5, Q1.*
   ```

   The user drops the image onto the placeholder line and deletes that line; the caption stays. Add a short "Images:" note near the top of the report saying which image is under which item.
6. Also give the user a placement table:

| Image | Goes under | Also shows |
|---|---|---|
| `<TICKET>_01_<short-name>.png` | C1 | MA1, MA3, MA4, MA5, Q1 |

Example captions (adapt the view, width and tags):
- `Image 1 – Desktop 1440px, Figma (top) vs UAT (bottom). Marks: C1, MA1, MA3.`
- `Image 2 – Hover state (UAT). Marks: MA6. Also relevant for C2: this state never appears on keyboard focus.`
- `Image 3 – Tablet (sm): Figma 768px (left) vs UAT 700px (right). Marks: MA2.`

## 9. Delivering

- **File:** always.
- **Jira comment:** show the final text and wait for a clear "yes" before posting — it is published in the user's name. Markdown is accepted by `addOrEditJiraIssueComment`.
- **Images in Jira:** uploading needs the Atlassian media token in a shell command, which auto mode blocks. Either the user drags the images into the comment by hand (use the placement table above), or the user adds a permission rule first.
- **Figma annotations:** writing to a shared design file needs explicit approval and may be blocked in auto mode. Ask before placing anything in Figma.
- **Corrections:** if a finding turns out wrong, say so plainly, correct the report file and give the user the replacement text for Jira.
