"""Colors: the first Foundation in the three-page structure (2026-10-22).
Overview (colors.html) / Primitive colors (colors-primitives.html) / Semantic tokens (colors-tokens.html).
Foundations have no Specifications or Code tab, so the set uses the custom page set of build.py (pages=[...]), like the Hero banner widget.
The old one-page version is in old-source/colors.html. The cards, the Cards / Table switch and the text of the token cards are the old page's, moved into color-kit.js."""
import os
from build import *

HERE_ = os.path.dirname(os.path.abspath(__file__))
OUT_F = os.path.normpath(os.path.join(HERE_, '..', 'foundations'))
SLUG = 'colors'
FIGMA = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System'


def card_link(href, icon, title, text):
    if not icon.startswith('<'):
        icon = '<span class="mo-ic">%s</span>' % icon
    return '<a class="ds-linkcard ds-linkcard--row" href="%s"><div class="ds-linkcard__visual" aria-hidden="true">%s</div><div class="ds-linkcard__body"><span class="ds-linkcard__title">%s</span><span class="ds-linkcard__desc">%s</span></div></a>' % (href, icon, title, text)


def sec(href, text):
    return '<a class="inline-link inline-link--large inline-link--secondary" href="%s">%s</a>' % (href, text)


STYLE = r'''    :root { --ds-subnav-h: 0px; }   /* the table header of the Cards / Table view sticks to the top of the window: no sticky bar above it from 1024px, where the table exists */
    .ds-linkcard__visual svg { width: 100%; max-width: 176px; height: auto; padding: 0 12px; box-sizing: border-box; }
    .ck-flow { display: flex; flex-direction: column; align-items: stretch; gap: 8px; width: 100%; }
    .ck-flow__col { display: flex; flex-direction: column; gap: 8px; min-width: 0; }
    .ck-flow__h { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; font-weight: 600; text-transform: uppercase; color: var(--color-text-tertiary); }
    .ck-flow__arrow { align-self: center; font-size: 24px; color: var(--color-icon-primary); }
    .ck-box { display: block; padding: 8px 12px; background: var(--color-surface-raised-primary); border: 1px solid var(--color-border-primary); font-size: 14px; line-height: 20px; letter-spacing: 0.36px; overflow-wrap: anywhere; }
    .ck-box--hex { display: flex; align-items: center; gap: 8px; }
    .ck-box--hex i { flex: none; width: 20px; height: 20px; background: var(--color-primitive-color-neutral-white); border: 1px solid var(--color-border-primary); }
    .ck-btns { display: flex; flex-wrap: wrap; gap: 8px; }
    .ck-btn { display: inline-flex; align-items: center; gap: 4px; min-height: 40px; padding: 0 16px; font-size: 14px; line-height: 20px; letter-spacing: 0.36px; font-weight: 600; text-transform: uppercase; }
    .ck-btn--light { background: var(--color-surface-action-2); color: var(--color-text-primary); border: 1px solid var(--color-border-primary); }
    .ck-btn--dark { background: var(--color-surface-action-1); color: var(--color-text-primary-inverted); }
    .ck-btn .mo-ic { font-size: 20px; }
    .ck-btn--dark .mo-ic { color: var(--color-icon-inverted); }
    @media (min-width: 769px) {
      .ck-flow { flex-direction: row; align-items: center; gap: 16px; }
      .ck-flow__col { flex: 1 1 0; }
      .ck-flow__arrow { transform: rotate(-90deg); }
    }
    .ck-use { display: flex; flex-direction: column; width: 100%; border: 1px solid var(--color-border-primary); background: var(--color-surface-raised-primary); }
    .ck-ramp { display: flex; height: 40px; }
    .ck-ramp span { flex: 1; }
    .ck-split { display: flex; height: 120px; }
    .ck-split span { height: 100%; }
    .ck-bars { display: flex; }
    .ck-bars span { flex: 1; padding: 8px 12px; font-size: 14px; line-height: 20px; letter-spacing: 0.36px; font-weight: 600; text-transform: uppercase; }
    .ck-bars .ck-swedol { background: var(--color-accent-default); color: var(--color-text-primary); }
    .ck-bars .ck-tools { background: var(--color-primitive-color-brand-tools-accent-brand); color: var(--color-text-primary-inverted); }'''

# ---------------------------------------------------------------- Overview
RAMP_DARK = ['100', '90', '80', '70', '60', '50', '40', '30', '20', '15', '10', '05', '02']
RAMP_LIGHT = ['15', '10', '05', '02']


