/**
 * Select: a field with its label bar and a chevron, and a menu of three rows that unfolds under it. The pointer
 * over the field lights its edge and sinks it; a press opens the menu and turns the chevron; the pointer over a
 * row lifts it; a press chooses it, the menu folds and the field shows the choice. A drawn cursor follows the
 * pointer and rests above the field's chevron. The slider is how high the menu rows stand.
 */
const {
  Cam, clamp, facing, fit, lerp, poly, proj, ringAt, rings, prism,
  mk, pointer, reducedMotion, reflect, register, solid, put, disposer, spring, stepS, unproj,
} = HL;

const PW = 96, PD = 100, PT = 6, FX0 = 8, FX1 = 88, FY0 = 10, FY1 = 34, FH = 3, RY0 = 40, RH = 12, RG = 2, N = 3;
const BARS = [30, 38, 24]; // label-bar length per row; the field's own bar is 22 empty, then the chosen row's
const ARROW = [[0, 0], [0, 15], [3.6, 11.6], [6.2, 17], [8.6, 15.8], [6, 10.6], [10.8, 10.6]];
const NAMES = ["Sweden", "Norway", "Finland"];

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

  // the field, its label bar and its chevron
  const [fOut, fIn] = rings(FX0, FY0, FX1, FY1, 0, 1.2);
  const field = solid(mk("g", {}, svg));
  const fbar = mk("path", { class: "dot", "data-part": "bar" }, svg);
  const chev = mk("path", { class: "dot", "data-part": "chev" }, svg);
  // the menu: one raised row each, with its label bar on top
  const rows = Array.from({ length: N }, (_, i) => {
    const y0 = RY0 + i * (RH + RG), [o, n] = rings(FX0, y0, FX1, y0 + RH, 0, 1.2);
    const s = solid(mk("g", {}, svg));
    const bar = mk("path", { class: "dot", "data-part": "bar" }, svg);
    return { y0, o, n, s, bar, hv: spring(0), last: "" };
  });
  const quad = (x0, y0, x1, y1, z) => poly([P(x0, y0, z), P(x1, y0, z), P(x1, y1, z), P(x0, y1, z)]);

  let open = 0, sel = -1, hot = -1, lastF = "";
  const fhv = spring(0), mo = spring(0, { k: 220, c: 26 }), ch = spring(0, { k: 220, c: 26 });

  function draw(force) {
    const m = clamp(mo.x, 0, 1), c = clamp(ch.x, 0, 1), zf = PT + FH - 1.2 * clamp(fhv.x, 0, 1);
    const kf = zf.toFixed(2) + c.toFixed(2) + sel;
    if (force || kf !== lastF) {
      lastF = kf;
      put(field, prism(P, front, fOut, fIn, PT, zf));
      const w = sel < 0 ? 22 : BARS[sel];
      fbar.setAttribute("d", quad(FX0 + 8, 20, FX0 + 8 + w, 24, zf + 0.1));
      fbar.setAttribute("data-part", sel < 0 ? "bar" : "bar-on");
      const a = lerp(25, 19, c), b = lerp(19, 25, c);
      chev.setAttribute("d", poly([P(72, b, zf + 0.1), P(80, b, zf + 0.1), P(76, a, zf + 0.1)]));
    }
    rows.forEach((r, i) => {
      const z1 = PT + m * (lift + 1) + 1.5 * clamp(r.hv.x, 0, 1), key = z1.toFixed(2) + (i === sel) + m;
      if (!force && key === r.last) return;
      r.last = key;
      const show = m > 0.02;
      for (const e of [r.s.g, r.bar]) e.setAttribute("display", show ? "inline" : "none");
      if (!show) return;
      put(r.s, prism(P, front, r.o, r.n, PT, z1));
      r.bar.setAttribute("d", quad(FX0 + 8, r.y0 + 4, FX0 + 8 + BARS[i], r.y0 + 8, z1 + 0.1));
      r.bar.setAttribute("data-part", i === sel ? "bar-on" : "bar");
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
    for (const q of [fhv, mo, ch, ax, ay, pr, ...rows.map((r) => r.hv)]) if (stepS(q, dt)) m = true;
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
    const i = rows.findIndex((r) => y > r.y0 - 1 && y < r.y0 + RH + 1);
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
      rows.forEach((r, i) => { r.hv.t = i + 1 === a ? 1 : 0; });
      field.sil.classList.toggle("hi", a === 0 || (a < 0 && !open));
      rows.forEach((r, i) => r.s.sil.classList.toggle("hi", i + 1 === a));
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
  tour: [[246, 131], [161, 180], null],
  mount,
});
