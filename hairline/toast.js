/**
 * System Toast: a toast card (status bar, check icon, one text line, close ×) on a slab, and a Primary trigger button in front.
 * Pressing the button slides the toast in from the right; pressing the toast (its close) slides it out again.
 * The pointer over the toast lifts it; over the button it presses it. A drawn cursor follows the pointer and rests
 * above the toast. The slider is how high the toast stands.
 */
const {
  Cam, bezier, clamp, facing, fit, lerp, poly, proj, ringAt, rrect, prism, rings,
  mk, pointer, reducedMotion, reflect, register, solid, put, disposer, spring, stepS, unproj,
} = HL;

const PW = 120, PD = 84, PT = 5, X0 = 10, X1 = 108, Y0 = 8, Y1 = 46, SLIDE = 70;
const BX0 = 12, BX1 = 56, BY0 = 58, BY1 = 74, BH = 4;
const ARROW = [[0, 0], [0, 15], [3.6, 11.6], [6.2, 17], [8.6, 15.8], [6, 10.6], [10.8, 10.6]];

function mount({ stage, svg, read }, value) {
  const bag = disposer();
  let h = value ?? 6;

  const C = Cam(45, 0.5, 1.9);
  fit(C, [[0, 0, 0], [PW, PD, 0], [PW, 0, 0], [0, PD, 0], [X1, Y0, PT + 10]], 200, 172);
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

  // the toast: card, status bar on its left edge, icon disc and two text lines on its top. It fades while it slides (the figure's own, the real toast does not)
  const tg = mk("g", { "data-part": "toast", "data-show": "" }, svg);
  const card = solid(mk("g", {}, tg)), bar = solid(mk("g", {}, tg));
  bar.sil.setAttribute("data-part", "status");
  const icon = mk("path", { class: "dot", "data-part": "icon" }, tg);
  const tick = mk("path", { class: "dot", "data-part": "tick" }, tg), l1 = mk("path", { class: "dot", "data-part": "line-on" }, tg), x = mk("path", { class: "dot", "data-part": "line-on" }, tg);
  const t = { x: 1, t: 1, from: 1, to: 1, t0: 0, last: "" }, lift = spring(0);
  const flat = (x0, y0, x1, y1, z) => poly([P(x0, y0, z), P(x1, y0, z), P(x1, y1, z), P(x0, y1, z)]);
  function drawToast(force) {
    const dx = (1 - t.x) * SLIDE, z = PT + h + 1.2 * clamp(lift.x, 0, 1), key = dx.toFixed(2) + z.toFixed(2);
    if (!force && key === t.last) return;
    t.last = key;
    const a = X0 + dx, [o, i] = rings(a, Y0, X1 + dx, Y1, 2, 1.2), [bo, bi] = rings(a, Y0, a + 3, Y1, 0, 0.8);
    put(card, prism(P, front, o, i, PT, z)); put(bar, prism(P, front, bo, bi, PT, z));
    const cy = (Y0 + Y1) / 2;
    const cx = a + 17, e = X1 + dx - 13, w = 1.3;
    icon.setAttribute("d", poly(ringAt(P, rrect(cx - 7.5, cy - 7.5, cx + 7.5, cy + 7.5, 7.5, 14), z)));
    tick.setAttribute("d", poly([[-4.4, 0.3], [-3, -1.1], [-1.2, 0.7], [3, -3.8], [4.4, -2.4], [-1.2, 3.4]].map(([u, v]) => P(cx + u, cy + v, z))));
    l1.setAttribute("d", flat(a + 33, cy - 2.6, a + 80, cy + 2.6, z));
    const dia = (x0, y0, x1, y1) => poly([[x0 - w, y0 + w], [x0 + w, y0 - w], [x1 + w, y1 - w], [x1 - w, y1 + w]].map(([u, v]) => P(u, v, z)));
    x.setAttribute("d", dia(e - 4, cy - 4, e + 4, cy + 4) + dia(e - 4, cy + 4, e + 4, cy - 4));
  }

  // the trigger button, as Primary on the Button figure: inked block, top lit on hover, dipped on press
  const [bro, bri] = rings(BX0, BY0, BX1, BY1, 0, 1.2);
  mk("path", { d: poly(ringAt(P, rrect(BX0 - 3, BY0 - 3, BX1 + 3, BY1 + 3, 0, 4), PT)), class: "nf lo" }, svg);
  const bg = mk("g", {}, svg), bsil = mk("path", { class: "dot", "data-part": "ink" }, bg), btop = mk("path", { class: "dot", "data-part": "ink-top" }, bg), bedge = mk("path", { class: "nf lo" }, bg);
  const bsp = spring(0, { k: 320, c: 30 });
  let bl = -1;
  function drawBtn() {
    const z = PT + BH - 3 * clamp(bsp.x, -0.6, 1.1);
    if (Math.abs(z - bl) < 0.01) return;
    bl = z;
    bsil.setAttribute("d", prism(P, front, bro, bri, PT, z).sil);
    const d = poly(ringAt(P, bro, z)); btop.setAttribute("d", d); bedge.setAttribute("d", d);
  }

  const rest = P(62, 34, PT + 10);
  const ax = spring(rest[0], { k: 140 }), ay = spring(rest[1], { k: 140 }), pr = spring(0);
  const cur = mk("path", { class: "dot", "data-part": "cursor" }, svg);
  const drawCur = () => cur.setAttribute("d", poly(ARROW.map(([u, v]) => [ax.x + u - 0.5, ay.x + v + 2.5 * clamp(pr.x, 0, 1)])));

  // the toast's motion is the component's: 300 ms, in on ease-decelerate-emphasized, out on ease-accelerate-generic
  const eIn = bezier(0.16, 0, 0.16, 1), eOut = bezier(0.36, 0.09, 1, 0.58);
  const slide = (now) => {
    if (t.t !== t.to) { t.from = t.x; t.to = t.t; t.t0 = now; }
    if (t.x === t.to) return false;
    const k = clamp((now - t.t0) / 300, 0, 1);
    t.x = reducedMotion() ? t.to : lerp(t.from, t.to, (t.to > t.from ? eIn : eOut)(k));
    return t.x !== t.to;
  };
  let act = -1, shown = 1, ghost = false, gt = 0, gdone = true;
  const say = () => { read.textContent = act === 0 && shown ? "toast" : act === 1 ? "trigger" : "rest"; };
  const setShown = (v) => { shown = v; t.t = v; tg.toggleAttribute("data-show", !!v); say(); };
  const press = (a) => {
    pr.x = 1; pr.t = 0;
    if (a === 0) { setShown(0); } else { bsp.x = 1; bsp.t = 0.35; if (!shown) setShown(1); }
    A.wake();
  };
  const A = register(stage, (dt, now) => {
    let m = false;
    if (ghost && act >= 0 && !gdone) { m = true; if (now - gt > 400) { gdone = true; press(act); } }
    if (slide(now)) m = true;
    for (const q of [lift, bsp, ax, ay, pr]) if (stepS(q, dt)) m = true;
    drawToast(); drawBtn(); drawCur();
    return m;
  });
  bag.add(A.unregister);

  // hit: the toast's resting top plane while shown (or sliding out), else only the button
  const pick = ([sx, sy]) => {
    let [x, y] = unproj(C, sx, sy, PT + h);
    if (shown && x > X0 - 2 && x < X1 + 2 && y > Y0 - 2 && y < Y1 + 2) return 0;
    [x, y] = unproj(C, sx, sy, PT + BH);
    return x > BX0 - 2 && x < BX1 + 2 && y > BY0 - 2 && y < BY1 + 2 ? 1 : -1;
  };
  function set(a, p) {
    if (a !== act) {
      act = a; gdone = !ghost; gt = performance.now();
      lift.t = a === 0 ? 1 : 0; bsp.t = a === 1 ? 0.35 : 0;
      card.sil.classList.toggle("hi", a === 0); btop.setAttribute("class", a === 1 ? "dot m" : "dot");
      say();
    }
    if (p) { ax.t = p[0]; ay.t = p[1]; } else { ax.t = rest[0]; ay.t = rest[1]; }
    A.wake();
  }
  bag.add(pointer(stage, {
    move: (p, e) => { ghost = e?.pointerType === "ghost"; set(pick(p), p); },
    down: (p) => { const a = pick(p); ghost = false; set(a, p); if (a >= 0) press(a); },
    leave: (e) => { if (e?.pointerType === "ghost") setShown(1); ghost = false; set(-1); },
  }));
  bag.add(() => svg.replaceChildren());

  drawToast(true); drawBtn(); drawCur();
  return { set: (v) => { h = v; t.last = ""; A.wake(); }, destroy: bag.dispose };
}

hairline({
  name: "toast",
  means: "A toast on a slab with a trigger button: a press on the toast slides it out, a press on the button slides it back in.",
  rules: [1, 4, 8, 9],
  range: [4, 6, 9],
  tour: [[219, 142], [133, 156], null],
  mount,
});
