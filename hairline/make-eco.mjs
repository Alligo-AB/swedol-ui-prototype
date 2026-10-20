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
// the bench play button starts the tour at once, like the cards (same patch as hairline/kernel.js)
const out = page.replace("</head>", `${links}<style>\n${css}</style>\n</head>`)
  .replace("function tour(stage, stops, onStop) {", "function tour(stage, stops, onStop, delay) {")
  .replace("let wait = RESUME + STAGGER * (started++ % 4);", "let wait = delay ?? RESUME + STAGGER * (started++ % 4);")
  .replace("figure.tour || HL.LAP, (i) => { if (window.hairline.onStop) window.hairline.onStop(i); });", "figure.tour || HL.LAP, (i) => { if (window.hairline.onStop) window.hairline.onStop(i); }, 0);");
writeFileSync(join(dir, `hairline-${name}.eco.html`), out);
console.log(`wrote hairline-${name}.eco.html`);
