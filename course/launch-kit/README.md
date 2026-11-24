# Launch pack — Kenya first, Nigeria second

Two PDFs, built from source so they can be regenerated after any edit.

| File | What it is | Sell it? |
| --- | --- | --- |
| `Clipping-From-Zero-Workbook.pdf` | 33 pages. Six parts, 24 chapters, 30-day log, designed cover. | **Yes** — this is the product |
| `Launch-Plan-Kenya-Nigeria-30-Days.pdf` | 11 pages. Budget reality, funnel, ad scripts, calendar, stop rules. | No — internal |
| `cover-square-1080.png` | Product image for the Selar listing and social posts. | Use as artwork |
| `cover-story-1080x1920.png` | Vertical promo image (story / Reel cover / status). | Use as artwork |

## The headline finding

**TikTok Ads will not run on ₦40,000.** The platform minimum is $50/day at campaign level
and $20/day per ad group. ₦40,000 is about $30 — less than one day, not four weeks.

The plan in the PDF therefore uses **Meta** (minimum ~$1–5/day, ~KSh 500/day practical in
Kenya) for a six-day test at KSh 500/day, and recommends spending **nothing** until:

1. a real Kenyan has completed checkout with real money, and
2. one stranger has bought without knowing you.

## Stack

- **Systeme.io** (free plan) — landing page, email capture, course area.
  Ceiling: 2,000 contacts, 3 funnels, 1 course, 1 automation rule, $10,000 lifetime sales.
- **Selar** — checkout in KES with M-Pesa. 5% + KSh 20 per Kenyan sale.
  Payouts: NGN in 1 business day, KES in 4.
- **Price** KSh 1,499 (≈ ₦15,500). Do not fake a discount.

## What the numbers actually say

| Target | Sales at KSh 1,499 |
| --- | --- |
| ₦200,000 | 13 |
| ₦500,000 | 32 |
| ₦1,000,000 | 65 |
| ₦2,000,000 | 129 |

Ten sales in 30 days is a **successful first launch** and worth roughly ₦155,000.
₦2,000,000 needs 129 sales and paid reach far beyond ₦40,000.

## Files

```
launch-kit/
  _pdfkit.py                     shared PDF engine (reportlab, DejaVu fonts)
  cover.py                       full-bleed vector cover pages, both PDFs
  make_images.py                 generates the two promo images from PDFs
  build_product.py               builds the workbook (two-pass, for TOC page numbers)
  build_plan.py                  builds the operating pack
  sec1.py ... sec6.py            workbook content, one module per part
  Clipping-From-Zero-Workbook.pdf
  Launch-Plan-Kenya-Nigeria-30-Days.pdf
```

Rebuild both:

```bash
cd course/launch-kit
pip install --break-system-packages reportlab fonttools
python3 build_product.py && python3 build_product.py   # twice: TOC page numbers
python3 build_plan.py
python3 make_images.py
```

`build_product.py` must run twice on a clean checkout — the first pass records the page
numbers each chapter lands on (`.toc_marks.json`), the second writes them into the
contents page.

## Before spending the first naira

- [ ] A real Kenyan completed checkout with real money and was refunded
- [ ] Sales page states the price in KES and says what the product is **not**
- [ ] Workbook PDF is finished, readable on a phone, no placeholder text
- [ ] Three creatives exist, each under 25 seconds, none containing an income claim
- [ ] The product is yours — not compiled from someone else's tutorials
- [ ] Stop rules written down before launch

## Currency assumptions

₦1,340 = $1 · KSh 1 = ₦10.35 · KSh 1,499 ≈ ₦15,500. Verify live rates before pricing.
