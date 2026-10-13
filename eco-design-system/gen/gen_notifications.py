"""The Notifications hub (components/notifications.html): one page, no tab bar, like the Badge hub. It chooses between the five types.
Each type has its own three-page set (gen_toast.py, gen_toast_ecom.py, gen_modal.py, gen_banner.py, gen_inline.py)."""
import sys
import build
from notif import *

SLUG = 'notifications'

STYLE = r'''    .pg-wiz { display: grid; gap: 24px; grid-template-columns: minmax(0, 1fr); width: 100%; }
    @media (min-width: 769px) { .pg-wiz { grid-template-columns: 360px minmax(0, 1fr); } }
    .pg-q { display: flex; flex-direction: column; gap: 20px; }
    .pg-res { display: flex; flex-direction: column; gap: 16px; }
    .pg-res h3 { font-size: 28px; line-height: 32px; font-weight: 600; }
    .pg-res p { font-size: 16px; line-height: 22px; letter-spacing: 0.32px; color: var(--color-text-secondary); }
    .pg-res .pg-prev { background: var(--color-surface-05); padding: 16px; border: 1px dashed var(--color-border-secondary); overflow: hidden; }
    .pg-res .pg-actions { display: flex; gap: 8px; flex-wrap: wrap; }
    .pg-ok { font-weight: 600; }
    .pg-btns { display: flex; gap: 8px; flex-wrap: wrap; }
    .pg-demo-stage { display: flex; flex-direction: column; gap: 16px; align-items: stretch; }
    .pg-flow-row { display: flex; align-items: center; gap: 16px; flex-wrap: wrap; padding: 16px 0; border-top: 1px solid var(--color-border-secondary); }
    .pg-flow-row:first-child { border-top: 0; padding-top: 0; }
    .pg-flow-row > div { flex: 1; min-width: 240px; }
    .pg-flow-row b { display: block; font-size: 16px; line-height: 22px; }
    .pg-flow-row span { font-size: 14px; line-height: 20px; color: var(--color-text-secondary); }
    .pg-note { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .ds-field[hidden] { display: none; }'''

def inl(href, text):
    return '<a href="%s" class="inline-link inline-link--small">%s</a>' % (href, text)

q = lambda i, lid, label, key, a, b: ('<div class="ds-field" id="q%d"><span class="form-label form-label--sm" id="%s">%s</span><div class="btn-group" role="group" aria-labelledby="%s" data-q="%s">'
                                      '<button type="button" data-v="%s" aria-pressed="true">%s</button><button type="button" data-v="%s" aria-pressed="false">%s</button></div></div>') % (i, lid, label, lid, key, a[0], a[1], b[0], b[1])

choose = '<h2 class="ds-h2">Which component</h2>' + desc('Answer up to three questions. The answer shows the component, why, and a live example you can fire.') + \
    '<div class="pg-wiz"><div class="ds-controls pg-q">' + \
    q(1, 'q1-l', 'Must the user decide before going on?', 'block', ('no', 'No'), ('yes', 'Yes')) + q(2, 'q2-l', 'What triggered it?', 'origin', ('task', 'A user action'), ('system', 'The system or an admin')) + \
    q(3, 'q3-l', 'Is it about a shopping action?', 'shop', ('no', 'No'), ('yes', 'Cart or wishlist')) + q(4, 'q4-l', 'How long should it stay?', 'life', ('brief', 'Briefly'), ('stay', 'Until the user acts')) + \
    '</div><div class="ds-stage pg-res" id="res" aria-live="polite"></div></div>'

matrix = '<h2 class="ds-h2">Decision matrix</h2><h3 class="ds-h3 ds-group">The five components</h3>' + desc('Two origins. <strong>Task-generated</strong> notifications answer something the user just did and belong next to where they are working. <strong>System-generated</strong> ones come from the application or an administrator, independent of what the user is doing.') + \
    '<div class="ds-table-wrap"><table class="ds-table"><thead><tr><th scope="col">Component</th><th scope="col">Disruption</th><th scope="col">Origin</th><th scope="col">Use when</th><th scope="col">Statuses</th></tr></thead><tbody id="mtx"></tbody></table></div>' + \
    '<h3 class="ds-h3 ds-group">When not to notify</h3>' + desc('Every notification interrupts. Frequent interruptions lower productivity and cause alert fatigue, so keep each one inside the part of the interface and the task where it matters. If the message is not needed, do not send it.')

