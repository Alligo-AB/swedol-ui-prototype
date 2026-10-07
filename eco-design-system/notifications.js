/* ══════════════════════════════════════════════════════════════
   ECO notifications: runtime for Toast, E-Com Toast and Modal, plus the
   close button of Banner and Inline. Pairs with notifications.css.
   Exposes window.ECO_N = { showToast, showEcomToast, openModal, dismissToast }.
   The Code sections on the doc pages print the blocks below.
   ══════════════════════════════════════════════════════════════ */

// @section runtime
(function (w) {
  var ICON = { info: 'info', success: 'check_circle', warning: 'warning', error: 'error' };
  var reduce = function () { return w.matchMedia && w.matchMedia('(prefers-reduced-motion: reduce)').matches; };
  var current = null;

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }
  function icon(name, cls) { var s = el('span', 'material-symbols-outlined' + (cls ? ' ' + cls : ''), name); s.setAttribute('aria-hidden', 'true'); return s; }
  /* Close = Blank icon button; Blank Inverted on dark and solid surfaces */
  function closeBtn(inverted, label) {
    var b = el('button', 'icon-btn icon-btn--close' + (inverted ? ' icon-btn--close-inverted' : '')); b.type = 'button'; b.setAttribute('aria-label', label || 'Close');
    var i = el('span', 'btn__icon', 'close'); i.setAttribute('aria-hidden', 'true'); b.appendChild(i); return b;
  }
  function button(cfg, cls, after) {
    var b = el('button', 'btn ' + cls); b.type = 'button'; b.appendChild(el('span', 'btn__label', cfg.label));
    b.addEventListener('click', function () { if (cfg.onClick) cfg.onClick(); if (after) after(); });
    return b;
  }

  /* Toasts live in one fixed host (top right; xs: top, full width). One toast at a time. */
  function present(node, opts) {
    if (current) current.dismiss(true);
    var host = document.querySelector('.toast-host');
    if (!host) { host = el('div', 'toast-host'); document.body.appendChild(host); }
    host.classList.toggle('toast-host--wide', !!opts.wide);
    host.setAttribute('role', 'status'); host.setAttribute('aria-live', 'polite');
    var done = false, timer = null;
    function outside(e) { if (!node.contains(e.target)) dismiss(); }
    function dismiss(now) {
      if (done) return; done = true;
      clearTimeout(timer); document.removeEventListener('click', outside);
      if (current === handle) current = null;
      if (now || reduce()) { node.remove(); return; }
      node.classList.remove('is-entering'); node.classList.add('is-leaving');
      /* never remove() without animating out: wait for the exit animation, whose length is the duration token in the CSS */
      var ms = parseFloat(getComputedStyle(node).animationDuration) * 1000 || 0;
      setTimeout(function () { node.remove(); }, ms + 20);
    }
    var handle = { dismiss: dismiss, el: node };
    node.classList.add('is-entering');
    host.appendChild(node);
    current = handle;
    setTimeout(function () { document.addEventListener('click', outside); }, 0);  /* the click that opened it must not close it */
    if (opts.autoHide) timer = setTimeout(dismiss, opts.autoHide);
    return handle;
  }

  /* System toast. actions: buttons { primary:{label,onClick}, secondary:{…} } OR inline links { links:[{label,onClick}, …] } makes it Actionable. */
  function showToast(o) {
    var status = o.status || 'info', t = el('div', 'toast toast--' + status + ' toast--' + (o.emphasis || 'strong'));
    var inner = el('div', 'toast__inner'), row = el('div', 'toast__row'), body = el('div', 'toast__body');
    row.appendChild(o.icon && status === 'info' ? icon(o.icon, 'toast__icon icon-outline') : icon(ICON[status], 'toast__icon'));
    if (o.title) body.appendChild(el('p', 'toast__title', o.title));
    body.appendChild(el('p', 'toast__text', o.text || ''));
    row.appendChild(body);
    var x = closeBtn(); row.appendChild(x); inner.appendChild(row); t.appendChild(inner);
    var h = present(t, { autoHide: o.autoHide });
    x.addEventListener('click', function () { h.dismiss(); });
    var a = o.actions;
    if (a) {
      var box = el('div', 'toast__actions');
      if (a.primary || a.secondary) {
        var btns = el('div', 'toast__btns');
        if (a.secondary) btns.appendChild(button(a.secondary, 'btn--secondary', h.dismiss));
        if (a.primary) btns.appendChild(button(a.primary, 'btn--primary', h.dismiss));
        box.appendChild(btns);
      }
      var ls = a.links || (a.link ? [a.link] : []);
      if (ls.length) {
        var lk = el('div', 'toast__links');
        ls.forEach(function (it) { var l = el('button', 'inline-link inline-link--medium', it.label); l.type = 'button'; l.addEventListener('click', function () { if (it.onClick) it.onClick(); h.dismiss(); }); lk.appendChild(l); });
        box.appendChild(lk);
      }
      inner.appendChild(box);
    }
    return h;
  }

  /* E-Com toast. variant 'cart' (image + two buttons) or 'info' (black, text + optional link). */
  function showEcomToast(o) {
    var cart = (o.variant || 'cart') === 'cart', t = el('div', 'ecom-toast ecom-toast--' + (cart ? 'cart' : 'info'));
    var name = el('span', 'ecom-toast__name', o.name), desc = el('span', '', ' ' + (o.text || ''));
    var x = closeBtn(!cart);
    if (cart) {
      var head = el('div', 'ecom-toast__header'), it = el('div', 'ecom-toast__image-text'), p = el('p', 'ecom-toast__text');
      var img = el('img', 'ecom-toast__img'); img.src = o.img || ''; img.alt = '';
      p.appendChild(name); p.appendChild(desc); it.appendChild(img); it.appendChild(p); head.appendChild(it); head.appendChild(x); t.appendChild(head);
    } else {
      var c = el('div', 'ecom-toast__info-content'), q = el('p', 'ecom-toast__info-text');
      q.appendChild(name); q.appendChild(desc); c.appendChild(q); t.appendChild(c); t.appendChild(x);
    }
    var h = present(t, { autoHide: o.autoHide == null ? 4000 : o.autoHide, wide: cart });
    x.addEventListener('click', function () { h.dismiss(); });
    if (cart && (o.primary || o.secondary)) {
      var f = el('div', 'ecom-toast__footer');
      if (o.secondary) f.appendChild(button(o.secondary, 'btn--blank', h.dismiss));
      if (o.primary) f.appendChild(button(o.primary, 'btn--primary', h.dismiss));
      t.appendChild(f);
    }
    if (!cart && o.link) {
      var l = el('button', 'inline-link inline-link--medium', o.link.label); l.type = 'button';
      l.addEventListener('click', function () { if (o.link.onClick) o.link.onClick(); h.dismiss(); });
      t.querySelector('.ecom-toast__info-content').appendChild(l);
    }
    return h;
  }

  /* Modal. Always closes with ×, ESC and a click on the overlay. Traps Tab, locks scroll, returns focus. */
  var modalSeq = 0;
  function openModal(o) {
    var opener = document.activeElement, id = 'modal-title-' + (++modalSeq);
    var ov = el('div', 'modal-overlay'), m = el('div', 'modal modal--' + (o.size || 'small'));
    m.setAttribute('role', 'dialog'); m.setAttribute('aria-modal', 'true'); m.setAttribute('aria-labelledby', id); m.tabIndex = -1;
    var content = el('div', 'modal__content'), head = el('div', 'modal__header'), ht = el('div', 'modal__header-text');
    if (o.label) ht.appendChild(el('p', 'modal__label', o.label));
    var title = el('h2', 'modal__title', o.title); title.id = id; ht.appendChild(title);
    var x = closeBtn(); head.appendChild(ht); head.appendChild(x); content.appendChild(head);
    content.appendChild(el('p', 'modal__body', o.body || ''));
    var foot = el('div', 'modal__footer'), cancel = button({ label: o.cancel || 'Cancel' }, 'btn--blank'), ok = button({ label: o.confirm || 'Confirm' }, 'btn--primary');
    foot.appendChild(cancel); foot.appendChild(ok); m.appendChild(content); m.appendChild(foot);
    var closed = false;
    function close(reason) {
      if (closed) return; closed = true;
      document.removeEventListener('keydown', key);
      ov.remove(); m.remove(); document.body.classList.remove('has-modal');
      if (opener && opener.focus) opener.focus();
      if (o.onClose) o.onClose(reason);
    }
    function key(e) {
      if (e.key === 'Escape') { e.preventDefault(); close('esc'); return; }
      if (e.key !== 'Tab') return;
      var f = m.querySelectorAll('button'); if (!f.length) return;
      var first = f[0], last = f[f.length - 1];
      if (e.shiftKey && (document.activeElement === first || document.activeElement === m)) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
    x.addEventListener('click', function () { close('close'); });
    ov.addEventListener('click', function () { close('overlay'); });
    cancel.addEventListener('click', function () { close('cancel'); });
    ok.addEventListener('click', function () { if (o.onConfirm) o.onConfirm(); close('confirm'); });
    document.addEventListener('keydown', key);
    document.body.classList.add('has-modal'); document.body.appendChild(ov); document.body.appendChild(m); m.focus();
    return { close: close, el: m };
  }

  /* Banner and Inline: the × hides the notification (the owner decides if it shows at all). */
  document.addEventListener('click', function (e) {
    var b = e.target.closest('.icon-btn--close'); if (!b) return;
    var n = b.closest('.banner-notification, .inline-notification'); if (!n) return;
    if (n.classList.contains('is-closing')) return;
    function done() { n.classList.remove('is-closing', 'is-collapsing'); n.style.height = ''; n.hidden = true; n.dispatchEvent(new CustomEvent('n-dismissed', { bubbles: true })); }
    if (reduce()) { done(); return; }
    var ms = parseFloat(getComputedStyle(n).transitionDuration) * 1000 || 0;  /* --n-close-duration */
    n.classList.add('is-closing');  /* fade out */
    if (!n.closest('[data-n-close="fade"]')) { n.style.height = n.offsetHeight + 'px'; n.offsetHeight; n.classList.add('is-collapsing'); n.style.height = '0px'; }  /* collapse: pin the start height so it can animate to 0 */
    setTimeout(done, ms + 20);
  });

  w.ECO_N = { showToast: showToast, showEcomToast: showEcomToast, openModal: openModal, dismissToast: function () { if (current) current.dismiss(); } };
})(window);
// @end runtime

