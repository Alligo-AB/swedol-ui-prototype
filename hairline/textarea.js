/**
 * Textarea: a tall text box cut into a slab, label over it, hint under it. The pointer over the box blackens the
 * rim, turns the arrow into a blinking text caret and types three lines in; a press focuses (second rim line).
 * The pointer over the resizer corner (two short strokes) stretches the box taller. The slider is the slot's depth.
 */
const {
  Cam, rrect, clamp, facing, fit, poly, proj, open, seg, run, ringAt, prism, rings,
  mk, pointer, reducedMotion, reflect, register, solid, put, disposer, spring, stepS, unproj,
} = HL;

const PW = 96, PD = 100, PT = 6, FX0 = 8, FX1 = 88, FY0 = 24, FY1 = 62, GROW = 12, LINES = ["THE ORDER", "CAME ON TIME", "AND FINE"], PLH = "PLACEHOLDER", KEY = 70;
const IBEAM = [[-2, -5.5], [2, -5.5], [2, -4.5], [0.5, -4.5], [0.5, 4.5], [2, 4.5], [2, 5.5], [-2, 5.5], [-2, 4.5], [-0.5, 4.5], [-0.5, -4.5], [-2, -4.5]]; // a text caret lying on the field's floor
// condensed heavy capitals and digits as closed outlines (as in the Button figure), 8 high, u right, v up; a second outline is a counter
const G = {
  O: [[[0, 1.2], [1.2, 0], [3.8, 0], [5, 1.2], [5, 6.8], [3.8, 8], [1.2, 8], [0, 6.8]], [[1.6, 1.5], [3.4, 1.5], [3.4, 6.5], [1.6, 6.5]]],
  R: [[[0, 0], [1.6, 0], [1.6, 3], [2.6, 3], [3.4, 0], [5, 0], [4.2, 3.3], [5, 4.2], [5, 6.8], [3.8, 8], [0, 8]], [[1.6, 4.5], [3, 4.5], [3.4, 4.9], [3.4, 6.1], [3, 6.5], [1.6, 6.5]]],
  P: [[[0, 0], [1.6, 0], [1.6, 3], [3.8, 3], [5, 4.2], [5, 6.8], [3.8, 8], [0, 8]], [[1.6, 4.5], [3, 4.5], [3.4, 4.9], [3.4, 6.1], [3, 6.5], [1.6, 6.5]]],
  D: [[[0, 0], [3.8, 0], [5, 1.2], [5, 6.8], [3.8, 8], [0, 8]], [[1.6, 1.5], [3.2, 1.5], [3.4, 1.7], [3.4, 6.3], [3.2, 6.5], [1.6, 6.5]]],
  E: [[[0, 0], [5, 0], [5, 1.5], [1.6, 1.5], [1.6, 3.3], [4.4, 3.3], [4.4, 4.7], [1.6, 4.7], [1.6, 6.5], [5, 6.5], [5, 8], [0, 8]]],
  N: [[[0, 0], [1.6, 0], [1.6, 4.8], [3.4, 0], [5, 0], [5, 8], [3.4, 8], [3.4, 3.2], [1.6, 8], [0, 8]]],
  U: [[[0, 1.2], [1.2, 0], [3.8, 0], [5, 1.2], [5, 8], [3.4, 8], [3.4, 1.5], [1.6, 1.5], [1.6, 8], [0, 8]]],
  M: [[[0, 0], [1.6, 0], [1.6, 5], [3, 2], [4.4, 5], [4.4, 0], [6, 0], [6, 8], [4.2, 8], [3, 5.2], [1.8, 8], [0, 8]]],
  B: [[[0, 0], [3.8, 0], [5, 1.2], [5, 3.2], [4.4, 4], [5, 4.8], [5, 6.8], [3.8, 8], [0, 8]], [[1.6, 1.5], [3.2, 1.5], [3.4, 1.7], [3.4, 3.1], [3.2, 3.3], [1.6, 3.3]], [[1.6, 4.7], [3.2, 4.7], [3.4, 4.9], [3.4, 6.3], [3.2, 6.5], [1.6, 6.5]]],
  L: [[[0, 0], [5, 0], [5, 1.5], [1.6, 1.5], [1.6, 8], [0, 8]]],
  H: [[[0, 0], [1.6, 0], [1.6, 3.3], [3.4, 3.3], [3.4, 0], [5, 0], [5, 8], [3.4, 8], [3.4, 4.7], [1.6, 4.7], [1.6, 8], [0, 8]]],
  A: [[[0, 0], [1.6, 0], [1.9, 2.2], [3.1, 2.2], [3.4, 0], [5, 0], [3.6, 8], [1.4, 8]], [[2.2, 3.6], [2.8, 3.6], [2.5, 5.6]]],
  C: [[[0, 1.2], [1.2, 0], [3.8, 0], [5, 1.2], [5, 2.6], [3.4, 2.6], [3.4, 1.5], [1.6, 1.5], [1.6, 6.5], [3.4, 6.5], [3.4, 5.4], [5, 5.4], [5, 6.8], [3.8, 8], [1.2, 8], [0, 6.8]]],
  F: [[[0, 0], [1.6, 0], [1.6, 3.3], [4.4, 3.3], [4.4, 4.7], [1.6, 4.7], [1.6, 6.5], [5, 6.5], [5, 8], [0, 8]]],
  Y: [[[0, 8], [1.7, 8], [2.5, 5], [3.3, 8], [5, 8], [3.3, 3.6], [3.3, 0], [1.7, 0], [1.7, 3.6]]],
  I: [[[0, 0], [1.6, 0], [1.6, 8], [0, 8]]],
  T: [[[1.7, 0], [3.3, 0], [3.3, 6.5], [5, 6.5], [5, 8], [0, 8], [0, 6.5], [1.7, 6.5]]],
  ".": [[[0, 0], [1.6, 0], [1.6, 1.6], [0, 1.6]]],
  1: [[[1.8, 0], [3.4, 0], [3.4, 8], [2, 8], [0, 6.2], [0, 4.9], [1.8, 6.2]]],
  2: [[[0, 0], [5, 0], [5, 1.5], [1.8, 1.5], [5, 4.2], [5, 6.8], [3.8, 8], [1.2, 8], [0, 6.8], [0, 5.4], [1.6, 5.4], [1.6, 6.5], [3.4, 6.5], [3.4, 5], [0, 2.2]]],
  4: [[[3, 0], [4.6, 0], [4.6, 2], [5, 2], [5, 3.4], [4.6, 3.4], [4.6, 8], [2.6, 8], [0, 3.6], [0, 2], [3, 2]], [[1.9, 3.4], [3, 3.4], [3, 5.4]]],
  8: [[[1.2, 0], [3.8, 0], [5, 1.2], [5, 3.2], [4.4, 4], [5, 4.8], [5, 6.8], [3.8, 8], [1.2, 8], [0, 6.8], [0, 4.8], [0.6, 4], [0, 3.2], [0, 1.2]], [[1.6, 4.7], [3.4, 4.7], [3.4, 6.5], [1.6, 6.5]], [[1.6, 1.5], [3.4, 1.5], [3.4, 3.3], [1.6, 3.3]]],
};
G[0] = G.O; // zero is the O
const GW = (ch) => (ch === " " ? 2 : Math.max(...G[ch][0].map((q) => q[0])));
/** text laid out along +x from x0, centred on yc, glyph height 8*u: [{ x0, x1, outs }] one per char (outs are world [x, y] outlines) */
function lay(text, x0, yc, u) {
  let x = x0;
  return [...text].map((ch) => {
    const outs = ch === " " ? [] : G[ch].map((s, k) => { const q = s.map(([a, b]) => [x + a * u, yc - (b - 4) * u]); return k ? q.reverse() : q; });
    const r = { x0: x, x1: x + GW(ch) * u, outs };
    x += (GW(ch) + 1.2) * u;
    return r;
  });
}
const flat = (P, z, ls) => ls.map((l) => l.outs.map((o) => poly(o.map(([x, y]) => P(x, y, z)))).join("")).join("");
const ARROW = [[0, 0], [0, 15], [3.6, 11.6], [6.2, 17], [8.6, 15.8], [6, 10.6], [10.8, 10.6]];