status = '<h2 class="ds-h2">Status and icon</h2><h3 class="ds-h3 ds-group">Status and icon</h3>' + desc('Status colors carry a fixed meaning, and each has one reserved icon. Never pair a status color with another status’s icon. Icons are Material Symbols Outlined, weight 300, filled.') + \
    '<div class="ds-table-wrap"><table class="ds-table"><thead><tr><th scope="col">Status</th><th scope="col">Icon</th><th scope="col">Color token</th><th scope="col">Used for</th></tr></thead><tbody id="stat"></tbody></table></div>' + \
    '<h3 class="ds-h3 ds-group">Without a status</h3>' + desc('<strong>E-Com</strong> (E-Com Toast, E-Com Modal) uses the brand’s black and white and no status color; any icon from the gallery may be used. <strong>Promotion</strong> banners use the brand’s accent color or neutral black and white, also with a free icon.') + \
    '<h3 class="ds-h3 ds-group">Emphasis per component</h3><div class="ds-table-wrap"><table class="ds-table"><thead><tr><th scope="col">Component</th><th scope="col">Emphasis</th><th scope="col">Sizes</th><th scope="col">Layouts</th></tr></thead><tbody id="emph"></tbody></table></div>' + \
    '<h3 class="ds-h3 ds-group" id="emphasis">Choosing the emphasis</h3>' + \
    desc('<strong>Weak is the default. Strong is used sparingly.</strong> <strong>Status</strong> says what the message is (color and icon). <strong>Emphasis</strong> says how loud it is. Choose the component first, then the status by its meaning, then the emphasis. <strong>The status does not decide the emphasis; the consequence does.</strong> An Error does not have to be Strong, and a Warning can be Strong if the consequence is serious.') + \
    note('<strong>Design guidance given 2026-10-13, not in Figma.</strong> Figma defines the tiers but not when to pick which. It agrees with the Banner guidance already here (Strong only for what is urgent, Weaker for general information) and with how <a class="inline-link inline-link--medium inline-link--secondary" href="https://carbondesignsystem.com/components/notification/usage/" target="_blank" rel="noopener">Carbon</a>, <a class="inline-link inline-link--medium inline-link--secondary" href="https://spectrum.adobe.com/page/toast" target="_blank" rel="noopener">Adobe Spectrum</a>, <a class="inline-link inline-link--medium inline-link--secondary" href="https://www.sap.com/design-system/fiori-design-web/v1-151/ui-elements/toast-web-component/usage" target="_blank" rel="noopener">SAP Fiori</a>, <a class="inline-link inline-link--medium inline-link--secondary" href="https://material.io/components/snackbars" target="_blank" rel="noopener">Material</a> treat routine confirmations. It does not cover Inline: the Inline row is a recommendation.') + \
    '<h3 class="ds-h3">Default and exception per component</h3>' + table(['Component', 'Default', 'Strong only when'], [
        ['Toast', 'Weak: normal feedback, “Saved”, “Copied”, “Could not save – try again”', 'Exceptionally, when the feedback needs extra visual attention. Never for a critical interruption or anything the user must notice or act on: use a Banner, or an Inline notification near the content.'],
        ['Banner', 'Weak (Weaker for general information and offers)', 'A critical outage, a blocked main flow, risk of data loss, or anything that needs immediate attention.'],
        ['Inline', 'Weak', 'The same as Banner, when it blocks a central flow in that area (recommendation).']]) + \
    '<h3 class="ds-h3">Weak or Strong for a warning or an error</h3>' + desc('<strong>Weak:</strong> an ordinary warning or error that can be handled locally, such as a failed action that can be tried again, or something the user must correct. <strong>Strong:</strong> a critical outage, a blocked main flow, risk of data loss, or anything that needs immediate attention.') + \
    '<h3 class="ds-h3">A toast disappears</h3>' + desc('If the message must be noticed, must stay, or needs an action, it does not belong in a toast. Show it as a Banner, or near the affected content. For critical or blocking information choose a persistent notification type; do not make a temporary toast louder.') + \
    '<h3 class="ds-h3">Which one</h3>' + desc('Ask in this order and take the first yes.') + \
    '<ol class="ds-bullets ds-bullets--num">' + ''.join('<li><strong>%s</strong> %s</li>' % x for x in [('Is it normal feedback on something the user just did?', 'Including “Could not save – try again”. Toast, Weak.'), ('Must the user notice it, act on it, or be able to read it again?', 'Not a toast. An Inline notification near the content, or a Banner.'), ('Is it general information or an offer?', 'Banner, Weaker.'), ('Is it an ordinary warning or error that can be handled locally?', 'Weak.'), ('Is it a critical outage, a blocked main flow, risk of data loss, or does it need immediate attention?', 'Strong. A Banner; a Toast only exceptionally.')]) + '</ol>' + \
    '<h3 class="ds-h3">Rules</h3>' + bullets(['<strong>Set the emphasis on purpose</strong>, and keep the same situation at the same emphasis across the product.', '<strong>One loud message at a time.</strong> Never stack Strong banners. Campaigns use the Promotion banner, not a higher emphasis.', '<strong>Emphasis is never the only signal.</strong> The icon and the text always carry the status; color and tint only add to it.'])

