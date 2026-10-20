#!/usr/bin/env python3
"""Builds components/switch-header-versions.html: a copy of switch.html whose header is shown three times, as three header-art layouts to compare
(v1 flat drawing beside the figure, v2 isometric drawing over the figure, v3 drawing as background). Reads the text of the current switch.html header.
Run from anywhere: python3 eco-design-system/gen/build_switch_header_versions.py (needs hero_switch.py, hero_switch_iso.py in this folder)."""
import os, re, sys
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
import hero_switch
import subprocess
comp = os.path.join(here, '..', 'components')
src = open(os.path.join(comp, 'switch.html')).read()
text = open(os.path.join(here, 'switch_header_text.html')).read()  # the header text (eyebrow, h1, leads); switch.html itself now carries v2b, so it is read from this file
iso = subprocess.check_output([sys.executable, os.path.join(here, 'hero_switch_iso.py')]).decode().strip()
fig = '<div data-hairline-card="switch" data-src="../../hairline/switch.js"></div>'
def head(t, first): return t if first else t.replace('<h1 class="ds-title">', '<p class="ds-title">').replace('</h1>', '</p>')
def sec(label, body, first):
    return f'<section class="ds-section ds-section--first{"" if first else " pg-vsec"}"><div class="ds-page ds-inner"><p class="pg-vlabel">{label}</p>{body}</div></section>'
v1 = sec('Version 1 · flat drawing beside the figure (this is the current switch.html header)',
    f'<div class="ds-hero-split"><div class="ds-hero-split__text">{text}</div><div class="ds-hero-art" aria-hidden="true">{fig}{hero_switch.flat("v1-")}</div></div>', True)
v2 = sec('Version 2 · isometric drawing, same camera, lies over the figure and takes over where it fades',
    f'<div class="ds-hero-split"><div class="ds-hero-split__text">{head(text, False)}</div><div class="ds-hero-art ds-hero-art--iso" aria-hidden="true">{fig}{iso}</div></div>', False)
bg3 = hero_switch.flat('v3-', 'ds-hero-art__bp', ' preserveAspectRatio="xMaxYMid meet"')
v3 = sec('Version 3 · the drawing is a faint background element behind the header, the figure in front',
    f'<div class="ds-hero-split ds-hero-split--bg"><div class="ds-hero-bg" aria-hidden="true">{bg3}</div><div class="ds-hero-split__text">{head(text, False)}</div><div class="ds-hero-art" aria-hidden="true">{fig}</div></div>', False)
scene = subprocess.check_output([sys.executable, os.path.join(here, 'hero_switch_iso.py'), 'scene']).decode().strip()
v2b = sec('Version 2b · version 2 as one background scene: the isometric drawing and the figure (a static picture) sit behind the header text and stay on smaller screens',
    f'<div class="ds-hero-split ds-hero-split--scene"><div class="ds-hero-scene" aria-hidden="true">{scene}</div><div class="ds-hero-split__text">{head(text, False)}</div></div>', False)
sep = '<div class="ds-sep"><hr class="divider" /></div>'
m = re.search(r'<section class="ds-section ds-section--first">.*?</section>', src, re.S)
page = src[:m.start()] + v1 + '\n' + sep + '\n' + v2 + '\n' + sep + '\n' + v2b + '\n' + sep + '\n' + v3 + src[m.end():]
page = page.replace('<title>Switch – ECO Design System</title>', '<title>Switch header art, three versions – ECO Design System</title>')
page = page.replace('<style>\n', '<style>\n    .pg-vlabel { font-size: 14px; line-height: 20px; letter-spacing: 0.56px; font-weight: 600; text-transform: uppercase; color: var(--color-text-tertiary); margin-bottom: var(--dimension-spacing-space-16); }\n    .ds-section.pg-vsec { padding-top: var(--dimension-spacing-space-48); }\n', 1)
open(os.path.join(comp, 'switch-header-versions.html'), 'w').write(page)
print('wrote components/switch-header-versions.html')
