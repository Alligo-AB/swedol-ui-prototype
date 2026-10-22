#!/usr/bin/env python3
"""Header-art scene for components/checkbox.html. Geometry and camera = hairline/checkbox.js: Cam(45,.5,2.5) + fit(...), slab 116 x 56, PT 6,
three 24 x 24 boxes at x 12 / 46 / 80, y 16..40, tile top z 7.5 (D = 2). Numbers = the three Checkbox pages (Large, Desktop).
python3 gen/hero_checkbox_iso.py > /tmp/scene.svg"""
from hero_scene_lib import make, scene
k = make(146.967, 95.986, 1.7678, 0.8839, 2.1651); P, f, line, dim, ext = k
PW, PD, PT, TOP = 116, 56, 6, 7.5
XS, Y0, Y1, BS = (12, 46, 80), 16, 40, 24
ex = [ext(P(12, Y0, TOP), P(12, Y0 - 14, TOP)) + ext(P(36, Y0, TOP), P(36, Y0 - 14, TOP)) + dim(12, 36, Y0 - 11, '24', 'x', z=TOP, lab=(0, -8)),
      ext(P(16, Y1, TOP), P(16, Y1 + 14, TOP)) + ext(P(32, Y1, TOP), P(32, Y1 + 14, TOP)) + dim(16, 32, Y1 + 11, '16', 'x', z=TOP, lab=(0, 14)),
      ext(P(12, Y0, TOP), P(4, Y0, TOP)) + ext(P(12, Y1, TOP), P(4, Y1, TOP)) + dim(Y0, Y1, 7, '24', 'y', z=TOP, lab=(-14, 4)),
      ext(P(36, Y0, TOP), P(36, Y0 - 26, TOP)) + ext(P(32, Y0 + 4, TOP), P(32, Y0 - 26, TOP)) + dim(32, 36, Y0 - 23, '4', 'x', z=TOP, lab=(0, -8))]
calls = [(P(24, 28, TOP), 'surface-100 · checked fill'), (P(58, 40, TOP), 'border-primary · box frame 1px'), (P(92, 28, TOP), 'border-hover · hover frame')]
sw = [('surface-100', '#000000', '--color-surface-100'), ('icon-inverted', '#ffffff', '--color-icon-inverted'), ('border-primary', '#e5e5e5', '--color-border-primary'),
      ('border-hover', '#333333', '--color-border-hover'), ('border-focus', '#455efb', '--color-border-focus'), ('surface-40', '#939595', '--color-surface-40')]
guide = ['Any number of options, saved on submit', 'Several options: a fieldset with a legend', 'One of many: use a radio', 'Applies at once: use a switch', 'Mixed = select-all parent only']
code = ['&lt;label class="form-checkbox-item"&gt;', '  &lt;input type="checkbox"&gt;&lt;span&gt;Leave at door&lt;/span&gt;', '&lt;/label&gt;',
        'dark surface  form-checkbox-item--dark', 'mixed  input.indeterminate = true (JS only)', 'link  /components/css/checkbox.css', 'sizes  default Large · form-checkbox-item--sm']
spec = ['Large  area 24  box 16  margin 4  gap 8  body-md', 'Small  area 20  box 14  margin 3  gap 4  body-sm', 'frame 1px · hover border-hover · focus ring 2px', 'tiles  swatch 24 · image 48 · number 48 (mobile 40)']
print(scene(k, 'checkbox', '../../hairline/checkbox.js', PW, PD, PT, [24, 58, 92], [28], ex, calls, [112, 160, 208], sw, guide, code, spec))
