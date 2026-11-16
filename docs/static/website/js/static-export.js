/* GitHub Pages build: there is no server to read the preference cookie, so
   theme and language live in localStorage here. */
(function () {
  var root = document.documentElement;
  var THEME_KEY = 'sti_theme', LANG_KEY = 'sti_lang';
  function store(key, value) { try { localStorage.setItem(key, value); } catch (e) {} }
  function read(key) { try { return localStorage.getItem(key); } catch (e) { return null; } }

  /* preferences picked on one page have to survive the next navigation */
  document.addEventListener('click', function (e) {
    var theme = e.target.closest('[data-theme-toggle], #themeToggle');
    if (theme) {
      var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      store(THEME_KEY, next);
      return;
    }
    var lang = e.target.closest('[data-pref="lang"]');
    if (lang && lang.dataset.value) store(LANG_KEY, lang.dataset.value);
  }, true);

  /* keep the visible label in sync when the overshell swapped the document */
  var theme = root.getAttribute('data-theme');
  var dark = theme === 'dark';
  var labels = document.querySelectorAll('[data-theme-label]');
  for (var i = 0; i < labels.length; i++) {
    labels[i].textContent = dark ? 'Light mode' : 'Dark mode';
  }
})();
