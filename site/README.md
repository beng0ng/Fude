# Fude — standalone site

One file, `index.html`, with everything inside it (paintings, fonts link, code). No build step and no server code.

## Why a standalone site
Live listening needs your browser's permission to use the microphone or to share a tab's audio. The Claude page viewer blocks both, so they only work when Fude runs as its own website (or opened straight from your computer).

## Put it online (pick one)
- **Netlify Drop (fastest, free):** go to https://app.netlify.com/drop and drag this `fude-site` folder onto the page. You get a link in seconds.
- **GitHub Pages:** create a public repository, add `index.html` at its root, then in the repository's Settings → Pages, choose "Deploy from a branch" with `main` and `/ (root)`. The site appears at `https://<your-username>.github.io/<repository>/`.
- **Just try it:** double-click `index.html` to open it in Chrome. The microphone and tab listening work from a local file too.

The site must be served over `https://` (all three options above are) for the browser to allow listening.

## On your phone
- **Install it:** once the site is online, open it in Safari (iPhone) or Chrome (Android). On iPhone, press **Get the app** on the opening screen, or tap Share then **Add to Home Screen**. On Android, press **Get the app** or choose Install from the browser menu. Fude then opens from its own icon, full screen, works offline, and keeps your colours and paintings. The menu at the bottom of the screen has the four steps and Zen mode.
- **App Store and Google Play:** the `fude-app` folder next to this one is a ready Capacitor project that wraps this page as a native iPhone and Android app. Its README says how to build it.

## Listening with Spotify (the companion)
- The installed app now opens straight into the companion: a full-screen painter you keep open while music plays. **Paint along with Spotify** on the front page (or **Paint on the side** in Bring the music) opens it from the site. It shows the painting and one Start button; New painting, Save, Headphones, Open Spotify and **All of Fude** are in the ⋯ menu. On a computer with Chrome or Edge it floats on top of your other windows; elsewhere it opens as a small window, and on a phone it fills the screen.
- Without Spotify linked it works as before. It hears each song start from the sound level, paints it as a new picture, finishes it after the short pause at the end, and waits for the next one. Songs that run straight into each other are painted as one; press **New painting** at the change.
- **Link Spotify** shows what is playing (cover, title, artist, progress) with previous, play/pause and next. Each track change starts a new picture named after the track, and pausing for 15 seconds finishes the current one. Play and skip need Spotify Premium; Fude says so if they are refused.
- **Headphones on** (in the ⋯ menu). With a speaker, Fude paints from what the microphone hears. With headphones nothing reaches the microphone, so Fude paints from the colours of each track's cover, matched to your note colours. If Fude hears nothing for a while it suggests switching.
- The screen stays on while it paints, where the browser allows it. On a phone, Fude has to stay on screen to keep listening: start the music in Spotify, then come back to Fude.
- The strip along the bottom holds this session's paintings (tap one to save it), and every painting also goes to your gallery.

### Turning on Link Spotify (one-time setup)
Spotify only lets a registered app read what you are playing, so the button stays hidden until Fude has a Spotify client ID.
1. Sign in at developer.spotify.com, open the Dashboard and **Create app**. Tick **Web API**.
2. Add the exact address where Fude is hosted as a **Redirect URI**, for example `https://yourname.github.io/fude/` (ending the same way the address does, usually with `/`).
3. Copy the app's **Client ID** into `const SPOTIFY_CLIENT_ID=''` in `index.html`, and upload it again. No secret is needed; Fude signs in with Spotify's PKCE flow.
4. Spotify's rules since 2026: an app in development mode needs its owner to have **Spotify Premium**, and only up to **5** Spotify accounts that you add under **User Management** can link. Spotify only opens apps to everyone for registered businesses, so for most people Link Spotify is for you and a few friends.
Linking works on the hosted site and its home-screen app. It does not work inside Claude's preview. The iPhone/Android app links too, once `app.fude.paint://spotify` is added as a second redirect URI (see its README). The Android app doesn't need linking to follow Spotify with headphones in; see "Headphones" in the app's README.

