/* ECO component JS: Picker Stepper. Skill: eco-picker-stepper. CSS: /components/css/picker-stepper.css
   Delegated, so steppers added later work too. Limits come from the input: min (default 1), max (default none), step (default 1).
   After every change the input fires a bubbling "change" event; read input.value there. */
(function () {
  function limits(input) {
    var min = parseInt(input.getAttribute('min'), 10), max = parseInt(input.getAttribute('max'), 10), step = parseInt(input.getAttribute('step'), 10);
    return { min: isNaN(min) ? 1 : min, max: isNaN(max) ? Infinity : max, step: isNaN(step) || step < 1 ? 1 : step };
  }
  function sync(root, value) {
    var input = root.querySelector('.picker-stepper__input'); if (!input) return;
    var l = limits(input), v = parseInt(value == null ? input.value : value, 10);
    if (isNaN(v)) v = l.min;
    v = Math.min(l.max, Math.max(l.min, v));
    var changed = String(v) !== input.value; input.value = v;
    root.querySelectorAll('.picker-stepper__btn[data-step]').forEach(function (b) {
      b.disabled = input.disabled || (Number(b.dataset.step) < 0 ? v <= l.min : v >= l.max);
    });
    return changed;
  }
  document.addEventListener('click', function (e) {
    var b = e.target.closest('.picker-stepper__btn[data-step]'); if (!b) return;
    var root = b.closest('.picker-stepper'), input = root && root.querySelector('.picker-stepper__input'); if (!input) return;
    var l = limits(input), dir = Number(b.dataset.step) < 0 ? -1 : 1;
    if (sync(root, (parseInt(input.value, 10) || l.min) + dir * l.step)) input.dispatchEvent(new Event('change', { bubbles: true }));
  });
  document.addEventListener('change', function (e) {
    if (e.target.matches && e.target.matches('.picker-stepper__input')) sync(e.target.closest('.picker-stepper'));
  });
  function init(scope) { (scope || document).querySelectorAll('.picker-stepper').forEach(function (r) { sync(r); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function () { init(); }); else init();
  window.ECO_PICKER_STEPPER = { init: init };   /* call init(root) after adding steppers with a value outside the limits */
})();
