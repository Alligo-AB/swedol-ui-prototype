"""Selection rule for the docs playgrounds (skill selection-guide, decided 2026-11-08).

build.emit() runs apply() on every generated page, so every generator (and every new one) gets the same controls
without changing its own btn_group / sel / sel_field calls:
  - on/off (Off/On, None/X, Shown/Hidden, No/Yes): a Small switch, one per row, its own text is the label
  - fields that recur across pages (State, Size, Value, Content, Type, Color, Variant, Status …): radio buttons everywhere
  - Breakpoint, Mode/Theme, Emphasis, Background, Weight, Style …: button group everywhere
  - other fields: 2-3 one-word options = button group, 4-7 options or longer labels = radio buttons
  - 8 or more options: select
Only the playground controls change; the rest of the page is left as it is.
The same converter was run once on the hand-edited pages (2026-11-08)."""
import re, html as _html
from build import radio_group, sw_group, btn_group

OFF_WORDS = {'off', 'none', 'hidden', 'hide', 'no'}
STATE_WORDS = {'enabled', 'hover', 'focus', 'disabled', 'active', 'current', 'error', 'success', 'open', 'unselected', 'selected', 'default', 'remove'}
RADIO_ALWAYS = {'state', 'size', 'value', 'content', 'type', 'color', 'variant', 'status', 'row', 'leading', 'trailing', 'header background', 'cells',
                'supporting text', 'divider', 'selection', 'crumbs', 'state (second tab)', 'track', 'link', 'row 3'}
GROUP_ALWAYS = {'breakpoint', 'mode', 'theme', 'emphasis', 'background', 'weight', 'label weight', 'style', 'label style', 'underline', 'placement',
                'direction', 'icons', 'pill', 'segments', 'options', 'selected', 'features per card', 'rows', 'accent colour (active line)', 'layout',
                'position', 'padding', 'alignment', 'tooltip', 'letter case', 'label'}
SWITCH_TEXT = {'disabled option': 'Last option disabled', 'recommended': 'Recommended (*)', 'left icon': 'Left icon (search)'}

GROUP_RE = re.compile(r'<div class="ds-field"((?: id="[^"]+")?(?: hidden)?)><span class="form-label form-label--sm" id="([^"]+)">([^<]+)</span><div class="btn-group" role="group" aria-labelledby="[^"]+" data-pg="([^"]+)"[^>]*>((?:<button[^>]*>[^<]*</button>)+)</div></div>')
SELECT_RE = re.compile(r'<div class="ds-field form-field"><label class="form-label form-label--sm" for="([^"]+)" id="([^"]+)">([^<]+)</label><div class="input-wrap"><select class="form-select form-select--sm" data-pg="([^"]+)" id="[^"]+">((?:<option[^>]*>[^<]*</option>)+)</select><span class="form-select-arrow" aria-hidden="true">arrow_drop_down</span></div></div>')


def decide(label, opts):
    lab = label.strip().lower()
    texts = [t.strip().lower() for _, t in opts]
    if len(opts) >= 8: return 'select'
    if len(opts) == 2 and lab not in RADIO_ALWAYS and (set(texts) & OFF_WORDS) and (set(texts) - OFF_WORDS): return 'switch'
    if lab in RADIO_ALWAYS or set(texts) <= STATE_WORDS: return 'radio'
    if lab in GROUP_ALWAYS: return 'group'
    if len(opts) >= 4 or any(len(t.split()) > 1 for t in texts): return 'radio'
    return 'group'


def _controls(s):
    i = s.find('class="ds-controls"')
    if i < 0: return None
    j = s.find('<h3 class="ds-h3">Markup for this selection', i)
    return i, (j if j > 0 else s.find('</section>', i))


def apply(s):
    span = _controls(s)
    if not span: return s
    i, j = span
    seg = s[i:j]
    items = []
    for m in GROUP_RE.finditer(seg):
        if 'data-bp-toggle' in m.group(0): continue
        opts = re.findall(r'data-v="([^"]*)"[^>]*>([^<]*)</button>', m.group(5))
        cur = re.search(r'data-v="([^"]*)" aria-pressed="true"', m.group(5))
        items.append((m.start(), m.end(), m.group(2), _html.unescape(m.group(3)), m.group(4), opts, cur.group(1) if cur else opts[0][0], 'group', m.group(1)))
    for m in SELECT_RE.finditer(seg):
        opts = re.findall(r'<option value="([^"]*)"[^>]*>([^<]*)', m.group(5))
        cur = re.search(r'<option value="([^"]*)" selected', m.group(5))
        items.append((m.start(), m.end(), m.group(2), _html.unescape(m.group(3)), m.group(4), opts, cur.group(1) if cur else (opts[0][0] if opts else ''), 'select', ''))
    items.sort()
    out, pos, need = [], 0, set()
    for st, en, lid, label, key, opts, cur, kind, attrs in items:
        if not opts: continue
        target = decide(label, opts)
        if target == 'switch':
            offv = [v for v, t in opts if t.strip().lower() in OFF_WORDS][0]
            onv = [v for v, t in opts if v != offv][0]
            new = sw_group(lid, None, [(key, SWITCH_TEXT.get(label.strip().lower(), label.strip()), cur == onv, onv, offv)]); need.add('switch')
        elif target == 'radio':
            new = radio_group(lid, label, key, opts, cur); need.add('radio')
        elif target == 'group' and kind == 'select':
            new = btn_group(lid, label, 'data-pg="%s"' % key, [(v, t, v == cur) for v, t in opts])
        else:
            continue
        if attrs: new = new.replace('<div class="ds-field"', '<div class="ds-field"' + attrs, 1)   # keep id / hidden that page JS toggles
        out.append(seg[pos:st]); out.append(new); pos = en
    if not out: return s
    out.append(seg[pos:])
    s = s[:i] + ''.join(out) + s[j:]
    for css in sorted(need):
        if 'components/css/%s.css' % css in s: continue
        m = re.search(r'\n  <link rel="stylesheet" href="\.\./\.\./components/css/[a-z-]+\.css[^"]*">', s)
        if m: s = s[:m.end()] + '\n  <link rel="stylesheet" href="../../components/css/%s.css">' % css + s[m.end():]
    return s
