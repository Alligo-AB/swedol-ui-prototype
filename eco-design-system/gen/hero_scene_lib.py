"""Shared builder for the header-art scene (see eco-doc-page, Header art). hero_switch_iso.py and hero_button_iso.py keep their own copy;
newer components (button group, checkbox, radio, input) import this. A component script sets the projection constants of its figure
(Cam(45, .5, S) + fit(...): SX = S cos45, SY = .5 S sin45, SZ = S sqrt(.75), OX/OY from the fit) and calls scene()."""
import math

def make(OX, OY, SX, SY, SZ):
    P = lambda x, y, z=0: (OX + SX * (x - y), OY + SY * (x + y) - SZ * z)
    f = lambda p: f'{p[0]:.1f} {p[1]:.1f}'
    line = lambda pts, close=False: 'M' + 'L'.join(f(p) for p in pts) + ('z' if close else '')
    def dim(a, b, off, label, along='x', z=0, lab=(0, -7)):
        (p, q) = (P(a, off, z), P(b, off, z)) if along == 'x' else (P(off, a, z), P(off, b, z))
        mid = ((p[0] + q[0]) / 2 + lab[0], (p[1] + q[1]) / 2 + lab[1])
        u = (q[0] - p[0], q[1] - p[1]); l = math.hypot(*u); u = (u[0] / l, u[1] / l)
        return (f'<g class="d"><path d="{line([p, q])}"/><path class="ar" d="M{f(p)}l{7*u[0]-3*u[1]:.1f} {7*u[1]+3*u[0]:.1f}l{6*u[1]:.1f} {-6*u[0]:.1f}zM{f(q)}l{-7*u[0]-3*u[1]:.1f} {-7*u[1]+3*u[0]:.1f}l{6*u[1]:.1f} {-6*u[0]:.1f}z"/>'
                f'<text x="{mid[0]:.1f}" y="{mid[1]:.1f}" text-anchor="middle">{label}</text></g>')
    ext = lambda p, q: f'<path class="x" d="{line([p, q])}"/>'
    return P, f, line, dim, ext

def scene(k, fig, fig_src, PW, PD, PT, ax_x, ax_y, extras, calls, rows, swatches, guide, code, spec, flat=True):
    """k = make(...) tuple; ax_x/ax_y = long axes through the figure's parts; extras = svg strings drawn over the figure;
    calls = [(point, label)]; swatches = [(token, hex, css var)]; guide/code/spec = lines of the three tabs."""
    P, f, line, dim, ext = k
    VX0, VW, VY0, VH, G0, G1 = -440, 1060, -24, 368, -260, 260
    out = [f'<svg class="ds-hero-art__bp" viewBox="{VX0} {VY0} {VW} {VH}" aria-hidden="true" focusable="false" preserveAspectRatio="xMaxYMid meet"><defs>'
           f'<clipPath id="iso-clip-s"><rect x="{VX0}" y="{VY0}" width="{VW}" height="{VH}"/></clipPath></defs>']
    g = []
    for c in range(G0, G1 + 1, 8):
        cls = 'gm' if c % 24 == 0 else 'gn'
        g.append((cls, line([P(c, G0), P(c, G1)]))); g.append((cls, line([P(G0, c), P(G1, c)])))
    out.append('<g clip-path="url(#iso-clip-s)" class="grid">' + ''.join(f'<path class="{c}" d="{d}"/>' for c, d in sorted(g)) + '</g>')
    ex = [f'<path class="g" d="{line([P(G0, y, PT), P(G1, y, PT)])}"/>' for y in ax_y] + [f'<path class="g" d="{line([P(x, G0, PT), P(x, G1, PT)])}"/>' for x in ax_x]
    for (x, y) in ((0, 0), (PW, 0), (PW, PD), (0, PD)):
        ex.append(f'<path class="x" d="{line([P(x, y, PT), P(x + (-1 if x == 0 else 1) * 60, y, PT)])}"/><path class="x" d="{line([P(x, y, PT), P(x, y + (-1 if y == 0 else 1) * 60, PT)])}"/>')
    for gx in range(-240, 241, 96):
        for gy in range(-240, 241, 96): ex.append(f'<path class="x" d="{line([P(gx - 3, gy, 0), P(gx + 3, gy, 0)])}M{f(P(gx, gy - 3, 0))}L{f(P(gx, gy + 3, 0))}"/>')
    for t in range(0, PW + 1, 8): ex.append(f'<path class="x" d="{line([P(t, PD + 4, PT), P(t, PD + (9 if t % 16 == 0 else 6), PT)])}"/>')
    for t in range(0, PD + 1, 8): ex.append(f'<path class="x" d="{line([P(PW + 4, t, PT), P(PW + (9 if t % 16 == 0 else 6), t, PT)])}"/>')
    out.insert(2, '<g>' + ''.join(ex) + '</g>')
    out.append(f'<foreignObject x="0" y="0" width="400" height="320"><div data-hairline-card="{fig}"{" data-flat" if flat else ""} data-src="{fig_src}" style="width:400px;height:320px"></div></foreignObject>')
    out += extras
    calls = sorted(calls, key=lambda c: c[0][1])
    for (p, label), ry in zip(calls, rows):
        out.append(f'<g class="c"><path d="M{f(p)}L400 {ry}H{VX0 + VW - 44}"/><circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="2.5"/><text x="404" y="{ry-5}">{label}</text></g>')
    sy0 = rows[-1] + 24
    out.append(f'<text class="lab" x="404" y="{sy0}">Colour</text>')
    for i, (name, hexv, var) in enumerate(swatches):
        y = sy0 + 12 + i * 13
        out.append(f'<rect class="sw" x="404" y="{y - 8}" width="9" height="9" style="fill:var({var})"/><text x="418" y="{y}">{name}</text><text class="code" x="{VX0 + VW - 44}" y="{y}" text-anchor="end">{hexv}</text>')
    out.append('<text class="lab" x="-120" y="-4">Examples &amp; Guidelines</text>' + ''.join(f'<text x="-120" y="{10 + i * 13}">{t}</text>' for i, t in enumerate(guide)))
    out.append('<text class="lab" x="196" y="-4">Code</text>' + ''.join(f'<text class="code" x="196" y="{10 + i * 12}">{t}</text>' for i, t in enumerate(code)))
    out.append('<text class="lab" x="60" y="268">Specifications</text>' + ''.join(f'<text class="code" x="60" y="{280 + i * 12}">{t}</text>' for i, t in enumerate(spec)))
    out.append('</svg>')
    return ''.join(out)
