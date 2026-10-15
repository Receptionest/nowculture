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

## Pricing — SA market prices
Every single shoe is priced at current South African market/retail value for its model
(not a flat rate): Vans from R1,299 · Samba R1,899 · Speedcat R1,999 · Dunk Low R2,299 ·
Shox R4 R2,999 · NB 9060 R3,199 · Jordan 1 R3,699 · Jordan 3 R4,099 · Jordan 4 R4,199 ·
Bapesta R3,999 · Diesel R3,499 · Karl R3,599 · Timberland Premium 6-inch R4,999 ·
Travis Scott collab at resale market R9,499. Combos = both pairs at market price, less 30%
(the struck-through price shows the combined separate cost). Benchmarks checked Oct 2026
against Nike ZA, Shelflife, Timberland SA and SA brand retail. Re-check quarterly and edit
the price fields (3rd/4th values per row) in `assets/products.js`.

## Ordering
"Add to bag" → Checkout opens WhatsApp (+27 68 179 3036) with the full NowCulture order pre-filled.
Free delivery + one free gift per order.

Brand names belong to their respective owners. NowCulture is the store; everything is sold here.
