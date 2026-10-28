/* Mounts Hairline figures into cards instead of the bench page.
   Usage: <div data-hairline-card="button-pair" data-src="../hairline/button-pair.js"></div> for every figure, then kernel.js and this file
   (classic scripts, in that order). Each figure's source is fetched and run inside its own function, so several figures on one
   page never share names. Needs a server (fetch), not file://. The stage must be 5:4: the kernel maps the pointer onto a 400 x 320 viewBox. */
(() => {
  /* data-play: the figure's tour runs while the card is hovered or keyboard-focused, and stops when the pointer leaves or focus moves out. */
  const addHoverTour = (el, figure) => {
    const card = el.closest(".ds-card") || el.parentElement;
    let run = null;
    const on = () => { if (!run) run = HL.tour(el, figure.tour, () => {}, 0, { travel: +el.dataset.travel || undefined, dwell: +el.dataset.dwell || undefined }); };
    const off = () => { run?.stop(); run = null; };
    card.addEventListener("mouseenter", on);
    card.addEventListener("mouseleave", off);
    card.addEventListener("focusin", (e) => { if (e.target.matches(":focus-visible")) on(); });
    card.addEventListener("focusout", off);
  };
  const mountInto = (el) => (figure) => {
    HL.inject(document);
    el.setAttribute("data-hairline", figure.name);
    const svg = HL.mk("svg", { viewBox: "0 0 400 320", "aria-hidden": "true" }, el);
    figure.mount({ stage: el, svg, read: { textContent: "" } }, figure.range[1]); // no read-out on a card
    if (el.hasAttribute("data-play") && figure.tour) addHoverTour(el, figure);
  };
  /* HLmount(root): mounts every figure inside root; runs once for the page, and pages that add figures later call it on the new part */
  const mountAll = (root) => root.querySelectorAll("[data-hairline-card][data-src]").forEach((el) => {
    fetch(el.dataset.src)
      .then((r) => { if (!r.ok) throw new Error(r.status); return r.text(); })
      .then((src) => new Function("HL", "hairline", src)(HL, mountInto(el))) // the figure's own scope; it calls hairline({...}) itself
      .catch((e) => console.error("hairline card " + el.dataset.hairlineCard + ": " + e.message));
  });
  window.HLmount = mountAll;
  mountAll(document);
})();
