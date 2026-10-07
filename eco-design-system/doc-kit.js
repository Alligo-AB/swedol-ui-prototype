/* ECO doc pages: small helpers shared by the notification pages (same behavior as the inline copies on the
   Form component pages). Exposes window.DK. */
(function (w) {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var uid = 0;

  document.addEventListener('keydown', function (e) { if (e.key === 'Tab') document.body.classList.add('keyboard-nav'); });
  document.addEventListener('mousedown', function () { document.body.classList.remove('keyboard-nav'); });

  function clear(n) { n.textContent = ''; return n; }
  function esc(t) { return String(t).replace(/&/g, '&amp;').replace(/</g, '&lt;'); }

  /* Segmented toggle: aria-pressed group, fn(value) on change */
  function seg(g, fn) {
    if (g.tagName === 'SELECT') { g.addEventListener('change', function () { fn(g.value); }); return; }
    g.addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b || b.disabled) return;
      $$('button', g).forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
      fn(b.dataset.v);
    });
  }
  /* Breakpoint preview toggle (Window / Desktop / Mobile) synced across every [data-bp-toggle] group */
  function bp(onChange) {
    $$('[data-bp-toggle]').forEach(function (g) {
      g.addEventListener('click', function (e) {
        var b = e.target.closest('button'); if (!b) return;
        var v = b.dataset.v;
        if (v === 'auto') document.body.removeAttribute('data-bp'); else document.body.setAttribute('data-bp', v);
        $$('[data-bp-toggle]').forEach(function (x) { $$('button', x).forEach(function (y) { y.setAttribute('aria-pressed', String(y.dataset.v === v)); }); });
        if (onChange) onChange(v);
      });
    });
  }
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-copy]'); if (!b) return;
    var txt = document.getElementById(b.dataset.copy).textContent;
    var ic = b.querySelector('.mo-ic'); var done = function () { ic.textContent = 'check'; setTimeout(function () { ic.textContent = 'content_copy'; }, 1200); };
    if (navigator.clipboard) navigator.clipboard.writeText(txt).then(done, done); else done();
  });

  function codeBox(title) {
    var box = document.createElement('div'), id = 'dk' + (uid++);
    box.className = 'ds-code';
    box.innerHTML = '<div class="ds-code__bar"><span></span><button type="button" class="mo-copy" data-copy="' + id + '" aria-label="Copy"><span class="mo-ic" aria-hidden="true">content_copy</span></button></div><pre id="' + id + '"></pre>';
    $('span', box).textContent = title; return box;
  }
  /* recipes(host, [[title, code], …]) */
  function recipes(host, list) {
    list.forEach(function (r) { var b = codeBox(r[0]); $('pre', b).textContent = r[1]; host.appendChild(b); });
  }
  /* Print one `@section name` block of a shared file (notifications.css / .js) into a code box. */
  var files = {};
  function load(url) { return files[url] || (files[url] = fetch(url, { cache: 'no-cache' }).then(function (r) { return r.text(); })); }
  function block(text, name) {
    var m = new RegExp('(?:/\\*|//) @section ' + name + '[^\\n]*\\n([\\s\\S]*?)(?:/\\*|//) @end ' + name).exec(text);
    return m ? m[1].replace(/\s+$/, '') : '/* section "' + name + '" not found */';
  }
  /* printFile(host, url, [[title, [sections…]], …]) */
  function printFile(host, url, list) {
    return load(url).then(function (t) {
      list.forEach(function (it) {
        var b = codeBox(it[0]); $('pre', b).textContent = it[1].map(function (n) { return block(t, n); }).join('\n\n'); host.appendChild(b);
      });
    });
  }
  /* Token table resolved live: rows [mode/state, part, token-without-prefix] */
  function tokenTable(tbody, rows) {
    var cs = getComputedStyle(document.documentElement);
    rows.forEach(function (t) {
      var name = t[2].indexOf('shadow-') === 0 || t[2].indexOf('dimension-') === 0 ? t[2] : 'color-' + t[2];
      var v = cs.getPropertyValue('--' + name).trim(), tr = document.createElement('tr');
      [t[0], t[1]].forEach(function (x, n) { var c = document.createElement(n ? 'td' : 'th'); if (!n) c.scope = 'row'; c.textContent = x; tr.appendChild(c); });
      var tc = document.createElement('td'), code = document.createElement('code'); code.textContent = 'var(--' + name + ')'; tc.appendChild(code); tr.appendChild(tc);
      var vc = document.createElement('td');
      if (name.indexOf('color-') === 0) { var dot = document.createElement('span'); dot.className = 'ds-dot'; dot.style.background = 'var(--' + name + ')'; dot.setAttribute('aria-hidden', 'true'); vc.appendChild(dot); }
      vc.appendChild(document.createTextNode(v || 'missing')); tr.appendChild(vc); tbody.appendChild(tr);
    });
  }
  /* Plain table row builder: rows of strings; first cell is a row header. Cells may contain simple HTML. */
  function rows(tbody, list) {
    list.forEach(function (r) {
      var tr = document.createElement('tr');
      r.forEach(function (x, n) { var c = document.createElement(n ? 'td' : 'th'); if (!n) c.scope = 'row'; c.innerHTML = x; tr.appendChild(c); });
      tbody.appendChild(tr);
    });
  }

  /* Motion section for a component page: its own section after `opts.anchor` (a section id) with a preview stage, sliders for
     Easing and Duration (every eco-motion token), a switch for Height collapse and a table of the chosen tokens and values.
     Applied live to the stage through --<prefix>-ease / --<prefix>-duration and data-<prefix>="fade".
     opts: { anchor, prefix, rec: {ease, dur, collapse}, collapse, why, role: 'exit', preview(): element }. Several motions on one page (e.g. Toast enter + exit): parts: [{ title, prefix, rec: {ease, dur}, exit }] replaces prefix/rec; show(): fires the real component (fixed in the window) instead of preview(), and the vars are set on <html>. role 'exit' adds the warnings table and a live warning. rec = the recommended default for this
     component, marked * and shown in the table. The sections after the new one swap their background so they keep alternating. */
  var EASE = [['decelerate-generic', 'Decelerate'], ['decelerate-emphasized', 'Decelerate emphasized'], ['standard', 'Standard'], ['accelerate-generic', 'Accelerate']];
  var DUR = [['fast-1', 'Fast 1', 50], ['fast-2', 'Fast 2', 100], ['fast-3', 'Fast 3', 150], ['fast-4', 'Fast 4', 200], ['medium-1', 'Medium 1', 250], ['medium-2', 'Medium 2', 300], ['medium-3', 'Medium 3', 350], ['medium-4', 'Medium 4', 400], ['slow-1', 'Slow 1', 450], ['slow-2', 'Slow 2', 500], ['slow-3', 'Slow 3', 550], ['slow-4', 'Slow 4', 600]];
  function motion(opts) {
    var parts = opts.parts || [{ title: '', prefix: opts.prefix, rec: opts.rec, exit: opts.role === 'exit' }];
    parts.forEach(function (pt) { pt.rec = { ease: pt.rec.ease, dur: pt.rec.dur, collapse: String(pt.rec.collapse !== false) }; pt.st = { ease: pt.rec.ease, dur: pt.rec.dur, collapse: pt.rec.collapse }; });
    var id = 'mo' + (uid++), cs = getComputedStyle(document.documentElement), tb;
    var anchor = document.getElementById(opts.anchor), sec = document.createElement('section');
    sec.className = 'ds-section' + (anchor.classList.contains('ds-section--secondary') ? '' : ' ds-section--secondary'); sec.id = 'motion';
    sec.innerHTML = '<div class="ds-page ds-inner"><h2 class="ds-h2">Motion</h2><p class="ds-desc">Choose easing and duration and close the component to see the motion. Recommended is marked <strong>*</strong>. ' + esc(opts.why || '') + '</p>'
      + '<div class="ds-playground"><div class="ds-stage ds-stage--center" style="align-items:stretch"><div id="mo-host" style="width:100%;align-self:center"></div></div><div class="ds-controls"></div></div>'
      + '<h3 class="ds-h3">Motion for this selection</h3><div class="ds-table-wrap"><table class="ds-table"><thead><tr><th scope="col">Property</th><th scope="col">Token</th><th scope="col">Value</th><th scope="col">Recommended</th></tr></thead><tbody></tbody></table></div></div>';
    var WARN = [
      ['Decelerate easing', function (st) { return st.ease.indexOf('decelerate') === 0; }, 'Decelerate (and emphasized) starts fast and brakes. It is made for elements that enter. When something leaves, use Accelerate.', 'eco-motion: Element disappears = accelerate-generic'],
      ['Slow duration (450 ms or more)', function (st) { return st.dur.indexOf('slow') === 0; }, 'A closing element should be out of the way quickly. Slow durations (450–600 ms) feel sluggish. Stay within Fast, or Medium 2 at the most.', 'eco-motion: Element disappears = fast fade'],
      ['Height: Fade only', function (st) { return st.collapse === 'false'; }, 'The content below jumps up when the fade ends, and the duration only affects the fade. Keep Collapse on unless the space must stay reserved.', 'No gap left behind']
    ];
    if (opts.role === 'exit') {
      var wt = document.createElement('div'); wt.innerHTML = '<h3 class="ds-h3">Recommendations and warnings</h3><p class="ds-desc">When the component is closed or removed. A warning shows under the controls when a choice matches.</p><div class="ds-table-wrap"><table class="ds-table"><thead><tr><th scope="col">Choice</th><th scope="col">Warning</th><th scope="col">Reference</th></tr></thead><tbody></tbody></table></div>';
      WARN.forEach(function (w) { var tr = document.createElement('tr'); [w[0], w[2], w[3]].forEach(function (c, i) { var e = document.createElement(i ? 'td' : 'th'); if (!i) e.scope = 'row'; e.textContent = c; tr.appendChild(e); }); $('tbody', wt).appendChild(tr); });
      $('.ds-inner', sec).appendChild(wt);
    }
    anchor.parentNode.insertBefore(sec, anchor.nextSibling);
    for (var n = sec.nextElementSibling; n && n.tagName === 'SECTION'; n = n.nextElementSibling) if (n.classList.contains('ds-section')) n.classList.toggle('ds-section--secondary');
    var link = document.querySelector('.ds-toc a[href="#' + opts.anchor + '"]');
    if (link) { var li = document.createElement('li'); li.innerHTML = '<a href="#motion">Motion</a>'; link.parentNode.parentNode.insertBefore(li, link.parentNode.nextSibling); }
    var cb = codeBox('Code for this selection'), pre = $('pre', cb), tw0 = $('.ds-table-wrap', sec); tw0.parentNode.insertBefore(cb, tw0.nextSibling);
    var controls = $('.ds-controls', sec), host = $('#mo-host', sec); tb = $('tbody', sec);
    function nameOf(list, v) { return list.filter(function (o) { return o[0] === v; })[0][1]; }
    function slider(pt, pi, title, key, list, tick) {
      var f = document.createElement('div'), ri = id + pi + key, st = pt.st, rec = pt.rec;
      f.className = 'ds-field';
      f.innerHTML = '<div class="form-range" data-range data-labels="' + list.map(function (o) { return key === 'dur' ? o[1] + ' · ' + o[2] + ' ms' : o[1]; }).join('|') + '" data-ticks="' + list.map(tick).join('|') + '" data-recommended="' + list.map(function (o) { return o[0]; }).indexOf(rec[key]) + '">'
        + '<div class="form-range__head"><label class="form-range__label" for="' + ri + '">' + esc(title) + '</label><output class="form-range__value" for="' + ri + '"></output></div>'
        + '<input class="form-range__input" id="' + ri + '" type="range" min="0" max="' + (list.length - 1) + '" step="1" value="' + list.map(function (o) { return o[0]; }).indexOf(st[key]) + '"><div class="form-range__ticks"></div></div>';
      w.ECO_RANGE.init(f);  /* shared component: components/js/range.js + css/range.css */
      $('input', f).addEventListener('input', function (e) { st[key] = list[e.target.value][0]; apply(); });
      return f;
    }
    function row(cells) { var tr = document.createElement('tr'); cells.forEach(function (c, i) { var e = document.createElement(i ? 'td' : 'th'); if (!i) e.scope = 'row'; if (c && c.code) { var k = document.createElement('code'); k.textContent = c.code; e.appendChild(k); } else e.textContent = c; tr.appendChild(e); }); return tr; }
    function apply() {
      var tgt = opts.show ? document.documentElement : host, many = parts.length > 1, code = [], note = [];
      clear(tb); if (warn) clear(warn);
      parts.forEach(function (pt) {
        var st = pt.st, rec = pt.rec, t = pt.title ? pt.title + ' ' : '';
        tgt.style.setProperty('--' + pt.prefix + '-ease', 'var(--ease-' + st.ease + ')');
        tgt.style.setProperty('--' + pt.prefix + '-duration', 'var(--duration-' + st.dur + ')');
        if (opts.collapse !== false) { if (st.collapse === 'true') tgt.removeAttribute('data-' + pt.prefix); else tgt.setAttribute('data-' + pt.prefix, 'fade'); }
        if (pt.exit) WARN.filter(function (w) { return w[1](st); }).forEach(function (w) { var p = document.createElement('p'); p.className = 'pg-note'; p.style.margin = '0'; p.textContent = 'Warning: ' + w[2]; warn.appendChild(p); });
        code.push('.your-wrapper {\n  --' + pt.prefix + '-ease: var(--ease-' + st.ease + ');\n  --' + pt.prefix + '-duration: var(--duration-' + st.dur + ');\n}'
          + (opts.collapse !== false && st.collapse === 'false' ? '\n\n<!-- Fade only: no height collapse -->\n<div class="your-wrapper" data-' + pt.prefix + '="fade"> … </div>' : ''));
        note.push(st.ease === rec.ease && st.dur === rec.dur && st.collapse === rec.collapse);
        tb.appendChild(row([t + 'Easing', { code: '--ease-' + st.ease }, cs.getPropertyValue('--ease-' + st.ease).trim(), st.ease === rec.ease ? 'Yes' : nameOf(EASE, rec.ease)]));
        tb.appendChild(row([t + 'Duration', { code: '--duration-' + st.dur }, cs.getPropertyValue('--duration-' + st.dur).trim(), st.dur === rec.dur ? 'Yes' : nameOf(DUR, rec.dur) + ' · ' + cs.getPropertyValue('--duration-' + rec.dur).trim()]));
        if (opts.collapse !== false) tb.appendChild(row(['Height', '—', st.collapse === 'true' ? 'Collapse' : 'Fade only', st.collapse === rec.collapse ? 'Yes' : (rec.collapse === 'true' ? 'Collapse' : 'Fade only')]));
      });
      var isRec = note.every(Boolean);
      pre.textContent = (isRec ? '/* Recommended: this is the default, no code needed. Shown here for reference. */\n' : '/* Overrides the recommended motion. Set on the element or a wrapper around it. */\n') + code.join('\n\n');
    }
    var hasH = opts.collapse !== false;
    parts.forEach(function (pt, pi) {
      var t = pt.title ? pt.title + ' ' : '';
      controls.appendChild(slider(pt, pi, t + (pt.title ? 'easing' : 'Easing'), 'ease', EASE, function (o) { return o[1].replace(' emphasized', ' emph.'); }));
      controls.appendChild(slider(pt, pi, t + (pt.title ? 'duration' : 'Duration'), 'dur', DUR, function (o) { return o[2]; }));
    });
    if (hasH) {
      var pt0 = parts[0], hf = document.createElement('div'), hl = document.createElement('span'), hg = document.createElement('div');
      hf.className = 'ds-field'; hl.className = 'form-label form-label--sm'; hl.id = id + 'h'; hl.textContent = 'Height';
      hg.className = 'btn-group'; hg.setAttribute('role', 'group'); hg.setAttribute('aria-labelledby', hl.id);
      [['false', 'Fade only'], ['true', 'Collapse']].forEach(function (o) { var bt = document.createElement('button'); bt.type = 'button'; bt.dataset.v = o[0]; bt.textContent = o[1] + (o[0] === pt0.rec.collapse ? '*' : ''); bt.setAttribute('aria-pressed', String(o[0] === pt0.st.collapse)); hg.appendChild(bt); });
      hf.appendChild(hl); hf.appendChild(hg); controls.appendChild(hf);
      seg(hg, function (v) { pt0.st.collapse = v; apply(); });
    }
    var warn = document.createElement('div'); warn.style.cssText = 'display:flex;flex-direction:column;gap:8px'; warn.setAttribute('role', 'status'); controls.appendChild(warn);
    var again = document.createElement('button'); again.type = 'button'; again.className = 'btn btn--secondary'; again.style.alignSelf = 'flex-start'; again.innerHTML = '<span class="btn__label"></span>'; again.firstChild.textContent = opts.show ? 'Show toast' : 'Show again';
    /* No visible × = nothing closes = no motion: the controls are disabled and the stage says why. */
    var off = document.createElement('p'); off.className = 'pg-note'; off.style.cssText = 'margin:12px 0 0;text-align:center'; off.hidden = true;
    off.textContent = 'This selection has no close button, so it has no closing motion. Change the selection in Playground.';
    host.parentNode.appendChild(off);
    function check() {
      if (opts.show) return;
      var x = host.querySelector('.icon-btn--close'), can = !!(x && x.offsetParent);
      controls.inert = !can; controls.style.opacity = can ? '' : '0.5'; off.hidden = can;
    }
    function render() {
      if (opts.show) { opts.show(); return; }
      clear(host).appendChild(opts.preview()); check();
    }
    if (opts.show) { var hint = document.createElement('p'); hint.className = 'pg-note'; hint.style.cssText = 'margin:0;text-align:center'; hint.textContent = 'The toast appears in the corner of your window. Press Show toast to see the motion.'; host.appendChild(hint); }
    again.addEventListener('click', render); controls.appendChild(again);
    window.addEventListener('resize', check); document.addEventListener('click', function (e) { if (e.target.closest('[data-bp-toggle]')) setTimeout(check, 0); });
    if (!opts.show) render(); apply();
    return { render: render };
  }

  w.DK = { motion: motion, $: $, $$: $$, clear: clear, esc: esc, seg: seg, bp: bp, recipes: recipes, printFile: printFile, tokenTable: tokenTable, rows: rows };
})(window);
