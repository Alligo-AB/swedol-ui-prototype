/**
 * Pill segment control: a stadium track recessed in a slab, two segments (ALL, NEW) and a black pill standing in it.
 * The pointer over the track darkens it and underlines the inactive label; a press slides the pill across on the
 * component's own timing (300 ms, ease-standard) and the labels swap sides. A drawn cursor follows the pointer
 * and rests above the pill. The slider is how high the pill stands.
 */
const {
  Cam, bezier, clamp, facing, fit, lerp, open, poly, proj, ringAt, rings, rrect, run, prism,
  mk, pointer, reducedMotion, reflect, register, solid, put, disposer, spring, stepS, unproj,
} = HL;

const PW = 148, PD = 56, PT = 6, D = 2, TY0 = 12, TY1 = 44, PAD = 5, SEGPAD = 22;
const ARROW = [[0, 0], [0, 15], [3.6, 11.6], [6.2, 17], [8.6, 15.8], [6, 10.6], [10.8, 10.6]];
const NAMES = ["ALL", "NEW"];
const G = {
  A: [[[0, 0], [1.6, 0], [1.9, 2.2], [3.1, 2.2], [3.4, 0], [5, 0], [3.6, 8], [1.4, 8]], [[2.2, 3.6], [2.8, 3.6], [2.5, 5.6]]],
  E: [[[0, 0], [5, 0], [5, 1.5], [1.6, 1.5], [1.6, 3.3], [4.4, 3.3], [4.4, 4.7], [1.6, 4.7], [1.6, 6.5], [5, 6.5], [5, 8], [0, 8]]],
  N: [[[0, 0], [1.6, 0], [1.6, 4.8], [3.4, 0], [5, 0], [5, 8], [3.4, 8], [3.4, 3.2], [1.6, 8], [0, 8]]],
  W: [[[0, 8], [1.6, 8], [1.6, 3], [3, 6], [4.4, 3], [4.4, 8], [6, 8], [6, 0], [4.2, 0], [3, 2.8], [1.8, 0], [0, 0]]],
  L: [[[0, 0], [5, 0], [5, 1.5], [1.6, 1.5], [1.6, 8], [0, 8]]],
  " ": [],
};
const GW = (ch) => (ch === " " ? 2.4 : Math.max(...G[ch][0].map((q) => q[0])));
const U = 1;
/** A string as flat world outlines starting at (x0, ymid): condensed heavy capitals, counters wound the other way. */
function label(text, x0, ym) {
  let x = x0;
  const out = [];
  for (const ch of text) {
    G[ch].forEach((o, k) => { const q = o.map(([u, v]) => [x + u * U, ym + (4 - v) * U]); out.push(k ? q.reverse() : q); });
    x += (GW(ch) + 1.2) * U;
  }
  return out;
}
const flat = (P, outs, z) => outs.map((o) => poly(o.map(([x, y]) => P(x, y, z)))).join("");
const lw = (t) => [...t].reduce((a, ch) => a + (GW(ch) + 1.2) * U, -1.2 * U);

