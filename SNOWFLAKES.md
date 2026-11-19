# Snowflakes

A snowflake is a deliberate one-off: a value or a pattern that is in Figma or in a prototype but is **not** a token, a component or a rule of the ECO Design System, and should not become one.

Only entries the user has confirmed as a snowflake are listed here. Something that is merely missing from the tokens or skills is a flag, not a snowflake: ask first (`CLAUDE.md`, Quality control rule 7).

How to use this list:

- Before you flag a value as "not a token", look here. A listed snowflake is used as it is, with a short comment in the CSS that points to this file.
- A snowflake applies only where the entry says. Never reuse it somewhere else; ask if it seems to fit a second place (then it may need to become a token or a component).
- Add an entry only after the user has confirmed it. Give the date, where it is used and the Figma node.

| # | Snowflake | Value | Where | Figma | Confirmed |
|---|---|---|---|---|---|
| 1 | Unit text in the Picker Stepper value cell ("st", "unit") | 10px/10px, letter-spacing 0.3px below 769px; 11px/11px, 0.33px from 769px. Not a type style in `tokens.json`. | `components/css/picker-stepper.css` (`.picker-stepper__unit`), skill `eco-picker-stepper` | ECO `1612:111715`, value states `1609:63554` | 2026-11-11 |
| 2 | Article-number badges that copy on click | Badge/Basic look on a `<button>`: click copies the number, a tooltip names the action, an E-Com toast (Informational) confirms. Badge itself stays non-interactive (`eco-badge`). A one-off "for now". | `pdp.html` Top info (`.pdp-artnr__copy`) | PLP & PDP `2665:542997` | 2026-11-11 |
