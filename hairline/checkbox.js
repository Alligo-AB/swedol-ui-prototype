/**
 * Checkbox: three boxes set into a slab, one checked, one empty, one mixed. The pointer over a box lights it; a press
 * fills it black and draws its tick (an empty or mixed box becomes checked, a checked one empties). A drawn cursor
 * follows the pointer and rests above the empty box. The slider is how deep the boxes are cut.
 */
const {
  Cam, bezier, clamp, facing, fit, lerp, poly, proj, open, ringAt, rrect, run, prism, rings,
  mk, pointer, reducedMotion, reflect, register, solid, put, disposer, spring, stepS, unproj,
} = HL;

const PW = 116, PD = 56, PT = 6, BS = 24, Y0 = 16;
const BX = [{ name: "checked", x0: 12, st: 1 }, { name: "empty", x0: 46, st: 0 }, { name: "mixed", x0: 80, st: 2 }];
const ARROW = [[0, 0], [0, 15], [3.6, 11.6], [6.2, 17], [8.6, 15.8], [6, 10.6], [10.8, 10.6]];
const bar = ([x0, y0], [x1, y1], w) => { const l = Math.hypot(x1 - x0, y1 - y0), nx = (-(y1 - y0) / l) * w / 2, ny = ((x1 - x0) / l) * w / 2; return [[x0 + nx, y0 + ny], [x1 + nx, y1 + ny], [x1 - nx, y1 - ny], [x0 - nx, y0 - ny]]; };
const TICK = [bar([.2, .52], [.42, .74], .15), bar([.42, .74], [.8, .3], .15)]; // two bars in the unit box
const DASH = [[.22, .43], [.78, .43], [.78, .57], [.22, .57]];

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

  // each box is a raised tile (height D*0.5+0.5): side faces from the prism, the coloured top and the tick on it
  const bxs = BX.map((b) => {
    const out = rrect(b.x0, Y0, b.x0 + BS, Y0 + BS, 0, 14), inn = rrect(b.x0 + 1.4, Y0 + 1.4, b.x0 + BS - 1.4, Y0 + BS - 1.4, 0, 14);
    const tile = solid(mk("g", {}, svg));
    const top = mk("path", { d: "", class: "lo" }, svg);
    const mark = mk("path", { d: "", class: "fo", "data-part": "mark" }, svg);
    return { ...b, cy: Y0 + BS / 2, out, inn, tile, top, mark, sp: { x: b.st ? 1 : 0, t: b.st ? 1 : 0, to: b.st ? 1 : 0, from: 0, t0: 0 }, hv: spring(0), pz: spring(0), kind: b.st, init: b.st, last: "" };
  });

  const q = (b, u, v, z) => P(b.x0 + u * BS, Y0 + v * BS, z);
  const grow = (pts, k) => pts.map(([u, v]) => [0.5 + (u - 0.5) * k, 0.5 + (v - 0.5) * k]);
  function draw(force) {
    for (const b of bxs) {
      const x = clamp(b.sp.x, 0, 1), key = x.toFixed(2) + D.toFixed(2) + b.kind + b.pz.x.toFixed(2);
      if (!force && key === b.last) continue;
      b.last = key;
      const zt = PT + D * 0.5 + 0.5 - 1.5 * clamp(b.pz.x, 0, 1); // only a press sinks the tile, hover does not
      put(b.tile, prism(P, front, b.out, b.inn, PT, zt));
      b.top.setAttribute("d", poly(ringAt(P, b.out, zt)));
      const ink = x > 0.5;
      b.top.setAttribute("class", ink ? "dot" : "lo"); b.top.setAttribute("data-part", ink ? "ink" : "track");
      const k = Math.max(x, 0.001), z = zt + 0.1;
      const shapes = b.kind === 2 ? [DASH] : TICK;
      b.mark.setAttribute("d", x < 0.05 ? "" : shapes.map((sh) => poly(grow(sh, k).map(([u, v]) => q(b, u, v, z)))).join(" "));
    }
  }

  const rest = P(BX[1].x0 + BS / 2 + 4, Y0 - 2, PT + 9);
  const ax = spring(rest[0], { k: 140 }), ay = spring(rest[1], { k: 140 }), pr = spring(0);
  const cur = mk("path", { class: "dot", "data-part": "cursor" }, svg);
  const drawCur = () => cur.setAttribute("d", poly(ARROW.map(([u, v]) => [ax.x + u - 0.5, ay.x + v + 2.5 * clamp(pr.x, 0, 1)])));

  // the tick's draw-in is the Checkbox's: 150ms on ease-standard (state change)
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
    for (const b of bxs) { if (slide(b.sp, now)) m = true; if (stepS(b.hv, dt)) m = true; if (stepS(b.pz, dt)) m = true; if (b.sp.x === 0 && b.sp.t === 0) b.kind = 0; }
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
  const flip = (a) => { const b = bxs[a]; if (b.sp.t === 1 && b.kind === 1) b.sp.t = 0; else { b.kind = 1; b.sp.t = 1; } pr.x = 1; pr.t = 0; b.pz.x = 1; b.pz.t = 0; say(); A.wake(); };
  const label = (b) => (b.sp.t === 0 ? "empty" : b.kind === 2 ? "mixed" : "checked");
  const say = () => { read.textContent = act < 0 ? "rest" : label(bxs[act]); };
  function set(a, p) {
    if (a !== act) {
      act = a;
      gdone = !ghost; gt = performance.now();
      bxs.forEach((b, i) => { b.hv.t = i === a ? 1 : 0; if (i === a) b.top.setAttribute("data-hover", ""); else b.top.removeAttribute("data-hover"); });
      say();
    }
    if (a < 0) { ax.t = rest[0]; ay.t = rest[1]; } else { ax.t = p[0]; ay.t = p[1]; }
    A.wake();
  }
  bag.add(pointer(stage, {
    move: (p, e) => {
      if (e?.pointerType === "ghost" && !ghost) for (const b of bxs) { b.kind = 0; b.sp.t = 0; } // the tour starts from three empty boxes
      ghost = e?.pointerType === "ghost"; set(pick(p), p); gt = performance.now(); },
    down: (p) => { const a = pick(p); set(a, p); ghost = false; if (a >= 0) flip(a); },
    leave: (e) => {
      if (e?.pointerType === "ghost") for (const b of bxs) { b.kind = b.init; b.sp.t = b.init ? 1 : 0; }
      ghost = false; set(-1);
    },
  }));
  bag.add(() => svg.replaceChildren());

  draw(true); drawCur();
  return { set: (v) => { D = v; draw(true); }, destroy: bag.dispose };
}

hairline({
  name: "checkbox",
  means: "Three checkboxes set into a slab, checked, empty and mixed: the pointer lights a box, a press fills it black and draws the tick.",
  rules: [1, 4, 8, 9],
  range: [1, 2, 4],
  tour: [[140, 129], [200, 159], [260, 189], [140, 129], [200, 159], [260, 189]],
  mount,
});