## Songs from Spotify and other music apps
- Paste or share a song link from **Spotify, Apple Music, YouTube, SoundCloud, Deezer or Tidal** into "From your music app" in Bring the music (the Paste button reads it from the clipboard). On Android, once Fude is installed, it also appears in the music app's own Share menu.
- Fude shows the service's own player for that song, with the song's name (taken from the share, the link, or the service's public lookup, and editable). Press play there, then **Listen and paint**: Fude hears it through the microphone and paints it, and the painting is named after the song. On a computer, **Listen to this tab** hears the player directly instead.
- When the song is a piece Fude already has (Für Elise, Gymnopédie No. 1, Canon in D and the rest of the library), Fude offers to play its own score and paint it instead, with no listening needed.
- Why listening: Spotify and the other services do not let any other app read their audio, and Spotify has closed its song-analysis data to new apps, so hearing the song is how Fude gets its notes. Without a Spotify login in the browser, Spotify's player plays a 30-second preview.

## Listening live
Fude finds notes by summing each candidate pitch's harmonics, taking the strongest, removing its overtones and looking again, so a bass note no longer masquerades as three. Onsets drive the notes that fly across the page, and the bass line helps name the chords (now including suspended, diminished and sixth chords).

- **Microphone:** the site asks for the microphone as soon as it opens, so the first listen is one press of "Start listening". The "Listen live" card shows "Microphone ready" once it is allowed. Play your song on any speaker nearby and press "Stop listening" when it ends. If you dismissed the prompt, the browser's site settings (the lock icon in the address bar) let you allow it later.
- **A browser tab (Chrome or Edge on a computer):** press "Listen to a browser tab", pick the tab playing Spotify Web, YouTube or anything else, and turn on **Also share tab audio**. The music keeps playing in that tab while Fude listens.
- **Paste a link:** paste a YouTube, Spotify or any other link into the box on the "Listen live" card and press "Open and listen". Fude opens it in a new tab and asks you to share that tab's audio.

## Your own music
- **Sheet music:** drop a MIDI (.mid), MusicXML (.musicxml, .xml, .mxl) or ABC (.abc) file on the "Your own music" card. ABC ties, dotted pairs (A>B), triplets and chord lengths are read as written, and MusicXML parts for transposing instruments (clarinet, trumpet, horn, saxophone) sound at concert pitch. Each track or voice becomes a part with its own instrument, and Fude plays and paints it right away.
- **Compose:** tap the keys or type note names into a part, add more parts for other instruments, and pick an arrangement (solo piano, music box, string quartet, chamber, organ, marimba and harp) or choose each part's instrument yourself. Your parts are kept in this browser between visits.

## Light and dark
- Fude follows your device's light or dark setting. The sun/moon button at the top (and in the companion) switches it; your choice is remembered, and switching back to what the device uses makes it follow the device again.

## Look and feel

Fude is dressed like a calm app: warm rice-paper tones (and a matching warm dark), soft rounded sections with plenty of room, a slow and gentle title shimmer, and a background where a few faint notes drift slowly upward.

**Zen mode** (on the opening screen, and the Zen button in the full-window view) plays the calm pieces in the library one after another, children's songs left out, and paints each as a different picture, masterpieces and quiet patterns in turn. Only the painting shows, with a breathing guide under it (four seconds in, a pause, then a long breath out) and the piece's name. The cat paints in silence. The controls (Stop or Play, Next piece, Breathing guide, Full screen, Leave) fade away when nothing moves and come back with a touch or a mouse move. After each piece the finished picture rests for a few breaths, then the next one begins. Space plays and stops, N moves to the next piece, and Escape leaves.

The page wears your twelve note colours: the Fude title shimmers in them, each section has a colour line and ring, and changing a colour changes them all. On the opening screen, three one-tap cards (Gymnopédie as The Starry Night, Für Elise as The Great Wave, Canon in D as Udnie) start a song and its painting straight away, and the painter cat waits by the intro with tips and can be petted. The menu ticks off each of the four steps as you do them, and a finished painting ends with a burst of paint in the song's colours.

The selected song sits in its own card with its title, composer, play buttons and settings. While a song plays on the page (from the library, your own music, or after closing the full window), its sheet music slides in at the side, with each note lighting up as it sounds and the page scrolling along; on phones it is a sheet above the bottom tabs. It has stop, full-window and hide buttons, and once hidden a small \"Sheet music\" tab on the edge brings it back. When the sheet music is hidden and you scroll away, a small "now playing" bar follows you down the page with the song's colours, its progress, a stop button and a way into the full window. On phones the mood chips scroll in one row, and the bar sits above the bottom navigation. Cards and buttons react when you hover or press them, sections rise gently into view (not when reduced motion is on), and the footer has a link back to the top.

## Published scores and the full-window view
- With **As written** chosen in the Arrangement menu (the default), 20 of the 54 library songs play from a published score, every part as printed: both piano hands, the four hymn voices, the string and orchestral parts. [published-scores.md](published-scores.md) lists each score, its source and licence, and the passage used. The other songs play Fude's own arrangement, and the note under the player says so.
- **Play and paint** opens a full-window view and starts the song. **Score and painting** opens the same view without starting. The view shows the sheet music on one side, engraved from exactly what plays, with each note lighting up as it sounds; the painting forms on the other side. On a phone the painting sits above the music. The painting starts as a blank white canvas and comes up through it as the music plays, redrawn every frame: a small cat in a beret lays down soft brushstrokes that reveal the picture, while the whole image slowly rises out of the white, and each new colour mix fades in over the last. The cat chats as it paints: it calls out the printed dynamics, says which note is leading and what colour that brings, notices chord changes and the tempo, and cheers at each quarter of the way. It glides with the brush, turns and leans into strokes, hops to each new patch, and gives a happy wave at the end. Loud passages paint darker and soft ones lighter. Paintings are drawn 1600 pixels across (1200 on phones), from the masterpieces' full-size scans, so saved images and posters stay sharp. Under the painting you can change the picture (even mid-song, and the next strokes paint the new one), pick a speed from half to one and a half times, switch the cat off, hold to see the original masterpiece, and save the picture. A thin line under the header shows how far through the song you are. Tap the cat to pet it; when the painting is done it sits in the corner instead of leaving. Space plays and stops, F goes full screen, and Escape closes. You can also switch the arrangement from the header.
- Sheet music is drawn by abcjs 6.4.4 (MIT licence), included in the page.

## Arrangements
- The player has an Arrangement menu: Melody only, Solo piano with both hands, Music box and harp, String quartet, Chamber, Organ with pedals, or Marimba and harp. Fude finds the key, meter (3/4, 4/4 or 6/8, with any pickup) and chords of the melody, including sevenths and the occasional secondary dominant, then writes the other parts in time with the tempo, which you can change next to it. Chords are voiced so the inner parts move as little as possible, the quartet and chamber styles get a counter-melody under the tune, and every performance opens with a two-bar introduction and closes on a held chord.
- Fude also finds the melody's phrases. Each phrase swells toward its middle and settles at its end, the tempo eases into phrase endings and the last bar, and the accompaniment takes a breath where the tune does. The left hand picks a style to suit the tune: a 6/8 lilt, a waltz bass, stride, block chords, tenths or Alberti figures. The note under the player names the key, the meter, the phrases and the left-hand style.
- Your own one-part melody gets the same treatment. A score you upload with several parts is played as written, and the arrangement only picks its instruments.

## Sound
- Piano, strings, flute and cello are real recorded notes (the FluidR3 General MIDI soundfont, CC BY 3.0, via MIDI.js soundfonts), a few per instrument, decoded once and pitched to every note. Harp, music box and marimba are synthesised note by note in a background worker and cached, and the organ is played live. If a sample set ever fails to decode, the synthesised piano stands in.
- Everything passes through a small hall reverb and a gentle compressor, and notes are nudged by a few milliseconds and a little velocity so arrangements breathe.

## Sharing, the gallery and posters
- **Share** copies a link (when Fude runs as its own site) or a code (inside Claude) that carries your colors, the song, the arrangement, the canvas and the exact picture. **Open a link or code** pastes one back. Links work for library songs and music you typed; uploaded scores and paintings you brought in stay on your computer.
- **Your gallery** keeps the last twelve paintings you made in this browser, under the caption. Click one to see it again, press Delete on it to remove it.
- **Save poster** downloads the painting with its title and the twelve-bar chart on one image. **Save A3 poster** lays the same out on an A3 sheet (2480 × 3508 px, 212 dpi) as a JPEG ready to print.
- **Shared gallery** (inside Claude only): under your own gallery, anyone who can post in the Claude page can post a painting with a short caption, and everyone who opens the page sees the posts, with the poster's name. Clicking a post opens that painting with its colors and arrangement; a poster can remove their own. People who open the page by a public link can look but not post. The standalone site has no shared gallery.

## The library and the first visit
- Every library melody, key, meter and tempo was checked against printed scores; `library-audit.md` lists each song's result and sources.
- The library has 54 public-domain songs, with chips for mood and kind (calm, bright, dance, children, hymns, classical and so on) and a search box. Searching for a song that is not there offers to look it up online.
- On a first visit a small card walks through the four movements; "Show me around" on the title replays it, and Escape or Skip closes it.

## Offline and installing
- The site has a manifest and a service worker, so once it has been opened over `https://` it works offline and can be installed from the browser menu ("Install Fude" or "Add to Home Screen").
- `preview.jpg` is the picture shown when the link is shared in chats and social sites. Some sites need an absolute address for it: once the site has its final address, change the `og:image` line near the top of `index.html` from `preview.jpg` to the full `https://…/preview.jpg`.
- Keep all the files in this folder together: `index.html`, `sw.js`, `manifest.webmanifest`, the icons and `preview.jpg`.

## Speed and phones
- Painting runs in a background worker, so the page and the intro never stall while a picture is computed. Phones get slightly smaller canvases and a lighter intro.
- On phones the movement nav (I to IV) becomes a bar at the bottom of the screen once you scroll past the intro.

## What only works inside Claude
Looking up songs and paintings with Claude, and Claude composing and titling new pieces, need the Claude viewer. On the standalone site those parts fall back to links and Fude's own composition, and everything else works the same.

## Privacy and fonts
`privacy.html` is Fude's privacy policy. Once the site is online, its address (for example `https://your-site.netlify.app/privacy.html`) is the privacy policy URL the app stores ask for. The ⋯ menu on Now has **About and privacy**, which links to it.
The fonts are in `fonts/`, so the site makes no requests to Google and looks right offline. Upload the whole folder, including `fonts/` and `privacy.html`.

