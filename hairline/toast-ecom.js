/**
 * E-Com Toast: the "added to cart" toast floats above a slab, casting a shadow: a product tile, a bold name, a line of
 * text, a close mark, a blank and a primary button. The pointer over a button sinks it; a press closes the toast (it
 * slides out and its shadow follows) and it slides back in a moment later. A drawn cursor follows the pointer and rests
 * beside the primary button. The slider is how high the toast floats.
 */
const {
  Cam, bezier, clamp, facing, fit, poly, proj, reducedMotion, reflect, ringAt, rings, prism,
  mk, pointer, register, solid, put, disposer, spring, stepS, unproj,
} = HL;

const PW = 96, PD = 100, PT = 6, X0 = 6, X1 = 90, Y0 = 26, Y1 = 74, PH = 2.5, BH = 1.6, REOPEN = 1100;
const BTN = [{ name: "choose accessories", text: "CHOOSE ACCESSORIES", x0: 10, x1: 50, y0: 52, y1: 66, u: 0.34 }, { name: "go to cart", text: "GO TO CART", x0: 54, x1: 86, y0: 52, y1: 66, u: 0.42 }];
const ARROW = [[0, 0], [0, 15], [3.6, 11.6], [6.2, 17], [8.6, 15.8], [6, 10.6], [10.8, 10.6]];
const G = {
  P: [[[0, 0], [1.6, 0], [1.6, 3], [3.8, 3], [5, 4.2], [5, 6.8], [3.8, 8], [0, 8]], [[1.6, 4.5], [3, 4.5], [3.4, 4.9], [3.4, 6.1], [3, 6.5], [1.6, 6.5]]],
  R: [[[0, 0], [1.6, 0], [1.6, 3], [2.6, 3], [3.4, 0], [5, 0], [4.2, 3.3], [5, 4.2], [5, 6.8], [3.8, 8], [0, 8]], [[1.6, 4.5], [3, 4.5], [3.4, 4.9], [3.4, 6.1], [3, 6.5], [1.6, 6.5]]],
  I: [[[0, 0], [1.6, 0], [1.6, 8], [0, 8]]],
  A: [[[0, 0], [1.6, 0], [1.9, 2.2], [3.1, 2.2], [3.4, 0], [5, 0], [3.6, 8], [1.4, 8]], [[2.2, 3.6], [2.8, 3.6], [2.5, 5.6]]],
  S: [[[0, 1.2], [1.2, 0], [3.8, 0], [5, 1.2], [5, 3.6], [3.8, 4.4], [1.6, 4.9], [1.6, 6.5], [5, 6.5], [5, 8], [1.2, 8], [0, 6.8], [0, 4.2], [1.2, 3.4], [3.4, 2.9], [3.4, 1.5], [0, 1.5]]],
  E: [[[0, 0], [5, 0], [5, 1.5], [1.6, 1.5], [1.6, 3.3], [4.4, 3.3], [4.4, 4.7], [1.6, 4.7], [1.6, 6.5], [5, 6.5], [5, 8], [0, 8]]],
  G: [[[0, 1.2], [1.2, 0], [3.8, 0], [5, 1.2], [5, 2.6], [3.4, 2.6], [3.4, 1.5], [1.6, 1.5], [1.6, 6.5], [3.4, 6.5], [3.4, 4.8], [2.4, 4.8], [2.4, 3.3], [5, 3.3], [5, 6.8], [3.8, 8], [1.2, 8], [0, 6.8]]],
  C: [[[0, 1.2], [1.2, 0], [3.8, 0], [5, 1.2], [5, 2.6], [3.4, 2.6], [3.4, 1.5], [1.6, 1.5], [1.6, 6.5], [3.4, 6.5], [3.4, 5.4], [5, 5.4], [5, 6.8], [3.8, 8], [1.2, 8], [0, 6.8]]],
  O: [[[0, 1.2], [1.2, 0], [3.8, 0], [5, 1.2], [5, 6.8], [3.8, 8], [1.2, 8], [0, 6.8]], [[1.6, 1.5], [3.4, 1.5], [3.4, 6.5], [1.6, 6.5]]],
  N: [[[0, 0], [1.6, 0], [1.6, 4.8], [3.4, 0], [5, 0], [5, 8], [3.4, 8], [3.4, 3.2], [1.6, 8], [0, 8]]],
  D: [[[0, 0], [3.8, 0], [5, 1.2], [5, 6.8], [3.8, 8], [0, 8]], [[1.6, 1.5], [3.2, 1.5], [3.4, 1.7], [3.4, 6.3], [3.2, 6.5], [1.6, 6.5]]],
  H: [[[0, 0], [1.6, 0], [1.6, 3.3], [3.4, 3.3], [3.4, 0], [5, 0], [5, 8], [3.4, 8], [3.4, 4.7], [1.6, 4.7], [1.6, 8], [0, 8]]],
  T: [[[1.7, 0], [3.3, 0], [3.3, 6.5], [5, 6.5], [5, 8], [0, 8], [0, 6.5], [1.7, 6.5]]],
  W: [[[0, 8], [1.6, 8], [1.6, 3], [3, 6], [4.4, 3], [4.4, 8], [6, 8], [6, 0], [4.2, 0], [3, 2.8], [1.8, 0], [0, 0]]],
  K: [[[0, 0], [1.6, 0], [1.6, 3.3], [3.4, 0], [5, 0], [3, 4], [5, 8], [3.4, 8], [1.6, 4.7], [1.6, 8], [0, 8]]],
  ".": [[[0, 0], [1.6, 0], [1.6, 1.6], [0, 1.6]]],
  "?": [[[0, 6.8], [1.2, 8], [3.8, 8], [5, 6.8], [5, 4.8], [3.4, 3.6], [3.4, 3], [1.8, 3], [1.8, 4.4], [3.4, 5.6], [3.4, 6.3], [1.6, 6.3], [1.6, 5.8], [0, 5.8]], Object.assign([[1.8, 0], [3.4, 0], [3.4, 1.6], [1.8, 1.6]], { sep: true })],
  " ": [],
};
const GW = (ch) => (ch === " " ? 2.4 : Math.max(...G[ch][0].map((q) => q[0])));

