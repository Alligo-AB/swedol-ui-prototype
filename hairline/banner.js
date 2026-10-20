/**
 * Banner: a page plane with a warning banner anchored at its top edge (icon, title, text, a x) and page content
 * under it. The pointer over the x lights its tile; a press closes the banner the way the component does (fades
 * out and collapses its height, 150 ms on ease-accelerate-generic) and the page content moves up. Leaving the
 * stage, or pressing the empty page, brings it back (300 ms on ease-decelerate-generic). A drawn cursor follows
 * the pointer and rests above the x. The slider is how high the banner stands.
 */
const {
  Cam, bezier, clamp, facing, fit, poly, proj, reducedMotion, ringAt, rings, prism,
  mk, pointer, reflect, register, solid, put, disposer, spring, stepS, unproj,
} = HL;

const PW = 148, PD = 72, PT = 5, X0 = 6, X1 = 142, Y0 = 6, BH = 18, XC = 134, XY = 15;
const ARROW = [[0, 0], [0, 15], [3.6, 11.6], [6.2, 17], [8.6, 15.8], [6, 10.6], [10.8, 10.6]];
const PAGE = [[6, 0, 70, 5], [6, 11, 126, 14], [6, 18, 100, 21], [6, 28, 60, 38]]; // y0 is relative to the page top

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
  // the banner: body, left edge, icon disc, two text bars, the x tile and its two strokes; all squash toward the top with c
  const g = mk("g", {}, svg), body = solid(mk("g", {}, g)), edge = solid(mk("g", {}, g));
  body.sil.setAttribute("class", "dot"); body.sil.setAttribute("data-part", "banner");
  edge.sil.setAttribute("class", "dot"); edge.sil.setAttribute("data-part", "banner-edge");
  const icon = mk("path", { class: "dot", "data-part": "banner-edge" }, g);
  const tbar = mk("path", { class: "dot", "data-part": "bar-on" }, g), bbar = mk("path", { class: "dot", "data-part": "bar" }, g);
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
    const v = c.x, y = (o) => Y0 + o * v, z = PT + h;
    g.setAttribute("display", v < 0.02 ? "none" : "");
    const [o, i] = rings(X0, Y0, X1, y(BH), 0, 1);
    put(body, prism(P, front, o, i, PT, z));
    const [eo, ei] = rings(X0, Y0, X0 + 3, y(BH), 0, 0.6);
    put(edge, prism(P, front, eo, ei, PT, z + 0.3));
    const cy = y(BH / 2);
    icon.setAttribute("d", poly(Array.from({ length: 14 }, (_, n) => P(16 + 3 * Math.cos((n / 14) * 2 * Math.PI), cy + 3 * v * Math.sin((n / 14) * 2 * Math.PI), z + 0.3))));
    tbar.setAttribute("d", flat(24, y(5), 58, y(7.4), z + 0.3));
    bbar.setAttribute("d", flat(24, y(10.6), 100, y(12.6), z + 0.3));
    tile.setAttribute("d", clamp(hv.x, 0, 1) > 0.02 ? flat(XC - 6, y(3), XC + 6, y(15), z + 0.3) : "");
    xs.forEach((s, n) => {
      const d = 3.2, w = 0.8;
      const q = n ? [[-d, -d + w], [-d + w, -d], [d, d - w], [d - w, d]] : [[-d, d - w], [-d + w, d], [d, -d + w], [d - w, -d]];
      s.setAttribute("d", poly(q.map(([a, b]) => P(XC + a, cy + b * v, z + 0.3))));
    });
    // page content follows the banner's bottom edge
    const top = y(BH) + 8;
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
    return c.to === 1 && x > XC - 8 && x < XC + 8 && y > Y0 && y < Y0 + BH;
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
  means: "A page with a warning banner at its top: a press on the x collapses the banner, the page moves up; leaving brings it back.",
  rules: [1, 4, 8, 9],
  range: [1.5, 2.5, 4],
  tour: [[240, 215], [332, 189], [240, 215], null],
  mount,
});
