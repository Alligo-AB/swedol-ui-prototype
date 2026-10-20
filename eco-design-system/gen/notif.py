"""Shared pieces of the five notification page sets (toast, toast-ecom, modal, banner, inline).
The sets are types of the Notifications hub (components/notifications.html), like the Badge types: breadcrumb Components / Notifications / Toast."""
from build import *

FIGMA = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=%s'
GUIDE = '.claude/skills/notifications-guide/SKILL.md'

# notifications.css loads BEFORE docs.css: docs.css imports button.css and inline-link.css, which must win over the .btn / .inline-link base of notifications.css.
PRE = ['../notifications.css?v=22']
# markup builders + runtime (every page: the Code page prints markup built by ECO_N.html), range for the Motion sliders and the auto-hide time
BODY = ['../notifications.js?v=12', '../../components/js/range.js']
ICON_PICKER = '../../components/icon-picker/icon-picker.js'

STYLE = r'''    .pg-note { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .pg-matrix td { vertical-align: top; padding-top: 16px; padding-bottom: 16px; }
    .pg-stack { display: flex; flex-direction: column; gap: 16px; align-items: stretch; width: 100%; }
    .pg-grid { display: grid; gap: 24px; grid-template-columns: minmax(0, 1fr); justify-items: start; width: 100%; }
    @media (min-width: 1100px) { .pg-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 24px 32px; } }
    .pg-row { display: flex; align-items: center; justify-content: space-between; gap: 16px; padding: 16px 0; border-top: 1px solid var(--color-border-secondary); flex-wrap: wrap; width: 100%; }
    .pg-row:first-child { border-top: 0; padding-top: 0; }
    .pg-row:last-child { padding-bottom: 0; }
    .pg-row__txt { flex: 1; min-width: 240px; }
    .pg-row__txt b { display: block; font-size: 16px; line-height: 22px; }
    .pg-row__txt span { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-secondary); }
    .ds-field[hidden], .form-range[hidden] { display: none; }
    .pg-fig-host { width: 100%; max-width: 100%; overflow: hidden; }
    .pg-btns { display: flex; gap: 8px; flex-wrap: wrap; }
    .pg-form__region { min-height: 0; width: 100%; }
    .pg-form__region:empty { display: none; }
    body[data-bp="mobile"] :is(.toast, .ecom-toast, .banner-notification, .inline-notification) { max-width: 375px; }   /* the forced Mobile preview is as wide as a phone: in real use these fill the window */'''


def sel_field(lid, sid, label, pg, options):
    opts = ''.join('<option value="%s">%s</option>' % (v, t) for v, t in options)
    return ('<div class="ds-field form-field"><label class="form-label form-label--sm" for="%s" id="%s">%s</label><div class="input-wrap"><select class="form-select form-select--sm" data-pg="%s" id="%s">%s</select>'
            '<span class="form-select-arrow" aria-hidden="true">arrow_drop_down</span></div></div>') % (sid, lid, label, pg, sid, opts)


def txt_field(id_, label, value, ph, field_id='', hidden=False, extra=''):
    return ('<div class="ds-field form-field"%s%s><label class="form-label form-label--sm" for="%s">%s</label><div class="input-wrap"><div class="input-box input-box--sm">'
            '<input class="form-input" type="text" id="%s" value="%s" placeholder="%s"%s /></div></div></div>') % (
        (' id="%s"' % field_id) if field_id else '', ' hidden' if hidden else '', id_, label, id_, esc_attr(value), esc_attr(ph), extra)


def icon_field(field_id='f-ic', input_id='pg-ic'):
    return ('<div class="ds-field form-field" id="%s" hidden><label class="form-label form-label--sm" for="%s">Icon (Informational only)</label><div class="input-wrap"><div class="input-box input-box--sm">'
            '<input class="form-input" type="text" id="%s" data-icon-picker value="" placeholder="Material Symbol name, e.g. local_shipping" aria-describedby="%s-h" /></div></div>'
            '<span class="pg-note" id="%s-h" style="margin:0">Google Material Symbols name. Shown as Outlined: Fill 0, Weight 300, Grade 0. Empty = the default filled icon.</span></div>') % (field_id, input_id, input_id, input_id, input_id)


def range_field():
    return ('<div class="form-range" id="pg-time-f" data-range data-unit=" s" data-ticks="2|3|4|5|6|7|8|9|10"><div class="form-range__head"><label class="form-range__label" for="pg-time">Auto-hide time</label>'
            '<output class="form-range__value" for="pg-time"></output></div><input class="form-range__input" id="pg-time" type="range" min="2" max="10" step="1" value="4"><div class="form-range__ticks"></div></div>')


def motion_note(what):
    return '<p class="pg-note" style="margin:0">%s is set in <a href="#motion" class="inline-link inline-link--small inline-link--tertiary">Motion</a>.</p>' % what


def fig_one_id(id_, cap=None, cls=''):
    return fig_one('<div class="%s" id="%s"></div>' % (cls or 'pg-stack', id_), cap)


def pair(do_id, do_cap, dont_id, dont_cap, cls='pg-stack'):
    return fig_pair('<div class="%s" id="%s"></div>' % (cls, do_id), do_cap, '<div class="%s" id="%s"></div>' % (cls, dont_id), dont_cap)


def which(rows):
    return table(['The message…', 'Use'], rows)


def lead_link(href, text):
    return '<a class="inline-link inline-link--xlarge" href="%s">%s</a>' % (href, text)


def lk(href, text):
    return '<a class="inline-link inline-link--small" href="%s">%s</a>' % (href, text)


def bp_toolbar(lid):
    return toolbar([(lid, 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')])


def parts_note(slug, what, spec_what, code_what):
    return three_pages(slug, what, spec_what, code_what)


# JS shared by the Examples pages: motion sections alternate backgrounds by default; the split pages are white with dividers
JS_MOTION_FIX = r'''
  $$('.ds-doc > section.ds-section').forEach(function (s) { s.classList.remove('ds-section--secondary'); });
  $('#motion').insertAdjacentHTML('beforebegin', '<div class="ds-sep"><hr class="divider" /></div>');
'''

JS_PRE = r'''
  var N = ECO_N, H = N.html, IMG = '/images/product-hantverksbyxa.jpg';
  var STATUS = [['info', 'Informational'], ['success', 'Success'], ['warning', 'Warning'], ['error', 'Error']];
  function mk(html) { var d = document.createElement('div'); d.innerHTML = html; return d.firstChild; }
'''

# the page frame of a type: eyebrow, hub parent, no Figma badge
BASE = dict(eyebrow='Components · Notifications', parent=('notifications.html', 'Notifications'), pre_css=PRE, body_js=BODY, css=['menu', 'range'], style=STYLE)
