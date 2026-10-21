/**
 * System Toast: the "Your changes were saved." toast floats above a slab, casting a shadow: a flat green status
 * strip, a check icon, the text and a close mark. The pointer over the close mark lights it; a press on the close mark closes
 * it: it slides out to the right and its shadow follows, then it slides back in a moment later. A drawn cursor follows
 * the pointer and rests below the toast. The slider is how high the toast floats.
 */
const {
  Cam, bezier, clamp, facing, fit, poly, proj, reducedMotion, reflect, ringAt, rings, rrect, prism,
  mk, pointer, register, solid, put, disposer, spring, stepS, unproj,
} = HL;

const PW = 120, PD = 84, PT = 6, X0 = 6, X1 = 114, Y0 = 28, Y1 = 56, PH = 2.5, REOPEN = 1100, SLIDE = 60, U = 0.42;
const ARROW = [[0, 0], [0, 15], [3.6, 11.6], [6.2, 17], [8.6, 15.8], [6, 10.6], [10.8, 10.6]];
// condensed heavy capitals as closed outlines, 8 high, v up; a second outline is the counter
const G = {
  Y: [[[0, 8], [1.7, 8], [2.5, 5], [3.3, 8], [5, 8], [3.3, 3.6], [3.3, 0], [1.7, 0], [1.7, 3.6]]],
  O: [[[0, 1.2], [1.2, 0], [3.8, 0], [5, 1.2], [5, 6.8], [3.8, 8], [1.2, 8], [0, 6.8]], [[1.6, 1.5], [3.4, 1.5], [3.4, 6.5], [1.6, 6.5]]],
  U: [[[0, 8], [1.6, 8], [1.6, 1.5], [3.4, 1.5], [3.4, 8], [5, 8], [5, 1.2], [3.8, 0], [1.2, 0], [0, 1.2]]],
  R: [[[0, 0], [1.6, 0], [1.6, 3], [2.6, 3], [3.4, 0], [5, 0], [4.2, 3.3], [5, 4.2], [5, 6.8], [3.8, 8], [0, 8]], [[1.6, 4.5], [3, 4.5], [3.4, 4.9], [3.4, 6.1], [3, 6.5], [1.6, 6.5]]],
  C: [[[0, 1.2], [1.2, 0], [3.8, 0], [5, 1.2], [5, 2.6], [3.4, 2.6], [3.4, 1.5], [1.6, 1.5], [1.6, 6.5], [3.4, 6.5], [3.4, 5.4], [5, 5.4], [5, 6.8], [3.8, 8], [1.2, 8], [0, 6.8]]],
  H: [[[0, 0], [1.6, 0], [1.6, 3.3], [3.4, 3.3], [3.4, 0], [5, 0], [5, 8], [3.4, 8], [3.4, 4.7], [1.6, 4.7], [1.6, 8], [0, 8]]],
  A: [[[0, 0], [1.6, 0], [1.9, 2.2], [3.1, 2.2], [3.4, 0], [5, 0], [3.6, 8], [1.4, 8]], [[2.2, 3.6], [2.8, 3.6], [2.5, 5.6]]],
  N: [[[0, 0], [1.6, 0], [1.6, 4.8], [3.4, 0], [5, 0], [5, 8], [3.4, 8], [3.4, 3.2], [1.6, 8], [0, 8]]],
  G: [[[0, 1.2], [1.2, 0], [3.8, 0], [5, 1.2], [5, 2.6], [3.4, 2.6], [3.4, 1.5], [1.6, 1.5], [1.6, 6.5], [3.4, 6.5], [3.4, 4.8], [2.4, 4.8], [2.4, 3.3], [5, 3.3], [5, 6.8], [3.8, 8], [1.2, 8], [0, 6.8]]],
  E: [[[0, 0], [5, 0], [5, 1.5], [1.6, 1.5], [1.6, 3.3], [4.4, 3.3], [4.4, 4.7], [1.6, 4.7], [1.6, 6.5], [5, 6.5], [5, 8], [0, 8]]],
  S: [[[0, 1.2], [1.2, 0], [3.8, 0], [5, 1.2], [5, 3.6], [3.8, 4.4], [1.6, 4.9], [1.6, 6.5], [5, 6.5], [5, 8], [1.2, 8], [0, 6.8], [0, 4.2], [1.2, 3.4], [3.4, 2.9], [3.4, 1.5], [0, 1.5]]],
  W: [[[0, 8], [1.6, 8], [1.6, 3], [3, 6], [4.4, 3], [4.4, 8], [6, 8], [6, 0], [4.2, 0], [3, 2.8], [1.8, 0], [0, 0]]],
  V: [[[0, 8], [1.7, 8], [2.5, 2.4], [3.3, 8], [5, 8], [3.3, 0], [1.7, 0]]],
  D: [[[0, 0], [3.8, 0], [5, 1.2], [5, 6.8], [3.8, 8], [0, 8]], [[1.6, 1.5], [3.2, 1.5], [3.4, 1.7], [3.4, 6.3], [3.2, 6.5], [1.6, 6.5]]],
  ".": [[[0, 0], [1.6, 0], [1.6, 1.6], [0, 1.6]]],
  " ": [],
};
const GW = (ch) => (ch === " " ? 2.4 : Math.max(...G[ch][0].map((q) => q[0])));
/** A string as flat world outlines, left edge x0, vertical middle ym. */
function label(text, x0, ym, u) {
  let x = x0;
  const out = [];
  for (const ch of text) {
    G[ch].forEach((o, k) => { const q = o.map(([a, v]) => [x + a * u, ym + (4 - v) * u]); out.push(k ? q.reverse() : q); });
    x += (GW(ch) + 1.2) * u;
  }
  return out;
}
const flat = (P, outs, z) => outs.map((o) => poly(o.map(([x, y]) => P(x, y, z)))).join("");
const rect = (P, x0, y0, x1, y1, z) => poly([P(x0, y0, z), P(x1, y0, z), P(x1, y1, z), P(x0, y1, z)]);
const cross = (cx, cy, r, w) => [[[cx - r, cy - r + w], [cx - r + w, cy - r], [cx + r, cy + r - w], [cx + r - w, cy + r]], [[cx + r - w, cy - r], [cx + r, cy - r + w], [cx - r + w, cy + r], [cx - r, cy + r - w]]];
const TICK = [[-4.4, 0.3], [-3, -1.1], [-1.2, 0.7], [3, -3.8], [4.4, -2.4], [-1.2, 3.4]];

