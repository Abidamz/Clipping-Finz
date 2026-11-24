from _pdfkit import *   # noqa
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
PW = A4[0] - 40 * mm

def build(story, doc):
    # ------------------------------------------------ PART 2
    story.append(PageBreak())
    story.append(Spacer(1, 40 * mm))
    story.append(P("PART TWO", S("p2d", fontName="DJB", fontSize=9, leading=12, textColor=ACCENT)))
    story.append(Spacer(1, 4 * mm))
    story.append(P("Find real work,<br/>not schemes", S("p2t", fontName="DJB", fontSize=27, leading=33, textColor=INK)))
    story.append(Spacer(1, 7 * mm))
    story.append(Rule(thickness=1.4, color=ACCENT, space=12))
    story.append(P("The clipping economy has more people selling courses about clipping than "
                   "people making a living from it. This part is about telling the two apart "
                   "before you spend your data, your time, or your money.",
                   S("p2s", fontSize=11, leading=16.5)))
    story.append(PageBreak())

    # ------------------------------------------------ 2.1
    story.append(SetSection(doc, "Part 2 \u00b7 Finding real work"))
    story.append(Mark(doc, "c2.1"))
    story += h1("Chapter 2.1", "The platforms that actually pay")
    story.append(P("These are the boards where campaigns are posted. Rates below are typical "
                   "ranges reported in late 2026 \u2014 they change per campaign, so treat them "
                   "as expectations, not prices."))
    story.append(Spacer(1, 1.5 * mm))
    story.append(data_table([
        ["Platform", "Typical rate", "Withdrawal", "Notes"],
        ["Content Rewards (on Whop)", "$1 \u2013 $1.25 / 1K", "from ~$1",
         "Largest board, most agency campaigns. Withdraw to a Nigerian bank account."],
        ["Vyro", "$1 \u2013 $2.50 / 1K", "$10", "Weekly payouts, median around $2."],
        ["Clipster", "median ~$1 / 1K", "varies", "Biggest campaign board by volume, app + web."],
        ["Clipping.net", "$0.40 \u2013 $3 / 1K", "varies", "Large brand campaigns, wide rate spread."],
        ["Clipping Culture", "top of range for gaming", "varies",
         "Game campaigns, official footage provided, no dedicated page required."],
        ["Trapster", "$1 \u2013 $5 / 1K", "Stripe",
         "Game studios only. Studios set their own CPM."],
        ["Clipur", "~$1.50 / 1K", "varies", "Creator-led, mostly X (Twitter). Different audience."],
        ["Promote.fun", "$0.50 \u2013 $3 / 1K", "crypto", "Memecoin campaigns. Volatile, high risk."],
    ], [PW * 0.23, PW * 0.21, PW * 0.14, PW * 0.42]))
    story.append(Spacer(1, 3 * mm))
    story.append(P("Two accounts you need regardless", st_h2))
    story.append(P("<b>Whop</b> is the payment rail behind Content Rewards and many agencies. "
                   "Even if you later join campaigns hosted elsewhere, most of them pay through "
                   "Whop. Set up the payout method before you earn, not after."))
    story.append(P("<b>A campaign spreadsheet or note</b> with the four numbers from 1.2 for "
                   "every campaign you join. Within a month you will have forgotten which "
                   "campaign had the $6 minimum and which had the 100,000-view threshold."))
    story.append(Spacer(1, 2 * mm))
    story.append(warn("How to spot a scheme dressed as a campaign", [
        P("A real campaign pays you. It does not ask you to pay it. If joining requires a "
          "\u201cstarter pack\u201d, a subscription, or a deposit \u2014 it is not a campaign. "
          "If payment requires you to recruit other clippers, it is a pyramid, whatever it is "
          "called. If the only way to learn the payout rules is to join a paid Discord, walk "
          "away.", st_small)
    ]))
    story.append(P("Task 2.1", st_h3))
    story.append(P("Create a Whop account and a Content Rewards account today. Browse the "
                   "Discover page without joining anything. Write down the three campaigns with "
                   "the best combination of rate, minimum and remaining budget for the accounts "
                   "you can actually make."))
    story.append(PageBreak())

    # ------------------------------------------------ 2.2
    story.append(Mark(doc, "c2.2"))
    story += h1("Chapter 2.2", "How to read a campaign brief")
    story.append(P("Most rejections are not editing failures. They are reading failures. A "
                   "brief takes eight minutes to read properly and saves you a week."))
    story.append(P("The five facts", st_h2))
    story.append(P("Extract these before you open an editor. If any is missing, the campaign "
                   "is not ready to join."))
    story += numbered([
        "<b>Rate</b>, per platform if it differs. A campaign can pay $2 on TikTok and $1.50 on Instagram.",
        "<b>Minimum</b> \u2014 views or earnings before anything is released.",
        "<b>Cap</b> \u2014 per clip and per account, and whether it applies per platform.",
        "<b>Platforms allowed</b> \u2014 posting on a platform that is not listed usually voids the submission.",
        "<b>Tags and disclosure</b> \u2014 the exact handle to tag and the exact disclosure wording required.",
    ])
    story.append(P("The five restrictions", st_h2))
    story += numbered([
        "<b>Permitted footage.</b> \u201cOfficial folder only\u201d means anything else is a rejection, however good it looks.",
        "<b>Watermarks.</b> Most campaigns exclude clips carrying another platform\u2019s watermark.",
        "<b>Caption originality.</b> Copy-pasted captions that reviewers have seen forty times get refused.",
        "<b>Country rules.</b> Which audience countries pay, and whether \u201cno country data\u201d is excluded.",
        "<b>What counts as an invalid view.</b> Bots, purchased views, and sometimes duplicate posts across accounts.",
    ])
    story.append(Spacer(1, 1 * mm))
    story.append(note("Read it twice: once before editing, once before submitting", [
        P("The second read catches the tag you forgot. It takes ninety seconds and is the "
          "single highest-value habit in this workbook.", st_small)
    ]))
    story.append(Spacer(1, 2 * mm))
    story.append(P("Check the budget is still there", st_h2))
    story.append(P("A campaign with a brilliant rate and $200 left in the pot will close before "
                   "your clips accumulate views. Remaining budget matters as much as rate. "
                   "Join early in a campaign\u2019s life, not at the end."))
    story.append(P("Task 2.2", st_h3))
    story.append(P("Take one live brief and write the five facts on paper. Tape it where you "
                   "edit. Then re-read the brief and add anything you missed in a different pen. "
                   "The second-pen items are the ones that would have cost you a payout."))
    story.append(PageBreak())

    # ------------------------------------------------ 2.3
    story.append(Mark(doc, "c2.3"))
    story += h1("Chapter 2.3", "Seven traps that eat beginners")
    story.append(Spacer(1, 1 * mm))
    traps = [
        ("The high threshold",
         "Pays only above 100,000 views per clip. A 90,000-view clip earns zero, not "
         "part-payment. Never make this your first campaign."),
        ("The unverified view",
         "Your dashboard shows 80,000; settlement says 55,000. Views are filtered for bots, "
         "replays and missing country data. Plan on the lower number."),
        ("The cap",
         "A viral clip stops earning at the ceiling. Five good clips beat one enormous one."),
        ("The disappearing budget",
         "Campaigns close when the money runs out, sometimes mid-week. Submit the same day "
         "you post."),
        ("The unpaid labour",
         "If a campaign asks you to pay to join, buy a starter pack, or recruit others to "
         "unlock payment, it is a scheme with a campaign\u2019s vocabulary."),
        ("The borrowed footage",
         "Clipping a creator who has not given permission can earn a takedown, a strike, or a "
         "copyright claim on the platform. \u201cIt is fair use\u201d is not a defence you can "
         "afford to test with your only account."),
        ("The location trick",
         "Spoofing a country with a VPN or a foreign SIM is the most expensive advice on the "
         "internet. Campaigns pay on audience country data; spoofed or missing data resolves "
         "to \u201cno country data\u201d and pays nothing, or trips fraud screening and closes "
         "the account. Skip it."),
    ]
    for title, body in traps:
        story.append(Paragraph(f'<b>{title}.</b>&nbsp; {body}', S(
            "trap" + title[:3], fontSize=9.4, leading=14.4, spaceAfter=7,
            leftIndent=8, firstLineIndent=-8)))
    story.append(Spacer(1, 2 * mm))
    story.append(caution("The one rule that covers all seven", [
        P("Treat every payout as zero until it is in your account. Log the views, celebrate "
          "the clip, but never spend money you have not received. Every trap above hurts "
          "because someone spent the payout before it cleared.", st_small)
    ]))
    story.append(P("Task 2.3", st_h3))
    story.append(P("For the campaign you are considering, write its settlement maths: views "
                   "\u00d7 rate \u00f7 1,000, minus a 30% verification haircut, compared with the "
                   "cap. That number is what one clip is realistically worth to you. If it is "
                   "below the minimum payout, you know what has to change."))
    story.append(PageBreak())

    # ------------------------------------------------ 2.4
    story.append(Mark(doc, "c2.4"))
    story += h1("Chapter 2.4", "Client work: the income that does not depend on luck")
    story.append(P("A client pays for a deliverable, not for a result. That single difference "
                   "makes client work the more reliable half of this month \u2014 and the half "
                   "most clippers never start, because it requires sending a message to a "
                   "stranger."))
    story.append(P("Who to approach", st_h2))
    story.append(P("Look for people publishing long-form video with no short-form output. "
                   "They have the problem you solve, and they have already shown they will "
                   "invest in content."))
    story += bullets([
        "Podcasters and interview hosts \u2014 the easiest yes, because the format is built for clipping.",
        "Coaches, consultants and course sellers \u2014 they understand paying for marketing.",
        "Small businesses with an active page but only static posts.",
        "Churches, event promoters and conference organisers \u2014 high volume, seasonal.",
        "Streamers and gamers with long VODs and no editor.",
    ])
    story.append(P("What to send", st_h2))
    story.append(P("Do not send a price list to a stranger. Send finished work \u2014 three "
                   "clips cut from their latest video, with no conditions. It converts far "
                   "better than any pitch."))
    story.append(Spacer(1, 1.5 * mm))
    story.append(Box([P("Hi [Name] \u2014 I cut short-form clips from long videos.<br/><br/>"
                        "I made three from your last episode, no charge and no strings: [link]<br/><br/>"
                        "If they fit your style, I do [8] clips a month for \u20a6[price], "
                        "captions and hooks included. You keep the files and the raw footage.<br/><br/>"
                        "Want me to keep going with this week\u2019s upload?",
                        S("tpl", fontSize=9.2, leading=14, textColor=INK))],
                   bg=PANEL, border=ACCENT, label="The message that works", pad=10))
    story.append(Spacer(1, 3 * mm))
    story.append(P("Pricing that does not undersell you", st_h2))
    story.append(data_table([
        ["Package", "What they get", "Nigeria", "Kenya"],
        ["Starter", "3 clips, 1 revision each", "\u20a610,000", "KSh 950"],
        ["Weekly", "8 clips, captions and hooks, 2 revisions", "\u20a625,000", "KSh 2,400"],
        ["Monthly", "20 clips, 2 revisions, priority turnaround", "\u20a660,000", "KSh 5,800"],
    ], [PW * 0.16, PW * 0.44, PW * 0.20, PW * 0.20]))
    story.append(Spacer(1, 2 * mm))
    story.append(P("Take a 50% deposit above \u20a620,000 and cap revisions at two per clip, in "
                   "writing. And never promise views: you are selling editing, not virality. "
                   "Promise reach and you will end up refunding someone.", st_small))
    story.append(Spacer(1, 1 * mm))
    story.append(P("Task 2.4", st_h3))
    story.append(P("List forty accounts that post long-form video and no shorts, then send "
                   "three clips to the top three names this week. Expect two silences and one reply.",
                   st_small))
