/* NowCulture app — feed, explore, saved, cart, WhatsApp checkout (all client-side, localStorage-persisted) */
const WA_NUMBER = "27613446518";
const SIZES = ["3","4","5","6","7","8","9"];
const $ = s => document.querySelector(s);
const money = n => "R " + n.toLocaleString("en-ZA");
const store = {
  get(k, d){ try { return JSON.parse(localStorage.getItem("nc_"+k)) ?? d } catch { return d } },
  set(k, v){ localStorage.setItem("nc_"+k, JSON.stringify(v)) }
};
let liked = new Set(store.get("liked", []));
let saved = new Set(store.get("saved", []));
let cart  = store.get("cart", []);               // {id,size,qty}
let comments = store.get("comments", {});        // id -> [{user,text}]
let activeBrand = "All", view = "feed", query = "";
let modalId = null, modalSize = null, modalQty = 1;

const initials = b => b.split(" ").map(x=>x[0]).join("").slice(0,2).toUpperCase();
const hashtags = p => p.combo ? "#SneakerCombos #Take2 #NowCulture #KicksSA" :
  `#${p.brand.replace(/\s/g,"")} #NowCulture #KicksSA #SneakerCulture #MzansiStyle`;
const captionFor = p => p.combo
  ? `COMBO DEAL 🎁 Two pairs, one price — save ${p.was?money(p.was-p.price):""} vs buying separately. Free delivery + a free gift.`
  : `Just dropped 🔥 Premium comfort, all-day culture. Free delivery nationwide + one free gift per order.`;

function filtered(){
  let list = PRODUCTS.slice();
  if (view === "saved") list = list.filter(p => saved.has(p.id));
  if (activeBrand !== "All") list = list.filter(p => activeBrand === "Combos" ? p.combo : p.brand === activeBrand);
  if (query) { const q = query.toLowerCase(); list = list.filter(p => (p.name+" "+p.brand).toLowerCase().includes(q)); }
  const s = $("#sortSel").value;
  if (s==="low") list.sort((a,b)=>a.price-b.price); else if (s==="high") list.sort((a,b)=>b.price-a.price);
  else if (s==="az") list.sort((a,b)=>a.name.localeCompare(b.name)); else if (s==="liked") list.sort((a,b)=>b.likes-a.likes);
  return list;
}

function postHTML(p){
  const isLiked = liked.has(p.id), isSaved = saved.has(p.id);
  const likeCount = p.likes + (isLiked?1:0);
  const cs = comments[p.id] || [];
  const off = p.was ? Math.round((1-p.price/p.was)*100) : 0;
  return `<article class="post" id="post-${p.id}">
    <div class="post-head">
      <div class="pav"><span>${initials(p.brand)}</span></div>
      <div><b>nowculture</b> <span class="verified">✔</span><small>${p.combo?"Sneaker Combos · 2 pairs, 1 price":"Originals · "+p.brand} · South Africa</small></div>
      <button class="dots" onclick="openProduct(${p.id})" title="More">•••</button>
    </div>
    <div class="post-media" ondblclick="dblLike(${p.id},this)" onclick="if(event.detail===1)openProduct(${p.id})">
      <img src="${p.img}" alt="${p.name} — ${p.brand} sneaker at NowCulture" loading="lazy" onerror="this.src='assets/logo.svg';this.style.objectFit='contain';this.style.padding='60px'">
      ${p.combo?'<span class="comboflag">🎁 COMBO · 2 PAIRS</span>':""}
      ${off?`<span class="saveoff">-${off}%</span>`:""}
      <span class="priceflag">${p.was?`<s>${money(p.was)}</s>`:""}${money(p.price)}</span>
      <span class="heartburst">♥</span>
    </div>
    <div class="actions">
      <button onclick="toggleLike(${p.id})" class="${isLiked?"liked":""}" title="Like">${isLiked?"❤️":"🤍"}</button>
      <button onclick="focusComment(${p.id})" title="Comment">💬</button>
      <button onclick="shareProduct(${p.id})" title="Share">✈️</button>
      <span class="spacer"></span>
      <button onclick="toggleSave(${p.id})" title="Save">${isSaved?"🔖":"📑"}</button>
    </div>
    <div class="likes">${likeCount.toLocaleString("en-ZA")} likes</div>
    <p class="caption"><b>nowculture</b><span class="priceinline">${p.name}</span> — ${captionFor(p)} <span class="priceinline">${money(p.price)}</span>${p.was?` <s>${money(p.was)}</s>`:""}<br><span class="hashtags">${hashtags(p)}</span></p>
    ${cs.length?`<div class="viewcomments" onclick="openProduct(${p.id})">View product & ${p.comments+cs.length} comments</div>`
               :`<div class="viewcomments" onclick="openProduct(${p.id})">View product · ${p.comments} comments</div>`}
    <div class="comments">${cs.slice(-3).map(c=>`<div><b>${c.user}</b>${c.text}</div>`).join("")}</div>
    <div class="postcta">
      <button class="btn grad grow" onclick="openProduct(${p.id})">👟 Pick size & bag it</button>
      <button class="btn wa" onclick="quickWhatsApp(${p.id})">💬 WhatsApp</button>
    </div>
    <form class="addcomment" onsubmit="addComment(event,${p.id})">
      <input placeholder="Add a comment…" maxlength="140" id="cinput-${p.id}"><button type="submit">Post</button>
    </form>
  </article>`;
}

