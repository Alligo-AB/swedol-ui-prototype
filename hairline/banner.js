/**
 * Banner: a page plane with a large informational banner anchored at its top edge (a ring icon, heading, two text lines, an action label, a x) and page content
 * under it. The pointer over the x lights its tile; a press closes the banner the way the component does (fades
 * out and slides it up off the page, 150 ms on ease-accelerate-generic) and the page content moves up. Leaving the
 * stage, or pressing the empty page, brings it back (300 ms on ease-decelerate-generic). A drawn cursor follows
 * the pointer and rests above the x. The slider is how high the banner stands.
 */
const {
  Cam, bezier, clamp, facing, fit, poly, proj, reducedMotion, ringAt, rings, prism,
  mk, pointer, reflect, register, solid, put, disposer, spring, stepS, unproj,
} = HL;

const PW = 148, PD = 84, PT = 5, X0 = 6, X1 = 142, Y0 = 6, BH = 37, XC = 134, XY = 8;
const ARROW = [[0, 0], [0, 15], [3.6, 11.6], [6.2, 17], [8.6, 15.8], [6, 10.6], [10.8, 10.6]];
// condensed heavy capitals as closed outlines (from tabs.js), 8 high, u right, v up
const G = {
  P: [[[0, 0], [1.6, 0], [1.6, 3], [3.8, 3], [5, 4.2], [5, 6.8], [3.8, 8], [0, 8]], [[1.6, 4.5], [3, 4.5], [3.4, 4.9], [3.4, 6.1], [3, 6.5], [1.6, 6.5]]],
  A: [[[0, 0], [1.6, 0], [1.9, 2.2], [3.1, 2.2], [3.4, 0], [5, 0], [3.6, 8], [1.4, 8]], [[2.2, 3.6], [2.8, 3.6], [2.5, 5.6]]],
  E: [[[0, 0], [5, 0], [5, 1.5], [1.6, 1.5], [1.6, 3.3], [4.4, 3.3], [4.4, 4.7], [1.6, 4.7], [1.6, 6.5], [5, 6.5], [5, 8], [0, 8]]],
  R: [[[0, 0], [1.6, 0], [1.6, 3], [2.6, 3], [3.4, 0], [5, 0], [4.2, 3.3], [5, 4.2], [5, 6.8], [3.8, 8], [0, 8]], [[1.6, 4.5], [3, 4.5], [3.4, 4.9], [3.4, 6.1], [3, 6.5], [1.6, 6.5]]],
  L: [[[0, 0], [5, 0], [5, 1.5], [1.6, 1.5], [1.6, 8], [0, 8]]],
  S: [[[0, 1.2], [1.2, 0], [3.8, 0], [5, 1.2], [5, 3.6], [3.8, 4.4], [1.6, 4.9], [1.6, 6.5], [5, 6.5], [5, 8], [1.2, 8], [0, 6.8], [0, 4.2], [1.2, 3.4], [3.4, 2.9], [3.4, 1.5], [0, 1.5]]],
  I: [[[0, 0], [1.6, 0], [1.6, 8], [0, 8]]],
  V: [[[0, 8], [1.7, 8], [2.5, 2.6], [3.3, 8], [5, 8], [3.3, 0], [1.7, 0]]],
  O: [[[0, 1.2], [1.2, 0], [3.8, 0], [5, 1.2], [5, 6.8], [3.8, 8], [1.2, 8], [0, 6.8]], [[1.6, 1.5], [3.4, 1.5], [3.4, 6.5], [1.6, 6.5]]],
  D: [[[0, 0], [3.8, 0], [5, 1.2], [5, 6.8], [3.8, 8], [0, 8]], [[1.6, 1.5], [3.2, 1.5], [3.4, 1.7], [3.4, 6.3], [3.2, 6.5], [1.6, 6.5]]],
  T: [[[1.7, 0], [3.3, 0], [3.3, 6.5], [5, 6.5], [5, 8], [0, 8], [0, 6.5], [1.7, 6.5]]],
  N: [[[0, 0], [1.6, 0], [1.6, 4.8], [3.4, 0], [5, 0], [5, 8], [3.4, 8], [3.4, 3.2], [1.6, 8], [0, 8]]],
  C: [[[0, 1.2], [1.2, 0], [3.8, 0], [5, 1.2], [5, 2.6], [3.4, 2.6], [3.4, 1.5], [1.6, 1.5], [1.6, 6.5], [3.4, 6.5], [3.4, 5.4], [5, 5.4], [5, 6.8], [3.8, 8], [1.2, 8], [0, 6.8]]],
  M: [[[0, 0], [1.6, 0], [1.6, 5], [3, 2], [4.4, 5], [4.4, 0], [6, 0], [6, 8], [4.2, 8], [3, 5.2], [1.8, 8], [0, 8]]],
};
const GW = (ch) => Math.max(...G[ch][0].map((q) => q[0]));
/** Text as flat world outlines: x0, top y0, scale u, y squash q; a counter is wound the other way so a fill leaves it open. */
function label(text, x0, y0, u, q) {
  let x = x0;
  const out = [];
  for (const ch of text) {
    if (ch === " ") { x += 3 * u; continue; }
    G[ch].forEach((o, k) => { const w = o.map(([a, b]) => [x + a * u, y0 + (8 - b) * u * q]); out.push(k ? w.reverse() : w); });
    x += (GW(ch) + 1.2) * u;
  }
  return out;
}
const PAGE = [[6, 0, 70, 4], [6, 9, 126, 11.5], [6, 14, 100, 16.5], [6, 22, 60, 31]]; // y0 is relative to the page top

