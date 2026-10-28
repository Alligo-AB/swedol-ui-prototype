/* Filter drawer of the docs pages (tokens.html, components-overview.html). CSS: docs.css ("Filter drawer + filter bar").
   A right-hand drawer at every width, built like the drawers on mypages/users.html (CLAUDE.md "Drawers"); a choice applies at once, the footer button only closes.
   DSFilter.open({ title, lead, body, onChange(drawer) })  body = one or more <fieldset class="tk-filters"> of DSFilter.row(...)
   DSFilter.row(value, label, count, checked)           List Item (eco-list-item): check box + label, count as trailing text tertiary */
(function () {
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;'); }
  function row(value, label, count, checked) {
    return '<div class="tk-row"><div class="list-item" role="checkbox" tabindex="0" aria-checked="' + !!checked + '" data-value="' + esc(value) + '"><span class="list-item__fill"><span class="list-item__check" aria-hidden="true"></span><span class="list-item__label">' + esc(label) + '</span></span><span class="list-item__trail-text list-item__trail-text--tertiary">' + count + '</span></div></div>';
  }
  function toggle(li) { li.setAttribute('aria-checked', String(li.getAttribute('aria-checked') !== 'true')); li.dispatchEvent(new CustomEvent('tk-toggle', { bubbles: true })); }
  document.addEventListener('click', function (e) { var li = e.target.closest('.tk-filters .list-item[role]'); if (li) toggle(li); });
  document.addEventListener('keydown', function (e) { var li = e.target.closest && e.target.closest('.tk-filters .list-item[role]'); if (li && (e.key === ' ' || e.key === 'Enter')) { e.preventDefault(); toggle(li); } });

  function open(o) {   // padding, title size and button sizes follow the users.html drawers per breakpoint
    var mob = !matchMedia('(min-width: 769px)').matches, opener = document.activeElement, still = matchMedia('(prefers-reduced-motion: reduce)').matches, closed = false;
    var ov = document.createElement('div'), d = document.createElement('aside');
    ov.className = 'tk-scrim'; d.className = 'tk-drawer'; d.setAttribute('role', 'dialog'); d.setAttribute('aria-modal', 'true'); d.setAttribute('aria-labelledby', 'tk-dt'); d.tabIndex = -1;
    d.innerHTML = '<div class="tk-drawer__head"><div class="tk-drawer__head-text"><h2 class="tk-drawer__title" id="tk-dt">' + esc(o.title) + '</h2></div><button type="button" class="btn btn--blank btn--' + (mob ? 'md' : 'sm') + ' btn--icon" data-x aria-label="Close"><span class="btn__icon" aria-hidden="true">close</span></button></div>' +
      '<div class="tk-drawer__body">' + (o.lead ? '<p class="tk-drawer__lead">' + esc(o.lead) + '</p>' : '') + o.body + '</div>' +
      '<div class="tk-drawer__foot"><button type="button" class="btn btn--primary btn--' + (mob ? 'lg' : 'sm') + '" data-x><span class="btn__label">Close</span></button></div>';
    var hd = d.querySelector('.tk-drawer__head'), bd = d.querySelector('.tk-drawer__body');
    bd.addEventListener('scroll', function () { hd.classList.toggle('is-elevated', bd.scrollTop > 0); });
    function close() {
      if (closed) return; closed = true; document.removeEventListener('keydown', key);
      ov.classList.add('is-leaving'); d.classList.add('is-leaving');
      var ms = still ? 0 : parseFloat(getComputedStyle(d).animationDuration) * 1000 || 0;
      setTimeout(function () { ov.remove(); d.remove(); }, ms + 20);
      if (opener && opener.focus) opener.focus();
    }
    function key(e) {
      if (e.key === 'Escape') { e.preventDefault(); close(); return; }
      if (e.key !== 'Tab') return;
      var f = [].slice.call(d.querySelectorAll('button, [role=checkbox]')), first = f[0], last = f[f.length - 1];
      if (e.shiftKey && (document.activeElement === first || document.activeElement === d)) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
    d.addEventListener('click', function (e) { if (e.target.closest('[data-x]')) close(); });
    d.addEventListener('tk-toggle', function () { if (o.onChange) o.onChange(d); });
    ov.addEventListener('click', close);
    document.addEventListener('keydown', key);
    document.body.appendChild(ov); document.body.appendChild(d); d.focus();
    return d;
  }
  window.DSFilter = { open: open, row: row, esc: esc };
})();
