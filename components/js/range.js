/* ECO range (slider): fills the value text and the tick labels of every [data-range] block and keeps them in sync.
   Skill: eco-range. Markup and attributes: see .claude/skills/eco-range/SKILL.md. Pair with components/css/range.css.
   Works on blocks present at load; call ECO_RANGE.init(root) for blocks added later. The input fires its normal `input` event. */
(function (w) {
  function init(root) {
    Array.prototype.forEach.call((root || document).querySelectorAll('[data-range]'), function (box) {
      if (box._range) return; box._range = true;
      var input = box.querySelector('input[type="range"]'), out = box.querySelector('.form-range__value'), ticks = box.querySelector('.form-range__ticks');
      var labels = box.dataset.labels ? box.dataset.labels.split('|') : null, tk = box.dataset.ticks ? box.dataset.ticks.split('|') : labels, rec = box.dataset.recommended, unit = box.dataset.unit || '';
      function show() {
        var i = Math.round((input.value - input.min) / input.step), t = labels ? labels[i] : input.value + unit;
        if (out) out.textContent = t; input.setAttribute('aria-valuetext', t);
      }
      if (ticks && tk) {
        ticks.setAttribute('aria-hidden', 'true');
        tk.forEach(function (txt, i) { var s = document.createElement('span'), p = i / (tk.length - 1) * 100; s.textContent = txt + (String(i) === rec ? '*' : ''); s.style.left = p + '%'; s.style.transform = 'translateX(-' + p + '%)'; ticks.appendChild(s); });
      }
      input.addEventListener('input', show); show();
    });
  }
  w.ECO_RANGE = { init: init };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function () { init(); }); else init();
})(window);
