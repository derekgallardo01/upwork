# One-click feed capture (bookmarklet)

Instead of select-all-copy-paste of the whole Upwork page, use this bookmarklet.
It runs in **your own logged-in browser, only when you click it** — it is not a
bot and does not crawl Upwork. It reads the job data Upwork already embedded in
the page (`window.__NUXT__`) and downloads a small, clean `feed.json` that
`upwork-radar` scores directly.

> **Why not an automated scraper?** Upwork has no open jobs API and its Terms
> prohibit bots/automated scraping — an automated logged-in scraper risks
> **account suspension**. This bookmarklet stays on the right side of that line:
> you trigger it, in your session, for your own use.

## Install (30 seconds)

1. Show your browser's bookmarks bar (Chrome/Edge: `Ctrl/Cmd+Shift+B`).
2. Right-click the bookmarks bar → **Add page** / **Add bookmark**.
3. **Name:** `Upwork → feed.json`
4. **URL:** paste the entire `javascript:` line from
   [`bookmarklet.url.txt`](bookmarklet.url.txt) (it's one long line).
5. Save.

The readable source is [`bookmarklet.js`](bookmarklet.js); the `.url.txt` file is
just that file minified into a clickable bookmark.

## Use

1. Open a feed, e.g. <https://www.upwork.com/nx/find-work/most-recent> (also works
   on **U.S. only** and any **saved search**).
2. Click **Load More Jobs** a few times to pull more per capture.
3. Click the **Upwork → feed.json** bookmark. A file like
   `upwork-feed-most-recent.json` downloads, and an alert shows how many jobs were saved.
4. Score it:
   ```bash
   python -m upwork_radar analyze --feed upwork-feed-most-recent.json \
       --profile profile.json --top 8
   ```

## Tips

- Capture each feed/saved search separately (one click each) to widen coverage.
- The exported JSON has real fields — exact `$ spent`, real post timestamps,
  hourly min/max — so scoring is more accurate than parsing rendered text.
- No data leaves your machine: the bookmarklet only writes a local file.