function render(){
  const list = filtered();
  $("#statPosts").textContent = PRODUCTS.length;
  $("#emptyState").hidden = list.length > 0;
  $("#feed").innerHTML = list.map(postHTML).join("");
  $("#grid").innerHTML = list.map(p=>`<button class="tile" onclick="openProduct(${p.id})"><img src="${p.img}" alt="${p.name}" loading="lazy" onerror="this.src='assets/logo.svg'"><span>${p.name} · ${money(p.price)}</span></button>`).join("");
  $("#cartCount").hidden = !cart.length; $("#cartCount").textContent = cart.reduce((a,c)=>a+c.qty,0);
  $("#savedCount").hidden = !saved.size; $("#savedCount").textContent = saved.size;
  $("#menuSaved").textContent = saved.size || ""; $("#menuCart").textContent = cart.reduce((a,c)=>a+c.qty,0) || "";
  $("#viewTitle").textContent = view==="saved" ? "Saved kicks 🔖" : view==="explore" ? "Explore the culture 🧭" :
    activeBrand==="All" ? "Latest drops" : activeBrand==="Combos" ? "Sneaker Combos 🎁 2 pairs, 1 price" : activeBrand + " at NowCulture";
}

function renderStories(){
  $("#stories").innerHTML = BRANDS.filter(b=>b!=="All").map(b=>{
    const p = PRODUCTS.find(x=> b==="Combos" ? x.combo : x.brand===b);
    return `<button class="story ${activeBrand===b?"active":""}" onclick="filterBrand('${b.replace(/'/g,"\\'")}')">
      <div class="ring"><img src="${p?p.img:"assets/logo.svg"}" alt="${b}" loading="lazy" onerror="this.src='assets/logo.svg'"></div><span>${b==="Combos"?"🎁 Combos":b}</span></button>`;
  }).join("");
}
function renderChips(){
  $("#chips").innerHTML = BRANDS.map(b=>`<button class="chip ${activeBrand===b?"active":""}" onclick="filterBrand('${b.replace(/'/g,"\\'")}')">${b==="Combos"?"🎁 Combos":b}</button>`).join("");
}
function renderRails(){
  const byLikes = [...PRODUCTS].sort((a,b)=>b.likes-a.likes);
  $("#suggested").innerHTML = byLikes.slice(0,5).map(p=>`<button class="sugg" onclick="openProduct(${p.id})">
    <span class="pav"><img src="${p.img}" alt="" loading="lazy" onerror="this.parentNode.textContent='${initials(p.brand)}'"></span>
    <span><b>${p.name}</b><small>${p.brand} · ${money(p.price)}</small></span><span class="follow">View</span></button>`).join("");
  $("#trending").innerHTML = PRODUCTS.filter(p=>p.combo).sort((a,b)=>b.likes-a.likes).slice(0,4).map(p=>
    `<button class="trend" onclick="openProduct(${p.id})"><img src="${p.img}" alt="" loading="lazy" onerror="this.src='assets/logo.svg'"><span><b>${p.name}</b><small>${money(p.price)}${p.was?" · was "+money(p.was):""}</small></span></button>`).join("");
}

