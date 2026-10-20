/**
 * Input: a text field on a slab, with a label bar over it and a hint bar under it. The pointer over the field
 * darkens its edge (hover); a press focuses it: the edge goes black with a second line inside, the placeholder
 * leaves, a caret blinks and the value types itself in, five marks. A drawn cursor follows the pointer and
 * rests on the field's right end. The slider is how high the field stands.
 */
const {
  Cam, rrect, clamp, facing, fit, poly, proj, open, run, ringAt, prism, rings,
  mk, pointer, reducedMotion, reflect, register, solid, put, disposer, spring, stepS, unproj,
} = HL;

const PW = 96, PD = 100, PT = 6, FX0 = 8, FX1 = 88, FY0 = 41, FY1 = 63, N = 5, KEY = 130;
const quad = (x0, y0, x1, y1) => [{ u: x0, v: y0 }, { u: x1, v: y0 }, { u: x1, v: y1 }, { u: x0, v: y1 }];
const IBEAM = [[-3.5, -8], [3.5, -8], [3.5, -6.6], [0.8, -6.6], [0.8, 6.6], [3.5, 6.6], [3.5, 8], [-3.5, 8], [-3.5, 6.6], [-0.8, 6.6], [-0.8, -6.6], [-3.5, -6.6]];
const ARROW = [[0, 0], [0, 15], [3.6, 11.6], [6.2, 17], [8.6, 15.8], [6, 10.6], [10.8, 10.6]];

