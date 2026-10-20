/**
 * Input: a text field on a slab, with a label bar over it and a hint bar under it. The pointer over the field
 * darkens its edge (hover); a press focuses it: the edge goes black with a second line inside, the placeholder
 * leaves, a caret blinks and the value types itself in, five marks. A drawn cursor follows the pointer and
 * rests on the field's right end. The slider is how high the field stands.
 */
const {
  Cam, rrect, clamp, facing, fit, poly, proj, ringAt, prism, rings,
  mk, pointer, reducedMotion, reflect, register, solid, put, disposer, spring, stepS, unproj,
} = HL;

const PW = 96, PD = 100, PT = 6, FX0 = 10, FX1 = 86, FY0 = 38, FY1 = 66, N = 5, KEY = 130;
const quad = (x0, y0, x1, y1) => [{ u: x0, v: y0 }, { u: x1, v: y0 }, { u: x1, v: y1 }, { u: x0, v: y1 }];
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
  bar(FX0, 22, FX0 + 28, 28, PT, "dot", "label");
  bar(FX0, 72, FX0 + 50, 75, PT, "dot", "hint");

  // the field: a thin plate; its edge is the state (grey, dark on hover, black and doubled on focus)
  const rect = (a, x0, y0, x1, y1) => rrect(x0 + a, y0 + a, x1 - a, y1 - a, 0.5, 3);
  const fo = rect(0, FX0, FY0, FX1, FY1), fi = rect(1.6, FX0, FY0, FX1, FY1);
  const fz = () => PT + 3 + lift;
  const field = solid(mk("g", {}, svg));
  const inner = mk("path", { class: "nf" }, svg); // second line of the focused edge
  const tx = (i) => FX0 + 10 + i * 6;
  const ph = mk("path", { class: "dot", "data-part": "ph" }, svg);
  const chars = Array.from({ length: N }, () => mk("path", { class: "dot", "data-part": "ink" }, svg));
  const caret = mk("path", { class: "dot", "data-part": "ink" }, svg);
  const midY = (FY0 + FY1) / 2;
  const q = (x0, x1, h) => poly(ringAt(P, quad(x0, midY - h, x1, midY + h), fz()));

  let focus = 0, n = 0, nt = 0, hov = 0;
  const hv = spring(0);
  function draw() {
    put(field, prism(P, front, fo, fi, PT, fz()));
    const on = focus || hov;
    field.sil.classList.toggle("hi", !!on);
    inner.setAttribute("d", focus ? poly(ringAt(P, rect(3.2, FX0, FY0, FX1, FY1), fz())) : "");
    inner.setAttribute("class", focus ? "nf hi" : "nf");
    ph.setAttribute("d", n === 0 ? q(tx(0), tx(0) + 22, 2.2) : "");
    chars.forEach((c, i) => c.setAttribute("d", i < n ? q(tx(i), tx(i) + 3.4, 4) : ""));
    caret.setAttribute("d", focus && (Math.floor(performance.now() / 500) % 2 === 0) ? q(tx(n) - 1, tx(n) - 0.2, 4.6) : "");
  }

  // the cursor
  const rest = P(FX1 - 12, midY + 2, PT + 12);
  const ax = spring(rest[0], { k: 140 }), ay = spring(rest[1], { k: 140 }), pr = spring(0);
  const cur = mk("path", { class: "dot", "data-part": "cursor" }, svg);
  const drawCur = () => cur.setAttribute("d", poly(ARROW.map(([u, v]) => [ax.x + u - 0.5, ay.x + v + 2.5 * clamp(pr.x, 0, 1)])));

  let ghost = false, gt = 0, gdone = true, over = false, nextKey = 0;
  const A = register(stage, (dt, now) => {
    let m = false;
    if (ghost && over && !gdone) { m = true; if (now - gt > 250) { gdone = true; press(now); } }
    if (focus) {
      m = true; // the caret blinks while focused
      if (n < nt && now >= nextKey) { n = reducedMotion() ? nt : n + 1; nextKey = now + KEY; }
    }
    for (const s of [hv, ax, ay, pr]) if (stepS(s, dt)) m = true;
    draw(); drawCur();
    return m;
  });
  bag.add(A.unregister);

  const pick = ([sx, sy]) => {
    const [x, y] = unproj(C, sx, sy, PT);
    return x > FX0 - 2 && x < FX1 + 2 && y > FY0 - 2 && y < FY1 + 2;
  };
  const say = () => { read.textContent = focus ? "focus" : over ? "hover" : "rest"; };
  const press = (now) => { focus = 1; nt = N; n = 0; nextKey = now + KEY; pr.x = 1; pr.t = 0; say(); A.wake(); };
  const blur = () => { focus = 0; n = 0; nt = 0; say(); A.wake(); };
  function set(o, p) {
    if (o !== over) { over = o; hov = o ? 1 : 0; gdone = !ghost; gt = performance.now(); say(); }
    if (o || focus) { ax.t = p[0]; ay.t = p[1]; } else { ax.t = rest[0]; ay.t = rest[1]; }
    A.wake();
  }
  bag.add(pointer(stage, {
    move: (p, e) => {
      const g = e?.pointerType === "ghost";
      if (g && !ghost) gdone = false; // the tour takes over from a real pointer: press after it settles
      ghost = g; set(pick(p), p); gt = performance.now();
    },
    down: (p) => {
      ghost = false;
      const o = pick(p); set(o, p);
      if (o) press(performance.now()); else blur();
    },
    leave: () => { ghost = false; blur(); set(false, rest); },
  }));
  bag.add(() => svg.replaceChildren());

  draw(); drawCur();
  return { set: (v) => { lift = v; draw(); }, destroy: bag.dispose };
}

hairline({
  name: "input",
  means: "A text field on a slab with a label and a hint: the pointer darkens its edge, a press focuses it and types a value in.",
  rules: [1, 4, 8, 9],
  range: [0, 1, 2],
  tour: [[200, 170], [200, 170], null],
  mount,
});