dismiss = '<h2 class="ds-h2">Dismissing</h2>' + desc('A notification that does not go away on its own must always be dismissable. A Modal must support all three ways: ×, ESC and a click outside.') + \
    '<div class="ds-table-wrap"><table class="ds-table"><thead><tr><th scope="col">Method</th><th scope="col">Toast</th><th scope="col">E-Com Toast</th><th scope="col">Inline</th><th scope="col">Banner</th><th scope="col">Modal</th></tr></thead><tbody id="dis"></tbody></table></div>' + \
    note('On a Banner, whether the × exists is decided by the administrator or content owner, not by the component.')

action = '<h2 class="ds-h2">In action</h2>' + desc('Fire each component, then three flows where components work together.') + \
    '<h3 class="ds-h3 ds-group">The five components</h3>' + desc('Each button fires that component. Banner and Inline appear under the buttons.') + \
    '<div class="ds-stage"><div class="pg-btns" id="cards"></div></div><div id="banner-slot" style="margin-top:16px"></div>' + \
    '<h3 class="ds-h3 ds-group">Flows</h3>' + desc('Real situations that combine components. Notice that each message uses the quietest component that does the job.') + '<div class="ds-stage pg-demo-stage" id="flows"></div>'

usage = '<h2 class="ds-h2">Usage</h2>' + rules(['Keep task feedback close to where the user is working.', 'Choose the least disruptive component that does the job.', 'Match status icon and status color.', 'Give errors a way forward: a retry, a fix, a link.'],
    ['Use a banner or modal for feedback on a click.', 'Notify when nothing the user cares about changed.', 'Use a notification for a single form field: use the field’s own message.', 'Show several notifications at once for the same event.'])

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets">' + ''.join('<li><strong>%s</strong>. %s</li>' % (link_large(h, n), t) for h, n, t in [
    ('toast.html', 'Toast', 'Short-lived feedback on something the user just did.'), ('toast-ecom.html', 'E-Com Toast', 'Confirms a shopping action.'), ('modal.html', 'Modal', 'A decision before the user can go on.'),
    ('banner.html', 'Banner', 'A message for the whole page or system.'), ('inline.html', 'Inline notification', 'Feedback that stays next to the content.')]) + '</ul>'

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.nngroup.com/articles/ten-usability-heuristics/', 'Nielsen Norman Group: 10 Usability Heuristics', 'Visibility of system status, the first heuristic.'),
    ('https://carbondesignsystem.com/components/notification/usage/', 'Carbon Design System: Notification', 'IBM.'),
    ('https://spectrum.adobe.com/page/toast', 'Adobe Spectrum: Toast', 'Adobe.'),
    ('https://material.io/components/snackbars', 'Material Design: Snackbars', 'Google.')])

secs = [('choose', choose), ('matrix', matrix), ('status', status), ('dismiss', dismiss), ('action', action), ('usage', usage), ('related', related), ('references', references)]

