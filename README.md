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
| `assets/products.js` | **175-product NowCulture catalogue** — every brand & combo, all sold on this site |
| `assets/images/` | **All 175 shoe images, hosted locally on this site** (`001`–`175`, per `manifest.json`) |
| `assets/app.js` | Likes (incl. double-tap), comments, saves, search, filters, sort, cart, WhatsApp checkout (localStorage-persisted) |
| `assets/style.css` | Instagram-clean styling; every image `object-fit: cover` in a fixed 4:5 frame — always fits perfectly |

## Catalogue
All 175 shoes — Nike, Jordan, Adidas, New Balance, Lacoste, Puma, Converse, Vans, Diesel, Bapesta,
Timberland, Karl Lagerfeld, Replay, plus every sneaker combo — live entirely on this site:
names, prices and images (`assets/images/`) are all local. Nothing is hotlinked or credited elsewhere.
To add a shoe: drop its image into `assets/images/` as the next number and add a row in
`assets/products.js` (format documented at the top of that file).

## Ordering
"Add to bag" → Checkout opens WhatsApp (+27 61 344 6518) with the full NowCulture order pre-filled.
Free delivery + one free gift per order.

Brand names belong to their respective owners. NowCulture is the store; everything is sold here.