function mount({ stage, svg, read }, value) {
  const bag = disposer();
  let lift = value;

  const C = Cam(45, 0.5, 2.3);
  fit(C, [[0, 0, 0], [PW, PD, 0], [PW, 0, 0], [0, PD, 0], [FX1, FY0, PT + 14]], 200, 172);
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

  // flat marks on the slab: label over the field, hint under it
  const bar = (x0, y0, x1, y1, z, cls, part) => mk("path", { d: poly(ringAt(P, quad(x0, y0, x1, y1), z)), class: cls, "data-part": part }, svg);
  bar(FX0, 26, FX0 + 26, 31, PT, "dot", "label");
  bar(FX0, 69, FX0 + 46, 72, PT, "dot", "hint");

  // the field: a slot cut into the slab (floor, far wall, rim, near lip), its rim is the state (grey, black on hover, doubled on focus)
  const rect = (a, x0, y0, x1, y1) => rrect(x0 + a, y0 + a, x1 - a, y1 - a, 0.5, 3);
  const out = rect(0, FX0, FY0, FX1, FY1);
  const far = run(out, (q) => !front(q)), near = run(out, front);
  const D = 2 + lift, zf = PT - D; // lift is the slot's depth
  const strip = (r) => poly([...ringAt(P, r, PT), ...ringAt(P, r, zf).reverse()]);
  const slot = mk("g", {}, svg);
  const tx = (i) => FX0 + 8 + i * 6, midY = (FY0 + FY1) / 2;
  const q = (x0, x1, h) => poly(ringAt(P, quad(x0, midY - h, x1, midY + h), zf));
  const ph = mk("path", { class: "dot", "data-part": "ph" }, svg);
  const chars = Array.from({ length: N }, () => mk("path", { class: "dot", "data-part": "ink" }, svg));
  const caret = mk("path", { class: "dot", "data-part": "ink" }, svg);
  const inner = mk("path", { class: "nf" }, svg); // second line of the focused edge, on the floor
  const lip = mk("path", { class: "fo" }, svg), rimN = mk("path", { class: "nf" }, svg), rim = mk("path", { class: "nf" }, svg);
  slot.replaceChildren();
  // order matters: floor, wall, rim, marks, then the near lip over the sunk part
  const floor = mk("path", { class: "fo" }, slot), wall = mk("path", { class: "lo", "data-part": "track-wall" }, slot);
  slot.append(rim);
  svg.append(ph, ...chars, caret, inner, lip, rimN);

  let focus = 0, n = 0, nt = 0, over = false, nextKey = 0;
  function draw() {
    floor.setAttribute("d", poly(ringAt(P, out, zf)));
    wall.setAttribute("d", strip(far));
    rim.setAttribute("d", poly(ringAt(P, out, PT)));
    lip.setAttribute("d", strip(near));
    rimN.setAttribute("d", open(ringAt(P, near, PT)));
    for (const e of [rim, rimN]) e.setAttribute("class", focus || over ? "nf hi" : "nf");
    inner.setAttribute("d", focus ? poly(ringAt(P, rect(2.4, FX0, FY0, FX1, FY1), zf)) : "");
    inner.setAttribute("class", focus ? "nf hi" : "nf");
    ph.setAttribute("d", n === 0 ? q(tx(0), tx(0) + 22, 2) : "");
    chars.forEach((c, i) => c.setAttribute("d", i < n ? q(tx(i), tx(i) + 3.4, 3.6) : ""));
    caret.setAttribute("d", focus && (Math.floor(performance.now() / 500) % 2 === 0) ? q(tx(n) - 1, tx(n) - 0.2, 4.6) : "");
  }

  // the cursor: an arrow, and over the field a blinking text caret (I-beam) that types
  const rest = P(FX1 - 12, midY + 2, PT + 12);
  const ax = spring(rest[0], { k: 140 }), ay = spring(rest[1], { k: 140 }), pr = spring(0);
  const cur = mk("path", { class: "dot", "data-part": "cursor" }, svg);
  const drawCur = (now) => {
    const pts = over ? (Math.floor(now / 500) % 2 === 0 ? IBEAM : []) : ARROW;
    cur.setAttribute("d", pts.length ? poly(pts.map(([u, v]) => [ax.x + u - (over ? 0 : 0.5), ay.x + v + (over ? 0 : 2.5 * clamp(pr.x, 0, 1))])) : "");
  };

  const A = register(stage, (dt, now) => {
    let m = false;
    if (over || focus) {
      m = true; // the caret blinks and the value types while the pointer is over the field
      if (n < nt && now >= nextKey) { n = reducedMotion() ? nt : n + 1; nextKey = now + KEY; }
    }
    for (const s of [ax, ay, pr]) if (stepS(s, dt)) m = true;
    draw(); drawCur(now);
    return m;
  });
  bag.add(A.unregister);

  const pick = ([sx, sy]) => {
    const [x, y] = unproj(C, sx, sy, PT);
    return x > FX0 - 2 && x < FX1 + 2 && y > FY0 - 2 && y < FY1 + 2;
  };
  const say = () => { read.textContent = focus ? "focus" : over ? "type" : "rest"; };
  const start = () => { nt = N; n = 0; nextKey = performance.now() + KEY; };
  function set(o, p) {
    if (o !== over) { over = o; if (o) start(); else if (!focus) { n = 0; nt = 0; } say(); }
    if (o || focus) { ax.t = p[0]; ay.t = p[1]; } else { ax.t = rest[0]; ay.t = rest[1]; }
    A.wake();
  }
  bag.add(pointer(stage, {
    move: (p) => set(pick(p), p),
    down: (p) => {
      const o = pick(p); set(o, p);
      focus = o ? 1 : 0; if (!o) { n = 0; nt = 0; } say(); A.wake();
    },
    leave: () => { focus = 0; n = 0; nt = 0; set(false, rest); },
  }));
  bag.add(() => svg.replaceChildren());

  draw(); drawCur(0);
  return { set: (v) => { lift = v; draw(); }, destroy: bag.dispose };
}

hairline({
  name: "input",
  means: "A text field on a slab with a label and a hint: the pointer turns into a blinking text caret and types a value in; a press focuses it.",
  rules: [1, 4, 8, 9],
  range: [0, 1, 2],
  tour: [[259, 175], [200, 170], null],
  mount,
});
