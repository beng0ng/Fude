# Fude: release kit

Everything needed to put Fude on the App Store, Google Play and the Chrome Web Store. The phone app is in the `fude-app` folder next to this one and the browser extension in `fude-extension`.

## What is in this folder

| File | What it is for |
|---|---|
| `app-store/iphone-6.9in/1.png` … `5.png` | iPhone screenshots, 1320 × 2868 (App Store Connect scales them for smaller iPhones) |
| `app-store/ipad-13in/1.png` … `3.png` | iPad screenshots, 2064 × 2752 (needed because the app also runs on iPad) |
| `app-store/icon-1024.png` | App Store icon (the same one already inside the Xcode project) |
| `google-play/phone/1.png` … `5.png` | Phone screenshots for Google Play, 1080 × 1920 |
| `google-play/feature-graphic.png` | Google Play feature graphic, 1024 × 500 |
| `google-play/icon-512.png` | Google Play app icon, 512 × 512 |
| `chrome-web-store/screenshot-1.png` … `5.png` | Chrome Web Store screenshots, 1280 × 800 |
| `chrome-web-store/promo-small.png` | Chrome Web Store small promo tile, 440 × 280 |
| `chrome-web-store/icon-128.png` | Chrome Web Store icon (the same one inside the extension) |
| `privacy.html` | The privacy policy. It is also in `fude-site`, so it goes online with the site. |

## Store listing

**Name:** Fude: Paint Your Music
(The name under the icon is just "Fude". The longer store name helps people find it when they search.)

**Subtitle (App Store) / short description (Google Play):** Every song becomes a painting

**Promotional text (App Store, can change any time):**
Pick a famous painting, choose its colors, and let your music repaint it. A little cat paints along, and the more you listen, the more pets and effects you unlock.

**Description:**

Fude turns the music you listen to into paintings.

Put on a song, in Spotify or anywhere else, and open Fude. It listens, works out the notes as they sound, and paints them. Every note has its own color, and each color covers exactly as much of the canvas as its note is played. A little cat paints the picture from the bottom up while the song plays, and when the song changes, a new painting begins.

• Start from a famous picture like The Starry Night or The Great Wave, or a new abstract one, and let the music recolor it while every brushstroke stays sharp.
• Choose the colors: your own, a preset like Sunset, Ocean or Neon night, a color wheel, or the scales of Newton, Scriabin and Rimsky-Korsakov.
• Watch the song's mood in words, the notes as they arrive, and the lyrics scrolling in time when Fude knows the song.
• Earn new pets and effects the more you listen and paint. When the music stops, your pet stops too and looks up at you.
• A gallery keeps every painting with the song it came from and how long it took to paint. Save posters or share them.
• Listen through the microphone, follow your music app on Android, play songs from the built-in library, or bring your own.
• Calm by design: light and dark modes, a zen mode, and no ads.

Private by design: Fude works out the notes on your device. Nothing it hears is recorded or sent anywhere, and it has no accounts and no tracking.

**Keywords (App Store, 100 characters):**
music,painting,art,visualizer,color,synesthesia,notes,zen,relax,piano,song,canvas,draw,spotify

**Category:** Music. Second category: Entertainment.

**Age rating:** 4+ on the App Store; "Everyone" on Google Play. Answer "no" to every content question.

**Privacy policy URL:** `https://<your site>/privacy.html` once `fude-site` is online.
**Support URL:** the site's address works.

## Privacy answers

- **App Store, App Privacy:** choose **Data Not Collected**. Fude has no server, no analytics and no tracking. The microphone is processed on the device and never leaves it. The only thing sent anywhere is a song's title, artist and length to LRCLIB for lyrics, which is not linked to the person and can be switched off, so it does not count as collected data.
- **Google Play, Data safety:** "Does your app collect or share any of the required user data types?" **No.** Sound the app processes on the device only, without sending it off the device, does not count as collected. The same goes for the song names and covers the Android app reads from the music app with headphones in: they never leave the phone.
- **Export compliance (App Store):** already answered in the app (`ITSAppUsesNonExemptEncryption` is set to NO), because Fude only uses standard HTTPS.

## Chrome Web Store (and Microsoft Edge Add-ons)

Upload `fude-extension.zip`. The same zip works for Edge in Microsoft Partner Center.

**Name:** Fude: paint your music (taken from the extension itself)

**Summary (132 characters max):** Fude paints the music playing in your browser, song by song, in the side panel: Spotify, YouTube and more.

**Category:** Entertainment. **Language:** English.

**Description:**

Fude turns the music playing in your browser into paintings, right in the side panel.

Play a song on Spotify, YouTube, YouTube Music, Apple Music, SoundCloud, Deezer, Tidal, Bandcamp or any other site, then click the Fude button. Fude hears that tab (headphones are fine, no microphone needed), works out the notes as they sound and paints them. Every note has its own color, and each color covers exactly as much of the canvas as its note is played. A little cat paints from the bottom up while the song plays, and a new painting starts with every new song.

