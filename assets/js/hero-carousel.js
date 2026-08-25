(function () {
  // Homepage hero carousel. Markup comes from _includes/hero-carousel.liquid,
  // slides from _data/carousel.yml. No dependencies — the site ships no
  // carousel library and one slideshow does not justify adding one.

  function initCarousel(root) {
    var slides = root.querySelectorAll("[data-hero-slide]");
    if (slides.length < 2) return;

    var dots = root.querySelectorAll("[data-hero-dot]");
    var prev = root.querySelector("[data-hero-prev]");
    var next = root.querySelector("[data-hero-next]");
    var interval = parseInt(root.getAttribute("data-interval"), 10) || 5000;
    var index = 0;
    var timer = null;

    // Respect the OS "reduce motion" setting: show the first slide and never
    // advance on our own. Manual controls keep working.
    var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    function show(n) {
      index = (n + slides.length) % slides.length;
      for (var i = 0; i < slides.length; i++) {
        var active = i === index;
        slides[i].classList.toggle("is-active", active);
        // aria-hidden rather than display:none so the crossfade still works.
        if (active) {
          slides[i].removeAttribute("aria-hidden");
        } else {
          slides[i].setAttribute("aria-hidden", "true");
        }
      }
      for (var j = 0; j < dots.length; j++) {
        dots[j].classList.toggle("is-active", j === index);
        dots[j].setAttribute("aria-selected", j === index ? "true" : "false");
      }
    }

    function stop() {
      if (timer) {
        clearInterval(timer);
        timer = null;
      }
    }

    function start() {
      if (reduceMotion) return;
      stop();
      timer = setInterval(function () {
        show(index + 1);
      }, interval);
    }

    // A manual jump restarts the clock, so the slide the user just picked gets
    // a full interval rather than whatever was left of the previous one.
    function goTo(n) {
      show(n);
      start();
    }

    if (prev) {
      prev.addEventListener("click", function () {
        goTo(index - 1);
      });
    }
    if (next) {
      next.addEventListener("click", function () {
        goTo(index + 1);
      });
    }
    for (var k = 0; k < dots.length; k++) {
      (function (dot) {
        dot.addEventListener("click", function () {
          goTo(parseInt(dot.getAttribute("data-hero-dot"), 10));
        });
      })(dots[k]);
    }

    root.addEventListener("mouseenter", stop);
    root.addEventListener("mouseleave", start);
    root.addEventListener("focusin", stop);
    root.addEventListener("focusout", start);

    // Don't burn cycles advancing slides nobody can see.
    document.addEventListener("visibilitychange", function () {
      if (document.hidden) {
        stop();
      } else {
        start();
      }
    });

    show(0);
    start();
  }

  document.addEventListener("DOMContentLoaded", function () {
    var roots = document.querySelectorAll("[data-hero-carousel]");
    for (var i = 0; i < roots.length; i++) {
      initCarousel(roots[i]);
    }
  });
})();
