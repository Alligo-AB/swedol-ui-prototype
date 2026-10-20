/**
 * Modal: a dialog panel floats above a slab that is dimmed behind it. The panel carries a title, two text bars,
 * a Cancel and a Delete button. The pointer over a button sinks it; a press closes the modal (the panel drops,
 * the scrim and panel fade) and it opens again a moment later. A drawn cursor follows the pointer and rests
 * beside Delete. The slider is how high the panel floats.
 */
const {
  Cam, clamp, facing, fit, poly, proj, reflect, ringAt, rings, prism,
  mk, pointer, register, solid, put, disposer, spring, stepS, unproj,
} = HL;

const PW = 96, PD = 100, PT = 6, PX0 = 8, PX1 = 88, PY0 = 8, PY1 = 82, PH = 2.5, BH = 1.6, REOPEN = 1100;
const BTN = [{ name: "cancel", text: "CANCEL", x0: 12, x1: 42, y0: 62, y1: 76 }, { name: "delete", text: "DELETE", x0: 46, x1: 84, y0: 62, y1: 76 }];
const ARROW = [[0, 0], [0, 15], [3.6, 11.6], [6.2, 17], [8.6, 15.8], [6, 10.6], [10.8, 10.6]];
const G = {
  P: [[[0, 0], [1.6, 0], [1.6, 3], [3.8, 3], [5, 4.2], [5, 6.8], [3.8, 8], [0, 8]], [[1.6, 4.5], [3, 4.5], [3.4, 4.9], [3.4, 6.1], [3, 6.5], [1.6, 6.5]]],
  R: [[[0, 0], [1.6, 0], [1.6, 3], [2.6, 3], [3.4, 0], [5, 0], [4.2, 3.3], [5, 4.2], [5, 6.8], [3.8, 8], [0, 8]], [[1.6, 4.5], [3, 4.5], [3.4, 4.9], [3.4, 6.1], [3, 6.5], [1.6, 6.5]]],
  I: [[[0, 0], [1.6, 0], [1.6, 8], [0, 8]]],
  M: [[[0, 0], [1.6, 0], [1.6, 5], [3, 2], [4.4, 5], [4.4, 0], [6, 0], [6, 8], [4.2, 8], [3, 5.2], [1.8, 8], [0, 8]]],
  A: [[[0, 0], [1.6, 0], [1.9, 2.2], [3.1, 2.2], [3.4, 0], [5, 0], [3.6, 8], [1.4, 8]], [[2.2, 3.6], [2.8, 3.6], [2.5, 5.6]]],
  Y: [[[0, 8], [1.7, 8], [2.5, 5], [3.3, 8], [5, 8], [3.3, 3.6], [3.3, 0], [1.7, 0], [1.7, 3.6]]],
  S: [[[0, 1.2], [1.2, 0], [3.8, 0], [5, 1.2], [5, 3.6], [3.8, 4.4], [1.6, 4.9], [1.6, 6.5], [5, 6.5], [5, 8], [1.2, 8], [0, 6.8], [0, 4.2], [1.2, 3.4], [3.4, 2.9], [3.4, 1.5], [0, 1.5]]],
  E: [[[0, 0], [5, 0], [5, 1.5], [1.6, 1.5], [1.6, 3.3], [4.4, 3.3], [4.4, 4.7], [1.6, 4.7], [1.6, 6.5], [5, 6.5], [5, 8], [0, 8]]],
  C: [[[0, 1.2], [1.2, 0], [3.8, 0], [5, 1.2], [5, 2.6], [3.4, 2.6], [3.4, 1.5], [1.6, 1.5], [1.6, 6.5], [3.4, 6.5], [3.4, 5.4], [5, 5.4], [5, 6.8], [3.8, 8], [1.2, 8], [0, 6.8]]],
  O: [[[0, 1.2], [1.2, 0], [3.8, 0], [5, 1.2], [5, 6.8], [3.8, 8], [1.2, 8], [0, 6.8]], [[1.6, 1.5], [3.4, 1.5], [3.4, 6.5], [1.6, 6.5]]],
  N: [[[0, 0], [1.6, 0], [1.6, 4.8], [3.4, 0], [5, 0], [5, 8], [3.4, 8], [3.4, 3.2], [1.6, 8], [0, 8]]],
  D: [[[0, 0], [3.8, 0], [5, 1.2], [5, 6.8], [3.8, 8], [0, 8]], [[1.6, 1.5], [3.2, 1.5], [3.4, 1.7], [3.4, 6.3], [3.2, 6.5], [1.6, 6.5]]],
  H: [[[0, 0], [1.6, 0], [1.6, 3.3], [3.4, 3.3], [3.4, 0], [5, 0], [5, 8], [3.4, 8], [3.4, 4.7], [1.6, 4.7], [1.6, 8], [0, 8]]],
  T: [[[1.7, 0], [3.3, 0], [3.3, 6.5], [5, 6.5], [5, 8], [0, 8], [0, 6.5], [1.7, 6.5]]],
  W: [[[0, 8], [1.6, 8], [1.6, 3], [3, 6], [4.4, 3], [4.4, 8], [6, 8], [6, 0], [4.2, 0], [3, 2.8], [1.8, 0], [0, 0]]],
  F: [[[0, 0], [1.6, 0], [1.6, 3.3], [4.4, 3.3], [4.4, 4.7], [1.6, 4.7], [1.6, 6.5], [5, 6.5], [5, 8], [0, 8]]],
  L: [[[0, 0], [5, 0], [5, 1.5], [1.6, 1.5], [1.6, 8], [0, 8]]],
  " ": [],
};
const GW = (ch) => (ch === " " ? 2.4 : Math.max(...G[ch][0].map((q) => q[0])));