function mount({ stage, svg, read }, value) {
  const bag = disposer();
  let lift = value;

  const C = Cam(45, 0.5, 2.3);
  fit(C, [[0, 0, 0], [PW, PD, 0], [PW, 0, 0], [0, PD, 0], [FX1, FY1 + GROW, PT + 14]], 200, 172);
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

  // flat text on the slab: label over the box, helper text under the largest box
  mk("path", { d: flat(P, PT, lay("COMMENT", FX0, 15, 0.7)), class: "dot", "data-part": "label" }, svg);
  mk("path", { d: flat(P, PT, lay("ADD MORE DETAIL.", FX0, 90, 0.36)), class: "dot", "data-part": "hint" }, svg);

  // the box: a slot cut into the slab (floor, far wall, rim, near lip); its rim is the state (grey, black on hover, doubled on focus)
  const rect = (a, y1) => rrect(FX0 + a, FY0 + a, FX1 - a, y1 - a, 0.5, 3);
  const D = 0 + lift, zf = PT - D; // lift is the slot's depth
  const strip = (r) => poly([...ringAt(P, r, PT), ...ringAt(P, r, zf).reverse()]);
  const slot = mk("g", {}, svg);
  const TU = 0.6, TX = FX0 + 5, LY = (k) => FY0 + 7 + k * 8;
  const lines = LINES.map((t, k) => lay(t, TX, LY(k), TU));
  const flatC = lines.flat();
  const tx = (i) => { const a = flatC[i - 1], k = lines.findIndex((l) => l.includes(a)); return a ? [a.x1 + 1.8 * TU, LY(k)] : [TX - 0.3, LY(0)]; }; // the caret's place after i marks
  const ph = mk("path", { class: "dot", "data-part": "ph" }, svg);
  const chars = flatC.map(() => mk("path", { class: "dot", "data-part": "ink" }, svg));
  const inner = mk("path", { class: "nf" }, svg); // second line of the focused edge, on the floor
  const grip = mk("path", { class: "nf" }, svg); // the resizer: two short strokes in the floor's corner
  const lip = mk("path", { class: "fo" }, svg), rimN = mk("path", { class: "nf" }, svg), rim = mk("path", { class: "nf" }, svg);
  slot.replaceChildren();
  // order matters: floor, wall, rim, marks, then the near lip over the sunk part
  const floor = mk("path", { class: "fo" }, slot), wall = mk("path", { class: "lo", "data-part": "track-wall" }, slot);
  slot.append(rim);
  svg.append(ph, ...chars, inner, grip, lip, rimN);

  let focus = 0, n = 0, nt = 0, over = false, corner = false, nextKey = 0;
  const g = spring(0, { k: 120 }); // how far the box has been stretched
  function draw() {
    const y1 = FY1 + g.x, out = rect(0, y1), far = run(out, (q) => !front(q)), near = run(out, front);
    floor.setAttribute("d", poly(ringAt(P, out, zf)));
    wall.setAttribute("d", strip(far));
    rim.setAttribute("d", poly(ringAt(P, out, PT)));
    lip.setAttribute("d", strip(near));
    rimN.setAttribute("d", open(ringAt(P, near, PT)));
    for (const e of [rim, rimN]) e.setAttribute("class", focus || over || corner ? "nf hi" : "nf");
    inner.setAttribute("d", focus ? poly(ringAt(P, rect(2.4, y1), zf)) : "");
    inner.setAttribute("class", focus ? "nf hi" : "nf");
    const gx = FX1 - 3, gy = y1 - 3;
    grip.setAttribute("d", seg(P(gx - 5, gy, zf), P(gx, gy - 5, zf)) + seg(P(gx - 9, gy, zf), P(gx, gy - 9, zf)));
    grip.setAttribute("class", corner ? "nf hi" : "nf");
    ph.setAttribute("d", n === 0 ? flat(P, zf, lay(PLH, TX, LY(0), TU)) : "");
    chars.forEach((c, i) => c.setAttribute("d", i < n ? flat(P, zf, [flatC[i]]) : ""));
  }

  // the cursor: an arrow, and over the box a blinking text caret (I-beam) that types
  const rest = P(FX1 - 12, FY0 + 18, PT + 12);
  const ax = spring(rest[0], { k: 140 }), ay = spring(rest[1], { k: 140 }), pr = spring(0);
  const cur = mk("path", { class: "dot", "data-part": "cursor" }, svg);
  const cu = spring(tx(0)[0], { k: 140 }), cv = spring(tx(0)[1], { k: 140 }); // the caret's place in the box, in world units
  const drawCur = (now) => {
    const typing = (over || focus) && !corner, blink = Math.floor(now / 500) % 2 === 0;
    cur.setAttribute("d", typing
      ? (blink ? poly(IBEAM.map(([u, v]) => P(cu.x + u, cv.x + v, zf + 0.3))) : "")
      : poly(ARROW.map(([u, v]) => [ax.x + u - 0.5, ay.x + v + 2.5 * clamp(pr.x, 0, 1)])));
  };

  const A = register(stage, (dt, now) => {
    let m = false;
    if (over || focus) {
      m = true; // the caret blinks and the text types while the pointer is over the box
      if (n < nt && now >= nextKey) { n = reducedMotion() ? nt : n + 1; nextKey = now + KEY; }
    }
    if (over || focus) { const [u, v] = tx(n); cu.t = u; cv.t = v; } // the caret sits in the box, after the last mark
    for (const s of [ax, ay, pr, cu, cv, g]) if (stepS(s, dt)) m = true;
    draw(); drawCur(now);
    return m;
  });
  bag.add(A.unregister);

  // hit areas are fixed to the rest pose (rule 01): the corner zone runs down to the stretched corner
  const pick = ([sx, sy]) => {
    const [x, y] = unproj(C, sx, sy, PT);
    const inBox = x > FX0 - 2 && x < FX1 + 2 && y > FY0 - 2 && y < FY1 + 2;
    const inCorner = x > FX1 - 12 && x < FX1 + 2 && y > FY1 - 12 && y < FY1 + GROW + 2;
    return [inBox || inCorner, inCorner];
  };
  const say = () => { read.textContent = corner ? "resize" : focus ? "focus" : over ? "type" : "rest"; };
  const start = () => { nt = flatC.length; n = 0; nextKey = performance.now() + KEY; };
  function set([o, c], p) {
    if (o !== over) { over = o; if (o) start(); else if (!focus) { n = 0; nt = 0; } }
    corner = c; g.t = c ? GROW : 0; say();
    if (!o && !focus) { ax.t = rest[0]; ay.t = rest[1]; }
    if (c) { ax.t = p[0]; ay.t = p[1]; }
    A.wake();
  }
  bag.add(pointer(stage, {
    move: (p) => set(pick(p), p),
    down: (p) => {
      const q = pick(p); set(q, p);
      focus = q[0] ? 1 : 0; if (!q[0]) { n = 0; nt = 0; } say(); A.wake();
    },
    leave: () => { focus = 0; n = 0; nt = 0; set([false, false], rest); },
  }));
  bag.add(() => svg.replaceChildren());

  draw(); drawCur(0);
  return { set: (v) => { lift = v; draw(); }, destroy: bag.dispose };
}

hairline({
  name: "textarea",
  means: "A text box on a slab: the pointer types three lines in, a press focuses, the corner stretches the box taller.",
  rules: [1, 4, 8, 9],
  range: [0, 1, 2],
  tour: [[203, 145], [246, 202], null],
  mount,
});
