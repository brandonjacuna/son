/* Minimal SCORM 1.2 runtime bridge. Falls back to preview mode when no LMS is present. */
var SCORM = (function () {
  var api = null;
  var active = false;

  function findAPI(win) {
    var tries = 0;
    try {
      while (win && !win.API && win.parent && win.parent !== win && tries < 10) {
        win = win.parent;
        tries++;
      }
      return win && win.API ? win.API : null;
    } catch (e) {
      return null; /* cross-origin parent: no reachable LMS, run in preview */
    }
  }

  function init() {
    try {
      api = findAPI(window) || (window.opener ? findAPI(window.opener) : null);
    } catch (e) { api = null; }
    if (!api) { return false; }
    var r = api.LMSInitialize("");
    active = r === "true" || r === true;
    if (active) {
      var status = api.LMSGetValue("cmi.core.lesson_status");
      if (status === "not attempted" || status === "") {
        api.LMSSetValue("cmi.core.lesson_status", "incomplete");
      }
      api.LMSCommit("");
    }
    return active;
  }

  function finish(score, mastery) {
    if (!active) { return; }
    api.LMSSetValue("cmi.core.score.min", "0");
    api.LMSSetValue("cmi.core.score.max", "100");
    api.LMSSetValue("cmi.core.score.raw", String(Math.round(score)));
    api.LMSSetValue("cmi.core.lesson_status", score >= mastery ? "passed" : "failed");
    api.LMSCommit("");
  }

  function close() {
    if (active) { api.LMSFinish(""); active = false; }
  }

  return { init: init, finish: finish, close: close, isLive: function () { return active; } };
})();
