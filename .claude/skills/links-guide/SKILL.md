---
name: links-guide
description: Use BEFORE building a link, to decide whether it should be an Inline Link (in body text), Action Link (standalone), or Tile Link (graphical/prominent). Then read the skill for the specific link type.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Links – Usage Guidelines (ECO Design System)

**Figma:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=1221-33213

The ECO Design System has three link types: **Inline Link**, **Action Link**, and **Tile Link**.

Links take users somewhere: another page, another site, a section of the same page, or a resource such as a PDF, an email address or a phone number. They are the lightest interactive element: where a Button performs an action, **a link always navigates**. The three components share one foundation (semantics, keyboard behavior, state logic) and differ in context and visual weight. Choose in this order: an action instead of navigation is not a link (use `eco-button`); inside a sentence or paragraph is an Inline Link; a graphic, prominent surface in a grid of peers is a Tile Link; standing on its own with an icon is an Action Link.

### When should a link be used?

Use a link when the user should:
- Navigate to another page within the site/application
- Navigate to an external site
- Jump to an element on the same page
- Act on something, e.g. open email or call a number

### Which link type?

| Type | Usage | Underline | Icons |
|---|---|---|---|
| **Inline Link** | Inside sentences or text blocks | Underlined when enabled, removed on hover | Never |
| **Action Link** | Standalone, not in body text | Underlined on hover only | Leading and/or trailing |
| **Tile Link** | Graphical/prominent, like a card or button | — | With or without |

### Interaction (all link types)

- **Mouse:** click anywhere on the link text or associated icon
- **Keyboard:** Enter key while the link has focus
- The **entire element** is the click target; Tab moves focus; Enter activates.
- **Sizing** follows the type scale: a link inside content matches the size of its context; a standalone link matches the page's default body copy size.

### Documentation

`eco-design-system/components/links-guide.html` is the hub (one page, no tab bar: which link type, in context, behavior, usage) and the three types are its children, each as three pages: `inline-link*.html`, `action-link*.html`, `tile-link*.html` (Examples & Guidelines / Specifications / Code, converted 2026-10-13). Breadcrumb: Components / Links guide / Inline link.

### Modifiers (all link types)

Figma's link info (1221:33213, read 2026-10-13): the action link is paired with a leading icon, a trailing icon or both (the earlier "in some cases none" was removed from Figma; a link without an icon in text is the Inline link, also its reverse underline), icons are the same color as the link text, the action link underlines on hover, inline links are not paired with icons, and the link size matches the type size of the text it is in (apart from other content: the default body copy size). Each type has the **weight** modifiers in the CSS (`--weight-medium`, `--bold`; Regular default); **italic** (`--italic`) is for the Inline Link and the Tile Link only, an Action Link is never italic; the Inline link also has `--reverse` (underline on hover only, in Figma as `Reverse=yes`). Which of these are in Figma is listed in each type skill; the others are added and need design confirmation.
