/* ECO chip behaviour (skill eco-chip, CSS components/css/chip.css).
   A filter chip is <button class="chip" aria-pressed="false">: a click toggles aria-pressed and fires "chip:change".
   A removable chip (.chip--removable) fires "chip:remove"; the page removes it. */
document.addEventListener('click', function (e) {
  var chip = e.target.closest('.chip');
  if (!chip || chip.disabled) return;
  if (chip.classList.contains('chip--removable')) { chip.dispatchEvent(new CustomEvent('chip:remove', { bubbles: true })); return; }
  if (!chip.hasAttribute('aria-pressed')) return;
  chip.setAttribute('aria-pressed', chip.getAttribute('aria-pressed') === 'true' ? 'false' : 'true');
  chip.dispatchEvent(new CustomEvent('chip:change', { bubbles: true, detail: { selected: chip.getAttribute('aria-pressed') === 'true' } }));
});
