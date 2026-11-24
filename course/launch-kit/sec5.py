from _pdfkit import *   # noqa
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
PW = A4[0] - 40 * mm

def build(story, doc):
    # ------------------------------------------------ PART 5
    story.append(PageBreak())
    story.append(Spacer(1, 40 * mm))
    story.append(P("PART FIVE", S("p5d", fontName="DJB", fontSize=9, leading=12, textColor=ACCENT)))
    story.append(Spacer(1, 4 * mm))
    story.append(P("Get the money", S("p5t", fontName="DJB", fontSize=27, leading=33, textColor=INK)))
    story.append(Spacer(1, 7 * mm))
    story.append(Rule(thickness=1.4, color=ACCENT, space=12))
    story.append(P("\u201cViews\u201d and \u201cmoney\u201d are separated by four administrative "
                   "steps, and most beginners lose their first payout in the gap between them.",
                   S("p5s", fontSize=11, leading=16.5)))
    story.append(PageBreak())

    # ------------------------------------------------ 5.1
    story.append(SetSection(doc, "Part 5 \u00b7 Getting paid"))
    story.append(Mark(doc, "c5.1"))
    story += h1("Chapter 5.1", "Submission, approval, and what you are actually paid")
    story.append(P("Posting is step one. The sequence that ends in money looks like this:"))
    story.append(Spacer(1, 1 * mm))
    story.append(data_table([
        ["#", "Step", "What goes wrong here"],
        ["1", "Post the clip publicly", "Set to private or friends-only \u2014 cannot be verified."],
        ["2", "Submit the post URL to the campaign", "Submitting your profile URL instead of the post URL."],
        ["3", "Wait for review", "Assuming approval is automatic. It is not."],
        ["4", "Views accrue and are verified", "Counting raw views; settlement minus filters is lower."],
        ["5", "Payout released to platform balance", "Not knowing the minimum withdrawal."],
        ["6", "Withdraw to your bank / M-Pesa", "Currency conversion and fees not accounted for."],
    ], [PW * 0.06, PW * 0.34, PW * 0.60]))
    story.append(Spacer(1, 3 * mm))
    story.append(P("Receipts, every time", st_h2))
    story.append(P("Screenshot each submission: the URL, the date, and the view count at the "
                   "moment you submitted. Keep them in one folder on your phone. If a payout "
                   "comes up short, that screenshot is your entire case \u2014 and without it you "
                   "have nothing to argue with."))
    story.append(Spacer(1, 1 * mm))
    story.append(caution("A rejection is not appealable into a payout", [
        P("Reviews happen once. This is why the four-pass check in 3.4 and the second read of "
          "the brief in 2.2 exist: they are cheaper than a rejection.", st_small)
    ]))
    story.append(P("Task 5.1", st_h3))
    story.append(P("Create a photo album called \u201cclip receipts\u201d. Screenshot every "
                   "submission screen from now on, without exception. In thirty days this album "
                   "will be the only reliable record of what you did."))
    story.append(PageBreak())

    # ------------------------------------------------ 5.2
    story.append(Mark(doc, "c5.2"))
    story += h1("Chapter 5.2", "Getting paid to a Nigerian or Kenyan bank")
    story.append(P("Two routes matter, and both have a delay you must plan around."))
    story.append(Spacer(1, 1 * mm))
    story.append(P("Campaign payouts", st_h2))
    story.append(P("Most campaigns settle into a platform balance \u2014 Whop is the most "
                   "common \u2014 and pay out to a Nigerian bank account. Set the withdrawal "
                   "method before you earn anything. Minimum withdrawals are small ($1 to $10 on "
                   "most boards), so test the route with the smallest possible amount as soon as "
                   "you have a balance. Learning how the money arrives is worth more than the "
                   "eight dollars it costs."))
    story.append(P("Selling a product or service", st_h2))
    story.append(data_table([
        ["", "Selar", "Systeme.io"],
        ["Cost to start", "No monthly fee; commission per sale", "Free plan, no card required"],
        ["Fee on a Kenyan sale", "5% + KSh 20", "0% platform fee (payment processor fees still apply)"],
        ["M-Pesa", "Supported", "Depends on your connected payment gateway and country"],
        ["KES payouts", "Available 4 business days after the sale", "Via your gateway"],
        ["NGN payouts", "Available 1 business day after the sale", "Via your gateway"],
        ["Best for", "Selling to Kenyan and Nigerian buyers today", "Building the funnel, email list and course area"],
        ["Free-plan ceilings", "\u2014", "2,000 contacts, 3 funnels, 1 course, 1 automation rule, $10,000 lifetime sales"],
    ], [PW * 0.20, PW * 0.40, PW * 0.40]))
    story.append(Spacer(1, 3 * mm))
    story.append(P("The arrangement that works", st_h2))
    story.append(P("<b>Systeme.io builds the machine, Selar takes the Kenyan money.</b> The free "
                   "Systeme.io plan hosts the landing page, the email capture and the course "
                   "area. Selar handles the checkout that a Kenyan buyer can actually complete in "
                   "shillings with M-Pesa. Do not try to make one platform do both jobs in week "
                   "one."))
    story.append(Spacer(1, 1 * mm))
    story.append(warn("Test the checkout with a real person before you spend on ads", [
        P("Five things must be true: the buyer sees the price in their currency; M-Pesa or card "
          "works; the confirmation is automatic; the buyer receives access instructions; and you "
          "can withdraw the money to an account you control. Until all five are true, advertising "
          "is a donation.", st_small)
    ]))
    story.append(P("Task 5.2", st_h3))
    story.append(P("Set up the withdrawal method on every platform you have joined and do one "
                   "smallest-possible withdrawal. Write down how long it took and what it cost. "
                   "That number is the real exchange rate of this business."))
    story.append(PageBreak())

    # ------------------------------------------------ 5.3
    story.append(Mark(doc, "c5.3"))
    story += h1("Chapter 5.3", "Records, tax and keeping clean")
    story.append(P("Boring, short, and the reason people get caught out at exactly the moment "
                   "the money starts being real."))
    story += bullets([
        "<b>One log, one line per payout:</b> date, platform, gross, fee, net, currency received, "
        "exchange rate on the day.",
        "<b>Separate the money.</b> One account for earnings, another for spending. It makes every "
        "budget honest, including a wedding budget.",
        "<b>Screenshot the exchange rate</b> when a foreign payout lands. It is the only defensible "
        "way to report foreign income later.",
        "<b>Freelance and digital income is taxable</b> in both Nigeria and Kenya. At small amounts "
        "nobody will chase you; the records cost nothing and reconstructing a year from memory costs "
        "a lot.",
        "<b>If the totals get real,</b> talk to an accountant once. One conversation is cheaper than "
        "a guess.",
    ])
    story.append(Spacer(1, 2 * mm))
    story.append(note("A note on the law, not just the platform rules", [
        P("Copyright on footage you did not create and were not licensed to clip belongs to "
          "whoever made it. Campaign footage is licensed for exactly this use. Nothing else is. "
          "Selling a product built from someone else\u2019s course material is a separate and "
          "larger problem. This workbook is written for you to sell something you made.", st_small)
    ]))
    story.append(P("Task 5.3", st_h3))
    story.append(P("Create the earnings log today, with the column headers above, and log the "
                   "first zero-value entry: today\u2019s date and \u201cstarted\u201d. The habit is "
                   "the asset, not the first payout."))