/* interactions */
function toggleLike(id){ liked.has(id)?liked.delete(id):liked.add(id); store.set("liked",[...liked]); render(); }
function dblLike(id, el){ if(!liked.has(id)){ liked.add(id); store.set("liked",[...liked]); render(); }
  const h = document.querySelector(`#post-${id} .heartburst`); if(h){ h.classList.remove("pop"); void h.offsetWidth; h.classList.add("pop"); } }
function toggleSave(id){ saved.has(id)?saved.delete(id):saved.add(id); store.set("saved",[...saved]); render(); toast(saved.has(id)?"Saved 🔖 Find it under Saved":"Removed from Saved"); }
function focusComment(id){ const i=$("#cinput-"+id); if(i){ i.focus(); i.scrollIntoView({behavior:"smooth",block:"center"}); } }
function addComment(e,id){ e.preventDefault(); const i=$("#cinput-"+id); const t=i.value.trim(); if(!t) return;
  (comments[id]=comments[id]||[]).push({user:"you",text:t.replace(/</g,"&lt;")}); store.set("comments",comments); render(); toast("Comment posted 💬"); }
async function shareProduct(id){ const p=PRODUCTS.find(x=>x.id===id); const url=location.origin+location.pathname+"#post-"+p.id;
  if(navigator.share){ try{ await navigator.share({title:"NowCulture — "+p.name, text:`${p.name} for ${money(p.price)} at NowCulture 👟`, url}); }catch{} }
  else { try{ await navigator.clipboard.writeText(url); toast("Link copied 🔗"); }catch{ toast(url); } } }
function quickWhatsApp(id){ const p=PRODUCTS.find(x=>x.id===id);
  openWA(`Hi NowCulture! 👟 I'm interested in:\n\n*${p.name}* (${p.brand})\nPrice: ${money(p.price)}\n\nIs it available in my size?`); }

function setView(v){ view=v; document.querySelectorAll(".menu button[data-view]").forEach(b=>b.classList.toggle("active",b.dataset.view===v));
  $("#feed").hidden = v==="explore"; $("#grid").hidden = v!=="explore"; render(); window.scrollTo({top:0,behavior:"smooth"}); }
function filterBrand(b){ activeBrand=b; if(view==="saved") view="feed"; setView(view); renderStories(); renderChips(); }
function goHome(e){ e.preventDefault(); activeBrand="All"; setView("feed"); renderStories(); renderChips(); }
function focusSearch(){ $("#searchInput").focus(); window.scrollTo({top:0,behavior:"smooth"}); const s=document.querySelector(".searchbox"); if(s) s.style.display="flex"; }

/* modal */
function openProduct(id){ const p=PRODUCTS.find(x=>x.id===id); modalId=id; modalSize=null; modalQty=1;
  $("#mImg").src=p.img; $("#mImg").alt=p.name; $("#mTag").textContent = p.combo?"🎁 COMBO · 2 PAIRS, 1 PRICE":"NEW DROP";
  $("#mBrand").textContent = p.brand + (p.combo?" · Sneaker Combo":""); $("#mName").textContent=p.name;
  $("#mPrice").innerHTML = (p.was?`<s>${money(p.was)}</s>`:"")+money(p.price);
  $("#mCaption").textContent = captionFor(p)+" "+hashtags(p);
  $("#mQty").textContent="1";
  $("#mSave").textContent = saved.has(id)?"🔖 Saved — tap to remove":"🔖 Save for later";
  $("#mSizes").innerHTML = SIZES.map(s=>`<button onclick="pickSize('${s}',this)">${s}</button>`).join("");
  $("#mAdd").onclick = ()=>addToBag(); $("#mWa").onclick = ()=>orderWhatsApp();
  $("#mSave").onclick = ()=>{ toggleSave(id); $("#mSave").textContent = saved.has(id)?"🔖 Saved — tap to remove":"🔖 Save for later"; };
  $("#modal").hidden=false; document.body.style.overflow="hidden"; }
