/* ECO doc pages: load eco-tokens/tokens.json and re-render when it changes.
   ECO.watch(url, onData, onError?) — calls onData(json) once, then again whenever the
   file content changes (checked every 4 s while the tab is visible and on tab focus).
   Needs http(s): fetch does not work from file://. */
window.ECO = (function () {
  function watch(url, onData, onError) {
    var last = null, failed = false;
    function check() {
      fetch(url, { cache: 'no-store' })
        .then(function (r) { if (!r.ok) throw new Error(r.status); return r.text(); })
        .then(function (text) {
          failed = false;
          if (text === last) return;
          last = text;
          onData(JSON.parse(text));
        })
        .catch(function (e) { if (!failed && onError) onError(e); failed = true; });
    }
    check();
    setInterval(function () { if (!document.hidden) check(); }, 4000);
    document.addEventListener('visibilitychange', function () { if (!document.hidden) check(); });
  }
  return { watch: watch };
})();