/** A string as flat world outlines, left edge x0, vertical middle ym, scale u. */
function label(text, x0, ym, u) {
  let x = x0;
  const out = [];
  for (const ch of text) {
    G[ch].forEach((o, k) => { const q = o.map(([a, v]) => [x + a * u, ym + (4 - v) * u]); out.push(k && !o.sep ? q.reverse() : q); });
    x += (GW(ch) + 1.2) * u;
  }
  return out;
}
const width = (text, u) => [...text].reduce((s, ch) => s + GW(ch) + 1.2, -1.2) * u;
const centred = (text, b, u) => label(text, (b.x0 + b.x1) / 2 - width(text, u) / 2, (b.y0 + b.y1) / 2, u);
const flat = (P, outs, z) => outs.map((o) => poly(o.map(([x, y]) => P(x, y, z)))).join("");
const rect = (P, x0, y0, x1, y1, z) => poly([P(x0, y0, z), P(x1, y0, z), P(x1, y1, z), P(x0, y1, z)]);
// the close cross, two bars, flat
const cross = (cx, cy, r, w) => [[[cx - r, cy - r + w], [cx - r + w, cy - r], [cx + r, cy + r - w], [cx + r - w, cy + r]], [[cx + r - w, cy - r], [cx + r, cy - r + w], [cx - r + w, cy + r], [cx - r, cy + r - w]]];


