/**
 * Button pair: an inked Primary block and an outlined Secondary block of the same height on a slab, each with
 * its label drawn as strokes on its top. The pointer over one presses it down
 * on a spring and lights its edge. The slider is how deep Primary travels.
 */
const {
  Cam, clamp, facing, fit, poly, proj, ringAt, rrect, prism, rings,
  mk, pointer, reflect, register, solid, put, disposer, spring, stepS, unproj,
} = HL;

const PW = 108, PD = 90, PT = 5, U = 1.2;
const BTN = [
  { name: "primary", text: "PRIMARY", y0: 10, y1: 40, ch: 6, k: 1 },
  { name: "secondary", text: "SECONDARY", y0: 50, y1: 80, ch: 6, k: 1 },
];
const X0 = 8, X1 = 100;
const SNAP = { k: 320, c: 30 }; // snappy: stiffer and slightly under-damped
const HOVER = 0.35, BOUNCE = [[0.28, 120]], DOWN = { k: 520, c: 34 }, UP = { k: 650, c: 26 }, HOLD = 420; // a real button: hover dips, a press travels fast and firm, release bounces once and settles
const ARROW = [[0, 0], [0, 15], [3.6, 11.6], [6.2, 17], [8.6, 15.8], [6, 10.6], [10.8, 10.6]]; // the pointer, as in the Switch figure
// condensed heavy capitals as closed outlines (Breuer-like), 8 high, u right, v up; the second outline, when there is one, is the counter
const G = {
  P: [[[0, 0], [1.6, 0], [1.6, 3], [3.8, 3], [5, 4.2], [5, 6.8], [3.8, 8], [0, 8]], [[1.6, 4.5], [3, 4.5], [3.4, 4.9], [3.4, 6.1], [3, 6.5], [1.6, 6.5]]],
  R: [[[0, 0], [1.6, 0], [1.6, 3], [2.6, 3], [3.4, 0], [5, 0], [4.2, 3.3], [5, 4.2], [5, 6.8], [3.8, 8], [0, 8]], [[1.6, 4.5], [3, 4.5], [3.4, 4.9], [3.4, 6.1], [3, 6.5], [1.6, 6.5]]],
  I: [[[0, 0], [1.6, 0], [1.6, 8], [0, 8]]],
  M: [[[0, 0], [1.6, 0], [1.6, 5], [3, 2], [4.4, 5], [4.4, 0], [6, 0], [6, 8], [4.2, 8], [3, 5.2], [1.8, 8], [0, 8]]],
  A: [[[0, 0], [1.6, 0], [1.9, 2.2], [3.1, 2.2], [3.4, 0], [5, 0], [3.6, 8], [1.4, 8]], [[2.2, 3.6], [2.8, 3.6], [2.5, 5.6]]],
  Y: [[[0, 8], [1.7, 8], [2.5, 5], [3.3, 8], [5, 8], [3.3, 3.6], [3.3, 0], [1.7, 0], [1.7, 3.6]]],
  S: [[[0, 1.2], [1.2, 0], [3.8, 0], [5, 1.2], [5, 3.6], [3.8, 4.4], [1.6, 4.9], [1.6, 6.5], [5, 6.5], [5, 8], [1.2, 8], [0, 6.8], [0, 4.2], [1.2, 3.4], [3.4, 2.9], [3.4, 1.5], [0, 1.5]]],
  E: [[[0, 0], [5, 0], [5, 1.5], [1.6, 1.5], [1.6, 3.3], [4.4, 3.3], [4.4, 4.7], [1.6, 4.7], [1.6, 6.5], [5, 6.5], [5, 8], [0, 8]]],
  C: [[[0, 1.2], [1.2, 0], [3.8, 0], [5, 1.2], [5, 2.6], [3.4, 2.6], [3.4, 1.5], [1.6, 1.5], [1.6, 6.5], [3.4, 6.5], [3.4, 5.4], [5, 5.4], [5, 6.8], [3.8, 8], [1.2, 8], [0, 6.8]]],
  O: [[[0, 1.2], [1.2, 0], [3.8, 0], [5, 1.2], [5, 6.8], [3.8, 8], [1.2, 8], [0, 6.8]], [[1.6, 1.5], [3.4, 1.5], [3.4, 6.5], [1.6, 6.5]]],
  N: [[[0, 0], [1.6, 0], [1.6, 4.8], [3.4, 0], [5, 0], [5, 8], [3.4, 8], [3.4, 3.2], [1.6, 8], [0, 8]]],
  D: [[[0, 0], [3.8, 0], [5, 1.2], [5, 6.8], [3.8, 8], [0, 8]], [[1.6, 1.5], [3.2, 1.5], [3.4, 1.7], [3.4, 6.3], [3.2, 6.5], [1.6, 6.5]]],
};
const GW = (ch) => Math.max(...G[ch][0].map((q) => q[0]));

