"""Frame for the three-page component docs (reference: tooltip.html / tooltip-specifications.html / tooltip-code.html).
Usage: from build import emit; emit(dict(...)). Writes <slug>.html, <slug>-specifications.html, <slug>-code.html into eco-design-system/components/."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, '..', 'components'))
BASE_CSS = ['badge', 'divider', 'input', 'button-group', 'button', 'select', 'tabs']
SEP = '<div class="ds-sep"><hr class="divider" /></div>'


def esc_attr(s):
    return s.replace('&', '&amp;').replace('"', '&quot;')


def section(sid, html, prose=True):
    cls = 'ds-page ds-inner' + (' ds-prose' if prose else '')
    return '<section class="ds-section" id="%s"><div class="%s">%s</div></section>' % (sid, cls, html)


def sections(items):
    out = []
    for it in items:
        sid, html = it[0], it[1]
        prose = it[2] if len(it) > 2 else True
        out.append(section(sid, html, prose))
    return ('\n' + SEP + '\n').join(out)


def head(c, kind):
    names = {'ex': '', 'spec': ': Specifications', 'code': ': Code', 'sb': ': Storyblok'}
    css = list(c.get('css_before', [])) + list(BASE_CSS)   # css_before: component files whose rules the base files must override (textarea.css repeats .form-label)
    for n in c.get('css', []):
        if n not in css:
            css.append(n)
    if kind == 'spec':
        css.append('measure')
    links = '\n'.join('  <link rel="stylesheet" href="../../components/css/%s.css">' % n for n in css)
    links = (c.get('head_extra', '') + '\n' if kind == 'ex' and c.get('head_extra') else '') + links   # extra links go BEFORE the component CSS, so the component files win (notifications.css has its own .btn base)
    pre = ''
    if kind in c.get('pre_css_kinds', ('ex', 'spec')):   # pre_css: component files that must load BEFORE docs.css, so that docs.css's imports (button.css, inline-link.css) win over their own .btn / .inline-link base (notifications.css)
        pre = ''.join('  <link rel="stylesheet" href="%s">\n' % h for h in c.get('pre_css', []))
    extra_js = ''
    for j in c.get('head_js', []):
        extra_js += '\n  <script src="%s"%s></script>' % (j, ' defer' if 'measure' in j else '')
    if kind == 'spec':
        extra_js += '\n  <script src="../../components/js/measure.js" defer></script>'
    local = c.get('style', '')
    local = ('\n  <style>\n    /* page-local: layout and state forcing for the demo only; no component or token values */\n%s\n  </style>' % local) if local.strip() else ''
    return '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>%s%s – ECO Design System</title>
  <link rel="stylesheet" href="https://unpkg.com/alligo-design-tokens@latest/dist/css/fonts.css">
  <link rel="stylesheet" href="https://unpkg.com/alligo-design-tokens@latest/dist/css/index.css">
%s  <link rel="stylesheet" href="../docs.css">
  <link rel="stylesheet" href="../docnav.css">
%s
  <script src="../../components/js/tabs.js"></script>%s%s
</head>''' % (c['title'], names[kind], pre, links, extra_js, local)


def crumbs(c, kind):
    b = '<a href="../../index.html" class="breadcrumb-item">Home</a><span class="breadcrumb-sep">/</span><a href="../overview.html" class="breadcrumb-item">ECO Design System</a><span class="breadcrumb-sep">/</span><a href="../components-overview.html" class="breadcrumb-item">Components</a><span class="breadcrumb-sep">/</span>'
    if c.get('parent'):   # a type of a hub (Badge, Notifications): Components / Notifications / Toast
        b += '<a href="%s" class="breadcrumb-item">%s</a><span class="breadcrumb-sep">/</span>' % c['parent']
    if kind == 'ex':
        b += '<span class="breadcrumb-item breadcrumb-item--active" aria-current="page">%s</span>' % c['title']
    else:
        b += '<a href="%s.html" class="breadcrumb-item">%s</a><span class="breadcrumb-sep">/</span><span class="breadcrumb-item breadcrumb-item--active" aria-current="page">%s</span>' % (c['slug'], c['title'], {'spec': 'Specifications', 'code': 'Code', 'sb': 'Storyblok'}[kind])
    return '<div class="ds-page">\n  <nav class="breadcrumb" aria-label="Breadcrumbs">\n    <div class="breadcrumb__bar">%s</div>\n  </nav>\n</div>' % b


def tabs(c, kind):
    def t(href, label, cur):
        return '<a class="tab"%s href="%s"><span class="tab__label">%s</span></a>' % (' aria-current="page"' if cur else '', href, label)
    s = c['slug']
    return '<div class="ds-tabs"><nav class="tab-bar tab-bar--primary" aria-label="%s">%s%s%s</nav></div>' % (
        c['title'], t(s + '.html', 'Examples &amp; Guidelines', kind == 'ex'), t(s + '-specifications.html', 'Specifications', kind == 'spec'), t(s + '-code.html', 'Code', kind == 'code') + (t(s + '-storyblok.html', 'Storyblok', kind == 'sb') if c.get('sb') else ''))


def intro(c, kind):
    second = {'ex': c['lead_ex'], 'spec': c['lead_spec'], 'code': c['lead_code'], 'sb': c.get('lead_sb', '')}[kind]
    return '''<section class="ds-section ds-section--first">
  <div class="ds-page ds-inner">
    <div class="ds-eyebrow-row"><span class="ds-eyebrow">%s</span>%s</div>
    <h1 class="ds-title">%s</h1>
    <p class="ds-lead">%s</p><p class="ds-lead">%s</p></div>
</section>''' % (c.get('eyebrow', 'Components · Form'), c.get('eyebrow_extra', ''), c['title'], c['lead'], second)


def page(c, kind):
    secs = {'ex': c['ex'], 'spec': c['spec'], 'code': c['code'], 'sb': c.get('sb', [])}[kind]
    script = {'ex': c.get('js_ex', ''), 'spec': c.get('js_spec', ''), 'code': c.get('js_code', ''), 'sb': c.get('js_sb', '')}[kind]
    tail = '<script src="../doc-kit.js"></script>\n'
    if c.get('select_menu', True):
        tail += '<script src="../../components/js/select-menu.js"></script>\n'
    for j in c.get('body_js', []):
        tail += '<script src="%s"></script>\n' % j
    if script.strip():
        tail += '<script>\n(function () {\n  var $ = DK.$, $$ = DK.$$, clear = DK.clear, esc = DK.esc;\n%s\n})();\n</script>\n' % script
    if kind == 'code':
        tail += '<script src="../tailwind-note.js"></script>\n'
    tail += '<script src="../toc.js"></script>\n<script src="../subnav.js"></script>\n'
    if c.get('tooltip', False):
        tail += '<script src="../../components/js/tooltip.js"></script>\n'
    return '%s\n<body data-ds="component">\n<script src="../docnav.js"></script>\n%s\n\n%s\n%s\n\n<div class="ds-doc" data-subnav="tabs">\n%s\n</div>\n\n%s</body>\n</html>\n' % (
        head(c, kind), crumbs(c, kind), intro(c, kind), tabs(c, kind), sections(secs), tail)


def emit(c):
    for kind, suffix in (('ex', ''), ('spec', '-specifications'), ('code', '-code')) + ((('sb', '-storyblok'),) if c.get('sb') else ()):
        p = os.path.join(OUT, c['slug'] + suffix + '.html')
        if os.path.exists(p) and '--force' not in sys.argv:   # the pages are the real files: never overwrite a hand-edited page by accident
            print('exists, skipped (use --force to overwrite):', p)
            continue
        with open(p, 'w') as f:
            f.write(page(c, kind))
        print('wrote', p)


# ---- shared snippets -------------------------------------------------------------------
def btn_group(label_id, label, attr, buttons, extra=''):
    """buttons: [(value, text, pressed)]"""
    b = ''.join('<button type="button" data-v="%s" aria-pressed="%s">%s</button>' % (v, 'true' if p else 'false', t) for v, t, p in buttons)
    return '<div class="ds-field"><span class="form-label form-label--sm" id="%s">%s</span><div class="btn-group" role="group" aria-labelledby="%s" %s%s>%s</div></div>' % (label_id, label, label_id, attr, extra, b)


BP_BUTTONS = [('auto', 'Window', True), ('desktop', 'Desktop', False), ('mobile', 'Mobile', False)]


def bp_field(pid):
    return btn_group(pid, 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')


def toolbar(items):
    """items: [(label_id, label, attr, buttons, extra)]  -> ds-toolbar"""
    out = '<div class="ds-toolbar">'
    for lid, lab, attr, btns, *ex in items:
        b = ''.join('<button type="button" data-v="%s" aria-pressed="%s">%s</button>' % (v, 'true' if p else 'false', t) for v, t, p in btns)
        out += '<span class="ds-toolbar__label" id="%s">%s</span><div class="btn-group" role="group" aria-labelledby="%s" %s%s>%s</div>' % (lid, lab, lid, attr, ex[0] if ex else '', b)
    return out + '</div>'


def code_box(id_, title, pre_id=None):
    return '<div class="ds-code"><div class="ds-code__bar"><span>%s</span><button type="button" class="mo-copy" data-copy="%s" aria-label="Copy"><span class="mo-ic" aria-hidden="true">content_copy</span></button></div><pre id="%s"></pre></div>' % (title, id_, id_)


def table(head_cols, rows, cls='ds-table', id_=None):
    h = ''.join('<th scope="col">%s</th>' % x for x in head_cols)
    body = ''
    for r in rows:
        cells = ''
        for i, x in enumerate(r):
            if i == 0:
                cells += '<th scope="row">%s</th>' % x
            else:
                cells += '<td>%s</td>' % x if not x.startswith('<td') else x
        body += '<tr>%s</tr>' % cells
    return '<div class="ds-table-wrap"><table class="%s"%s><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (cls, (' id="%s"' % id_) if id_ else '', h, body)


def rules(do, dont):
    li = lambda L: ''.join('<li>%s</li>' % x for x in L)
    return '<div class="ds-rules"><div class="ds-rule ds-rule--do"><h3 class="ds-rule__title">Do</h3><ul>%s</ul></div><div class="ds-rule ds-rule--dont"><h3 class="ds-rule__title">Don’t</h3><ul>%s</ul></div></div>' % (li(do), li(dont))


def link_large(href, text, ext=False):
    return '<a class="inline-link inline-link--large inline-link--secondary" href="%s"%s>%s</a>' % (href, ' target="_blank" rel="noopener"' if ext else '', text)


def refs(items):
    """items: [(url, name, note)]"""
    return '<ul class="ds-bullets">' + ''.join('<li>%s. %s</li>' % (link_large(u, n, True), note) for u, n, note in items) + '</ul>'


# ---- more helpers ---------------------------------------------------------------------
OLD = os.path.join(HERE, 'old-source') + '/'


def old_js(name, start, end):
    """Slice of the old page's script: from the line containing `start` up to (not including) the line containing `end`."""
    src = open(OLD + name + '.html').read()
    a = src.index(start)
    b = src.index(end, a)
    return src[a:b]


