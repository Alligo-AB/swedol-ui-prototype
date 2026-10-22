#!/usr/bin/env python3
"""Header-art scene for components/input.html. Geometry and camera = hairline/input.js: Cam(45,.5,2.3) + fit(...), slab 96 x 100, PT 6, field slot
x 8..88, y 41..63 (rim at the slab top, z 6), label bar at y 28.5, hint at y 71. Numbers = the three Input pages (Large, Desktop).
python3 gen/hero_input_iso.py > /tmp/scene.svg"""
from hero_scene_lib import make, scene
k = make(203.2527, 92.3091, 1.6263, 0.8132, 1.9919); P, f, line, dim, ext = k
PW, PD, PT, TOP = 96, 100, 6, 6
FX0, FX1, FY0, FY1 = 8, 88, 41, 63
ex = [ext(P(FX0, FY0, TOP), P(FX0 - 14, FY0, TOP)) + ext(P(FX0, FY1, TOP), P(FX0 - 14, FY1, TOP)) + dim(FY0, FY1, FX0 - 11, '48', 'y', z=TOP, lab=(-14, 4)),
      ext(P(FX0, FY1, TOP), P(FX0, FY1 + 14, TOP)) + ext(P(FX0 + 12, FY1, TOP), P(FX0 + 12, FY1 + 14, TOP)) + dim(FX0, FX0 + 12, FY1 + 11, '12', 'x', z=TOP, lab=(0, 14)),
      ext(P(FX1, FY0, TOP), P(FX1 + 14, FY0, TOP)) + ext(P(FX1, FY0 - 4, TOP), P(FX1 + 14, FY0 - 4, TOP)) + dim(FY0 - 4, FY0, FX1 + 11, '4', 'y', z=TOP, lab=(14, 4))]
calls = [(P(FX0 + 30, FY0, TOP), 'border-input-default · frame 1px'), (P(FX1, FY0 + 11, TOP), 'border-hover · hover frame'), (P(FX0 + 40, FY1, TOP), 'border-selected · active frame')]
sw = [('border-input-default', '#939595', '--color-border-input-default'), ('border-hover', '#333333', '--color-border-hover'), ('border-selected', '#000000', '--color-border-selected'),
      ('border-focus', '#455efb', '--color-border-focus'), ('text-tertiary', '#737373', '--color-text-tertiary'), ('text-disabled', '#939595', '--color-text-disabled')]
guide = ['Free text, number, code or search', 'Every field has a visible label', 'Say what is wrong in the message', 'Picked from a list: use a select', 'Several lines: use a textarea']
code = ['&lt;div class="form-field"&gt;&lt;label class="form-label"&gt;Order number&lt;/label&gt;', '  &lt;div class="input-wrap"&gt;&lt;div class="input-box"&gt;', '    &lt;input class="form-input" type="text"&gt;', '  &lt;/div&gt;&lt;/div&gt;&lt;/div&gt;',
        'sizes  default Large · input-box--sm · input-box--xs', 'link  /components/css/input.css + keyboard script', 'tailwind  h-12 border border-[var(--color-border-input-default)]']
spec = ['Desktop  Large 48  Small 40  XSmall 32', 'Mobile   Large 40  Small 32', 'pad L/R  12/8 · 8/4 · 8/6   icon 24 / 20 / 20', 'label to box space-4 · box to message space-4', 'frame 1px · focus ring 2px, 3px outside']
print(scene(k, 'input', '../../hairline/input.js', PW, PD, PT, [(FX0 + FX1) / 2], [(FY0 + FY1) / 2], ex, calls, [112, 160, 208], sw, guide, code, spec))
