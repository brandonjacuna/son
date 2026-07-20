// Sŏn investor site — motion (pass 4).
// Timed reveal only: no pin, no scrub, no parallax, no smooth-scroll
// library. Transform and opacity only; the CSS in site.css carries the
// durations, rises, and the band wipe. This file only decides WHEN.
//
// Reduced motion is a designed path, not a kill switch: every element is
// set to its complete state immediately (the immersive kill rule in
// tokens/motion-immersive.css collapses the transitions themselves), so
// the band appears complete and the hero appears settled, and nothing is
// lost. Without JavaScript the page renders complete; the html.js gate
// keeps hidden states out of the no-JS path.

(() => {
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const marked = "[data-reveal], [data-reveal-band]";

  const arm = (el, i) => {
    const delay = el.dataset.delay !== undefined ? Number(el.dataset.delay) : i * 80;
    if (el.hasAttribute("data-reveal-band")) {
      el.style.setProperty("--beat-delay", `${delay}ms`);
    } else {
      el.style.transitionDelay = `${delay}ms`;
    }
    el.classList.add("is-in");
  };

  if (reduce) {
    // Reduced motion is a designed path: everything arrives complete.
    // The chrome and the form below still run; their transitions collapse.
    document.querySelectorAll(marked).forEach((el) => el.classList.add("is-in"));
  } else {
    // The load beat: the hero entrance and the chrome fade. Once, on load,
    // nothing on scroll after it.
    const loadBeat = () => {
      document.querySelectorAll("[data-load]").forEach((el, i) => arm(el, i));
    };
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", () => requestAnimationFrame(loadBeat));
    } else {
      requestAnimationFrame(loadBeat);
    }
  }

  // The chrome: transparent and present over the hero; past it, hides on
  // scroll-down and returns on scroll-up as a summoned, solid object.
  // Feedback register. Focus into the header always reveals it, so A1
  // stays keyboard-reachable.
  const header = document.querySelector(".site-header");
  const hero = document.querySelector(".slot-hero");
  if (header && hero) {
    let lastY = window.scrollY;
    const onScroll = () => {
      const y = window.scrollY;
      const past = y > hero.offsetHeight - header.offsetHeight;
      header.classList.toggle("is-away", past);
      if (!past) header.classList.remove("is-hidden");
      else if (y > lastY + 2) header.classList.add("is-hidden");
      else if (y < lastY - 2) header.classList.remove("is-hidden");
      lastY = y;
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    header.addEventListener("focusin", () => header.classList.remove("is-hidden"));
    onScroll();
  }

  // The scroll beats: IntersectionObserver on enter, at roughly 85% of the
  // viewport height, firing once and never re-firing.
  if (!reduce) {
    const io = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (!entry.isIntersecting) continue;
          io.unobserve(entry.target);
          const beat = entry.target;
          const items = [
            ...(beat.matches(marked) ? [beat] : []),
            ...beat.querySelectorAll(marked),
          ];
          items.forEach((el, i) => arm(el, i));
        }
      },
      { rootMargin: "0px 0px -15% 0px" }
    );
    document.querySelectorAll("[data-beat]").forEach((beat) => io.observe(beat));
  }

  // The form (A3): validation as feedback, never narrative. The palette
  // has no red, so an invalid field speaks through the 2px border
  // exception plus a message, never color alone. The confirmation is the
  // one separate surface, a 200ms functional cross-fade, and conversion
  // has already happened when it appears.
  const form = document.querySelector(".ask-form");
  if (form) {
    const card = form.closest(".ask-card");
    const confirmation = card.querySelector(".ask-confirmation");
    const disclaimer = card.querySelector(".disclaimer");
    const messages = {
      name: "Add your full name.",
      email: "Add your email.",
      emailFormat: "Check the email format.",
      interest: "Tell us what interests you.",
      send: "Something interrupted the request. Try again.",
    };

    const errorFor = (input) => {
      const id = `${input.id}-error`;
      let el = document.getElementById(id);
      if (!el) {
        el = document.createElement("p");
        el.className = "son-field-error";
        el.id = id;
        input.insertAdjacentElement("afterend", el);
      }
      return el;
    };
    const setError = (input, message) => {
      const el = errorFor(input);
      el.textContent = message;
      input.setAttribute("aria-invalid", "true");
      input.setAttribute("aria-describedby", el.id);
    };
    const clearError = (input) => {
      const el = document.getElementById(`${input.id}-error`);
      if (el) el.remove();
      input.removeAttribute("aria-invalid");
      input.removeAttribute("aria-describedby");
    };
    const validate = (input) => {
      const value = input.value.trim();
      if (!value) {
        setError(input, messages[input.name] || messages.name);
        return false;
      }
      if (input.type === "email" && !/^\S+@\S+\.\S+$/.test(value)) {
        setError(input, messages.emailFormat);
        return false;
      }
      clearError(input);
      return true;
    };

    form.addEventListener("input", (e) => {
      if (e.target.hasAttribute("aria-invalid")) validate(e.target);
    });

    const showConfirmation = () => {
      form.classList.add("is-leaving");
      disclaimer.classList.add("is-leaving");
      window.setTimeout(() => {
        form.hidden = true;
        disclaimer.hidden = true;
        confirmation.hidden = false;
        requestAnimationFrame(() => {
          confirmation.classList.add("is-in");
          confirmation.focus();
        });
      }, reduce ? 0 : 200);
    };

    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      const inputs = [...form.querySelectorAll(".son-field[required]")];
      const invalid = inputs.filter((input) => !validate(input));
      if (invalid.length) {
        invalid[0].focus();
        return;
      }
      const endpoint = form.dataset.endpoint;
      if (!endpoint) {
        console.warn("Sŏn ask form: no endpoint configured (data-endpoint); request not sent.");
        showConfirmation();
        return;
      }
      const submit = form.querySelector(".ask-submit");
      submit.disabled = true;
      try {
        const res = await fetch(endpoint, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(Object.fromEntries(new FormData(form))),
        });
        if (!res.ok) throw new Error(String(res.status));
        showConfirmation();
      } catch {
        submit.disabled = false;
        const email = form.querySelector("#ask-email");
        setError(email, messages.send);
        email.focus();
      }
    });
  }
})();
