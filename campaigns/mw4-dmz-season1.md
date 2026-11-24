# MW4 DMZ Intel Briefing — Season 1 clipping campaign

Source: `Season 1 DMZ Intel Briefing XO1.mp4` — 00:01:03.98, 3840x2160, 60 fps, 30 Mb/s.
Platforms: TikTok + Instagram Reels. Footage must come only from the official content folder.

## Timeline from the contact sheet

| Time | Content |
| --- | --- |
| 0:00–0:03 | "SEASON 1 INTEL BRIEFING" title card |
| 0:04–0:07 | Tactical map, orange thermal overlay with UI markers |
| 0:08–0:15 | Snowy street, squad walking into mist ("GAME ENGINE FOOTAGE") |
| 0:16–0:22 | Interior warehouse, fluorescent lights, machinery, crates |
| 0:23–0:30 | Hangar/setup shot, two operators with rifles |
| 0:33–0:38 | Red laser beams crossing a gold-lit structure |
| 0:39–0:45 | Teal laser corridor, operator silhouette in doorway |
| 0:44–0:47 | Neon market alley, Korean signage, red/pink light |
| 0:48–0:55 | Close-quarters takedown, two operators |
| 0:56–0:59 | Hooded masked operator close-up |
| 1:00–1:04 | End card: "SEASON 1 · NOVEMBER 6" + press quotes |

## Four clips to cut

| # | Window | What it shows | Hook text (on screen) |
| --- | --- | --- | --- |
| 1 | 00:03–00:15 | Map reveal → snowy squad | NEW DMZ MAP |
| 2 | 00:16–00:30 | Warehouse → hangar | NEW LOCATIONS |
| 3 | 00:33–00:45 | Red lasers → teal corridor → neon | LOOK AT THIS |
| 4 | 00:48–01:02 | Close combat → end card | WAIT FOR IT |

## Captions (original, compliant)

1. `This is the new DMZ map and it is huge @callofduty #Ad`
2. `New DMZ locations in MW4 Season 1 @callofduty #Ad`
3. `The lighting in new DMZ is unreal @callofduty #Ad`
4. `Close quarters in DMZ hits different now @callofduty #Ad`

Every caption carries the required tag and the `#Ad` disclosure. Do not invent
stats, dates, or weapon names.

## Export (PowerShell, from the folder holding the mp4)

```powershell
$src = "Season 1 DMZ Intel Briefing XO1.mp4"
$cuts = @(
  @{n=1; ss="00:00:03"; to="00:00:15"},
  @{n=2; ss="00:00:16"; to="00:00:30"},
  @{n=3; ss="00:00:33"; to="00:00:45"},
  @{n=4; ss="00:00:48"; to="00:01:02"}
)
foreach ($c in $cuts) {
  ffmpeg -ss $c.ss -to $c.to -i $src `
    -vf "crop=ih*9/16:ih,scale=1080:1920,setsar=1" `
    -c:v libx264 -preset medium -crf 20 -r 30 -c:a aac -b:a 192k `
    "clip$($c.n).mp4"
}
```

`crop=ih*9/16:ih` centre-crops 16:9 to 9:16. If a shot loses its subject, shift
the crop window with `crop=ih*9/16:ih:x:0` (x in pixels, negative allowed), or
keep the full frame on a blurred pad instead:

```powershell
-vf "scale=1080:-2,boxblur=20:5,pad=1080:1920:0:(oh-ih)/2,scale=1080:1920"
```

## Stills

`MW4_S1_DMZ_001_R06.png`, `MW4_S1_DMZ_002.png`, `MW4_S1_DMZ_002_R08.png` can be
cut as a 3-image slideshow with a slow zoom, or used as the first 2 seconds of a
video clip as a pattern interrupt.

## Submission checklist

- [ ] Footage only from the official content folder
- [ ] `@callofduty` tagged on TikTok **and** Instagram
- [ ] `#Ad` present
- [ ] Caption original and matching the clip
- [ ] 9:16, audio audible, no third-party watermarks
- [ ] Submitted separately to each platform
- [ ] Checked that Nigerian views are paid (not in the excluded country list)
