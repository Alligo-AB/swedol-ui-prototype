#!/usr/bin/env python3
"""Isometric blueprint for the Switch docs header, version 2 (same camera as hairline/switch.js, so it lies exactly over the figure).
viewBox -40 0 600 320: the figure's stage is x 0..400, the extra 100 on the right is room for callouts. World units are the figure's
(slab 96x100, slots 64x32 = 48x24 px x 4/3, thumb r 13), labels are the real px values. Projection constants come from
Cam(45, .5, 2.3) + fit(...) in switch.js: change them if the figure's camera or fit points change (hairline/ has the kernel).
python3 gen/hero_switch_iso.py > /tmp/iso.svg"""
import math, sys
SCENE = 'scene' in sys.argv
SUF = '-s' if SCENE else ''  # unique ids when both drawings are on one page
PAR = ' preserveAspectRatio="xMaxYMid meet"' if SCENE else ''
# 'scene': a wide drawing for the header background (version 2b): bigger grid, long axes, spacing ticks, no clipping at the figure's stage
VX0, VW = (-440, 1060) if SCENE else (-40, 600)
VY0, VH = (-24, 368) if SCENE else (0, 320)
G0, G1 = (-260, 260) if SCENE else (-48, 148)
FIG_SRC = '../../hairline/switch.js'  # the figure sits in the scene as a foreignObject, so it scales with the drawing
OX, OY, SX, SY, SZ = 203.2527, 92.3091, 1.6263, 0.8132, 1.9918
def P(x, y, z=0): return (OX + SX * (x - y), OY + SY * (x + y) - SZ * z)
f = lambda p: f'{p[0]:.1f} {p[1]:.1f}'
def line(pts, close=False): return 'M' + 'L'.join(f(p) for p in pts) + ('z' if close else '')
PW, PD, PT, D = 96, 100, 6, 2
TX0, TX1, R, IN, LIFT = 16, 80, 13, 3, 2
SLOTS = [(14, 46), (54, 86)]; ON, OFF = TX1 - R - IN, TX0 + R + IN
T = 'var(--color-text-tertiary)'; PR = 'var(--color-text-primary)'; G = 'var(--color-surface-success-default)'

def pill(x0, y0, x1, y1, z, n=14):
    r = (y1 - y0) / 2; pts = []
    for i in range(n + 1):  # right cap, then left cap
        a = -math.pi / 2 + math.pi * i / n; pts.append(P(x1 - r + r * math.cos(a), y0 + r + r * math.sin(a), z))
    for i in range(n + 1):
        a = math.pi / 2 + math.pi * i / n; pts.append(P(x0 + r + r * math.cos(a), y0 + r + r * math.sin(a), z))
    return pts
def circ(cx, cy, r, z, n=28): return [P(cx + r * math.cos(2 * math.pi * i / n), cy + r * math.sin(2 * math.pi * i / n), z) for i in range(n)]
def dim(a, b, off, label, along='x', z=PT, lab=(0, -7)):
    """a, b: world coordinate range along `along`; off: world coordinate of the dimension line on the other axis; extension lines run from `ext` to it."""
    (p, q) = (P(a, off, z), P(b, off, z)) if along == 'x' else (P(off, a, z), P(off, b, z))
    mid = ((p[0] + q[0]) / 2 + lab[0], (p[1] + q[1]) / 2 + lab[1])
    u = (q[0] - p[0], q[1] - p[1]); l = math.hypot(*u); u = (u[0] / l, u[1] / l)
    ar = lambda e, s: f'M{f(e)}l{s*7*u[0]-3*u[1]:.1f} {s*7*u[1]+3*u[0]:.1f}l0 0m0 0L{f(e)}l{s*7*u[0]+3*u[1]:.1f} {s*7*u[1]-3*u[0]:.1f}'
    return f'<g class="d"><path d="{line([p, q])}"/><path class="ar" d="M{f(p)}l{7*u[0]-3*u[1]:.1f} {7*u[1]+3*u[0]:.1f}l{6*u[1]:.1f} {-6*u[0]:.1f}zM{f(q)}l{-7*u[0]-3*u[1]:.1f} {-7*u[1]+3*u[0]:.1f}l{6*u[1]:.1f} {-6*u[0]:.1f}z"/><text x="{mid[0]:.1f}" y="{mid[1]:.1f}" text-anchor="middle">{label}</text></g>'
def ext(p, q): return f'<path class="x" d="{line([p, q])}"/>'

out = []
out.append(f'<svg class="ds-hero-art__bp" viewBox="{VX0} {VY0} {VW} {VH}" aria-hidden="true" focusable="false"{PAR}><defs>'
           f'<clipPath id="iso-clip{SUF}"><rect x="{VX0}" y="{VY0}" width="{VW}" height="{VH}"/></clipPath>'
           f'<pattern id="iso-hatch{SUF}" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><path d="M0 0V6" stroke="{G}" stroke-width=".9"/></pattern></defs>')
