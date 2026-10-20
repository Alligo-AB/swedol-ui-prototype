/**
 * Button: a pill cap standing proud of a rounded plate. The pointer over the
 * cap's resting footprint presses it down on a spring, and the cap's edge goes
 * bright. The slider is how deep it travels.
 */
const {
  Cam, clamp, facing, fit, hull, open, poly, proj, ringAt, rrect, run, prism, rings,
  mk, place, pointer, reflect, register, solid, put, disposer, spring, stepS, unproj,
} = HL;

const PW = 150, PD = 84, PT = 5, CX0 = 24, CX1 = 126, CY0 = 18, CY1 = 58, CT = 22;

function mount({ stage, svg, read }, value) {
  const bag = disposer();
  let depth = value;

  const C = Cam(45, 0.5, 1.7);
  fit(C, [[0, 0, 0], [PW, PD, 0], [PW, 0, 0], [0, PD, 0], [0, 0, CT]], 200, 170);
  const P = proj(C), front = facing(C);

  // plate: opaque slab, with the well the cap sits in marked on its top
  const pOut = rrect(0, 0, PW, PD, 14, 14), pIn = rrect(1.6, 1.6, PW - 1.6, PD - 1.6, 12.4, 14);
  reflect(svg, mk("g", {}, svg), P, front, pOut, 0, 14);
  const plate = solid(mk("g", {}, svg));
  put(plate, prism(P, front, pOut, pIn, 0, PT));
  plate.sil.setAttribute("class", "sil");
  const well = rrect(CX0 - 4, CY0 - 4, CX1 + 4, CY1 + 4, 24, 14);
  mk("path", { d: poly(ringAt(P, well, PT)), class: "nf lo" }, svg);

  // three indicator dots on the plate's front strip
  [16, 25, 34].forEach((x) => place(mk("circle", { r: 1.5, class: "dot off" }, svg), P(x, 72, PT)));

  // cap
  const cOut = rrect(CX0, CY0, CX1, CY1, 20, 14), cIn = rrect(CX0 + 2, CY0 + 2, CX1 - 2, CY1 - 2, 18, 14);
  const cap = solid(mk("g", {}, svg));
  const label = mk("path", { class: "nf" }, svg), icon = mk("circle", { r: 1.7, class: "dot" }, svg);
  const barRing = rrect(58, 35.5, 98, 40.5, 2.5, 6);

  const sp = spring(0);
  let last = -1;
  function draw() {
    const z = CT - depth * clamp(sp.x, 0, 1.1);
    if (Math.abs(z - last) < 0.01) return;
    last = z;
    put(cap, prism(P, front, cOut, cIn, PT, z));
    label.setAttribute("d", poly(ringAt(P, barRing, z)));
    place(icon, P(46, 38, z));
  }

  const B = register(stage, (dt) => { const m = stepS(sp, dt); draw(); return m; });
  bag.add(B.unregister);

  // the pointer is tested on the ground plane against the cap's resting footprint, which never moves
  let on = false;
  function set(a) {
    if (a === on) return;
    on = a;
    sp.t = a ? 1 : 0;
    cap.sil.classList.toggle("hi", a);
    icon.setAttribute("class", a ? "dot m" : "dot");
    read.textContent = a ? "press" : "rest";
    B.wake();
  }
  const hit = ([sx, sy]) => {
    const [x, y] = unproj(C, sx, sy, 0);
    return x > CX0 - 3 && x < CX1 + 3 && y > CY0 - 3 && y < CY1 + 3;
  };
  bag.add(pointer(stage, { move: (p) => set(hit(p)), leave: () => set(false) }));
  bag.add(() => svg.replaceChildren());

  draw();
  return { set: (v) => { depth = v; last = -1; draw(); }, destroy: bag.dispose };
}

hairline({
  name: "button",
  means: "A pill button on a plate: the pointer over it presses it down, and its edge lights.",
  rules: [1, 4, 8, 9],
  range: [4, 8, 12],
  tour: [[205, 184], [260, 255], [190, 176], null],
  mount,
});
