/**
 * Range: one groove cut into a slab, a round thumb standing in it, five ticks along the near edge. The pointer
 * over the control sinks the thumb; a press or drag snaps it to the nearest step and inks the ticks it has
 * passed. A drawn cursor follows the pointer and rests above the thumb. The slider is how high the thumb stands.
 */
const {
  Cam, bezier, clamp, facing, fit, lerp, poly, proj, open, ringAt, rrect, run, prism, rings,
  mk, pointer, reducedMotion, reflect, register, solid, put, disposer, spring, stepS, unproj,
} = HL;

const PW = 96, PD = 64, PT = 6, D = 2, GX0 = 6, GX1 = 90, GY0 = 20, GY1 = 36, R = 6.5, IN = 2.5, N = 5, REST = 1;
const CY = (GY0 + GY1) / 2, X0 = GX0 + 8 + IN - 1, X1 = GX1 - 8 - IN + 1;
const ARROW = [[0, 0], [0, 15], [3.6, 11.6], [6.2, 17], [8.6, 15.8], [6, 10.6], [10.8, 10.6]];

function mount({ stage, svg, read }, value) {
  const bag = disposer();
  let lift = value;

  const C = Cam(45, 0.5, 2.5);
  fit(C, [[0, 0, 0], [PW, PD, 0], [PW, 0, 0], [0, PD, 0], [X1, CY, PT + 12]], 200, 172);
  const P = proj(C), front = facing(C);

  const [pOut, pIn] = rings(0, 0, PW, PD, 0, 1.6);
  if (stage.hasAttribute("data-flat")) {
    // a flat slab: no thickness, no reflection, only the top plane (its fill can be made see-through in CSS via data-part="slab")
    const sl = solid(mk("g", {}, svg));
    sl.sil.setAttribute("class", "sil"); sl.sil.setAttribute("data-part", "slab");
    sl.sil.setAttribute("d", poly(ringAt(P, pOut, PT))); sl.cr.setAttribute("d", poly(ringAt(P, pIn, PT)));
  } else {
    reflect(svg, mk("g", {}, svg), P, front, pOut, 0, 14);
    put(solid(mk("g", {}, svg)), prism(P, front, pOut, pIn, 0, PT));
    svg.lastChild.firstChild.setAttribute("class", "sil");
  }

  // ticks on the slab, along the near edge of the groove
  const stepX = (i) => lerp(X0, X1, i / (N - 1));
  const ticks = Array.from({ length: N }, (_, i) => {
    const x = stepX(i);
    return mk("path", { d: poly([[x - 0.9, 46], [x + 0.9, 46], [x + 0.9, 51], [x - 0.9, 51]].map(([u, v]) => P(u, v, PT))), class: "dot" }, svg);
  });

  // the groove: floor, far wall, rim; the thumb stands in it; the near lip then hides the sunk part
  const out = rrect(GX0, GY0, GX1, GY1, 8, 14);
  const far = run(out, (q) => !front(q)), near = run(out, front);
  const strip = (r) => poly([...ringAt(P, r, PT), ...ringAt(P, r, PT - D).reverse()]);
  const floor = mk("path", { d: poly(ringAt(P, out, PT - D)), class: "lo", "data-part": "track" }, svg);
  const wall = mk("path", { d: strip(far), class: "lo", "data-part": "track-wall" }, svg);
  mk("path", { d: poly(ringAt(P, out, PT - D)), class: "nf lo" }, svg);
  mk("path", { d: poly(ringAt(P, out, PT)), class: "nf" }, svg);
  const thumb = solid(mk("g", {}, svg));
  mk("path", { d: strip(near), class: "fo" }, svg);
  mk("path", { d: open(ringAt(P, near, PT)), class: "nf" }, svg);

  const sp = { x: REST, t: REST, to: REST, from: REST, t0: 0 }, hv = spring(0);
  let step = REST, last = "";
  const tx = () => lerp(X0, X1, clamp(sp.x, 0, N - 1) / (N - 1));
  function draw(force) {
    const z0 = PT - D + 0.6, z1 = PT + lift - 1.5 * clamp(hv.x, 0, 1), x = tx();
    const key = x.toFixed(2) + z1.toFixed(2) + step;
    if (!force && key === last) return;
    last = key;
    const o = rrect(x - R, CY - R, x + R, CY + R, R, 14), i = rrect(x - R + 1.6, CY - R + 1.6, x + R - 1.6, CY + R - 1.6, R - 1.6, 14);
    put(thumb, prism(P, front, o, i, z0, z1));
    ticks.forEach((t, k) => t.setAttribute("data-part", k <= step ? "tick-on" : "tick"));
  }

  // the cursor: tip at (ax, ay) on screen, pressed down by pr
  const rest = P(stepX(REST) + 1, CY - 1, PT + 9);
  const ax = spring(rest[0], { k: 140 }), ay = spring(rest[1], { k: 140 }), pr = spring(0);
  const cur = mk("path", { class: "dot", "data-part": "cursor" }, svg);
  const drawCur = () => cur.setAttribute("d", poly(ARROW.map(([u, v]) => [ax.x + u - 0.5, ay.x + v + 2.5 * clamp(pr.x, 0, 1)])));

  // the thumb's slide: 150ms on ease-standard, like the Range component's neighbours
  const ez = bezier(0.35, 0, 0.35, 1);
  const slide = (now) => {
    if (sp.t !== sp.to) { sp.from = sp.x; sp.to = sp.t; sp.t0 = now; }
    if (sp.x === sp.to) return false;
    sp.x = reducedMotion() ? sp.to : sp.from + (sp.to - sp.from) * ez(clamp((now - sp.t0) / 150, 0, 1));
    return sp.x !== sp.to;
  };
  const A = register(stage, (dt, now) => {
    let m = slide(now);
    for (const q of [hv, ax, ay, pr]) if (stepS(q, dt)) m = true;
    draw(); drawCur();
    return m;
  });
  bag.add(A.unregister);

  // hit: the control's resting band (groove and ticks), a fixed plane
  const world = ([sx, sy]) => unproj(C, sx, sy, PT);
  const inBand = ([x, y]) => x > GX0 - 2 && x < GX1 + 2 && y > GY0 - 4 && y < 54;
  const nearest = (x) => Math.round(clamp((x - X0) / (X1 - X0), 0, 1) * (N - 1));
  let on = false, held = false;
  const say = () => { read.textContent = on ? "step " + (step + 1) : "rest"; };
  const goto = (k) => { step = k; sp.t = k; say(); A.wake(); };
  function set(p, a) {
    on = a;
    hv.t = a ? 1 : 0;
    floor.toggleAttribute("data-hover", a); wall.toggleAttribute("data-hover", a);
    if (a) { ax.t = p[0]; ay.t = p[1]; } else { ax.t = rest[0]; ay.t = rest[1]; }
    say(); A.wake();
  }
  bag.add(pointer(stage, {
    move: (p, e) => {
      const w = world(p), ghost = e?.pointerType === "ghost";
      if (!ghost && !(e?.buttons & 1)) held = false;
      set(p, held || inBand(w));
      if (on && (ghost || held)) goto(nearest(w[0]));
    },
    down: (p) => {
      const w = world(p);
      set(p, inBand(w));
      if (on) { held = true; pr.x = 1; pr.t = 0; goto(nearest(w[0])); }
    },
    leave: (e) => {
      held = false;
      if (e?.pointerType === "ghost") goto(REST);
      set(null, false);
    },
  }));
  bag.add(() => svg.replaceChildren());

  thumb.sil.classList.add("hi");
  draw(true); drawCur();
  return { set: (v) => { lift = v; draw(true); }, destroy: bag.dispose };
}

hairline({
  name: "range",
  means: "A groove in a slab with a round thumb and five ticks: the pointer sinks the thumb, a drag snaps it along and inks the ticks passed.",
  rules: [1, 4, 8, 9],
  range: [1, 2, 3],
  tour: [[120, 190], [290, 120], null],
  mount,
});