• Pick a famous painting or an abstract one each time you open Fude, then choose its colors: your own, a preset, a color wheel, or a mood you describe.
• A peek window shows the corner the cat is painting; the full picture is revealed when it's done.
• See the song's mood, the notes as they arrive, and the lyrics scrolling in time with the song.
• Earn new pets and effects the more you listen and paint. When the music stops, your pet stops and looks up at you; press Pause to keep the painting open.
• Switch tab lets Fude follow music in another tab, and Hear the whole computer covers desktop apps on Windows and ChromeOS.
• A gallery keeps every painting with its song and how long it took.

Private by design: the sound is turned into notes on your computer and is never recorded or sent. No accounts, no ads, no tracking.

**What a new user sees:** installing opens a short how-to page, and the ⋯ menu's About and privacy has the version, the how-to and the privacy policy, so reviewers can find their way without instructions.

**Single purpose:** Fude turns the music playing in a browser tab into a painting shown in the side panel.

**Permission justifications** (paste each into its box):
- `sidePanel`: Fude's whole interface is the side panel beside the music tab.
- `tabCapture`: to hear the music tab the person clicked Fude's button on, or picked with Switch tab, and turn its sound into notes on the computer. Nothing is recorded or sent.
- `activeTab`: lets Fude capture and read the tab only after the person clicks its button on that tab.
- `scripting`: to read the song's title, artist, cover and play position from the page's Media Session on the listed music sites, so each painting is named after its song and a new painting starts when the song changes.
- `storage`: keeps settings, colors and unlocked pets on the computer.
- Host permissions (open.spotify.com, music.youtube.com, www.youtube.com, music.apple.com, soundcloud.com, www.deezer.com, listen.tidal.com, *.bandcamp.com): the music sites whose Media Session Fude reads, as above. Nothing else on the page is read.
- Optional `desktopCapture`: asked for only when the person turns on Hear the whole computer, to hear a desktop music app. Only the sound is kept.
- Optional `identity`: asked for only if Spotify linking is ever turned on (it is off in this release).
- **Remote code:** No, Fude does not use remote code. All scripts are in the package.

**Data usage (Privacy practices tab):** tick none of the data types. Then tick all three certifications (no selling, no unrelated use, no creditworthiness use). Song titles and artists are sent to LRCLIB only to fetch lyrics and are not collected by Fude.

**Privacy policy URL:** the same `https://<your site>/privacy.html`.

## Notes for the App Review team

Paste this into App Store Connect under App Review Information → Notes:

> Fude paints the music it hears. To try it, play any song near the device (or on the device itself) and tap Start on the Now screen; allow the microphone when asked. A painting forms within a few seconds and grows as the song plays. The Music tab also has built-in songs that play and paint with no microphone needed. No account or sign-in is required.

## What only you can do

1. **Put the site online** so the privacy policy has an address. Drag the `fude-site` folder onto app.netlify.com/drop. That gives you a link like `https://something.netlify.app`, and the policy is at `/privacy.html`.
2. **iPhone and iPad**
   1. Join the Apple Developer Program ($99 a year).
   2. On a Mac, open `fude-app` and run `npm install`, then `npx cap sync ios`, then `npx cap open ios`.
   3. In Xcode, choose your team under Signing & Capabilities. Plug in your iPhone and press Run to try it on the phone.
   4. Choose Product → Archive, then Distribute App → App Store Connect.
   5. In App Store Connect, create the app with the bundle ID `app.fude.paint`. Fill in the listing from this page, add the screenshots, and submit. TestFlight lets you install the build on your own phone first.
3. **Android**
   1. Create a Google Play developer account ($25 once).
   2. Open `fude-app` and run `npm install`, then `npx cap sync android`, then `npx cap open android`.
   3. Plug in an Android phone with USB debugging on and press Run to try it.
   4. Choose Build → Generate Signed App Bundle and create an upload key. **Keep the key file and its password safe.** Every future update must be signed with the same key.
   5. In Play Console, create the app, fill in the listing and the Data safety form from this page, and upload the `.aab` file.
   6. Google requires new personal developer accounts to run a closed test with at least 12 testers for 14 days before they can publish to everyone. Start that test early.
4. **Chrome and Edge**
   1. Register as a Chrome Web Store developer at chrome.google.com/webstore/devconsole ($5 once).
   2. Choose **New item**, upload `fude-extension.zip`, and fill in the listing, privacy tab and permission answers from the Chrome Web Store section above. Add the pictures from `chrome-web-store`.
   3. For Edge, sign in at partner.microsoft.com/dashboard/microsoftedge (free) and upload the same zip.
5. **Spotify linking (optional, can stay off).** The app works with Spotify without linking: through the microphone with a speaker, and on Android with headphones too, by following the music app. The **Link Spotify** button stays hidden until you add a Spotify Client ID (see "Listening with Spotify" in the `fude-app` README). Spotify now allows only 5 hand-picked accounts per app and only opens apps to everyone for registered businesses, so release without it.

## For each update

1. Raise the version.
   - **Android:** `versionCode` and `versionName` in `android/app/build.gradle`.
   - **iPhone:** in Xcode, under General → Identity.
2. Copy the new `fude-site` files into `fude-app/www`.
3. Run `npx cap sync` and build again.
4. **Extension:** upload the new `fude-extension.zip` in the Chrome Web Store dashboard under Package. The version inside it must be higher than the last one.
