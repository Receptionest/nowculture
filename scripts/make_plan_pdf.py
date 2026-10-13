#!/usr/bin/env python3
"""Generates docs/NowCulture-Social-Media-and-WhatsApp-Marketing-Plan.pdf"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                PageBreak, KeepTogether, HRFlowable)

OUT = "docs/NowCulture-Social-Media-and-WhatsApp-Marketing-Plan.pdf"
INK = colors.HexColor("#0b0b0f"); PINK = colors.HexColor("#d62976"); ORANGE = colors.HexColor("#fa7e1e")
PURPLE = colors.HexColor("#962fbf"); GREY = colors.HexColor("#555555"); LIGHT = colors.HexColor("#f6f2f8")
WA = colors.HexColor("#128c4b")

def S(name, **kw):
    base = dict(fontName="Helvetica", fontSize=10.5, leading=15, textColor=INK, spaceAfter=5, alignment=TA_LEFT)
    base.update(kw); return ParagraphStyle(name, **base)

TITLE = S("t", fontName="Helvetica-Bold", fontSize=30, leading=34, textColor=colors.white)
SUB   = S("sub", fontSize=13, leading=18, textColor=colors.HexColor("#ffe3ef"))
_H1 = S("h1", fontName="Helvetica-Bold", fontSize=17, leading=21, textColor=PINK, spaceBefore=14, spaceAfter=7)
_H2 = S("h2", fontName="Helvetica-Bold", fontSize=12.5, leading=16, textColor=INK, spaceBefore=10, spaceAfter=4)
def H1(txt): return Paragraph(txt, _H1)
def H2(txt): return Paragraph(txt, _H2)
BODY = S("b"); SMALL = S("sm", fontSize=9, leading=12.5, textColor=GREY)
BULLET = S("bul", leftIndent=13, bulletIndent=4, spaceAfter=3)
CELL = S("c", fontSize=8.8, leading=11.5); CELLB = S("cb", fontName="Helvetica-Bold", fontSize=8.8, leading=11.5, textColor=colors.white)
QUOTE = S("q", fontName="Helvetica-Oblique", fontSize=10, leading=14, textColor=GREY, leftIndent=10)

def bullets(items):
    return [Paragraph(f"•&nbsp;&nbsp;{i}", BULLET) for i in items]

def table(data, widths, header=True):
    t = Table([[Paragraph(str(c).replace("\n","<br/>"), CELLB if (header and r == 0) else CELL) for c in row] for r, row in enumerate(data)],
              colWidths=widths, repeatRows=1 if header else 0, hAlign="LEFT")
    style = [("VALIGN", (0,0), (-1,-1), "TOP"), ("GRID", (0,0), (-1,-1), .4, colors.HexColor("#ddd3e0")),
             ("LEFTPADDING", (0,0), (-1,-1), 5), ("RIGHTPADDING", (0,0), (-1,-1), 5),
             ("TOPPADDING", (0,0), (-1,-1), 4), ("BOTTOMPADDING", (0,0), (-1,-1), 4),
             ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, LIGHT])]
    if header: style.append(("BACKGROUND", (0,0), (-1,0), PINK))
    t.setStyle(TableStyle(style)); return t

def header_footer(canvas, doc):
    canvas.saveState()
    if doc.page > 1:
        canvas.setFillColor(PINK); canvas.rect(0, A4[1]-14*mm, A4[0], 14*mm, stroke=0, fill=1)
        canvas.setFillColor(colors.white); canvas.setFont("Helvetica-Bold", 10)
        canvas.drawString(15*mm, A4[1]-9*mm, "NOWCULTURE  —  Social Media & WhatsApp Marketing Plan")
        canvas.setFont("Helvetica", 8); canvas.drawRightString(A4[0]-15*mm, A4[1]-9*mm, "nowculture.co.za  ·  The Culture. On Your Feet.")
        canvas.setFillColor(GREY); canvas.setFont("Helvetica", 8)
        canvas.drawString(15*mm, 10*mm, "Confidential — prepared for NowCulture, October 2026. Catalogue & pricing: SGM Touch (sgmtouch.co.za).")
        canvas.drawRightString(A4[0]-15*mm, 10*mm, f"Page {doc.page}")
    canvas.restoreState()

story = []
# ---------- COVER ----------
cover = Table([[Paragraph("NOWCULTURE", TITLE)],
               [Paragraph("The Culture. On Your Feet.", SUB)],
               [Spacer(1, 6*mm)],
               [Paragraph("<b>FULL SOCIAL MEDIA &amp; WHATSAPP MARKETING PLAN</b><br/>Instagram · TikTok · Facebook · WhatsApp Business", S("cs", fontSize=12, leading=17, textColor=colors.white))],
               [Spacer(1, 8*mm)],
               [Paragraph("Prepared: 13 October 2026  |  Market: South Africa  |  Storefront: nowculture (this website)<br/>Catalogue: 160+ sneakers &amp; sneaker combos from SGM Touch — Nike, Jordan, Adidas, New Balance, Lacoste, Puma, Converse, Vans, Diesel, Bapesta, Timberland, Karl Lagerfeld, Replay<br/>Price architecture: singles R1,250–R1,890 · combos R1,599–R3,299 · free delivery · one free gift per order", S("cs2", fontSize=9.5, leading=14, textColor=colors.HexColor("#f3d9e8")))],
               ], colWidths=[170*mm])
cover.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), INK), ("LEFTPADDING", (0,0), (-1,-1), 16),
                           ("RIGHTPADDING", (0,0), (-1,-1), 16), ("TOPPADDING", (0,0), (-1,-1), 10),
                           ("BOTTOMPADDING", (0,0), (-1,-1), 10), ("ROUNDEDCORNERS", [6,6,6,6])]))
story += [Spacer(1, 18*mm), cover, Spacer(1, 10*mm),
          Paragraph("<b>One-line strategy:</b> Run NowCulture like a social feed, sell like a conversation. Every post is a product, every product is one tap from a WhatsApp checkout — because in South Africa, the sale closes in the chat, not on the website.", BODY),
          Paragraph("<b>North-star goal (first 90 days):</b> 25,000 Instagram followers · 5,000 WhatsApp opt-ins · 600 orders · R900k+ revenue at an average order value of ±R1,550 · cost per order under R120.", BODY),
          Paragraph("How to use this plan: Section 2 sets the brand, Section 3–5 give channel playbooks you can execute today, Section 6 is a ready-to-post 30-day calendar, Section 7 contains copy-paste captions and WhatsApp scripts, Sections 8–10 cover paid ads, budget, KPIs and the weekly operating rhythm.", SMALL)]

# ---------- 1. Snapshot ----------
story += [H1("1. Business snapshot — what we are selling"), Paragraph(
    "NowCulture is an Instagram-style sneaker storefront. Instead of a traditional catalogue, customers scroll a feed of posts — and every post is a real, buyable sneaker sourced from SGM Touch (sgmtouch.co.za), with live pricing in Rand, UK sizes 3–9, a working shopping bag and one-tap WhatsApp checkout to +27 61 344 6518.", BODY)]
story += bullets([
 "<b>Singles (R1,250–R1,890):</b> 110+ styles across 13 brands. Hero lines: Nike Shox/Air Max 90/P-6000/Rift, Jordan 1 &amp; 3 &amp; 4, Adidas Samba Jane/SL72/Spezial, New Balance 9060/1000/Abzorb, Lacoste Baseshot/T-Clip, Puma Speedcat/XL, Converse Chuck 70, Timberland Premium, Diesel Ukiyo, Bapesta, Karl, Replay, Vans.",
 "<b>Sneaker Combos (R1,599–R3,299) — the signature offer:</b> two pairs for one price (e.g. Jordan + Air Force R1,899 vs R2,720 separately; Timberland + Timberland R3,299 vs R4,500). Combos are NowCulture's unfair advantage: higher basket size, built-in 'tag your person' virality, and a story competitors can't copy price-for-price.",
 "<b>Trust stack:</b> free nationwide delivery, one free gift per order, verified-customer reviews (Thandi, Lerato, Sipho, Precious), size-swap support on WhatsApp.",
 "<b>Audience:</b> SA sneaker culture, 16–34, mobile-first, price-smart but drip-obsessed — students, young professionals, resellers and gift-buyers (combos = 'one for me, one for bae/friend')."])
story += [H1("2. Brand system"), ]
story += [table([["Element","NowCulture standard"],
 ["Logo","“NC” monogram in a rounded app-icon tile, Instagram-gradient ring (assets/logo.svg). Always on white or black; never stretch, never recolour the wordmark."],
 ["Wordmark","now<b>culture</b> — lowercase, gradient on 'culture', '.co.za' in grey. Username everywhere: @nowculture / @nowculture.co.za (secure both)."],
 ["Voice","Mzansi street, zero cringe. Short lines. Emoji as punctuation, not decoration. Mix English with light vernacular (sharp, danko, ayeye) — never forced."],
 ["Colours","Black #0B0B0F, white, Instagram gradient (#feda75 → #fa7e1e → #d62976 → #962fbf → #4f5bd5), WhatsApp green #25D366 only for chat CTAs."],
 ["Hashtag bank","#NowCulture #KicksSA #SneakerCulture #MzansiStyle #SGM #SneakerCombos #Take2 + per-post brand tag (#Nike #Jordan1 #Samba #NewBalance9060). Max 8 per caption."],
 ["Handles to secure today","Instagram @nowculture.co.za · TikTok @nowcultureza · Facebook Page 'NowCulture ZA' · WhatsApp Business +27 61 344 6518 · Link-in-bio: this website."]],
 [28*mm, 142*mm])]

# ---------- 3 Instagram ----------
story += [PageBreak(), H1("3. Instagram playbook — the shop window"),
 Paragraph("Instagram is NowCulture's home ground: the website already looks and behaves like Instagram (feed, stories, likes, saves, comments), so social content and store are one continuous experience. Link every post to the matching product on the site.", BODY),
 H2("Profile setup (do once, do properly)")]
story += bullets([
 "Name field (searchable): 'NowCulture 👟 Sneakers & Combos SA'. Bio: 'The Culture. On Your Feet. 🇿🇦 / Singles R1,450 · Combos from R1,599 / 🚚 Free delivery · 🎁 Free gift per order / 👇 Shop the feed'.",
 "Highlights (use site story covers): New Drops · Combos 🎁 · Nike · Jordan · Adidas · Reviews ⭐ · How to Order · Sizes.",
 "Shop/product tags on every post; pinned posts: (1) 'How to order in 60 seconds', (2) 'Combos explained — 2 pairs, 1 price', (3) 'Reviews wall'.",
 "Post the website's product photos 1:1 or 4:5, object-fit, clean background — exactly as they appear in the feed so the tap-through feels seamless."])
story += [H2("Weekly content engine — 5 pillars")]
story += [table([["Pillar","Format","Per week","Example"],
 ["1. The Drop","Feed post + Reel try-on/on-feet","3 posts, 2 Reels","'NIKE SHOX WHITE METALLIC just landed — R1,450'"],
 ["2. Combo Culture","Carousel: pair A + pair B + saving","2 carousels","'Jordan + Airforce R1,899. Separately R2,720. Danko.'"],
 ["3. Culture & Community","UGC repost, polls, 'this or that' stories","Daily stories","Customer on-feet pics; 'Samba Jane or Speedcat?' poll"],
 ["4. Proof","Review screenshot, unboxing, delivery POV","1 post, 2 stories","Thandi's 5★ review as a designed quote card"],
 ["5. The Plug (offer)","Countdown, payday & student specials","1 post","'Payday Combo Weekend — extra gift on combos, ends Sunday'"]],
 [30*mm, 48*mm, 24*mm, 68*mm])]
story += bullets([
 "<b>Cadence:</b> 1 feed post/day (18:00–20:00 SAST peak), 1 Reel/day (Reels are the discovery engine — on-feet rotation, unboxing ASMR, 'R1,450 vs R1,899 fit check'), 5–10 stories/day.",
 "<b>Stories system:</b> Morning = new drop; Midday = poll/quiz; Afternoon = combo of the day with price flag; Evening = 'WhatsApp us your size' sticker link to wa.me/27613446518.",
 "<b>Engagement loop:</b> reply to every comment in 1 hour; comment meaningfully on 15 culture accounts/day (sneaker pages, stylists, campuses); weekly Live 'Size & Stock Check' (Fridays 19:00).",
 "<b>Growth mechanics:</b> monthly 'Tag & Win a Combo' giveaway (follow + tag 2 friends + share to story = entry, winner announced on Live); collab posts with 2 micro-creators/month (5k–50k followers, product-for-post + affiliate code)."])

# ---------- 4 TikTok/FB ----------
story += [H1("4. TikTok & Facebook playbooks"), H2("TikTok — the discovery rocket")]
story += bullets([
 "3 videos/day for the first 30 days, then 1–2/day. Formats that sell sneakers: (1) 7-second on-feet spin with price overlay, (2) 'Two pairs for R1,899?!' combo reveal, (3) unboxing + quality close-ups, (4) 'POV: your NowCulture parcel arrived' delivery joy, (5) duets/stitches of celeb fits matched to a NowCulture pair ('Get the look for R1,450').",
 "Hook in first 2 seconds, captions burnt in, trending SA sounds (amapiano/gqom instrumentals), post 07:00, 13:00, 19:30. Pin the combo explainer. Bio link → website; every video ends 'WhatsApp link in bio — send your size'.",
 "Go LIVE twice a week (stock room sessions): show pairs, call out sizes left, drop a live-only combo code."])
story += [H2("Facebook — the trust & parents' rand")]
story += bullets(["Mirror Instagram posts + join 20 SA buy/sell & sneaker groups (post value-first, no spam; combos perform exceptionally with gift-buyers).",
 "Marketplace listings for the top 20 products with WhatsApp CTA; Events for sale weekends; retargeting via the Meta pixel (Section 8).",
 "Facebook audience skews 28–45 with cards and salaries — lead with Timberland, Lacoste, Karl and 'gift a combo' angles on payday weekends."])

# ---------- 5 WhatsApp ----------
story += [H1("5. WhatsApp marketing playbook — where the sale closes"),
 Paragraph("WhatsApp is NowCulture's till point. The website's checkout already opens a pre-filled WhatsApp order to +27 61 344 6518. Everything below turns that number into a revenue channel — compliantly: only message people who opted in (clicked a wa.me link, ordered, or replied START). Never buy lists; honour STOP instantly. POPIA applies.", BODY),
 H2("Setup checklist (Day 1)")]
story += bullets([
 "WhatsApp Business app (or API via a BSP when volume exceeds ±200 chats/day): business profile with logo, hours 08:00–21:00 SAST, catalogue with the top 40 products (photos, price, 'View on website' link).",
 "Greeting message, away message, and Quick Replies for the 12 scripts in Section 7. Labels: New Lead / Size Confirmed / Paid / Dispatched / Delivered / VIP / Reseller.",
 "Click-to-WhatsApp everywhere: website buttons, Instagram story link stickers, TikTok bio, Facebook ads, QR code (Section 5.4) on every parcel and flyer."])
story += [H2("The 5 money flows"),
 table([["Flow","Trigger","Goal","Message rhythm"],
 ["1. Order close","Customer taps order/checkout on site","Payment within 30 min","Auto pre-filled order → confirm stock & size → payment link/EFT details → proof of payment → dispatch note. SLA: first human reply < 5 min in hours."],
 ["2. Abandoned bag","Bag created, no order in 2 hrs (site prompt: 'Send my bag to WhatsApp')","Recover 15–25%","1 nudge at +2h, 1 at +24h with combo upsell, then stop."],
 ["3. Broadcast drops","New stock / sale (opted-in list only)","Sell-through in 48h","Max 2 broadcasts/week, Tue & Fri 18:30. Photo + price + 'Reply with size'. Segment: brand interest & past buyers."],
 ["4. Post-purchase","Delivered","Review + repeat order","Delivery check (+1 day) → review ask (+3 days, incentivise with R50 next-order voucher) → 'your combo match' (+14 days)."],
 ["5. VIP & resellers","3+ orders, or reseller enquiry","Loyalty & bulk","Early access 24h before public drops; reseller price list (SGM reseller groups exist — mirror that energy); birthday voucher."]],
 [26*mm, 42*mm, 32*mm, 70*mm]),
 H2("Broadcast rules that protect the number"),
 Paragraph("Keep broadcasts under 2/week, always lead with value (drop/saving), personalise with first name, include an easy opt-out line ('Reply STOP to opt out'), and warm the number with conversational replies before scaling volume — bulk-blasting a cold number gets it banned. Quality rating (Settings → Business tools) is checked every Monday.", BODY),
 H2("Offline → WhatsApp")]
story += bullets(["Parcel insert card: 'Scan for R50 off your next pair' QR → wa.me link with pre-filled 'NC50' — turns every delivery into an opt-in.",
 "Campus & taxi-rank flyers (Joburg, Pretoria, Durban, Cape Town): combo hero photo, price, QR. One flyer design per brand pillar.",
 "Till/partner barbershops & car washes: table-talkers with QR 'Win a combo monthly'."])

# ---------- 6 Calendar ----------
story += [PageBreak(), H1("6. Ready-to-post 30-day content calendar"),
 Paragraph("Post times SAST. IG = Instagram feed, R = Reel, S = Stories, TT = TikTok, WA = WhatsApp broadcast/status. Product names/prices match the website catalogue.", SMALL)]
cal = [["Day","Channel","Content","Hook / CTA"]]
rows = [
 ("1","IG+R+TT","Launch: brand reveal + Shox White Metallic R1,450","'SA, your feed is now a sneaker store.' → WhatsApp size check"),
 ("2","IG carousel","Combo 101: Black + White Airforce R1,599 (save R701)","'Two pairs. One price. Tag your person.'"),
 ("3","TT+R","On-feet: Adidas Samba Jane (all colourways)","'Jane era. R1,450. Which colour?' poll"),
 ("4","IG+S","New Balance 9060 family R1,450","Story quiz: 9060 or 1000?"),
 ("5","WA","Broadcast: Weekend Combo Drop (Jordan + Airforce R1,899)","'Reply with your UK size — free delivery'"),
 ("6","IG+R","Jordan 1 Cool Grey vs OG Denim","'Pick one. Loser leaves the rotation.'"),
 ("7","IG","Review wall: Thandi 5★ quote card","'Real people. Real pairs.' → Reviews highlight"),
 ("8","TT","Unboxing ASMR: Timberland Premium Wheat R1,890","'That new-boot smell…'"),
 ("9","IG carousel","Lacoste clean-fit edit (Baseshot/T-Clip) R1,450","'Quiet luxury, loud price. R1,450.'"),
 ("10","R+TT","Puma Speedcat R4 Red fit check","'Speedcat szn.' Sound: trending amapiano"),
 ("11","IG+S","Combo face-off: Lowdunk+AF vs Samba+AF (R1,780/R1,799)","Story vote; loser gets Friday price drop"),
 ("12","WA","Broadcast: Payday Combo Weekend + extra gift","'Combos from R1,599. Ends Sunday 23:59.'"),
 ("13","IG","Bapesta Black/Grey/Blue R1,450","'Rare energy. Three colourways.'"),
 ("14","Live","IG Live: size & stock check + giveaway tease","Live-only code NC LIVE = R100 off combos"),
 ("15","IG+R","Mid-month Drop Day: Nike Rift family R1,450","'Rift check — velvet, beige, metallic, polka.'"),
 ("16","TT","'R1,450 vs R3,299 — guess the combo' stitch game","Comment bait → profile visits"),
 ("17","IG carousel","New Balance Abzorb Black/Grey/Blue (was R1,800)","'Bubbles. Now R1,450.'"),
 ("18","S+IG","Customer UGC repost day (on-feet thread)","Repost 5 customers; voucher each"),
 ("19","WA","Broadcast: Jordan Combo restock (8 styles R1,899)","'Reply JORDAN + size'"),
 ("20","IG+R","Karl 2-Tone + Replay Field Speed — designer edit","'Designer drip, sneaker price.'"),
 ("21","TT+R","Delivery POV: order → door in 48h (real parcel)","Trust content; pin to profile"),
 ("22","IG","Converse Chuck 70 Plus stack R1,450","'Platform season.'"),
 ("23","IG carousel","Timberland Combos R2,399/R3,299 (save up to R1,201)","'One for you, one for the plug.'"),
 ("24","S","Polls day: this-or-that across 10 pairs","Winners get tomorrow's Reel"),
 ("25","WA","Broadcast: Student Special (valid student card = free gift upgrade)","Opt-ins from campuses"),
 ("26","IG+R","Adidas Spezial Purple + SL72 OG R1,450","Retro wave content"),
 ("27","TT","Creator collab duet: 'style my NowCulture pair 3 ways'","Creator code = 10% affiliate"),
 ("28","IG","Giveaway final call: Win a Combo (tag 2 friends)","Closes Day 30 on Live"),
 ("29","IG+S","Vans Checkboard + Diesel Ukiyo — skater/street edit","Cross-post to FB groups"),
 ("30","Live+WA","Winner Live + Month-2 Drop List broadcast","Early-access list invite → VIP segment"),
]
for r in rows: cal.append(list(r))
story += [table(cal, [12*mm, 24*mm, 72*mm, 62*mm])]
story += [Paragraph("Production rule: batch-shoot every Sunday (10 Reels/photos in 2 hours, on-feet + flat-lay + unboxing). Edit Monday. Schedule with Meta Business Suite / TikTok scheduler. WhatsApp Status mirrors Instagram Stories daily — Status is free reach to every opted-in contact.", BODY)]

# ---------- 7 Scripts ----------
story += [PageBreak(), H1("7. Copy-paste library"), H2("Instagram captions (fill the brackets)")]
for q in ["🔥 JUST DROPPED: [NIKE SHOX WHITE METALLIC] — R1,450 (UK 3–9). Free delivery nationwide + a free gift with every order. Tap the post to bag it, or WhatsApp your size: link in bio. Sharp! #Nike #NowCulture #KicksSA",
 "🎁 COMBO CULTURE: [Jordan + Airforce] = R1,899. Separately R2,720 — you save R821. One for the rotation, one for your person. Free delivery + free gift. WhatsApp 'COMBO + your size' to order. Ends [Sunday]. #SneakerCombos #Take2 #NowCulture",
 "⭐ REAL REVIEWS, REAL PAIRS: '[paste review]' — [Thandi]. Join 100s of happy feet. Shop the feed, checkout on WhatsApp, track your parcel with us in chat. #MzansiStyle #NowCulture"]:
    story += [Paragraph(q, QUOTE), Spacer(1, 2*mm)]
story += [H2("WhatsApp scripts (save as Quick Replies / shortcuts)")]
story += [table([["Shortcut","Message"],
 ["/size","Sharp [Name]! 👟 For the *[Product]* we have UK [3–9] in stock right now. What's your UK size? I'll reserve your pair for 2 hours while you decide. 🚚 Delivery is free, and you get a free gift 🎁"],
 ["/pay","Perfect — your order is confirmed:\n*[Product]* · UK [size] · [Qty] · *R[amount]* (free delivery)\nPay here: [payment link / EFT details]. Please send proof of payment and your delivery address + name. We dispatch within 24h and send tracking right here. Danko! 🙏"],
 ["/track","Great news [Name] 🎉 Your *[Product]* is on the way! Tracking: [number/link]. ETA [date]. Reply here if you need anything — we're on it."],
 ["/swap","No stress [Name] — size swaps are part of the culture. Reply with the size you need; we'll arrange the swap once your pair is back with us (unworn, boxed). We'll confirm stock first so you're never left hanging. 👟"],
 ["/recover","Hi [Name], it's NowCulture 👟 You left *[Product]* (R[price]) in your bag. Still keen? Reply YES and I'll check your size — or make it a combo and save up to R1,201 🎁 Free delivery either way."],
 ["/review","Danko for rocking NowCulture, [Name]! 🙏 How's the fit? A quick review + on-feet pic gets you *R50 off* your next pair — and you might be featured on our page ⭐"],
 ["/vip","[Name], VIP early access 🔐 Tomorrow's drop goes public at 18:00 — you can order now: [top 3 products + prices]. Reply with size to jump the queue."]],
 [24*mm, 146*mm])]
story += [Paragraph("Response-time standard: under 5 minutes 08:00–21:00; away message outside hours promises a reply by 09:00 and links the website so night shoppers can still bag items.", BODY)]

# ---------- 8 Ads ----------
story += [H1("8. Paid media plan"), Paragraph("Organic builds the culture; paid turns the tap on. All ads click to WhatsApp (highest-converting destination in SA) or to the matching product on the website.", BODY)]
story += [table([["Campaign","Platform","Objective","Creative","Budget share"],
 ["Combo Hero","Meta (IG/FB)","WhatsApp conversations","Carousel/Reel: 2 pairs, saving badge, 'Send WhatsApp Message'","35%"],
 ["Drop Retargeting","Meta","Website visitors & engagers → WhatsApp","Exact product they viewed; 'Your size is waiting'","20%"],
 ["TikTok Spark","TikTok","Views → profile → WhatsApp","Boost top 2 organic Reels/week (creator-whitelisted)","20%"],
 ["Catalogue Sales","Meta Advantage+","Purchases","Full catalogue feed from the website product list","15%"],
 ["Giveaway/Follower","Meta + TikTok","Engagement & opt-ins","Tag-and-win combo creative; wa.me opt-in landing","10%"]],
 [30*mm, 26*mm, 38*mm, 48*mm, 28*mm])]
story += bullets([
 "Targeting: 18–34, Gauteng/Western Cape/KZN metros first; interests: sneaker & streetwear pages, local culture/music; Advantage+ broad once pixel has 500+ events. Exclude existing buyers from prospecting (they get VIP WhatsApp instead).",
 "Install the Meta pixel + TikTok pixel on the website; track ViewContent (product open), AddToBag, WhatsAppClick. Judge ads on cost per WhatsApp conversation and cost per order — not likes.",
 "Creative refresh every 10–14 days; kill any ad set above R180 cost/order after R500 spend; scale winners 20%/day."])

# ---------- 9 Budget/KPI ----------
story += [H1("9. Budget scenarios (monthly, ZAR)")]
story += [table([["Line","Starter","Growth (recommended)","Scale"],
 ["Paid media (Meta + TikTok)","R3,000","R8,000","R20,000"],
 ["Creators (2–6 micro, product + fees)","R1,500","R4,000","R10,000"],
 ["Giveaway product (1 combo/month)","+R1,899 stock cost","+R1,899 stock cost","2 combos"],
 ["Content production (data, props, editing apps)","R600","R1,200","R3,000"],
 ["Tools (scheduler, WhatsApp BSP when needed, design)","R350","R800","R2,000"],
 ["Total","±R5,450","±R14,000","±R35,000"],
 ["Target orders / revenue","90 orders · ±R140k","320 orders · ±R496k","900 orders · ±R1.4m"]],
 [62*mm, 36*mm, 36*mm, 36*mm]),
 Paragraph("Targets assume AOV ±R1,550 (combos lift AOV — push combo attach rate to 35%+), conversion of WhatsApp chats to orders at 18–25%, and organic content running daily as specified. Reinvest 15% of revenue into media until cost/order exceeds R150.", SMALL),
 H1("10. KPIs & weekly rhythm")]
story += [table([["Metric","90-day target","Check"],
 ["Instagram followers / reach","25k followers · 1.5m reach/mo","Mon review"],
 ["WhatsApp opt-ins & quality rating","5,000 opt-ins · 'High' quality","Mon review"],
 ["Chat → order conversion","18–25%","Weekly"],
 ["Cost per order (paid)","< R120","Weekly kill/scale"],
 ["Combo attach rate","≥ 35% of orders","Weekly"],
 ["Revenue / AOV","R900k in 90 days · AOV ≥ R1,550","Monthly"],
 ["Repeat purchase (60-day)","≥ 18%","Monthly"]],
 [62*mm, 62*mm, 46*mm])]
story += [Paragraph("<b>Monday:</b> numbers (30 min) — followers, chats, orders, cost/order, WhatsApp quality rating. <b>Wednesday:</b> shoot/edit batch 2. <b>Friday 19:00:</b> Live stock check. <b>Sunday:</b> batch-shoot + schedule the week. <b>Monthly:</b> giveaway draw, creator review, price/stock sync with SGM Touch, refresh this plan's calendar.", BODY),
 H1("Risks & house rules")]
story += bullets([
 "Trademark care: brand names are used descriptively to sell the listed products; never imply NowCulture is Nike/Adidas/etc. Keep the site footer disclaimer. Use SGM Touch product imagery as supplied by the catalogue source and re-verify prices/stock weekly — update the website data file when SGM pricing changes.",
 "WhatsApp bans: opt-in only, ≤2 broadcasts/week, honour STOP, conversational tone. POPIA: store only name/number/order data, never sell lists.",
 "Stock risk: combos sell fast — confirm size on WhatsApp before payment (built into script /size), and mark sold-out pairs on the site the same day.",
 "Load-shedding & data costs: keep images compressed (site uses width-optimised CDN images), post downloadable-size flyers, and schedule posts for when the audience is online, not when the office is."])
story += [Paragraph("— End of plan. Now go make the feed shoppable. 👟🔥", BODY)]

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=15*mm, rightMargin=15*mm, topMargin=19*mm, bottomMargin=14*mm,
                        title="NowCulture — Social Media & WhatsApp Marketing Plan", author="NowCulture")
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print("Built", OUT)