def ramp(steps):
    return '<div class="ck-ramp" aria-hidden="true">' + ''.join('<span style="background:var(--color-surface-%s)"></span>' % n for n in steps) + '<span style="background:var(--color-surface-00)"></span></div>'


def use_fig(black_pct, steps, cap):
    return ('<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage"><div class="ck-use" role="img" aria-label="%s">' % cap +
            ramp(steps) +
            '<div class="ck-split"><span style="flex:%d;background:var(--color-surface-100)"></span><span style="flex:%d;background:var(--color-surface-00)"></span></div>' % (black_pct, 100 - black_pct) +
            '<div class="ck-bars"><span class="ck-swedol">Swedol</span><span class="ck-tools">Tools</span></div></div></div><figcaption class="ds-fig__cap">%s</figcaption></figure></div>' % cap)


overview = '<h2 class="ds-h2">Overview</h2>' + \
    desc('In our UI, colors are applied according to their specific function. These functions are called <strong>semantic colors</strong> and describe the color categories we use. They derive from our base colors, the <strong>primitive colors</strong>, which serve only as references and are never used directly in the UI.') + \
    desc('If you need a color beyond the semantic colors, consult a designer to evaluate whether the palette should be extended. ECO is built for consistency and efficiency, so always use the provided guidelines without altering or extending the styles.') + \
    '<p class="ds-desc">This documentation has three pages. <strong>Overview</strong> (this page) explains how color works in ECO. ' + sec('colors-primitives.html', 'Primitive colors') + ' lists the base palette. ' + sec('colors-tokens.html', 'Semantic tokens') + ' lists every token the components use, as cards or as a table.</p>'

semantic = '<h2 class="ds-h2">Semantic colors</h2>' + \
    desc('Semantic colors are associated with particular meanings and are used directly in the user interface.') + \
    desc('Semantic colors help the users of the design system create consistency by giving them a collection of self-documenting tokens. The tokens can be applied across different UI components, instead of picking at random from a broad range of neutral colors.') + \
    desc('By using tokens to define and categorize roles instead of relying on hex values, any change to the color palette is reflected systematically. A change to one color then cascades consistently to every role that uses it.') + \
    card_link('colors-tokens.html', '<svg width="176" height="48" viewBox="0 0 176 48" aria-hidden="true"><path d="M24 0 48 24 24 48 0 24Z" fill="var(--color-accent-dark)"/><path d="M24 0 0 24 24 48Z" fill="var(--color-accent-default)" opacity=".55"/><circle cx="88" cy="24" r="24" fill="var(--color-surface-30)"/><path d="M88 0a24 24 0 0 1 0 48Z" fill="var(--color-surface-02)"/><rect x="128" width="48" height="48" fill="var(--color-primitive-color-system-electric-blue)"/><rect x="144" y="16" width="16" height="16" fill="var(--color-surface-information-weaker)"/></svg>', 'Semantic color tokens', 'Every token the components use, with hex, RGB and purpose.')

primitive = '<h2 class="ds-h2">Primitive colors</h2>' + \
    desc('Primitive colors are our base palette, which the semantic palette derives from. A primitive is a color with a name, and the name derives from the hex code. They are references only: a component never uses one.') + \
    bullets(['<strong>Neutral (grey):</strong> black, white and a ladder of greys. The foundation of the UI.',
             '<strong>System:</strong> the colors of messages and status.',
             '<strong>Concept brand colors:</strong> the accent of each Alligo concept brand.',
             '<strong>Text emphasis and opacity:</strong> the colors the text tokens and the overlays derive from.']) + \
    card_link('colors-primitives.html', 'colorize', 'Primitive colors', 'The base palette, read live from the token package.')