function mount({ stage, svg, read }, value) {
  const bag = disposer();
  let lift = value;

  // segments laid out by their labels, centred on the slab
  const W = NAMES.map((n) => lw(n) + 2 * SEGPAD), TW = W[0] + W[1] + 2 * PAD, TX0 = (PW - TW) / 2, TX1 = TX0 + TW;
  const SEG = [{ x0: TX0 + PAD, x1: TX0 + PAD + W[0] }, { x0: TX0 + PAD + W[0], x1: TX1 - PAD }];
  const cy = (TY0 + TY1) / 2, H = TY1 - TY0 - 2 * PAD, TR = (TY1 - TY0) / 2;
  const labels = NAMES.map((n, i) => label(n, (SEG[i].x0 + SEG[i].x1) / 2 - lw(n) / 2, cy));

  const C = Cam(45, 0.5, 2.3);
  fit(C, [[0, 0, 0], [PW, PD, 0], [PW, 0, 0], [0, PD, 0], [SEG[1].x1, cy, PT + 12]], 200, 172);
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

  // the track: a slot cut into the slab (floor, far wall, rim), the pill stands in it, the near lip hides its sunk part
  const out = rrect(TX0, TY0, TX1, TY1, TR, 14), far = run(out, (q) => !front(q)), near = run(out, front);
  const strip = (r) => poly([...ringAt(P, r, PT), ...ringAt(P, r, PT - D).reverse()]);
  const floor = mk("path", { d: poly(ringAt(P, out, PT - D)), class: "lo", "data-part": "track" }, svg);
  const wall = mk("path", { d: strip(far), class: "lo", "data-part": "track-wall" }, svg);
  mk("path", { d: poly(ringAt(P, out, PT - D)), class: "nf lo" }, svg);
  mk("path", { d: poly(ringAt(P, out, PT)), class: "nf" }, svg);
  // labels on the floor, shown where the pill is not; the white ones ride on the pill
  const zf = PT - D + 0.15;
  const low = labels.map((l) => mk("path", { d: flat(P, l, zf), class: "dot", "data-part": "bar" }, svg));
  const ul = mk("path", { class: "dot", "data-part": "bar" }, svg);
  const pill = solid(mk("g", {}, svg));
  pill.sil.setAttribute("data-part", "pill");
  mk("path", { d: strip(near), class: "fo" }, svg);
  mk("path", { d: open(ringAt(P, near, PT)), class: "nf" }, svg);
  const top = labels.map(() => mk("path", { class: "dot", "data-part": "bar-on" }, svg));

  const sp = { x: 0, t: 0, to: 0, from: 0, t0: 0 }, hv = spring(0);
  let on = 0, act = -1, lastK = "";
  function draw(force) {
    const s = clamp(sp.x, 0, 1), h = clamp(hv.x, 0, 1), z1 = PT + lift - 1.2 * h;
    const key = s.toFixed(3) + z1.toFixed(2) + act;
    if (!force && key === lastK) return;
    lastK = key;
    const x0 = lerp(SEG[0].x0, SEG[1].x0, s), x1 = lerp(SEG[0].x1, SEG[1].x1, s), y0 = TY0 + PAD, y1 = TY1 - PAD, r = H / 2;
    put(pill, prism(P, front, rrect(x0, y0, x1, y1, r, 14), rrect(x0 + 1.6, y0 + 1.6, x1 - 1.6, y1 - 1.6, r - 1.6, 14), PT - D + 0.6, z1));
    labels.forEach((l, i) => {
      const cov = Math.abs(s - i) < 0.5;
      low[i].setAttribute("display", cov ? "none" : "inline");
      top[i].setAttribute("display", cov ? "inline" : "none");
      if (cov) top[i].setAttribute("d", flat(P, l, z1 + 0.2));
    });
    const u = act >= 0 && act !== on ? labels[act] : null;
    ul.setAttribute("display", u ? "inline" : "none");
    if (u) { const a = SEG[act].x0 + SEG[act].x1; const w = lw(NAMES[act]); ul.setAttribute("d", poly([P(a / 2 - w / 2, cy + 5, zf), P(a / 2 + w / 2, cy + 5, zf), P(a / 2 + w / 2, cy + 6.2, zf), P(a / 2 - w / 2, cy + 6.2, zf)])); }
    for (const e of [floor, wall]) { if (act >= 0) e.setAttribute("data-hover", ""); else e.removeAttribute("data-hover"); }
  }

  // the cursor: tip at (ax, ay) on screen, pressed down by pr
  const rest = P((SEG[0].x0 + SEG[0].x1) / 2 + 3, cy - 2, PT + 9);
  const ax = spring(rest[0], { k: 140 }), ay = spring(rest[1], { k: 140 }), pr = spring(0);
  const cur = mk("path", { class: "dot", "data-part": "cursor" }, svg);
  const drawCur = () => cur.setAttribute("d", poly(ARROW.map(([u, v]) => [ax.x + u - 0.5, ay.x + v + 2.5 * clamp(pr.x, 0, 1)])));

  // the pill's slide is the component's: 300 ms on ease-standard
  const ez = bezier(0.35, 0, 0.35, 1);
  const slide = (q, now) => {
    if (q.t !== q.to) { q.from = q.x; q.to = q.t; q.t0 = now; }
    if (q.x === q.to) return false;
    q.x = reducedMotion() ? q.to : q.from + (q.to - q.from) * ez(clamp((now - q.t0) / 300, 0, 1));
    return q.x !== q.to;
  };
  let ghost = false, gt = 0, gdone = true;
  const A = register(stage, (dt, now) => {
    let m = false;
    if (ghost && act >= 0 && !gdone) { m = true; if (now - gt > 250) { gdone = true; choose(act); } }
    if (slide(sp, now)) m = true;
    for (const q of [hv, ax, ay, pr]) if (stepS(q, dt)) m = true;
    draw(); drawCur();
    return m;
  });
  bag.add(A.unregister);

  // hit: each segment's resting top band
  const pick = ([sx, sy]) => {
    const [x, y] = unproj(C, sx, sy, PT);
    if (y < TY0 - 2 || y > TY1 + 2 || x < TX0 - 2 || x > TX1 + 2) return -1;
    return x < SEG[1].x0 ? 0 : 1;
  };
  const say = () => { read.textContent = act >= 0 ? NAMES[act].toLowerCase() : on || sp.t ? NAMES[on].toLowerCase() : "rest"; };
  const choose = (a) => { if (a !== on) { on = a; sp.t = a; } pr.x = 1; pr.t = 0; say(); A.wake(); };
  function set(a, p) {
    if (a !== act) {
      act = a; gdone = !ghost; gt = performance.now(); hv.t = a >= 0 ? 1 : 0;
      pill.sil.classList.toggle("hi", a < 0 || a === on);
      say();
    }
    if (a < 0) { ax.t = rest[0]; ay.t = rest[1]; } else { ax.t = p[0]; ay.t = p[1]; }
    A.wake();
  }
  bag.add(pointer(stage, {
    move: (p, e) => { ghost = e?.pointerType === "ghost"; set(pick(p), p); gt = performance.now(); },
    down: (p) => { const a = pick(p); set(a, p); ghost = false; if (a >= 0) choose(a); },
    leave: (e) => {
      if (e?.pointerType === "ghost") { on = 0; sp.t = 0; }
      ghost = false; set(-1);
    },
  }));
  bag.add(() => svg.replaceChildren());

  pill.sil.classList.add("hi");
  draw(true); drawCur();
  return { set: (v) => { lift = v; draw(true); }, destroy: bag.dispose };
}

hairline({
  name: "pill",
  means: "A two-segment pill control set into a slab: the pointer darkens the track, a press slides the black pill under the other label.",
  rules: [1, 4, 8, 9],
  range: [1, 2, 3],
  tour: [[250, 185], [148, 134], null],
  mount,
});
