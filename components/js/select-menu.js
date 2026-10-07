/* ECO select menu behavior (native <select> opens an ECO .menu). Shared by the docs page (components/select.html) and every prototype page.
   Skill: eco-select. Link it, do not copy it: <script src="/components/js/select-menu.js"></script>. Needs /components/css/select.css and menu.css. */
/* Exposed dropdown: a native <select> opens an ECO .menu instead of the browser list.
   The <select> stays the form control (value, label, disabled, :has() active state); this only replaces the popup. */
(function () {
  var open = null;
  function close(focus) {
    if (!open) return;
    open.menu.remove(); open.sel.setAttribute('aria-expanded', 'false');
    if (focus) open.sel.focus();
    open = null;
  }
  function holder(sel) { return sel.closest('.input-wrap'); }
  function openMenu(sel) {
    close();
    var small = /form-select--(sm|xs)/.test(sel.className);
    var menu = document.createElement('div'); menu.className = 'menu' + (small ? ' menu--sm' : '');
    var ul = document.createElement('ul'); ul.className = 'menu__items'; ul.setAttribute('role', 'listbox');
    var l = sel.id && document.querySelector('label[for="' + sel.id + '"]'), by = sel.getAttribute('aria-labelledby') && document.getElementById(sel.getAttribute('aria-labelledby'));
    if (l || by) ul.setAttribute('aria-label', (l || by).textContent);
    Array.prototype.forEach.call(sel.options, function (o) {
      if (o.value === '') return;   /* placeholder option is not a choice */
      var li = document.createElement('li'); li.className = 'menu__item'; li.tabIndex = -1; li.setAttribute('role', 'option');
      li.setAttribute('aria-selected', String(o.selected)); li.dataset.value = o.value;
      if (o.disabled) { li.setAttribute('aria-disabled', 'true'); }
      li.innerHTML = '<span class="menu__item-label"></span><span class="menu__item-icon" aria-hidden="true"></span>';
      li.firstChild.textContent = o.textContent; ul.appendChild(li);
    });
    menu.appendChild(ul); holder(sel).appendChild(menu);
    /* Room check: flip upwards when it does not fit below and there is more room above; else cap the height and scroll */
    var r = sel.getBoundingClientRect(), gap = 12, room = window.innerHeight - r.bottom - gap;
    if (menu.offsetHeight > room && r.top - gap > room) { menu.classList.add('menu--up'); room = r.top - gap; }
    if (menu.offsetHeight > room) ul.style.maxHeight = Math.max(room, 0) + 'px';
    sel.setAttribute('aria-expanded', 'true'); open = { sel: sel, menu: menu };
    (ul.querySelector('[aria-selected="true"]') || ul.querySelector('.menu__item:not([aria-disabled="true"])') || ul.firstChild).focus();
  }
  function choose(li) {
    var sel = open.sel; sel.value = li.dataset.value;
    sel.dispatchEvent(new Event('change', { bubbles: true })); close(true);
  }
  document.addEventListener('mousedown', function (e) {
    var sel = e.target.closest('.form-select');
    if (sel) {
      if (sel.disabled) return;
      e.preventDefault(); sel.focus();
      if (open && open.sel === sel) close(); else openMenu(sel);
    } else if (open && !e.target.closest('.menu')) close();
  });
  document.addEventListener('click', function (e) {
    var li = e.target.closest('.menu__item'); if (li && open && open.menu.contains(li) && li.getAttribute('aria-disabled') !== 'true') choose(li);
  });
  window.addEventListener('resize', function () { close(); });
  document.addEventListener('keydown', function (e) {
    var t = e.target;
    if (open && open.menu.contains(t)) {
      var items = Array.prototype.slice.call(open.menu.querySelectorAll('.menu__item:not([aria-disabled="true"])')), i = items.indexOf(t);
      if (e.key === 'ArrowDown') { e.preventDefault(); (items[i + 1] || t).focus(); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); (items[i - 1] || t).focus(); }
      else if (e.key === 'Home') { e.preventDefault(); items[0].focus(); }
      else if (e.key === 'End') { e.preventDefault(); items[items.length - 1].focus(); }
      else if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); if (t.getAttribute('aria-disabled') !== 'true') choose(t); }
      else if (e.key === 'Escape') { e.preventDefault(); close(true); }
      else if (e.key === 'Tab') close();
    } else if (t.classList && t.classList.contains('form-select') && !t.disabled && /^(Enter| |ArrowDown|ArrowUp)$/.test(e.key)) {
      e.preventDefault(); openMenu(t);
    }
  });
})();