how = '<h2 class="ds-h2">How color tokens work</h2>' + \
    desc('Tokens start as primitive values, which have a name that derives from a hex code. In production we use the semantic tokens, which derive from the primitive tokens. The name of a semantic token describes how and where it should be used.') + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage"><div class="ck-flow" role="img" aria-label="A hex value becomes a primitive token, which becomes two semantic tokens, which a button uses">' + \
    '<div class="ck-flow__col"><span class="ck-flow__h">Hex value</span><span class="ck-box ck-box--hex"><i aria-hidden="true"></i><span id="fl-hex">&nbsp;</span></span></div>' + \
    '<span class="ck-flow__arrow mo-ic" aria-hidden="true">arrow_downward</span>' + \
    '<div class="ck-flow__col"><span class="ck-flow__h">Primitive token</span><span class="ck-box">--color-primitive-color-neutral-white</span></div>' + \
    '<span class="ck-flow__arrow mo-ic" aria-hidden="true">arrow_downward</span>' + \
    '<div class="ck-flow__col"><span class="ck-flow__h">Semantic tokens</span><span class="ck-box">--color-surface-action-2</span><span class="ck-box">--color-icon-inverted</span></div>' + \
    '<span class="ck-flow__arrow mo-ic" aria-hidden="true">arrow_downward</span>' + \
    '<div class="ck-flow__col"><span class="ck-flow__h">In a component</span><div class="ck-btns"><span class="ck-btn ck-btn--light">Button label</span><span class="ck-btn ck-btn--dark"><span class="mo-ic" aria-hidden="true">check</span>Label</span></div></div>' + \
    '</div></div><figcaption class="ds-fig__cap">One hex value, one primitive, two semantic tokens: the surface of the light button and the icon on the dark one. The page you are reading uses the same tokens.</figcaption></figure></div>' + \
    '<h3 class="ds-h3 ds-group">Naming</h3>' + \
    bullets(['A primitive is <code>--color-primitive-color-&lt;group&gt;-&lt;name&gt;</code>, for example <code>neutral-grey-90</code>.',
             'A semantic token is <code>--color-&lt;role&gt;-&lt;name&gt;</code>, for example <code>surface-action-2</code> or <code>text-primary</code>.',
             'The role comes first: surface, text, icon, border, accent. Status and state come after it.'])

families = '<h2 class="ds-h2">Token families</h2>' + \
    desc('Pick the token by role, not by how it looks. Each family has its own section on the ' + sec('colors-tokens.html', 'Semantic tokens') + ' page.') + \
    table(['Family', 'Use it for', 'Example'], [
        ['Neutrals and surfaces', 'The page, the full-width sections and the cards on them. Never pick a grey by hand.', '<code>background-primary</code>, <code>surface-raised-secondary</code>'],
        ['Brand accent', 'Emphasis and brand moments. Not decoration, and not text on white.', '<code>accent-default</code>'],
        ['Text and icon', 'Content, support text, links and buttons. The badge on each swatch is the contrast.', '<code>text-primary</code>, <code>icon-inverted</code>'],
        ['Border', 'Structure and outline, and the borders of interactive states.', '<code>border-primary</code>, <code>border-focus</code>'],
        ['Status', 'Information, success, warning and danger, each as default, weak and weaker. Never branding.', '<code>surface-danger-weak</code>'],
        ['Action and state', 'Fills for buttons, navigation and disabled controls.', '<code>surface-action-1</code>'],
        ['Overlays', 'Transparent black and white for hover fills, scrims and layers.', '<code>surface-opacity-black-20</code>']])

online = '<h2 class="ds-h2">Online vs traditional</h2>' + \
    desc('The colors divide into main and complementary colors, which together represent the visual identity. Swedol, for example, is primarily perceived as a black and lime green company, while Tools is white and red. To make that visible online we use, for example, a dark header for Swedol and a lighter touch for Tools.') + \
    '<h3 class="ds-h3 ds-group">Traditional media</h3>' + \
    desc('Black is generally the base color for the whole Alligo group and is used on larger surfaces. It represents professionalism and puts competence in what we do.') + \
    use_fig(75, RAMP_DARK, 'Alligo general color use: a black base, with the Swedol and Tools accents.') + \
    '<h3 class="ds-h3 ds-group">E-com</h3>' + \
    desc('The colors for e-com are weighted towards a lighter, white base. White is a proven color for creating higher online sales and for mediating a positive user experience.') + \
    use_fig(0, RAMP_LIGHT, 'E-com color use: a white base, with the same accents.')

contrast = '<h2 class="ds-h2">Contrast ratios</h2>' + \
    desc('Contrast is the difference in brightness between two elements. The Web Content Accessibility Guidelines (WCAG) set the ratios that give the minimum contrast for legibility.') + \
    table(['Content', 'Level AA', 'Level AAA'], [
        ['Normal text', '4.5:1', '7:1'], ['Large text', '3:1', '4.5:1'], ['Graphical elements and interface components, such as chart marks and input borders', '3:1', 'Not defined']]) + \
    desc('Large text is 18 point (typically 24px) or larger, or 14 point (typically 18.66px) or larger when it is bold. The swatches of the text tokens on the ' + sec('colors-tokens.html#text', 'Semantic tokens') + ' page show the ratio on the intended surface.')