def fig_link(url, text, size='xlarge'):
    return '<a class="inline-link inline-link--%s" href="%s" target="_blank" rel="noopener">%s</a>' % (size, url, text)


def sec_link(slug, anchor, text, page='specifications'):
    return '<a class="inline-link inline-link--large inline-link--secondary" href="%s-%s.html#%s">%s</a>' % (slug, page, anchor, text)


def three_pages(slug, what, spec_what, code_what):
    return ('<p class="ds-desc">This documentation has three pages. <strong>Examples &amp; Guidelines</strong> (this page) shows when and how to use %s. ' % what +
            link_large(slug + '-specifications.html', 'Specifications') + ' holds %s. ' % spec_what + link_large(slug + '-code.html', 'Code') + ' shows %s.</p>' % code_what)


def fig_one(inner, cap=None, stage_attr='', stage_cls=''):
    return '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage%s"%s>%s</div>%s</figure></div>' % ((' ' + stage_cls) if stage_cls else '', stage_attr, inner, ('<figcaption class="ds-fig__cap">%s</figcaption>' % cap) if cap else '')


def sel(lid, sid, label, pg, options, cur):
    """A Small eco-select field for a playground (options: [(value, text)], cur = the selected value)."""
    opts = ''.join('<option value="%s"%s>%s</option>' % (v, ' selected' if v == cur else '', t) for v, t in options)
    return ('<div class="ds-field form-field"><label class="form-label form-label--sm" for="%s" id="%s">%s</label><div class="input-wrap"><select class="form-select form-select--sm" data-pg="%s" id="%s">%s</select>'
            '<span class="form-select-arrow" aria-hidden="true">arrow_drop_down</span></div></div>') % (sid, lid, label, pg, sid, opts)


def fig_pair(do_inner, do_cap, dont_inner, dont_cap):
    return ('<div class="ds-figs"><figure class="ds-fig ds-fig--do"><div class="ds-fig__stage">%s</div><figcaption class="ds-fig__cap"><span class="ds-fig__ic" aria-hidden="true">check_circle</span>%s</figcaption></figure>'
            '<figure class="ds-fig ds-fig--dont"><div class="ds-fig__stage">%s</div><figcaption class="ds-fig__cap"><span class="ds-fig__ic" aria-hidden="true">cancel</span>%s</figcaption></figure></div>') % (do_inner, do_cap, dont_inner, dont_cap)


def ol_parts(items):
    return '<ol class="ds-bullets ds-bullets--num">' + ''.join('<li><strong>%s.</strong> %s</li>' % (a, b) for a, b in items) + '</ol>'


def bullets(items):
    return '<ul class="ds-bullets">' + ''.join('<li>%s</li>' % x for x in items) + '</ul>'


def note(t):
    return '<p class="ds-desc ds-note">%s</p>' % t


def desc(t):
    return '<p class="ds-desc">%s</p>' % t
