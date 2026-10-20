/**
 * Range, as the component: the title and the value above, a thin track, a black round thumb, the step labels
 * under it, all on a slab. The pointer over the control lights a halo round the thumb; a press or drag snaps it
 * to the nearest step, and the value and the step label follow. A drawn cursor rests above the thumb. The slider
 * is how high the thumb stands.
 */
const {
  Cam, bezier, clamp, facing, fit, lerp, poly, proj, open, ringAt, rrect, run, prism, rings,
  mk, pointer, reducedMotion, reflect, register, solid, put, disposer, spring, stepS, unproj,
} = HL;

const PW = 124, PD = 64, PT = 6, R = 5, HR = 8.5, N = 6, REST = 2, X0 = 18, X1 = 106, TY = 30, U = 0.75, UL = 0.58, XR = PW - 8;
const VALUES = ["100", "150", "200", "300", "350", "450"];
const ARROW = [[0, 0], [0, 15], [3.6, 11.6], [6.2, 17], [8.6, 15.8], [6, 10.6], [10.8, 10.6]];
// condensed heavy capitals and digits as closed outlines, 8 high, u right, v up; a second outline is the counter
const G = {
  D: [[[0, 0], [3.8, 0], [5, 1.2], [5, 6.8], [3.8, 8], [0, 8]], [[1.6, 1.5], [3.2, 1.5], [3.4, 1.7], [3.4, 6.3], [3.2, 6.5], [1.6, 6.5]]],
  U: [[[0, 1.2], [1.2, 0], [3.8, 0], [5, 1.2], [5, 8], [3.4, 8], [3.4, 1.5], [1.6, 1.5], [1.6, 8], [0, 8]]],
  R: [[[0, 0], [1.6, 0], [1.6, 3], [2.6, 3], [3.4, 0], [5, 0], [4.2, 3.3], [5, 4.2], [5, 6.8], [3.8, 8], [0, 8]], [[1.6, 4.5], [3, 4.5], [3.4, 4.9], [3.4, 6.1], [3, 6.5], [1.6, 6.5]]],
  A: [[[0, 0], [1.6, 0], [1.9, 2.2], [3.1, 2.2], [3.4, 0], [5, 0], [3.6, 8], [1.4, 8]], [[2.2, 3.6], [2.8, 3.6], [2.5, 5.6]]],
  T: [[[1.8, 0], [3.4, 0], [3.4, 6.5], [5.2, 6.5], [5.2, 8], [0, 8], [0, 6.5], [1.8, 6.5]]],
  I: [[[0, 0], [1.6, 0], [1.6, 8], [0, 8]]],
  O: [[[0, 1.2], [1.2, 0], [3.8, 0], [5, 1.2], [5, 6.8], [3.8, 8], [1.2, 8], [0, 6.8]], [[1.6, 1.5], [3.4, 1.5], [3.4, 6.5], [1.6, 6.5]]],
  N: [[[0, 0], [1.6, 0], [1.6, 4.8], [3.4, 0], [5, 0], [5, 8], [3.4, 8], [3.4, 3.2], [1.6, 8], [0, 8]]],
  0: [[[0, 1.2], [1.2, 0], [3.8, 0], [5, 1.2], [5, 6.8], [3.8, 8], [1.2, 8], [0, 6.8]], [[1.6, 1.5], [3.4, 1.5], [3.4, 6.5], [1.6, 6.5]]],
  1: [[[1.8, 0], [3.4, 0], [3.4, 8], [1.9, 8], [0, 6.4], [0, 5.1], [1.8, 6.1]]],
  2: [[[0, 6.8], [1.2, 8], [3.8, 8], [5, 6.8], [5, 4.6], [1.8, 1.5], [5, 1.5], [5, 0], [0, 0], [0, 2.2], [3.4, 5.2], [3.4, 6.3], [3.2, 6.5], [1.8, 6.5], [1.6, 6.3], [1.6, 5.4], [0, 5.4]]],
  3: [[[0, 6.8], [1.2, 8], [3.8, 8], [5, 6.8], [5, 5], [4.4, 4], [5, 3], [5, 1.2], [3.8, 0], [1.2, 0], [0, 1.2], [0, 2.6], [1.6, 2.6], [1.6, 1.5], [3.4, 1.5], [3.4, 3.3], [2, 3.3], [2, 4.7], [3.4, 4.7], [3.4, 6.5], [1.6, 6.5], [1.6, 5.4], [0, 5.4]]],
  4: [[[3, 0], [4.6, 0], [4.6, 2], [5.4, 2], [5.4, 3.5], [4.6, 3.5], [4.6, 8], [3, 8], [0, 3.5], [0, 2], [3, 2]], [[3, 3.5], [1.7, 3.5], [3, 5.6]]],
  5: [[[0, 1.2], [1.2, 0], [3.8, 0], [5, 1.2], [5, 4.2], [3.8, 5.2], [1.6, 5.2], [1.6, 6.5], [5, 6.5], [5, 8], [0, 8], [0, 3.7], [3.4, 3.7], [3.4, 1.5], [1.6, 1.5], [1.6, 2.4], [0, 2.4]]],
};
const GW = (ch) => Math.max(...G[ch][0].map((q) => q[0]));
/** Text as world outlines, aligned at x (-1 left, 0 centre, 1 right) with its baseline at y: one list of [x, y] per outline. */
function text(str, x, y, align, U) {
  const adv = 1.2, total = [...str].reduce((s, ch) => s + GW(ch) + adv, -adv) * U;
  let cx = x - ((align + 1) / 2) * total;
  const out = [];
  for (const ch of str) {
    G[ch].forEach((s, k) => { const q = s.map(([u, v]) => [cx + u * U, y - v * U]); out.push(k ? q.reverse() : q); });
    cx += (GW(ch) + adv) * U;
  }
  return out;
}

