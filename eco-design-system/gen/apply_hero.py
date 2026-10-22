#!/usr/bin/env python3
"""Put a generated header-art scene into a component page (first page only). python3 gen/apply_hero.py components/<page>.html /tmp/scene.svg
Idempotent: replaces an existing scene. Adds the doc-hero/hairline-card css links and the kernel/embed scripts when missing."""
import re, sys
page, svg = sys.argv[1], open(sys.argv[2]).read()
s = open(page).read()
for href in ('../doc-hero.css', '../../hairline/hairline-card.css'):
    if href not in s: s = s.replace('</head>', f'  <link rel="stylesheet" href="{href}">\n</head>', 1)
for src in ('../../hairline/kernel.js', '../../hairline/embed.js'):
    if src not in s: s = s.replace('<script src="../doc-kit.js"></script>', f'<script src="{src}"></script>\n<script src="../doc-kit.js"></script>', 1)
if 'ds-hero-split--scene' in s:
    s = re.sub(r'(<div class="ds-hero-scene" aria-hidden="true">).*?(</div><div class="ds-hero-split__text">)', lambda m: m.group(1) + svg + m.group(2), s, count=1, flags=re.S)
else:
    a = s.index('<section class="ds-section ds-section--first">'); b = s.index('</section>', a)
    h = s[a:b]
    h = h.replace('<div class="ds-page ds-inner">', f'<div class="ds-page ds-inner"><div class="ds-hero-split ds-hero-split--scene"><div class="ds-hero-scene" aria-hidden="true">{svg}</div><div class="ds-hero-split__text">', 1)
    h = h.rstrip()
    assert h.endswith('</div>'); h = h + '</div>\n'
    s = s[:a] + h + s[b:]
open(page, 'w').write(s)
