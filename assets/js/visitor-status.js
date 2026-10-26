(function () {
  function showUnavailable() {
    ["site_uv", "site_pv"].forEach(function (metric) {
      var value = document.getElementById("busuanzi_value_" + metric);
      var container = document.getElementById("busuanzi_container_" + metric);
      if (!value || /^\d+$/.test(value.textContent.trim())) return;
      value.innerHTML = '<span class="lang-zh">暂不可用</span><span class="lang-en">Unavailable</span>';
      if (container) container.style.display = "inline";
    });
  }
  // Leave successful counts intact; never substitute invented visitor numbers.
  window.setTimeout(showUnavailable, 15000);
})();
