# Fude as a Chrome/Edge extension: the companion in the browser's side panel, and the whole of Fude in a tab.
# Extension pages allow no inline scripts and no blob workers, so each script and worker becomes a file of its own.
import re,os,json,shutil
from PIL import Image
OUT='ext';keep=open(OUT+'/README.md').read() if os.path.exists(OUT+'/README.md') else None  # the README is written by hand
shutil.rmtree(OUT,ignore_errors=True);os.makedirs(OUT)
if keep:open(OUT+'/README.md','w').write(keep)
page=open('site/index.html').read()
page=re.sub(r"<script>if\('serviceWorker'.*?</script>\n?",'',page,flags=re.S)
page=page.replace('<link rel="manifest" href="manifest.webmanifest">\n','')
scripts=re.findall(r'<script>(.*?)</script>',page,flags=re.S)
assert len(scripts)==3,len(scripts)
names=['theme.js','abc.js','muse.js']
# which is which: the early theme is short, abcjs is the big library, Fude's own script has its engine markers
order=sorted(range(3),key=lambda i:('/*ENGINE-START*/' in scripts[i],len(scripts[i])>5000 and 'abcjs' in scripts[i][:400]))
kinds={}
for i,s in enumerate(scripts):
    kinds[i]='muse.js' if '/*ENGINE-START*/' in s else 'theme.js' if len(s)<400 else 'abc.js'
# the paintings as image files beside the script, rather than text inside it: a smaller script to read when the panel opens
import base64
def unpack(js):
    m=re.search(r'const PAINT_SRC = (\{.*?\});\n',js,flags=re.S)
    if not m:return js
    srcs=json.loads(m.group(1));os.makedirs(f'{OUT}/img',exist_ok=True);out={}
    for k,v in srcs.items():
        head,data=v.split(',',1);ext='jpg' if 'jpeg' in head else 'png' if 'png' in head else 'webp'
        open(f'{OUT}/img/{k}.{ext}','wb').write(base64.b64decode(data));out[k]=f'img/{k}.{ext}'
    return js[:m.start(1)]+json.dumps(out)+js[m.end(1):]
for i,s in enumerate(scripts):open(f'{OUT}/{kinds[i]}','w').write(unpack(s) if kinds[i]=='muse.js' else s)
k=[0]
def sub(m):
    i=k[0];k[0]+=1;return f'<script src="{kinds[i]}"></script>'
body=re.sub(r'<script>.*?</script>',sub,page,flags=re.S)
for kind in ['panel','full']:
    open(f'{OUT}/flag-{kind}.js','w').write(f"window.MUSE_EXT='{kind}';\n")
    html=body.replace('<script src="theme.js"></script>',f'<script src="flag-{kind}.js"></script><script src="theme.js"></script>',1)
    if kind=='panel':html=html.replace('<title>Fude</title>','<title>Fude · beside your music</title>')
    open(f'{OUT}/{kind}.html','w').write(html)