function mount({ stage, svg, read }, value) {
  const bag = disposer();
  let lift = value;

  const C = Cam(45, 0.5, 2.1);
  fit(C, [[0, 0, 0], [PW, PD, 0], [PW, 0, 0], [0, PD, 0], [X1, TY, PT + 8]], 200, 172);
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

  const stepX = (i) => lerp(X0, X1, i / (N - 1));
  const flat = (strokes, z) => strokes.map((q) => poly(q.map(([x, y]) => P(x, y, z)))).join("");
  const mkText = (str, x, y, align, part, u = U) => mk("path", { d: flat(text(str, x, y, align, u), PT), class: "dot", "data-part": part }, svg);
  mkText("DURATION", 8, 14, -1, "title");
  const val = mkText(VALUES[REST], XR, 14, 1, "value");
  const labels = VALUES.map((v, i) => mkText(v, stepX(i), 52, 0, "tick", UL));
  // the track: a thin line on the slab; under the thumb a halo that shows on hover
  mk("path", { d: poly([[X0 - 4, TY - 1], [X1 + 4, TY - 1], [X1 + 4, TY + 1], [X0 - 4, TY + 1]].map(([u, v]) => P(u, v, PT))), class: "dot", "data-part": "line" }, svg);
  const halo = mk("path", { class: "dot", "data-part": "halo" }, svg);
  const thumb = solid(mk("g", {}, svg));
  thumb.sil.setAttribute("data-part", "thumb");

  const sp = { x: REST, t: REST, to: REST, from: REST, t0: 0 }, hv = spring(0);
  let step = REST, last = "";
  const tx = () => lerp(X0, X1, clamp(sp.x, 0, N - 1) / (N - 1));
  function draw(force) {
    const x = tx();
    const key = x.toFixed(2) + step;
    if (!force && key === last) return;
    last = key;
    const o = rrect(x - R, TY - R, x + R, TY + R, R, 14), i = rrect(x - R + 1.4, TY - R + 1.4, x + R - 1.4, TY + R - 1.4, R - 1.4, 14);
    put(thumb, prism(P, front, o, i, PT, PT + 0.25 * lift));
    halo.setAttribute("d", poly(ringAt(P, rrect(x - HR, TY - HR, x + HR, TY + HR, HR, 14), PT)));
    labels.forEach((t, k) => t.setAttribute("data-part", k === step ? "tick-on" : "tick"));
    val.setAttribute("d", flat(text(VALUES[step], XR, 14, 1, U), PT));
  }

  // the cursor: tip at (ax, ay) on screen, pressed down by pr
  const rest = P(stepX(REST) + 4, TY - 3, PT + 9);
  const ax = spring(rest[0], { k: 140 }), ay = spring(rest[1], { k: 140 }), pr = spring(0);
  const cur = mk("path", { class: "dot", "data-part": "cursor" }, svg);
  const drawCur = () => cur.setAttribute("d", poly(ARROW.map(([u, v]) => [ax.x + u - 0.5, ay.x + v + 2.5 * clamp(pr.x, 0, 1)])));

  // the thumb's slide: slower than the component's 150ms so a step reads as a glide; ease-standard
  const SLIDE = 360, ez = bezier(0.35, 0, 0.35, 1);
  const slide = (now) => {
    if (sp.t !== sp.to) { sp.from = sp.x; sp.to = sp.t; sp.t0 = now; }
    if (sp.x === sp.to) return false;
    sp.x = reducedMotion() ? sp.to : sp.from + (sp.to - sp.from) * ez(clamp((now - sp.t0) / SLIDE, 0, 1));
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
  const inBand = ([x, y]) => x > 4 && x < PW - 4 && y > 18 && y < 58;
  const nearest = (x) => Math.round(clamp((x - X0) / (X1 - X0), 0, 1) * (N - 1));
  let on = false, held = false, gin = false;
  const say = () => { read.textContent = on ? VALUES[step] : "rest"; };
  const goto = (k) => { step = k; sp.t = k; say(); A.wake(); };
  function set(p, a) {
    on = a;
    hv.t = a ? 1 : 0;
    halo.toggleAttribute("data-hover", a);
    if (a) { ax.t = p[0]; ay.t = p[1]; } else { ax.t = rest[0]; ay.t = rest[1]; }
    say(); A.wake();
  }
  bag.add(pointer(stage, {
    move: (p, e) => {
      const w = world(p), ghost = e?.pointerType === "ghost";
      if (!ghost && !(e?.buttons & 1)) held = false;
      // the tour's unseen pointer only counts once it reaches the thumb: no fumbling on the way in
      if (ghost && !gin) {
        if (Math.abs(w[0] - tx()) < 4 && inBand(w)) gin = true;
        else return;
      }
      set(p, held || inBand(w));
      if (on && (ghost || held)) goto(nearest(w[0]));
    },
    down: (p) => {
      const w = world(p);
      set(p, inBand(w));
      if (on) { held = true; pr.x = 1; pr.t = 0; goto(nearest(w[0])); }
    },
    leave: (e) => {
      held = false; gin = false;
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
  means: "A slab with the Range control: title, value, thin track, black thumb and step labels; a drag snaps the thumb step by step.",
  rules: [1, 4, 8, 9],
  range: [1, 2, 3],
  tour: [[190, 153], [216, 166], [242, 179], [268, 192], null],
  mount,
});