function pickSize(s,btn){ modalSize=s; document.querySelectorAll("#mSizes button").forEach(b=>b.classList.toggle("sel",b===btn)); }
function stepQty(d){ modalQty=Math.min(5,Math.max(1,modalQty+d)); $("#mQty").textContent=modalQty; }
function closeModal(){ $("#modal").hidden=true; document.body.style.overflow=""; }
function addToBag(){ if(!modalSize){ toast("Please pick a size first 👟"); return; }
  const found=cart.find(c=>c.id===modalId&&c.size===modalSize);
  found?found.qty+=modalQty:cart.push({id:modalId,size:modalSize,qty:modalQty});
  store.set("cart",cart); render(); closeModal(); toast("Added to bag 🛍️"); toggleCart(true); }
function waTextFor(p,size,qty){ return `Hi NowCulture! 👟 I'd like to order:\n\n*${p.name}* (${p.brand})\nSize (UK): ${size||"— please advise"}\nQty: ${qty||1}\nPrice: ${money(p.price)}\n\nPlease confirm availability, payment & free delivery. Thank you!`; }
function orderWhatsApp(){ if(!modalSize){ toast("Pick a size so we can check stock 👟"); return; }
  const p=PRODUCTS.find(x=>x.id===modalId); openWA(waTextFor(p,modalSize,modalQty)); }
function openWA(text){ window.open(`https://wa.me/${WA_NUMBER}?text=${encodeURIComponent(text)}`,"_blank"); }

/* cart */
function toggleCart(open){ $("#cartWrap").hidden=!open; if(open) renderCart(); }
function renderCart(){ const box=$("#cartItems");
  if(!cart.length){ box.innerHTML=`<p class="muted" style="padding:18px 0">Your bag is empty. Scroll the feed and cop something 🔥</p>`; }
  else box.innerHTML = cart.map((c,i)=>{ const p=PRODUCTS.find(x=>x.id===c.id); return `<div class="cartitem">
    <img src="${p.img}" alt="" onerror="this.src='assets/logo.svg'"><div><b>${p.name}</b><small>${p.brand} · UK ${c.size} · ×${c.qty}</small><br>
    <button class="rm" onclick="removeItem(${i})">Remove</button></div><span class="amt">${money(p.price*c.qty)}</span></div>`; }).join("");
  $("#cartTotal").textContent = money(cart.reduce((a,c)=>a+PRODUCTS.find(x=>x.id===c.id).price*c.qty,0)); }
function removeItem(i){ cart.splice(i,1); store.set("cart",cart); renderCart(); render(); }
function checkoutWhatsApp(){ if(!cart.length){ toast("Your bag is empty 🛍️"); return; }
  const lines=cart.map(c=>{ const p=PRODUCTS.find(x=>x.id===c.id); return `• *${p.name}* (${p.brand}) — UK ${c.size} ×${c.qty} — ${money(p.price*c.qty)}`; });
  const total=money(cart.reduce((a,c)=>a+PRODUCTS.find(x=>x.id===c.id).price*c.qty,0));
  openWA(`Hi NowCulture! 👟 I'd like to order:\n\n${lines.join("\n")}\n\n*Total: ${total}*\nDelivery: FREE 🚚 + 1 free gift 🎁\n\nName:\nDelivery address:\n\nPlease confirm payment details. Thank you!`); }

function toast(msg){ const t=$("#toast"); t.textContent=msg; t.hidden=false; clearTimeout(t._h); t._h=setTimeout(()=>t.hidden=true,2600); }

$("#searchInput").addEventListener("input", e=>{ query=e.target.value; render(); });
document.addEventListener("keydown", e=>{ if(e.key==="Escape"){ closeModal(); toggleCart(false); } });
$("#modal").addEventListener("click", e=>{ if(e.target.id==="modal") closeModal(); });
$("#cartWrap").addEventListener("click", e=>{ if(e.target.id==="cartWrap") toggleCart(false); });

renderStories(); renderChips(); renderRails(); render();
