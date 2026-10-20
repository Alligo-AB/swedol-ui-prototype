#!/usr/bin/env python3
"""Blueprint drawing for the Switch docs header (components/switch.html, .ds-hero-art__bp). Prints the <svg>.
1 px of the real switch = K units (track 48x24, thumb 20, inset 2: sizes from eco-switch). Run:  python3 gen/hero_switch.py > /tmp/bp.svg
Use as a model for another component: change the geometry block, the dimensions and the token callouts; CSS is doc-hero.css."""
K = 5; VW, VH = 700, 352; X0, CY = 300, 176; W, H = 48 * K, 24 * K; Y0 = CY - H // 2; X1 = X0 + W
TR = 10 * K; INS = 2 * K; ON = X1 - INS - TR; OFF = X0 + INS + TR
T = 'var(--color-text-tertiary)'; P = 'var(--color-text-primary)'; G = 'var(--color-surface-success-default)'
def dim_h(y, a, b, label, ly):
    return f'<g class="d"><path d="M{a} {y}H{b}M{a} {y-5}V{y+5}M{b} {y-5}V{y+5}"/><path class="ar" d="M{a} {y}l8 -3v6zM{b} {y}l-8 -3v6z"/><text x="{(a+b)//2}" y="{ly}" text-anchor="middle">{label}</text></g>'
def dim_v(x, a, b, label, lx):
    return f'<g class="d"><path d="M{x} {a}V{b}M{x-5} {a}H{x+5}M{x-5} {b}H{x+5}"/><path class="ar" d="M{x} {a}l-3 8h6zM{x} {b}l-3 -8h6z"/><text x="{lx}" y="{(a+b)//2+4}" text-anchor="end">{label}</text></g>'
def call(x1, y1, x2, y2, x3, label, anchor='start'):
    return f'<g class="c"><path d="M{x1} {y1}L{x2} {y2}H{x3}"/><circle cx="{x1}" cy="{y1}" r="2.5"/><text x="{min(x2,x3) if anchor=="start" else max(x2,x3)}" y="{y2-5}" text-anchor="{anchor}">{label}</text></g>'
def flat(pre='', cls='ds-hero-art__bp', extra=''):
    return f'''<svg class="{cls}" viewBox="0 0 {VW} {VH}" aria-hidden="true" focusable="false"{extra}>
  <defs>
    <pattern id="{pre}hg-minor" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M20 0H0V20" fill="none" stroke="{T}" stroke-width=".5" opacity=".28"/></pattern>
    <pattern id="{pre}hg-major" width="100" height="100" patternUnits="userSpaceOnUse"><path d="M100 0H0V100" fill="none" stroke="{T}" stroke-width=".75" opacity=".5"/></pattern>
    <pattern id="{pre}hg-hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><path d="M0 0V6" stroke="{G}" stroke-width=".9"/></pattern>
  </defs>
  <rect width="{VW}" height="{VH}" fill="url(#{pre}hg-minor)"/><rect width="{VW}" height="{VH}" fill="url(#{pre}hg-major)"/>
  <g class="g" fill="none"><path d="M{X0} 12V340M{X1} 12V340" stroke-dasharray="2 4"/><path d="M12 {CY}H688" stroke-dasharray="2 4"/><path d="M{ON} 96V340M{OFF} 96V340" stroke-dasharray="6 3 1 3"/></g>
  <text class="code" x="{X0}" y="30">.form-switch-item input[role="switch"] {{</text>
  <text class="code" x="{X0+12}" y="46">width: 48px; height: 24px; border-radius: 999px;</text>
  <text class="code" x="{X0}" y="62">}}</text>
  <rect x="{X0}" y="{Y0}" width="{W}" height="{H}" rx="{H//2}" fill="url(#{pre}hg-hatch)" stroke="{P}" stroke-width="1.25"/>
  <circle class="ghost" cx="{OFF}" cy="{CY}" r="{TR}" fill="none" stroke-dasharray="4 4"/>
  <circle cx="{ON}" cy="{CY}" r="{TR}" fill="var(--color-background-primary)" stroke="{P}" stroke-width="1.25"/>
  <circle cx="{ON}" cy="{CY}" r="2.5" fill="{P}"/>
  {dim_h(Y0-34, X0, X1, '48', Y0-42)}
  {dim_v(X0-28, Y0, Y0+H, '24', X0-36)}
  {dim_h(CY+TR+30, ON-TR, ON+TR, '20', CY+TR+46)}
  {dim_h(CY+TR+70, OFF, ON, '24 travel', CY+TR+86)}
  <g class="d"><path d="M{ON+TR} {CY}H{X1}"/><text x="{X1+14}" y="{CY+4}">2</text></g>
  {call(X1-24, Y0+22, X1+40, Y0+2, 686, 'surface-success-default')}
  {call(ON+35, CY+35, ON+80, CY+66, 686, 'surface-raised-primary')}
</svg>'''


if __name__ == '__main__':
    print(flat())
