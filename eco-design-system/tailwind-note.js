/* ECO doc pages: the "Using with Tailwind" block, appended to the Code section of every component page (or the last section when there is none). */
(function () {
  function run() {
  var host = document.querySelector('#code .ds-inner') || (function () { var s = document.querySelectorAll('section .ds-inner'); return s[s.length - 1]; })();
  if (!host) return;
  var uid = 0;
  function box(title, code) {
    var id = 'tw-code-' + (uid++), b = document.createElement('div');
    b.className = 'ds-code';
    b.innerHTML = '<div class="ds-code__bar"><span></span><button type="button" class="mo-copy" data-copy="' + id + '" aria-label="Copy"><span class="mo-ic" aria-hidden="true">content_copy</span></button></div><pre id="' + id + '"></pre>';
    b.querySelector('span').textContent = title; b.querySelector('pre').textContent = code; return b;
  }
  var h = document.createElement('h3'); h.className = 'ds-h3'; h.id = 'tailwind'; h.textContent = 'Using with Tailwind';
  var p = document.createElement('p'); p.className = 'ds-desc';
  p.innerHTML = 'Pages in this project are styled with Tailwind. The component CSS (printed in the Code section of each component page) is <strong>plain component CSS</strong> with ordinary class names; it works next to Tailwind and does not have to be rewritten as utility classes (states such as <code>:hover</code>, <code>::after</code>, <code>:has()</code> and <code>[data-state]</code> are clearer as CSS). Three things make it fit: add it once in a <code>@layer components</code> block, use the tokens as <code>[var(--…)]</code> for everything around the component, and set <code>md</code> to <strong>769px</strong>, as the component CSS does.';
  var note = document.createElement('p'); note.className = 'ds-desc';
  note.innerHTML = 'Tailwind’s preflight resets margins, borders, headings and button styles. The component CSS sets what it needs itself, but check headings and lists that you place inside the component.';
  host.appendChild(h); host.appendChild(p);
  host.appendChild(box('1 · CSS: add the component CSS once, after Tailwind', '/* app.css */\n@import "tailwindcss";   /* your Tailwind entry */\n\n@layer components {\n  /* paste the component CSS here */\n}'));
  host.appendChild(box('2 · tailwind.config.js: the ECO breakpoints (md = 769px, not 768px)', "module.exports = {\n  theme: {\n    screens: {\n      sm: '640px',   // tablet (looks like mobile)\n      md: '769px',   // desktop small\n      lg: '1024px',\n      xl: '1281px',\n    },\n  },\n};"));
  host.appendChild(box('3 · Tokens as utilities around the component', '<section class="bg-[var(--color-surface-raised-primary)] px-[var(--dimension-spacing-space-16)] md:px-[var(--dimension-spacing-space-24)]">\n  <!-- the component markup from this page -->\n</section>\n\n<!-- Color, spacing and shadow always come from the tokens: -->\n<p class="text-[var(--color-text-secondary)] shadow-[var(--shadow-elevation-b-20)]">…</p>'));
  host.appendChild(note);
  }
  /* the notification pages print their CSS and JS asynchronously into #files: wait for it so this block comes last */
  var files = document.getElementById('files'), tries = 0;
  (function wait() { if (files && !files.querySelector('.ds-code') && tries++ < 40) return setTimeout(wait, 100); run(); })();
})();
