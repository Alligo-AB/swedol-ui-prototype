"""The Breadcrumb hub (components/breadcrumb.html): one page, no tab bar, like the Badge, Links guide and Notifications hubs.
It chooses between the two parts. Each has its own three-page set (gen_breadcrumb_base.py, gen_breadcrumb_bar.py)."""
import os
import sys
import build
from bc import *

SLUG = 'breadcrumb'

overview = '<h2 class="ds-h2">Overview</h2>' + desc('A breadcrumb shows <strong>where the page sits</strong> in the site and lets the user go back up in one click. It is made of two parts: the <strong>Breadcrumb Base</strong>, one level in a bordered box, and the <strong>Breadcrumb Bar</strong>, the row of crumbs with a slash between them. The base is a component; the bar is a <strong>pattern</strong>, because it is composed of several crumbs and the page spacing, so it is documented under Patterns.') + \
    '<h3 class="ds-h3 ds-group">When to use a breadcrumb</h3>' + desc('Use it when the page sits more than one step down the navigation tree, so the user can go up a level without the browser’s back button:') + \
    bullets(['Category, product list, product and landing pages', 'Pages in My Pages that sit below another page']) + \
    '<h3 class="ds-h3 ds-group">When not to use it</h3>' + bullets(['The home page, or a page directly under Home with no level in between', 'Tabs or a clear back link already lead the user up a level: avoid two ways to do the same thing']) + \
    '<h3 class="ds-h3 ds-group">How this guide is organized</h3>' + desc('This page chooses the part and shows them together. Each part has its own three pages: Examples &amp; Guidelines, Specifications and Code. Open one from the table below or from the navigation.')

choose = '<h2 class="ds-h2">Which part</h2>' + desc('A page almost always uses the bar. The base is the piece the bar is built from.') + \
    '<div class="ds-table-wrap"><table class="ds-table pg-type"><thead><tr><th scope="col">Part</th><th scope="col">What it is, and what to use it for</th></tr></thead><tbody>' + \
    '<tr><th scope="row">' + link_large('breadcrumb-bar.html', 'Breadcrumb Bar') + ' (pattern)</th><td><p style="margin:0 0 12px">A row of two to six crumbs with a “/” between them, and the page spacing. Use it for the trail at the top of a page.</p><div id="ch-bar"></div></td></tr>' + \
    '<tr><th scope="row">' + link_large('breadcrumb-base.html', 'Breadcrumb Base') + ' (component)</th><td><p style="margin:0 0 12px">One level: a bordered box with a label, in three states. Use it to build a bar in a custom layout.</p><div id="ch-base"></div></td></tr>' + \
    '</tbody></table></div>'

context = '<h2 class="ds-h2">In context</h2>' + desc('The bar sits directly under the header, as the first element of the page, before the title.') + \
    fig_one('<div class="pg-col" style="gap:0;align-items:stretch"><div id="ctx-bar"></div><p class="pg-title" style="margin:0 0 8px;font-size:32px;line-height:36px;text-transform:uppercase;font-weight:600;font-family:\'Breuer Condensed\',Arial,sans-serif">Carpenter pants</p><p class="pg-note" style="margin:0">The block after the bar has no top padding of its own.</p></div>', None, '', 'ds-fig__stage--bar')

behavior = '<h2 class="ds-h2">Behavior</h2>' + desc('The bar and the crumbs follow one interaction model.') + \
    table(['Topic', 'Result'], [['Links', 'Every crumb but the last is a link. The last is the current page and is not clickable.'], ['Hover', 'The text turns to the action color and is underlined. The border does not change.'], ['Keyboard', 'Tab moves through the parent crumbs. Enter follows a link.'], ['Wrapping', 'A trail that is too long wraps to the next row. A crumb never wraps its label.'], ['Breakpoint', 'Sizes change at 769px. A tablet looks like mobile.']])

usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When not to use</h3><h3 class="ds-h3">Use the bar, not loose crumbs</h3>' + desc('A trail is built with the bar, so the separators, the spacing and the landmark are right. A single crumb on its own does not show where the user is.') + \
    fig_pair('<div id="fig-do"></div>', 'Do use the bar for a trail.', '<div id="fig-dont"></div>', 'Do not show one crumb as the whole navigation.') + \
    rules(['Put the bar first in the page, under the header.', 'Make every crumb but the last a real link.', 'Use the page names as the labels, kept short.', 'Use the page margin <code>var(--px-page)</code> for the side padding.'],
          ['Underline the crumbs in the enabled state.', 'Use chevrons or icons between the crumbs.', 'Make the current page a link.', 'Show a bar on the home page.'])

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('breadcrumb-bar.html', 'Breadcrumb Bar') + '</strong>. The whole trail.</li><li><strong>' + link_large('breadcrumb-base.html', 'Breadcrumb Base') + '</strong>. One level of the trail.</li><li><strong>' + link_large('tabs.html', 'Tabs') + '</strong>. Sub-navigation in the same context.</li><li><strong>' + link_large('links-guide.html', 'Links guide') + '</strong>. Other links in a page.</li><li><strong>' + link_large('section.html', 'Section') + '</strong>. The block after the bar zeroes its top padding.</li></ul>'

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.w3.org/WAI/ARIA/apg/patterns/breadcrumb/', 'WAI-ARIA Authoring Practices: Breadcrumb pattern', 'The landmark, the list of links and aria-current.'),
    ('https://www.w3.org/WAI/WCAG22/Understanding/location.html', 'WCAG 2.2: Location', 'Success criterion 2.4.8: show where the user is.'),
    ('https://www.nngroup.com/articles/breadcrumbs/', 'Nielsen Norman Group: Breadcrumbs', 'Guidelines for location breadcrumbs.'),
    ('https://fluent2.microsoft.design/components/web/react/core/breadcrumb/usage', 'Fluent 2: Breadcrumb', 'Microsoft.'),
    ('https://carbondesignsystem.com/components/breadcrumb/usage/', 'Carbon Design System: Breadcrumb', 'IBM.')])

secs = [('overview', overview), ('which-part', choose), ('in-context', context), ('behavior', behavior), ('usage', usage), ('related', related), ('references', references)]

JS = JS_BUILD + r'''
  function put(sel, node) { clear($(sel)).appendChild(node); }
  put('#ch-bar', bar(3, 'Work pants')); put('#ch-base', crumb('Work pants', 'enabled'));
  put('#ctx-bar', bar(3, 'Work pants'));
  put('#fig-do', bar(3, 'Work pants')); put('#fig-dont', crumb('Work pants', 'enabled'));
'''

STYLE_HUB = STYLE + '\n    .pg-type td { vertical-align: middle; padding-top: 16px; padding-bottom: 16px; }'

C = dict(slug=SLUG, title='Breadcrumb', eyebrow='Components · Status and navigation', css=['breadcrumb'], style=STYLE_HUB, select_menu=False,
    lead='ECO has two breadcrumb parts: the <strong>base</strong>, one crumb (a component), and the <strong>bar</strong>, a row of crumbs (a pattern built from it). Read this guide before you build a trail.',
    lead_ex='Choose the part below, then open the page for it: ' + ', '.join(link_large(h, n).replace(' inline-link--secondary', '').replace('inline-link--large', 'inline-link--xlarge') for h, n in [('breadcrumb-bar.html', 'Breadcrumb Bar'), ('breadcrumb-base.html', 'Breadcrumb Base')]) + '. Every example is the real component. Figma: ' + fig_link(FIGMA_BAR, 'Bar') + ', ' + fig_link(FIGMA_BASE, 'Base') + ' and ' + fig_link(FIGMA_RESP, 'responsive behavior') + '.',
    lead_spec='', lead_code='', ex=secs, spec=[], code=[])


def hub():
    c = C
    tail = '<script src="../doc-kit.js"></script>\n<script>\n(function () {\n  var $ = DK.$, $$ = DK.$$, clear = DK.clear, esc = DK.esc;\n%s\n})();\n</script>\n<script src="../tailwind-note.js"></script>\n<script src="../toc.js"></script>\n<script src="../subnav.js"></script>\n' % JS
    return '%s\n<body data-ds="component">\n<script src="../docnav.js"></script>\n%s\n\n%s\n\n<div class="ds-doc" data-subnav="tabs">\n%s\n</div>\n\n%s</body>\n</html>\n' % (
        build.head(c, 'ex'), build.crumbs(c, 'ex'), build.intro(c, 'ex') + '\n' + build.SEP, build.sections(secs), tail)   # a hub has no tab bar, so the divider after the white header is added here (rule in eco-doc-page)


if __name__ == '__main__':
    p = os.path.join(build.OUT, 'breadcrumb.html')
    if os.path.exists(p) and '--force' not in sys.argv:
        print('exists, skipped (use --force to overwrite):', p)
    else:
        open(p, 'w').write(hub()); print('wrote', p)
