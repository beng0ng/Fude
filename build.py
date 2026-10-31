import json
s=open('fude.src.html').read()
full=s.replace('/*IMGS*/',json.dumps(json.load(open('imgs.json')))).replace('/*SAMPLES*/',json.dumps(json.load(open('samples.json'))))
abcjs=open('vendor/abcjs/abcjs-basic-min.js').read().replace('/*! For license information please see abcjs_basic.LICENSE */','/*! abcjs is MIT licensed: https://github.com/paulrosen/abcjs/blob/main/LICENSE.md */')
assert '</script' not in abcjs.lower()
full=full.replace('/*SCORES*/',open('scores/library-scores.json').read().strip()).replace('<script>/*ABCJS*/</script>','<script>'+abcjs+'</script>')
open('fude.html','w').write(full)
i=full.index('</style>')+len('</style>')
reset='<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>\n'
desc='<meta name="description" content="Fude: give each musical note a color, choose or play a song, and watch it painted in exactly the proportions its notes are played.">\n'
import hashlib
ver=hashlib.sha1(full.encode()).hexdigest()[:10]
head=('<link rel="manifest" href="manifest.webmanifest">\n<meta name="theme-color" content="#F3F0E9">\n<link rel="icon" href="icon.svg" type="image/svg+xml">\n<link rel="apple-touch-icon" href="icon-192.png">\n<meta name="mobile-web-app-capable" content="yes">\n<meta name="apple-mobile-web-app-capable" content="yes">\n<meta name="apple-mobile-web-app-title" content="Fude">\n<meta name="apple-mobile-web-app-status-bar-style" content="default">\n'
 '<meta property="og:title" content="Fude">\n<meta property="og:description" content="Give each note a color, bring a song, and see it painted in exactly the proportions its notes are played.">\n<meta property="og:image" content="preview.jpg">\n<meta property="og:type" content="website">\n<meta name="twitter:card" content="summary_large_image">\n')
sw="<script>if('serviceWorker' in navigator&&location.protocol==='https:'&&!window.Capacitor)addEventListener('load',()=>navigator.serviceWorker.register('sw.js').catch(()=>{}))</script>\n"
GF=full[:i]
import re as _re
fl=_re.search(r'<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2[^"]*">',GF)
assert fl
# the site and the app carry their own copies of the fonts, so they look right offline and make no requests to Google
GF=GF.replace(fl.group(0),'<link rel="stylesheet" href="fonts/fonts.css">')
import os,shutil
shutil.copy('privacy.html','site/privacy.html');shutil.copy('back.js','site/back.js')
FONTFILES=['./fonts/fonts.css']+['./fonts/'+f for f in sorted(os.listdir('site/fonts')) if f.endswith('.woff2')]
open('site/index.html','w').write('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'+desc+head+reset+GF+'\n</head>\n<body>\n'+full[i:]+sw+'\n</body>\n</html>\n')
open('site/sw.js','w').write("""// Fude offline: the page is fetched from the network when it can be and kept for when it cannot
const CACHE='muse-%s',FILES=['./','./index.html','./privacy.html','./back.js','./manifest.webmanifest','./icon.svg','./icon-192.png','./icon-512.png',%s];
self.addEventListener('install',e=>{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(FILES)).then(()=>self.skipWaiting()))});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
self.addEventListener('fetch',e=>{const u=new URL(e.request.url);if(u.origin!==location.origin||e.request.method!=='GET')return;
  e.respondWith(fetch(e.request).then(r=>{if(r.ok){const cp=r.clone();caches.open(CACHE).then(c=>c.put(e.request,cp))}return r}).catch(()=>caches.match(e.request,{ignoreSearch:true}).then(r=>r||caches.match('./index.html'))))});
""" % (ver,",".join(repr(f) for f in FONTFILES)))
open('site/manifest.webmanifest','w').write('{"name":"Fude","short_name":"Fude","description":"Give each note a color, bring a song, and see it painted in exactly the proportions its notes are played.","id":"./","start_url":"./?side=1","scope":"./","display":"standalone","orientation":"any","categories":["music","entertainment","art"],"background_color":"#F3F0E9","theme_color":"#F3F0E9","share_target":{"action":"./","method":"GET","params":{"title":"title","text":"text","url":"url"}},"shortcuts":[{"name":"All of Fude","url":"./?full=1"},{"name":"Listen and paint","url":"./#listen"},{"name":"Bring a song from a music app","url":"./#mlink"}],"icons":[{"src":"icon.svg","sizes":"any","type":"image/svg+xml","purpose":"any"},{"src":"icon-192.png","sizes":"192x192","type":"image/png"},{"src":"icon-512.png","sizes":"512x512","type":"image/png","purpose":"any maskable"}]}')
# a test build that exposes internals on window.__t
site=open('site/index.html').read()
expose="try{localStorage.setItem('muse.seen','1')}catch(e){}\nwindow.__t={get master(){return master},samplesReady,get sampleBufs(){return sampleBufs},playSample,shareState,openShared,get gallery(){return gallery},posterCanvas,get last(){return last},listener,freq,renderVoice,audio,arrangedSong,prepareVoices,voiceCache,voicePending,setArrStyle,tone,startMelody,stopSong,selectSong,get voiceWorker(){return voiceWorker},get playing(){return playing},get song(){return song},get AC(){return AC},get SONGS(){return SONGS},posterA3,tourShow,parseABC,parseMusicXML,parseMIDI,parseMelody,songToABC,scoreSong,SCORES,openStage,closeStage,renderStage,get stageEvents(){return stageEvents},get arrStyle(){return arrStyle},get pick(){return pick},paint};\nif(SIDEMODE)smInit();else if(!(location.hash.length>1&&openShared(location.hash.slice(1))))paint(false,true);\n})();"
assert site.count('if(SIDEMODE)smInit();else if(!(location.hash.length>1&&openShared(location.hash.slice(1))))paint(false,true);\n})();')==1
open('site/test.html','w').write(site.replace('if(SIDEMODE)smInit();else if(!(location.hash.length>1&&openShared(location.hash.slice(1))))paint(false,true);\n})();',expose))