usage = '<h2 class="ds-h2">Usage</h2>' + \
    rules(['Write <code>var(--color-…)</code>. Look the name up in <code>tokens.json</code>.', 'Pick the token by role (text, surface, border, status), not by how it looks.', 'Use inverted text and icon tokens on dark surfaces.', 'Keep status colors for status: information, success, warning, danger.'],
          ['Hardcode hex or rgb, even when it matches a token today.', 'Use a primitive color in a component.', 'Use the brand accent as text color on white.', 'Put light-mode tokens on a dark surface.', 'Invent a new grey. If nothing fits, ask before adding a value.'])

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html', 'WCAG 2.2: Contrast (Minimum)', 'Success criterion 1.4.3: the ratios for text.'),
    ('https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html', 'WCAG 2.2: Non-text Contrast', 'Success criterion 1.4.11: the ratio for graphics and components.'),
    ('https://m3.material.io/styles/color/roles', 'Material Design 3: Color roles', 'Google.'),
    ('https://carbondesignsystem.com/elements/color/overview/', 'Carbon Design System: Color', 'IBM.')])

ex = [('overview', overview), ('semantic-colors', semantic), ('primitive-colors', primitive), ('how-color-tokens-work', how), ('token-families', families), ('online-vs-traditional', online), ('contrast-ratios', contrast), ('usage', usage), ('references', references)]

JS_EX = r'''
  COLORKIT.fetchPackage(function (pkg) {   // the hex of the primitive in the diagram comes from the package, never typed here
    var p = pkg.prim['neutral-white'], b = $('#fl-hex');
    if (p) b.textContent = p.value.toUpperCase();
  }, function () { $('#fl-hex').textContent = 'Not loaded'; });
'''

# ---------------------------------------------------------------- Primitive colors
def grid(id_, cap=None):
    return '<div class="ds-grid" id="%s"></div>' % id_


p_about = '<h2 class="ds-h2">About primitive colors</h2>' + \
    desc('Primitive colors are our base palette, which the semantic palette derives from. Below are the colors that define it. They are the references the ' + sec('colors-tokens.html', 'semantic tokens') + ' point to: a component uses the semantic token, never the primitive.') + \
    desc('Every swatch shows which semantic tokens use it. If you need a color that no primitive has, consult a designer before adding one.')

p_neutral = '<h2 class="ds-h2">Neutral (grey)</h2>' + \
    desc('The neutral palette is foundational and dominant in our UI, which makes it easier to add specific brand colors and system colors and make them stand out.') + \
    desc('Neutral colors apply to most backgrounds, text and shapes. They do not typically have a meaning of their own, though they can imply things like disabled states.') + \
    desc('A mainly grey palette gives the designs nuance and creates opportunities for a purposeful use of color, which makes a good user experience. Each screen should be dominated by the greys and the core colors of black, white and the appropriate brand color for accent.') + \
    grid('g-neutral')

p_system = '<h2 class="ds-h2">System</h2>' + \
    desc('The system colors help communicate messages. Use them for elements such as badges, alert and critical message boxes, or areas and sections that require immediate attention.') + grid('g-system')

p_brand = '<h2 class="ds-h2">Concept brand colors</h2>' + \
    desc('Alligo concept brands each have their own set of these colors. They put some flavor into the site and accent the brand that it represents.') + \
    desc('Brand colors are mostly placed in common elements that occur throughout the site, which leaves the other colors, for example the customer price and the system colors, to give the visual aid they are there for.') + \
    '<h3 class="ds-h3">Swedol</h3>' + grid('g-swedol') + \
    '<h3 class="ds-h3">Tools</h3>' + grid('g-tools') + \
    '<div id="brand-more" hidden><h3 class="ds-h3">Other concept brands in the package</h3>' + desc('These primitives exist in the token package. No semantic token uses them yet.') + grid('g-brand-more') + '</div>'

p_text = '<h2 class="ds-h2">Text emphasis</h2>' + \
    desc('Primitives named after how strong the text is. The text tokens derive from them, so a hex that looks like a grey here is still not a neutral.') + grid('g-text')

p_opacity = '<h2 class="ds-h2">Opacity</h2>' + \
    desc('Transparent black and white. The overlay tokens (hover fills, scrims, layers) derive from them. The checkerboard shows the transparency.') + grid('g-opacity')

