/*
 * upwork-radar bookmarklet  (readable source)
 * -------------------------------------------------------------------------
 * Runs in YOUR logged-in browser when YOU click it — it is not a bot and does
 * not crawl Upwork. It reads the job data Upwork already embedded in the page
 * (window.__NUXT__) and downloads a small, clean feed.json that upwork-radar
 * can score directly.
 *
 * Install: see BOOKMARKLET.md for the one-line `javascript:` version to paste
 * into a browser bookmark. This file is the human-readable original.
 *
 * Usage: open https://www.upwork.com/nx/find-work/most-recent (or any feed /
 * saved search), click "Load More Jobs" a few times to pull more, then click
 * the bookmark. A feed.json downloads. Run:
 *   python -m upwork_radar analyze --feed feed.json --profile profile.json
 */
(function () {
  var nuxt = window.__NUXT__;
  if (!nuxt || !nuxt.state) {
    alert("upwork-radar: couldn't find Upwork job data on this page.\n" +
          "Open a Find Work feed (e.g. /nx/find-work/most-recent) and retry.");
    return;
  }
  var state = nuxt.state;

  // Collect jobs from whichever feeds are present on this page.
  var feeds = ["feedMostRecent", "feedBestMatch", "feedDomestic", "feedMy"];
  var raw = [];
  feeds.forEach(function (key) {
    var f = state[key];
    if (f && Array.isArray(f.jobs)) raw = raw.concat(f.jobs);
  });
  if (!raw.length) {
    alert("upwork-radar: no jobs found in the current feed.");
    return;
  }

  var now = Date.now();

  function minutesSince(iso) {
    if (!iso) return null;
    var t = Date.parse(iso);
    if (isNaN(t)) return null;
    return Math.max(0, Math.round((now - t) / 60000));
  }

  function isVerified(client) {
    var pv = client && client.paymentVerificationStatus;
    if (pv === 1 || pv === "1") return true;
    if (typeof pv === "string") return /^verif/i.test(pv);
    return false;
  }

  function normalize(job) {
    var client = job.client || {};
    var hb = job.hourlyBudget || {};
    var hasRange = (hb.min || hb.max);
    var pricing, budget = null, lo = null, hi = null;

    // type 2 == hourly in Upwork's state; fall back to a present hourly range.
    if (job.type === 2 || job.type === "hourly" || hasRange) {
      pricing = "hourly";
      lo = hb.min || null;
      hi = hb.max || null;
    } else {
      pricing = "fixed";
      budget = (job.amount && job.amount.amount) || null;
    }

    var skills = (job.attrs || [])
      .map(function (a) { return a && (a.prettyName || a.prefLabel); })
      .filter(Boolean);

    var posted = job.publishedOn || job.createdOn || null;

    return {
      title: job.title || "",
      url: job.ciphertext ? "https://www.upwork.com/jobs/" + job.ciphertext : null,
      description: job.description || "",
      pricing_type: pricing,
      budget: budget,
      rate_low: lo,
      rate_high: hi,
      experience: job.tierText || job.tier || null,
      proposals_raw: job.proposalsTier || null,
      posted_raw: posted,
      posted_minutes: minutesSince(posted),
      skills: skills,
      payment_verified: isVerified(client),
      client_rating: (client.totalFeedback != null ? client.totalFeedback : null),
      client_spent: (client.totalSpent != null ? client.totalSpent : 0),
      client_country: (client.location && client.location.country) || null
    };
  }

  // De-duplicate by URL/title across feeds.
  var seen = {};
  var jobs = [];
  raw.forEach(function (j) {
    var rec = normalize(j);
    var key = (rec.url || rec.title).toLowerCase();
    if (!seen[key]) { seen[key] = 1; jobs.push(rec); }
  });

  var topic = (state.topics && state.topics.currentTopic) || "feed";
  var payload = {
    captured_at: new Date(now).toISOString(),
    source: topic,
    count: jobs.length,
    jobs: jobs
  };

  // Download as feed.json.
  var blob = new Blob([JSON.stringify(payload, null, 2)], { type: "application/json" });
  var a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "upwork-feed-" + topic + ".json";
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  setTimeout(function () { URL.revokeObjectURL(a.href); }, 1000);

  alert("upwork-radar: saved " + jobs.length + " jobs to " + a.download);
})();