// @section markup
/* Markup builders: the same HTML for the live example and for the "markup for this selection" code. */
(function (w) {
  var ICON = { info: 'info', success: 'check_circle', warning: 'warning', error: 'error' };
  function e(t) { return String(t == null ? '' : t).replace(/&/g, '&amp;').replace(/</g, '&lt;'); }
  function X(inv) { return '<button type="button" class="icon-btn icon-btn--close' + (inv ? ' icon-btn--close-inverted' : '') + '" aria-label="Close"><span class="btn__icon" aria-hidden="true">close</span></button>'; }
  /* Inline links of an action area: o.links = ['A', 'B'] (or the single o.link). Buttons OR links: use one of them. */
  function links(o) { return o.links && o.links.length ? o.links : (o.link ? [o.link] : []); }
  function LK(list, cls, pad, tag, size) {
    var lc = 'inline-link inline-link--' + (size || 'medium');
    if (size === 'small' && cls === 'banner-notification__links') lc += ' inline-link--bold';  /* system banners: Small Bold */
    if (!list.length) return '';
    return pad + '<div class="' + cls + '">\n' + list.map(function (t) { return pad + '  ' + (tag === 'a' ? '<a href="#" class="' + lc + '">' : '<button type="button" class="' + lc + '">') + e(t) + (tag === 'a' ? '</a>' : '</button>') + '\n'; }).join('') + pad + '</div>\n';
  }
  function B(v, label) { return '<button type="button" class="btn btn--' + v + '"><span class="btn__label">' + e(label) + '</span></button>'; }
  /* Status icon: the default is the filled status symbol. Only Informational may take an icon chosen by the user,
     and that one is the OUTLINE variant, not the filled one. */
  function sic(o, s, cls) {
    return (o.icon && s === 'info') ? ic(o.icon, cls + ' icon-outline') : ic(ICON[s], cls);
  }
  function ic(name, cls) { return '<span class="material-symbols-outlined' + (cls ? ' ' + cls : '') + '" aria-hidden="true">' + e(name) + '</span>'; }

  /* o: { status, emphasis, title, text, primary, secondary, link } (button/link labels as strings) */
  function toast(o) {
    var s = o.status || 'info', act = o.primary || o.secondary || links(o).length, h = '';
    h += '<div class="toast toast--' + s + ' toast--' + (o.emphasis || 'strong') + '">\n  <div class="toast__inner">\n    <div class="toast__row">\n      ' + sic(o, s, 'toast__icon') + '\n      <div class="toast__body">\n';
    if (o.title) h += '        <p class="toast__title">' + e(o.title) + '</p>\n';
    h += '        <p class="toast__text">' + e(o.text) + '</p>\n      </div>\n      ' + X() + '\n    </div>\n';
    if (act) {
      h += '    <div class="toast__actions">\n';
      if (o.primary || o.secondary) {
        h += '      <div class="toast__btns">\n';
        if (o.secondary) h += '        ' + B('secondary', o.secondary) + '\n';
        if (o.primary) h += '        ' + B('primary', o.primary) + '\n';
        h += '      </div>\n';
      }
      h += LK(links(o), 'toast__links', '      ');
      h += '    </div>\n';
    }
    return h + '  </div>\n</div>';
  }

  /* o: { variant:'cart'|'info', name, text, img, primary, secondary, link } */
  function ecom(o) {
    if ((o.variant || 'cart') === 'info') {
      return '<div class="ecom-toast ecom-toast--info">\n  <div class="ecom-toast__info-content">\n    <p class="ecom-toast__info-text"><span class="ecom-toast__name">' + e(o.name) + '</span> ' + e(o.text) + '</p>\n' +
        (o.link ? '    <button type="button" class="inline-link inline-link--medium">' + e(o.link) + '</button>\n' : '') + '  </div>\n  ' + X(true) + '\n</div>';
    }
    return '<div class="ecom-toast ecom-toast--cart">\n  <div class="ecom-toast__header">\n    <div class="ecom-toast__image-text">\n      <img class="ecom-toast__img" src="' + e(o.img || '') + '" alt="" />\n      <p class="ecom-toast__text"><span class="ecom-toast__name">' + e(o.name) + '</span> ' + e(o.text) + '</p>\n    </div>\n    ' + X() + '\n  </div>\n  <div class="ecom-toast__footer">\n' +
      (o.secondary ? '    ' + B('blank', o.secondary) + '\n' : '') + (o.primary ? '    ' + B('primary', o.primary) + '\n' : '') + '  </div>\n</div>';
  }

  /* o: { size:'small'|'large'|'promotion', status, emphasis, icon, title, text, heading, body, primary, secondary, link, closable (Banner and Inline) } */
  function banner(o) {
    var s = o.status || 'info', strong = o.emphasis === 'strong' || o.emphasis === 'dark', cl = o.closable === false ? '' : X(strong);
    if (o.size === 'promotion') {
      return '<div class="banner-notification banner-notification--promotion banner-notification--' + (o.emphasis || 'dark') + '">\n  <p class="banner-notification__promo"><span class="banner-notification__title">' + e(o.title) + '</span> <a href="#" class="inline-link inline-link--medium">' + e(o.link) + '</a></p>\n  ' + cl + '\n</div>';
    }
    var base = 'banner-notification' + (o.size === 'large' ? ' banner-notification--large' : '') + ' banner-notification--' + s + ' banner-notification--' + (o.emphasis || 'weak');
    if (o.size === 'large') {
      return '<div class="' + base + '">\n  <div class="banner-notification__left-border"></div>\n  <div class="banner-notification__inner">\n    <div class="banner-notification__main">\n      ' + sic(o, s, 'banner-notification__icon') + '\n      <div class="banner-notification__textblock">\n        <p class="banner-notification__heading">' + e(o.heading) + '</p>\n        <p class="banner-notification__body">' + e(o.body) + '</p>\n      </div>\n      ' + cl + '\n    </div>\n' +
        ((o.primary || o.secondary || links(o).length) ? '    <div class="banner-notification__footer">\n' + ((o.primary || o.secondary) ? '      <div class="banner-notification__btns">\n' + (o.secondary ? '        ' + B(strong ? 'secondary-inverted' : 'secondary', o.secondary) + '\n' : '') + (o.primary ? '        ' + B(strong ? 'blank-inverted' : 'blank', o.primary) + '\n' : '') + '      </div>\n' : '') + LK(links(o), 'banner-notification__links', '      ', 'a') + '    </div>\n' : '') + '  </div>\n</div>';
    }
    return '<div class="' + base + '">\n  <div class="banner-notification__base">\n    <div class="banner-notification__left-border"></div>\n    <div class="banner-notification__container">\n      <div class="banner-notification__inner">\n        <div class="banner-notification__content">\n          ' + sic(o, s, 'banner-notification__icon') + '\n          <p class="banner-notification__text">' + (o.title ? '<span class="banner-notification__title">' + e(o.title) + ':</span> ' : '') + e(o.text) + '</p>\n' + LK(links(o), 'banner-notification__links', '          ', 'a', 'small') + '        </div>\n        ' + cl + '\n      </div>\n    </div>\n  </div>\n</div>';
  }

  /* o: { size:'large'|'small', status, emphasis, icon, title, text, primary, secondary, link } */
  function inline(o) {
    var s = o.status || 'info', cls = 'inline-notification inline-notification--' + s + ' inline-notification--' + (o.emphasis || 'strong') + (o.size === 'small' ? ' inline-notification--small' : ''), act = o.size !== 'small' && (o.primary || o.secondary || links(o).length);
    return '<div class="' + cls + '">\n  <div class="inline-notification__base">\n    <div class="inline-notification__left-border"></div>\n    <div class="inline-notification__container">\n      <div class="inline-notification__inner">\n        <div class="inline-notification__header">\n          ' + sic(o, s, 'inline-notification__icon') + '\n          <p class="inline-notification__text">' + (o.title ? '<span class="inline-notification__title">' + e(o.title) + ':</span> ' : '') + e(o.text) + '</p>\n          ' + (o.closable === false ? '' : X()) + '\n        </div>\n' +
      (act ? '        <div class="inline-notification__actions">\n' + ((o.primary || o.secondary) ? '          <div class="inline-notification__btns">\n' + (o.secondary ? '            ' + B('secondary', o.secondary) + '\n' : '') + (o.primary ? '            ' + B('primary', o.primary) + '\n' : '') + '          </div>\n' : '') + LK(links(o), 'inline-notification__links', '          ', 'button', 'small') + '        </div>\n' : '') + '      </div>\n    </div>\n  </div>\n</div>';
  }

  /* o: { size, label, title, body, cancel, confirm } (markup of the open dialog; the overlay is separate) */
  function modal(o) {
    return '<div class="modal-overlay" data-close-modal></div>\n<div class="modal modal--' + (o.size || 'small') + '" role="dialog" aria-modal="true" aria-labelledby="modal-title">\n  <div class="modal__content">\n    <div class="modal__header">\n      <div class="modal__header-text">\n' + (o.label ? '        <p class="modal__label">' + e(o.label) + '</p>\n' : '') + '        <h2 class="modal__title" id="modal-title">' + e(o.title) + '</h2>\n      </div>\n      ' + X() + '\n    </div>\n    <p class="modal__body">' + e(o.body) + '</p>\n  </div>\n  <div class="modal__footer">\n    ' + B('blank', o.cancel || 'Cancel') + '\n    ' + B('primary', o.confirm || 'Confirm') + '\n  </div>\n</div>';
  }
  w.ECO_N = w.ECO_N || {}; w.ECO_N.html = { toast: toast, ecom: ecom, banner: banner, inline: inline, modal: modal };
})(window);
// @end markup