p_cov = '<h2 class="ds-h2">Coverage</h2><p class="ds-desc" id="coverage-text"></p>'

prim = [('about', p_about), ('neutral', p_neutral), ('system', p_system), ('concept-brand-colors', p_brand), ('text-emphasis', p_text), ('opacity', p_opacity), ('coverage', p_cov)]

JS_PRIM = r'''
  var K = COLORKIT, GROUPS = ['g-neutral', 'g-system', 'g-swedol', 'g-tools', 'g-brand-more', 'g-text', 'g-opacity'];
  var NEUTRAL = ['neutral-black'].concat(['90', '80', '70', '60', '50', '40', '30', '20', '15', '10', '05', '02'].map(function (n) { return 'neutral-grey-' + n; }), ['neutral-white']);
  var SYSTEM = ['dark-navy', 'ultramarine', 'sky-blue', 'ice-blue', 'deep-forrest-green', 'forrest-green', 'mint', 'mint-white', 'brownish-yellow', 'mustard-yellow', 'sun-yellow', 'light-yellow', 'maroon', 'dark-red', 'bright-red', 'coral-pink', 'light-pink', 'electric-blue', 'dark-cyan'].map(function (n) { return 'system-' + n; });
  function render(pkg) {
    K.clear(GROUPS);
    var old = document.getElementById('other'); if (old) { old.previousElementSibling.remove(); old.remove(); }
    var names = Object.keys(pkg.prim), shown = {};
    function rest(prefix, list) { return list.concat(names.filter(function (n) { return n.indexOf(prefix) === 0 && list.indexOf(n) < 0; })); }
    function place(id, list) {
      var host = document.getElementById(id); host._cols = K.PRIMITIVE;
      list.forEach(function (n) {
        if (!pkg.prim[n] || shown[n]) return; shown[n] = 1;
        K.add(host, { key: n, t: { var: pkg.prim[n].var, value: pkg.prim[n].value }, kind: 'fill', prim: true, used: pkg.used[n] });
      });
      return host._recs ? host._recs.length : 0;
    }
    place('g-neutral', rest('neutral-', NEUTRAL));
    place('g-system', rest('system-', SYSTEM));
    place('g-swedol', ['brand-swedol-accent-brand', 'brand-swedol-accent-light', 'brand-swedol-accent-dark']);
    place('g-tools', ['brand-tools-accent-brand', 'brand-tools-accent-light', 'brand-tools-accent-dark']);
    var more = place('g-brand-more', names.filter(function (n) { return n.indexOf('brand-') === 0; }));
    document.getElementById('brand-more').hidden = !more;
    place('g-text', names.filter(function (n) { return n.indexOf('text-') === 0; }));
    place('g-opacity', names.filter(function (n) { return n.indexOf('opacity-') === 0; }));
    var left = names.filter(function (n) { return !shown[n]; });
    if (left.length) {   // anything the page above did not place (a new group in a later package version)
      var cs = document.getElementById('coverage'), sep = cs.previousElementSibling.cloneNode(true), s = document.createElement('section');
      s.className = 'ds-section'; s.id = 'other';
      s.innerHTML = '<div class="ds-page ds-inner ds-prose"><h2 class="ds-h2">Other</h2><p class="ds-desc">Primitive colors not yet placed in a group on this page.</p><div class="ds-grid" id="g-other"></div></div>';
      cs.parentNode.insertBefore(sep, cs); cs.parentNode.insertBefore(s, sep);
      place('g-other', left);
    }
    K.finish();
    var usedBy = {}; Object.keys(pkg.used).forEach(function (k) { pkg.used[k].forEach(function (t) { usedBy[t] = 1; }); });
    document.getElementById('coverage-text').textContent = names.length + ' primitive colors in the token package, all shown on this page' + (left.length ? ' (' + left.length + ' in “Other”)' : '') + '. ' + Object.keys(usedBy).length + ' semantic tokens use one of them directly. Source: the package file ' + 'dist/css/base/color.css, read when the page loads.';
  }
  K.fetchPackage(render, function () {
    var m = document.createElement('p'); m.className = 'ds-desc'; m.textContent = 'Could not load the token package (alligo-design-tokens) from the CDN. Check the connection and reload.';
    document.getElementById('about').querySelector('.ds-inner').appendChild(m);
  });
'''