/** The label as world outlines, centred in the button: [x, y] pairs, one list per outline. */
function label(text, y0, y1) {
  const adv = 1.2;
  const total = [...text].reduce((s, ch) => s + GW(ch) + adv, -adv) * U;
  let x = (X0 + X1) / 2 - total / 2;
  const yb = (y0 + y1) / 2 + 4 * U, out = [];
  for (const ch of text) {
    // a counter is wound the other way so a fill leaves it open
    G[ch].forEach((s, k) => { const q = s.map(([u, v]) => [x + u * U, yb - v * U]); out.push(k ? q.reverse() : q); });
    x += (GW(ch) + adv) * U;
  }
  return out;
}

function mount({ stage, svg, read }, value) {
  const bag = disposer();
  let depth = value;

  const C = Cam(45, 0.5, 1.9);
  fit(C, [[0, 0, 0], [PW, PD, 0], [PW, 0, 0], [0, PD, 0], [0, 0, PT + 6]], 200, 172);
  const P = proj(C), front = facing(C);

  const [pOut, pIn] = rings(0, 0, PW, PD, 0, 1.6);
  if (stage.hasAttribute("data-flat")) {
    // a flat slab: no thickness, no reflection, only the top plane (see-through in CSS via data-part="slab")
    const sl = solid(mk("g", {}, svg));
    sl.sil.setAttribute("class", "sil"); sl.sil.setAttribute("data-part", "slab");
    sl.sil.setAttribute("d", poly(ringAt(P, pOut, PT))); sl.cr.setAttribute("d", poly(ringAt(P, pIn, PT)));
  } else {
    reflect(svg, mk("g", {}, svg), P, front, pOut, 0, 14);
    put(solid(mk("g", {}, svg)), prism(P, front, pOut, pIn, 0, PT));
    svg.lastChild.firstChild.setAttribute("class", "sil");
  }

  const btns = BTN.map((b) => {
    const [out, inn] = rings(X0, b.y0, X1, b.y1, 0, 1.2);
    mk("path", { d: poly(ringAt(P, rrect(X0 - 3, b.y0 - 3, X1 + 3, b.y1 + 3, 0, 4), PT)), class: "nf lo" }, svg);
    // Primary is inked: body and top take the kernel's dot fill (black), a dim line sets the top off from the sides; Secondary stays an outline
    const ink = b.name === "primary", g = mk("g", {}, svg);
    const cap = ink ? { sil: mk("path", { class: "dot", "data-part": "ink" }, g), top: mk("path", { class: "dot", "data-part": "ink-top" }, g), edge: mk("path", { class: "nf lo" }, g) } : solid(g);
    const text = mk("path", { class: ink ? "fo" : "dot", "data-part": ink ? "ink-label" : "label" }, svg); // Primary's label is fill only (ground colour), Secondary's is the dot fill (black)
    return { ...b, ink, out, inn, cap, text, strokes: label(b.text, b.y0, b.y1), sp: spring(0, SNAP), last: -1, down: false, rel: 0, pop: 0, st: 0 };
  });

  const top = (b) => PT + b.ch - depth * b.k * clamp(b.sp.x, -0.6, 1.1);
  function draw(force) {
    for (const b of btns) {
      const z = top(b);
      if (!force && Math.abs(z - b.last) < 0.01) continue;
      b.last = z;
      const pr = prism(P, front, b.out, b.inn, PT, z);
      if (b.ink) { b.cap.sil.setAttribute("d", pr.sil); const t = poly(ringAt(P, b.out, z)); b.cap.top.setAttribute("d", t); b.cap.edge.setAttribute("d", t); } else put(b.cap, pr);
      b.text.setAttribute("d", b.strokes.map((s) => poly(s.map(([x, y]) => P(x, y, z)))).join(""));
    }
  }
  // the pointer, as in the Switch figure: rests above Primary, follows the real one only while it is over a button, dips on a press
  const rest = P(46, 93, 0);
  const GLIDE = { k: 120, c: 22 }; // critically damped: the arrow glides, never overshoots
  const ax = spring(rest[0], GLIDE), ay = spring(rest[1], GLIDE), pr = spring(0, { k: 260, c: 28 });
  const halo = mk("path", { class: "fo" }, svg), cur = mk("path", { class: "dot", "data-part": "cursor" }, svg); // a ground-colour halo keeps the arrow readable on black
  const drawCur = () => {
    const x = ax.x - 0.5, y = ay.x + 2.5 * clamp(pr.x, 0, 1);
    cur.setAttribute("d", poly(ARROW.map(([u, v]) => [x + u, y + v])));
    // outline: the arrow copied eight ways, 0.8 units out, in the ground colour
    halo.setAttribute("d", [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]].map(([i, j]) => poly(ARROW.map(([u, v]) => [x + u + i * 0.8, y + v + j * 0.8]))).join(""));
  };
  let act = -1, ghost = false, gt = 0, gdone = true;
  const level = (b, i) => (b.down ? 1 : i === act ? HOVER : 0);
  function click(a) {
    const b = btns[a], now = performance.now();
    Object.assign(b.sp, DOWN); b.down = true; b.rel = now + HOLD; b.sp.t = 1; pr.x = 1; pr.t = 0;
    B.wake();
  }
  const B = register(stage, (dt, now) => {
    let m = false;
    if (ghost && act >= 0 && !gdone) { m = true; if (now - gt > 520) { gdone = true; click(act); } }
    btns.forEach((b, i) => {
      if (b.down && now > b.rel) { b.down = false; Object.assign(b.sp, UP); b.st = 0; b.sp.t = BOUNCE[0][0]; b.pop = now + BOUNCE[0][1]; } // release: one small pop up...
      else if (b.pop && now > b.pop) { // ...then settle on the hover level
        b.st++;
        if (b.st < BOUNCE.length) { b.sp.t = BOUNCE[b.st][0]; b.pop = now + BOUNCE[b.st][1]; } else { b.pop = 0; b.sp.t = level(b, i); }
      }
      if (b.down || b.pop) m = true;
      if (stepS(b.sp, dt)) m = true;
    });
    for (const q of [ax, ay, pr]) if (stepS(q, dt)) m = true;
    draw();
    drawCur();
    return m;
  });
  bag.add(B.unregister);

  // hit: each button's resting top plane, so a pressed cap cannot drop out from under the pointer
  const pick = ([sx, sy]) => {
    for (const i of [1, 0]) {
      const b = btns[i], [x, y] = unproj(C, sx, sy, PT + b.ch);
      if (x > X0 - 2 && x < X1 + 2 && y > b.y0 - 2 && y < b.y1 + 2) return i;
    }
    return -1;
  };
  function set(a) {
    if (a === act) return;
    act = a;
    btns.forEach((b, i) => {
      if (!b.down && !b.pop) { Object.assign(b.sp, UP); b.sp.t = level(b, i); }
      if (b.ink) b.cap.top.setAttribute("class", i === a ? "dot m" : "dot"); // pressed: the top lifts to the medium ink
      else b.cap.sil.classList.toggle("hi", i === a);
    });
    gdone = !ghost; gt = performance.now();
    read.textContent = a < 0 ? "rest" : btns[a].name;
    B.wake();
  }
  const aim = (p) => { if (p) { ax.t = p[0]; ay.t = p[1]; } else { ax.t = rest[0]; ay.t = rest[1]; } }; // follows the pointer over the whole stage; home when it leaves
  bag.add(pointer(stage, {
    move: (p, e) => { ghost = e?.pointerType === "ghost"; set(pick(p)); aim(p); B.wake(); },
    down: (p) => { const a = pick(p); ghost = false; set(a); aim(p); if (a >= 0) click(a); },
    leave: () => { ghost = false; set(-1); aim(null); B.wake(); },
  }));
  bag.add(() => svg.replaceChildren());

  draw(true);
  drawCur();
  return { set: (v) => { depth = v; draw(true); }, destroy: bag.dispose };
}

hairline({
  name: "button-pair",
  means: "Two buttons on a slab, Primary and Secondary: a drawn pointer presses the one it is over and its edge lights.",
  rules: [1, 4, 8, 9],
  range: [1.5, 3, 5],
  tour: [[227, 158], [173, 185], null],
  mount,
});
