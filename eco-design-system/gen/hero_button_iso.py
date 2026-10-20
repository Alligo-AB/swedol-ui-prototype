#!/usr/bin/env python3
"""Header-art scene for the Button docs page (components/button.html): the same recipe as gen/hero_switch_iso.py (scene mode), with the geometry and
the numbers of hairline/button-pair.js and of the three Button pages. Projection constants = Cam(45, .5, 1.9) + fit(...) in button-pair.js
(slab 108 x 90, PT 5, buttons x 8..100, y 10..40 and 50..80, top z 12). Change them if that figure's camera or fit points change.
python3 gen/hero_button_iso.py > /tmp/scene.svg   (the figure is a foreignObject: ../../hairline/button-pair.js, data-flat)"""
import math
OX, OY, SX, SY, SZ = 187.9085, 114.5466, 1.3435, 0.6718, 1.6454
def P(x, y, z=0): return (OX + SX * (x - y), OY + SY * (x + y) - SZ * z)
f = lambda p: f'{p[0]:.1f} {p[1]:.1f}'
def line(pts, close=False): return 'M' + 'L'.join(f(p) for p in pts) + ('z' if close else '')
PW, PD, PT, TOP = 108, 90, 5, 12
BX0, BX1 = 8, 100; BTN = [(10, 40), (50, 80)]
VX0, VW, VY0, VH = -440, 1060, -24, 368
G0, G1 = -260, 260
FIG_SRC = '../../hairline/button-pair.js'
T = 'var(--color-text-tertiary)'

def dim(a, b, off, label, along='x', z=PT, lab=(0, -7)):
    (p, q) = (P(a, off, z), P(b, off, z)) if along == 'x' else (P(off, a, z), P(off, b, z))
    mid = ((p[0] + q[0]) / 2 + lab[0], (p[1] + q[1]) / 2 + lab[1])
    u = (q[0] - p[0], q[1] - p[1]); l = math.hypot(*u); u = (u[0] / l, u[1] / l)
    return (f'<g class="d"><path d="{line([p, q])}"/><path class="ar" d="M{f(p)}l{7*u[0]-3*u[1]:.1f} {7*u[1]+3*u[0]:.1f}l{6*u[1]:.1f} {-6*u[0]:.1f}zM{f(q)}l{-7*u[0]-3*u[1]:.1f} {-7*u[1]+3*u[0]:.1f}l{6*u[1]:.1f} {-6*u[0]:.1f}z"/>'
            f'<text x="{mid[0]:.1f}" y="{mid[1]:.1f}" text-anchor="middle">{label}</text></g>')
def ext(p, q): return f'<path class="x" d="{line([p, q])}"/>'

out = [f'<svg class="ds-hero-art__bp" viewBox="{VX0} {VY0} {VW} {VH}" aria-hidden="true" focusable="false" preserveAspectRatio="xMaxYMid meet"><defs>'
       f'<clipPath id="iso-clip-s"><rect x="{VX0}" y="{VY0}" width="{VW}" height="{VH}"/></clipPath></defs>']
g = []
for c in range(G0, G1 + 1, 8):
    cls = 'gm' if c % 24 == 0 else 'gn'
    g.append((cls, line([P(c, G0), P(c, G1)]))); g.append((cls, line([P(G0, c), P(G1, c)])))
out.append('<g clip-path="url(#iso-clip-s)" class="grid">' + ''.join(f'<path class="{c}" d="{d}"/>' for c, d in sorted(g)) + '</g>')
ex = []
for (y0, y1) in BTN: ex.append(f'<path class="g" d="{line([P(G0, (y0 + y1) / 2, PT), P(G1, (y0 + y1) / 2, PT)])}"/>')
for x in (BX0, BX1): ex.append(f'<path class="g" d="{line([P(x, G0, PT), P(x, G1, PT)])}"/>')
for (x, y) in ((0, 0), (PW, 0), (PW, PD), (0, PD)):
    ex.append(f'<path class="x" d="{line([P(x, y, PT), P(x + (-1 if x == 0 else 1) * 60, y, PT)])}"/><path class="x" d="{line([P(x, y, PT), P(x, y + (-1 if y == 0 else 1) * 60, PT)])}"/>')
for gx in range(-240, 241, 96):
    for gy in range(-240, 241, 96): ex.append(f'<path class="x" d="{line([P(gx - 3, gy, 0), P(gx + 3, gy, 0)])}M{f(P(gx, gy - 3, 0))}L{f(P(gx, gy + 3, 0))}"/>')
