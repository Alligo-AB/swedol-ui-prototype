/**
 * Select: a field with its label and a chevron, and one menu plate of three rows that unfolds under it. The pointer
 * over the field lights its edge and sinks it; a press opens the menu and turns the chevron; the pointer over a
 * row lifts it; a press chooses it, the menu folds and the field shows the choice. A drawn cursor follows the
 * pointer and rests above the field's chevron. The slider is how high the menu rows stand.
 */
const {
  Cam, clamp, facing, fit, lerp, open: polyline, poly, proj, ringAt, rings, prism,
  mk, pointer, reducedMotion, reflect, register, solid, put, disposer, spring, stepS, unproj,
} = HL;

const PW = 96, PD = 100, PT = 6, FX0 = 8, FX1 = 88, FY0 = 10, FY1 = 34, FH = 3, RY0 = 38, RH = 14, N = 3;
const ARROW = [[0, 0], [0, 15], [3.6, 11.6], [6.2, 17], [8.6, 15.8], [6, 10.6], [10.8, 10.6]];
const NAMES = ["Sweden", "Norway", "Finland"];
const HOLD = "Choose an option";
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
/** The circled check, flat: ring (a hole inside) plus a tick, centred on (cx, cy). */
function check(cx, cy) {
  const n = 16, ring = (r, d) => Array.from({ length: n }, (_, i) => [cx + r * Math.cos((i / n) * 2 * Math.PI * d), cy + r * Math.sin((i / n) * 2 * Math.PI * d)]);
  const T = [[-1.6, 0.2], [-0.9, -0.5], [-0.3, 0.3], [1.5, -1.6], [2.2, -0.9], [-0.3, 1.7]].map(([u, v]) => [cx + u * 1.3, cy + v * 1.3]);
  return [ring(4.4, 1), ring(3.5, -1), T];
}
const flat = (P, outs, z) => outs.map((o) => poly(o.map(([x, y]) => P(x, y, z)))).join("");


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

  const holdT = label(HOLD.toUpperCase(), FX0 + 8, 22);
  const nameT = NAMES.map((n) => (ym) => label(n.toUpperCase(), FX0 + 8, ym));
  // the field, its label bar and its chevron
  const [fOut, fIn] = rings(FX0, FY0, FX1, FY1, 0, 1.2);
  const field = solid(mk("g", {}, svg));
  const fbar = mk("path", { class: "dot", "data-part": "bar" }, svg);
  const chev = mk("path", { class: "dot", "data-part": "chev" }, svg);
  // the menu: one plate holding three rows, set apart by hairlines; a hovered row gets a tint, its name; the chosen one carries a check
  const [mOut, mIn] = rings(FX0, RY0, FX1, RY0 + N * RH, 0, 1.2);
  const menu = solid(mk("g", {}, svg));
  const rows = Array.from({ length: N }, (_, i) => ({
    y0: RY0 + i * RH,
    tint: mk("path", { class: "dot", "data-part": "rowhi" }, svg),
    line: i ? mk("path", { class: "nf lo" }, svg) : null,
    bar: mk("path", { class: "dot", "data-part": "bar-on" }, svg),
    tick: mk("path", { class: "dot", "data-part": "chev", "fill-rule": "nonzero" }, svg),
  }));
  const quad = (x0, y0, x1, y1, z) => poly([P(x0, y0, z), P(x1, y0, z), P(x1, y1, z), P(x0, y1, z)]);

  let open = 0, sel = -1, hot = -1, lastF = "", lastM = "";
  const fhv = spring(0), mo = spring(0, { k: 220, c: 26 }), ch = spring(0, { k: 220, c: 26 });

  function draw(force) {
    const m = clamp(mo.x, 0, 1), c = clamp(ch.x, 0, 1), zf = PT + FH - 1.2 * clamp(fhv.x, 0, 1);
    const kf = zf.toFixed(2) + c.toFixed(2) + sel;
    if (force || kf !== lastF) {
      lastF = kf;
      put(field, prism(P, front, fOut, fIn, PT, zf));
      fbar.setAttribute("d", flat(P, sel < 0 ? holdT : nameT[sel](22), zf + 0.1));
      fbar.setAttribute("data-part", sel < 0 ? "bar" : "bar-on");
      const a = lerp(25, 19, c), b = lerp(19, 25, c);
      chev.setAttribute("d", poly([P(74, b, zf + 0.1), P(82, b, zf + 0.1), P(78, a, zf + 0.1)]));
    }
    const z1 = PT + m * (lift + 1), key = z1.toFixed(2) + sel + act;
    if (!force && key === lastM) return;
    lastM = key;
    const show = m > 0.02;
    menu.g.setAttribute("display", show ? "inline" : "none");
    rows.forEach((r, i) => {
      for (const e of [r.tint, r.line, r.bar, r.tick]) e?.setAttribute("display", show ? "inline" : "none");
      if (!show) return;
      if (i === 0) put(menu, prism(P, front, mOut, mIn, PT, z1));
      r.tint.setAttribute("display", show && act === i + 1 ? "inline" : "none");
      r.tint.setAttribute("d", quad(FX0 + 1.2, r.y0 + 0.6, FX1 - 1.2, r.y0 + RH - 0.6, z1 + 0.1));
      r.line?.setAttribute("d", polyline([P(FX0 + 4, r.y0, z1 + 0.1), P(FX1 - 4, r.y0, z1 + 0.1)]));
      r.bar.setAttribute("d", flat(P, nameT[i](r.y0 + RH / 2), z1 + 0.2));
      r.tick.setAttribute("display", i === sel ? "inline" : "none");
      r.tick.setAttribute("d", flat(P, check(FX1 - 8, r.y0 + RH / 2), z1 + 0.2));
    });
  }

  const rest = P(62, 30, PT + FH + 9);
  const ax = spring(rest[0], { k: 140 }), ay = spring(rest[1], { k: 140 }), pr = spring(0);
  const cur = mk("path", { class: "dot", "data-part": "cursor" }, svg);
  const drawCur = () => cur.setAttribute("d", poly(ARROW.map(([u, v]) => [ax.x + u - 0.5, ay.x + v + 2.5 * clamp(pr.x, 0, 1)])));

  let ghost = false, gt = 0, gdone = true, act = -1;
  const A = register(stage, (dt, now) => {
    let m = false;
    if (ghost && act >= 0 && !gdone) { m = true; if (now - gt > 250) { gdone = true; press(act); } }
    for (const q of [fhv, mo, ch, ax, ay, pr, ]) if (stepS(q, dt)) m = true;
    draw(); drawCur();
    return m;
  });
  bag.add(A.unregister);

  // hit: the field's and the rows' resting top planes; rows only count while the menu is open
  const pick = ([sx, sy]) => {
    const [x, y] = unproj(C, sx, sy, PT + FH);
    if (x < FX0 - 2 || x > FX1 + 2) return -1;
    if (y > FY0 - 2 && y < FY1 + 2) return 0;
    if (!open) return -1;
    const i = rows.findIndex((r) => y >= r.y0 && y < r.y0 + RH);
    return i < 0 ? -1 : i + 1;
  };
  const say = () => { read.textContent = act > 0 ? NAMES[act - 1] : open ? "open" : act === 0 ? "field" : sel < 0 ? "rest" : NAMES[sel]; };
  const setOpen = (v) => { open = v; mo.t = v; ch.t = v; };
  function press(a) {
    if (a === 0) setOpen(1 - open);
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
      if (e?.pointerType === "ghost") { sel = -1; setOpen(0); say(); }
      ghost = false; set(-1);
    },
  }));
  bag.add(() => svg.replaceChildren());

  field.sil.classList.add("hi");
  draw(true); drawCur();
  return { set: (v) => { lift = v; draw(true); }, destroy: bag.dispose };
}

hairline({
  name: "select",
  means: "A select field with a menu under it: a press opens it and turns the chevron, a press on a row chooses it.",
  rules: [1, 4, 8, 9],
  range: [1, 2, 3],
  tour: [[246, 131], [161, 180], [150, 205], null],
  mount,
});