# the workers, from the same marked code the page uses
src=[s for s in scripts if '/*ENGINE-START*/' in s][0]
def between(a,b):i=src.index(a)+len(a);return src[i:src.index(b,i)]
eng=between('/*ENGINE-START*/','/*ENGINE-END*/');voice=between('/*VOICE-START*/','/*VOICE-END*/')
ptail=between('/*PAINT-TAIL*/','/*PAINT-TAIL-END*/').strip();vtail=between('/*VOICE-TAIL*/','/*VOICE-TAIL-END*/').strip()
assert ptail[0]=='`' and ptail[-1]=='`' and '${' not in ptail;assert vtail[0]=="'" and vtail[-1]=="'"
open(f'{OUT}/paint-worker.js','w').write(eng+ptail[1:-1])
open(f'{OUT}/voice-worker.js','w').write(voice+vtail[1:-1].replace('\\n','\n'))
open(f'{OUT}/background.js','w').write("""// Fude: the toolbar button (or Alt+Shift+F) opens the side panel beside the tab and lets Fude hear that tab.
// Chrome only lets an extension hear a tab after its button was pressed on that tab, so the press is handled here:
// it opens the panel, asks Chrome for the tab's sound at once, and tells the panel which tab to paint
chrome.runtime.onInstalled.addListener(()=>{chrome.sidePanel.setPanelBehavior({openPanelOnActionClick:false}).catch(()=>{})});
chrome.sidePanel.setPanelBehavior({openPanelOnActionClick:false}).catch(()=>{});
chrome.action.onClicked.addListener(tab=>{
  chrome.sidePanel.open({windowId:tab.windowId}).catch(()=>{});
  const tell=streamId=>{const v={tabId:tab.id,streamId:streamId||'',at:Date.now()};chrome.storage.session.set({fudeTab:v}).catch(()=>{});chrome.runtime.sendMessage({fude:'tab',...v}).catch(()=>{})};
  if(!/^https?:/.test(tab.url||'https:'))return tell('');
  chrome.tabCapture.getMediaStreamId({targetTabId:tab.id},id=>{void chrome.runtime.lastError;tell(id)});
});
""")
# asking for the microphone happens in a tab of its own: a side panel cannot show Chrome's permission question
open(f'{OUT}/mic.html','w').write("""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Fude · microphone</title>
<link rel="stylesheet" href="fonts/fonts.css"><link rel="icon" href="icon.svg" type="image/svg+xml">
<style>:root{--bg:#F3F0E9;--fg:#2B2925;--muted:#6E685F;--accent:#4F6E5E;color-scheme:light}@media (prefers-color-scheme:dark){:root{--bg:#171614;--fg:#E8E3DA;--muted:#A39D92;--accent:#9DBBA9;color-scheme:dark}}
body{margin:0;min-height:100vh;display:grid;place-items:center;background:var(--bg);color:var(--fg);font:16px/1.6 "Hanken Grotesk",system-ui,sans-serif;text-align:center;padding:24px;box-sizing:border-box}
h1{font:500 30px/1.25 "Shippori Mincho",Georgia,serif;margin:0 0 8px}p{color:var(--muted);max-width:420px;margin:0 auto 22px}
button{font:inherit;font-weight:500;border:0;border-radius:999px;padding:12px 26px;background:var(--fg);color:var(--bg);cursor:pointer}button:focus-visible{outline:2px solid var(--accent);outline-offset:3px}</style></head>
<body><main><h1 id="h">Let Fude use the microphone</h1><p id="p">Chrome asks for this in a tab of its own. Fude only listens while you have pressed Start, and nothing it hears is kept or sent anywhere.</p><button id="b" type="button">Allow the microphone</button></main><script src="mic.js"></script></body></html>
""")
open(f'{OUT}/mic.js','w').write("""const done=()=>{document.getElementById('h').textContent='The microphone is on';document.getElementById('p').textContent='Go back to the Fude panel and press Start. You can close this tab.';document.getElementById('b').hidden=true;chrome.runtime.sendMessage({fude:'mic'}).catch(()=>{})};
document.getElementById('b').onclick=async()=>{try{const s=await navigator.mediaDevices.getUserMedia({audio:true});s.getTracks().forEach(t=>t.stop());done()}catch(e){document.getElementById('p').textContent=e&&e.name==='NotAllowedError'?'Chrome blocked it. Click the icon at the left of the address bar, allow the microphone, and try again.':'No microphone was found on this computer.'}};
navigator.permissions.query({name:'microphone'}).then(p=>{if(p.state==='granted')done()}).catch(()=>{});
""")
ic=Image.open('site/icon-512.png').convert('RGBA')
for n in (16,32,48,128):ic.resize((n,n),Image.LANCZOS).save(f'{OUT}/icon-{n}.png')
music=['https://open.spotify.com/*','https://music.youtube.com/*','https://www.youtube.com/*','https://music.apple.com/*','https://soundcloud.com/*','https://www.deezer.com/*','https://listen.tidal.com/*','https://*.bandcamp.com/*']
man={"manifest_version":3,"name":"Fude: paint your music","short_name":"Fude","version":"1.0.6",
 "description":"Fude paints the music playing in your browser, song by song, in the side panel: Spotify, YouTube and more.",
 "icons":{str(n):f'icon-{n}.png' for n in (16,32,48,128)},
 "action":{"default_title":"Paint this music with Fude","default_icon":{str(n):f'icon-{n}.png' for n in (16,32)}},
 "side_panel":{"default_path":"panel.html"},
 "background":{"service_worker":"background.js"},
 "permissions":["sidePanel","tabCapture","activeTab","scripting","identity","storage"],
 "optional_permissions":["desktopCapture"],
 "commands":{"_execute_action":{"suggested_key":{"default":"Alt+Shift+F"},"description":"Paint the music in this tab"}},
 "host_permissions":music+['https://api.spotify.com/*','https://accounts.spotify.com/*'],
 "minimum_chrome_version":"116"}
open(f'{OUT}/manifest.json','w').write(json.dumps(man,indent=2))
print(sorted(os.listdir(OUT)))
