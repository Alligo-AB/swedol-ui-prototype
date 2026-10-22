#!/usr/bin/env python3
"""Header-art scene for components/radio.html. Geometry and camera = hairline/radio.js (same as checkbox.js): Cam(45,.5,2.5) + fit(...), slab 116 x 56,
PT 6, three 24 x 24 wells at x 12 / 46 / 80, y 16..40, cut into the slab, so the measured plane is the slab top (z 6). Numbers = the three Radio pages (Large, Desktop).
python3 gen/hero_radio_iso.py > /tmp/scene.svg"""
from hero_scene_lib import make, scene
k = make(146.967, 95.986, 1.7678, 0.8839, 2.1651); P, f, line, dim, ext = k
PW, PD, PT, TOP = 116, 56, 6, 6
Y0, Y1 = 16, 40
ex = [ext(P(12, Y0, TOP), P(12, Y0 - 14, TOP)) + ext(P(36, Y0, TOP), P(36, Y0 - 14, TOP)) + dim(12, 36, Y0 - 11, '24', 'x', z=TOP, lab=(0, -8)),
      ext(P(16, Y1, TOP), P(16, Y1 + 14, TOP)) + ext(P(32, Y1, TOP), P(32, Y1 + 14, TOP)) + dim(16, 32, Y1 + 11, '16', 'x', z=TOP, lab=(0, 14)),
      ext(P(12, 28, TOP), P(4, 28, TOP)) + ext(P(12, 22, TOP), P(4, 22, TOP)) + dim(22, 34, 7, '6', 'y', z=TOP, lab=(-14, 4)),
      ext(P(36, Y0, TOP), P(36, Y0 - 26, TOP)) + ext(P(32, Y0 + 4, TOP), P(32, Y0 - 26, TOP)) + dim(32, 36, Y0 - 23, '4', 'x', z=TOP, lab=(0, -8))]
calls = [(P(24, 28, TOP), 'surface-100 · dot 6px'), (P(58, 40, TOP), 'border-input-control-default · 1px'), (P(92, 28, TOP), 'border-hover · hover frame')]
sw = [('surface-100', '#000000', '--color-surface-100'), ('border-input-control-default', '#737373', '--color-border-input-control-default'), ('border-hover', '#333333', '--color-border-hover'),
      ('border-selected-hover', '#737373', '--color-border-selected-hover'), ('border-focus', '#455efb', '--color-border-focus'), ('border-disabled', '#dad9d7', '--color-border-disabled')]
guide = ['Exactly one of 2+ options, all visible', 'Preselect a default in every group', 'Stack vertically; row only for 2 short', 'Several choices: use a checkbox', 'Applies at once: use a switch']
code = ['&lt;fieldset class="form-radio-group"&gt;&lt;legend&gt;Delivery&lt;/legend&gt;', '  &lt;label class="form-radio-item"&gt;', '    &lt;input type="radio" name="d" checked&gt;&lt;span&gt;Home&lt;/span&gt;', '  &lt;/label&gt;&lt;/fieldset&gt;',
        'same name per group · form-radio-item--sm', 'link  /components/css/radio.css', 'dot  radial-gradient, no SVG or image']
spec = ['Large  area 24  circle 16  margin 4  dot 6  gap 8', 'Small  area 20  circle 14  margin 3  dot 6  gap 8', 'frame 1px · focus ring 2px, offset 2px', 'options 4 apart · no motion, state changes at once']
print(scene(k, 'radio', '../../hairline/radio.js', PW, PD, PT, [24, 58, 92], [28], ex, calls, [112, 160, 208], sw, guide, code, spec))
