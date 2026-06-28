# First 30 days on Upwork — tactical checklist

Concrete actions, ordered. Pair with the 30-60-90 plan in
[`upwork-playbook.md §4`](upwork-playbook.md#4-30-60-90-day-plan).

---

## Day 0 — Before opening Upwork

- [ ] **Pin the 6 runnable demos** on your GitHub profile
      (github.com/derekgallardo01 → "Customize your pins"). 60 sec, no API.
- [ ] **Set GitHub profile bio + hireable**:
      ```
      gh auth refresh -h github.com -s user
      echo '{"name":"Derek Gallardo","bio":"Microsoft 365 + AI engineer · Copilot Studio · Power Platform · RAG with citations + evals. Pinned repos = runnable demos.","hireable":true}' | gh api -X PATCH user --input -
      ```
- [ ] **Profile photo** ready (head + shoulders, neutral background, looking at camera).
      Upwork rejects unclear / silly photos and that's a 3-5 day delay.
- [ ] **Stripe / payment method** verified on Upwork (do this first; takes 24-48 hours).

---

## Day 1 — Profile + first proposals

### Profile setup (~90 min)

- [ ] Paste main profile title + overview from
      [`profile-and-proposals.md`](profile-and-proposals.md).
- [ ] Add the two specialized profiles (also in `profile-and-proposals.md`).
- [ ] **Hourly rate: USD 110** (mid-band from the playbook). You'll raise
      this in 30 days.
- [ ] Skills tags: paste the suggested list from `profile-and-proposals.md`.
- [ ] **Portfolio entries**: link 3 of the 6 runnable repos at minimum
      (copilot-studio-support-agent, rag-over-docs-kit, powerbi-fabric-consolidation
      are the strongest visual cluster). Each portfolio entry should
      have:
      - A short description (paste from the repo's README intro).
      - A link to the live Pages demo (the runnables all have one).
      - A screenshot (download from `docs/screenshots/` in each repo).
- [ ] Identity verification submitted. Required for "Top Rated" later.

### First 3 proposals (~60 min)

- [ ] Scan Upwork's "Most recent" feed in your target categories.
- [ ] Apply the 30-second filter from `upwork-playbook.md §1`.
- [ ] Pick 3 jobs that pass; bid using the templates in
      `profile-and-proposals.md §Cover letter`.
- [ ] **Two specific questions** at the end of each — that's the
      conversion signal.

---

## Days 2-5 — Cadence

Daily (~75 min):

- [ ] **5 proposals sent.** Not less; not more. (Quality > quantity above 5.)
- [ ] **Reply to any inbound** within 4 hours during business hours
      (Upwork's response-time metric matters for search ranking).
- [ ] **Log each send** in a tracking sheet — columns: posting URL,
      date, replied? (Y/N), reply type (interview / decline / no
      response), notes.

Friday wrap-up (~15 min):

- [ ] Look at the week's tracking sheet.
- [ ] Which category had the highest reply rate? Which had zero replies?
      Bias next week toward what worked.

---

## Days 6-10 — First interview

When you get the first "interested" reply:

- [ ] Send the **paid 1-hour scoping call** offer using template A4
      from [`inbound-replies.md`](inbound-replies.md).
- [ ] If they accept: **schedule within 48 hours**. Send a calendar
      link, not "what time works for you?"
- [ ] Prep: read their job post 3 times, scan their Upwork history
      (other jobs they've posted), have 5 written questions ready.
- [ ] During the call: ask the questions, take notes, **don't quote
      live**. End with "I'll send a written recommendation + price
      within 24 hours."
- [ ] Within 24 hours: deliver the written recommendation as a SOW
      using the template from
      [`ms-delivery-discovery-kit/sow-template.md`](https://github.com/derekgallardo01/ms-delivery-discovery-kit/blob/main/sow-template.md).

---

## Days 11-20 — First engagement

If the SOW is signed:

- [ ] **Set up the eval set first** — even one case. The eval set is
      what makes the build measurable. Add cases as you discover
      requirements.
- [ ] Fill the handover guide + runbook **as you build** (per
      [`project-handover-pack`](https://github.com/derekgallardo01/project-handover-pack)
      `docs/getting-started.md`).
- [ ] Send a brief status update every 3-4 days, even if nothing
      changed. Silence makes clients nervous.
- [ ] Don't ship until the eval set is 100% green AND you've done a
      smoke test in production-like conditions.

---

## Days 21-30 — Acceptance, handover, review

- [ ] Production cutover with the client watching (Loom or screen-share).
- [ ] Deliver the handover pack (guide + runbook + Loom). Take the 3
      minutes to actually record the Loom; it's the single biggest
      review-quality lever.
- [ ] **Invoice the same day** as acceptance — don't drift.
- [ ] **7-10 days after delivery**: send the review request (template
      C1 from `inbound-replies.md`). Stop asking after one nudge.

---

## End of Day 30 — Review and adjust

- [ ] How many proposals sent total?
- [ ] How many replies?
- [ ] How many converted to a scoping call?
- [ ] How many converted to a signed SOW?
- [ ] How much cash in the door?
- [ ] How much cash invoiced but unpaid?

Reference targets from the playbook:

- **Proposals sent:** ~100 (5/day × 20 working days)
- **Reply rate:** 3-8% to start = ~3-8 replies
- **Scoping calls booked:** 1-2
- **Engagements completed:** 1-2 (even small)
- **Cash:** USD 2,000-5,000

If you're well under these: bid on jobs above your floor (your rate is
too low / proposals too generic / wrong categories). If you're well
over: raise the hourly rate by 20%, drop the bottom-quartile categories.

---

## Don't-do list

These eat your first 30 days and produce nothing:

- ❌ Spending more than 2 hours on a proposal. If the job justifies that,
      it's a paid scoping call, not a free pitch.
- ❌ Bidding on jobs below your floor "to build reviews." Reviews anchor
      to rate — low-rate reviews hurt you on the next pricing
      conversation.
- ❌ Joining Discord / Telegram / WhatsApp groups the client suggests.
      Upwork keeps your conversations on-platform for a reason.
- ❌ Sending follow-ups more than once after silence. Hounding clients
      costs you more goodwill than the chance of conversion is worth.
- ❌ Telling a client "I've never done X before but I'm willing to
      learn." There's a freelancer who has done X — they'll get hired.
