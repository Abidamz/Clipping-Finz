# Clipping-Finz

A 30-day clipping income project with a **₦2,000,000 target** before December.

## What's here

`index.html` — a single-file console that runs in any browser, no build step, no
dependencies. Data is stored in the browser's `localStorage`, so it stays on the
device you open it on.

Open it by double-clicking the file, or:

```bash
# any static server works
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.

## The two income streams

| Stream | What it is | 30-day target |
| --- | --- | --- |
| **A — Campaigns** | Clip approved creators' content; paid per verified 1,000 views | ₦500,000 |
| **B — Client edits** | Edit long videos into short clips for a fee | ₦1,500,000 |

Stream B is the reliable half: a client pays for the edit, not for the algorithm.

## The honest arithmetic

₦2,000,000 in 30 days is roughly **₦66,667 a day**.

| Route | What it demands |
| --- | --- |
| Campaign at ₦500 / 1K views | 4,000,000 views |
| Campaign at ₦1,000 / 1K views | 2,000,000 views |
| Campaign at $2.00 / 1K views (~₦3,000) | ~650,000 views |
| Client edits at ₦5,000 per clip | 400 clips |
| Client retainers at ₦60,000 / month | 33 clients |

So the target is a stretch, not a plan you can bank on. Treat anything above
₦300,000–₦600,000 as upside, and do not schedule wedding payments against the
best case.

## Console tabs

- **Dashboard** — progress, pace per day, both streams, start date for the 30 days
- **Income** — log each payment by stream; totals feed the dashboard
- **Clips** — clips produced, views, average views per clip
- **30-Day Plan** — a checklist that saves your progress
- **Calculator** — views needed to hit a target at a given CPM; client revenue maths
- **Client Kit** — price list, outreach templates, campaign caption bank, and the
  pre-submission checklist

## Rules that decide whether you get paid

Campaign clips are pass/fail. One missed requirement means the clip is rejected
and pays nothing:

- Footage only from the campaign's official content folder
- Required creator tag on **every** platform
- Disclosure hashtag (`#Ad`) in the caption
- Captions in your own words, matching the clip
- No invented facts, stats or dates

And before joining any campaign: check the payout threshold, the per-country
payout table (some campaigns pay nothing for certain viewer countries), whether
you have written rights to the footage, and whether anyone is asking you to pay
to join.

## Status

The scaffold and console are in place. Next: hook bank, posting schedule, and a
per-campaign payout estimator.

## Clipping Playbook (course)

`course/index.html` — a 30-lesson, 8-module course built from the clipping threads
the user collected, with the unverifiable parts stripped out.

- Modules: orientation, account setup, campaigns, cutting, testing, distribution,
  getting paid, client work.
- Progress checkboxes persist in localStorage; left nav tracks completion.
- Two appendices: **Cut list** (what was removed and why — location spoofing,
  earnings screenshots, paywall teases, multi-account farms, crypto QR Tweets) and
  **Sources** (every thread mapped to what it actually contributed, with a weight
  rating).
- Every lesson ends with a drill and, where relevant, a "watch out" box.
- No external dependencies; open the file directly in a browser.

## Launch kit (Kenya → Nigeria)

`course/launch-kit/` — a sellable 32-page workbook plus a 10-page internal launch plan,
built as PDFs from Python source. See `course/launch-kit/README.md` for the build commands,
the Systeme.io + Selar stack, and the finding that TikTok Ads cannot run on N40,000
($50/day minimum vs ~$30 total).