# ---------------------------------------------------------------- Semantic tokens
t_neutrals = '<h2 class="ds-h2">Neutrals</h2>' + \
    desc('Black, white and a ladder of greys carry most of the interface. Swedol is monochrome by design, which keeps the brand accent scarce and meaningful. Numbers follow the share of black: <code>surface-100</code> is black, <code>surface-02</code> is almost white.') + \
    '<div class="ds-ramp" id="ramp" role="img" aria-label="Neutral surface scale from surface-100 (black) to surface-02 (near white)"></div>' + \
    '<div class="ds-grid" id="g-neutral"></div>' + \
    '<h3 class="ds-h3">Page and raised surfaces</h3>' + \
    desc('Every page sits on <code>background-primary</code>. Full-width sections alternate between <code>surface-raised-primary</code> and <code>surface-raised-secondary</code>, if nothing else is stated, and a card takes the opposite surface of the section it sits in, so it always reads as raised. Never pick a grey by hand.') + \
    '''<figure class="ds-layers" aria-label="Layering: page background, two alternating sections, and cards on the opposite surface">
      <div class="ds-layer ds-layer--page">
        <span class="ds-layer__tag">Page · background-primary</span>
        <div class="ds-layer ds-layer--primary">
          <span class="ds-layer__tag">Section · surface-raised-primary</span>
          <div class="ds-layer__row">
            <div class="ds-layer ds-layer--secondary ds-layer--card"><span class="ds-layer__tag">Card · surface-raised-secondary</span><i></i><i></i></div>
            <div class="ds-layer ds-layer--secondary ds-layer--card"><span class="ds-layer__tag">Card · surface-raised-secondary</span><i></i><i></i></div>
          </div>
        </div>
        <div class="ds-layer ds-layer--secondary">
          <span class="ds-layer__tag">Section · surface-raised-secondary</span>
          <div class="ds-layer__row">
            <div class="ds-layer ds-layer--primary ds-layer--card"><span class="ds-layer__tag">Card · surface-raised-primary</span><i></i><i></i></div>
            <div class="ds-layer ds-layer--primary ds-layer--card"><span class="ds-layer__tag">Card · surface-raised-primary</span><i></i><i></i></div>
          </div>
        </div>
      </div>
    </figure>''' + '<div class="ds-grid" id="g-page"></div>'

t_brand = '<h2 class="ds-h2">Brand accent</h2>' + \
    desc('The Swedol lime. Use it for emphasis and brand moments, not for decoration and not for text on white: its contrast is too low. Light accent works as a highlight surface, for example in table headings.') + \
    '<h3 class="ds-h3">Swedol</h3><div class="ds-grid ds-grid--feature" id="g-accent"></div>' + \
    '<h3 class="ds-h3">Tools</h3>' + desc('Tools has its own accent. These are primitive tokens from the package (<code>--color-primitive-color-brand-tools-accent-*</code>), so they are not in <code>tokens.json</code>; the Swedol <code>accent-*</code> tokens above are what the components use. All primitives are on the ' + sec('colors-primitives.html', 'Primitive colors') + ' page.') + \
    '<div class="ds-grid ds-grid--feature" id="g-tools"></div>'

t_text = '<h2 class="ds-h2">Text &amp; icon</h2>' + \
    desc('Choose the text token by role: <code>primary</code> for content, <code>secondary</code> and <code>tertiary</code> for support, <code>action</code> for links and buttons. The badge on each swatch is the WCAG contrast on the intended surface: white, or black for inverted and on-black tokens.') + \
    '<h3 class="ds-h3">Text</h3><div class="ds-grid" id="g-text"></div><h3 class="ds-h3">Icon</h3><div class="ds-grid" id="g-icon"></div>'

t_border = '<h2 class="ds-h2">Border</h2>' + \
    desc('Borders separate and outline. Default structure uses <code>primary</code> to <code>tertiary</code>; interactive states (hover, focus, selected) have their own tokens so the change is always the same across components.') + '<div class="ds-grid" id="g-border"></div>'

t_status = '<h2 class="ds-h2">Status</h2>' + \
    desc('Information, success, warning and danger each come as a matched set. <code>default</code> is the strong version, <code>weak</code> and <code>weaker</code> tone it down for backgrounds. Use them for status only, never for branding.') + '<div class="ds-status" id="g-status"></div>'

t_state = '<h2 class="ds-h2">Action &amp; state</h2>' + desc('Fills for buttons, navigation and disabled controls.') + '<div class="ds-grid" id="g-state"></div>'

