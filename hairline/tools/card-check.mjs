#!/usr/bin/env node
// Verifies a Hairline card on components-overview.html in Chrome (playwright-core from the hairline-look cache).
// Needs the repo served:  npx serve . -l 4173   (from the repo root)
// node hairline/tools/card-check.mjs <component> <outPrefix>      e.g.  switch /tmp/sw
// Writes <outPrefix>-rest.png, -hover.png (pointer over the figure), -play.png (4 s into the tour, only with data-play);
// prints: console errors, content rows (for vertical centring: want top ≈ 160 - bottom), play button state.
import { createRequire } from "node:module";
const require = createRequire(process.env.HOME + "/Library/Caches/hairline-look/");
const { chromium } = require("playwright-core");
const [comp, out = "/tmp/card"] = process.argv.slice(2);
const b = await chromium.launch({ channel: "chrome" });
const p = await b.newPage({ viewport: { width: 1300, height: 900 } });
const errs = []; p.on("console", (m) => m.type() === "error" && errs.push(m.text())); p.on("pageerror", (e) => errs.push(String(e)));
await p.goto("http://localhost:4173/eco-design-system/components-overview.html"); await p.waitForTimeout(1500);
const c = p.locator(`a.ds-card[href="components/${comp}.html"]`); await c.scrollIntoViewIfNeeded(); await p.waitForTimeout(400);
await c.screenshot({ path: `${out}-rest.png` });
const r = await c.locator("svg").boundingBox();
await p.mouse.move(r.x + r.width * 0.64, r.y + r.height * 0.49); await p.waitForTimeout(600); await c.screenshot({ path: `${out}-hover.png` });
await p.mouse.move(5, 5);
const play = c.locator(".hl-play");
if (await play.count()) { await play.click(); await p.waitForTimeout(4000); await c.screenshot({ path: `${out}-play.png` }); console.log("play pressed:", await play.getAttribute("aria-pressed"), "url:", p.url()); await play.click(); }
console.log("console errors:", JSON.stringify(errs.filter((e) => !/404/.test(e))), "(404s ignored: favicon)");
await b.close();