# ground grid on z=0: minor every 8 units, major every 24
g = []
for c in range(G0, G1 + 1, 8):
    cls = 'gm' if c % 24 == 0 else 'gn'
    g.append((cls, line([P(c, G0), P(c, G1)]))); g.append((cls, line([P(G0, c), P(G1, c)])))
out.append(f'<g clip-path="url(#iso-clip{SUF})" class="grid">' + ''.join(f'<path class="{c}" d="{d}"/>' for c, d in sorted(g)) + '</g>')
FIGSTR = ''
if SCENE:
    FIGSTR = (f'<foreignObject x="0" y="0" width="400" height="320"><div data-hairline-card="switch" data-flat data-src="{FIG_SRC}" style="width:400px;height:320px"></div></foreignObject>')
    out.append(FIGSTR)
# slab
out.append(f'<path class="o" d="{line([P(0,0,PT),P(PW,0,PT),P(PW,PD,PT),P(0,PD,PT)], True)}"/><path class="x" d="{line([P(0,PD,PT),P(0,PD,0),P(PW,PD,0),P(PW,PD,PT)])}"/><path class="x" d="{line([P(PW,0,PT),P(PW,0,0),P(PW,PD,0)])}"/>')

if SCENE:
    # abstract details in the figure's own world: long axes through the slots and thumbs, extension lines of the slab, registration crosses, spacing ticks
    ex = []
    for cy in (30, 70): ex.append(f'<path class="g" d="{line([P(G0, cy, PT), P(G1, cy, PT)])}"/>')
    for x in (TX0, TX1, ON, OFF): ex.append(f'<path class="g" d="{line([P(x, G0, PT), P(x, G1, PT)])}"/>')
    for (x, y) in ((0, 0), (PW, 0), (PW, PD), (0, PD)):
        ex.append(f'<path class="x" d="{line([P(x, y, PT), P(x + (-1 if x == 0 else 1) * 60, y, PT)])}"/><path class="x" d="{line([P(x, y, PT), P(x, y + (-1 if y == 0 else 1) * 60, PT)])}"/>')
    for gx in range(-240, 241, 96):
        for gy in range(-240, 241, 96):
            ex.append(f'<path class="x" d="{line([P(gx - 3, gy, 0), P(gx + 3, gy, 0)])}M{f(P(gx, gy - 3, 0))}L{f(P(gx, gy + 3, 0))}"/>')
    for t in range(0, PW + 1, 8): ex.append(f'<path class="x" d="{line([P(t, PD + 4, PT), P(t, PD + (9 if t % 16 == 0 else 6), PT)])}"/>')
    for t in range(0, PD + 1, 8): ex.append(f'<path class="x" d="{line([P(PW + 4, t, PT), P(PW + (9 if t % 16 == 0 else 6), t, PT)])}"/>')
    out.insert(2, '<g>' + ''.join(ex) + '</g>')
# slots: outline at the rim, hatched floor on the Email slot, thumbs
for i, (y0, y1) in enumerate(SLOTS):
    cy = (y0 + y1) / 2
    out.append(f'<path class="o" d="{line(pill(TX0, y0, TX1, y1, PT), True)}"/>')
    hatch_attr = ' fill="url(#iso-hatch' + SUF + ')"' if i == 0 else ''
    out.append(f'<path class="{"hatch" if i == 0 else "x"}"{hatch_attr} d="{line(pill(TX0, y0, TX1, y1, PT - D), True)}"/>')
    out.append(f'<path class="g" d="{line([P(TX0 - 6, cy, PT), P(TX1 + 6, cy, PT)])}"/>')
