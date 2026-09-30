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
5. **Report language and format.** Ask (default: English, Markdown for the new Jira editor).

## 2. Read the design

- Load `figma-design-to-code` before `get_design_context`. Large frames come back as sparse metadata — call `get_design_context` on the sub-layers (page title, toolbar, table, pagination, mobile card) instead.
- Note which values are bound to variables/text styles and which are hardcoded **in Figma itself**. Figma's own local deviations go in a separate "Issues in the Figma file" section so developers do not copy a wrong value.
- Also search the ECO library (`search_design_system`, file `42MgqJjV9vfplwQnrUB62r`) when a component's origin is unclear.

## 3. Measure the implementation

- **Browser choice.** A page behind basic auth or a user login returns 401 in the built-in browser pane. Use Claude in Chrome (the user's own logged-in Chrome); if it is not connected, ask the user to install/sign in to the extension.
- **Read computed values, never guess from screenshots:** `getComputedStyle` for font size/weight/line-height/letter-spacing/`font-feature-settings`, colours, borders, padding, gaps, sizes, and `getBoundingClientRect` for spacing between elements.
- **Widths.** If the Chrome window cannot be made narrow enough, load the same URL in a same-origin `<iframe>` of exact width inside the page and measure inside it. Check at least 375, 639, 640, 700, 768, 769, 1024 and the desktop frame width. Confirm the mobile→desktop switch happens exactly between 768 and 769.
- **Tokens.** Check `:root` for ECO variables (`--color-*`, `--shadow-elevation-*`) and scan stylesheet rules for the page's selectors to see whether values use tokens, legacy variables or literals.
- **States and accessibility.** Hover, keyboard focus (do hover-only menus appear on focus? is there a focus ring?), sortable headers (`<button>`, `aria-sort`, visible active sort), a visible `<h1>`, tooltips, empty/disabled states.
- **Acceptance criteria.** Test the behaviour the ticket asks for (search as you type, sorting, rows per load).
- **Clean up** any injected iframes or test elements afterwards.

## 4. Verify before you report

Every claim of a *visible* difference must be checked by rendering or measuring it. A CSS value that differs from the spec is not automatically a visible deviation — for example, `font-feature-settings` has no effect because the web fonts do not contain the stylistic sets (see `eco-typography`). If unsure whether something is intentional, put it under "To confirm" and ask, instead of guessing.

## 5. Severity

| Level | Meaning |
|---|---|
| 🔴 **Critical** | Breaks the design system / tokens, breaks WCAG, or is visibly wrong. |
| 🟠 **Should fix** | Smaller but noticeable deviation. |
| 🟢 **Nice-to-have** | Polish, marginal. |
| ❓ **To confirm** | Possibly intentional, platform-level, or a design decision — needs an answer. |

The user decides the final severity of platform-level items (e.g. missing ECO tokens).

## 6. Report structure

```
# Design review: <page> (<TICKET>)
Page reviewed / Figma frames (one link per breakpoint) / Source of truth / Method
## 🔴 Critical        C1, C2 …
## 🟠 Should fix      S-1, S-2 …
## 🟢 Nice-to-have    N1, N2 …
## ❓ To confirm      Q1, Q2 …
## 📐 Issues in the Figma file itself (for design, not developers)   F1, F2 …
## ✅ Matches design and ECO
```

Each item: **Deviation**, **Should be** (Figma node or ECO token/skill), **Currently** (measured value), **Suggestion** (selector/file). Keep UI strings from the page in their original language.

Save the report where the user can find it (e.g. a folder on the Desktop), not only in a temp/scratchpad folder.

## 7. Comparison images (optional)

Use them where text alone may be misread: layout differences, spacing, hover menus, missing states.

- **Figma side:** `download_assets` on the relevant node at `defaultScale: 2`.
- **Implementation side:** automated export from the authenticated page is blocked (injecting libraries and passing upload tokens are refused). Ask the user for DevTools screenshots instead — give a table with file name, width and exactly what must be visible. DevTools: Cmd+Shift+M for the device toolbar (Swedish: "Växla enhetsverktygsfält"), Cmd+Shift+P → "Capture screenshot" ("Ta skärmbild").
- **Compose** with Pillow: Figma and implementation side by side or stacked, blue marks = design, red marks = deviation, short tags on the image (`C1`, `S-2`) and a legend with one line per tag under the image. Check each image visually for overlapping labels before delivering. See `compose-example.py` in this folder.

### Where images go in the Jira comment

1. Put each image **once**, directly under the **first** item in the comment that it shows.
2. Number images in the order they appear in the comment (Image 1, 2, …), not by file name.
3. Under each image, a caption: `Image N – <view, width>, Figma (top/left) vs UAT (bottom/right). Marks: <tags>.`
4. In every other item the image covers, add a last line: `See Image N.` (or `See Image 1 (desktop) and Image 4 (tablet).`).
5. **Write the report as if the images were already in place.** When the user inserts the images by hand, put a placeholder line where each image goes, then the caption, and the `See Image N.` references in the other items:

   ```
   > 📷 **INSERT IMAGE 1 HERE:** `AE-3036_01_desktop_search_table.png` *(delete this line after inserting the image)*

   *Image 1 – Desktop 1440px, Figma (top) vs UAT (bottom). Marks: C1, S-1, S-3, S-4, S-5, Q1.*
   ```

   The user drops the image onto the placeholder line and deletes that line; the caption stays. Add a short "Images:" note near the top of the report saying which image is under which item.
6. Also give the user a placement table:

| Image | Goes under | Also shows |
|---|---|---|
| `…_01_desktop_search_table.png` | C1 | S-1, S-3, S-4, S-5, Q1 |

Example captions (AE-3036):
- `Image 1 – Desktop 1440px, Figma (top) vs UAT (bottom). Marks: C1, S-1, S-3, S-4, S-5, Q1.`
- `Image 2 – Row actions on hover (UAT). Marks: S-6, N2. Also relevant for C2: this menu never appears on keyboard focus.`
- `Image 3 – After sorting by "Namn": list is sorted, header icon unchanged. Marks: C3, F3.`
- `Image 4 – Tablet (sm): Figma 768px (left) vs UAT 700px (right). Marks: S-2, S-1, F2.`

## 8. Delivering

- **File:** always.
- **Jira comment:** show the final text and wait for a clear "yes" before posting — it is published in the user's name. Markdown is accepted by `addOrEditJiraIssueComment`.
- **Images in Jira:** uploading needs the Atlassian media token in a shell command, which auto mode blocks. Either the user drags the images into the comment by hand (use the placement table above), or the user adds a permission rule first.
- **Figma annotations:** writing to a shared design file needs explicit approval and may be blocked in auto mode. Ask before placing anything in Figma.
- **Corrections:** if a finding turns out wrong, say so plainly, correct the report file and give the user the replacement text for Jira.
