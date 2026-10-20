/**
 * Icon picker: a labelled field holding an icon name. A press opens a panel on top of it (search box and a grid of six
 * icons); the pointer over a cell tints it; a press on a cell puts its name in the field and closes the panel. A drawn
 * cursor follows the pointer and rests below the field. The slider is how high the panel stands.
 */
const {
  Cam, clamp, facing, fit, lerp, open: polyline, poly, proj, ringAt, rings, prism,
  mk, pointer, reducedMotion, reflect, register, solid, put, disposer, spring, stepS, unproj,
} = HL;

const PW = 96, PD = 100, PT = 6, FX0 = 8, FY0 = 16, FX1 = 88, FY1 = 40, FH = 3, PY0 = 4, PY1 = 94, CY0 = 34, CH = 25, N = 6;
const ARROW = [[0, 0], [0, 15], [3.6, 11.6], [6.2, 17], [8.6, 15.8], [6, 10.6], [10.8, 10.6]];
const NAMES = ["HOME", "ADD", "DONE", "MENU", "INFO", "SEARCH"];
const circ = (cx, cy, r, d) => Array.from({ length: 20 }, (_, i) => [cx + r * Math.cos((i / 20) * 2 * Math.PI * d), cy + r * Math.sin((i / 20) * 2 * Math.PI * d)]);
// icons on a 10 x 10 grid, v up; o = outlines, h = holes (given the same way round, the draw turns them)
const ICONS = [
  { o: [[[1.4, 0], [8.6, 0], [8.6, 4.5], [10, 4.5], [5, 10], [0, 4.5], [1.4, 4.5]]], h: [[[3.4, 1.6], [6.6, 1.6], [6.6, 5], [3.4, 5]]] },
  { o: [[[4.2, 0], [5.8, 0], [5.8, 4.2], [10, 4.2], [10, 5.8], [5.8, 5.8], [5.8, 10], [4.2, 10], [4.2, 5.8], [0, 5.8], [0, 4.2], [4.2, 4.2]]], h: [] },
  { o: [[[3.6, 0.2], [10, 6.8], [8.6, 8.2], [3.6, 3], [1.4, 5.2], [0, 3.8]]], h: [] },
  { o: [[[0, 0], [10, 0], [10, 1.6], [0, 1.6]], [[0, 4.2], [10, 4.2], [10, 5.8], [0, 5.8]], [[0, 8.4], [10, 8.4], [10, 10], [0, 10]]], h: [] },
  { o: [circ(5, 5, 5, 1), [[4.2, 1.6], [5.8, 1.6], [5.8, 5], [4.2, 5]], [[4.2, 6], [5.8, 6], [5.8, 7.6], [4.2, 7.6]]], h: [circ(5, 5, 3.8, 1)] },
  { o: [circ(4, 6, 4, 1), [[6.23, 2.63], [8.93, -0.07], [10.07, 1.07], [7.37, 3.77]]], h: [circ(4, 6, 2.6, 1)] },
];
const G = {
  H: [[[0, 0], [1.6, 0], [1.6, 3.3], [3.4, 3.3], [3.4, 0], [5, 0], [5, 8], [3.4, 8], [3.4, 4.7], [1.6, 4.7], [1.6, 8], [0, 8]]],
  O: [[[0, 1.2], [1.2, 0], [3.8, 0], [5, 1.2], [5, 6.8], [3.8, 8], [1.2, 8], [0, 6.8]], [[1.6, 1.5], [3.4, 1.5], [3.4, 6.5], [1.6, 6.5]]],
  M: [[[0, 0], [1.6, 0], [1.6, 5], [3, 2], [4.4, 5], [4.4, 0], [6, 0], [6, 8], [4.2, 8], [3, 5.2], [1.8, 8], [0, 8]]],
  E: [[[0, 0], [5, 0], [5, 1.5], [1.6, 1.5], [1.6, 3.3], [4.4, 3.3], [4.4, 4.7], [1.6, 4.7], [1.6, 6.5], [5, 6.5], [5, 8], [0, 8]]],
  A: [[[0, 0], [1.6, 0], [1.9, 2.2], [3.1, 2.2], [3.4, 0], [5, 0], [3.6, 8], [1.4, 8]], [[2.2, 3.6], [2.8, 3.6], [2.5, 5.6]]],
  D: [[[0, 0], [3.8, 0], [5, 1.2], [5, 6.8], [3.8, 8], [0, 8]], [[1.6, 1.5], [3.2, 1.5], [3.4, 1.7], [3.4, 6.3], [3.2, 6.5], [1.6, 6.5]]],
  N: [[[0, 0], [1.6, 0], [1.6, 4.8], [3.4, 0], [5, 0], [5, 8], [3.4, 8], [3.4, 3.2], [1.6, 8], [0, 8]]],
  U: [[[0, 1.2], [1.2, 0], [3.8, 0], [5, 1.2], [5, 8], [3.4, 8], [3.4, 1.5], [1.6, 1.5], [1.6, 8], [0, 8]]],
  I: [[[0, 0], [1.6, 0], [1.6, 8], [0, 8]]],
  F: [[[0, 0], [1.6, 0], [1.6, 3.3], [4.4, 3.3], [4.4, 4.7], [1.6, 4.7], [1.6, 6.5], [5, 6.5], [5, 8], [0, 8]]],
  S: [[[0, 1.2], [1.2, 0], [3.8, 0], [5, 1.2], [5, 3.6], [3.8, 4.4], [1.6, 4.9], [1.6, 6.5], [5, 6.5], [5, 8], [1.2, 8], [0, 6.8], [0, 4.2], [1.2, 3.4], [3.4, 2.9], [3.4, 1.5], [0, 1.5]]],
  R: [[[0, 0], [1.6, 0], [1.6, 3], [2.6, 3], [3.4, 0], [5, 0], [4.2, 3.3], [5, 4.2], [5, 6.8], [3.8, 8], [0, 8]], [[1.6, 4.5], [3, 4.5], [3.4, 4.9], [3.4, 6.1], [3, 6.5], [1.6, 6.5]]],
  C: [[[0, 1.2], [1.2, 0], [3.8, 0], [5, 1.2], [5, 2.6], [3.4, 2.6], [3.4, 1.5], [1.6, 1.5], [1.6, 6.5], [3.4, 6.5], [3.4, 5.4], [5, 5.4], [5, 6.8], [3.8, 8], [1.2, 8], [0, 6.8]]],
  " ": [],
};
const GW = (ch) => (ch === " " ? 2.4 : Math.max(...G[ch][0].map((q) => q[0])));
const U = 0.55;
/** A string as flat world outlines starting at (x0, ymid): condensed heavy capitals, counters wound the other way. */
function label(text, x0, ym) {
  let x = x0;
  const out = [];
  for (const ch of text) {
    G[ch].forEach((o, k) => { const q = o.map(([u, v]) => [x + u * U, ym + (4 - v) * U]); out.push(k ? q.reverse() : q); });
    x += (GW(ch) + 1.2) * U;
  }
  return out;
}
/** An icon, flat, centred on (cx, cy), `s` world units per grid unit; holes wound the other way. */
const icon = (k, cx, cy, s) => {
  const t = ([u, v]) => [cx + (u - 5) * s, cy + (5 - v) * s];
  return [...ICONS[k].o.map((o) => o.map(t)), ...ICONS[k].h.map((o) => o.map(t).reverse())];
};
const flat = (P, outs, z) => outs.map((o) => poly(o.map(([x, y]) => P(x, y, z)))).join("");
const CX = [24, 48, 72], CYS = [CY0 + CH / 2, CY0 + CH * 1.5 + 1];

