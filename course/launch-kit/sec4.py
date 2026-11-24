from _pdfkit import *   # noqa
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
PW = A4[0] - 40 * mm

def build(story, doc):
    # ------------------------------------------------ PART 4
    story.append(PageBreak())
    story.append(Spacer(1, 40 * mm))
    story.append(P("PART FOUR", S("p4d", fontName="DJB", fontSize=9, leading=12, textColor=ACCENT)))
    story.append(Spacer(1, 4 * mm))
    story.append(P("Publish, test,<br/>and repeat", S("p4t", fontName="DJB", fontSize=27, leading=33, textColor=INK)))
    story.append(Spacer(1, 7 * mm))
    story.append(Rule(thickness=1.4, color=ACCENT, space=12))
    story.append(P("A page that is not being distributed looks identical to a page making bad "
                   "clips. This part is about telling the difference, then doing something about "
                   "it with numbers instead of feelings.",
                   S("p4s", fontSize=11, leading=16.5)))
    story.append(PageBreak())

    # ------------------------------------------------ 4.1
    story.append(SetSection(doc, "Part 4 \u00b7 Publishing and testing"))
    story.append(Mark(doc, "c4.1"))
    story += h1("Chapter 4.1", "Setting up an account that is not throttled")
    story.append(P("A brand-new account that uploads clips on day one looks like a bot. The "
                   "algorithm has no behaviour to read, so it shows the clips to almost nobody, "
                   "and every clip caps at a few hundred views regardless of quality."))
    story.append(P("Five days costs you nothing and is the cheapest insurance in this workbook."))
    story.append(Spacer(1, 1 * mm))
    story.append(data_table([
        ["Day", "What you do"],
        ["1", "Scroll 30\u201360 minutes in your niche. Watch to the end. Like a few. Follow 5\u201310 accounts."],
        ["2", "Scroll, like, save one or two clips, share one."],
        ["3", "Comment once or twice, follow more niche accounts, post a story."],
        ["4", "Repeat day 3. Post nothing yet."],
        ["5", "Repeat day 3. The account now has a behavioural history."],
    ], [PW * 0.10, PW * 0.90]))
    story.append(Spacer(1, 3 * mm))
    story.append(P("The rest of the setup", st_h2))
    story += bullets([
        "<b>Name and handle do different jobs.</b> The name field is what search matches; the "
        "handle is what you can still get. Fill both, and keep them unrelated to any single "
        "campaign so you can pivot.",
        "<b>One profile picture, one colour scheme.</b> It should look like a media account, not "
        "a personal account with clips bolted on.",
        "<b>Three-line bio:</b> what you post, who it is for, how to reach you. End with "
        "\u201cDM for collabs\u201d \u2014 that one line is how client work finds you.",
        "<b>No advertising language in the bio.</b> Never \u201csponsored\u201d, never "
        "\u201c#Ad\u201d. Disclosure belongs on each post.",
        "<b>Set the account to a creator/professional category.</b> It unlocks the analytics you "
        "need in 4.3.",
    ])
    story.append(Spacer(1, 1 * mm))
    story.append(warn("One device, and not because you are hiding", [
        P("Stacking five accounts on one phone with one IP, all posting all day, is a bot "
          "pattern and you will lose accounts for it. Clipping on one phone used for nothing "
          "else is normal hygiene. What is not normal, and not allowed, is automation, bulk "
          "posting tools, or running accounts you did not create.", st_small)
    ]))
    story.append(P("Task 4.1", st_h3))
    story.append(P("Create one account with the name, handle, picture, banner and three-line "
                   "bio all finished before you post anything. Look at the profile on a phone, "
                   "not a laptop. Then start the five-day clock."))
    story.append(PageBreak())

    # ------------------------------------------------ 4.2
    story.append(Mark(doc, "c4.2"))
    story += h1("Chapter 4.2", "Posting schedule and platform order")
    story.append(P("Two platforms, one file. Do not re-export per platform and never post "
                   "anything carrying another platform\u2019s watermark."))
    story.append(Spacer(1, 1 * mm))
    story.append(data_table([
        ["Platform", "Why", "Typical rate", "Watch out"],
        ["TikTok", "Fastest cold-start distribution; a new account can reach 100k views.",
         "$1 \u2013 $2.50 / 1K", "Watermarks and repost artefacts are punished hardest here."],
        ["Instagram Reels", "Free second placement for the same file.",
         "$1 \u2013 $1.50 / 1K", "Share to the feed, not Stories only."],
        ["YouTube Shorts", "Longer tail on evergreen footage, slower start.",
         "$0.50 \u2013 $1 / 1K", "Skip in week one; attention is scarce."],
        ["X (Twitter)", "Pays well for crypto campaigns, native clips credit the creator.",
         "$1 \u2013 $15 / 1K", "Different audience entirely. Not a first-month platform."],
    ], [PW * 0.17, PW * 0.35, PW * 0.18, PW * 0.30]))
    story.append(Spacer(1, 3 * mm))
    story.append(P("Cadence", st_h2))
    story += bullets([
        "One to three posts a day, every day. Consistency beats volume; volume beats perfection.",
        "Space posts at least an hour apart so they do not compete with each other for the same test audience.",
        "Posting from Lagos or Nairobi to a European or American evening audience means scheduling, not waking up.",
        "Do not delete underperformers as a reflex \u2014 old clips get picked up by search weeks later.",
    ])
    story.append(Spacer(1, 1 * mm))
    story.append(caution("Live is not submitted", [
        P("A clip that is posted but not submitted to the campaign earns zero, and submission is "
          "a separate step people forget when they are tired at midnight. Submit the moment it "
          "goes live.", st_small)
    ]))
    story.append(P("Task 4.2", st_h3))
    story.append(P("Choose three posting slots for the week and put them in your phone calendar "
                   "with the clip name attached. Post for seven consecutive days. If you miss a "
                   "day, note why \u2014 the reason is usually the thing that will kill the whole "
                   "month."))
    story.append(PageBreak())

    # ------------------------------------------------ 4.3
    story.append(Mark(doc, "c4.3"))
    story += h1("Chapter 4.3", "The split test that turns luck into a format")
    story.append(P("Sooner or later one clip does ten times better than the rest. Most people "
                   "enjoy the number and move on. The ones who build an income work out why, "
                   "then keep it."))
    story.append(P("Step 1: find the outlier", st_h3))
    story.append(P("Post in three distinct styles \u2014 a style being the whole package: visual "
                   "hook, text hook, caption voice, music, colour treatment. If most clips do 500 "
                   "views and one does 10,000, that one is your outlier. Write down the reason in "
                   "one sentence. \u201cIt was better\u201d is not a reason."))
    story.append(P("Step 2: five clips, one variable each", st_h3))
    story.append(data_table([
        ["Clip", "Kept from the outlier", "Everything else"],
        ["1", "Same visual hook", "Changed"],
        ["2", "Same text hook", "Changed"],
        ["3", "Same caption style", "Changed"],
        ["4", "Same sound", "Changed"],
        ["5", "Same colour treatment", "Changed"],
    ], [PW * 0.12, PW * 0.48, PW * 0.40]))
    story.append(Spacer(1, 2 * mm))
    story.append(P("Whichever one wins tells you which element is doing the work. Then run round "
                   "two: lock the winner, add one more element from the outlier, change the rest. "
                   "Repeat until only one thing changes per clip. At that point you have a "
                   "format, and a format is what turns a page into an income stream."))
    story.append(P("Keep everything else constant while you test", st_h2))
    story.append(P("Same account, same posting times, same clip length. Change one variable and "
                   "you learn something. Change three and you are measuring noise and calling it "
                   "instinct."))
    story.append(Spacer(1, 1 * mm))
    story.append(note("Track medians, not totals", [
        P("One viral clip can hide a dying page. Median views per clip is the real health "
          "reading; the total is a story you tell yourself.", st_small)
    ]))
    story.append(P("Task 4.3", st_h3))
    story.append(P("Run one round of five this week. Log every clip and its 24-hour view count "
                   "on one line each. Identify which element the winner kept, and write your next "
                   "five clips around it."))
    story.append(PageBreak())

    # ------------------------------------------------ 4.4
    story.append(Mark(doc, "c4.4"))
    story += h1("Chapter 4.4", "When to kill an account")
    story.append(P("Thirty to sixty clips with nothing past ten thousand views means the "
                   "account is not being distributed. That is not a sign to try harder with the "
                   "same account. It is a sign to start again with everything you learned."))
    story.append(P("The maths of a dead account", st_h2))
    story.append(P("An account carries a distribution history. A new account carries none, which "
                   "means it gets a fresh test audience. Restarting costs you nothing but the "
                   "follows you never had. Keep the edits, keep the format, discard the account."))
    story.append(Spacer(1, 1 * mm))
    story.append(data_table([
        ["Signal", "What it usually means", "What to do"],
        ["Every clip sits at 200\u2013500 views", "Account-level suppression", "Finish the 30-clip test, then restart"],
        ["One clip exploded, rest flat", "A lucky format, not a format", "Split-test the winner (4.3)"],
        ["Views arrive but from the wrong country", "Audience mismatch", "Change the niche or the posting time"],
        ["Submissions rejected repeatedly", "Checklist failure, not editing", "Re-read the brief (2.2)"],
        ["Clients not replying", "Message, not the work", "Send clips, not a price list (2.4)"],
    ], [PW * 0.30, PW * 0.30, PW * 0.40]))
    story.append(Spacer(1, 3 * mm))
    story.append(P("Decide before you start", st_h2))
    story.append(P("Write your kill thresholds down now: how many clips, what view floor, and "
                   "which date you will review. Deciding in advance stops you defending a bad "
                   "account for three weeks because starting again feels like admitting "
                   "something."))
    story.append(Spacer(1, 1 * mm))
    story.append(P("Do not apply this logic to people", st_h2))
    story.append(P("Restarting an account is free. Restarting a client relationship is not. A "
                   "client who goes quiet is a follow-up, not a kill."))
    story.append(P("Task 4.4", st_h3))
    story.append(P("Write three lines in your notebook: \u201cI will restart this account if "
                   "___ clips produce fewer than ___ views by ___.\u201d Fill in the blanks today. "
                   "You will not be objective about it in three weeks."))
