/**
 * Tabs: a Primary tab bar on a slab, OVERVIEW active, DETAILS and REVIEWS beside it. The pointer over a tab greys
 * its label and grows a light line under it; a press slides the black active line to that tab (the component's
 * 300 ms on ease-standard). A drawn cursor follows the pointer and rests above the active tab. The slider is how
 * high the lines stand.
 */
const {
  Cam, bezier, clamp, facing, fit, lerp, poly, proj, reducedMotion, ringAt, rings, prism,
  mk, pointer, reflect, register, solid, put, disposer, spring, stepS, unproj,
} = HL;

const PW = 148, PD = 46, PT = 5, U = 0.58, GAP = 8, YM = 20, LY0 = 30.2, LY1 = 33.4;
const NAMES = ["OVERVIEW", "DETAILS", "REVIEWS", "SUPPORT"];
const ARROW = [[0, 0], [0, 15], [3.6, 11.6], [6.2, 17], [8.6, 15.8], [6, 10.6], [10.8, 10.6]];
// condensed heavy capitals as closed outlines (Breuer-like), 8 high, u right, v up; the second outline, when there is one, is the counter
const G = {
  R: [[[0, 0], [1.6, 0], [1.6, 3], [2.6, 3], [3.4, 0], [5, 0], [4.2, 3.3], [5, 4.2], [5, 6.8], [3.8, 8], [0, 8]], [[1.6, 4.5], [3, 4.5], [3.4, 4.9], [3.4, 6.1], [3, 6.5], [1.6, 6.5]]],
  I: [[[0, 0], [1.6, 0], [1.6, 8], [0, 8]]],
  A: [[[0, 0], [1.6, 0], [1.9, 2.2], [3.1, 2.2], [3.4, 0], [5, 0], [3.6, 8], [1.4, 8]], [[2.2, 3.6], [2.8, 3.6], [2.5, 5.6]]],
  S: [[[0, 1.2], [1.2, 0], [3.8, 0], [5, 1.2], [5, 3.6], [3.8, 4.4], [1.6, 4.9], [1.6, 6.5], [5, 6.5], [5, 8], [1.2, 8], [0, 6.8], [0, 4.2], [1.2, 3.4], [3.4, 2.9], [3.4, 1.5], [0, 1.5]]],
  E: [[[0, 0], [5, 0], [5, 1.5], [1.6, 1.5], [1.6, 3.3], [4.4, 3.3], [4.4, 4.7], [1.6, 4.7], [1.6, 6.5], [5, 6.5], [5, 8], [0, 8]]],
  O: [[[0, 1.2], [1.2, 0], [3.8, 0], [5, 1.2], [5, 6.8], [3.8, 8], [1.2, 8], [0, 6.8]], [[1.6, 1.5], [3.4, 1.5], [3.4, 6.5], [1.6, 6.5]]],
  D: [[[0, 0], [3.8, 0], [5, 1.2], [5, 6.8], [3.8, 8], [0, 8]], [[1.6, 1.5], [3.2, 1.5], [3.4, 1.7], [3.4, 6.3], [3.2, 6.5], [1.6, 6.5]]],
  T: [[[1.7, 0], [3.3, 0], [3.3, 6.5], [5, 6.5], [5, 8], [0, 8], [0, 6.5], [1.7, 6.5]]],
  W: [[[0, 8], [1.6, 8], [1.6, 3], [3, 6], [4.4, 3], [4.4, 8], [6, 8], [6, 0], [4.2, 0], [3, 2.8], [1.8, 0], [0, 0]]],
  L: [[[0, 0], [5, 0], [5, 1.5], [1.6, 1.5], [1.6, 8], [0, 8]]],
  U: [[[0, 0], [5, 0], [5, 8], [3.4, 8], [3.4, 1.5], [1.6, 1.5], [1.6, 8], [0, 8]]],
  P: [[[0, 0], [1.6, 0], [1.6, 3], [3.8, 3], [5, 4.2], [5, 6.8], [3.8, 8], [0, 8]], [[1.6, 4.5], [3, 4.5], [3.4, 4.9], [3.4, 6.1], [3, 6.5], [1.6, 6.5]]],
  V: [[[0, 8], [1.7, 8], [2.5, 2.6], [3.3, 8], [5, 8], [3.3, 0], [1.7, 0]]],
};
const GW = (ch) => Math.max(...G[ch][0].map((q) => q[0]));
const ADV = 1.2, WID = (t) => [...t].reduce((s, ch) => s + GW(ch) + ADV, -ADV) * U;

