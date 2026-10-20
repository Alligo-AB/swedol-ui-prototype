/**
 * E-Com Toast: a product box on a slab and a cart tray set into it. The pointer over the box lights it; a press
 * hops it into the cart, and a toast with a product tile and two buttons slides in at the back. A press on the
 * box again takes it out; a press on the toast closes it. A drawn cursor follows the pointer and rests above
 * the box. The slider is how high the box and the toast stand.
 */
const {
  Cam, bezier, clamp, facing, fit, lerp, poly, proj, open, ringAt, rrect, run, prism, rings,
  mk, pointer, reducedMotion, reflect, register, solid, put, disposer, spring, stepS, unproj,
} = HL;

const PW = 96, PD = 100, PT = 6, D = 2, BH = 12;
const BOX = { x0: 10, y0: 64, x1: 32, y1: 86 }, CART = { x0: 54, y0: 60, x1: 86, y1: 90 };
const TOAST = { x0: 8, y0: 8, x1: 88, y1: 46, h: 3 };
const ARROW = [[0, 0], [0, 15], [3.6, 11.6], [6.2, 17], [8.6, 15.8], [6, 10.6], [10.8, 10.6]];

function mount({ stage, svg, read }, value) {
  const bag = disposer();
  let lift = value;

  const C = Cam(45, 0.5, 2.3);
  fit(C, [[0, 0, 0], [PW, PD, 0], [PW, 0, 0], [0, PD, 0], [BOX.x0 + 40, 56, PT + 22], [TOAST.x1 + 30, 8, PT + 10]], 200, 172);
  const P = proj(C), front = facing(C);
  const quad = (x0, y0, x1, y1, z) => poly([P(x0, y0, z), P(x1, y0, z), P(x1, y1, z), P(x0, y1, z)]);

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

  // the toast (far side): a plate, a product tile, a name bar, a body bar, a blank and a primary button
  const [tOut, tIn] = rings(TOAST.x0, TOAST.y0, TOAST.x1, TOAST.y1, 0, 1.2);
  const tg = mk("g", {}, svg), toast = solid(tg);
  const tile = solid(tg);
  const tp = ["bar-on", "bar", "bar", "ink"].map((part) => mk("path", { class: "dot", "data-part": part }, tg));
  const [kOut, kIn] = rings(TOAST.x0 + 6, TOAST.y0 + 6, TOAST.x0 + 22, TOAST.y0 + 22, 0, 1.2);

  // the cart: a tray cut into the slab (floor, far wall, rim, near lip over the sunk box)
  const out = rrect(CART.x0, CART.y0, CART.x1, CART.y1, 3, 6);
  const far = run(out, (q) => !front(q)), near = run(out, front);
  const strip = (r) => poly([...ringAt(P, r, PT), ...ringAt(P, r, PT - D).reverse()]);
  const floor = mk("path", { d: poly(ringAt(P, out, PT - D)), class: "lo", "data-part": "track" }, svg);
  const wall = mk("path", { d: strip(far), class: "lo", "data-part": "track-wall" }, svg);
  mk("path", { d: poly(ringAt(P, out, PT - D)), class: "nf lo" }, svg);
  mk("path", { d: poly(ringAt(P, out, PT)), class: "nf" }, svg);
  const box = solid(mk("g", {}, svg));
  mk("path", { d: strip(near), class: "fo" }, svg);
  mk("path", { d: open(ringAt(P, near, PT)), class: "nf" }, svg);

  const bw = BOX.x1 - BOX.x0, bd = BOX.y1 - BOX.y0;
  const q = { b: { x: 0, t: 0, to: 0, from: 0, t0: 0, d: 400, e: bezier(0.35, 0, 0.35, 1) }, t: { x: 0, t: 0, to: 0, from: 0, t0: 0, d: 300, e: bezier(0.16, 0, 0.16, 1) } };
  let last = "";
  function draw(force) {
    const b = clamp(q.b.x, 0, 1), t = clamp(q.t.x, 0, 1), hv = clamp(bh.x, 0, 1);
    const key = b.toFixed(3) + t.toFixed(3) + hv.toFixed(2) + lift.toFixed(2);
    if (!force && key === last) return;
    last = key;
    // the box hops: x along the slab, z on an arc, landing sunk in the tray
    const cx = lerp(BOX.x0, CART.x0 + (CART.x1 - CART.x0 - bw) / 2, b), cy = lerp(BOX.y0, CART.y0 + (CART.y1 - CART.y0 - bd) / 2, b);
    const z0 = lerp(PT, PT - D + 0.6, b) + 4 * 14 * b * (1 - b), h = BH + lift - 1.5 * hv;
    const bo = rrect(cx, cy, cx + bw, cy + bd, 2, 4), bi = rrect(cx + 1.2, cy + 1.2, cx + bw - 1.2, cy + bd - 1.2, 1, 4);
    put(box, prism(P, front, bo, bi, z0, z0 + h));
    floor.setAttribute("class", b > 0.5 ? "dot" : "lo"); floor.setAttribute("data-part", b > 0.5 ? "ink" : "track");
    wall.setAttribute("class", b > 0.5 ? "dot" : "lo"); wall.setAttribute("data-part", b > 0.5 ? "ink-wall" : "track-wall");
    // the toast slides in from the right, dropping onto the slab
    const on = t > 0.01;
    tg.setAttribute("display", on ? "inline" : "none");
    if (!on) return;
    const dx = (1 - t) * 40, dz = (1 - t) * 10, z = PT + dz;
    const sh = (r) => r.map((s) => ({ ...s, u: s.u + dx }));
    put(toast, prism(P, front, sh(tOut), sh(tIn), z, z + TOAST.h + lift * 0.3));
    const zt = z + TOAST.h + lift * 0.3 + 0.1, x = TOAST.x0 + dx;
    put(tile, prism(P, front, sh(kOut), sh(kIn), zt, zt + 3));
    tp[0].setAttribute("d", quad(x + 28, TOAST.y0 + 8, x + 62, TOAST.y0 + 10.4, zt));
    tp[1].setAttribute("d", quad(x + 28, TOAST.y0 + 14, x + 70, TOAST.y0 + 15.8, zt));
    tp[2].setAttribute("d", quad(x + 8, TOAST.y1 - 9, x + 28, TOAST.y1 - 7.2, zt));
    tp[3].setAttribute("d", quad(x + 36, TOAST.y1 - 12, x + 72, TOAST.y1 - 5, zt));
  }
  const slide = (s, now) => {
    if (s.t !== s.to) { s.from = s.x; s.to = s.t; s.t0 = now; }
    if (s.x === s.to) return false;
    s.x = reducedMotion() ? s.to : s.from + (s.to - s.from) * s.e(clamp((now - s.t0) / s.d, 0, 1));
    return s.x !== s.to;
  };

  const rest = P(BOX.x1 - 2, (BOX.y0 + BOX.y1) / 2, PT + BH + 9);
  const ax = spring(rest[0], { k: 140 }), ay = spring(rest[1], { k: 140 }), pr = spring(0), bh = spring(0);
  const cur = mk("path", { class: "dot", "data-part": "cursor" }, svg);
  const drawCur = () => cur.setAttribute("d", poly(ARROW.map(([u, v]) => [ax.x + u - 0.5, ay.x + v + 2.5 * clamp(pr.x, 0, 1)])));

  let ghost = false, gt = 0, gdone = true, act = -1, added = 0, shown = 0;
  const A = register(stage, (dt, now) => {
    let m = false;
    if (ghost && act === 0 && !gdone) { m = true; if (now - gt > 250) { gdone = true; press(0); } }
    for (const s of [q.b, q.t]) if (slide(s, now)) m = true;
    for (const s of [ax, ay, pr, bh]) if (stepS(s, dt)) m = true;
    draw(); drawCur();
    return m;
  });
  bag.add(A.unregister);

  // hit: the box's resting top plane (while it is not in the cart), the cart, and the toast when it is meant to be shown
  const pick = ([sx, sy]) => {
    const [x, y] = unproj(C, sx, sy, PT + BH);
    if (x > BOX.x0 - 2 && x < BOX.x1 + 2 && y > BOX.y0 - 2 && y < BOX.y1 + 2 && !added) return 0;
    const [u, v] = unproj(C, sx, sy, PT);
    if (added && u > CART.x0 - 2 && u < CART.x1 + 2 && v > CART.y0 - 2 && v < CART.y1 + 2) return 0;
    return shown && u > TOAST.x0 && u < TOAST.x1 && v > TOAST.y0 && v < TOAST.y1 ? 1 : -1;
  };
  const say = () => { read.textContent = act === 1 ? "toast" : act === 0 ? (added ? "cart" : "box") : added ? "added" : "rest"; };
  const setAdded = (v) => { added = v; shown = v; q.b.t = v; q.t.t = v; q.t.d = v ? 300 : 150; q.t.e = v ? bezier(0.16, 0, 0.16, 1) : bezier(0.36, 0.09, 1, 0.58); };
  function press(a) {
    if (a === 0) setAdded(1 - added);
    else if (a === 1) { shown = 0; q.t.t = 0; q.t.d = 150; q.t.e = bezier(0.36, 0.09, 1, 0.58); }
    pr.x = 1; pr.t = 0; say(); A.wake();
  }
  function set(a, p) {
    if (a !== act) {
      act = a; gdone = !ghost; gt = performance.now();
      bh.t = a === 0 ? 1 : 0;
      box.sil.classList.toggle("hi", a === 0 || (a < 0 && !added));
      toast.sil.classList.toggle("hi", a === 1);
      say();
    }
    if (a < 0) { ax.t = rest[0]; ay.t = rest[1]; } else { ax.t = p[0]; ay.t = p[1]; }
    A.wake();
  }
  bag.add(pointer(stage, {
    move: (p, e) => { ghost = e?.pointerType === "ghost"; set(pick(p), p); gt = performance.now(); },
    down: (p) => { const a = pick(p); set(a, p); ghost = false; if (a >= 0) press(a); },
    leave: (e) => {
      if (e?.pointerType === "ghost") { setAdded(0); say(); }
      ghost = false; set(-1);
    },
  }));
  bag.add(() => svg.replaceChildren());

  box.sil.classList.add("hi");
  draw(true); drawCur();
  return { set: (v) => { lift = v; draw(true); }, destroy: bag.dispose };
}

hairline({
  name: "toast-ecom",
  means: "A product box and a cart tray set into a slab: a press hops the box into the cart and a toast with a product tile and two buttons slides in.",
  rules: [1, 4, 8, 9],
  range: [1, 2, 3],
  tour: [[104, 135], [226, 137], null],
  mount,
});
