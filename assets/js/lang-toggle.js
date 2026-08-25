(function () {
  var STORAGE_KEY = "site-lang";

  var stored = null;
  try {
    stored = localStorage.getItem(STORAGE_KEY);
  } catch (e) {
    // Private mode / blocked storage: fall through to the default language.
  }
  var lang = stored === "zh" || stored === "en" ? stored : "en";
  document.documentElement.setAttribute("data-lang", lang);

  // Reflect the active language on the segmented control so the current
  // option renders filled. aria-pressed doubles as the styling hook.
  function syncButtons() {
    var current = document.documentElement.getAttribute("data-lang");
    var buttons = document.querySelectorAll("[data-set-lang]");
    for (var i = 0; i < buttons.length; i++) {
      buttons[i].setAttribute("aria-pressed", buttons[i].getAttribute("data-set-lang") === current ? "true" : "false");
    }
  }

  function setLang(next) {
    if (next !== "zh" && next !== "en") return;
    document.documentElement.setAttribute("data-lang", next);
    try {
      localStorage.setItem(STORAGE_KEY, next);
    } catch (e) {
      // Preference just won't persist across reloads.
    }
    syncButtons();
  }

  document.addEventListener("DOMContentLoaded", function () {
    var buttons = document.querySelectorAll("[data-set-lang]");
    for (var i = 0; i < buttons.length; i++) {
      buttons[i].addEventListener("click", function () {
        setLang(this.getAttribute("data-set-lang"));
      });
    }
    syncButtons();
  });
})();