function mount({ stage, svg, read }, value) {
  const bag = disposer();
  let lift = value;

  const C = Cam(45, 0.5, 1.9);
  fit(C, [[0, 0, 0], [PW, PD, 0], [PW, 0, 0], [0, PD, 0], [X1 + 20, Y0, PT + 16 + PH]], 200, 172);
  const P = proj(C), front = facing(C);

  const [pOut, pIn] = rings(0, 0, PW, PD, 0, 1.6);
  if (stage.hasAttribute("data-flat")) {
    const sl = solid(mk("g", {}, svg));
    sl.sil.setAttribute("class", "sil"); sl.sil.setAttribute("data-part", "slab");
    sl.sil.setAttribute("d", poly(ringAt(P, pOut, PT))); sl.cr.setAttribute("d", poly(ringAt(P, pIn, PT)));
  } else {
    reflect(svg, mk("g", {}, svg), P, front, pOut, 0, 14);
    put(solid(mk("g", {}, svg)), prism(P, front, pOut, pIn, 0, PT));
    svg.lastChild.firstChild.setAttribute("class", "sil");
  }

  const shadow = mk("path", { class: "dot", "data-part": "tshadow" }, svg);
  const mg = mk("g", {}, svg);
  const [qOut, qIn] = rings(X0, Y0, X1, Y1, 0, 1.2);
  const panel = solid(mg);
  const part = (p) => mk("path", { class: "dot", "data-part": p }, mg);
  const hi = part("rowhi"), strip = part("status"), icon = part("icon"), tick = part("tick"), text = part("bar-on"), x = part("bar-on");

  // the toast slides in from the right (decelerate-emphasized, 300ms) and out again (accelerate-generic, 150ms)
  const q = { x: 1, t: 1, to: 1, from: 1, t0: 0, d: 300, e: null };
  const ez = { in: bezier(0.16, 0, 0.16, 1), out: bezier(0.36, 0.09, 1, 0.58) };
  const slide = (now) => {
    if (q.t !== q.to) { q.from = q.x; q.to = q.t; q.t0 = now; q.d = q.t ? 300 : 150; q.e = q.t ? ez.in : ez.out; }
    if (q.x === q.to) return false;
    q.x = reducedMotion() ? q.to : q.from + (q.to - q.from) * q.e(clamp((now - q.t0) / q.d, 0, 1));
    return q.x !== q.to;
  };
  let closedAt = 0, act = -1, last = "";
  const cy = (Y0 + Y1) / 2;
  function draw(force) {
    const m = clamp(q.x, 0, 1), z0 = PT + 0.4 + (lift - 0.4) * Math.min(1, m * 1.5), zt = z0 + PH, dx = (1 - m) * SLIDE;
    const key = m.toFixed(3) + z0.toFixed(2) + act;
    if (!force && key === last) return;
    last = key;
    const show = m > 0.01;
    shadow.setAttribute("display", show ? "inline" : "none"); mg.setAttribute("display", show ? "inline" : "none");
    if (!show) return;
    const sh = (z0 - PT) * 0.45, s = (r) => r.map((p) => ({ ...p, u: p.u + dx })), z = zt + 0.1, cx = X0 + dx + 17;
    shadow.setAttribute("d", rect(P, X0 + dx + sh, Y0 + sh, X1 + dx + sh, Y1 + sh, PT + 0.1));
    put(panel, prism(P, front, s(qOut), s(qIn), z0, zt));
    strip.setAttribute("d", rect(P, X0 + dx, Y0, X0 + dx + 2.4, Y1, z)); // flat on the top, not a wall
    icon.setAttribute("d", poly(ringAt(P, rrect(cx - 7, cy - 7, cx + 7, cy + 7, 7, 14), z)));
    tick.setAttribute("d", poly(TICK.map(([u, v]) => P(cx + u * 0.9, cy + v * 0.9, z + 0.05))));
    text.setAttribute("d", flat(P, label("YOUR CHANGES WERE SAVED.", X0 + dx + 32, cy, U), z));
    hi.setAttribute("d", rect(P, X1 - 17 + dx, cy - 7, X1 - 3 + dx, cy + 7, zt + 0.05)); hi.setAttribute("display", act >= 0 ? "inline" : "none");
    x.setAttribute("d", flat(P, cross(X1 - 10 + dx, cy, 3.4, 1.4), z));
  }

  const rest = P(X1 - 30, Y1 + 14, PT + 1);
  const ax = spring(rest[0], { k: 140 }), ay = spring(rest[1], { k: 140 }), pr = spring(0);
  const halo = mk("path", { class: "fo" }, svg), cur = mk("path", { class: "dot", "data-part": "cursor" }, svg);
  const drawCur = () => {
    const px = ax.x - 0.5, py = ay.x + 2.5 * clamp(pr.x, 0, 1);
    cur.setAttribute("d", poly(ARROW.map(([u, v]) => [px + u, py + v])));
    halo.setAttribute("d", [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]].map(([i, j]) => poly(ARROW.map(([u, v]) => [px + u + i * 0.8, py + v + j * 0.8]))).join(""));
  };

  const setOpen = (v, now) => { q.t = v; closedAt = now; };
  let ghost = false, gt = 0, gdone = true;
  const press = () => { setOpen(0, performance.now()); pr.x = 1; pr.t = 0; say(); A.wake(); };
  const A = register(stage, (dt, now) => {
    let m = slide(now);
    if (ghost && act >= 0 && !gdone) { m = true; if (now - gt > 200) { gdone = true; press(); } }
    if (!q.t) { m = true; if (now - closedAt > REOPEN) setOpen(1, now); }
    for (const s of [ax, ay, pr]) if (stepS(s, dt)) m = true;
    draw(); drawCur();
    return m;
  });
  bag.add(A.unregister);

  // hit: the toast's resting top plane
  const pick = ([sx, sy]) => {
    if (!q.t) return -1;
    const [px, py] = unproj(C, sx, sy, PT + lift + PH);
    return px > X1 - 18 && px < X1 - 2 && py > cy - 8 && py < cy + 8 ? 0 : -1; // only the close mark answers
  };
  const say = () => { read.textContent = !q.t ? "closed" : act < 0 ? "open" : "close"; };
  function set(a, p) {
    if (a !== act) { act = a; gdone = !ghost; gt = performance.now(); say(); }
    if (p) { ax.t = p[0]; ay.t = p[1]; } else { ax.t = rest[0]; ay.t = rest[1]; }
    A.wake();
  }
  bag.add(pointer(stage, {
    move: (p, e) => { ghost = e?.pointerType === "ghost"; set(pick(p), p); gt = performance.now(); },
    down: (p) => { const a = pick(p); ghost = false; set(a, p); if (a >= 0) press(); },
    leave: () => { ghost = false; set(-1); }, // a closed toast reopens on its own timer
  }));
  bag.add(() => svg.replaceChildren());

  draw(true); drawCur();
  return { set: (v) => { lift = v; draw(true); }, destroy: bag.dispose };
}

hairline({
  name: "toast",
  means: "The saved toast floating over a slab: a press on its close mark closes it, it slides out to the right, then back in.",
  rules: [1, 4, 8, 9],
  range: [6, 12, 16],
  tour: [[259, 168], null, [259, 168], null],
  mount,
});
