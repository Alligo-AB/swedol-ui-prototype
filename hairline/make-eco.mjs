#!/usr/bin/env node
// node hairline/make-eco.mjs <name>
// Builds hairline-<name>.eco.html: the clean validated page plus the ECO fonts/tokens links and <name>.eco.css pasted in.
// Run it after every rebuild of hairline-<name>.html (skill hairline-create: look.mjs/build.mjs). Run from anywhere.
import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
const dir = dirname(fileURLToPath(import.meta.url)), name = process.argv[2];
if (!name) { console.error("usage: make-eco.mjs <name>"); process.exit(2); }
const page = readFileSync(join(dir, `hairline-${name}.html`), "utf8"), css = readFileSync(join(dir, `${name}.eco.css`), "utf8");
const links = '<link rel="stylesheet" href="https://unpkg.com/alligo-design-tokens@latest/dist/css/fonts.css">\n<link rel="stylesheet" href="https://unpkg.com/alligo-design-tokens@latest/dist/css/index.css">\n';
// the bench's play button starts the tour at once (same as the cards: kernel.js patch), not after the resume pause (also when Play is pressed again)
const eco = page.replace("</head>", `${links}<style>\n${css}</style>\n</head>`).replace("let wait = RESUME + STAGGER * (started++ % 4);", "let wait = 0; started++;").replaceAll("wait = RESUME;", "wait = 0;").replace("var TRAVEL = 900;", "var TRAVEL = 500;");
writeFileSync(join(dir, `hairline-${name}.eco.html`), eco);
console.log(`wrote hairline-${name}.eco.html`);
