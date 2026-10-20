/* ECO pagination behavior. Skill: eco-pagination. Link it, do not copy it: <script src="/components/js/pagination.js"></script> */
function updatePagination(key, visible, total) {
  document.getElementById(key + '-pagination-count').textContent = visible;
  document.getElementById(key + '-pagination-bar').style.width = (total ? (visible / total) * 100 : 0) + '%';
  var btn = document.querySelector('#pagination-' + key + ' button');
  if (btn) btn.disabled = visible >= total; // nothing more to load: the button stays, disabled
}
