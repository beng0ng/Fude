# Fude for Chrome and Edge

Fude sits in the browser's side panel and paints whatever is playing in the tab next to it: Spotify's web player, YouTube, YouTube Music, Apple Music, SoundCloud, Deezer, Tidal, Bandcamp, or any other site. It hears the tab's own sound, so headphones are fine and no microphone is needed. Each song becomes its own picture, named after the song when the site shares what's playing.

## Try it now (unpacked)
1. Open `chrome://extensions` (or `edge://extensions`) and turn on **Developer mode**.
2. Choose **Load unpacked** and pick this `fude-extension` folder (or unzip `fude-extension.zip` and pick that).
3. Pin Fude to the toolbar. Open your music in a tab, then click the Fude button (or press **Alt+Shift+F**). The side panel opens beside it and starts painting that tab straight away.
4. You'll keep hearing the music through Fude while it paints. Clicking the button on another tab moves Fude over to that tab.

If Fude says it can't hear the tab, click the Fude button again while the music tab is in front. Chrome only lets an extension listen to a tab after you click its button on that tab. In the ⋯ menu, **Listen to the music tab** off switches to the microphone instead; the first time, Fude opens a tab where Chrome asks for the microphone, because a side panel can't ask. **All of Fude** opens the full app in a tab.

## What it asks for, and why
- **Tab capture, active tab**: to hear the tab you clicked Fude on. Nothing is recorded or sent anywhere.
- **Scripting, and the music sites listed in the manifest**: to read the song's name, artist and cover from the page's Media Session (what your keyboard's media keys and lock screen show).
- **Side panel**: to show Fude beside the page.
- **Identity, and the Spotify addresses**: only for the optional Link Spotify.

## Publishing it
Upload `fude-extension.zip` in the Chrome Web Store developer dashboard (and in Microsoft Partner Center for Edge). The store review will ask why each permission is needed; the list above is the answer.

## Link Spotify (optional)
Fude already follows Spotify's web player without a Spotify login. Linking adds play, pause and skip, and lets Fude follow the Spotify desktop or phone app. To turn it on, add `https://<extension-id>.chromiumapp.org/spotify` as a redirect URI in your Spotify app (the ID is shown on `chrome://extensions`; it changes once the extension is in the store). Then set `SPOTIFY_CLIENT_ID` in `muse.js`.

## Rebuilding
These files are made from the Fude site. When Fude changes, the extension is rebuilt from the new `index.html`: each script becomes its own file, because extension pages can't run inline scripts.
