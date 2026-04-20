---
name: Do not change table structure
description: Never alter the structure, setup, or column logic of the data tables in the frontend
type: feedback
---

Do not change any structure or setup regarding the design tables in the frontend.

**Why:** The user explicitly instructed this — table structure, column definitions, ordering logic, and layout should remain untouched unless the user specifically asks to change them.

**How to apply:** When working on adjacent features (tooltips, drawers, styling, etc.), leave the table HTML structure, the COLS array order, and any table-related JS (applyColOrderToTable, buildColList, column visibility logic) exactly as they are. Only touch table-related code if the user's request directly targets the table itself.