JS = JS_PRE + r'''
  /* Triggers, shared by the chooser and the cards */
  var T = {
    toast: function () { N.showToast({ status: 'success', emphasis: 'weak', text: 'Settings saved.', autoHide: 4000 }); },
    ecom: function () { N.showEcomToast({ variant: 'cart', name: 'Carpenter Soul work pants stretch black', text: 'has been added to the cart.', img: IMG, secondary: { label: 'Choose accessories' }, primary: { label: 'Go to cart' } }); },
    modal: function () { N.openModal({ size: 'small', title: 'Delete this address?', body: 'The address is removed from your address book.', cancel: 'Cancel', confirm: 'Delete' }); },
    banner: function () { var s = clear($('#banner-slot')); s.appendChild(mk(H.banner({ size: 'small', status: 'warning', emphasis: 'weak', title: 'Planned maintenance', text: 'The site is unavailable on Sunday 02:00–04:00.' }))); s.scrollIntoView({ block: 'nearest', behavior: 'smooth' }); },
    inline: function () { var s = clear($('#banner-slot')); s.appendChild(mk(H.inline({ size: 'large', status: 'error', emphasis: 'strong', title: 'Payment declined', text: 'Check your card details.', secondary: 'Change card', primary: 'Try again' }))); s.scrollIntoView({ block: 'nearest', behavior: 'smooth' }); }
  };
  var COMP = {
    toast: { n: 'Toast', u: 'toast.html', why: 'A brief confirmation of what the user just did, away from the content so nothing is blocked. It leaves by itself.', prev: function () { return H.toast({ status: 'success', emphasis: 'weak', text: 'Settings saved.' }); }, trig: 'Show toast' },
    ecom: { n: 'E-Com Toast', u: 'toast-ecom.html', why: 'A brief confirmation of a shopping action, with the natural next steps for the shopper.', prev: function () { return H.ecom({ variant: 'info', name: 'Belt stretch black', text: 'added to your wishlist.', link: 'View' }); }, trig: 'Show toast' },
    inline: { n: 'Inline', u: 'inline.html', why: 'Feedback that belongs to one section or form and must stay visible until the user acts or the state changes.', prev: function () { return H.inline({ size: 'large', status: 'warning', emphasis: 'strong', text: 'That password is easy to guess.' }); }, trig: 'Show inline' },
    banner: { n: 'Banner', u: 'banner.html', why: 'A message from the system or an administrator about the whole page, site or a customer group, set at the top.', prev: function () { return H.banner({ size: 'small', status: 'warning', emphasis: 'weak', title: 'Planned maintenance', text: 'The site is unavailable on Sunday.' }); }, trig: 'Show banner' },
    modal: { n: 'Modal', u: 'modal.html', why: 'The user must decide before going on. It blocks the page, so it is the last resort.', prev: function () { return null; }, trig: 'Open modal' }
  };
  var q = { block: 'no', origin: 'task', shop: 'no', life: 'brief' };
  function pick() {
    if (q.block === 'yes') return 'modal';
    if (q.origin === 'system') return 'banner';
    if (q.life === 'stay') return 'inline';
    return q.shop === 'yes' ? 'ecom' : 'toast';
  }
  function res() {
    $('#q2').hidden = q.block === 'yes'; $('#q3').hidden = q.block === 'yes' || q.origin === 'system'; $('#q4').hidden = q.block === 'yes' || q.origin === 'system';
    var k = pick(), c = COMP[k], h = clear($('#res'));
    h.innerHTML = '<span class="ds-toolbar__label">Use</span><h3></h3><p></p><div class="pg-prev"></div><div class="pg-actions"></div>';
    $('h3', h).textContent = c.n; $('p', h).textContent = c.why;
    var pv = c.prev(), box = $('.pg-prev', h);
    if (pv) box.appendChild(mk(pv)); else { box.textContent = 'A dialog over a dimmed page. Press the button to open the real one.'; box.style.fontSize = '14px'; }
    var b = document.createElement('button'); b.type = 'button'; b.className = 'btn btn--primary btn--sm'; b.innerHTML = '<span class="btn__label"></span>'; $('span', b).textContent = c.trig;
    b.addEventListener('click', function () { T[k](); }); $('.pg-actions', h).appendChild(b);
    var a = document.createElement('a'); a.href = c.u; a.className = 'btn btn--secondary btn--sm'; a.innerHTML = '<span class="btn__label"></span>'; $('span', a).textContent = 'Open ' + c.n + ' page'; a.style.textDecoration = 'none'; $('.pg-actions', h).appendChild(a);
  }
  $$('[data-q]').forEach(function (g) { DK.seg(g, function (v) { q[g.dataset.q] = v; res(); }); });

  DK.rows($('#mtx'), [
    ['<a href="banner.html" class="inline-link inline-link--small">Banner</a>', 'Medium, at the top', 'System', 'Global or product-level messages: maintenance, outage, campaigns, notices to a customer group.', 'All four, plus Promotion'],
    ['<a href="inline.html" class="inline-link inline-link--small">Inline</a>', 'Low, embedded', 'Task', 'Contextual feedback or status in the region of active work.', 'All four'],
    ['<a href="toast.html" class="inline-link inline-link--small">Toast</a>', 'Low, slides in', 'Task', 'Brief, transient confirmation that needs minimal interaction.', 'All four'],
    ['<a href="toast-ecom.html" class="inline-link inline-link--small">E-Com Toast</a>', 'Low, slides in', 'Task', 'Add to cart, wishlist or brief shopping information.', 'None (brand black and white)'],
    ['<a href="modal.html" class="inline-link inline-link--small">Modal</a>', 'High, blocks the page', 'Either', 'Crucial information or a decision needed before the user can go on.', 'None']]);
  [['info', 'Informational', 'info', 'information', 'Neutral guidance, status, helpful context.'], ['success', 'Success', 'check_circle', 'success', 'A completed or confirmed outcome.'], ['warning', 'Warning', 'warning', 'warning', 'Something to be careful about; not a failure.'], ['error', 'Error', 'error', 'danger', 'A failure or a blocking problem.']].forEach(function (s) {
    DK.rows($('#stat'), [[s[1], '<span class="material-symbols-outlined" aria-hidden="true" style="font-size:24px;color:var(--color-surface-' + s[3] + '-default)">' + s[2] + '</span> <code>' + s[2] + '</code>', '<span class="ds-dot" aria-hidden="true" style="background:var(--color-surface-' + s[3] + '-default)"></span><code>surface-' + s[3] + '-default</code>', s[4]]]);
  });
  DK.rows($('#emph'), [['Banner', 'Strong, Weak, Weaker; Promotion: Dark, Light, Strong, Weak', 'Small, Large (Large: My Pages only)', 'Default'], ['Inline', 'Strong, Weak', 'Large, Small', 'Default, Actionable (Large)'],
    ['Toast', 'Strong, Weak', 'One', 'Default, Actionable'], ['E-Com Toast', 'None', 'One', 'Add to cart, Informational'], ['Modal', 'None', 'Small, Large', 'Label optional']]);
  DK.rows($('#dis'), [['× close icon', '<b class="pg-ok">Yes</b>', '<b class="pg-ok">Yes</b>', '<b class="pg-ok">Yes</b>', '<b class="pg-ok">Yes</b> (if the owner allows)', '<b class="pg-ok">Always</b>'],
    ['Click outside', '<b class="pg-ok">Yes</b>', '<b class="pg-ok">Yes</b>', '<span class="ds-na">No</span>', '<span class="ds-na">No</span>', '<b class="pg-ok">Always</b>'],
    ['ESC key', '<span class="ds-na">No</span>', '<span class="ds-na">No</span>', '<span class="ds-na">No</span>', '<span class="ds-na">No</span>', '<b class="pg-ok">Always</b>'],
    ['Auto-dismiss', '<b class="pg-ok">Yes</b> (4 s)', '<b class="pg-ok">Yes</b> (4 s)', '<span class="ds-na">No</span>', '<span class="ds-na">No</span>', '<span class="ds-na">No</span>']]);

  [['toast', 'Toast'], ['ecom', 'E-Com Toast'], ['modal', 'Modal'], ['banner', 'Banner'], ['inline', 'Inline']].forEach(function (c) {
    var b = document.createElement('button'); b.type = 'button'; b.className = 'btn btn--primary btn--sm'; b.innerHTML = '<span class="btn__label"></span>'; $('span', b).textContent = c[1]; b.addEventListener('click', T[c[0]]); $('#cards').appendChild(b);
  });

  /* Flows */
  var fl = $('#flows');
  function flow(title, desc, label, cls, run) {
    var w = document.createElement('div'); w.className = 'pg-flow-row'; w.innerHTML = '<div><b></b><span></span></div>';
    $('b', w).textContent = title; $('span', w).textContent = desc;
    var b = document.createElement('button'); b.type = 'button'; b.className = 'btn btn--sm ' + cls; b.innerHTML = '<span class="btn__label"></span>'; $('span', b).textContent = label; b.addEventListener('click', run); w.appendChild(b); fl.appendChild(w);
  }
  flow('Add to cart → E-Com Toast', 'A shopping action, short-lived, with next steps.', 'Add to cart', 'btn--primary', T.ecom);
  flow('Delete account → Modal → Toast', 'A destructive action needs a decision (Modal). The result is brief feedback (Toast).', 'Delete account', 'btn--secondary', function () {
    N.openModal({ size: 'small', title: 'Delete your account?', body: 'Your orders and addresses are deleted. This cannot be undone.', cancel: 'Cancel', confirm: 'Delete account',
      onConfirm: function () { setTimeout(function () { N.showToast({ status: 'success', emphasis: 'weak', text: 'Your account was deleted.', autoHide: 4000 }); }, 200); } }); });
  flow('Subscribe → Inline', 'Feedback tied to a form stays next to the form (Inline), not in a corner. Press twice to see both results.', 'Subscribe', 'btn--secondary', (function () {
    var ok = false; return function () {
      var slot = $('#flow-inline'); if (!slot) { slot = document.createElement('div'); slot.id = 'flow-inline'; slot.setAttribute('aria-live', 'polite'); fl.appendChild(slot); }
      ok = !ok; clear(slot).appendChild(mk(ok ? H.inline({ size: 'large', status: 'error', emphasis: 'strong', title: 'Invalid email', text: 'Enter an address like name@company.com.' }) : H.inline({ size: 'large', status: 'success', emphasis: 'strong', text: 'You are subscribed. Check your inbox to confirm.' })));
    }; })());

  res();
'''