t_overlay = '<h2 class="ds-h2">Overlays</h2>' + desc('Transparent black and white for hover fills, scrims and layers. The checkerboard shows the transparency.') + '<div class="ds-grid" id="g-overlay"></div>'

t_cov = '<h2 class="ds-h2">Coverage</h2><p class="ds-desc" id="coverage-text"></p>'

tok = [('neutrals', t_neutrals), ('brand', t_brand), ('text', t_text), ('border', t_border), ('status', t_status), ('state', t_state), ('overlay', t_overlay), ('coverage', t_cov)]

JS_TOK = r'''
  var K = COLORKIT, el = K.el, TOKENS_URL = '../../.claude/skills/eco-tokens/tokens.json';
  var STATUS = ['information', 'success', 'warning', 'danger'];
  var RAMP = ['100', '90', '80', '70', '60', '50', '40', '30', '20', '15', '10', '05', '02'];
  var GROUPS = ['g-neutral', 'g-page', 'g-accent', 'g-tools', 'g-text', 'g-icon', 'g-border', 'g-state', 'g-overlay', 'g-status', 'ramp'];
  var shown = {};

  function place(id, keys, colors, kind) {
    var host = document.getElementById(id);
    keys.forEach(function (k) {
      if (!colors[k] || shown[k]) return;
      shown[k] = 1;
      K.add(host, { key: k, t: colors[k], kind: kind });
    });
  }
  function build(colors) {
    K.clear(GROUPS);
    var old = document.getElementById('other'); if (old) { old.previousElementSibling.remove(); old.remove(); }
    shown = {};
    var keys = Object.keys(colors), rootCS = K.rootCS();
    var isStatus = function (k) { return new RegExp('^(surface|border)-(' + STATUS.join('|') + ')-').test(k); };

    // Ramp + neutral cards
    var ramp = document.getElementById('ramp');
    var rk = RAMP.map(function (n) { return 'surface-' + n; });
    rk.forEach(function (k) {
      var t = colors[k]; if (!t) return;
      var s = el('div', 'ds-ramp__step', k.replace('surface-', ''));
      s.style.background = 'var(' + t.var + ')';
      s.style.color = K.contrast(K.parseHex(t.value), [0, 0, 0]) > 4.5 ? 'var(--color-text-primary)' : 'var(--color-text-primary-inverted)';
      ramp.appendChild(s);
    });
    place('g-neutral', rk.concat(['greyscale-black']), colors, 'fill');
    place('g-page', ['background-primary', 'background-secondary', 'surface-raised-primary', 'surface-raised-secondary'], colors, 'fill');

    place('g-accent', keys.filter(function (k) { return k.indexOf('accent-') === 0; }), colors, 'fill');
    // Tools accent: primitives read live from the package CSS (they are not in tokens.json)
    var tools = document.getElementById('g-tools');
    [['brand', 'Primary accent of the Tools concept brand.'], ['light', 'Light accent: highlight surface, same role as accent-light.'], ['dark', 'Dark accent: hover state, same role as accent-dark.']].forEach(function (a) {
      var v = '--color-primitive-color-brand-tools-accent-' + a[0], val = rootCS.getPropertyValue(v).trim();
      if (val) K.add(tools, { key: 'tools-accent-' + a[0], t: { var: v, value: val, description: a[1] }, kind: 'fill', prim: true });
    });
    place('g-text', keys.filter(function (k) { return k.indexOf('text-') === 0; }), colors, 'text');
    place('g-icon', keys.filter(function (k) { return k.indexOf('icon-') === 0; }), colors, 'icon');
    place('g-border', keys.filter(function (k) { return k.indexOf('border-') === 0 && !isStatus(k); }), colors, 'border');
    place('g-state', ['surface-action-1', 'surface-action-2', 'surface-navigation-hover', 'surface-disabled'], colors, 'fill');
    place('g-overlay', keys.filter(function (k) { return /^surface-opacity-/.test(k); }), colors, 'fill');

    // Status matrix
    var host = document.getElementById('g-status');
    STATUS.forEach(function (s) {
      var col = el('div', 'ds-status__col');
      col.appendChild(el('div', 'ds-status__title', s.charAt(0).toUpperCase() + s.slice(1)));
      var rows = [
        ['surface-' + s + '-default', 'Surface · default', 'fill'],
        ['surface-' + s + '-weak', 'Surface · weak', 'fill'],
        ['surface-' + s + '-weaker', 'Surface · weaker', 'fill'],
        ['border-' + s + '-default', 'Border · default', 'border'],
        ['border-' + s + '-weak', 'Border · weak', 'border'],
        ['border-' + s + '-weaker', 'Border · weaker', 'border'],
        ['text-' + s + '-default', 'Text', 'text']
      ];
      rows.forEach(function (r) {
        var k = r[0]; if (!k || !colors[k]) return;
        shown[k] = 1;
        K.add(host, { key: k, t: colors[k], kind: r[2] });   // a record for the table view; the column below is the card view of this section
        var row = el('div', 'ds-status__row');
        var dot = el('span', 'ds-status__dot');
        dot.setAttribute('aria-hidden', 'true');
        if (r[2] === 'fill') dot.style.background = 'var(' + colors[k].var + ')';
        else if (r[2] === 'border') dot.style.cssText = 'border: 4px solid var(' + colors[k].var + ');';
        else { dot.textContent = 'Aa'; dot.style.color = 'var(' + colors[k].var + ')'; }
        var lab = el('span', 'ds-status__label');
        lab.appendChild(el('b', null, r[1]));
        lab.appendChild(el('span', null, k + ' · ' + colors[k].value));
        row.appendChild(dot); row.appendChild(lab);
        col.appendChild(row);
      });
      host.appendChild(col);
    });

    // Anything the page above did not place (new tokens in a later package version)
    var rest = keys.filter(function (k) { return !shown[k]; });
    if (rest.length) {
      var cs = document.getElementById('coverage'), sep = cs.previousElementSibling.cloneNode(true), s = document.createElement('section');
      s.className = 'ds-section'; s.id = 'other';
      s.innerHTML = '<div class="ds-page ds-inner ds-prose"><h2 class="ds-h2">Other</h2><p class="ds-desc">Tokens not yet placed in a group on this page.</p><div class="ds-grid" id="g-other"></div></div>';
      cs.parentNode.insertBefore(sep, cs); cs.parentNode.insertBefore(s, sep);
      place('g-other', rest, colors, 'fill');
    }
    var drift = K.finish();
    document.getElementById('coverage-text').textContent =
      keys.length + ' semantic color tokens, all shown on this page' + (rest.length ? ' (' + rest.length + ' in “Other”)' : '') +
      '. Source: .claude/skills/eco-tokens/tokens.json (this page reloads its content when that file changes).' +
      (drift ? ' ' + drift + ' token(s) differ from the live package and are flagged on their swatches: regenerate tokens.json with generate-tokens.py.' : ' All values match the live package.');
  }

  ECO.watch(TOKENS_URL, function (j) {
    var err = document.getElementById('load-error'); if (err) err.remove();
    build(j.color);
  }, function () {
    if (document.getElementById('load-error')) return;
    var m = el('p', 'ds-desc', 'Could not load tokens.json. Open this page through the local server (npx serve), not as a file.');
    m.id = 'load-error';
    document.getElementById('neutrals').querySelector('.ds-inner').appendChild(m);
  });
'''

