/**
 * E-Com Toast: the "added to cart" toast itself, standing on a slab: a product tile, a bold name and a line of
 * text, a close mark, a blank and a primary button. The pointer over it lifts it; a press closes it (it slides out
 * to the right) and after a pause it slides back in. A drawn cursor follows the pointer and rests above the
 * primary button. The slider is how high the toast stands.
 */
const {
  Cam, bezier, clamp, facing, fit, lerp, poly, proj, open, ringAt, rrect, run, prism, rings,
  mk, pointer, reducedMotion, reflect, register, solid, put, disposer, spring, stepS, unproj,
} = HL;

const PW = 96, PD = 100, PT = 6;
const T = { x0: 6, y0: 30, x1: 90, y1: 70, h: 3 };
const ARROW = [[0, 0], [0, 15], [3.6, 11.6], [6.2, 17], [8.6, 15.8], [6, 10.6], [10.8, 10.6]];

function mount({ stage, svg, read }, value) {
  const bag = disposer();
  let lift = value;

  const C = Cam(45, 0.5, 2.3);
  fit(C, [[0, 0, 0], [PW, PD, 0], [PW, 0, 0], [0, PD, 0], [T.x1 + 30, T.y0, PT + 12]], 200, 172);
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

  // the toast: a plate, a product tile, a name bar, text, a close mark, a blank and a primary button
  const [tOut, tIn] = rings(T.x0, T.y0, T.x1, T.y1, 0, 1.2);
  const [kOut, kIn] = rings(T.x0 + 4, T.y0 + 5, T.x0 + 18, T.y0 + 19, 0, 1);
  const toast = solid(mk("g", {}, svg)), tile = solid(mk("g", {}, svg));
  const tp = ["bar-on", "bar", "bar", "bar-on", "bar-on", "ink"].map((part) => mk("path", { class: "dot", "data-part": part }, svg));

  const q = { x: 1, t: 1, to: 1, from: 1, t0: 0, d: 300, e: bezier(0.16, 0, 0.16, 1) };
  const hv = spring(0);
  let last = "";
  function draw(force) {
    const t = clamp(q.x, 0, 1), h = clamp(hv.x, 0, 1), key = t.toFixed(3) + h.toFixed(2) + lift.toFixed(2);
    if (!force && key === last) return;
    last = key;
    const on = t > 0.01;
    for (const e of [toast.g, tile.g, ...tp]) e.setAttribute("display", on ? "inline" : "none");
    if (!on) return;
    // it slides in from the right, dropping onto the slab
    const dx = (1 - t) * 40, z = PT + (1 - t) * 10, top = z + T.h + lift * 0.3 + 1.2 * h, zt = top + 0.1, x = T.x0 + dx, y = T.y0;
    const sh = (r) => r.map((s) => ({ ...s, u: s.u + dx }));
    put(toast, prism(P, front, sh(tOut), sh(tIn), z, top));
    put(tile, prism(P, front, sh(kOut), sh(kIn), zt, zt + 2));
    const bar = (i, u0, u1, v, hh) => tp[i].setAttribute("d", quad(x + u0, y + v, x + u1, y + v + hh, zt));
    bar(0, 22, 52, 6, 3); bar(1, 54, 70, 6, 2.6); bar(2, 22, 46, 13, 2.6);
    const d = (u, v) => P(x + 77 + u, y + 7.5 + v, zt);
    tp[3].setAttribute("d", poly([d(-2, -2.6), d(-2.6, -2), d(2, 2.6), d(2.6, 2)]) + poly([d(2, -2.6), d(2.6, -2), d(-2, 2.6), d(-2.6, 2)]));
    bar(4, 4, 22, 29.5, 2.2); bar(5, 30, 80, 25, 10);
  }
  const ez = { in: bezier(0.16, 0, 0.16, 1), out: bezier(0.36, 0.09, 1, 0.58) };
  const slide = (now) => {
    if (q.t !== q.to) { q.from = q.x; q.to = q.t; q.t0 = now; q.d = q.t ? 300 : 150; q.e = q.t ? ez.in : ez.out; }
    if (q.x === q.to) return false;
    q.x = reducedMotion() ? q.to : q.from + (q.to - q.from) * q.e(clamp((now - q.t0) / q.d, 0, 1));
    return q.x !== q.to;
  };

  const rest = P(T.x0 + 66, T.y0 + 20, PT + T.h + 9);
  const ax = spring(rest[0], { k: 140 }), ay = spring(rest[1], { k: 140 }), pr = spring(0);
  const cur = mk("path", { class: "dot", "data-part": "cursor" }, svg);
  const drawCur = () => cur.setAttribute("d", poly(ARROW.map(([u, v]) => [ax.x + u - 0.5, ay.x + v + 2.5 * clamp(pr.x, 0, 1)])));

  let ghost = false, gt = 0, gdone = true, act = -1, back = 0;
  const A = register(stage, (dt, now) => {
    let m = slide(now);
    if (ghost && act === 0 && !gdone) { m = true; if (now - gt > 250) { gdone = true; press(); } }
    if (back) { m = true; if (now > back) { back = 0; q.t = 1; } }
    for (const s of [ax, ay, pr, hv]) if (stepS(s, dt)) m = true;
    draw(); drawCur();
    return m;
  });
  bag.add(A.unregister);

  // hit: the toast's resting top plane, while it is meant to be shown
  const pick = ([sx, sy]) => {
    const [x, y] = unproj(C, sx, sy, PT + T.h);
    return q.t && x > T.x0 && x < T.x1 && y > T.y0 && y < T.y1 ? 0 : -1;
  };
  const say = () => { read.textContent = act === 0 ? "toast" : q.t ? "rest" : "closed"; };
  function press() { q.t = 0; back = performance.now() + 900; pr.x = 1; pr.t = 0; say(); A.wake(); }
  function set(a, p) {
    if (a !== act) {
      act = a; gdone = !ghost; gt = performance.now();
      hv.t = a === 0 ? 1 : 0;
      toast.sil.classList.toggle("hi", a === 0 || a < 0);
      say();
    }
    if (a < 0) { ax.t = rest[0]; ay.t = rest[1]; } else { ax.t = p[0]; ay.t = p[1]; }
    A.wake();
  }
  bag.add(pointer(stage, {
    move: (p, e) => { ghost = e?.pointerType === "ghost"; set(pick(p), p); gt = performance.now(); },
    down: (p) => { const a = pick(p); set(a, p); ghost = false; if (a === 0) press(); },
    leave: (e) => {
      if (e?.pointerType === "ghost") { back = 0; q.t = 1; say(); }
      ghost = false; set(-1);
    },
  }));
  bag.add(() => svg.replaceChildren());

  toast.sil.classList.add("hi");
  draw(true); drawCur();
  return { set: (v) => { lift = v; draw(true); }, destroy: bag.dispose };
}

hairline({
  name: "toast-ecom",
  means: "The added-to-cart toast on a slab: a press closes it, it slides out, then back in.",
  rules: [1, 4, 8, 9],
  range: [1, 2, 3],
  tour: [[154, 131], [272, 175], null],
  mount,
});