/** A string as flat world outlines, left edge x0, vertical middle ym, scale u. */
function label(text, x0, ym, u) {
  let x = x0;
  const out = [];
  for (const ch of text) {
    G[ch].forEach((o, k) => { const q = o.map(([a, v]) => [x + a * u, ym + (4 - v) * u]); out.push(k ? q.reverse() : q); });
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
  fit(C, [[0, 0, 0], [PW, PD, 0], [PW, 0, 0], [0, PD, 0], [PX1, PY0, PT + 16 + PH + BH]], 200, 172);
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

  // the scrim over the slab and the panel's shadow on it fade with the open state (the skin sets the transition)
  const sg = mk("g", { "data-part": "fade" }, svg);
  const scrim = mk("path", { class: "dot", "data-part": "scrim", d: rect(P, 0, 0, PW, PD, PT + 0.05) }, sg);
  const shadow = mk("path", { class: "dot", "data-part": "shadow" }, sg);
  const mg = mk("g", { "data-part": "fade" }, svg);
  const [qOut, qIn] = rings(PX0, PY0, PX1, PY1, 0, 1.2);
  const panel = solid(mk("g", {}, mg));
  const title = mk("path", { class: "dot", "data-part": "bar-on" }, mg);
  const x = mk("path", { class: "dot", "data-part": "bar-on" }, mg);
  const bars = [0, 1].map(() => mk("path", { class: "dot", "data-part": "bar" }, mg));
  const barsXY = [[16, 40, 76, 43.4], [16, 48, 56, 51.4]];
  const btns = BTN.map((b) => {
    const [out, inn] = rings(b.x0, b.y0, b.x1, b.y1, 0, 1.2), g = mk("g", {}, mg), ink = b.name === "delete";
    const cap = ink ? { sil: mk("path", { class: "dot", "data-part": "ink" }, g), top: mk("path", { class: "dot", "data-part": "ink-top" }, g), edge: mk("path", { class: "nf lo" }, g) } : solid(g);
    const text = mk("path", { class: ink ? "fo" : "dot", "data-part": ink ? "ink-label" : "label" }, mg);
    return { ...b, ink, out, inn, cap, text, strokes: centred(b.text, b, 0.62), hv: spring(0) };
  });

  let open = 1, closedAt = 0, act = -1, last = "";
  const o = spring(1, { k: 45, c: 13.4 });
  function draw(force) {
    const m = clamp(o.x, 0, 1), z0 = PT + 0.4 + m * (lift - 0.4), zt = z0 + PH;
    const key = z0.toFixed(2) + btns.map((b) => b.hv.x.toFixed(2)).join();
    if (!force && key === last) return;
    last = key;
    const show = m > 0.02;
    sg.setAttribute("display", show ? "inline" : "none"); mg.setAttribute("display", show ? "inline" : "none");
    if (!show) return;
    const sh = (z0 - PT) * 0.45; // the shadow slides away as the panel rises
    shadow.setAttribute("d", rect(P, PX0 + sh, PY0 + sh, PX1 + sh, PY1 + sh, PT + 0.1));
    put(panel, prism(P, front, qOut, qIn, z0, zt));
    title.setAttribute("d", flat(P, label("DELETE ADDRESS", 14, 20, 0.66), zt + 0.1));
    x.setAttribute("d", flat(P, cross(78, 20, 2.6, 1.3), zt + 0.1));
    bars.forEach((e, i) => e.setAttribute("d", rect(P, ...barsXY[i].slice(0, 2), ...barsXY[i].slice(2), zt + 0.1)));
    for (const b of btns) {
      const z1 = zt + BH - 0.9 * clamp(b.hv.x, 0, 1);
      const pr = prism(P, front, b.out, b.inn, zt, z1);
      if (b.ink) { b.cap.sil.setAttribute("d", pr.sil); const t = poly(ringAt(P, b.out, z1)); b.cap.top.setAttribute("d", t); b.cap.edge.setAttribute("d", t); } else put(b.cap, pr);
      b.text.setAttribute("d", flat(P, b.strokes, z1 + 0.05));
    }
  }

  const rest = P(PX1 - 6, PY1 + 10, PT + 1);
  const ax = spring(rest[0], { k: 140 }), ay = spring(rest[1], { k: 140 }), pr = spring(0);
  const halo = mk("path", { class: "fo" }, svg), cur = mk("path", { class: "dot", "data-part": "cursor" }, svg);
  const drawCur = () => {
    const px = ax.x - 0.5, py = ay.x + 2.5 * clamp(pr.x, 0, 1);
    cur.setAttribute("d", poly(ARROW.map(([u, v]) => [px + u, py + v])));
    halo.setAttribute("d", [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]].map(([i, j]) => poly(ARROW.map(([u, v]) => [px + u + i * 0.8, py + v + j * 0.8]))).join(""));
  };

  const setOpen = (v, now) => { open = v; o.t = v; closedAt = now; if (v) { sg.setAttribute("data-open", ""); mg.setAttribute("data-open", ""); } else { sg.removeAttribute("data-open"); mg.removeAttribute("data-open"); } };
  let ghost = false, gt = 0, gdone = true;
  const press = (a) => { setOpen(0, performance.now()); pr.x = 1; pr.t = 0; say(); A.wake(); };
  const A = register(stage, (dt, now) => {
    let m = false;
    if (ghost && act >= 0 && !gdone) { m = true; if (now - gt > 250) { gdone = true; press(act); } }
    if (!open) { m = true; if (now - closedAt > REOPEN) setOpen(1, now); }
    for (const q of [o, ax, ay, pr, ...btns.map((b) => b.hv)]) if (stepS(q, dt)) m = true;
    draw(); drawCur();
    return m;
  });
  bag.add(A.unregister);
  sg.setAttribute("data-open", ""); mg.setAttribute("data-open", "");

  const zr = PT + lift + PH + BH; // resting button tops
  const pick = ([sx, sy]) => {
    if (!open) return -1;
    const [px, py] = unproj(C, sx, sy, zr);
    return btns.findIndex((b) => px > b.x0 - 2 && px < b.x1 + 2 && py > b.y0 - 2 && py < b.y1 + 2);
  };
  const say = () => { read.textContent = !open ? "closed" : act < 0 ? "open" : btns[act].name; };
  function set(a, p) {
    if (a !== act) {
      act = a; gdone = !ghost; gt = performance.now();
      btns.forEach((b, i) => { b.hv.t = i === a ? 1 : 0; if (b.ink) b.cap.top.setAttribute("class", i === a ? "dot m" : "dot"); else b.cap.sil.classList.toggle("hi", i === a); });
      say();
    }
    if (p) { ax.t = p[0]; ay.t = p[1]; } else { ax.t = rest[0]; ay.t = rest[1]; }
    A.wake();
  }
  bag.add(pointer(stage, {
    move: (p, e) => { ghost = e?.pointerType === "ghost"; set(pick(p), p); gt = performance.now(); },
    down: (p) => { const a = pick(p); ghost = false; set(a, p); if (a >= 0) press(a); },
    leave: (e) => { if (e?.pointerType === "ghost") setOpen(1, performance.now()); ghost = false; set(-1); },
  }));
  bag.add(() => svg.replaceChildren());

  panel.sil.classList.add("hi");
  draw(true); drawCur();
  return { set: (v) => { lift = v; draw(true); }, destroy: bag.dispose };
}

hairline({
  name: "modal",
  means: "A dialog panel floating over a dimmed slab with Cancel and Delete: a press on a button closes the modal and it opens again.",
  rules: [1, 4, 8, 9],
  range: [6, 12, 16],
  tour: [[197, 157], null, [133, 129], null],
  mount,
});
