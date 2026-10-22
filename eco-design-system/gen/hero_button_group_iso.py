#!/usr/bin/env python3
"""Header-art scene for components/button-group.html. Geometry and camera = hairline/button-group.js: Cam(45,.5,2.3) + fit(...),
slab 108 x 70, PT 5, buttons x 6..102 (3 x 32), y 24..46, resting top z 10, selected (M) sunk 3.5 to z 6.5. Numbers = the three Button group pages.
python3 gen/hero_button_group_iso.py > /tmp/scene.svg"""
from hero_scene_lib import make, scene
k = make(169.0994, 115.5625, 1.6263, 0.8132, 1.9919); P, f, line, dim, ext = k
PW, PD, PT, TOP = 108, 70, 5, 10
X0, X1, Y0, Y1 = 6, 102, 24, 46
ex = [ext(P(X0, Y0, TOP), P(X0 - 14, Y0, TOP)) + ext(P(X0, Y1, TOP), P(X0 - 14, Y1, TOP)) + dim(Y0, Y1, X0 - 11, '40', 'y', z=TOP, lab=(-14, 4)),
      ext(P(X0, Y0, TOP), P(X0, Y0 - 14, TOP)) + ext(P(X0 + 16, Y0, TOP), P(X0 + 16, Y0 - 14, TOP)) + dim(X0, X0 + 16, Y0 - 11, '16', 'x', z=TOP, lab=(0, -8))]
calls = [(P(38, 30, TOP), 'surface-opacity-black-12 · selected'), (P(70, 46, TOP), 'border-action-3 · frame 1px'), (P(22, 46, TOP), 'border-hover · hover frame')]
sw = [('text-action-primary', '#000000', '--color-text-action-primary'), ('surface-opacity-black-12', '#0000001f', '--color-surface-opacity-black-12'),
      ('border-action-3', '#0000001a', '--color-border-action-3'), ('border-hover', '#333333', '--color-border-hover'), ('border-focus', '#455efb', '--color-border-focus')]
guide = ['2 to 4 short options on one row', 'Label the group: aria-label', 'Selected: aria-pressed="true"', 'More options: use a select', 'Not for page navigation']
code = ['&lt;div class="btn-group" role="group" aria-label="Size"&gt;', '  &lt;button type="button" aria-pressed="true"&gt;M&lt;/button&gt;', '&lt;/div&gt;',
        'link  /components/css/button-group.css', 'your script moves aria-pressed; the CSS does not', 'tailwind  inline-flex max-w-full', '          duration-100 ease-[cubic-bezier(.35,0,.35,1)]']
spec = ['Mobile   h 32  pad 0 10  label 14/14 .42px', 'Desktop  h 40  pad 0 16  label 16/16 .48px  (769px+)', 'frame 1px inside · neighbours share it, ml -1', 'focus ring 2px, gap 2px · fill + frame 100ms']
print(scene(k, 'button-group', '../../hairline/button-group.js', PW, PD, PT, [X0 + 16, X0 + 48, X0 + 80], [(Y0 + Y1) / 2], ex, calls, [112, 160, 208], sw, guide, code, spec))
