/* Branching scenario player. Data comes from data.js (window.MODULE_DATA). */
(function () {
  var data = window.MODULE_DATA;
  var root = document.getElementById("app");
  var scores = [];
  var index = 0;
  var SCORE = { strong: 100, recoverable: 70, failure: 0 };

  function el(tag, cls, html) {
    var n = document.createElement(tag);
    if (cls) { n.className = cls; }
    if (html !== undefined) { n.innerHTML = html; }
    return n;
  }

  function shuffle(a) {
    for (var i = a.length - 1; i > 0; i--) {
      var k = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[k]; a[k] = t;
    }
    return a;
  }

  function text(s) {
    return (s || "").replace(/\[binding: ([^\]]+)\]/g, '<span class="binding">binding: $1</span>');
  }

  function media(node, into) {
    if (!node.media) { return; }
    var m;
    if (/\.(mp4|webm)(\?|$)/i.test(node.media)) {
      m = el("video", "media"); m.src = node.media; m.controls = true; m.playsInline = true;
    } else if (/\.(png|jpe?g|gif|webp|svg)(\?|$)/i.test(node.media)) {
      m = el("img", "media"); m.src = node.media; m.alt = "";
    } else {
      m = el("iframe", "media"); m.src = node.media; m.style.aspectRatio = "16 / 9"; m.style.border = "0";
      m.setAttribute("allowfullscreen", "");
    }
    into.appendChild(m);
  }

  function header(sc) {
    var frag = document.createDocumentFragment();
    frag.appendChild(el("p", "eyebrow", data.id + " &middot; Scenario " + (index + 1) + " of " + data.scenarios.length));
    frag.appendChild(el("h1", null, text(sc.title)));
    return frag;
  }

  function showSetup() {
    var sc = data.scenarios[index];
    root.innerHTML = "";
    if (!SCORM.isLive()) { root.appendChild(el("div", "preview", "Preview mode: no LMS connected, results are not recorded.")); }
    root.appendChild(header(sc));
    media(sc, root);
    root.appendChild(el("p", null, text(sc.setup)));
    var go = el("button", "primary", "Begin");
    go.onclick = function () { showNode(sc.start); };
    root.appendChild(go);
  }

  function showNode(id) {
    var sc = data.scenarios[index];
    var node = sc.nodes[id];
    root.innerHTML = "";
    root.appendChild(header(sc));
    if (!node) { root.appendChild(el("p", null, "Missing node: " + id)); return; }
    media(node, root);

    if (node.type === "decision") {
      if (id === sc.start) { root.appendChild(el("p", "situation", text(sc.setup))); }
      root.appendChild(el("p", null, text(node.prompt)));
      var list = el("div", "choices");
      shuffle(node.choices.slice()).forEach(function (c) {
        var b = el("button", null, text(c.label));
        b.onclick = function () { showNode(c.to); };
        list.appendChild(b);
      });
      root.appendChild(list);
      return;
    }

    var end = node.end;
    var box = el("div", "panel" + (end ? " end-" + end : ""));
    if (node.consequence) { box.appendChild(el("div", "label", "What happens")); box.appendChild(el("p", null, text(node.consequence))); }
    if (node.feedback) { box.appendChild(el("div", "label", "Why")); box.appendChild(el("p", null, text(node.feedback))); }
    root.appendChild(box);

    if (node.rationale) {
      var reveal = el("button", null, "How an expert reads this");
      reveal.onclick = function () {
        var r = el("div", "panel");
        r.appendChild(el("div", "label", "Expert rationale"));
        r.appendChild(el("p", null, text(node.rationale)));
        reveal.replaceWith(r);
      };
      root.appendChild(reveal);
    }

    var next = el("button", "primary", end ? "Continue" : "Next");
    next.style.marginTop = "16px";
    next.onclick = function () {
      if (!end) { showNode(node.next); return; }
      scores.push(SCORE[end]);
      index += 1;
      if (index < data.scenarios.length) { showSetup(); } else { showEnd(); }
    };
    root.appendChild(next);
  }

  function showEnd() {
    var total = scores.reduce(function (a, b) { return a + b; }, 0) / scores.length;
    SCORM.finish(total, data.mastery);
    root.innerHTML = "";
    root.appendChild(el("p", "eyebrow", data.id));
    root.appendChild(el("h1", null, "Done"));
    root.appendChild(el("p", null, data.closing || "Bring one thing from this into your next shift."));
    var again = el("button", null, "Run it again");
    again.onclick = function () { scores = []; index = 0; showSetup(); };
    root.appendChild(again);
  }

  SCORM.init();
  window.addEventListener("beforeunload", SCORM.close);
  document.title = data.title;
  showSetup();
})();