function mount({ stage, svg, read }, value) {
  const bag = disposer();
  let h = value;

  const C = Cam(45, 0.5, 2.3);
  fit(C, [[0, 0, 0], [PW, PD, 0], [PW, 0, 0], [0, PD, 0], [XC, 8, PT + 9]], 200, 172);
  const P = proj(C), front = facing(C);

  const [pOut, pIn] = rings(0, 0, PW, PD, 0, 1.6);
  if (stage.hasAttribute("data-flat")) {
    // a flat slab: no thickness, no reflection, only the top plane (its fill can be made see-through in CSS via data-part="slab")
    const sl = solid(mk("g", {}, svg));
    sl.sil.setAttribute("class", "sil"); sl.sil.setAttribute("data-part", "slab");
    sl.sil.setAttribute("d", poly(ringAt(P, pOut, PT))); sl.cr.setAttribute("d", poly(ringAt(P, pIn, PT)));
  } else {
    reflect(svg, mk("g", {}, svg), P, front, pOut, 0, 14);
    put(solid(mk("g", {}, svg)), prism(P, front, pOut, pIn, 0, PT));
    svg.lastChild.firstChild.setAttribute("class", "sil");
  }

  const flat = (x0, y0, x1, y1, z) => poly([[x0, y0], [x1, y0], [x1, y1], [x0, y1]].map(([x, y]) => P(x, y, z)));
  const page = PAGE.map(([x0, y0, x1, y1], i) => ({ x0, y0, x1, y1, el: mk("path", { class: "dot", "data-part": i === 0 ? "title" : i === 3 ? "card" : "line" }, svg) }));
  // the banner: body, left edge, icon disc, two text bars, the x tile and its two strokes; all pushed up and off the page with c
  const g = mk("g", {}, svg), body = solid(mk("g", {}, g));
  body.sil.setAttribute("class", "dot"); body.sil.setAttribute("data-part", "banner");
  const edge = mk("path", { class: "dot", "data-part": "banner-edge" }, g); // the left border: flat, level with the banner top
  const icon = mk("path", { class: "dot", "data-part": "banner-edge" }, g), leaf = mk("path", { class: "dot", "data-part": "banner-edge" }, g);
  const txt = [mk("path", { class: "dot", "data-part": "bar-on" }, g), mk("path", { class: "dot", "data-part": "bar-on" }, g), mk("path", { class: "dot", "data-part": "bar-on" }, g), mk("path", { class: "dot", "data-part": "bar-on" }, g)];
  const tile = mk("path", { class: "dot", "data-part": "halo" }, g);
  const xs = [1, -1].map(() => mk("path", { class: "dot", "data-part": "bar-on" }, g));

  const c = { x: 1, f: 1, to: 1, t0: 0, on: false };
  const ezIn = bezier(0.36, 0.09, 1, 0.58), ezOut = bezier(0.16, 0.38, 0.58, 1); // close: accelerate 150 ms; open: decelerate 300 ms
  const go = (to) => { if (c.to === to) return; Object.assign(c, { f: c.x, to, t0: performance.now(), on: true }); A.wake(); };
  const slide = (now) => {
    if (!c.on) return false;
    const k = reducedMotion() ? 1 : clamp((now - c.t0) / (c.to ? 300 : 150), 0, 1);
    c.x = c.f + (c.to - c.f) * (c.to ? ezOut : ezIn)(k);
    if (k >= 1) { c.x = c.to; c.on = false; }
    return c.on;
  };

  let key = "";
  const hv = spring(0);
  function draw(force) {
    const k = c.x.toFixed(3) + h + hv.x.toFixed(2);
    if (!force && k === key) return;
    key = k;
    const v = 1, off = -(1 - c.x) * (BH + Y0 + 8), y = (o) => Y0 + o + off, z = PT + h; // closing pushes the banner off the page, up past its top edge
    g.setAttribute("display", c.x < 0.02 ? "none" : "");
    const [o, i] = rings(X0, Y0, X1, y(BH), 0, 1);
    put(body, prism(P, front, o, i, PT, z));
    edge.setAttribute("d", flat(X0, Y0, X0 + 4, y(BH), z + 0.1));
    const cy = y(8);
    // the icon: a ring and, inside it, a leaf outline with a vein that runs on as a stem (outlines wound the other way leave holes)
    const IX = 22, IY = y(11), at = (a, b) => P(IX + a, IY + b * v, z + 0.3);
    const circ = (rad, up) => { const a = Array.from({ length: 24 }, (_, n) => at(rad * Math.cos((n / 24) * 2 * Math.PI), rad * Math.sin((n / 24) * 2 * Math.PI))); return up ? a : a.reverse(); };
    const lens = (bulge, up) => { const a = Array.from({ length: 13 }, (_, n) => { const t = n / 12, w = bulge * Math.sin(Math.PI * t); return at(-3.6 + 7.2 * t + w * 0.707, 3.6 - 7.2 * t + w * 0.707); }).concat(Array.from({ length: 11 }, (_, n) => { const t = 1 - (n + 1) / 12, w = bulge * Math.sin(Math.PI * t); return at(-3.6 + 7.2 * t - w * 0.707, 3.6 - 7.2 * t - w * 0.707); })); return up ? a : a.reverse(); };
    icon.setAttribute("d", poly(circ(7.6, 1)) + poly(circ(5.9, 0)));
    leaf.setAttribute("d", poly(lens(3.3, 1)) + poly(lens(1.9, 0)) + poly([[-4.4, 4.4], [-3.6, 4.4 + 0.1], [3.2, -2.4], [2.5, -3.1], [-4.3, 3.7]].map(([a, b]) => at(a, b))));
    txt[0].setAttribute("d", label("PAPERLESS", 38, y(3), 0.62, v).map((o) => poly(o.map(([x, yy]) => P(x, yy, z + 0.3)))).join(""));
    txt[1].setAttribute("d", label("INVOICES ARE SENT", 38, y(13.2), 0.42, v).map((o) => poly(o.map(([x, yy]) => P(x, yy, z + 0.3)))).join(""));
    txt[2].setAttribute("d", label("VIA EMAIL", 38, y(19.2), 0.42, v).map((o) => poly(o.map(([x, yy]) => P(x, yy, z + 0.3)))).join(""));
    txt[3].setAttribute("d", label("READ MORE", 40, y(28), 0.45, v).map((o) => poly(o.map(([x, yy]) => P(x, yy, z + 0.3)))).join(""));
    tile.setAttribute("d", clamp(hv.x, 0, 1) > 0.02 ? flat(XC - 6, y(2), XC + 6, y(14), z + 0.3) : "");
    xs.forEach((s, n) => {
      const d = 3.2, w = 0.8;
      const q = n ? [[-d, -d + w], [-d + w, -d], [d, d - w], [d - w, d]] : [[-d, d - w], [-d + w, d], [d, -d + w], [d - w, -d]];
      s.setAttribute("d", poly(q.map(([a, b]) => P(XC + a, cy + b * v, z + 0.3))));
    });
    // page content follows the banner's bottom edge
    const top = Y0 + BH * c.x + 8; // the space under the banner collapses with it
    for (const p of page) p.el.setAttribute("d", flat(p.x0, top + p.y0, p.x1, top + p.y1, PT));
  }

  // the cursor: tip at (ax, ay) on screen, pressed down by pr; rests above the x
  const rest = P(XC, XY, PT + 9);
  const ax = spring(rest[0], { k: 140 }), ay = spring(rest[1], { k: 140 }), pr = spring(0);
  const cur = mk("path", { class: "dot", "data-part": "cursor" }, svg);
  const drawCur = () => cur.setAttribute("d", poly(ARROW.map(([u, v]) => [ax.x + u - 0.5, ay.x + v + 2.5 * clamp(pr.x, 0, 1)])));

  let ghost = false, gt = 0, gdone = true, hot = false;
  const A = register(stage, (dt, now) => {
    let m = false;
    if (ghost && hot && !gdone) { m = true; if (now - gt > 250) { gdone = true; press(); } }
    if (slide(now)) m = true;
    for (const q of [hv, ax, ay, pr]) if (stepS(q, dt)) m = true;
    draw(); drawCur();
    return m;
  });
  bag.add(A.unregister);

  const lit = () => { if (hot) tile.setAttribute("data-hover", ""); else tile.removeAttribute("data-hover"); };
  const say = () => { lit(); read.textContent = c.to ? (hot ? "dismiss" : "rest") : "closed"; };
  // hit: the x's tile while the banner is open
  const pick = ([sx, sy]) => {
    const [x, y] = unproj(C, sx, sy, PT + h);
    return c.to === 1 && x > XC - 8 && x < XC + 8 && y > Y0 && y < Y0 + 16;
  };
  function press() { go(0); pr.x = 1; pr.t = 0; hot = false; hv.t = 0; say(); A.wake(); }
  function set(on, p) {
    if (on !== hot) { hot = on; hv.t = on ? 1 : 0; gdone = !ghost; gt = performance.now(); say(); }
    if (on) { ax.t = p[0]; ay.t = p[1]; } else if (c.to) { ax.t = rest[0]; ay.t = rest[1]; } else { ax.t = p[0]; ay.t = p[1]; }
    A.wake();
  }
  bag.add(pointer(stage, {
    move: (p, e) => { ghost = e?.pointerType === "ghost"; set(pick(p), p); gt = performance.now(); },
    down: (p) => { ghost = false; if (pick(p)) { set(true, p); press(); } else if (!c.to) { go(1); say(); } },
    leave: () => { ghost = false; hot = false; hv.t = 0; go(1); ax.t = rest[0]; ay.t = rest[1]; say(); A.wake(); },
  }));
  bag.add(() => svg.replaceChildren());

  draw(true); drawCur();
  return { set: (v) => { h = v; draw(true); }, destroy: bag.dispose };
}

hairline({
  name: "banner",
  means: "A page with a banner at its top: a press on the x pushes the banner off the page, the content moves up; leaving brings it back.",
  rules: [1, 4, 8, 9],
  range: [1.5, 2.5, 4],
  tour: [[240, 215], [353, 178], [240, 215], null],
  mount,
});