function mount({ stage, svg, read }, value) {
  const bag = disposer();
  let lift = value;

  const C = Cam(45, 0.5, 2.3);
  fit(C, [[0, 0, 0], [PW, PD, 0], [PW, 0, 0], [0, PD, 0], [FX1, 40, PT + 12]], 200, 172);
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

  const titleT = label("ICON NAME", FX0, 10);
  const nameT = NAMES.map((n) => label(n, FX0 + 6, 28));
  const searchT = label("SEARCH ICONS", FX0 + 6, 22);
  const tit = mk("path", { class: "dot", "data-part": "title" }, svg);
  tit.setAttribute("d", flat(P, titleT, PT + 0.1));
  // the field
  const [fOut, fIn] = rings(FX0, FY0, FX1, FY1, 0, 1.2);
  const field = solid(mk("g", {}, svg));
  const fbar = mk("path", { class: "dot", "data-part": "bar-on" }, svg);
  // the panel on top of it: one group, so the skin can fade it in and out
  const [mOut, mIn] = rings(4, PY0, 92, PY1, 0, 1.2);
  const mg = mk("g", { "data-part": "menu" }, svg);
  const menu = solid(mg);
  const ptit = mk("path", { class: "dot", "data-part": "title" }, mg);
  const sbox = mk("path", { class: "nf", "data-part": "sbox" }, mg);
  const sbar = mk("path", { class: "dot", "data-part": "bar" }, mg);
  const cells = Array.from({ length: N }, (_, i) => ({
    x: CX[i % 3], y: CYS[(i / 3) | 0],
    tint: mk("path", { class: "dot", "data-part": "rowhi" }, mg),
    ic: mk("path", { class: "dot", "data-part": "chev", "fill-rule": "nonzero" }, mg),
  }));
  const quad = (x0, y0, x1, y1, z) => poly([P(x0, y0, z), P(x1, y0, z), P(x1, y1, z), P(x0, y1, z)]);

  let open = 0, sel = 0, lastF = "", lastM = "";
  const fhv = spring(0), mo = spring(0, { k: 45, c: 13.4 });

  function draw(force) {
    const m = clamp(mo.x, 0, 1), zf = PT + FH - 1.2 * clamp(fhv.x, 0, 1);
    const kf = zf.toFixed(2) + sel;
    if (force || kf !== lastF) {
      lastF = kf;
      put(field, prism(P, front, fOut, fIn, PT, zf));
      fbar.setAttribute("d", flat(P, nameT[sel], zf + 0.1));
    }
    const z1 = PT + m * (lift + 1), key = z1.toFixed(2) + sel + act;
    if (!force && key === lastM) return;
    lastM = key;
    const show = m > 0.02;
    mg.setAttribute("display", show ? "inline" : "none");
    if (!show) return;
    put(menu, prism(P, front, mOut, mIn, PT, z1));
    ptit.setAttribute("d", flat(P, titleT, z1 + 0.1));
    sbox.setAttribute("d", poly([P(FX0, 16, z1 + 0.1), P(FX1, 16, z1 + 0.1), P(FX1, 28, z1 + 0.1), P(FX0, 28, z1 + 0.1)]));
    sbar.setAttribute("d", flat(P, searchT, z1 + 0.1));
    cells.forEach((c, i) => {
      c.tint.setAttribute("display", act === i + 1 ? "inline" : "none");
      c.tint.setAttribute("d", quad(c.x - 12, c.y - 12, c.x + 12, c.y + 12, z1 + 0.1));
      c.ic.setAttribute("d", flat(P, icon(i, c.x, c.y, 1.3), z1 + 0.2));
    });
  }

  const rest = P(70, 64, PT + FH + 9);
  const ax = spring(rest[0], { k: 140 }), ay = spring(rest[1], { k: 140 }), pr = spring(0);
  const cur = mk("path", { class: "dot", "data-part": "cursor" }, svg);
  const drawCur = () => cur.setAttribute("d", poly(ARROW.map(([u, v]) => [ax.x + u - 0.5, ay.x + v + 2.5 * clamp(pr.x, 0, 1)])));

  let ghost = false, gt = 0, gdone = true, act = -1;
  const A = register(stage, (dt, now) => {
    let m = false;
    if (ghost && act >= 0 && !gdone) { m = true; if (now - gt > 250) { gdone = true; press(act); } }
    for (const q of [fhv, mo, ax, ay, pr]) if (stepS(q, dt)) m = true;
    draw(); drawCur();
    return m;
  });
  bag.add(A.unregister);

  // hit: the field's and the cells' resting planes; cells only count while the panel is open (act 1..6 = cell + 1)
  const pick = ([sx, sy]) => {
    const [x, y] = unproj(C, sx, sy, PT + FH);
    if (open) {
      if (x < FX0 || x > FX1 || y < CY0 || y > CY0 + CH * 2 + 1) return -1;
      return Math.min(2, ((x - FX0) / ((FX1 - FX0) / 3)) | 0) + (y < CY0 + CH + 0.5 ? 0 : 3) + 1;
    }
    return x > FX0 - 2 && x < FX1 + 2 && y > FY0 - 2 && y < FY1 + 2 ? 0 : -1;
  };
  const say = () => { read.textContent = act > 0 ? NAMES[act - 1].toLowerCase() : open ? "open" : act === 0 ? "field" : "rest"; };
  const setOpen = (v) => { open = v; mo.t = v; if (v) mg.setAttribute("data-open", ""); else mg.removeAttribute("data-open"); };
  function press(a) {
    if (a === 0) setOpen(1);
    else if (a > 0) { sel = a - 1; setOpen(0); }
    pr.x = 1; pr.t = 0; say(); A.wake();
  }
  function set(a, p) {
    if (a !== act) {
      act = a; gdone = !ghost; gt = performance.now();
      fhv.t = a === 0 ? 1 : 0;
      field.sil.classList.toggle("hi", a === 0 || (a < 0 && !open));
      menu.sil.classList.toggle("hi", a > 0);
      say();
    }
    if (a < 0) { ax.t = rest[0]; ay.t = rest[1]; } else { ax.t = p[0]; ay.t = p[1]; }
    A.wake();
  }
  bag.add(pointer(stage, {
    move: (p, e) => { ghost = e?.pointerType === "ghost"; set(pick(p), p); gt = performance.now(); },
    down: (p) => { const a = pick(p); set(a, p); ghost = false; if (a >= 0) press(a); },
    leave: (e) => {
      if (e?.pointerType === "ghost") { sel = 0; setOpen(0); say(); }
      ghost = false; set(-1);
    },
  }));
  bag.add(() => svg.replaceChildren());

  field.sil.classList.add("hi");
  draw(true); drawCur();
  return { set: (v) => { lift = v; draw(true); }, destroy: bag.dispose };
}

hairline({
  name: "icon-picker",
  means: "An icon-name field with a panel on top of it: a press opens it, a press on an icon puts its name in the field.",
  rules: [1, 4, 8, 9],
  range: [1, 2, 3],
  tour: [[236, 136], [204, 191], null],
  mount,
});
