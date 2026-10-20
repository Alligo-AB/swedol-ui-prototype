/**
 * Radio button: three radios set into a slab, one chosen. The pointer over a radio lights it; a press sinks the dot
 * out of the old choice and grows it in the new one (a chosen radio stays chosen). A drawn cursor follows the
 * pointer and rests above the middle radio. The slider is how deep the wells are cut.
 */
const {
  Cam, bezier, clamp, facing, fit, lerp, poly, proj, open, ringAt, rrect, run, prism, rings,
  mk, pointer, reducedMotion, reflect, register, solid, put, disposer, spring, stepS, unproj,
} = HL;

const PW = 116, PD = 56, PT = 6, BS = 24, Y0 = 16;
const BX = [{ name: "first", x0: 12, st: 1 }, { name: "second", x0: 46, st: 0 }, { name: "third", x0: 80, st: 0 }];
const ARROW = [[0, 0], [0, 15], [3.6, 11.6], [6.2, 17], [8.6, 15.8], [6, 10.6], [10.8, 10.6]];
const DOT = Array.from({ length: 20 }, (_, i) => [.5 + .24 * Math.cos(i * Math.PI / 10), .5 + .24 * Math.sin(i * Math.PI / 10)]); // the dot in the unit box

function mount({ stage, svg, read }, value) {
  const bag = disposer();
  let D = value;

  const C = Cam(45, 0.5, 2.5);
  fit(C, [[0, 0, 0], [PW, PD, 0], [PW, 0, 0], [0, PD, 0], [BX[1].x0 + BS - 2, Y0 + 4, PT + 9]], 200, 172);
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

  const bxs = BX.map((b) => {
    const out = rrect(b.x0, Y0, b.x0 + BS, Y0 + BS, BS / 2, 14);
    const far = run(out, (q) => !front(q)), near = run(out, front);
    const strip = (r) => poly([...ringAt(P, r, PT), ...ringAt(P, r, PT - D).reverse()]);
    const floor = mk("path", { d: "", class: "lo" }, svg);
    const wall = mk("path", { d: "", class: "lo" }, svg);
    const fe = mk("path", { d: "", class: "nf lo", "data-part": "rim" }, svg);
    const rim = mk("path", { d: poly(ringAt(P, out, PT)), class: "nf", "data-part": "rim" }, svg);
    const mark = mk("path", { d: "", class: "fo", "data-part": "mark" }, svg);
    const lip = mk("path", { d: "", class: "fo" }, svg);
    const lipLine = mk("path", { d: open(ringAt(P, near, PT)), class: "nf", "data-part": "rim" }, svg);
    return { ...b, cy: Y0 + BS / 2, out, far, near, strip, floor, wall, fe, mark, lip, sp: { x: b.st ? 1 : 0, t: b.st ? 1 : 0, to: b.st ? 1 : 0, from: 0, t0: 0 }, hv: spring(0), kind: b.st, init: b.st, last: "" };
  });

  const q = (b, u, v, z) => P(b.x0 + u * BS, Y0 + v * BS, z);
  const grow = (pts, k) => pts.map(([u, v]) => [0.5 + (u - 0.5) * k, 0.5 + (v - 0.5) * k]);
  function draw(force) {
    for (const b of bxs) {
      const x = clamp(b.sp.x, 0, 1), key = x.toFixed(2) + D.toFixed(2) + b.kind + b.hv.x.toFixed(2);
      if (!force && key === b.last) continue;
      b.last = key;
      const zf = PT - D;
      b.floor.setAttribute("d", poly(ringAt(P, b.out, zf)));
      b.fe.setAttribute("d", poly(ringAt(P, b.out, zf)));
      b.wall.setAttribute("d", poly([...ringAt(P, b.far, PT), ...ringAt(P, b.far, zf).reverse()]));
      b.lip.setAttribute("d", b.strip(b.near));
      for (const [e, w] of [[b.floor, ""], [b.wall, "-wall"]]) e.setAttribute("data-part", "track" + w);
      const k = Math.max(x, 0.001), z = zf + 0.1;
      b.mark.setAttribute("d", x < 0.05 ? "" : poly(grow(DOT, k).map(([u, v]) => q(b, u, v, z))));
    }
  }

  const rest = P(BX[1].x0 + BS / 2 + 4, Y0 - 2, PT + 9);
  const ax = spring(rest[0], { k: 140 }), ay = spring(rest[1], { k: 140 }), pr = spring(0);
  const cur = mk("path", { class: "dot", "data-part": "cursor" }, svg);
  const drawCur = () => cur.setAttribute("d", poly(ARROW.map(([u, v]) => [ax.x + u - 0.5, ay.x + v + 2.5 * clamp(pr.x, 0, 1)])));

  // the dot's grow-in is the Radio's: 150ms on ease-standard (state change)
  const ez = bezier(0.35, 0, 0.35, 1);
  const slide = (s, now) => {
    if (s.t !== s.to) { s.from = s.x; s.to = s.t; s.t0 = now; }
    if (s.x === s.to) return false;
    s.x = reducedMotion() ? s.to : s.from + (s.to - s.from) * ez(clamp((now - s.t0) / 150, 0, 1));
    return s.x !== s.to;
  };
  let ghost = false, gt = 0, gdone = true;
  const A = register(stage, (dt, now) => {
    let m = false;
    if (ghost && act >= 0 && !gdone) { m = true; if (now - gt > 250) { gdone = true; flip(act); } }
    for (const b of bxs) { if (slide(b.sp, now)) m = true; if (stepS(b.hv, dt)) m = true; }
    for (const s of [ax, ay, pr]) if (stepS(s, dt)) m = true;
    draw(); drawCur();
    return m;
  });
  bag.add(A.unregister);

  const pick = ([sx, sy]) => {
    const [x, y] = unproj(C, sx, sy, PT);
    return bxs.findIndex((b) => x > b.x0 - 2 && x < b.x0 + BS + 2 && y > Y0 - 2 && y < Y0 + BS + 2);
  };
  let act = -1;
  // empty or mixed -> checked; checked -> empty
  // a press chooses; the old choice's dot shrinks out, a chosen radio stays chosen
  const flip = (a) => { bxs.forEach((b, i) => { b.kind = i === a ? 1 : 0; b.sp.t = b.kind; }); pr.x = 1; pr.t = 0; say(); A.wake(); };
  const say = () => { read.textContent = act < 0 ? "rest" : bxs[act].name + (bxs[act].sp.t ? " chosen" : ""); };
  function set(a, p) {
    if (a !== act) {
      act = a;
      gdone = !ghost; gt = performance.now();
      bxs.forEach((b, i) => { b.hv.t = i === a ? 1 : 0; for (const e of [b.floor, b.wall]) { if (i === a) e.setAttribute("data-hover", ""); else e.removeAttribute("data-hover"); } });
      say();
    }
    if (a < 0) { ax.t = rest[0]; ay.t = rest[1]; } else { ax.t = p[0]; ay.t = p[1]; }
    A.wake();
  }
  bag.add(pointer(stage, {
    move: (p, e) => { ghost = e?.pointerType === "ghost"; set(pick(p), p); gt = performance.now(); },
    down: (p) => { const a = pick(p); set(a, p); ghost = false; if (a >= 0) flip(a); },
    leave: (e) => {
      if (e?.pointerType === "ghost") for (const b of bxs) { b.kind = b.init; b.sp.t = b.init; }
      ghost = false; set(-1);
    },
  }));
  bag.add(() => svg.replaceChildren());

  draw(true); drawCur();
  return { set: (v) => { D = v; draw(true); }, destroy: bag.dispose };
}

hairline({
  name: "radio",
  means: "Three radios set into a slab, one chosen: the pointer lights a radio, a press moves the black dot to it.",
  rules: [1, 4, 8, 9],
  range: [1, 2, 4],
  tour: [[140, 129], [200, 159], [260, 189], null],
  mount,
});
