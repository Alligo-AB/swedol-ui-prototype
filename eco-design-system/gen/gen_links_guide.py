"""The Links guide hub (components/links-guide.html): one page, no tab bar, like the Badge and Notifications hubs. It chooses between the three link types.
Each type has its own three-page set (gen_inline_link.py, gen_action_link.py, gen_tile_link.py)."""
import os
import sys
import build
from build import *

FIGMA = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=1221-33213'
SLUG = 'links-guide'

STYLE = r'''    .pg-note { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .pg-row { display: flex; flex-wrap: wrap; align-items: center; gap: 16px 24px; }
    .pg-col { display: flex; flex-direction: column; align-items: flex-start; gap: 24px; width: 100%; }
    .pg-p { margin: 0; color: var(--color-text-primary); max-width: 560px; }
    .pg-cell { display: flex; flex-direction: column; align-items: flex-start; gap: 8px; }
    .pg-type td { vertical-align: middle; padding-top: 16px; padding-bottom: 16px; }'''

IL = '<a href="#" class="inline-link inline-link--medium" data-prevent>%s</a>'
AL = '<a href="#" class="action-link action-link--medium" data-prevent><span class="action-link__label">%s</span><span class="action-link__icon" aria-hidden="true">chevron_right</span></a>'
TL = '<a href="#" class="tile-link tile-link--large tile-link--vertical tile-link--white" data-prevent><div class="tile-link__inner"><span class="tile-link__icon" aria-hidden="true">%s</span><span class="tile-link__label">%s</span></div></a>'


def inl(href, text):
    return '<a href="%s" class="inline-link inline-link--small">%s</a>' % (href, text)


overview = '<h2 class="ds-h2">Overview</h2>' + desc('Links take users somewhere: to another page, to another site, to a section of the same page, or to a resource such as a PDF, an email address or a phone number. They are the lightest interactive element in the ECO Design System. Where a Button performs an action, <strong>a link always navigates</strong>.') + \
    desc('The system has three link components: <strong>Inline link</strong>, <strong>Action link</strong> and <strong>Tile link</strong>. They share the same foundation (semantics, keyboard behavior and state logic) and serve different contexts. Choosing the right one comes down to where the link lives and how much visual weight it needs. Read this guide before you build a link.') + \
    '<h3 class="ds-h3 ds-group">When to use a link</h3>' + desc('Use a link when the user should:') + \
    bullets(['Go to another page in the site or the application', 'Go to an external site', 'Jump to an element on the same page', 'Open a resource, such as a PDF, an email (<code>mailto:</code>) or a phone number (<code>tel:</code>)']) + \
    desc('A link navigates; a button acts. For an action in the page (save, send, open a modal) use <code>eco-button</code>.') + \
    '<h3 class="ds-h3 ds-group">Modifiers</h3>' + desc('Every type has a <strong>weight</strong> (Regular by default, Medium and Bold). The Inline link and the Tile link also have an <strong>italic</strong> style, so a link can follow the text around it; the Action link is never italic. The Inline link also has a <strong>reverse underline</strong> (underline on hover only).') + \
    '<h3 class="ds-h3 ds-group">How this guide is organized</h3>' + desc('This page chooses the type and shows them together. Each type has its own three pages: Examples &amp; Guidelines, Specifications and Code. Open one from the table below or from the navigation.')

choose = '<h2 class="ds-h2">Which link type</h2>' + desc('Choose the type by where the link sits first, and by how prominent it must be second.') + \
    '<div class="ds-table-wrap"><table class="ds-table pg-type"><thead><tr><th scope="col">Type</th><th scope="col">Where</th><th scope="col">Underline</th><th scope="col">Icons</th><th scope="col">Example</th></tr></thead><tbody>' + \
    '<tr><th scope="row">' + inl('inline-link.html', 'Inline link') + '</th><td>Inside a sentence or text block</td><td>On when enabled, off on hover</td><td>Never</td><td>Read more on the ' + IL % 'product page' + '.</td></tr>' + \
    '<tr><th scope="row">' + inl('action-link.html', 'Action link') + '</th><td>Standalone, not in body text</td><td>Off when enabled, on on hover</td><td>Leading and/or trailing</td><td>' + AL % 'View all products' + '</td></tr>' + \
    '<tr><th scope="row">' + inl('tile-link.html', 'Tile link') + '</th><td>Graphical and prominent, like a card or button</td><td>None</td><td>With or without</td><td>' + TL % ('checkroom', 'Work wear') + '</td></tr>' + \
    '</tbody></table></div>' + \
    '<h3 class="ds-h3 ds-group">Which one</h3>' + desc('Ask in this order and take the first yes.') + \
    '<ol class="ds-bullets ds-bullets--num">' + ''.join('<li><strong>%s</strong> %s</li>' % x for x in [
        ('Does the element perform an action instead of navigating?', 'Not a link: use <code>eco-button</code>.'), ('Does the link sit inside a sentence, a paragraph or other text?', 'Inline link.'), ('Is it a graphic, prominent surface in a grid or a scroller of peers (a brand, a category, a shortcut)?', 'Tile link.'), ('Does it stand on its own, with an icon?', 'Action link.')]) + '</ol>'

context = '<h2 class="ds-h2">In context</h2>' + desc('The three types together, as they would be used on a page.') + \
    fig_one('<div class="pg-col"><p class="pg-p" style="font-size:17px;line-height:24px">Read more about our work wear on the ' + IL % 'product page' + '.</p>' + AL % 'View all products' + '<div class="pg-row">' + TL % ('checkroom', 'Work wear') + TL % ('construction', 'Tools') + '</div></div>')

