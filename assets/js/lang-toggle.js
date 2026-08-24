(function () {
  var STORAGE_KEY = "site-lang";

  var stored = localStorage.getItem(STORAGE_KEY);
  var lang = stored === "zh" || stored === "en" ? stored : "en";
  document.documentElement.setAttribute("data-lang", lang);

  function updateLabel() {
    var label = document.getElementById("lang-toggle-label");
    if (!label) return;
    var current = document.documentElement.getAttribute("data-lang");
    label.textContent = current === "zh" ? "EN" : "中文";
  }

  document.addEventListener("DOMContentLoaded", function () {
    updateLabel();
    var btn = document.getElementById("lang-toggle");
    if (!btn) return;
    btn.addEventListener("click", function () {
      var current = document.documentElement.getAttribute("data-lang");
      var next = current === "zh" ? "en" : "zh";
      document.documentElement.setAttribute("data-lang", next);
      localStorage.setItem(STORAGE_KEY, next);
      updateLabel();
    });
  });
})();
