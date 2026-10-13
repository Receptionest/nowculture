#!/usr/bin/env python3
"""Download every product image in assets/products.js into assets/images/ (runs on GitHub Actions, which has internet)."""
import re, pathlib, sys, urllib.request, concurrent.futures, json
root = pathlib.Path(__file__).resolve().parent.parent
text = (root/"assets/products.js").read_text()
# RAW rows: ["name","brand",price,was,"FILE?v=...","handle",combo]
rows = re.findall(r'^\[".*?",\s*"(.*?)",\s*\d+,\s*\d+,\s*"([^"]+)",\s*"([^"]+)",\s*\d+\]', text, re.M)
print(f"{len(rows)} products found")
out = root/"assets/images"; out.mkdir(parents=True, exist_ok=True)
CDN = "https://sgmtouch.co.za/cdn/shop/files/"
def job(args):
    i, (brand, f, handle) = args
    base = f.split("?")[0]
    ext = base.rsplit(".",1)[-1].lower()
    if ext not in ("jpg","jpeg","png","webp","avif"): ext="jpg"
    name = f"{i:03d}.{ext}"
    dest = out/name
    if dest.exists() and dest.stat().st_size>3000: return (i,name,True,"cached")
    url = CDN + f + "&width=800"
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0"})
            data = urllib.request.urlopen(req, timeout=30).read()
            if len(data) < 1000: raise ValueError(f"too small {len(data)}")
            dest.write_bytes(data)
            return (i,name,True,f"{len(data)} bytes")
        except Exception as e:
            err=str(e)
    return (i,name,False,err)

results=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
    for r in ex.map(job, enumerate(rows,1)):
        results.append(r); print(r, flush=True)
manifest={str(i):name for i,name,ok,_ in results if ok}
(root/"assets/images/manifest.json").write_text(json.dumps(manifest,indent=1))
failed=[r for r in results if not r[2]]
print(f"OK {len(manifest)} / {len(rows)}  FAILED {len(failed)}")
if failed:
    print("FAILED:", failed[:20])
    # don't fail the whole run if most succeeded
    if len(manifest) < len(rows)*0.8: sys.exit(1)
