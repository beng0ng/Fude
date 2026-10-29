# Muse for iPhone and Android

This folder turns the Muse website into a real phone app with [Capacitor](https://capacitorjs.com). The app is the same page as `muse-site/index.html`, in the `www` folder, inside a native shell that has its own icon, splash screen and microphone permission.

## What you need
- **iPhone app:** a Mac with Xcode. Publishing to the App Store needs the Apple Developer Program.
- **Android app:** Android Studio on any computer. Publishing to Google Play needs a Google Play developer account.
- Node.js 20 or newer.

## Build and run
1. In this folder, run `npm install`, then `npx cap sync`.
2. Run `npx cap open ios` (opens Xcode) or `npx cap open android` (opens Android Studio).
3. Pick your phone or a simulator and press Run. In Xcode, choose your team under Signing & Capabilities first.

## Updating the app after Muse changes
Copy the new `muse-site/index.html` into `www/`, then run `npx cap sync` and build again.

## What is already set up
- App name **Muse**, app id `app.muse.paint` (change it in `capacitor.config.json` before publishing if you like).
- Icons and splash screens for both platforms, made from the Muse colour wheel (sources in `assets/`).
- Microphone permission, with the message "Muse listens to the music you play so it can paint it."
- **Android:** Muse appears in the Share menu of Spotify, YouTube Music, Apple Music and other apps. Sharing a song opens it in Muse, ready to listen and paint.
- **iPhone:** copy the song's link in your music app (Share, then Copy Link), then press Paste in Muse. A Share menu entry on iPhone needs a separate share extension, which this project does not include yet.

## Listening with Spotify
The app opens straight into the companion: a full-screen painter you keep open while Spotify plays, which paints every song as a new picture. **All of Muse** in the ⋯ menu opens everything else, and the sun/moon button switches between light and dark (it follows the phone's own setting until you choose).
**Link Spotify** signs in through Spotify's page in the system browser and comes back to the app through its own address, `app.muse.paint://spotify` (registered for Android in `AndroidManifest.xml` and for iPhone in `Info.plist`, and handled by the `@capacitor/app` and `@capacitor/browser` plugins).
To turn it on, follow the site README's "Turning on Link Spotify" steps, and add **both** redirect URIs to the Spotify app: the site's address and `app.muse.paint://spotify`. Then put the Client ID in `www/index.html` (or in the site's `index.html` before copying it over) and run `npx cap sync`.

## How the app is laid out
On a phone the app works like an app rather than a web page: a tab bar along the bottom with **Now** (the listening companion it opens to), **Colours**, **Music**, **Style** and **Gallery**, one screen at a time. Links and buttons that used to scroll down the page open the right tab instead, and the phone's back button returns from Now to where you were. Zen mode is in the ⋯ menu on Now.

## Releasing
The `muse-store` folder has everything for the App Store and Google Play: screenshots, the listing text, privacy answers, review notes and the steps to submit. Already done in this project:
- **Version:** 1.0.0 (build 1) on both platforms.
- **iPhone:** a privacy manifest (`PrivacyInfo.xcprivacy`: no tracking, no data collected) and the export-compliance answer (`ITSAppUsesNonExemptEncryption` = NO).
- **Offline:** the fonts and the privacy policy are inside the app (`www/fonts`, `www/privacy.html`), so Muse looks right with no connection.
- **Status bar:** the status bar follows Muse's light or dark, and the screen reaches under the notch with the header padded below it.
- **About and privacy:** this is in the ⋯ menu on Now, with the version number.

