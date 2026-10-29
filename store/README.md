# Muse: release kit

Everything needed to put Muse on the App Store and Google Play. The app itself is in the `muse-app` folder next to this one.

## What is in this folder

| File | What it is for |
|---|---|
| `app-store/iphone-6.9in/1.png` … `5.png` | iPhone screenshots, 1320 × 2868 (App Store Connect scales them for smaller iPhones) |
| `app-store/ipad-13in/1.png` … `3.png` | iPad screenshots, 2064 × 2752 (needed because the app also runs on iPad) |
| `app-store/icon-1024.png` | App Store icon (the same one already inside the Xcode project) |
| `google-play/phone/1.png` … `5.png` | Phone screenshots for Google Play, 1080 × 1920 |
| `google-play/feature-graphic.png` | Google Play feature graphic, 1024 × 500 |
| `google-play/icon-512.png` | Google Play app icon, 512 × 512 |
| `privacy.html` | The privacy policy. It is also in `muse-site`, so it goes online with the site. |

## Store listing

**Name:** Muse: Paint Your Music
(Plain "Muse" is very likely taken on both stores. The app's name under its icon stays "Muse".)

**Subtitle (App Store) / short description (Google Play):** Every song becomes a painting

**Promotional text (App Store, can change any time):**
Keep Muse open while your music plays. It listens, finds the notes, and paints a new picture for every song, while a little cat paints along.

**Description:**

Muse turns the music you listen to into paintings.

Put on a song, in Spotify or anywhere else, and open Muse. It listens, works out the notes as they sound, and paints them. Every note has its own color, and each color covers exactly as much of the canvas as its note is played. When the song changes, a new painting begins.

• Every song becomes a painting: famous pictures like The Starry Night and The Great Wave, recolored by your music, or new abstract ones.
• Give each note your own color, or start from the color scales of Newton, Scriabin and Rimsky-Korsakov.
• Listen live through the microphone, play a song from the built-in library, or bring your own music and sheet music.
• A gallery keeps every painting, with a chart of the notes behind it. Save posters or share them.
• Calm by design: light and dark modes, a zen mode, and no ads.

Private by design: Muse works out the notes on your device. Nothing it hears is recorded or sent anywhere, and it has no accounts and no tracking.

**Keywords (App Store, 100 characters):**
music,painting,art,visualizer,color,synesthesia,notes,zen,relax,piano,song,canvas,draw,spotify

**Category:** Music. Second category: Entertainment.

**Age rating:** 4+ on the App Store; "Everyone" on Google Play. Answer "no" to every content question.

**Privacy policy URL:** `https://<your site>/privacy.html` once `muse-site` is online.
**Support URL:** the site's address works.

## Privacy answers

- **App Store, App Privacy:** choose **Data Not Collected**. Muse has no server, no analytics and no tracking. The microphone is processed on the device and never leaves it.
- **Google Play, Data safety:** "Does your app collect or share any of the required user data types?" **No.** Sound the app processes on the device only, without sending it off the device, does not count as collected.
- **Export compliance (App Store):** already answered in the app (`ITSAppUsesNonExemptEncryption` is set to NO), because Muse only uses standard HTTPS.

## Notes for the App Review team

Paste this into App Store Connect under App Review Information → Notes:

> Muse paints the music it hears. To try it, play any song near the device (or on the device itself) and tap Start on the Now screen; allow the microphone when asked. A painting forms within a few seconds and grows as the song plays. The Music tab also has built-in songs that play and paint with no microphone needed. No account or sign-in is required.

## What only you can do

1. **Put the site online** so the privacy policy has an address. Drag the `muse-site` folder onto app.netlify.com/drop. That gives you a link like `https://something.netlify.app`, and the policy is at `/privacy.html`.
2. **iPhone and iPad**
   1. Join the Apple Developer Program ($99 a year).
   2. On a Mac, open `muse-app` and run `npm install`, then `npx cap sync ios`, then `npx cap open ios`.
   3. In Xcode, choose your team under Signing & Capabilities. Plug in your iPhone and press Run to try it on the phone.
   4. Choose Product → Archive, then Distribute App → App Store Connect.
   5. In App Store Connect, create the app with the bundle ID `app.muse.paint`. Fill in the listing from this page, add the screenshots, and submit. TestFlight lets you install the build on your own phone first.
3. **Android**
   1. Create a Google Play developer account ($25 once).
   2. Open `muse-app` and run `npm install`, then `npx cap sync android`, then `npx cap open android`.
   3. Plug in an Android phone with USB debugging on and press Run to try it.
   4. Choose Build → Generate Signed App Bundle and create an upload key. **Keep the key file and its password safe.** Every future update must be signed with the same key.
   5. In Play Console, create the app, fill in the listing and the Data safety form from this page, and upload the `.aab` file.
   6. Google requires new personal developer accounts to run a closed test with at least 12 testers for 14 days before they can publish to everyone. Start that test early.
4. **Spotify linking (optional, can wait for an update).** The app works with Spotify without linking: Muse hears the music through the microphone. The **Link Spotify** button stays hidden until you add a Spotify Client ID (see "Listening with Spotify" in the `muse-app` README). Spotify only allows 25 hand-picked users until it approves the app for wider use, so release without it first.

## For each update

1. Raise the version.
   - **Android:** `versionCode` and `versionName` in `android/app/build.gradle`.
   - **iPhone:** in Xcode, under General → Identity.
2. Copy the new `muse-site` files into `muse-app/www`.
3. Run `npx cap sync` and build again.
