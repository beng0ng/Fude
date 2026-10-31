#!/bin/sh
# Rebuild the website, the phone app's web files and the browser extension from fude.src.html
set -e
cd "$(dirname "$0")"
python3 build.py
python3 build_ext.py
cp site/icon.svg site/icon-192.png site/privacy.html site/back.js welcome.html ext/
rm -rf ext/fonts && cp -r site/fonts ext/fonts
cp site/index.html site/privacy.html site/back.js site/manifest.webmanifest site/icon.svg site/icon-192.png site/icon-512.png app/www/
rm -rf app/www/fonts && cp -r site/fonts app/www/fonts
if [ -d app/node_modules ]; then (cd app && npx cap copy); else echo "Run 'npm install' in app/ once, then 'npx cap copy' to update the native projects."; fi
