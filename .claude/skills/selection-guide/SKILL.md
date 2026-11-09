---
name: selection-guide
description: Use BEFORE building anything where the user chooses — a form question, a filter, a setting, a list of options — to decide between Radio button, Checkbox, Chip, Select, Switch and Pill Segment Control by how many choices the user makes and how many options there are. Then read the skill for the chosen component.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Choosing a selection control (ECO Design System)

Decided with the user 2026-11-08. Two questions decide the control, in this order:

1. **Does the user make one choice or several?**
2. **How many options are there, and how long are their labels?**

### The rule

| Situation | Use | Skill |
|---|---|---|
| One choice, on/off that takes effect at once (a setting) | Switch | `eco-switch` |
| One choice, on/off inside a form that is submitted (accept terms, subscribe) | Checkbox | `eco-checkbox` |
| One choice, 2–7 options | Radio buttons | `eco-radio` |
| One choice, 8 or more options | Select | `eco-select` |
| Several choices, short options (1–2 words), about 12 or fewer, "pick all that apply" | Chips, with the helper text "Välj alla som passar" / "Select all that apply" | `eco-chip` |
| Several choices, long labels, options that need a description, or each option is a statement or a consent | Checkboxes | `eco-checkbox` |
| Several choices, very many options (about 15+) | Searchable list of checkboxes | `eco-checkbox` (+ `eco-input` for the search field) |
| Switching between two views of the same content (not a form value) | Pill Segment Control | `eco-pill-segment-control` |

### Conditions that always apply

- **Every option must be visible.** Radio buttons and chips work because the user sees all options without opening anything. If they do not fit, above all at xs/sm, use a Select (one choice) or a list (several choices) instead.
- **Chips do not show that several can be picked.** A checkbox says so by its shape; a chip does not. A chip group for several choices always has a helper text under the question ("Välj alla som passar"), most of all when radio buttons are near it (they teach "only one").
- **A form button does not decide it.** Chips are fine in a form with a Continue/Save button when the options are short and the question is "pick all that apply" (example: "Vilka verktyg använder ni?" with Claude, Figma, Slack …). The length and number of the options decide, not the button.
- **Offer "Annat" / "Other"** when the list may not cover every answer (a chip or checkbox that opens a text field).
- **Ordered ranges are one choice.** Team size, price range, quantity bands: radio buttons (or Select from 8), never chips.
- **Never a Pill Segment Control for a form value**, and never radio buttons to switch views.

### Docs playgrounds (2026-11-08)

The controls panel of every docs playground follows the same rule, applied automatically by `eco-design-system/gen/playground_rule.py` (run by `build.emit()` on every generated page; the hand-edited pages were converted with the same code):

| Field | Control |
|---|---|
| On/off (Off/On, None/X, Shown/Hidden, No/Yes) | Small switch (`sw_group`), one per row, its own text is the label (no heading); a set of related switches may share a heading (collapsible: Row, Header) |
| A field that recurs across pages: State, Size, Value, Content, Type, Color, Variant, Status | Radio buttons (`radio_group`, Small) on every page, even with 2 options |
| Breakpoint, Mode/Theme, Emphasis, Background, Weight, Style, Underline, Placement, Direction, Letter case | Button group on every page |
| Any other field, 2-3 one-word options | Button group |
| Any other field, 4-7 options or longer labels | Radio buttons |
| 8 or more options (button Variant, select State, tooltip Type) | Select |

**Exception, decision helpers** (user decision 2026-11-08): a question-and-answer helper on a docs page, such as "Primary or Secondary" on `components/tabs.html` (Usage), keeps button groups for its answers, also Yes/No and longer answers. The answers are quick replies in a small quiz, not settings or a form. `playground_rule.py` only touches the playground controls, so it leaves them alone.

**Same field, same control** (user decision 2026-11-08): a field that appears on several pages looks the same everywhere, even where the count rule would pick another control. Only fields unique to one page follow the count rule. The same principle applies to prototype pages.

### Example (reference, 2026-11-08)

An onboarding step with two questions: "Hur stort är ert team?" (5 ordered ranges, one choice → radio buttons) and "Vilka verktyg använder ni?" (8 short names, several choices → chips with "Välj alla som passar"). The different shapes also tell the user that the two questions work differently.

### Documentation

No docs page yet. A page "Choosing a selection control" under Patterns in `eco-design-system/` is planned once the rule has been tried on a few pages (ask the user first). Until then this skill is the only source.
