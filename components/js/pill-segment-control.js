/* ECO pill segment control behavior. Skill: eco-pill-segment-control. Link it, do not copy it: <script src="/components/js/pill-segment-control.js"></script>
   Slides the thumb to the active button (offsetLeft/offsetWidth: the buttons can have different widths), keeps aria-pressed in sync,
   and fires a bubbling "segment-change" event on the control with detail.button. ECO_SEGMENT.init(container) wires controls added later. */
(function (w) {
  function move(c) {
    var t = c.querySelector('.pill-segment-control__thumb'), a = c.querySelector('.pill-segment-control__btn--active');
    if (!t || !a) return;
    t.style.width = a.offsetWidth + 'px';
    t.style.transform = 'translateX(' + a.offsetLeft + 'px)';
  }
  function init(root) {
    Array.prototype.forEach.call((root || document).querySelectorAll('.pill-segment-control'), function (c) {
      if (!c.__eco) {
        c.__eco = true;
        c.addEventListener('click', function (e) {
          var b = e.target.closest('.pill-segment-control__btn'); if (!b || b.disabled) return;
          Array.prototype.forEach.call(c.querySelectorAll('.pill-segment-control__btn'), function (x) {
            x.classList.toggle('pill-segment-control__btn--active', x === b); x.setAttribute('aria-pressed', String(x === b));
          });
          move(c);
          c.dispatchEvent(new CustomEvent('segment-change', { bubbles: true, detail: { button: b } }));
        });
      }
      move(c);
    });
  }
  w.ECO_SEGMENT = { init: init, move: move };
  document.addEventListener('DOMContentLoaded', function () { init(); });
  w.addEventListener('load', function () { init(); });
  w.addEventListener('resize', function () { init(); });
})(window);
