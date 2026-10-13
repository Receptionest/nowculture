# NowCulture 👟 — The Culture. On Your Feet.

An Instagram-style sneaker storefront for South Africa. Instead of a normal shop page,
customers **scroll a feed** — and every post is a real, buyable sneaker.

## Run it
Open `index.html` in a browser, or serve it:
```bash
python3 -m http.server 8000   # then visit http://localhost:8000
```
No build step, no backend, no dependencies.

## What's inside
| File | Purpose |
|---|---|
| `index.html` | Feed layout (top bar, stories, posts, explore grid, saved, bag, product sheet, reviews) |
| `assets/logo.svg` | The clean NowCulture "NC" logo (app-icon tile + gradient ring) |
| `assets/products.js` | **±175-product catalogue collected from sgmtouch.co.za** — every brand & combo collection |
| `assets/app.js` | Likes (incl. double-tap), comments, saves, search, filters, sort, cart, WhatsApp checkout (localStorage-persisted) |
| `assets/style.css` | Instagram-clean styling; every image `object-fit: cover` in a fixed 4:5 frame — always fits perfectly |
| `docs/NowCulture-Social-Media-and-WhatsApp-Marketing-Plan.pdf` | Full Instagram/TikTok/Facebook/WhatsApp marketing plan (10 pages) |
| `scripts/make_plan_pdf.py` | Regenerates the plan PDF (`pip install reportlab && python3 scripts/make_plan_pdf.py`) |

## Catalogue source (SGM Touch)
Scrolled on 13 Oct 2026 via sgmtouch.co.za collection pages — names & prices are the live listings,
images stream from the SGM Shopify CDN (width-optimised):
Nike (221 listings), Jordan (50), Adidas (57), New Balance (33), Lacoste (17), Puma (8), Converse (6),
Vans (3), Diesel (3), Bapesta (3), Timberland (3), Karl (3), Replay (3), plus all combo collections
(Sneaker Combos 117, Jordan Combo 56, Lowdunk Combo 52, Adidas/Airforce/Shox/Portal/TN/Puma/Timberland combos).
The ±175 unique products in `assets/products.js` are deduplicated; each card links to its original SGM product page.
To refresh: re-scrape the collection, replace rows in `assets/products.js` (format documented at the top of that file).

## Ordering
"Add to bag" → Checkout opens WhatsApp (+27 61 344 6518, SGM's number) with the full order pre-filled.
Free delivery + one free gift per order, as on SGM Touch.

Brand names belong to their respective owners; NowCulture is a concept storefront built on the SGM Touch catalogue.
