/**
 * Button group: three joined buttons (S, M, L) on a slab, M selected. A selected button stands sunk with a
 * grey top (the component's black-12 fill); the others stand tall. The pointer over one dips it and tints its
 * top; a press sinks it and lifts the one that was selected. A drawn cursor follows the pointer. The slider is
 * how deep the selected button sinks.
 */
const {
  Cam, clamp, facing, fit, poly, proj, ringAt, prism, rings,
  mk, pointer, reflect, register, solid, put, disposer, spring, stepS, unproj,
} = HL;

const PW = 108, PD = 70, PT = 5, CH = 5, U = 1.4;
const X0 = 6, BW = 32, Y0 = 24, Y1 = 46;
const BTN = [{ name: "s", text: "S" }, { name: "m", text: "M" }, { name: "l", text: "L" }];
const SNAP = { k: 320, c: 30 };
const HOVER = 0.25, DOWN = { k: 520, c: 34 }, UP = { k: 650, c: 26 }; // as the Button figure: a press travels fast and firm, release pops and settles
const ARROW = [[0, 0], [0, 15], [3.6, 11.6], [6.2, 17], [8.6, 15.8], [6, 10.6], [10.8, 10.6]];
// condensed heavy capitals as closed outlines, 8 high, u right, v up
const G = {
  S: [[[0, 1.2], [1.2, 0], [3.8, 0], [5, 1.2], [5, 3.6], [3.8, 4.4], [1.6, 4.9], [1.6, 6.5], [5, 6.5], [5, 8], [1.2, 8], [0, 6.8], [0, 4.2], [1.2, 3.4], [3.4, 2.9], [3.4, 1.5], [0, 1.5]]],
  M: [[[0, 0], [1.6, 0], [1.6, 5], [3, 2], [4.4, 5], [4.4, 0], [6, 0], [6, 8], [4.2, 8], [3, 5.2], [1.8, 8], [0, 8]]],
  L: [[[0, 0], [5, 0], [5, 1.5], [1.6, 1.5], [1.6, 8], [0, 8]]],
};
const GW = (ch) => Math.max(...G[ch][0].map((q) => q[0]));

/** One letter as a world outline, centred in the button spanning x0..x1. */
function label(ch, x0, x1) {
  const x = (x0 + x1) / 2 - (GW(ch) * U) / 2, yb = (Y0 + Y1) / 2 + 4 * U;
  return G[ch].map((s) => s.map(([u, v]) => [x + u * U, yb - v * U]));
}

function mount({ stage, svg, read }, value) {
  const bag = disposer();
  let depth = value;

  const C = Cam(45, 0.5, 2.3);
  fit(C, [[0, 0, 0], [PW, PD, 0], [PW, 0, 0], [0, PD, 0], [0, 0, PT + CH + 6]], 200, 172);
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

  let sel = 1;
  const btns = BTN.map((b, i) => {
    const x0 = X0 + i * BW, x1 = x0 + BW, [out, inn] = rings(x0, Y0, x1, Y1, 0, 1.0);
    const cap = solid(mk("g", {}, svg));
    const tint = mk("path", { class: "dot", "data-part": "bg-tint" }, svg);
    const text = mk("path", { class: "dot", "data-part": "bg-label" }, svg);
    return { ...b, x0, x1, out, inn, cap, tint, text, strokes: label(b.text, x0, x1), sp: spring(i === sel ? 1 : 0, SNAP), last: -1 };
  });

  const top = (b) => PT + CH - depth * clamp(b.sp.x, -0.3, 1.2);
  function draw(force) {
    for (const b of btns) {
      const z = top(b);
      if (!force && Math.abs(z - b.last) < 0.01) continue;
      b.last = z;
      put(b.cap, prism(P, front, b.out, b.inn, PT, z));
      b.tint.setAttribute("d", poly(ringAt(P, b.out, z)));
      b.text.setAttribute("d", b.strokes.map((s) => poly(s.map(([x, y]) => P(x, y, z)))).join(""));
    }
  }

  // the pointer: rests below the group, follows the real one, dips on a press
  const rest = P(PW - 14, 58, PT);
  const GLIDE = { k: 120, c: 22 };
  const ax = spring(rest[0], GLIDE), ay = spring(rest[1], GLIDE), pr = spring(0, { k: 260, c: 28 });
  const halo = mk("path", { class: "fo" }, svg), cur = mk("path", { class: "dot", "data-part": "cursor" }, svg);
  const drawCur = () => {
    const x = ax.x - 0.5, y = ay.x + 2.5 * clamp(pr.x, 0, 1);
    cur.setAttribute("d", poly(ARROW.map(([u, v]) => [x + u, y + v])));
    halo.setAttribute("d", [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]].map(([i, j]) => poly(ARROW.map(([u, v]) => [x + u + i * 0.8, y + v + j * 0.8]))).join(""));
  };

  let act = -1, ghost = false, gt = 0, gdone = true;
  const level = (i) => (i === sel ? 1 : i === act ? HOVER : 0);
  const paint = () => btns.forEach((b, i) => {
    b.sp.t = level(i);
    if (i === sel || i === act) b.tint.setAttribute("data-show", ""); else b.tint.removeAttribute("data-show");
  });
  function choose(a) { const was = sel; sel = a; Object.assign(btns[a].sp, DOWN); if (was !== a) Object.assign(btns[was].sp, UP); pr.x = 1; pr.t = 0; paint(); say(); B.wake(); }
  const say = () => { read.textContent = act < 0 ? "rest" : btns[act].name + (act === sel ? " selected" : ""); };
  const B = register(stage, (dt, now) => {
    let m = false;
    if (ghost && act >= 0 && !gdone) { m = true; if (now - gt > 200) { gdone = true; choose(act); } }
    for (const b of btns) if (stepS(b.sp, dt)) m = true;
    for (const q of [ax, ay, pr]) if (stepS(q, dt)) m = true;
    draw(); drawCur();
    return m;
  });
  bag.add(B.unregister);

  // hit: the group's resting top plane
  const pick = ([sx, sy]) => {
    const [x, y] = unproj(C, sx, sy, PT + CH);
    if (y < Y0 - 2 || y > Y1 + 2 || x < X0 - 2 || x > X0 + 3 * BW + 2) return -1;
    return clamp(Math.floor((x - X0) / BW), 0, 2);
  };
  function set(a) {
    if (a === act) return;
    act = a; paint(); say();
    gdone = !ghost; gt = performance.now();
    B.wake();
  }
  const aim = (p) => { if (p) { ax.t = p[0]; ay.t = p[1]; } else { ax.t = rest[0]; ay.t = rest[1]; } };
  bag.add(pointer(stage, {
    move: (p, e) => { ghost = e?.pointerType === "ghost"; set(pick(p)); aim(p); B.wake(); },
    down: (p) => { const a = pick(p); ghost = false; set(a); aim(p); if (a >= 0) choose(a); },
    leave: (e) => {
      if (e?.pointerType === "ghost") sel = 1; // the tour ends where it began
      ghost = false; act = -2; set(-1); aim(null); B.wake();
    },
  }));
  bag.add(() => svg.replaceChildren());

  paint(); btns.forEach((b) => { b.sp.x = b.sp.t; });
  draw(true); drawCur();
  return { set: (v) => { depth = v; draw(true); }, destroy: bag.dispose };
}

hairline({
  name: "button-group",
  means: "Three joined buttons, S M L with M selected: the pointer dips one, a press sinks it and the former pick pops back up.",
  rules: [1, 4, 8, 9],
  range: [1.5, 3.5, 5],
  tour: [[148, 142], [200, 168], [249, 192], null],
  mount,
});
