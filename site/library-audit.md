# Fude library audit

Every library melody was compared with a printed score where one could be reached, and every tempo with the composer's own metronome mark, the tempo word in the score, or, for folk songs, hymns and children's songs, a conventional singing tempo (these have no official tempo). Tempos are quarter notes per minute; for 6/8 the dotted-quarter beat is two thirds of that, and for 2/2 the half-note beat is half.

| Song | Result | Key | Meter | Tempo | Where the tempo comes from | What changed |
|---|---|---|---|---|---|---|
| Sakura Sakura | Already right | A minor | 4/4 | 76 | Conventional (folk song, no official tempo); matches the 76 BPM of the flutetunes.com Sakura Sakura edition | Nothing |
| Gymnopédie No. 1 | Corrected | D major | 3/4 | 72 | Satie: 'Lent et douloureux' (no metronome mark); typical recordings run about quarter = 66-78, so 72 (was 84, on the fast side). | Bars 5-31 rhythm and most pitches confirmed, but three octave marks in the .ly were misread before: 'e,2.' is E4 (not E5), 'a c, d e d b d' is A5 C5 D5 E5 D5 B4 D5 (not C6 D6 E6 D6 B5 D6) and the first-ending close 'fis,2.' is F#4 (not F#5). Tied notes are merged (F#4:12, E4:9, D5:5), so those segments span several bars. |
| Ode to Joy | Corrected | D major | 4/4 | 160 | Beethoven's own mark for the finale theme: Allegro assai, half note = 80 -> 160 quarter bpm (Wikipedia Symphony No. 9 and Anthem of Europe pages both cite minim = 80). Was 108. | Pitches were right, but bar 12 lacked Beethoven's syncopation: the last phrase's first F# enters on beat 4 of bar 12 and is tied over the bar (D E A3 F#~ / F# F# G A), instead of D E A3:2. Tempo raised from 108 to Beethoven's half = 80. The bar-12 segment holds two bars (8 beats) because of the tie. |
| Für Elise | Corrected | A minor | 3/8 | 72 | Beethoven: 'Poco moto' (no metronome mark); the Mutopia edition's MIDI tempo is quarter = 72, which matches typical recordings (about 66-76). | Pitches were right but every value was doubled: the piece is in 3/8 with sixteenth notes (.25), not eighths, and the eighth rests after A4/B4/C5 were folded into the notes. Now uses the printed sixteenths, eighths and rests, with the 1st-ending A4 quarter at the end. At the same bpm it now plays at the correct speed instead of half speed. |
| Greensleeves | Already right | A minor | 3/4 | 96 | Conventional (folk song, no official tempo); a moderate 3/4 at about 96 | Nothing |
| Amazing Grace | Corrected | C major | 3/4 | 80 | Hymnals give no metronome mark; 80 is a conventional congregational tempo for New Britain in 3/4. The hymnwiki .ly sets MIDI playback at 90. | Pitches and rhythms match the hymnwiki soprano exactly. Only the final note changes, from 3 beats to 2 as printed. In that file 'me' is a plain dotted half with no extra hold, so the bar lines in the second half fall where the file puts them. C major is kept. |
| Canon in D | Corrected | D major | 4/4 | 56 | No tempo mark from Pachelbel; Wikipedia's engraved score sets quarter = 56, mid-range of standard recordings (about 46-76 depending on style). | The pitches were right, but every value was doubled (halves/quarters). In Pachelbel's score the ground bass is in quarter notes (2 bars per statement), so Violin I's first variations are quarters and the third is eighths. bpm is now set for quarter notes (56). |
| Twinkle, Twinkle | Already right | C major | 4/4 | 100 | conventional singing tempo (no official tempo); the Musica Viva ABC marks Q:120, so 100-120 is typical | Nothing |
| Lullaby (Wiegenlied) | Corrected | Eb major | 3/4 | 84 | Brahms: 'Zart bewegt' (no metronome mark); 84 is within the range of typical recordings (about quarter = 72-88), so it is unchanged. | Bars 1-2 had the wrong rhythm: the score is Bb4 dotted quarter, G4 eighth, G4 quarter / Bb4 quarter, quarter rest, then G4 Bb4 eighths. The src had Bb4:2 G4:.5 G4:.5 and folded the rests into the notes. Printed rests are restored after Bb4, Ab4 and the final Eb5. |
| Silent Night | Corrected | C major | 6/8 | 72 | No hymnal metronome mark. A conventional gentle carol tempo of dotted quarter = 48 gives quarter = 72. | The old src was written at double values, a 6/4-style bar of 6, at bpm 90, which plays very slowly. It is now in real 6/8 values: dotted eighth, sixteenth, eighth, dotted quarter. It also used to stop mid-verse on E4 (bar 6). It now runs to the end of the 12-bar verse on the tonic. C major is kept; Gruber's original is in D and hymnwiki has Bb. |
| Jingle Bells | Corrected | C major | 4/4 | 132 | Conventional: no official tempo for the popular chorus; 132 is a typical lively singing tempo. The cited ABC has Q:200, which is too fast to sing. | The first 8 bars were already correct note for note. The old src stopped on the half cadence (D-G). The second half of the chorus is added so the line ends on the tonic C. |
| Happy Birthday | Already right | C major | 3/4 | 100 | conventional singing tempo (no official tempo) | Nothing |
| Auld Lang Syne | Already right | F major | 4/4 | 84 | Conventional: folk song, no official tempo; 84 is a typical moderate singing tempo. | Nothing |
| Morning Mood | Not checkable | E major | 6/8 | 84 | Allegretto pastorale (Wikipedia); the flutetunes.com edition prints an editorial (dotted quarter = 58) and lists 60; typical recordings open around dotted quarter = 52-60. Dotted quarter = 56 -> 84 quarter bpm. | The old src was in quarters (should be 6/8 eighths) and used G# E D# C#, which is not pentatonic. It looks like a mis-transposition of the well-known sol-mi-re-do-re-mi figure. My best reconstruction is the flute's 4-bar phrase B G# F# E F# G# / B G# F# E F#G#F#G# (sixteenths) / B G# B C# G# C# / B G# F# E. Pitches and octave still need checking against a real score. |
| In the Hall of the Mountain King | Corrected | B minor | 4/4 | 138 | Grieg's mark: 'Alla marcia e molto marcato', quarter = 138 (in Mutopia's edition of Grieg's own piano arrangement; it later accelerates to Piu vivo 154 and beyond). | Notes and rhythm match, except the score spells the raised note in bar 2 as E#4 ('eis'), not F4. Tempo raised from 120 to Grieg's quarter = 138. The register is kept an octave above the score, where the theme sits around B1-B2 (bassoons, low strings). |
| Eine kleine Nachtmusik | Corrected | G major | 4/4 | 136 | Mozart: Allegro (no metronome mark); standard recordings take quarter = about 130-144, so 136 (was 120). | The rhythm was wrong: the score is G quarter, eighth rest, D eighth (not D eighth then rest), and bars 2 and 4 end with a quarter note plus a quarter rest (not a half note). It is now in Violin I's written octave (G5, up to D6); the old src was an octave lower. |
| Spring | Corrected | E major | 4/4 | 100 | Vivaldi: Allegro (no metronome mark); typical recordings take quarter = about 96-112, so 100 is unchanged. | Badly off before: the eighth pickup was missing, the motif was quarter/eighth instead of 3 eighths + 2 sixteenths, the B5 was a dotted half instead of dotted quarter + B A sixteenths, and the closing bar (G# A B A G# F# D# B E) was missing. Now the opening ritornello statement is exact (pickup + bars 1-3). |
| Swan Lake | Not checkable | B minor | 4/4 | 76 | Act 2 No. 10 Scene: Moderato. I could not confirm a composer metronome mark; 76 is within typical recordings (about quarter = 66-80), so it is unchanged. | The old src was in the wrong key (E minor contour) with mixed-up rhythms. Moved to B minor as the oboe theme: long F#5, quick B C# D E eighths, three dotted figures F#.D F#.D F#.B, then D B G D eighths to B4. Rhythm was inferred from consistent letter-note spacing (2 dashes = eighth), so verify against a score; the opening F#5 length (half) is the least certain. |
| Moonlight Sonata | Corrected | C# minor | 2/2 | 56 | Beethoven: Adagio sostenuto, alla breve, no metronome mark; standard recordings run about quarter = 50-60 (half = 25-30), so 56 is unchanged. | The dotted rhythm was missing: the melody enters on beat 4 with G#4 dotted-eighth + sixteenth, then G#4 dotted half + dotted-eighth/sixteenth, G#4 half A4 half, G#4 half F#4 B4 quarters, resolving to E4 (bar 9). The old src used 3- and 2-beat values throughout and ended on a 3-beat E4. |
| Londonderry Air | Corrected | C major | 4/4 | 66 | Conventional slow singing tempo for Danny Boy (folk air, no official tempo). The cited ABC marks Q:1/4=80; sung versions are usually slower. | Confirmed that this was rebuilt from tunearch Derry Air. Fixed two bars: in bars 8 and 10 the ABC ties the long note (G4- G, G2- G), but the src re-struck it as an extra C4:.5, so those bars added up to 4.5 beats. Removed the extra notes. The last note is now 2.5 beats (G4- G), which balances the 1.5-beat pickup. |
| Scarborough Fair | Corrected | D minor | 3/4 | 96 | Conventional (folk song, no official tempo); moderate 3/4 near the usual singing pace | Two fixes in the first two phrases (same span as before). Bar 2 now has three notes (A A A) where it had two; both ABCs give three notes there, so one syllable was missing. Bars 5-6 now begin with a rest, then A C / D(half) C, as in Carthy, replacing A C(half) / D C(half). The tune is D Dorian (B natural), notated with a D minor signature. |
| Arirang | Not checkable | C major | 3/4 | 80 | Conventional; flutetunes.com Arirang edition is 3/4 at 80 BPM and Hooktheory lists 3/4 at 81 BPM | No change, unverified. The meter (3/4), pentatonic pitch set (G A C D E), and low-sol to high-sol range match every source reached. Bars 1-4 match the usual Bonjo Arirang reading (sol la sol / do re do / re mi re mi / sol mi re do la). The final C5:3 is a constructed close: in the song, bar 5 continues with do re do. The hymnary incipit (a hymnal arrangement) adds passing notes in bars 1-2, which I could not check against a score. |
| Frère Jacques | Already right | C major | 4/4 | 108 | Conventional (children's round, no official tempo) | Nothing |
| William Tell Overture | Not checkable | E major | 2/4 | 152 | Finale marked 'Allegro vivace, quarter = 152' in 2/4 (flutetunes edition of the finale, PDF text). | The meter was 4/4 with doubled values; it is now 2/4 with real values (sixteenth-sixteenth-eighth gallop). The old pitches started the theme on E and rose A-B-C#, which is do-re-mi of A major, not of the E major the line declares. Every scored source has the repeated note on the dominant, rising do-re-mi to the tonic, so the theme is now on B rising E-F#-G#. Mutopia has no Rossini Tell, and I could not read a note-level score of the original. The second phrase (B B B B E G# / E B) is the old shape transposed and is unconfirmed; the Barwell arrangement has 'do mi re ti sol' there instead. |
| Yankee Doodle | Already right | C major | 2/4 | 112 | Conventional march tempo (folk song, no official tempo) | Nothing |
| Oh! Susanna | Corrected | C major | 2/4 | 116 | Conventional (no metronome mark in the source); about 116 per quarter in 2/4, the usual lively singing pace | The old src was written at double note values in 4/4. At 116 BPM that made the song half speed, and its bar 3 was E E D D:4 (7 beats). Rewrote it at the score's real 2/4 values, so the same BPM now gives the normal pace. Pitch fixes: the first line ends E E D C / D (not E E D D). "Al-a-ba-ma" is straight eighths. The chorus opens F F / A A(syncopated) A / G G E C / D, as in the source. |
| Oh My Darling, Clementine | Not checkable | C major | 3/4 | 100 | Conventional waltz tempo; the flutetunes.com edition (Percy Montrose) is 3/4 at 100 BPM and the Yamaha PSR-E283 songbook has a quarter note at 104 ("Country Waltz") | No change. Checked as asked: 3/4 is right (both editions use waltz time), and C major is a valid choice (flutetunes uses G). Every bar adds up to 3 after a 1-beat pickup, ending on C4:3. The pitches are the standard tune (C C / C G E E / E C C E / G G F E / D ...). No printed score was read to confirm the dotted-quarter/eighth rhythm note by note. |
| Aura Lee | Not checkable | C major | 4/4 | 88 | Yamaha PSR-E283 songbook, Aura Lee: quarter = 88 (no mark in Poulton 1861) | No change to the notes. These are the standard first two phrases in C (the same tune as "Love Me Tender"). Tempo changed from 84 to 88 to match the Yamaha songbook mark. |
| When the Saints Go Marching In | Corrected | C major | 4/4 | 120 | Conventional lively singing tempo (traditional, no official tempo; the Yamaha songbook plays it at 96 in a 2/4 style) | The old src had broken durations (G4:5 notes, D4:5, a stray G4:.5 and F4:2.5), so no bar added up. Rebuilt it as the standard 16-bar lead sheet: pickup C E F, held G, then the "Oh Lord I want to be in that number" line (E E D / C. C / E G G / F / F E F G / E C / D / C). Long notes are followed by rests, not ties across the bar line. The pitches are the standard tune, but there was no note-level score to check them against. |
| Mary Had a Little Lamb | Already right | C major | 4/4 | 104 | conventional singing tempo (no official tempo) | Nothing |
| Hot Cross Buns | Already right | C major | 4/4 | 100 | conventional singing tempo (no official tempo) | Nothing |
| London Bridge Is Falling Down | Already right | C major | 4/4 | 108 | conventional singing tempo (no official tempo) | Nothing |
| Row, Row, Row Your Boat | Corrected | C major | 6/8 | 96 | conventional singing tempo (no official tempo): dotted quarter = 64, i.e. quarter = 96 | The old src used simple-meter quarters for the opening (C C C D E…), not the 6/8 rhythm. Rewritten in true 6/8: two dotted-quarter Cs, then quarter-eighth patterns, a dotted-half G, triplet-feel eighths on the descent and a dotted-half final C. |
| Old MacDonald Had a Farm | Already right | G major | 4/4 | 112 | conventional singing tempo (no official tempo) | Nothing |
| Three Blind Mice | Corrected | C major | 6/8 | 108 | conventional singing tempo: dotted quarter = 72 (quarter 108), matching the 'Moderately quick' heading of the 1904 Ivimey printing on Project Gutenberg | The old src used simple-meter values (E D C:2, eighth runs) with no 6/8 grouping. Rewritten in true 6/8 from the score: dotted-quarter openings, a tied E with a G pickup, the C-C-BAB/C-G-G running bars with their quarter-eighth patterns, and the closing E D C. |
| Baa, Baa, Black Sheep | Already right | C major | 4/4 | 100 | conventional singing tempo (no official tempo) | Nothing |
| This Old Man | Corrected | C major | 2/4 | 112 | conventional singing tempo (no official tempo); quarter = 112 in 2/4 with eighth-note syllables | Bars 4 and 6 did not add up. Bar 4 held F as a long note plus two extra beats, and the G closing bar 6 was cut short. Rewritten in true 2/4 values from the score: D-E-F then E-F sixteenths, then G-C-C-C / C-D-E-F sixteenths to a quarter G. Bpm raised from 108 to 112 to suit the real (halved) note values. |
| Pop Goes the Weasel | Corrected | C major | 6/8 | 120 | conventional singing/dance tempo (no official tempo): dotted quarter = 80, i.e. quarter = 120 | The old src had no eighth-note pickups (the score has G before bar 1 and at the ends of bars 2 and 4), and bar 3 ended D-D where the score has D-F. Bars 2 and 4 now end with quarter + pickup eighth instead of a dotted quarter. Written an octave below the DT file to keep the old range. Note: some English manuscripts on tunearch (Watson, Barry) do have D-D in bar 3 with no pickups. |
| Lightly Row (Hänschen klein) | Corrected | C major | 4/4 | 100 | conventional singing tempo (no official tempo) | The pitches were right, but the 1927 score ends both phrases (bars 8 and 16) with a note followed by a rest. The old src held a whole-note E instead. Values are doubled from the 2/4 printing into the familiar 4/4 (Suzuki-style) form. Kept in C (source is in G). |
| Au clair de la lune | Already right | C major | 4/4 | 92 | Conventional Moderato; the Widor edition is marked Moderato in common time | Nothing |
| La Cucaracha | Corrected | F major | 4/4 | 200 | Conventional lively tempo; the flutetunes.com La Cucaracha edition is 4/4 at 200 BPM | Rebuilt in 2/4 at its usual note values; the rhythm could not be checked against a printed score. |
| Korobeiniki | Not checkable | A minor | 4/4 | 140 | Conventional; the flutetunes.com edition (Tetris Theme A / Korobeiniki) is 4/4 at 144 BPM | No change, unverified. The 8 bars are the standard A-section (as in Tetris Theme A), they add up to 4/4, and the key matches flutetunes. Only the PDF/MIDI on flutetunes holds the notes, and it could not be read. |
| God Save the King | Corrected | G major | 3/4 | 60 | Wikipedia: 'The official tempo for the opening section is a metronome setting of 60', with the second part broader at 52. 60 is used here. | Notes and rhythms already matched the Cooke manuscript, including E-C-B-A in the second-to-last bar. Only the tempo changes, from 76 to the official 60. |
| Joy to the World | Corrected | C major | 2/4 | 100 | Hymnals give no metronome mark; 100 is a conventional congregational tempo for Antioch in 2/4. The hymnwiki .ly sets MIDI playback at 56, which is far slower than it is sung. | The last round's correction still did not match the score. The opening was C5 dotted quarter, B eighth, A quarter instead of C5 quarter, B dotted eighth, A sixteenth. An extra rest and an extra C5 had been added in bars 7-8, and an extra D4 eighth in bar 14. All bars now add up to 2/4. C major is kept. |
| We Wish You a Merry Christmas | Corrected | G major | 3/4 | 120 | Conventional: folk carol, no official tempo; 120 is a typical brisk singing tempo. | Bar 2 was E E E; all three sources give E C E. Bar 4 was F# D D; two sources give F# D F#. Everything else matched. |
| O Tannenbaum | Corrected | F major | 3/4 | 92 | Conventional: folk carol, no official tempo; 92 is a typical moderate singing tempo. | Rhythms in bars 1, 3, 4, 5-8 and 9 did not match the score. Bar 1 is F dotted-eighth, F sixteenth, F quarter, G quarter. 'treu sind deine' is G dotted-eighth, A sixteenth, Bb quarter, E quarter, not G A Bb dotted, E eighth. The phrase ends F F quarter, eighth rest, C eighth. Dotted-eighth/sixteenth pairs replace the plain eighth pairs in the middle section. Many German songbooks print 'baum, o' as F dotted quarter, G eighth; this score has two quarters. |
| Good King Wenceslas | Corrected | F major | 4/4 | 108 | Conventional: no hymnal metronome mark; 108 is a typical brisk carol tempo. The Mutopia file's MIDI tempo is 120. | The last two bars were F F half notes, but the score ends F half, Bb half, then F whole. Bars 1-15 were already correct. F major is kept. |
| The First Noel | Corrected | D major | 3/4 | 96 | Conventional: no hymnal metronome mark; 96 is a typical congregational tempo in 3/4. | Bar 3 of each half was D5 half, C#5 eighth, B4 eighth; the score has three quarters, D5 C#5 B4. Everything else matched. The passage is the full verse, two identical halves, ending on F#4 before the Noel refrain. |
| O Come, All Ye Faithful | Corrected | G major | 4/4 | 96 | Conventional: no hymnal metronome mark; 96 is a typical congregational tempo. The Mutopia MIDI uses 55, which is slow. | The quarter-note pickup was missing: the old src opened with G4 half, G4 quarter. The end of the phrase was garbled (F# G A F# E D dotted half) and now matches both Mutopia scores: F# G A B / F# half, E dotted quarter, D eighth / D whole. 4/4 and G major are confirmed. |
| Minuet in G major | Already right | G major | 3/4 | 112 | No tempo word or mark in the source; minuet tempo in typical recordings is about quarter = 104-132 (Mutopia's MIDI uses 140), so 112 is kept. | Nothing |
| Prelude in C major | Corrected | C major | 4/4 | 72 | No mark from Bach; Mutopia's edition sets quarter = 60, and standard recordings run about 60-76, so 72 is kept. | Every note was an eighth, but the figure is in sixteenths (.25), so bars were twice as long. Bar 5's second half was wrong (E4 A4 E5 -> A4 E5 A5), and so was bar 7's (D4 G4 D5 -> G4 D5 G5). Each bar is two identical 8-note groups. |
| Symphony No. 5, opening | Corrected | C minor | 2/4 | 216 | Beethoven's own mark: Allegro con brio, half note = 108 (one bar of 2/4 per beat) -> 216 quarter bpm. Was 120. | The meter is 2/4, not 4/4. The second motto's D4 is tied over two bars (4 beats, fermata), and the old src's extra rests and 1-beat Eb4 made bars that do not add up. Bars 6-10 are now the real imitative entries as one line: Violin II (r G G G / Eb), viola (Ab Ab Ab / G), Violin I (Eb5 Eb5 Eb5 / C5 tied to bar 10). The fermatas on Eb4 and D4 cannot be shown and are kept at their written lengths. |
| Also sprach Zarathustra, sunrise | Not checkable | C major | 4/4 | 69 | Strauss marks only 'Sehr breit' (no metronome). Two published arrangements of the opening (8notes trumpet, flutetunes flute/organ) print 4/4, C major, quarter = 69. | Could not read a score of bars 5-8 (scores are images/PDF only), so pitches (C-G-C, then E/Eb, then Eb/E) are left as they were. The order of the thirds matches Wikipedia's account. Note lengths cross the 4/4 bar lines and are not checked against the score. 4/4 and C major are confirmed by two arrangements. bpm changed from 72 to 69 to match them. |
| The Entertainer | Corrected | C major | 2/4 | 72 | Joplin marks only 'Not fast' (no metronome). 72 is the quarter-note tempo in the Mutopia edition's MIDI block (copied from the 1902 edition) and is typical of 'not fast' ragtime performances. | The old src used doubled values (eighths for sixteenths) at bpm 88, and the two tied C5s were too short. It is now in real 2/4 values, sixteenth = .25, from the first strain (bars 5-12 plus pickup), with tempo 72. Two C5s are tied across a bar line (1.5 and 1.75 beats). Each is written as one note in the bar where it starts, so checkbars shows bars 2/3 and 6/7 as 3.25/.75 and 3.5/.5. Each pair adds up to 4 beats, which is two correct 2/4 bars. |

## Sources read

- http://trillian.mit.edu/~jc/music/abc/mirror/musicaviva.com/tunes/england/mary-had-a-little-lamb-g.abc
- https://abcnotation.com/tunePage?a=abc.sourceforge.net%2FNMD%2Fnmd%2Freelsu-z.txt%2F0023
- https://abcnotation.com/tunePage?a=pghardy.net%2Ftunebooks%2Fpgh_songs_tunebook%2F0001
- https://abcnotation.com/tunePage?a=www.joe-offer.com%2Ffolkinfo%2Fsongs%2Fabc%2F565%2F0000
- https://data.yamaha.com/files/download/other_assets/3/2232933/psr_e283_en_songbook_a0.pdf
- https://en.wikibooks.org/wiki/Songbook/Oh_My_Darling_Clementine
- https://en.wikipedia.org/wiki/Also_sprach_Zarathustra_(Strauss)
- https://en.wikipedia.org/wiki/God_Save_the_King
- https://en.wikipedia.org/wiki/Korobeiniki
- https://en.wikipedia.org/wiki/Morning_Mood
- https://en.wikipedia.org/wiki/Pachelbel%27s_Canon
- https://en.wikipedia.org/wiki/Sakura_Sakura
- https://englishtap.com/music/abc-notation-files/abc-carol-we-wish-you-a-merry-christmas.abc
- https://folkinfo.mainlynorfolk.info/songs/208.html
- https://folkinfo.mainlynorfolk.info/songs/21.html
- https://folkinfo.mainlynorfolk.info/songs/abc/208.abc
- https://folkinfo.mainlynorfolk.info/songs/abc/21.abc
- https://folkinfo.mainlynorfolk.info/songs/abc/683.abc
- https://gutenberg.org/cache/epub/26060/pg26060-images.html
- https://hymnary.org/media/fetch/131107
- https://hymnary.org/media/fetch/133267
- https://hymnary.org/tune/arirang
- https://hymnary.org/tune/o_tannenbaum_german
- https://imslp.org/wiki/Aura_Lea_(Poulton%2C_George_R.)
- https://imslp.org/wiki/Korobeiniki_(Folk_Songs
- https://new.folktunefinder.com/tunes/157996
- https://new.folktunefinder.com/tunes/4110
- https://pages.cpsc.ucalgary.ca/~bdstephe/217_F26/jingle_bells_with_lyrics.abc
- https://pianoandsynth.com/we-wish-you-a-merry-christmas/
- https://pianochord.org/play-by-ear/when-the-saints-go-marching-in.html
- https://pianoletternotes.blogspot.com/2017/10/swan-lake-op-20-by-tchaikovsky.html
- https://raw.githubusercontent.com/baobach/abc_search/main/database/abc/QmabT81EESkyapBMoApv2Uc68pJp8996ANQLQRB189fc8D.abc
- https://raw.githubusercontent.com/oriolcolomefont/The-Sound-of-AI-workshop/main/wikifonia-dataset/original-abc/traditionalnurserysongOldMacDonaldHadaFarm.abc
- https://raw.githubusercontent.com/syntithenai/abc2book/master/abcresources/folkinfo/abc_tune_folkinfo_1650.abc
- https://raw.githubusercontent.com/syntithenai/abc2book/master/abcresources/folktunefinder/abc_tune_folktunefinder_174580.txt
- https://raw.githubusercontent.com/syntithenai/abc2book/master/abcresources/jc/abc_tune_jc_201218952.abc
- https://raw.githubusercontent.com/syntithenai/abc2book/master/abcresources/jc/abc_tune_jc_201225562.abc
- https://raw.githubusercontent.com/syntithenai/abc2book/master/abcresources/jc/abc_tune_jc_201273539.abc
- https://raw.githubusercontent.com/syntithenai/abc2book/master/abcresources/jc/abc_tune_jc_201294348.abc
- https://raw.githubusercontent.com/syntithenai/abc2book/master/abcresources/jc/abc_tune_jc_201307679.abc
- https://raw.githubusercontent.com/syntithenai/abc2book/master/abcresources/robinson/abc_tune_robinson_12682.abc
- https://raw.githubusercontent.com/syntithenai/abc2book/master/scrape/kids%20songs.abc
- https://raw.githubusercontent.com/yetist/music-score/master/abc/abc_dtrad/ROWROWBT.abc
- https://raw.githubusercontent.com/yetist/music-score/master/abc/abc_dtrad/THREEBLN.abc
- https://raw.githubusercontent.com/yetist/music-score/master/abc/abc_dtrad/WEASLPOP.abc
- https://sejongculturalsociety.org/composition/current/music/arirang.php
- https://trillian.mit.edu/~jc/music/abc/mirror/musicaviva.com/england/row-row-c/row-row-c-c24.abc
- https://trillian.mit.edu/~jc/music/abc/mirror/musicaviva.com/france/ah-vous-c/ah-vous-c-1.abc
- https://tunearch.org/wiki/Annotation:Yankee_Doodle_Dandy
- https://tunearch.org/wiki/Auld_Lang_Syne_(2)
- https://tunearch.org/wiki/Derry_Air
- https://tunearch.org/wiki/O!_Susanna
- https://tunearch.org/wiki/Pop_Goes_the_Weasel
- https://www.8notes.com/scores/16622.asp
- https://www.bethsnotesplus.com/2012/03/la-cucaracha.html
- https://www.chiffandfipple.com/t/abc-conversion/54659
- https://www.flutetunes.com/tunes.php?id=120
- https://www.flutetunes.com/tunes.php?id=148
- https://www.flutetunes.com/tunes.php?id=164
- https://www.flutetunes.com/tunes.php?id=192
- https://www.flutetunes.com/tunes.php?id=21
- https://www.flutetunes.com/tunes.php?id=228
- https://www.flutetunes.com/tunes.php?id=27
- https://www.flutetunes.com/tunes.php?id=305
- https://www.flutetunes.com/tunes.php?id=337
- https://www.flutetunes.com/tunes/rossini-william-tell-overture.pdf
- https://www.gutenberg.org/cache/epub/42711/music/006auclair.pdf
- https://www.gutenberg.org/cache/epub/42711/music/018-019frerejacques.pdf
- https://www.gutenberg.org/cache/epub/42711/pg42711-images.html
- https://www.hooktheory.com/theorytab/view/korean-traditional/arirang
- https://www.hymnwiki.org/Amazing_Grace
- https://www.hymnwiki.org/Joy_to_the_World
- https://www.hymnwiki.org/Silent_Night
- https://www.hymnwiki.org/wiki/images/2/22/082_Silent_Night.ly
- https://www.hymnwiki.org/wiki/images/2/2c/Amazing_Grace.ly
- https://www.hymnwiki.org/wiki/images/c/ca/188_Joy_to_the_World.ly
- https://www.ibiblio.org/mutopia/cgibin/piece-info.cgi?id=109
- https://www.ibiblio.org/mutopia/cgibin/piece-info.cgi?id=263
- https://www.ibiblio.org/mutopia/ftp/BachJS/BWV846/wtk1-prelude1/wtk1-prelude1.ly
- https://www.ibiblio.org/mutopia/ftp/BeethovenLv/WoO59/fur_Elise_WoO59/fur_Elise_WoO59.ly
- https://www.ibiblio.org/mutopia/ftp/JoplinS/entertainer/entertainer.ly
- https://www.ibiblio.org/mutopia/ftp/SatieE/gymnopedie_1/gymnopedie_1.ly
- https://www.ibiblio.org/mutopia/ftp/WadeJF/adeste/adeste.ly
- https://www.mit.edu/~jcb/Red_Herring/dances/ode-to-joy-tune.shtml
- https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=1265
- https://www.mutopiaproject.org/ftp/Anonymous/GoodKingWenceslas/GoodKingWenceslas.ly
- https://www.mutopiaproject.org/ftp/BachJS/BWVAnh114/anna-magdalena-04/anna-magdalena-04.ly
- https://www.mutopiaproject.org/ftp/BeethovenLv/O27/moonlight/moonlight-lys/moonlight1-a4.ly
- https://www.mutopiaproject.org/ftp/BeethovenLv/O67/Symphony5_1/Symphony5_1-lys/violinoone.ly
- https://www.mutopiaproject.org/ftp/BeethovenLv/ode/ode.ly
- https://www.mutopiaproject.org/ftp/BrahmsJ/O49/Wiegenlied/Wiegenlied-lys/Wiegenlied.ly
- https://www.mutopiaproject.org/ftp/GriegE/O46/Dans_l_antre_du_roi_de_la_montagne/Dans_l_antre_du_roi_de_la_montagne.ly
- https://www.mutopiaproject.org/ftp/MozartWA/KV525/eine-kleine-nachtmusik-mvt1/eine-kleine-nachtmusik-mvt1-lys/violin1.ly
- https://www.mutopiaproject.org/ftp/Traditional/GreensleevesAcc/GreensleevesAcc.ly
- https://www.mutopiaproject.org/ftp/VivaldiA/O8/spring/spring-lys/spring1.ly
- https://www.mutopiaproject.org/ftp/WadeJF/adeste_fideles/adeste_fideles.ly
- https://www.singing-bell.com/au-clair-de-la-lune-glockenspiel-xylophone-note-chart-sheet-music/
- https://www.singing-bell.com/la-cucaracha/