C = dict(
    slug=SLUG, title='Colors', eyebrow='Foundations', out=OUT_F, first_plain=True,
    crumb_group=('../foundations-overview.html', 'Foundations'),
    lead='Color in ECO is <strong>semantic</strong>. A token says what a color is <em>for</em>, not what it looks like, so text, surfaces, borders and status each have their own family and a component never needs a raw hex value.',
    select_menu=False, css=['pill-segment-control'], style=STYLE,
    body_js=['../tokens-loader.js', '../color-kit.js', '../../components/js/pill-segment-control.js'],
    pages=[
        dict(kind='ex', suffix='', label='Overview', secs=ex, js=JS_EX,
             lead='Here in the color section you’ll find the colors of ECO that serve as the foundation for the majority of surfaces, borders and more, acting as essential components of our visual identity.'),
        dict(kind='prim', suffix='-primitives', label='Primitive colors', secs=prim, js=JS_PRIM,
             lead='The base palette that the semantic tokens derive from, read live from the token package. Primitives are references: a component uses a semantic token, never a primitive.'),
        dict(kind='tok', suffix='-tokens', label='Semantic tokens', secs=tok, js=JS_TOK,
             lead='Every semantic color token from <code>alligo-design-tokens</code>, live from the CDN this site already loads, as cards or as a table. The semantic naming style is a helpful way to indicate a color’s use: some colors are used broadly across ECO, and some have a more specific use. Swatches use <code>var(--color-…)</code> directly, so when the package is updated the page updates with it.'),
    ])

if __name__ == '__main__':
    emit(C)
