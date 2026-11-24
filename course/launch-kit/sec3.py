from _pdfkit import *   # noqa
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
PW = A4[0] - 40 * mm

def build(story, doc):
    # ------------------------------------------------ PART 3
    story.append(PageBreak())
    story.append(Spacer(1, 40 * mm))
    story.append(P("PART THREE", S("p3d", fontName="DJB", fontSize=9, leading=12, textColor=ACCENT)))
    story.append(Spacer(1, 4 * mm))
    story.append(P("Cut a clip that<br/>survives a phone", S("p3t", fontName="DJB", fontSize=27, leading=33, textColor=INK)))
    story.append(Spacer(1, 7 * mm))
    story.append(Rule(thickness=1.4, color=ACCENT, space=12))
    story.append(P("The editing here is deliberately simple. You need one skill that separates "
                   "a clip people watch from a clip people swipe: what happens in the first two "
                   "seconds, on a screen the size of a palm.",
                   S("p3s", fontSize=11, leading=16.5)))
    story.append(PageBreak())

    # ------------------------------------------------ 3.1
    story.append(SetSection(doc, "Part 3 \u00b7 Cutting the clip"))
    story.append(Mark(doc, "c3.1"))
    story += h1("Chapter 3.1", "The vertical crop")
    story.append(P("Everything you post should be 1080 \u00d7 1920 \u2014 nine by sixteen. "
                   "Campaign footage usually arrives in 16:9 landscape, which means most of the "
                   "frame is outside the phone screen. Three ways to handle that, in order of "
                   "how often you should use them."))
    story.append(P("1. Centre crop (default)", st_h3))
    story.append(P("Take the middle vertical slice. Correct whenever the subject is near the "
                   "centre, which is how most game and product footage is composed."))
    story.append(Spacer(1, 1 * mm))
    story.append(Box([P("ffmpeg -y -ss 00:00:33 -to 00:00:45 -i \"source.mp4\" \\<br/>"
                        "&nbsp;&nbsp;-vf \"crop=ih*9/16:ih,scale=1080:1920,setsar=1\" \\<br/>"
                        "&nbsp;&nbsp;-c:v libx264 -preset medium -crf 20 -r 30 \\<br/>"
                        "&nbsp;&nbsp;-c:a aac -b:a 192k clip3.mp4", st_mono)],
                   bg=colors.HexColor("#0f131c"), border=None, pad=9))
    story.append(Spacer(1, 2 * mm))
    story.append(P("That command copy/pastes into a terminal or PowerShell window. If you do "
                   "not have ffmpeg, CapCut\u2019s free \u201c9:16\u201d ratio setting does the "
                   "same job visually \u2014 just never leave a watermark on the export.", st_small))
    story.append(P("2. Shifted crop", st_h3))
    story.append(P("When the subject sits left or right, move the window instead of centring "
                   "it. In the filter, <font face=\"DJM\">crop=ih*9/16:ih:x:0</font> \u2014 "
                   "increase <font face=\"DJM\">x</font> to slide the crop right. Test one "
                   "still frame before you encode the whole clip."))
    story.append(P("3. Blurred pad", st_h3))
    story.append(P("For wide shots, text, logos and end cards, do not crop at all. Fit the "
                   "whole frame to the width and fill the rest with a blurred copy of itself. "
                   "Nothing is lost, and it looks deliberate rather than broken."))
    story.append(Spacer(1, 1 * mm))
    story.append(Box([P("ffmpeg -y -loop 1 -i still.png -filter_complex \\<br/>"
                        "&nbsp;&nbsp;\"[0:v]split=2[a][b];<br/>"
                        "&nbsp;&nbsp;&nbsp;[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=25[bg];<br/>"
                        "&nbsp;&nbsp;&nbsp;[b]scale=1080:-2[fg];<br/>"
                        "&nbsp;&nbsp;&nbsp;[bg][fg]overlay=(W-w)/2:(H-h)/2,format=yuv420p\" \\<br/>"
                        "&nbsp;&nbsp;-t 4 -r 30 -c:v libx264 -crf 20 slide1.mp4", st_mono)],
                   bg=colors.HexColor("#0f131c"), border=None, pad=9))
    story.append(Spacer(1, 3 * mm))
    story.append(P("Check the crop before you post", st_h2))
    story.append(P("Export one still frame from every clip and look at it on your phone, in "
                   "your hand, at arm\u2019s length. Crops that look fine on a laptop timeline "
                   "routinely look broken at phone size \u2014 especially dark footage, where a "
                   "mis-centred crop turns the subject into a black smear."))
    story.append(Spacer(1, 1 * mm))
    story.append(caution("When the crop keeps failing, change the segment", [
        P("If three attempts at a vertical crop of one shot all look bad, the shot is not "
          "vertically composable. Pick a different moment from the same video. Fighting a bad "
          "frame is the most common way beginners burn an evening.", st_small)
    ]))
    story.append(P("Task 3.1", st_h3))
    story.append(P("Export four versions of one clip: two centre crops from different moments, "
                   "one shifted crop, one blurred pad. View all four on your phone. Keep the two "
                   "that read best and note which treatment won and why."))
    story.append(PageBreak())

    # ------------------------------------------------ 3.2
    story.append(Mark(doc, "c3.2"))
    story += h1("Chapter 3.2", "Hooks: the first two seconds")
    story.append(P("The platform measures whether people stay. If they swipe in the first two "
                   "seconds, distribution stops and nothing downstream matters. This is the "
                   "whole game, and it is decided before your editing style gets a chance to "
                   "matter."))
    story.append(P("Four rules that cover most of it", st_h2))
    story += numbered([
        "<b>Start mid-action.</b> No title card, no fade, no logo. Cut into the most kinetic "
        "frame you have, then explain.",
        "<b>Never open on black.</b> Much campaign footage begins on a fade \u2014 trim it. A "
        "second of black is a second of swiping.",
        "<b>Assume no sound.</b> A large share of viewers watch muted. If the clip only makes "
        "sense with audio, it does not work.",
        "<b>One idea per clip.</b> A clip that tries to show the map, the guns and the date "
        "shows none of them.",
    ])
    story.append(Spacer(1, 1 * mm))
    story.append(P("On-screen text", st_h2))
    story.append(P("Three to six words, top third of the frame, bold, white on a dark bar. "
                   "Keep the bottom 15% clear \u2014 that is where the app puts its own interface "
                   "and where your caption will sit."))
    story.append(data_table([
        ["Works", "Fails"],
        ["NEW MAP", "Check out this incredible new map that just dropped"],
        ["3 THINGS I GOT WRONG", "Here are some things you should know about clipping"],
        ["\u20a625,000 FOR 8 CLIPS", "Pricing information for my editing services"],
    ], [PW * 0.42, PW * 0.58]))
    story.append(Spacer(1, 2 * mm))
    story.append(P("Text overlay is not the caption", st_h2))
    story.append(P("The overlay is for the eye and lives inside the video file. The caption is "
                   "the text field you fill when posting, and it is where the campaign\u2019s "
                   "required tag and disclosure go. You need both. Burning the caption into the "
                   "video does not satisfy the campaign and makes the post look like an advert."))
    story.append(Spacer(1, 1 * mm))
    story.append(note("The hook bank habit", [
        P("Keep a running note of every hook that stopped you while scrolling this week. "
          "Twenty entries is enough raw material for a month of posts, and it is free.", st_small)
    ]))
    story.append(P("Task 3.2", st_h3))
    story.append(P("Take one clip and make three versions with three different hooks: a claim, "
                   "a question, and a number. Post them a day apart on the same account. Write "
                   "down which one held attention longer and what you think caused it."))
    story.append(PageBreak())

    # ------------------------------------------------ 3.3
    story.append(Mark(doc, "c3.3"))
    story += h1("Chapter 3.3", "Captions, tags and disclosure")
    story.append(P("This is the least interesting page in the workbook and the one that costs "
                   "people the most money. Campaigns check the caption before they check the "
                   "clip."))
    story.append(P("What a compliant caption contains", st_h2))
    story += numbered([
        "<b>Your own words, specific to the clip.</b> Name something visible in the footage. "
        "Generic hype reads as spam to a reviewer and to the algorithm.",
        "<b>The required tag</b>, spelled exactly as the brief gives it, on every platform. Check "
        "after posting that it rendered as a real mention \u2014 some web uploaders leave it as "
        "plain text.",
        "<b>The required disclosure.</b> In most markets this is a legal requirement, not just a "
        "campaign one. It belongs in the caption, visible without expanding anything.",
        "<b>Nothing the footage does not show.</b> No invented dates, features, statistics or "
        "claims. A misleading caption voids the submission and can flag the account.",
    ])
    story.append(Spacer(1, 1 * mm))
    story.append(P("What not to do with the audio", st_h2))
    story.append(P("Keep the original audio unless the brief allows replacement. The game sound "
                   "or the voice is usually the reason the clip is watchable. If you add music, "
                   "keep it under the original rather than instead of it."))
    story.append(Spacer(1, 2 * mm))
    story.append(caution("Three things that void a submission", [
        P("<b>A watermark</b> from another platform. <b>A caption copied</b> from someone "
          "else\u2019s post. <b>A missing disclosure.</b> Each of these is checked, and each one "
          "turns a finished clip into zero.", st_small)
    ]))
    story.append(Spacer(1, 2 * mm))
    story.append(P("On VPNs and \u201ctargeting tier-1\u201d", st_h2))
    story.append(P("You will find long threads explaining how to set a phone to another country, "
                   "buy a SIM, and run a paid VPN so the algorithm shows your clips to American "
                   "viewers. Do not do this."))
    story.append(P("It breaks the terms of every platform involved, and it breaks campaign rules "
                   "directly: payouts are calculated from your audience\u2019s country data, and "
                   "spoofed or missing location resolves to \u201cno country data\u201d, which is "
                   "excluded. You would be risking a working account to chase a payment structure "
                   "that already pays your real audience."))
    story.append(P("Task 3.3", st_h3))
    story.append(P("Write three captions for one clip, each naming something specific you can "
                   "see. None may contain a claim that is not visible in the video. Choose the "
                   "one that would still make sense to someone who has never heard of the game, "
                   "brand or topic."))
    story.append(PageBreak())

    # ------------------------------------------------ 3.4
    story.append(Mark(doc, "c3.4"))
    story.append(Mark(doc, "c3.4"))
    story += h1("Chapter 3.4", "The four-pass quality check")
    story.append(P("Ninety seconds, every clip, before it goes anywhere. This routine catches "
                   "almost every rejection and most of the clips that quietly die."))
    story.append(Spacer(1, 1 * mm))
    story.append(data_table([
        ["Pass", "What you do", "What you are hunting for"],
        ["1. Muted", "Watch it with the sound off.",
         "Captions unreadable, text outside the safe area, a story that only works with audio."],
        ["2. Blind", "Listen without looking at the screen.",
         "Awkward cuts, silence at the start, audio clipping, a dead first second."],
        ["3. Normal", "Watch it as a viewer would.",
         "Three shots stapled together, a missing middle, a clip that peaks too early."],
        ["4. Ending", "Watch only the last three seconds.",
         "A cut-off word, a fade to black, a payoff that lands after the video stops."],
    ], [PW * 0.14, PW * 0.34, PW * 0.52]))
    story.append(Spacer(1, 3 * mm))
    story.append(P("Then check the boring things", st_h2))
    story += bullets([
        "1080 \u00d7 1920, not 1920 \u00d7 1080.",
        "Audio present and audible at normal phone volume.",
        "No watermark, no black bars, no letterboxing.",
        "Correct tag and correct disclosure in the caption.",
        "File plays start to finish on your phone before you upload it.",
    ])
    story.append(Spacer(1, 2 * mm))
    story.append(good("Batch, do not dribble", [
        P("Source once, cut many. One 60-second video can yield four to six distinct clips if "
          "the segments differ visually. Doing them in one sitting is roughly three times faster "
          "than doing them one at a time \u2014 and a week of clips in reserve means a bad day "
          "does not break your posting streak.", st_small)
    ]))