C = dict(slug=SLUG, title='Notifications', eyebrow='Components · Notifications', pre_css=PRE, css=['menu'], style=STYLE, head_js=[], body_js=['../notifications.js?v=12'], select_menu=False,
    lead='Notifications tell users that something changed. Five components cover it, from a toast that vanishes in four seconds to a modal that stops the page. <strong>The skill is choosing the right one</strong>, and as <em>quiet</em> a one as the situation allows.',
    lead_ex='Use the chooser below, then open the page for the component: ' + ', '.join(lead_link(h, n) for h, n in [('toast.html', 'Toast'), ('toast-ecom.html', 'E-Com Toast'), ('modal.html', 'Modal'), ('banner.html', 'Banner'), ('inline.html', 'Inline')]) + '. Specification: <code>' + GUIDE + '</code>.',
    lead_spec='', lead_code='', ex=secs, spec=[], code=[])


def hub():
    c = C
    tail = '<script src="../doc-kit.js"></script>\n<script src="../notifications.js?v=12"></script>\n<script>\n(function () {\n  var $ = DK.$, $$ = DK.$$, clear = DK.clear, esc = DK.esc;\n%s\n})();\n</script>\n<script src="../tailwind-note.js"></script>\n<script src="../toc.js"></script>\n<script src="../subnav.js"></script>\n' % JS
    return '%s\n<body data-ds="component">\n<script src="../docnav.js"></script>\n%s\n\n%s\n\n<div class="ds-doc" data-subnav="tabs">\n%s\n</div>\n\n%s</body>\n</html>\n' % (
        build.head(c, 'ex'), build.crumbs(c, 'ex'), build.intro(c, 'ex'), build.sections(secs), tail)


if __name__ == '__main__':
    import os
    p = os.path.join(build.OUT, 'notifications.html')
    if os.path.exists(p) and '--force' not in sys.argv:
        print('exists, skipped (use --force to overwrite):', p)
    else:
        open(p, 'w').write(hub()); print('wrote', p)
