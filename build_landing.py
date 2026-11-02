# The website: a page about the Chrome and Edge extension, with its privacy policy and a download of the extension
import os,shutil,zipfile
OUT='web'
shutil.rmtree(OUT,ignore_errors=True);os.makedirs(OUT+'/downloads')
shutil.copy('landing/index.html',OUT+'/index.html')
shutil.copytree('landing/media',OUT+'/media')
shutil.copytree('site/fonts',OUT+'/fonts')
for f in ('privacy.html','back.js','icon.svg','icon-192.png','icon-512.png'):shutil.copy('site/'+f,OUT+'/'+f)
with zipfile.ZipFile(OUT+'/downloads/fude-for-chrome.zip','w',zipfile.ZIP_DEFLATED) as z:
  for root,_,files in os.walk('ext'):
    for f in files:
      p=os.path.join(root,f)
      if p!='ext/README.md':z.write(p,os.path.relpath(p,'ext'))
print(sorted(os.listdir(OUT)))
