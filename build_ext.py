# Muse as a Chrome/Edge extension: the companion in the browser's side panel, and the whole of Muse in a tab.
# Extension pages allow no inline scripts and no blob workers, so each script and worker becomes a file of its own.
import re,os,json,shutil
from PIL import Image
OUT='ext';shutil.rmtree(OUT,ignore_errors=True);os.makedirs(OUT)
page=open('site/index.html').read()
page=re.sub(r"<script>if\('serviceWorker'.*?</script>\n?",'',page,flags=re.S)
page=page.replace('<link rel="manifest" href="manifest.webmanifest">\n','')
scripts=re.findall(r'<script>(.*?)</script>',page,flags=re.S)
assert len(scripts)==3,len(scripts)
names=['theme.js','abc.js','muse.js']
# which is which: the early theme is short, abcjs is the big library, Muse's own script has its engine markers
order=sorted(range(3),key=lambda i:('/*ENGINE-START*/' in scripts[i],len(scripts[i])>5000 and 'abcjs' in scripts[i][:400]))
kinds={}
for i,s in enumerate(scripts):
    kinds[i]='muse.js' if '/*ENGINE-START*/' in s else 'theme.js' if len(s)<400 else 'abc.js'
for i,s in enumerate(scripts):open(f'{OUT}/{kinds[i]}','w').write(s)
k=[0]
def sub(m):
    i=k[0];k[0]+=1;return f'<script src="{kinds[i]}"></script>'
body=re.sub(r'<script>.*?</script>',sub,page,flags=re.S)
for kind in ['panel','full']:
    open(f'{OUT}/flag-{kind}.js','w').write(f"window.MUSE_EXT='{kind}';\n")
    html=body.replace('<script src="theme.js"></script>',f'<script src="flag-{kind}.js"></script><script src="theme.js"></script>',1)
    if kind=='panel':html=html.replace('<title>Muse</title>','<title>Muse · beside your music</title>')
    open(f'{OUT}/{kind}.html','w').write(html)
# the workers, from the same marked code the page uses
src=[s for s in scripts if '/*ENGINE-START*/' in s][0]
def between(a,b):i=src.index(a)+len(a);return src[i:src.index(b,i)]
eng=between('/*ENGINE-START*/','/*ENGINE-END*/');voice=between('/*VOICE-START*/','/*VOICE-END*/')
ptail=between('/*PAINT-TAIL*/','/*PAINT-TAIL-END*/').strip();vtail=between('/*VOICE-TAIL*/','/*VOICE-TAIL-END*/').strip()
assert ptail[0]=='`' and ptail[-1]=='`' and '${' not in ptail;assert vtail[0]=="'" and vtail[-1]=="'"
open(f'{OUT}/paint-worker.js','w').write(eng+ptail[1:-1])
open(f'{OUT}/voice-worker.js','w').write(voice+vtail[1:-1].replace('\\n','\n'))
open(f'{OUT}/background.js','w').write("""// Muse: the toolbar button opens the side panel, which paints whatever is playing in the tab beside it
chrome.runtime.onInstalled.addListener(()=>{chrome.sidePanel.setPanelBehavior({openPanelOnActionClick:true}).catch(()=>{})});
chrome.sidePanel.setPanelBehavior({openPanelOnActionClick:true}).catch(()=>{});
""")
ic=Image.open('site/icon-512.png').convert('RGBA')
for n in (16,32,48,128):ic.resize((n,n),Image.LANCZOS).save(f'{OUT}/icon-{n}.png')
music=['https://open.spotify.com/*','https://music.youtube.com/*','https://www.youtube.com/*','https://music.apple.com/*','https://soundcloud.com/*','https://www.deezer.com/*','https://listen.tidal.com/*','https://*.bandcamp.com/*']
man={"manifest_version":3,"name":"Muse: paint your music","short_name":"Muse","version":"1.0.0",
 "description":"Muse paints the music playing in your browser, song by song, in the side panel: Spotify, YouTube and more.",
 "icons":{str(n):f'icon-{n}.png' for n in (16,32,48,128)},
 "action":{"default_title":"Paint this music with Muse","default_icon":{str(n):f'icon-{n}.png' for n in (16,32)}},
 "side_panel":{"default_path":"panel.html"},
 "background":{"service_worker":"background.js"},
 "permissions":["sidePanel","tabCapture","activeTab","scripting","identity"],
 "host_permissions":music+['https://api.spotify.com/*','https://accounts.spotify.com/*'],
 "minimum_chrome_version":"116"}
open(f'{OUT}/manifest.json','w').write(json.dumps(man,indent=2))
print(sorted(os.listdir(OUT)))