function mount({ stage, svg, read }, value) {
  const bag = disposer();
  let lift = value;

  const C = Cam(45, 0.5, 2.3);
  fit(C, [[0, 0, 0], [PW, PD, 0], [PW, 0, 0], [0, PD, 0], [X1 + 30, Y0, PT + 16 + PH + BH]], 200, 172);
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
  const [qOut, qIn] = rings(X0, Y0, X1, Y1, 0, 1.2), [kOut, kIn] = rings(X0 + 4, Y0 + 5, X0 + 20, Y0 + 21, 0, 1);
  const panel = solid(mg), tile = solid(mg);
  const part = (p) => mk("path", { class: "dot", "data-part": p }, mg);
  const name = part("bar-on"), x = part("bar-on"), body = part("bar");
  const btns = BTN.map((b) => {
    const [out, inn] = rings(b.x0, b.y0, b.x1, b.y1, 0, 1.2), g = mk("g", {}, mg), ink = b.name === "go to cart";
    const text = mk("path", ink ? { class: "fo", "data-part": "ink-label" } : { class: "dot", "data-part": "label" }, mg), strokes = centred(b.text, b, b.u);
    if (!ink) return { ...b, ink, out, inn, tint: mk("path", { class: "dot", "data-part": "rowhi" }, g), text, strokes, hv: spring(0) };
    const cap = { sil: mk("path", { class: "dot", "data-part": "ink" }, g), top: mk("path", { class: "dot", "data-part": "ink-top" }, g), edge: mk("path", { class: "nf lo" }, g) };
    return { ...b, ink, out, inn, cap, text, strokes, hv: spring(0) };
  });

  // the toast slides in from the right (decelerate-emphasized, 300ms) and out again (accelerate-generic, 150ms)
  const q = { x: 1, t: 1, to: 1, from: 1, t0: 0, d: 300, e: bezier(0.16, 0, 0.16, 1) };
  const ez = { in: bezier(0.16, 0, 0.16, 1), out: bezier(0.36, 0.09, 1, 0.58) };
  const slide = (now) => {
    if (q.t !== q.to) { q.from = q.x; q.to = q.t; q.t0 = now; q.d = q.t ? 300 : 150; q.e = q.t ? ez.in : ez.out; }
    if (q.x === q.to) return false;
    q.x = reducedMotion() ? q.to : q.from + (q.to - q.from) * q.e(clamp((now - q.t0) / q.d, 0, 1));
    return q.x !== q.to;
  };
  let closedAt = 0, act = -1, last = "";
  function draw(force) {
    const m = clamp(q.x, 0, 1), z0 = PT + 0.4 + (lift - 0.4) * Math.min(1, m * 1.5), zt = z0 + PH, dx = (1 - m) * 44;
    const key = m.toFixed(3) + z0.toFixed(2) + btns.map((b) => b.hv.x.toFixed(2)).join();
    if (!force && key === last) return;
    last = key;
    const show = m > 0.01;
    shadow.setAttribute("display", show ? "inline" : "none"); mg.setAttribute("display", show ? "inline" : "none");
    if (!show) return;
    const sh = (z0 - PT) * 0.45, s = (r) => r.map((p) => ({ ...p, u: p.u + dx })), x0 = X0 + dx;
    shadow.setAttribute("d", rect(P, X0 + dx + sh, Y0 + sh, X1 + dx + sh, Y1 + sh, PT + 0.1));
    put(panel, prism(P, front, s(qOut), s(qIn), z0, zt));
    put(tile, prism(P, front, s(kOut), s(kIn), zt, zt + 1.4));
    const mv = (outs) => outs.map((o) => o.map(([a, b]) => [a + dx, b]));
    name.setAttribute("d", flat(P, mv(label("WORK PANTS", X0 + 24, Y0 + 11, 0.5)), zt + 0.1));
    body.setAttribute("d", flat(P, mv(label("ADDED TO THE CART", X0 + 24, Y0 + 20, 0.36)), zt + 0.1));
    x.setAttribute("d", flat(P, mv(cross(X1 - 8, Y0 + 9, 2.4, 1.2)), zt + 0.1));
    for (const b of btns) {
      const bx = { ...b, x0: b.x0 + dx, x1: b.x1 + dx }, [out, inn] = b.ink ? rings(bx.x0, b.y0, bx.x1, b.y1, 0, 1.2) : [0, 0];
      const st = mv(b.strokes);
      if (!b.ink) { b.tint.setAttribute("d", rect(P, bx.x0, b.y0, bx.x1, b.y1, zt + 0.05)); b.tint.setAttribute("display", b.hv.x > 0.5 ? "inline" : "none"); b.text.setAttribute("d", flat(P, st, zt + 0.1)); continue; }
      const z1 = zt + BH - 0.9 * clamp(b.hv.x, 0, 1), pr = prism(P, front, out, inn, zt, z1), t = poly(ringAt(P, out, z1));
      b.cap.sil.setAttribute("d", pr.sil); b.cap.top.setAttribute("d", t); b.cap.edge.setAttribute("d", t);
      b.text.setAttribute("d", flat(P, st, z1 + 0.05));
    }
  }

  const rest = P(X1 - 8, Y1 + 10, PT + 1);
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
    if (ghost && act >= 0 && !gdone) { m = true; if (now - gt > 250) { gdone = true; press(); } }
    if (!q.t) { m = true; if (now - closedAt > REOPEN) setOpen(1, now); }
    for (const s of [ax, ay, pr, ...btns.map((b) => b.hv)]) if (stepS(s, dt)) m = true;
    draw(); drawCur();
    return m;
  });
  bag.add(A.unregister);

  const zr = PT + lift + PH + 0.8; // resting button tops
  const pick = ([sx, sy]) => {
    if (!q.t) return -1;
    const [px, py] = unproj(C, sx, sy, zr);
    return btns.findIndex((b) => px > b.x0 - 2 && px < b.x1 + 2 && py > b.y0 - 2 && py < b.y1 + 2);
  };
  const say = () => { read.textContent = !q.t ? "closed" : act < 0 ? "open" : btns[act].name; };
  function set(a, p) {
    if (a !== act) {
      act = a; gdone = !ghost; gt = performance.now();
      btns.forEach((b, i) => { b.hv.t = i === a ? 1 : 0; if (b.ink) b.cap.top.setAttribute("class", i === a ? "dot m" : "dot"); });
      say();
    }
    if (p) { ax.t = p[0]; ay.t = p[1]; } else { ax.t = rest[0]; ay.t = rest[1]; }
    A.wake();
  }
  bag.add(pointer(stage, {
    move: (p, e) => { ghost = e?.pointerType === "ghost"; set(pick(p), p); gt = performance.now(); },
    down: (p) => { const a = pick(p); ghost = false; set(a, p); if (a >= 0) press(); },
    leave: (e) => { if (e?.pointerType === "ghost") setOpen(1, performance.now()); ghost = false; set(-1); },
  }));
  bag.add(() => svg.replaceChildren());

  panel.sil.classList.add("hi");
  draw(true); drawCur();
  return { set: (v) => { lift = v; draw(true); }, destroy: bag.dispose };
}

hairline({
  name: "toast-ecom",
  means: "The added-to-cart toast floating over a slab: a press on a button closes it, it slides out, then back in.",
  rules: [1, 4, 8, 9],
  range: [6, 12, 16],
  tour: [[221, 155], null, [156, 123], null],
  mount,
});
