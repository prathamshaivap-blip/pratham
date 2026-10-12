from pathlib import Path

html = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#111111">
<title>Royal Enfield | Ride Beyond</title>
<style>
:root{--ink:#151515;--paper:#f4f1eb;--cream:#e5dfd3;--red:#b5221c;--muted:#aaa49a}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:Arial,Helvetica,sans-serif;background:var(--paper);color:var(--ink)}a{color:inherit;text-decoration:none}button{font:inherit;cursor:pointer}
.topline{height:4px;background:var(--red)}header{height:76px;padding:0 6vw;display:flex;align-items:center;justify-content:space-between;background:#111;color:#fff;position:sticky;top:0;z-index:20;border-bottom:1px solid #333}.brand{font-family:Georgia,serif;font-weight:700;letter-spacing:2px;font-size:21px;line-height:1.05}.brand small{display:block;font-family:Arial,sans-serif;font-size:8px;letter-spacing:5px;margin-top:6px;color:#d4c7b1}.nav{display:flex;align-items:center;gap:30px;font-size:11px;font-weight:700;letter-spacing:1.4px;text-transform:uppercase}.nav a{opacity:.85;transition:.2s}.nav a:hover{color:#d5a36b;opacity:1}.nav-cta{border:1px solid #b9a98e;padding:13px 17px}.menu{display:none;background:none;border:0;color:#fff;font-size:25px}
.hero{min-height:610px;position:relative;display:flex;align-items:center;overflow:hidden;color:white;background:#27231f url('https://images.unsplash.com/photo-1558981806-ec527fa84c39?auto=format&fit=crop&w=2000&q=85') center 54%/cover no-repeat}.hero:before{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.83),rgba(0,0,0,.45) 48%,rgba(0,0,0,.08)),linear-gradient(0deg,rgba(0,0,0,.35),transparent 45%)}.hero-content{position:relative;z-index:1;padding:70px 10vw;max-width:790px}.eyebrow{font-size:11px;letter-spacing:4px;text-transform:uppercase;color:#d9b27e;font-weight:bold}.hero h1{font-family:Georgia,serif;font-size:clamp(48px,7.4vw,94px);line-height:.98;letter-spacing:-2px;margin:22px 0}.hero p{max-width:460px;color:#e5e0d9;line-height:1.8;font-size:15px}.actions{display:flex;gap:13px;flex-wrap:wrap;margin-top:30px}.btn{display:inline-flex;align-items:center;justify-content:center;padding:16px 22px;border:1px solid #d4c4a7;background:var(--red);color:white;font-size:11px;font-weight:bold;letter-spacing:1.4px;text-transform:uppercase;transition:transform .2s,background .2s}.btn:hover{transform:translateY(-2px);background:#8e1915}.btn.outline{background:transparent;border-color:#e0d6c5}.scroll-note{position:absolute;right:6vw;bottom:32px;writing-mode:vertical-rl;font-size:10px;letter-spacing:3px;color:#eee}
.stats{display:grid;grid-template-columns:repeat(3,1fr);background:#181818;color:#fff;padding:27px 9vw;text-align:center}.stat{border-right:1px solid #444}.stat:last-child{border:0}.stat strong{font-family:Georgia,serif;font-size:24px;font-weight:normal}.stat span{display:block;font-size:9px;letter-spacing:2px;color:#b9b1a5;margin-top:8px;text-transform:uppercase}
.section{padding:92px 8vw}.section-head{display:flex;align-items:end;justify-content:space-between;gap:25px;margin-bottom:38px}.kicker{font-size:10px;letter-spacing:3px;color:var(--red);font-weight:bold;text-transform:uppercase}.section h2{font-family:Georgia,serif;font-weight:normal;font-size:clamp(36px,5vw,58px);line-height:1.05;margin:13px 0 0}.section-head p{max-width:360px;color:#6b675f;font-size:13px;line-height:1.8}
.models{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}.model-card{background:#fff;position:relative;overflow:hidden;transition:transform .25s;box-shadow:0 10px 35px #302a2010}.model-card:hover{transform:translateY(-6px)}.model-image{height:245px;background:#d2ccc1 center/cover no-repeat;position:relative}.model-image:after{content:"";position:absolute;inset:45% 0 0;background:linear-gradient(transparent,rgba(0,0,0,.25))}.model-label{position:absolute;left:18px;top:18px;color:white;font-size:9px;letter-spacing:2px;text-transform:uppercase;z-index:1;background:#111b;padding:8px 10px}.model-info{padding:25px}.model-info h3{font-family:Georgia,serif;font-weight:normal;font-size:27px;margin:0 0 8px}.model-info p{font-size:12px;line-height:1.7;color:#77766f;min-height:42px}.model-bottom{display:flex;justify-content:space-between;align-items:center;border-top:1px solid #e9e5df;padding-top:17px;margin-top:20px}.price{font-weight:bold;font-size:13px}.arrow{font-size:22px;color:var(--red)}
.story{display:grid;grid-template-columns:1fr 1fr;min-height:480px;background:#20201e;color:#f6f1e8}.story-photo{min-height:430px;background:url('https://images.unsplash.com/photo-1558981403-c5f9899a28bc?auto=format&fit=crop&w=1200&q=85') center/cover no-repeat}.story-copy{padding:70px clamp(30px,7vw,100px);align-self:center}.story-copy h2{font-family:Georgia,serif;font-size:clamp(38px,4.4vw,60px);font-weight:normal;line-height:1.05;margin:17px 0 20px}.story-copy p{font-size:13px;line-height:1.9;color:#c7c2b8;max-width:440px}.story-copy .btn{margin-top:18px}
.experience{background:#e5dfd3}.experience-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:#c7bfb1;margin-top:35px;border:1px solid #c7bfb1}.experience-item{background:#e5dfd3;padding:31px}.experience-item .number{font-family:Georgia,serif;font-size:35px;color:var(--red)}.experience-item h3{font-family:Georgia,serif;font-size:22px;font-weight:normal;margin:18px 0 9px}.experience-item p{font-size:12px;line-height:1.8;color:#6f6a60}
.cta{padding:75px 8vw;text-align:center;background:#b5221c;color:#fff}.cta .eyebrow{color:#f1c8a2}.cta h2{font-family:Georgia,serif;font-weight:normal;font-size:clamp(36px,5vw,58px);margin:14px 0}.cta p{font-size:13px;color:#f3deda}.cta .btn{background:#171717;border-color:#171717;margin-top:18px}
footer{background:#111;color:#e8e2d7;padding:45px 8vw 25px}.footer-top{display:flex;justify-content:space-between;gap:30px;align-items:start;padding-bottom:35px;border-bottom:1px solid #383838}.footer-copy{max-width:320px;font-size:12px;line-height:1.8;color:#a7a198}.footer-links{display:flex;gap:22px;flex-wrap:wrap;font-size:10px;letter-spacing:1px;text-transform:uppercase}.footer-bottom{display:flex;justify-content:space-between;gap:20px;padding-top:20px;font-size:10px;color:#8d8982}
.modal{position:fixed;inset:0;background:#000b;display:none;align-items:center;justify-content:center;padding:20px;z-index:50}.modal.open{display:flex}.modal-box{background:var(--paper);width:min(480px,100%);padding:34px;position:relative}.modal-box h2{font-family:Georgia,serif;font-size:34px;font-weight:normal;margin:0 0 8px}.modal-box p{font-size:12px;color:#6f6a60;line-height:1.7}.close{position:absolute;right:16px;top:12px;border:0;background:none;font-size:26px}.form-row{margin-top:15px}.form-row label{display:block;font-size:10px;letter-spacing:1px;text-transform:uppercase;margin-bottom:7px}.form-row input,.form-row select{width:100%;padding:12px;border:1px solid #c9c2b6;background:#fff;font:inherit}.modal-box .btn{width:100%;margin-top:20px}
@media(max-width:800px){.nav{display:none;position:absolute;left:0;right:0;top:76px;background:#111;padding:25px 7vw;flex-direction:column;align-items:flex-start;gap:23px}.nav.open{display:flex}.menu{display:block}.hero{min-height:570px;background-position:58% center}.hero-content{padding:60px 7vw}.section{padding:70px 6vw}.section-head{display:block}.models{grid-template-columns:1fr 1fr}.model-image{height:210px}.story{grid-template-columns:1fr}.story-photo{min-height:300px}.story-copy{padding:55px 7vw}.experience-grid{grid-template-columns:1fr}.footer-top{flex-direction:column}.scroll-note{display:none}}
@media(max-width:520px){header{padding:0 5vw}.brand{font-size:18px}.hero h1{font-size:52px}.stats{padding:23px 4vw}.stat strong{font-size:20px}.stat span{font-size:8px;letter-spacing:1px}.models{grid-template-columns:1fr}.model-image{height:245px}.model-info p{min-height:0}.section{padding:58px 6vw}.footer-bottom{flex-direction:column}.hero p{font-size:14px}}
</style>
</head>
<body>
<div class="topline"></div>
<header>
  <a class="brand" href="#home" aria-label="Royal Enfield home">ROYAL ENFIELD<small>MADE LIKE A GUN</small></a>
  <nav class="nav" id="nav">
    <a href="#models">Motorcycles</a><a href="#heritage">Our Story</a><a href="#experience">Experiences</a>
    <a href="#contact">Contact</a><a href="#models" class="nav-cta">Explore Models ↗</a>
  </nav>
  <button class="menu" id="menu" aria-label="Toggle menu">☰</button>
</header>
<main>
<section class="hero" id="home">
  <div class="hero-content">
    <div class="eyebrow">Pure motorcycling since 1901</div>
    <h1>Ride your<br>own story.</h1>
    <p>Some roads take you places. Others take you closer to yourself. Find your next adventure on a motorcycle built for the journey.</p>
    <div class="actions"><a class="btn" href="#models">Discover the range&nbsp; ↗</a><button class="btn outline" data-open-modal>Book a test ride</button></div>
  </div>
  <div class="scroll-note">SCROLL TO EXPLORE ↓</div>
</section>
<div class="stats">
  <div class="stat"><strong>1901</strong><span>Born to ride</span></div>
  <div class="stat"><strong>Timeless</strong><span>Design philosophy</span></div>
  <div class="stat"><strong>Every road</strong><span>One spirit</span></div>
</div>
<section class="section" id="models">
  <div class="section-head"><div><div class="kicker">Find your machine</div><h2>Made for the miles.</h2></div><p>From winding mountain roads to everyday city rides, there is a Royal Enfield for the way you want to travel.</p></div>
  <div class="models">
    <article class="model-card"><div class="model-image" style="background-image:url('https://images.unsplash.com/photo-1558981806-ec527fa84c39?auto=format&fit=crop&w=900&q=80')"><span class="model-label">Classic spirit</span></div><div class="model-info"><h3>Classic 350</h3><p>Iconic silhouette. Unhurried character. A timeless ride for every day.</p><div class="model-bottom"><span class="price">Explore the classic</span><a class="arrow" href="https://www.royalenfield.com/in/en/motorcycles/classic-350/" aria-label="Explore Classic 350">↗</a></div></div></article>
    <article class="model-card"><div class="model-image" style="background-image:url('https://images.unsplash.com/photo-1558981403-c5f9899a28bc?auto=format&fit=crop&w=900&q=80')"><span class="model-label">Urban explorer</span></div><div class="model-info"><h3>Hunter 350</h3><p>Agile handling and bold attitude, made for the rhythm of the city.</p><div class="model-bottom"><span class="price">Explore the hunter</span><a class="arrow" href="https://www.royalenfield.com/in/en/motorcycles/hunter-350/" aria-label="Explore Hunter 350">↗</a></div></div></article>
    <article class="model-card"><div class="model-image" style="background-image:url('https://images.unsplash.com/photo-1558980394-0c6c1e4a4a4f?auto=format&fit=crop&w=900&q=80')"><span class="model-label">Go further</span></div><div class="model-info"><h3>Himalayan</h3><p>Built for the unknown, with the spirit to take the long way around.</p><div class="model-bottom"><span class="price">Explore the Himalayan</span><a class="arrow" href="https://www.royalenfield.com/in/en/motorcycles/new-himalayan/" aria-label="Explore Himalayan">↗</a></div></div></article>
  </div>
</section>
<section class="story" id="heritage">
  <div class="story-photo" role="img" aria-label="Motorcycle on an open road"></div>
  <div class="story-copy"><div class="eyebrow">A legacy in motion</div><h2>Not just a ride.<br>A way of life.</h2><p>For generations, the open road has meant freedom, discovery and the stories we collect along the way. Our motorcycles are made to bring you closer to that feeling—one ride at a time.</p><a class="btn outline" href="https://www.royalenfield.com/in/en/our-world/" target="_blank" rel="noopener">Discover our world ↗</a></div>
</section>
<section class="section experience" id="experience">
  <div class="kicker">Beyond the destination</div><h2>Make the ride yours.</h2>
  <div class="experience-grid">
    <article class="experience-item"><div class="number">01</div><h3>Take the first ride</h3><p>Get a feel for your next motorcycle. Book a test ride and discover the difference on the road.</p></article>
    <article class="experience-item"><div class="number">02</div><h3>Find your people</h3><p>Meet fellow riders, share routes and discover a community that lives for the journey.</p></article>
    <article class="experience-item"><div class="number">03</div><h3>Go beyond</h3><p>Turn weekends into adventures and familiar roads into new experiences.</p></article>
  </div>
</section>
<section class="cta" id="contact"><div class="eyebrow">Your next chapter starts here</div><h2>The road is calling.</h2><p>Find your motorcycle. Plan your ride. Make it unforgettable.</p><button class="btn" data-open-modal>Book a test ride&nbsp; ↗</button></section>
</main>
<footer><div class="footer-top"><div><a class="brand" href="#home">ROYAL ENFIELD<small>MADE LIKE A GUN</small></a><p class="footer-copy">A concept fan website created for learning and demonstration. Not an official Royal Enfield website.</p></div><div class="footer-links"><a href="#models">Motorcycles</a><a href="#heritage">Our story</a><a href="#experience">Experiences</a><a href="https://www.royalenfield.com/in/en/" target="_blank" rel="noopener">Official website ↗</a></div></div><div class="footer-bottom"><span>© 2026 Concept Website</span><span>Ride safe. Ride free.</span></div></footer>
<div class="modal" id="rideModal" role="dialog" aria-modal="true" aria-labelledby="modalTitle"><div class="modal-box"><button class="close" id="closeModal" aria-label="Close">×</button><h2 id="modalTitle">Book a test ride</h2><p>Tell us a little about your preferred ride. This demo form shows a confirmation locally and does not send your information anywhere.</p><form id="rideForm"><div class="form-row"><label for="fullName">Your name</label><input id="fullName" name="name" required placeholder="Enter your name"></div><div class="form-row"><label for="phone">Phone number</label><input id="phone" name="phone" required type="tel" placeholder="Enter your phone number"></div><div class="form-row"><label for="bike">Motorcycle of interest</label><select id="bike" name="bike"><option>Classic 350</option><option>Hunter 350</option><option>Himalayan</option><option>I'd like some guidance</option></select></div><div class="form-row"><label for="city">City</label><input id="city" name="city" placeholder="Enter your city" required></div><button class="btn" type="submit">Request test ride ↗</button><p id="formMessage" aria-live="polite"></p></form></div></div>
<script>
const nav=document.getElementById('nav');
document.getElementById('menu').addEventListener('click',()=>nav.classList.toggle('open'));
nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>nav.classList.remove('open')));
const modal=document.getElementById('rideModal');
document.querySelectorAll('[data-open-modal]').forEach(b=>b.addEventListener('click',()=>{modal.classList.add('open');document.getElementById('fullName').focus()}));
document.getElementById('closeModal').addEventListener('click',()=>modal.classList.remove('open'));
modal.addEventListener('click',e=>{if(e.target===modal)modal.classList.remove('open')});
document.addEventListener('keydown',e=>{if(e.key==='Escape')modal.classList.remove('open')});
document.getElementById('rideForm').addEventListener('submit',e=>{e.preventDefault();document.getElementById('formMessage').textContent='Thanks, '+document.getElementById('fullName').value+'! This demo has recorded no data. Connect a backend to accept real bookings.';});
</script>
</body>
</html>'''
path = Path("/mnt/data/royal_enfield_website.html")
path.write_text(html, encoding="utf-8")
print(f"Created website: {path} ({path.stat().st_size:,} bytes)")
