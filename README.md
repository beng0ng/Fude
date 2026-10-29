# Fude

Fude turns music into paintings. Every note has its own color, and each color covers as much of the canvas as its note is played. Keep it open while your music plays, and it paints a new picture for every song while a little cat paints along.

It runs as a website, an iPhone and Android app, and a Chrome or Edge side panel.

## What's here

| Folder or file | What it is |
|---|---|
| `fude.src.html` | The whole app, in one file. Edit this. |
| `build.sh` | Rebuilds everything below from `fude.src.html`. |
| `site/` | The website. Publish this folder (Netlify, GitHub Pages, Cloudflare Pages). It works offline and installs to the home screen. |
| `app/` | The iPhone and Android app (Capacitor). See `app/README.md`. |
| `ext/` | The browser extension. Load it unpacked from `chrome://extensions`. |
| `store/` | App Store and Google Play screenshots, listing text and the privacy policy. See `store/README.md`. |
| `privacy.html` | The privacy policy, copied into the site, app and extension. |
| `imgs.json`, `samples.json`, `scores/`, `vendor/abcjs/` | Paintings, instrument samples, song library and the sheet-music engine that the build puts into the page. |

## Making a change

1. Edit `fude.src.html`.
2. Run `./build.sh` (needs Python 3; for the native projects, also Node.js and `npm install` in `app/`).
3. Commit. If the site is connected to Netlify or GitHub Pages, it updates by itself.

## Licenses

The paintings are public domain. The sheet-music engine is [abcjs](https://github.com/paulrosen/abcjs) (MIT, see `vendor/abcjs/LICENSE.md`). The fonts are Shippori Mincho, Hanken Grotesk and IBM Plex Mono (SIL Open Font License).
