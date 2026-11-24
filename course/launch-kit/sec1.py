from _pdfkit import *   # noqa
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
PW = A4[0] - 40 * mm

def build(story, doc):
    # ------------------------------------------------ PART 1 divider
    story.append(Spacer(1, 40 * mm))
    story.append(P("PART ONE", S("pd", fontName="DJB", fontSize=9, leading=12, textColor=ACCENT)))
    story.append(Spacer(1, 4 * mm))
    story.append(P("Understand the<br/>business first", S("pdt", fontName="DJB", fontSize=27, leading=33, textColor=INK)))
    story.append(Spacer(1, 7 * mm))
    story.append(Rule(thickness=1.4, color=ACCENT, space=12))
    story.append(P("Most people who fail at clipping fail here, in the first week, before "
                   "they have made a single clip. They joined the wrong campaign, or the "
                   "right campaign for the wrong reason, or they never understood that "
                   "the money is attached to views they do not control.",
                   S("pds", fontSize=11, leading=16.5)))
    story.append(PageBreak())

    # ------------------------------------------------ 1.1
    story.append(SetSection(doc, "Part 1 \u00b7 Understanding the business"))
    story.append(Mark(doc, "c1.1"))
    story += h1("Chapter 1.1", "What clipping actually is")
    story.append(P("Clipping is distribution work. Three sentences: someone with footage "
                   "wants an audience. You cut that footage into short vertical videos and "
                   "post them on your own accounts. They pay you for the views those posts "
                   "collect."))
    story.append(P("That is the whole model. Everything else \u2014 the editing, the hooks, "
                   "the captions, the hashtags \u2014 exists to make those views happen."))
    story.append(P("Two things follow from this, and both are uncomfortable:"))
    story += bullets([
        "<b>You are not paid for the edit.</b> A beautiful clip with 300 views earns 300 "
        "views\u2019 worth of money, which is usually nothing. A rough clip with 300,000 views "
        "earns properly. The market pays for reach.",
        "<b>Your skill is not editing software.</b> It is the ability to look at a long video "
        "and identify the three seconds that will stop a thumb. That skill is free to practise "
        "and most people never deliberately practise it.",
    ])
    story.append(Spacer(1, 2 * mm))
    story.append(P("Why brands do this", st_h2))
    story.append(P("A brand can pay an advertising platform for reach, or it can pay dozens of "
                   "independent clippers a small amount per thousand views. The second option "
                   "gives it dozens of different attempts at a viral moment for a cost that "
                   "scales with results rather than with impressions. The clipper absorbs the "
                   "risk of not being seen. That is the trade, stated plainly."))
    story.append(P("Why it suits beginners", st_h2))
    story += bullets([
        "No face, no voice, no audience required on day one.",
        "No money required to start \u2014 a phone and data will do.",
        "The footage is provided, so you are not creating anything from scratch.",
        "Feedback is immediate and numerical: views arrive or they do not.",
        "The same edits can serve two platforms, and later two income streams.",
    ])
    story.append(Spacer(1, 2 * mm))
    story.append(caution("The part nobody puts in the hook", [
        P("Because the payout is attached to views, clipping is a piece-rate job with a "
          "lottery attached. Some months the algorithm picks you up and the work pays "
          "several times what it should. Some months it does not, and the same effort "
          "earns nothing. Anyone who shows you a monthly figure without showing you the "
          "distribution of their clips \u2014 how many did badly \u2014 is showing you the "
          "lottery, not the job.", st_small)
    ]))
    story.append(P("Task 1.1", st_h3))
    story.append(P("Before you read on, open any social feed and scroll for ten minutes. "
                   "Count how many videos you pass before one stops you. Write down what "
                   "stopped you \u2014 a face, a number, motion, a claim, a question. Note how "
                   "many seconds in the scroll stopped. Five entries is enough to keep. "
                   "That list is the beginning of everything in Part 3."))
    story.append(PageBreak())

    # ------------------------------------------------ 1.2
    story.append(Mark(doc, "c1.2"))
    story += h1("Chapter 1.2", "How the money works")
    story.append(P("Clipping campaigns are priced in <b>CPM</b>: cost per mille, meaning per "
                   "thousand views. A campaign paying \u201c$2 per 1K\u201d pays two US dollars "
                   "for every thousand qualifying views on your post."))
    story.append(P("Four numbers decide what you actually receive. Learn all four before you "
                   "join anything."))
    story.append(Spacer(1, 1.5 * mm))
    story.append(data_table([
        ["Number", "What it means", "Where you find it"],
        ["Rate", "Money per 1,000 views. Ranges roughly $0.40\u2013$3.00 across platforms.",
         "The campaign brief"],
        ["Minimum", "Views or earnings needed before a payout is released at all.",
         "Campaign terms page"],
        ["Cap", "The maximum a single clip or account can earn. Usually per platform.",
         "Campaign brief, often in small print"],
        ["Verification", "Which views count. Bots, replays and unknown countries are filtered.",
         "Campaign FAQ"],
    ], [PW * 0.17, PW * 0.48, PW * 0.35]))
    story.append(Spacer(1, 3 * mm))
    story.append(P("Worked example", st_h2))
    story.append(P("Your clip gets 40,000 views on TikTok. The campaign pays $2.00 per 1K, "
                   "the minimum is $6, and the cap is $1,200."))
    story.append(Spacer(1, 1 * mm))
    story.append(data_table([
        ["Step", "Working", "Result"],
        ["Gross at rate", "40 \u00f7 1,000 \u00d7 $2.00", "$80.00"],
        ["Less verification filter (assume 30%)", "28,000 verified views \u00d7 $2 \u00f7 1,000", "$56.00"],
        ["Above the $6 minimum?", "Yes", "pays"],
        ["Below the $1,200 cap?", "Yes", "not capped"],
        ["<b>What you receive</b>", "", "<b>$56.00 \u2248 \u20a675,000</b>"],
    ], [PW * 0.36, PW * 0.42, PW * 0.22]))
    story.append(Spacer(1, 2 * mm))
    story.append(P("That 30% figure is an assumption, not a rule. Some campaigns filter almost "
                   "nothing; others filter heavily when a post reaches an audience outside the "
                   "targeted country. Build your expectations on the lower number and be "
                   "pleasantly surprised.", st_small))
    story.append(Spacer(1, 2 * mm))
    story.append(warn("The threshold trap, in plain words", [
        P("A campaign that only pays above 100,000 views per clip is not a campaign that "
          "pays a bit less for smaller clips. It pays <b>zero</b> for a 90,000-view clip. "
          "Beginners join these because the rate looks high, then produce fifteen good clips "
          "and receive nothing. Never make a threshold campaign your first.", st_small)
    ]))
    story.append(P("Task 1.2", st_h3))
    story.append(P("Take the campaign you are considering and write the four numbers on a "
                   "single line: rate, minimum, cap, verification rule. If you cannot find "
                   "one of them, you have not finished reading the brief."))
    story.append(PageBreak())

    # ------------------------------------------------ 1.3
    story.append(Mark(doc, "c1.3"))
    story += h1("Chapter 1.3", "What a view is worth \u2014 in naira and shillings")
    story.append(P("Convert everything into the money you spend, then decide whether the "
                   "target you have in your head is a plan or a wish."))
    story.append(P("The arithmetic is the same everywhere. The figures below are in naira and "
                   "Kenyan shillings because those are the two markets this edition prices for "
                   "\u2014 substitute your own currency and the method still holds.", st_small))
    story.append(Spacer(1, 1 * mm))
    story.append(P("Rates used throughout: \u20a61,340 = $1 and KSh1 = \u20a610.35, October "
                   "2026 mid-market. Check the live rate before you price anything.", st_small))
    story.append(Spacer(1, 3 * mm))
    story.append(P("What 100,000 views is worth", st_h2))
    story.append(data_table([
        ["Platform rate", "Gross", "In naira", "In shillings"],
        ["$1.00 per 1K", "$100", "\u20a6134,000", "KSh 12,950"],
        ["$1.50 per 1K", "$150", "\u20a6201,000", "KSh 19,420"],
        ["$2.00 per 1K", "$200", "\u20a6268,000", "KSh 25,900"],
        ["$3.00 per 1K", "$300", "\u20a6402,000", "KSh 38,850"],
    ], [PW * 0.28, PW * 0.18, PW * 0.27, PW * 0.27]))
    story.append(Spacer(1, 3 * mm))
    story.append(P("What a target requires", st_h2))
    story.append(data_table([
        ["Your target", "At $1/1K", "At $2/1K", "Views per day, 30 days, at $2"],
        ["\u20a650,000", "25,000 views", "12,500 views", "417"],
        ["\u20a6150,000", "75,000 views", "37,500 views", "1,250"],
        ["\u20a6500,000", "250,000 views", "125,000 views", "4,167"],
        ["\u20a61,000,000", "500,000 views", "250,000 views", "8,333"],
        ["\u20a62,000,000", "1,000,000 views", "500,000 views", "16,667"],
    ], [PW * 0.24, PW * 0.24, PW * 0.24, PW * 0.28]))
    story.append(Spacer(1, 3 * mm))
    story.append(P("Read the last column slowly. \u20a62 million in 30 days needs roughly "
                   "17,000 qualifying views every day for a month, starting from an account "
                   "nobody follows. That is not a plan you can schedule rent around."))
    story.append(Spacer(1, 2 * mm))
    story.append(good("What a good month looks like", [
        P("Thirty days of consistent posting, one campaign, two platforms, no viral "
          "breakout: 8\u201315 clips a week, a median of 1,000\u20135,000 views each, one or "
          "two clips that overshoot into 20,000\u2013100,000. That is typically "
          "\u20a625,000\u2013\u20a6150,000 in campaign income. Real, modest, repeatable. "
          "The viral clip is a bonus, not the plan.", st_small)
    ]))
    story.append(Spacer(1, 2 * mm))
    story.append(P("Why the second stream matters", st_h2))
    story.append(P("Every number above depends on a platform deciding to show your video. "
                   "Client work does not: a podcaster who pays \u20a625,000 for eight clips pays "
                   "whether they get 200 views or 200,000. Run both \u2014 campaigns for "
                   "upside, clients for a floor."))
    story.append(P("Task 1.3", st_h3))
    story.append(P("Write your real target for the next 30 days \u2014 not the number you "
                   "want, the number you need \u2014 and the views per day it requires at your "
                   "actual campaign rate. Then write the same figure for client work, using "
                   "\u20a65,000 per clip and 8 clips per client. Compare which one you can "
                   "control."))
    story.append(PageBreak())

    # ------------------------------------------------ 1.4
    story.append(Mark(doc, "c1.4"))
    story += h1("Chapter 1.4", "Four ways people earn from clipping")
    story.append(P("These are four different businesses that happen to share an editing "
                   "skill. Confusing them is why people post forty clips, earn nothing, and "
                   "conclude that clipping does not work."))
    story.append(Spacer(1, 1.5 * mm))
    rows = [
        ["", "<b>1. Campaign clipping</b>", "<b>2. Client editing</b>"],
        ["What you do", "Cut provided footage, post it, submit links.",
         "Cut a client\u2019s footage, deliver files, invoice."],
        ["Who pays", "A campaign or agency, per 1,000 views.",
         "A person or business, per clip or per month."],
        ["When you are paid", "After views accrue and are verified \u2014 weeks.",
         "On delivery, or half up front."],
        ["What you control", "The edit and the hook. Not the reach.",
         "Everything. The price is agreed before you start."],
        ["Realistic first month", "\u20a60\u2013\u20a6150,000", "\u20a60\u2013\u20a6120,000"],
        ["Main risk", "You do great work and nobody sees it.",
         "Nobody replies to your messages."],
    ]
    story.append(data_table(rows, [PW * 0.22, PW * 0.39, PW * 0.39]))
    story.append(Spacer(1, 3 * mm))
    story.append(P("3. Running your own pages", st_h3))
    story.append(P("You build pages in a niche, grow an audience, and monetise through "
                   "campaigns, affiliate deals, or by selling promotion to creators. Slowest "
                   "to start, most durable once it works. Not a 30-day plan \u2014 it is what "
                   "the first two streams quietly build while you are doing them."))
    story.append(P("4. Teaching", st_h3))
    story.append(P("Selling a course or mentoring other clippers. Only legitimate once you "
                   "have your own documented results \u2014 and it is the most crowded, most "
                   "distrusted corner of this market. See the warning below."))
    story.append(Spacer(1, 2 * mm))
    story.append(caution("If you are thinking of selling a course", [
        P("A course built from other people\u2019s tutorials, screenshots and earnings claims "
          "sells once and destroys your name. It also may not be legal: downloading or "
          "compiling someone else\u2019s teaching does not give you the right to resell it, "
          "and platform rules on financial claims are strict. The only version worth building "
          "is your own: your footage, your numbers, your losses documented honestly \u2014 "
          "and that material does not exist until you have done the work.", st_small)
    ]))
    story.append(P("Task 1.4", st_h3))
    story.append(P("Choose your primary stream for the next 30 days and write one sentence "
                   "explaining why. Most beginners should pick campaigns, because the "
                   "footage is provided and the learning is fast. Anyone with a laptop, decent "
                   "English and two hours a day should run client work in parallel from week two."))
    story.append(PageBreak())

    # ------------------------------------------------ 1.5
    story.append(Mark(doc, "c1.5"))
    story += h1("Chapter 1.5", "What you need before day one")
    story.append(P("The honest list. Most of it you already own."))
    story.append(Spacer(1, 1 * mm))
    story.append(data_table([
        ["Needed", "Minimum", "Notes"],
        ["Phone or laptop", "Android phone from the last 5 years",
         "A laptop makes batch editing far faster but is not required."],
        ["Editing app", "CapCut (free)",
         "Free tier is enough. Watermark removal requires care \u2014 see 3.1."],
        ["Data", "1\u20132 GB per week", "Uploading video is the expensive part, not editing."],
        ["Accounts", "TikTok + Instagram",
         "Only create the platforms your campaign allows."],
        ["Payout account", "Nigerian or Kenyan bank / M-Pesa",
         "Check the platform supports your country before you earn."],
        ["Time", "1\u20132 hours a day minimum",
         "Below this, you will produce too few clips to learn anything from."],
        ["Money", "\u20a60 to start",
         "Optional: \u20a640,000 for ads, but only after the free version is proven."],
    ], [PW * 0.22, PW * 0.30, PW * 0.48]))
    story.append(Spacer(1, 3 * mm))
    story.append(P("What you do not need", st_h2))
    story += bullets([
        "A course. Everything in this workbook is free knowledge; the paid part is the structure.",
        "A camera, a microphone, or your face on screen.",
        "Followers. Campaign payouts do not require an audience.",
        "Expensive software. CapCut\u2019s free tier does everything in Part 3.",
        "A website. Clients can be invoiced from a phone.",
        "A VPN. See 3.3 \u2014 this is not a technical requirement, it is a myth that gets accounts banned.",
    ])
    story.append(Spacer(1, 1.5 * mm))
    story.append(P("Two decisions to make now", st_h2))
    story.append(P("<b>One:</b> which single device you will clip on. Changing devices mid-month "
                   "scatters your accounts across environments and makes it harder to tell what "
                   "is working."))
    story.append(P("<b>Two:</b> which niche. Pick based on whether you can get legal footage "
                   "every week, not on what you enjoy watching. A niche with official campaign "
                   "footage beats a niche you love with no permission to use anything."))
    story.append(Spacer(1, 2 * mm))
    story.append(note("A note on age and money", [
        P("Campaigns and payment platforms require you to be 18 or older, or to have an adult "
          "account holder. If you are under 18, involve a parent or guardian in the accounts, "
          "the contracts and the payouts. Do not misrepresent your age \u2014 it is the fastest "
          "way to lose a payout you have already earned.", st_small)
    ]))
    story.append(P("Task 1.5", st_h3))
    story.append(P("Confirm the four things that can actually block you: device, data "
                   "allowance for a month, account age/eligibility, and a payout route that "
                   "works in your country. Write each one and whether it is ready. Any "
                   "\u201cno\u201d becomes your first task tomorrow, before any editing."))