behavior = '<h2 class="ds-h2">Behavior</h2>' + desc('All three link types share one interaction model: the <strong>entire element is the click target</strong>, Tab moves focus and Enter activates.') + \
    table(['Topic', 'Result'], [['Mouse', 'Click anywhere on the link: the text, an icon or the whole tile.'], ['Keyboard', 'Tab moves focus and shows the focus ring. Enter activates the link.'], ['Markup', 'A real <code>&lt;a href&gt;</code> in every case. Links navigate; buttons act.'], ['Motion', 'Color changes over <code>duration-fast-3</code> with <code>ease-standard</code>.'],
        ['Sizing', 'Sizes follow the type scale. A link inside content matches the size of the text around it (Inline link, Large, Medium or Small). A standalone link matches the default body copy size of the page.']])

usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When not to use</h3><h3 class="ds-h3">Name the destination</h3>' + desc('The link text says where the link goes, for every type. A vague text does not help the user, and a screen reader reads links out of context.') + \
    fig_pair('<div class="pg-col" style="gap:16px">' + AL % 'View all products' + '</div>', 'Do name the destination in the link text.', '<div class="pg-col" style="gap:16px">' + AL % 'Click here' + '</div>', 'Do not write “click here” as the link text.') + \
    '<h3 class="ds-h3">One type per group</h3>' + desc('Links that sit together are the same type, so the group reads as one set.') + \
    fig_pair('<div class="pg-row">' + TL % ('checkroom', 'Work wear') + TL % ('construction', 'Tools') + '</div>', 'Do use one type for a group of links.', '<div class="pg-col" style="gap:16px">' + TL % ('checkroom', 'Work wear') + AL % 'Tools' + '</div>', 'Do not mix link types in one group.') + \
    '<h3 class="ds-h3">For an action that does not navigate</h3>' + desc('A link goes somewhere. For an action in the page use <code>eco-button</code>.') + \
    rules(['Choose the type by placement first, prominence second.', 'Name the destination in the link text.', 'Use one type per group of links.', 'Use <code>eco-button</code> for actions that do not navigate.'],
          ['Use an inline link outside a sentence.', 'Add an icon to an inline link.', 'Use a tile link for ordinary text navigation.', 'Write “click here” as the link text.'])

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('inline-link.html', 'Inline link') + '</strong>. A link inside a sentence.</li><li><strong>' + link_large('action-link.html', 'Action link') + '</strong>. A standalone link with an optional icon.</li><li><strong>' + link_large('tile-link.html', 'Tile link') + '</strong>. A graphical, prominent link.</li><li><strong>' + link_large('button.html', 'Button') + '</strong>. For an action that does not navigate.</li><li><strong>' + link_large('breadcrumb.html', 'Breadcrumb') + '</strong>. Links that show where the page is in the site.</li></ul>'

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context.html', 'WCAG 2.2: Link Purpose (In Context)', 'Success criterion 2.4.4.'),
    ('https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html', 'WCAG 2.2: Use of Color', 'Success criterion 1.4.1.'),
    ('https://www.nngroup.com/articles/guidelines-for-visualizing-links/', 'Nielsen Norman Group: Guidelines for Visualizing Links', 'How links should look and behave.'),
    ('https://fluent2.microsoft.design/components/web/react/core/link/usage', 'Fluent 2: Link', 'Microsoft.'),
    ('https://carbondesignsystem.com/components/link/usage/', 'Carbon Design System: Link', 'IBM.')])

secs = [('overview', overview), ('which-link-type', choose), ('in-context', context), ('behavior', behavior), ('usage', usage), ('related', related), ('references', references)]

JS = r'''
  $$('[data-prevent]').forEach(function (a) { a.addEventListener('click', function (e) { e.preventDefault(); }); });
'''

C = dict(slug=SLUG, title='Links guide', eyebrow='Components · Links',
    css=['inline-link', 'action-link', 'tile-link'], style=STYLE, select_menu=False,
    lead='ECO has three link types: <strong>inline link</strong>, <strong>action link</strong> and <strong>tile link</strong>. Read this guide before you build a link.',
    lead_ex='Choose the type below, then open the page for it: ' + ', '.join(link_large(h, n).replace(' inline-link--secondary', '').replace('inline-link--large', 'inline-link--xlarge') for h, n in [('inline-link.html', 'Inline link'), ('action-link.html', 'Action link'), ('tile-link.html', 'Tile link')]) + '. Every example is the real component. Specification: <code>.claude/skills/links-guide/SKILL.md</code>. Figma: ' + fig_link(FIGMA, 'Links usage guidelines') + '.',
    lead_spec='', lead_code='', ex=secs, spec=[], code=[])


def hub():
    c = C
    tail = '<script src="../doc-kit.js"></script>\n<script>\n(function () {\n  var $ = DK.$, $$ = DK.$$, clear = DK.clear, esc = DK.esc;\n%s\n})();\n</script>\n<script src="../tailwind-note.js"></script>\n<script src="../toc.js"></script>\n<script src="../subnav.js"></script>\n' % JS
    return '%s\n<body data-ds="component">\n<script src="../docnav.js"></script>\n%s\n\n%s\n\n<div class="ds-doc" data-subnav="tabs">\n%s\n</div>\n\n%s</body>\n</html>\n' % (
        build.head(c, 'ex'), build.crumbs(c, 'ex'), build.intro(c, 'ex'), build.sections(secs), tail)


if __name__ == '__main__':
    p = os.path.join(build.OUT, 'links-guide.html')
    if os.path.exists(p) and '--force' not in sys.argv:
        print('exists, skipped (use --force to overwrite):', p)
    else:
        open(p, 'w').write(hub()); print('wrote', p)
