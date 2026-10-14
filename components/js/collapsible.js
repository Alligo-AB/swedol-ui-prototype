/* ECO collapsible behavior. Skill: eco-collapsible. Link it, do not copy it: <script src="/components/js/collapsible.js"></script>
   Header: <button class="collapsible-item" onclick="toggleCollapsible(this)" aria-expanded="false" aria-controls="id"> (recommended), or the older <div class="collapsible-item" onclick="…">.
   A click on a control inside the header (the toggle switch, a link, a button with data-collapsible-ignore) does not open or close the row. A disabled row does not open. */
function toggleCollapsible(header) {
  const wrap = header.parentElement;
  const content = header.nextElementSibling;
  if (wrap.classList.contains('collapsible-wrap--disabled') || header.disabled || header.getAttribute('aria-disabled') === 'true') return;
  const ev = window.event;
  if (ev && ev.target.closest && ev.target.closest('.form-switch-item, a, [data-collapsible-ignore]') && header.contains(ev.target)) return;
  const isOpen = wrap.classList.contains('collapsible-wrap--open');
  wrap.classList.toggle('collapsible-wrap--open', !isOpen);
  if (header.hasAttribute('aria-expanded')) header.setAttribute('aria-expanded', String(!isOpen));
  content.style.maxHeight = isOpen ? null : content.scrollHeight + 'px';
}