for t in range(0, PW + 1, 8): ex.append(f'<path class="x" d="{line([P(t, PD + 4, PT), P(t, PD + (9 if t % 16 == 0 else 6), PT)])}"/>')
for t in range(0, PD + 1, 8): ex.append(f'<path class="x" d="{line([P(PW + 4, t, PT), P(PW + (9 if t % 16 == 0 else 6), t, PT)])}"/>')
out.insert(2, '<g>' + ''.join(ex) + '</g>')
out.append(f'<foreignObject x="0" y="0" width="400" height="320"><div data-hairline-card="button-pair" data-flat data-src="{FIG_SRC}" style="width:400px;height:320px"></div></foreignObject>')
# dimensions: width and height of a Large button (desktop), the 8px gap
y0, y1 = BTN[0]; y2 = BTN[1][0]
out.append(ext(P(BX0, y0, TOP), P(BX0, y0 - 14, TOP)) + ext(P(BX1, y0, TOP), P(BX1, y0 - 14, TOP)) + dim(BX0, BX1, y0 - 11, '134', 'x', z=TOP, lab=(0, -8)))
out.append(ext(P(BX0, y0, TOP), P(BX0 - 14, y0, TOP)) + ext(P(BX0, y1, TOP), P(BX0 - 14, y1, TOP)) + dim(y0, y1, BX0 - 11, '56', 'y', z=TOP, lab=(-14, 4)))
out.append(ext(P(BX1, y1, TOP), P(BX1 + 14, y1, TOP)) + ext(P(BX1, y2, TOP), P(BX1 + 14, y2, TOP)) + dim(y1, y2, BX1 + 11, '8', 'y', z=TOP, lab=(14, 4)))
# callouts to the right (sorted by height so leaders never cross)
calls = [(P(50, 25, TOP), 'surface-action-1 · fill'), (P(70, 80, TOP), 'border-action-1 · frame 1px'), (P(30, 50, TOP), 'surface-opacity-white-20 · hover')]
calls.sort(key=lambda c: c[0][1]); rows = [112, 160, 208]
for (p, label), ry in zip(calls, rows):
    out.append(f'<g class="c"><path d="M{f(p)}L400 {ry}H{VX0 + VW - 44}"/><circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="2.5"/><text x="404" y="{ry-5}">{label}</text></g>')
# colour swatches (token, hex)
sw = [('surface-action-1', '#000000', '--color-surface-action-1'), ('border-action-1', '#000000', '--color-border-action-1'), ('surface-danger-default', '#d90000', '--color-surface-danger-default'),
      ('accent-default', '#c7d300', '--color-accent-default'), ('border-action-3', '#0000001a', '--color-border-action-3'), ('surface-opacity-white-20', '#ffffff33', '--color-surface-opacity-white-20')]
out.append('<text class="lab" x="404" y="232">Colour</text>')
for i, (name, hexv, var) in enumerate(sw):
    y = 244 + i * 13
    out.append(f'<rect class="sw" x="404" y="{y - 8}" width="9" height="9" style="fill:var({var})"/><text x="418" y="{y}">{name}</text><text class="code" x="{VX0 + VW - 44}" y="{y}" text-anchor="end">{hexv}</text>')
# the three tabs of the docs page as data: Guidelines, Code, Specifications
gd = ['One Primary per screen or section', 'Primary + Secondary, space-8 apart', 'Label names the action', 'Not for links: use a link', 'Tab: ring 2px, offset 2px']
out.append('<text class="lab" x="-120" y="-4">Examples &amp; Guidelines</text>' + ''.join(f'<text x="-120" y="{10 + k * 13}">{t}</text>' for k, t in enumerate(gd)))
code = ['&lt;button class="btn btn--primary btn--lg"&gt;', '  &lt;span class="btn__label"&gt;Add to cart&lt;/span&gt;', '&lt;/button&gt;',
        'btn--primary · secondary · blank · destructive · accent · system', 'btn--lg · md · sm · xs   (switch at 769px)', 'tailwind  h-14 px-4 bg-[var(--color-surface-action-1)]', '          duration-100 ease-[cubic-bezier(.35,0,.35,1)]']
out.append('<text class="lab" x="196" y="-4">Code</text>' + ''.join(f'<text class="code" x="196" y="{10 + k * 12}">{t}</text>' for k, t in enumerate(code)))
spec = ['Large    56 / 48  pad 16 / 12  inset 8  icon 24', 'Medium   48 / 40  pad 12 / 8   inset 8  icon 24', 'Small    40 / 32  pad 8 / 4    inset 8 / 6  icon 24', 'XSmall   32 / 32  pad 6        inset 4  icon 20', 'frame 1px inside · hover 100ms ease-standard']
out.append('<text class="lab" x="60" y="268">Specifications</text>' + ''.join(f'<text class="code" x="60" y="{280 + k * 12}">{t}</text>' for k, t in enumerate(spec)))
out.append('</svg>')
print(''.join(out))
