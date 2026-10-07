/* ECO collapsible behavior. Skill: eco-collapsible. Link it, do not copy it: <script src="/components/js/collapsible.js"></script> */
function toggleCollapsible(header) {
  const wrap = header.parentElement;
  const content = header.nextElementSibling;
  const isOpen = wrap.classList.contains('collapsible-wrap--open');
  wrap.classList.toggle('collapsible-wrap--open', !isOpen);
  content.style.maxHeight = isOpen ? null : content.scrollHeight + 'px';
}
