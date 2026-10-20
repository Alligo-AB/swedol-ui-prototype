/**
 * Inline notification: a field, a blue notification block and a line of content on a slab. The notification sits
 * in the flow between field and content and pushes the content down. The pointer over its x lights it; a press
 * closes it (the block fades out and its height collapses, the content moves up); a press on the field brings it
 * back. A drawn cursor rests above the x. The slider is the notification's thickness.
 */
const {
  Cam, bezier, clamp, facing, fit, lerp, poly, proj, ringAt, rrect, prism, rings, seg,
  mk, pointer, reducedMotion, reflect, register, solid, put, disposer, spring, stepS, unproj,
} = HL;

const PW = 96, PD = 100, PT = 6, X0 = 8, X1 = 88, FY0 = 18, FY1 = 34, NY = 40, NH = 16, XC = 80;
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
  ":": [[[0, 0], [1.6, 0], [1.6, 1.6], [0, 1.6]], [[0, 4.6], [1.6, 4.6], [1.6, 6.2], [0, 6.2]]],
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
  fit(C, [[0, 0, 0], [PW, PD, 0], [PW, 0, 0], [0, PD, 0], [X1, NY, PT + 9]], 200, 172);
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

  const flatRect = (x0, y0, x1, y1, z) => poly([P(x0, y0, z), P(x1, y0, z), P(x1, y1, z), P(x0, y1, z)]);
  const part = (name, cls = "dot") => mk("path", { class: cls, "data-part": name }, svg);

  // static: label bar and the field (a plain outlined box)
  part("bar-dk").setAttribute("d", flatRect(X0, 9.6, 30, 12.6, PT));
  mk("path", { d: poly(ringAt(P, rrect(X0, FY0, X1, FY1, 0.5, 3), PT)), class: "fo" }, svg);
  mk("path", { d: poly(ringAt(P, rrect(X0, FY0, X1, FY1, 0.5, 3), PT)), class: "nf" }, svg);
  part("bar").setAttribute("d", flatRect(X0 + 5, 24.9, X0 + 36, 27.9, PT));

  // the notification: a thin raised block with a blue left edge; its icon, text and x show once it has opened
  const body = solid(mk("g", {}, svg)); body.sil.setAttribute("data-part", "note");
  const edge = solid(mk("g", {}, svg)); edge.sil.setAttribute("data-part", "edge");
  const icon = part("icon"), ii = part("icon-i", "fo"), t1 = part("bar-dk"), t2 = part("txt");
  const TU = 0.42, tA = lay("INFO:", X0 + 16, 0, TU), tB = lay("ONLY 4 LEFT", tA[tA.length - 1].x1 + 4 * TU, 0, TU); // laid out at y 0, moved with the block
  const xg = mk("path", { class: "nf" }, svg), xhit = mk("path", { class: "nf" }, svg);
  // the content under it: two text lines and a black button, which move with the collapse
  const l1 = part("bar-dk"), l2 = part("bar");
  const bt = mk("g", {}, svg), bs = mk("path", { class: "dot", "data-part": "btn" }, bt), bp = mk("path", { class: "dot", "data-part": "btn-top" }, bt);

  const h = spring(NH, { k: 140 }); // open height of the block; fades/collapses by a timed tween (below)
  let from = NH, to = NH, t0 = 0, cur0 = NH, hot = false;
  const ZN = () => 2.4 + lift - 2; // the block's thickness above the slab
  const draw = () => {
    const hh = cur0, vis = hh > NH - 0.4, cb = 42 + hh * (1 + 4 / NH), z = PT + Math.max(0.6, ZN());
    if (hh > 0.05) {
      put(body, prism(P, front, rrect(X0, NY, X1, NY + hh, 0, 4), null, PT, z));
      put(edge, prism(P, front, rrect(X0, NY, X0 + 2.6, NY + hh, 0, 4), null, PT, z + 0.4));
    } else { body.sil.setAttribute("d", ""); body.cr.setAttribute("d", ""); edge.sil.setAttribute("d", ""); edge.cr.setAttribute("d", ""); }
    const my = NY + hh / 2, zt = z + 0.01;
    const circ = rrect(X0 + 6.5, my - 3.2, X0 + 12.9, my + 3.2, 3.2, 10);
    icon.setAttribute("d", vis ? poly(ringAt(P, circ, zt)) : "");
    ii.setAttribute("d", vis ? flatRect(X0 + 9.4, my - 0.4, X0 + 10, my + 2.2, zt) + flatRect(X0 + 9.4, my - 2.1, X0 + 10, my - 1.4, zt) : "");
    const lift2 = (ls) => flat(P, zt, ls.map((l) => ({ outs: l.outs.map((o) => o.map(([x, y]) => [x, y + my])) })));
    t1.setAttribute("d", vis ? lift2(tA) : "");
    t2.setAttribute("d", vis ? lift2(tB) : "");
    const xs = (u) => seg(P(XC - 2.2, my - 2.2 + u, zt), P(XC + 2.2, my + 2.2 - u, zt)) + seg(P(XC - 2.2, my + 2.2 - u, zt), P(XC + 2.2, my - 2.2 + u, zt));
    xg.setAttribute("d", vis ? xs(0) : "");
    xg.setAttribute("class", hot ? "nf hi" : "nf");
    l1.setAttribute("d", flatRect(X0, cb, X0 + 62, cb + 3, PT));
    l2.setAttribute("d", flatRect(X0, cb + 6, X0 + 48, cb + 9, PT));
    const bo = rrect(X0, cb + 14, X0 + 28, cb + 25, 0, 4), bz = PT + 2.4;
    bs.setAttribute("d", prism(P, front, bo, null, PT, bz).sil);
    bp.setAttribute("d", poly(ringAt(P, bo, bz)));
  };

  // the cursor: tip at (ax, ay), rests above the x
  const rest = P(XC + 6, NY + NH / 2 + 3, PT + 9);
  const ax = spring(rest[0], { k: 140 }), ay = spring(rest[1], { k: 140 }), pr = spring(0);
  const cur = mk("path", { class: "dot", "data-part": "cursor" }, svg);
  const drawCur = () => cur.setAttribute("d", poly(ARROW.map(([u, v]) => [ax.x + u - 0.5, ay.x + v + 2.5 * clamp(pr.x, 0, 1)])));

  // the notification's motion is the Inline's: opens on ease-decelerate-generic 250ms, closes on ease-accelerate-generic 150ms
  const eo = bezier(0.16, 0.38, 0.58, 1), ec = bezier(0.36, 0.09, 1, 0.58);
  const goTo = (v, now) => { if (v === to) return; from = cur0; to = v; t0 = now; };
  let ghost = false, gt = 0, gdone = true, act = "";
  const A = register(stage, (dt, now) => {
    let m = false;
    if (ghost && act && !gdone) { m = true; if (now - gt > 250) { gdone = true; press(act); } }
    if (cur0 !== to) {
      const d = to < from ? 150 : 250, k = reducedMotion() ? 1 : clamp((now - t0) / d, 0, 1);
      cur0 = from + (to - from) * (to < from ? ec : eo)(k);
      if (k < 1) m = true; else cur0 = to;
    }
    for (const q of [ax, ay, pr]) if (stepS(q, dt)) m = true;
    draw(); drawCur();
    return m;
  });
  bag.add(A.unregister);

  // hit areas are fixed to the rest pose (rule 01): the x while the block is open, the field always
  const pick = ([sx, sy]) => {
    const [x, y] = unproj(C, sx, sy, PT);
    if (x > XC - 6 && x < XC + 6 && y > NY && y < NY + NH && to > 0) return "x";
    if (x > X0 - 2 && x < X1 + 2 && y > FY0 - 2 && y < FY1 + 2) return "field";
    return "";
  };
  const say = () => { read.textContent = to > 0 ? (act === "x" ? "close" : "open") : "closed"; };
  function press(a) {
    const now = performance.now();
    if (a === "x" && to > 0) goTo(0, now); else if (a === "field" && to === 0) goTo(NH, now);
    pr.x = 1; pr.t = 0; hot = a === "x" && to > 0; say(); A.wake();
  }
  function set(a, p) {
    if (a !== act) { act = a; gdone = !ghost; gt = performance.now(); hot = a === "x" && to > 0; }
    if (a === "") { ax.t = rest[0]; ay.t = rest[1]; } else { ax.t = p[0]; ay.t = p[1]; }
    say(); A.wake();
  }
  bag.add(pointer(stage, {
    move: (p, e) => { ghost = e?.pointerType === "ghost"; set(pick(p), p); gt = performance.now(); },
    down: (p) => { const a = pick(p); set(a, p); ghost = false; if (a) press(a); },
    leave: (e) => {
      if (e?.pointerType === "ghost") goTo(NH, performance.now());
      ghost = false; hot = false; set("", rest);
    },
  }));
  bag.add(() => svg.replaceChildren());

  draw(); drawCur();
  return { set: (v) => { lift = v; draw(); }, destroy: bag.dispose };
}

hairline({
  name: "inline-notification",
  means: "A field, a blue notification block and content on a slab: the x closes the block and the content moves up, the field brings it back.",
  rules: [1, 4, 8, 9],
  range: [1, 2, 3],
  tour: [[259, 175], [190, 150], null],
  mount,
});
