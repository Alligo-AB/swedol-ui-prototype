/* ECO measurement figure: reads the padding of each .measure__subject and sets --pt/--pr/--pb/--pl on its .measure__obj, plus the numbers.
   Skill: eco-doc-page. Markup: see components/css/measure.css. Runs on load; call ECO_MEASURE.init(root) for figures added later. */
(function () {
  function init(root) {
    (root || document).querySelectorAll('.measure__obj').forEach(function (obj) {
      var s = obj.querySelector('.measure__subject'); if (!s) return;
      var cs = getComputedStyle(s), box = s.hasAttribute('data-measure-margin') ? 'margin' : 'padding';   /* data-measure-margin: the space is the subject's margin (checkbox, radio, switch) */
      var edge = obj.querySelector('[data-measure-edge]');   /* data-measure-edge: a status edge that sits outside the padding (toast, banner, inline): the left shading starts after it. On the subject itself it is its left border; on another element, that element's width */
      obj.style.setProperty('--edge', edge ? (edge === s ? cs.borderLeftWidth : getComputedStyle(edge).width) : '0px');
      [['t', 'Top'], ['r', 'Right'], ['b', 'Bottom'], ['l', 'Left']].forEach(function (d) {
        var v = cs[box + d[1]];
        obj.style.setProperty('--p' + d[0], v);
        var dim = obj.querySelector('.measure__dim--' + d[0]), pad = obj.querySelector('.measure__pad--' + d[0]), n = dim && dim.querySelector('span'), zero = !parseFloat(v);
        if (n) n.textContent = Math.round(parseFloat(v) * 100) / 100;
        if (dim) dim.hidden = zero; if (pad) pad.hidden = zero;   /* no padding on that side: draw nothing */
      });
    });
  }
  window.ECO_MEASURE = { init: init };
  var rt; window.addEventListener('resize', function () { clearTimeout(rt); rt = setTimeout(function () { init(); }, 100); });   /* the padding changes at 769px */
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function () { init(); }); else init();
})();