cy1, cy2 = 30, 70
if SCENE: del out[out.index(FIGSTR) + 1:]  # the figure already draws slab, slots and thumbs; keep ghost thumb, axes, dimensions, callouts
if not SCENE: out.append(f'<path class="o f" d="{line(circ(ON, cy1, R, PT + LIFT), True)}"/><path class="x" d="{line([P(ON-R,cy1,PT+LIFT),P(ON-R,cy1,PT-D+.6)])}M{f(P(ON+R,cy1,PT+LIFT))}L{f(P(ON+R,cy1,PT-D+.6))}"/><path class="x" d="{line(circ(ON, cy1, R, PT-D+.6), True)}"/>')
out.append(f'<path class="gh" d="{line(circ(OFF, cy1, R, PT + LIFT), True)}"/><path class="g" d="{line([P(ON,cy1-R-8,PT),P(ON,cy1+R+8,PT)])}M{f(P(OFF,cy1-R-8,PT))}L{f(P(OFF,cy1+R+8,PT))}"/>')
if not SCENE: out.append(f'<path class="o f" d="{line(circ(OFF, cy2, R, PT + LIFT), True)}"/>')
# dimensions (real px values): 48 wide, 24 tall, thumb 20, inset 2, travel 24
y0, y1 = SLOTS[0]
out.append(ext(P(TX0, y0, PT), P(TX0, y0 - 14, PT)) + ext(P(TX1, y0, PT), P(TX1, y0 - 14, PT)) + dim(TX0, TX1, y0 - 11, '48', 'x', lab=(0, -8)))
out.append(ext(P(TX0, y0, PT), P(TX0 - 14, y0, PT)) + ext(P(TX0, y1, PT), P(TX0 - 14, y1, PT)) + dim(y0, y1, TX0 - 11, '24', 'y', lab=(-14, 4)))
out.append(ext(P(ON, cy1 - R, PT + LIFT), P(TX1 + 14, cy1 - R, PT + LIFT)) + ext(P(ON, cy1 + R, PT + LIFT), P(TX1 + 14, cy1 + R, PT + LIFT)) + dim(cy1 - R, cy1 + R, TX1 + 11, '20', 'y', lab=(16, 4)))
out.append(dim(OFF, ON, (y1 + SLOTS[1][0]) / 2, '24 travel', 'x', lab=(-6, 24)))
out.append(ext(P(TX1, y0 - 4, PT), P(TX1, y0 - 12, PT)) if False else '')
# code snippet, top right of the figure
if not SCENE: out.append('<text class="code" x="196" y="22">.form-switch-item input[role="switch"] {</text><text class="code" x="208" y="37">width: 48px; height: 24px; border-radius: 999px;</text><text class="code" x="196" y="52">}</text>')
# callouts to the right, sorted by height so the leaders never cross
calls = [(P(ON + 6, cy1 + 6, PT + LIFT), 'surface-raised-primary'), (P(40, 22, PT - D), 'surface-success-default'), (P(52, cy2 + 6, PT - D), 'surface-20 · off')]
rows = [112, 176, 240]
if SCENE:
    # focus ring (2px ring, 2px offset, border-focus) and its callout
    out.append(f'<path class="fr" d="{line(circ(ON, cy1, R + 4, PT + LIFT), True)}"/>')
    calls.append((P(ON + (R + 4) * .7, cy1 - (R + 4) * .7, PT + LIFT), 'border-focus · ring 2px, offset 2px'))
    rows = [100, 138, 176, 214]
calls.sort(key=lambda c: c[0][1])
for (p, label), ry in zip(calls, rows):
    out.append(f'<g class="c"><path d="M{f(p)}L{400} {ry}H{VX0 + VW - 44}"/><circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="2.5"/><text x="404" y="{ry-5}">{label}</text></g>')
if SCENE:
    # colour swatches (token, hex) and the Tailwind equivalent of the same switch
    sw = [('surface-success-default', '#248616', '--color-surface-success-default', 'on'), ('on · hover', '#71b790', None, ''), ('surface-20', '#cccccc', '--color-surface-20', 'off'),
          ('surface-15', '#dad9d7', '--color-surface-15', 'off · hover'), ('surface-raised-primary', '#ffffff', '--color-surface-raised-primary', 'thumb')]
    out.append('<text class="lab" x="404" y="240">Colour</text>')
    for i, (name, hexv, var, role) in enumerate(sw):
        y = 252 + i * 13
        fillv = f'var({var})' if var else '#71b790'
        out.append(f'<rect class="sw" x="404" y="{y - 8}" width="9" height="9" style="fill:{fillv}"/><text x="418" y="{y}">{name}</text><text class="code" x="{VX0 + VW - 44}" y="{y}" text-anchor="end">{hexv}</text>')
    # the three tabs of the docs page as data: Guidelines, Code, Specifications
    g = ['On or off: one setting', 'Applies at once', 'Not for options: use radio', 'Space, Tab, click · role=switch', 'Ring 2px, offset 2px · WCAG 1.4.1']
    out.append('<text class="lab" x="-120" y="-4">Examples &amp; Guidelines</text>' + ''.join(f'<text x="-120" y="{10 + k * 13}">{t}</text>' for k, t in enumerate(g)))
    code = ['&lt;label class="form-switch-item"&gt;', '  &lt;input type="checkbox" role="switch" checked&gt;', '  &lt;span&gt;Email&lt;/span&gt;&lt;/label&gt;',
            'form-switch-item · --sm · --xs · --dark', 'tailwind  h-6 w-12 rounded-full p-0.5 · thumb h-5 w-5 translate-x-6', '          duration-150 ease-[cubic-bezier(.35,0,.35,1)]']
    out.append('<text class="lab" x="196" y="-4">Code</text>' + ''.join(f'<text class="code" x="196" y="{10 + k * 12}">{t}</text>' for k, t in enumerate(code)))
    spec = ['Large, Small   track 48×24 · thumb 20 · inset 2 · travel 24', 'X-Small        track 32×16 · thumb 12 · inset 2 · travel 16', 'label body-md 16/22, 17/24 from 769 · gap space-8', 'motion duration-fast-3 · ease-standard (150ms)']
    out.append('<text class="lab" x="60" y="272">Specifications</text>' + ''.join(f'<text class="code" x="60" y="{285 + k * 12}">{t}</text>' for k, t in enumerate(spec)))
out.append('</svg>')
print(''.join(out))
