/**
 * Switch: two switches on a slab, Email on and SMS off. Each is a rounded track with a round thumb on it. The
 * pointer over one lifts its thumb and lights its edge; a press throws it across on a spring and inks or
 * empties the track. A drawn cursor follows the pointer and rests above Email's thumb. The slider is how high
 * the thumbs stand.
 */
const {
  Cam, bezier, clamp, facing, fit, lerp, poly, proj, open, ringAt, rrect, run, prism, rings,
  mk, pointer, reducedMotion, reflect, register, solid, put, disposer, spring, stepS, unproj,
} = HL;

const PW = 96, PD = 100, PT = 6, D = 2, TX0 = 16, TX1 = 80, R = 13, IN = 3;
const SW = [{ name: "email", y0: 14, y1: 46, on: 1 }, { name: "sms", y0: 54, y1: 86, on: 0 }];
const ARROW = [[0, 0], [0, 15], [3.6, 11.6], [6.2, 17], [8.6, 15.8], [6, 10.6], [10.8, 10.6]];

function mount({ stage, svg, read }, value) {
  const bag = disposer();
  let lift = value;

  const C = Cam(45, 0.5, 2.3);
  fit(C, [[0, 0, 0], [PW, PD, 0], [PW, 0, 0], [0, PD, 0], [TX1, 14, PT + 9]], 200, 172);
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

  const sws = SW.map((s) => {
    const cy = (s.y0 + s.y1) / 2;
    const out = rrect(TX0, s.y0, TX1, s.y1, 16, 14);
    const far = run(out, (q) => !front(q)), near = run(out, front);
    const strip = (r) => poly([...ringAt(P, r, PT), ...ringAt(P, r, PT - D).reverse()]);
    // a slot cut into the slab: floor, far wall, rim; the thumb stands in it; the near lip then hides the sunk part
    const floor = mk("path", { d: poly(ringAt(P, out, PT - D)), class: "lo" }, svg);
    const wall = mk("path", { d: strip(far), class: "lo" }, svg);
    mk("path", { d: poly(ringAt(P, out, PT - D)), class: "nf lo" }, svg); // floor edge, so an inked slot keeps its outline
    mk("path", { d: poly(ringAt(P, out, PT)), class: "nf" }, svg);
    const thumb = solid(mk("g", {}, svg));
    mk("path", { d: strip(near), class: "fo" }, svg);
    mk("path", { d: open(ringAt(P, near, PT)), class: "nf" }, svg);
    return { ...s, cy, floor, wall, thumb, sp: { x: s.on, t: s.on, to: s.on, from: s.on, t0: 0 }, hv: spring(0), on: s.on, init: s.on, last: "" };
  });

  const tx = (s) => lerp(TX0 + R + IN, TX1 - R - IN, clamp(s.sp.x, 0, 1));
  function draw(force) {
    for (const s of sws) {
      const z0 = PT - D + 0.6, z1 = PT + lift - 1.5 * clamp(s.hv.x, 0, 1), x = tx(s);
      const key = x.toFixed(2) + z1.toFixed(2) + s.on;
      if (!force && key === s.last) continue;
      s.last = key;
      const o = rrect(x - R, s.cy - R, x + R, s.cy + R, R, 14), i = rrect(x - R + 1.6, s.cy - R + 1.6, x + R - 1.6, s.cy + R - 1.6, R - 1.6, 14);
      put(s.thumb, prism(P, front, o, i, z0, z1));
      const ink = s.sp.x > 0.5;
      for (const [e, w] of [[s.floor, ""], [s.wall, "-wall"]]) { e.setAttribute("class", ink ? "dot" : "lo"); e.setAttribute("data-part", (ink ? "ink" : "track") + w); }
    }
  }

  // the cursor: tip at (ax, ay) on screen, pressed down by pr
  const rest = P(TX1 - R - IN, 30, PT + 9);
  const ax = spring(rest[0], { k: 140 }), ay = spring(rest[1], { k: 140 }), pr = spring(0);
  const cur = mk("path", { class: "dot", "data-part": "cursor" }, svg);
  const drawCur = () => cur.setAttribute("d", poly(ARROW.map(([u, v]) => [ax.x + u - 0.5, ay.x + v + 2.5 * clamp(pr.x, 0, 1)])));

  // the thumb's slide is the Switch component's: 150ms on ease-standard
  const ez = bezier(0.35, 0, 0.35, 1);
  const slide = (q, now) => {
    if (q.t !== q.to) { q.from = q.x; q.to = q.t; q.t0 = now; }
    if (q.x === q.to) return false;
    q.x = reducedMotion() ? q.to : q.from + (q.to - q.from) * ez(clamp((now - q.t0) / 150, 0, 1));
    return q.x !== q.to;
  };
  let ghost = false, gt = 0, gdone = true;
  const A = register(stage, (dt, now) => {
    let m = false;
    if (ghost && act >= 0 && !gdone) { m = true; if (now - gt > 250) { gdone = true; flip(act); } }
    for (const s of sws) { if (slide(s.sp, now)) m = true; if (stepS(s.hv, dt)) m = true; }
    for (const q of [ax, ay, pr]) if (stepS(q, dt)) m = true;
    draw(); drawCur();
    return m;
  });
  bag.add(A.unregister);

  // hit: each track's resting top plane
  const pick = ([sx, sy]) => {
    const [x, y] = unproj(C, sx, sy, PT);
    return sws.findIndex((s) => x > TX0 - 2 && x < TX1 + 2 && y > s.y0 - 2 && y < s.y1 + 2);
  };
  let act = -1;
  const flip = (a) => { const s = sws[a]; s.on = 1 - s.on; s.sp.t = s.on; pr.x = 1; pr.t = 0; say(); A.wake(); };
  const say = () => { read.textContent = act < 0 ? "rest" : sws[act].name + " " + (sws[act].on ? "on" : "off"); };
  function set(a, p) {
    if (a !== act) {
      act = a;
      gdone = !ghost; gt = performance.now();
      sws.forEach((s, i) => { s.hv.t = i === a ? 1 : 0; for (const e of [s.floor, s.wall]) { if (i === a) e.setAttribute("data-hover", ""); else e.removeAttribute("data-hover"); } s.thumb.sil.classList.toggle("hi", a < 0 ? i === 0 : i === a); });
      say();
    }
    if (a < 0) { ax.t = rest[0]; ay.t = rest[1]; } else { ax.t = p[0]; ay.t = p[1]; }
    A.wake();
  }
  bag.add(pointer(stage, {
    move: (p, e) => { ghost = e?.pointerType === "ghost"; set(pick(p), p); gt = performance.now(); },
    down: (p) => {
      const a = pick(p);
      set(a, p);
      ghost = false;
      if (a >= 0) flip(a);
    },
    leave: (e) => {
      if (e?.pointerType === "ghost") for (const s of sws) { s.on = s.init; s.sp.t = s.on; }
      ghost = false; set(-1);
    },
  }));
  bag.add(() => svg.replaceChildren());

  sws[0].thumb.sil.classList.add("hi");
  draw(true); drawCur();
  return { set: (v) => { lift = v; draw(true); }, destroy: bag.dispose };
}

hairline({
  name: "switch",
  means: "Two switches set into a slab, Email on and SMS off: the pointer lifts a thumb, a press slides it along its slot and inks the slot.",
  rules: [1, 4, 8, 9],
  range: [1, 2, 3],
  tour: [[259, 157], [135, 160], null],
  mount,
});
