/* ECO component JS: tooltip. Skill: eco-tooltip. Link it, do not copy it: <script src="/components/js/tooltip.js"></script>
   Pairs with components/css/tooltip.css. Two jobs:

   1. Flip. When an automatic Top or Bottom tooltip (.tooltip-wrap > .tooltip--top / --bottom) opens (pointer over its wrap)
      with too little room on its side and more on the other, it gets .tooltip--flip and sits on the other side. When a centered
      tooltip would leave the viewport sideways it gets .tooltip--align-start / --align-end: its edge lines up with the trigger's
      outer edge and the beak stays on the trigger's center.

   2. Global tooltip. Any element with data-tooltip="Label" shows ONE shared tooltip (a popover in the top layer, so no
      overflow or stacking context can clip or hide it). Optional data-tooltip-position="top|bottom" (default top). Works for
      elements added later (events are delegated). No markup besides the attribute; keep an aria-label with the same text.

   A page with a sticky header sets --tooltip-safe-top (the header's height, in px) on :root: room above then counts from
   below the header. .tooltip--manual tooltips are never touched by the flip. */
(function () {
  var anchored = CSS.supports('position-area', 'bottom') && CSS.supports('anchor-scope', '--x');
  function safeTop() { return parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--tooltip-safe-top')) || 0; }

  /* Pick the side with room: 'flip' when the declared side is too tight and the other is roomier. */
  function needsFlip(r, bottom, h) {
    var need = h + 10; /* tooltip + 6px beak + 4px distance */
    var below = innerHeight - r.bottom, above = r.top - safeTop(), own = bottom ? below : above, other = bottom ? above : below;
    return own < need && other > own;
  }

  /* Sideways: a centered tooltip that would leave the viewport lines up with the trigger's outer edge instead (start or end),
     the beak stays on the trigger's center. */
  function alignSide(tip, r) {
    tip.classList.remove('tooltip--align-start', 'tooltip--align-end');
    var tw = tip.offsetWidth, cx = r.left + r.width / 2, vw = document.documentElement.clientWidth, m = 8;
    if (cx - tw / 2 < m) tip.classList.add('tooltip--align-start');
    else if (cx + tw / 2 > vw - m) tip.classList.add('tooltip--align-end');
  }

  /* 1. declarative tooltips */
  function placeWrap(wrap) {
    var tip = wrap.querySelector(':scope > .tooltip');
    if (!tip || tip.classList.contains('tooltip--manual')) return;
    var bottom = tip.classList.contains('tooltip--bottom');
    if (!bottom && !tip.classList.contains('tooltip--top')) return;
    var wr = wrap.getBoundingClientRect();
    tip.classList.toggle('tooltip--flip', needsFlip(wr, bottom, tip.offsetHeight));
    alignSide(tip, wr);
  }

  /* 2. global tooltip */
  var tip, current;
  function globalTip() {
    if (tip) return tip;
    tip = document.createElement('div');
    tip.className = 'tooltip tooltip--global';
    tip.setAttribute('role', 'tooltip');
    tip.setAttribute('popover', 'manual');
    document.body.appendChild(tip);
    return tip;
  }
  function show(el) {
    var t = globalTip(), bottom = el.dataset.tooltipPosition === 'bottom';
    if (current && current !== el) current.style.anchorName = '';
    current = el;
    t.textContent = el.dataset.tooltip;
    t.className = 'tooltip tooltip--global tooltip--' + (bottom ? 'bottom' : 'top');
    t.style.cssText = '';
    if (anchored) el.style.anchorName = '--tooltip-global';
    else t.classList.add('tooltip--manual');
    if (!t.matches(':popover-open')) t.showPopover();
    var r = el.getBoundingClientRect();
    if (anchored) { if (needsFlip(r, bottom, t.offsetHeight)) t.classList.add('tooltip--flip'); alignSide(t, r); }
    else { /* no anchor positioning: centered on the element, kept inside the viewport, on the roomier side */
      var flip = needsFlip(r, bottom, t.offsetHeight), below = bottom !== flip;
      var left = Math.max(8, Math.min(r.left + r.width / 2 - t.offsetWidth / 2, innerWidth - t.offsetWidth - 8));
      t.style.cssText = 'position:fixed;transform:none;right:auto;bottom:auto;left:' + left + 'px;top:' + (below ? r.bottom + 10 : r.top - t.offsetHeight - 10) + 'px';
    }
  }
  function hide() {
    if (current) { current.style.anchorName = ''; current = null; }
    if (tip && tip.matches(':popover-open')) tip.hidePopover();
  }

  document.addEventListener('pointerover', function (e) {
    var w = e.target.closest && e.target.closest('.tooltip-wrap');
    if (w) placeWrap(w);
    var g = e.target.closest && e.target.closest('[data-tooltip]');
    if (g) { if (g !== current) show(g); } else if (current) hide();
  });
  document.addEventListener('pointerout', function (e) {
    var g = e.target.closest && e.target.closest('[data-tooltip]');
    if (g && g === current && !(e.relatedTarget && g.contains(e.relatedTarget))) hide();
  });
  /* a click closes it for the mouse; on touch the tap that opens it (pointerover comes first) stays, a tap elsewhere closes it */
  document.addEventListener('pointerdown', function (e) {
    var g = e.target.closest && e.target.closest('[data-tooltip]');
    if (e.pointerType === 'mouse' || !g) hide();
  });
})();
