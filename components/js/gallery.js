/* ECO component JS: Gallery + Expanded Gallery. CSS: /components/css/gallery.css
   Keeps thumbnails and dots in step with the image in view, and moves the track when a thumbnail or a previous/next button is pressed.
   The track itself scrolls natively (touch swipe, trackpad, keyboard arrows when focused); a mouse can drag the image. Previous/next wrap around.
   Expanded Gallery: pressing the image (or Enter on the focused track) opens a full-screen <dialog> built from the same images,
   on the same image; closing it puts the page gallery on the image that was last shown. Add data-gallery-expand="off" to turn it off. */
(function () {
  function setup(g) {
    if (g._gallery) return;
    var track = g.querySelector('.gallery__track'); if (!track) return;
    var slides = [].slice.call(track.children), thumbs = [].slice.call(g.querySelectorAll('.gallery__thumb')), dots = [].slice.call(g.querySelectorAll('.gallery__dots > *'));
    var row = g.querySelector('.gallery__thumbs'), cur = -1;
    function left(i) { return slides[i].offsetLeft - slides[0].offsetLeft; }
    function show(i) {
      if (i === cur) return; if (cur > -1) g.classList.add('is-moved');   /* the previous button shows only after the first change */
      cur = i;
      thumbs.forEach(function (t, k) { if (k === i) t.setAttribute('aria-current', 'true'); else t.removeAttribute('aria-current'); });
      dots.forEach(function (d, k) { d.classList.toggle('is-active', k === i); });
      var t = thumbs[i];
      if (t && row && row.clientWidth) row.scrollTo({ left: t.offsetLeft - row.offsetLeft - (row.clientWidth - t.offsetWidth) / 2, behavior: 'smooth' });
    }
    function go(i, instant) { i = (i + slides.length) % slides.length; track.scrollTo({ left: left(i), behavior: instant ? 'instant' : 'auto' }); show(i); }
    track.addEventListener('scroll', function () {   /* no requestAnimationFrame: it never fires in a background tab, and this is cheap */
      var x = track.scrollLeft, best = 0, d = Infinity;
      slides.forEach(function (s, k) { var v = Math.abs(left(k) - x); if (v < d) { d = v; best = k; } });
      show(best);
    });
    /* Mouse drag: the image follows the pointer and settles on the next or previous image when dragged past 15% of the width (no wrap).
       Touch and trackpad use the native scroll. Not the .swipe-row glide of tabs.js: a gallery moves one image at a time. A drag over 5px is not a click. */
    var x0 = null, s0, i0, dragged = false;
    track.addEventListener('pointerdown', function (e) { if (e.pointerType !== 'mouse' || e.button) return; x0 = e.clientX; s0 = track.scrollLeft; i0 = cur; dragged = false; });
    track.addEventListener('pointermove', function (e) {
      if (x0 === null) return; var dx = e.clientX - x0;
      if (!dragged) { if (Math.abs(dx) < 5) return; dragged = true; track.setPointerCapture(e.pointerId); track.classList.add('is-dragging'); }
      track.scrollLeft = s0 - dx;
    });
    function drop(e) {
      if (x0 === null) return; var dx = e.clientX - x0; x0 = null; if (!dragged) return;
      track.classList.remove('is-dragging');
      go(Math.max(0, Math.min(slides.length - 1, i0 + (Math.abs(dx) > track.clientWidth * 0.15 ? (dx < 0 ? 1 : -1) : 0))));
    }
    track.addEventListener('pointerup', drop); track.addEventListener('pointercancel', drop);
    track.addEventListener('dragstart', function (e) { e.preventDefault(); });   /* an image must not start a native drag */
    track.addEventListener('click', function (e) { if (dragged) { dragged = false; e.stopPropagation(); } }, true);
    g.addEventListener('click', function (e) {
      var nav = e.target.closest('[data-gallery]'), t = e.target.closest('.gallery__thumb');
      if (nav) go(cur + (nav.dataset.gallery === 'prev' ? -1 : 1));
      else if (t) go(thumbs.indexOf(t));
      else if (expandable && e.target.closest('.gallery__slide')) expand(g);
    });
    var expandable = !g.classList.contains('gallery--expanded') && g.dataset.galleryExpand !== 'off';
    if (expandable) {
      slides.forEach(function (s) { s.classList.add('gallery__slide--zoom'); });
      track.addEventListener('keydown', function (e) { if (e.key === 'Enter' && e.target === track) { e.preventDefault(); expand(g); } });
    }
    g._gallery = { go: go, index: function () { return cur; } };
    show(0);
  }

  /* Expanded Gallery: one dialog per page gallery, built on first use */
  function expand(g) {
    var d = g._galleryDialog;
    if (!d) {
      d = document.createElement('dialog'); d.className = 'gallery-x';
      d.setAttribute('aria-label', g.getAttribute('aria-label') || 'Bilder');
      var inner = g.cloneNode(true);
      inner.classList.add('gallery--expanded'); inner.removeAttribute('role'); inner.removeAttribute('aria-label');
      inner.querySelectorAll('[loading]').forEach(function (i) { i.removeAttribute('loading'); });
      inner.querySelectorAll('.gallery__slide--zoom').forEach(function (s) { s.classList.remove('gallery__slide--zoom'); });
      inner.querySelectorAll('.gallery__nav').forEach(function (b) { b.classList.replace('btn--primary-inverted', 'btn--primary'); });   /* Figma: Primary here */
      d.innerHTML = '<button type="button" class="btn btn--blank btn--sm btn--icon gallery-x__close" aria-label="Stäng"><span class="btn__icon" aria-hidden="true">close</span></button>';
      d.appendChild(inner); document.body.appendChild(d);
      setup(inner);
      d.querySelector('.gallery-x__close').addEventListener('click', function () { d.close(); });
      d.addEventListener('close', function () { g._gallery.go(inner._gallery.index(), true); });
      g._galleryDialog = d; d._inner = inner;
    }
    d.showModal();
    d._inner._gallery.go(g._gallery.index(), true);
  }

  function init(scope) { [].forEach.call((scope || document).querySelectorAll('.gallery'), setup); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function () { init(); }); else init();
  window.ECO_GALLERY = { init: init };
})();