/** The label as flat world outlines from x0, centred on YM; a counter is wound the other way so a fill leaves it open. */
function label(text, x0) {
  let x = x0;
  const out = [];
  for (const ch of text) {
    G[ch].forEach((o, k) => { const q = o.map(([u, v]) => [x + u * U, YM + (4 - v) * U]); out.push(k ? q.reverse() : q); });
    x += (GW(ch) + ADV) * U;
  }
  return out;
}
const EX = { REVIEWS: 7 }; // a count badge after the label
const TW = (n) => WID(n) + (EX[n] || 0);
const TOTAL = NAMES.reduce((s, n) => s + TW(n), 0) + GAP * (NAMES.length - 1);
const TABS = (() => { let x = (PW - TOTAL) / 2; return NAMES.map((n) => { const t = { name: n.toLowerCase(), text: n, x0: x, x1: x + TW(n) }; x = t.x1 + GAP; return t; }); })();

function mount({ stage, svg, read }, value) {
  const bag = disposer();
  let h = value;

  const C = Cam(45, 0.5, 2.3);
  fit(C, [[0, 0, 0], [PW, PD, 0], [PW, 0, 0], [0, PD, 0], [PW / 2, 4, PT + 9]], 200, 172);
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

  // the bar's divider: a thin flat strip across the slab
  mk("path", { d: poly(ringAt(P, rings(8, LY0 + 1.2, PW - 8, LY1 - 1.2, 0, 0.4)[0], PT)), class: "dot", "data-part": "line" }, svg);

  const tabs = TABS.map((t) => {
    const [out, inn] = rings(t.x0, LY0, t.x1, LY1, 0, 0.9);
    const g = mk("g", {}, svg), bar = solid(g);
    bar.sil.setAttribute("class", "dot"); bar.sil.setAttribute("data-part", "bar-hover");
    const text = mk("path", { class: "dot", "data-part": "label", d: label(t.text, t.x0).map((s) => poly(s.map(([x, y]) => P(x, y, PT)))).join("") }, svg);
    if (EX[t.text]) { // the count badge: a flat red disc
      const d = Array.from({ length: 14 }, (_, i) => [t.x1 - 2.5 + 2.5 * Math.cos((i / 14) * 2 * Math.PI), YM + 2.5 * Math.sin((i / 14) * 2 * Math.PI)]);
      mk("path", { d: poly(d.map(([x, y]) => P(x, y, PT))), class: "dot", "data-part": "count" }, svg);
    }
    return { ...t, out, inn, g, bar, text, hv: spring(0), last: -1 };
  });
  // the active line: one black bar that slides between the tabs (x0 and width interpolated)
  const act = mk("g", {}, svg), abar = solid(act);
  abar.sil.setAttribute("class", "dot"); abar.sil.setAttribute("data-part", "bar");
  let cur = 0;
  const sl = { x0: TABS[0].x0, x1: TABS[0].x1, f0: 0, f1: 0, t0: 0, to: 0, on: false, t: 0 };
  const ez = bezier(0.35, 0, 0.35, 1);
  const slide = (now) => {
    if (!sl.on) return false;
    const k = reducedMotion() ? 1 : ez(clamp((now - sl.t0) / 300, 0, 1));
    sl.x0 = lerp(sl.f0, TABS[sl.to].x0, k); sl.x1 = lerp(sl.f1, TABS[sl.to].x1, k);
    if (k >= 1) sl.on = false;
    return sl.on;
  };
  const go = (a) => { if (a === cur) return; cur = a; Object.assign(sl, { f0: sl.x0, f1: sl.x1, t0: performance.now(), to: a, on: true }); };

  let key = "";
  function draw(force) {
    const k = sl.x0.toFixed(2) + sl.x1.toFixed(2) + h + tabs.map((t) => t.hv.x.toFixed(2)).join();
    if (!force && k === key) return;
    key = k;
    for (const t of tabs) {
      const v = clamp(t.hv.x, 0, 1);
      t.g.setAttribute("display", v < 0.03 ? "none" : "");
      if (v >= 0.03) put(t.bar, prism(P, front, t.out, t.inn, PT, PT + h * v));
    }
    const [o, i] = rings(sl.x0, LY0, sl.x1, LY1, 0, 0.9);
    put(abar, prism(P, front, o, i, PT, PT + h));
  }

  // the cursor: tip at (ax, ay) on screen, pressed down by pr; rests above the active tab
  const restFor = (a) => P((TABS[a].x0 + TABS[a].x1) / 2, 8, PT + 9);
  let rest = restFor(0);
  const ax = spring(rest[0], { k: 140 }), ay = spring(rest[1], { k: 140 }), pr = spring(0);
  const curs = mk("path", { class: "dot", "data-part": "cursor" }, svg);
  const drawCur = () => curs.setAttribute("d", poly(ARROW.map(([u, v]) => [ax.x + u - 0.5, ay.x + v + 2.5 * clamp(pr.x, 0, 1)])));

  let ghost = false, gt = 0, gdone = true, hov = -1;
  const A = register(stage, (dt, now) => {
    let m = false;
    if (ghost && hov >= 0 && !gdone) { m = true; if (now - gt > 250) { gdone = true; press(hov); } }
    if (slide(now)) m = true;
    for (const t of tabs) if (stepS(t.hv, dt)) m = true;
    for (const q of [ax, ay, pr]) if (stepS(q, dt)) m = true;
    draw(); drawCur();
    return m;
  });
  bag.add(A.unregister);

  const say = () => { read.textContent = hov < 0 ? "rest" : tabs[hov].name + (hov === cur ? " active" : ""); };
  // hit: the tab's label with a little air, over the whole bar height
  const pick = ([sx, sy]) => {
    const [x, y] = unproj(C, sx, sy, PT);
    if (y < YM - 10 || y > LY1 + 5) return -1;
    return tabs.findIndex((t) => x > t.x0 - GAP / 2 && x < t.x1 + GAP / 2);
  };
  const paint = () => tabs.forEach((t, i) => t.text.setAttribute("data-part", i === hov && i !== cur ? "label-hover" : "label"));
  function press(a) { go(a); pr.x = 1; pr.t = 0; hov = a; hover(a); A.wake(); }
  function hover(a) { hov = a; tabs.forEach((t, i) => { t.hv.t = i === a && i !== cur ? 1 : 0; }); paint(); say(); }
  function set(a, p) {
    if (a !== hov) { hover(a); gdone = !ghost; gt = performance.now(); }
    rest = restFor(cur);
    if (a < 0) { ax.t = rest[0]; ay.t = rest[1]; } else { ax.t = p[0]; ay.t = p[1]; }
    A.wake();
  }
  bag.add(pointer(stage, {
    move: (p, e) => { ghost = e?.pointerType === "ghost"; set(pick(p), p); gt = performance.now(); },
    down: (p) => { const a = pick(p); set(a, p); ghost = false; if (a >= 0) press(a); },
    leave: (e) => {
      if (e?.pointerType === "ghost") go(0);
      ghost = false; hov = -2; set(-1);
    },
  }));
  bag.add(() => svg.replaceChildren());

  draw(true); drawCur();
  return { set: (v) => { h = v; draw(true); }, destroy: bag.dispose };
}

hairline({
  name: "tabs",
  means: "A tab bar on a slab, Overview active: the pointer greys a tab and grows a light line under it, a press slides the black active line over.",
  rules: [1, 4, 8, 9],
  range: [1.5, 2.5, 4],
  tour: [[176, 145], [231, 173], [288, 201], null],
  mount,
});
