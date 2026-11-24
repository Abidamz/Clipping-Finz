#!/usr/bin/env python3
"""
Builds the seller's launch pack:
  Launch-Plan-Kenya-Nigeria-30-Days.pdf
Companion to the sellable workbook. Internal use.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pdfkit import *   # noqa
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "Launch-Plan-Kenya-Nigeria-30-Days.pdf")
PW = A4[0] - 40 * mm

doc = Doc(OUT, "Launch Plan \u2014 Kenya & Nigeria, 30 Days")
story = []

def hr(s):
    story.append(SetSection(doc, s))

# ---------------------------------------------------------------- cover
story.append(NextPageTemplate("body"))
story.append(Spacer(1, 14 * mm))
story.append(P("OPERATING PACK", S("k", fontName="DJB", fontSize=9, leading=12, textColor=ACCENT)))
story.append(Spacer(1, 5 * mm))
story.append(P("Selling Clipping From Zero", S("t1", fontName="DJB", fontSize=27, leading=34, textColor=INK)))
story.append(P("Kenya first, Nigeria second", S("t2", fontName="DJB", fontSize=27, leading=34, textColor=INK)))
story.append(Spacer(1, 6 * mm))
story.append(Rule(thickness=2, color=ACCENT, space=12))
story.append(P("A 30-day launch plan with a real advertising budget, the exact ad scripts, "
               "the checkout setup, and the numbers behind every claim.",
               S("s", fontSize=11.5, leading=17)))
story.append(Spacer(1, 8 * mm))
story.append(data_table([
    ["Budget assumed", "\u20a640,000 advertising (about $30)"],
    ["Primary market", "Kenya \u2014 because M-Pesa checkout works and the audience is buying digital courses"],
    ["Secondary market", "Nigeria \u2014 free traffic and warm network, not paid initially"],
    ["Stack", "Systeme.io (free) for pages, email and course area; Selar for KES checkout"],
    ["Main offer", "KSh 1,499 \u2248 \u20a615,500"],
    ["Goal", "First 10 paying customers in 30 days, not 129"],
], [PW * 0.28, PW * 0.72], header=False, zebra=False))
story.append(Spacer(1, 7 * mm))
story.append(caution("The one thing to read before page 2", [
    P("TikTok Ads has a hard minimum of <b>$50 per day at campaign level and $20 per ad group</b>. "
      "\u20a640,000 is roughly $30. That is <b>less than one day</b> of TikTok advertising at the "
      "platform minimum \u2014 not four weeks. Any plan built on running TikTok ads for a month on "
      "\u20a640,000 is arithmetic that cannot happen. Page 4 shows what the same money buys "
      "elsewhere, and what to do about it.", st_small)
]))
story.append(PageBreak())

# ---------------------------------------------------------------- 1. reality
hr("1 \u00b7 The budget reality")
story += h1("Section 1", "What \u20a640,000 actually buys")
story.append(P("Advertising minimums are set by the platform, not by your plan. Here is the "
               "comparison that matters, using October 2026 rates (\u20a61,340 = $1)."))
story.append(Spacer(1, 1.5 * mm))
story.append(data_table([
    ["Platform", "Minimum to run", "What \u20a640,000 (\u2248$30) buys"],
    ["TikTok Ads", "$50/day campaign, $20/day ad group",
     "<b>Less than one day.</b> Cannot run a multi-day test at all."],
    ["Meta (Facebook/Instagram)", "$1\u2013$5/day minimum; ~KSh 500/day practical in Kenya",
     "<b>4\u20136 days</b> of a small test, or 2 weeks at the bare minimum."],
    ["Google/YouTube", "Varies, typically $10/day",
     "About 3 days. Wrong format for this offer."],
    ["No ads at all", "\u2014",
     "Unlimited, if the product is good and you do the outreach yourself."],
], [PW * 0.21, PW * 0.33, PW * 0.46]))
story.append(Spacer(1, 3 * mm))
story.append(P("Three ways to proceed. Pick one before you spend anything.", st_h2))
story.append(Spacer(1, 1 * mm))
story.append(P("<b>Option A \u2014 Meta test, \u20a640,000 (\u2248 KSh 3,000).</b> Six days at "
               "KSh 500/day, one campaign, three ad sets with three creatives, objective "
               "\u201cSales\u201d if the Selar checkout pixel is installed, otherwise "
               "\u201cTraffic\u201d. This is the only option that produces real data on a "
               "\u20a640,000 budget. It is what this pack plans around."))
story.append(P("<b>Option B \u2014 no ads, all outreach.</b> Zero spend, 100% of the budget "
               "kept. Slower and less scalable, but with a brand-new page and an unproven "
               "product, a cold Meta audience converts poorly anyway. Twenty DMs to Kenyan "
               "creators and student communities may beat KSh 3,000 of ads."))
story.append(P("<b>Option C \u2014 save the \u20a640,000.</b> Launch entirely organically for "
               "two weeks. If nothing sells at all, the ads were never the problem, and you "
               "still have the money."))
story.append(Spacer(1, 2 * mm))
story.append(warn("Recommended: B, then A", [
    P("Run two weeks of organic and outreach first, at zero cost. Only release the "
      "\u20a640,000 once you have (a) a checkout that a real Kenyan has completed, and (b) at "
      "least one stranger who said yes without knowing you. Advertising amplifies demand; it "
      "does not create it. Spending first is how the budget disappears with nothing learned.",
      st_small)
]))
story.append(PageBreak())

# ---------------------------------------------------------------- 2. numbers
hr("2 \u00b7 The numbers")
story += h1("Section 2", "What you need to sell, and what you keep")
story.append(P("Convert the target once, then stop looking at it and look at the units."))
story.append(Spacer(1, 1.5 * mm))
story.append(data_table([
    ["Your target", "Sales at KSh 1,499", "Sales at KSh 999", "Sales at KSh 2,499"],
    ["\u20a6200,000", "13", "19", "8"],
    ["\u20a6500,000", "32", "48", "20"],
    ["\u20a61,000,000", "65", "97", "39"],
    ["\u20a62,000,000", "129", "193", "78"],
], [PW * 0.28, PW * 0.24, PW * 0.24, PW * 0.24]))
story.append(Spacer(1, 2 * mm))
story.append(P("At KSh 1,499 selling to Kenya, Selar takes 5% + KSh 20 per sale. That is about "
               "KSh 95 per sale, so you keep roughly KSh 1,404 (\u20a614,530)."))
story.append(Spacer(1, 3 * mm))
story.append(P("The funnel maths that decides your ad budget", st_h2))
story.append(data_table([
    ["Step", "Realistic rate", "On 1,000 ad clicks"],
    ["Landing page view", "100%", "1,000"],
    ["Reads past the headline", "40%", "400"],
    ["Reaches the price", "15%", "150"],
    ["Starts checkout", "4%", "40"],
    ["Completes payment", "1.5\u20132.5%", "15\u201325"],
    ["Net after Selar fees", "\u2248 KSh 1,404 each", "\u2248 \u20a6218,000\u2013\u20a6363,000"],
], [PW * 0.34, PW * 0.28, PW * 0.38]))
story.append(Spacer(1, 2 * mm))
story.append(P("Those conversion rates are optimistic for a cold audience and an unknown "
               "brand. Assume the lower end. Then price the traffic: in Kenya, Meta traffic "
               "typically costs KSh 8\u201340 per click on a small budget, so 1,000 clicks is "
               "KSh 8,000\u2013KSh 40,000 \u2014 the entire budget or more, to produce maybe "
               "fifteen sales if everything works.", st_small))
story.append(Spacer(1, 2 * mm))
story.append(caution("So the honest conclusion", [
    P("Ads are not the growth engine at this budget. Ten to twenty sales in 30 days will come "
      "from people who already trust something: your own audience, your WhatsApp contacts, "
      "Kenyan creator partnerships, student groups. The \u20a640,000 is best spent proving "
      "which advert earns attention, not buying an audience you cannot afford yet.", st_small)
]))
story.append(PageBreak())

# ---------------------------------------------------------------- 3. funnel
hr("3 \u00b7 The funnel")
story += h1("Section 3", "Systeme.io + Selar, built today")
story.append(P("Two tools, two jobs. Do not make either one do the other\u2019s work in week one."))
story.append(Spacer(1, 1.5 * mm))
story.append(data_table([
    ["Layer", "Tool", "Why", "Free-plan ceiling"],
    ["Landing page", "Systeme.io", "Drag-and-drop, one page, no code",
     "3 funnels, 15 steps total"],
    ["Email capture + delivery", "Systeme.io", "Unlimited sends on the free plan",
     "2,000 contacts, 1 email campaign, 1 automation rule"],
    ["Course area (videos)", "Systeme.io", "Built-in course hosting",
     "1 course"],
    ["Checkout (KES + M-Pesa)", "Selar", "A Kenyan buyer can actually complete it",
     "Commission only: 5% + KSh 20"],
    ["Payouts", "Selar \u2192 your bank", "NGN in 1 business day, KES in 4",
     "\u2014"],
], [PW * 0.18, PW * 0.14, PW * 0.38, PW * 0.30]))
story.append(Spacer(1, 3 * mm))
story.append(P("Build order \u2014 four hours, today", st_h2))
story += numbered([
    "<b>Systeme.io account</b> (free, no card). Create one funnel: opt-in page \u2192 thank-you page \u2192 course area.",
    "<b>The lead magnet</b>: a 6-page PDF that solves one small problem \u2014 \u201cThe 5 Checks Before You Submit a Clip\u201d. This is what the ads and DMs point at, not the paid product.",
    "<b>The sales page</b>: headline, what it is, who it is for, what is inside, price, three FAQs, buy button.",
    "<b>Selar product</b>: upload the workbook + video access instructions, price at KSh 1,499, set the currency to KES.",
    "<b>Connect</b>: the Systeme.io buy button links to the Selar checkout; the Selar confirmation email sends access.",
    "<b>Test with a real Kenyan</b>: one friend or contact completes the purchase end to end with real money (refund them). Screenshot every step.",
])
story.append(Spacer(1, 2 * mm))
story.append(PageBreak())
story.append(P("The page that converts (copy this structure)", st_h2))
story.append(data_table([
    ["Order", "Section", "Example line"],
    ["1", "Headline", "Learn video clipping from zero \u2014 and find real work in 30 days."],
    ["2", "Sub-line", "A practical workbook for beginners in Kenya and Nigeria. No editing experience needed."],
    ["3", "What it is", "Six parts, 24 chapters, a 30-day log. Workbook + video walkthroughs."],
    ["4", "Who it is for", "Complete beginners, students, anyone who wants a digital skill that pays per clip."],
    ["5", "Proof of work", "Sample clips you cut. Your own page. Screenshots of the actual lessons."],
    ["6", "Price \u2014 and what it is not", "KSh 1,499, one payment. \u201cThis is not a get-rich scheme and I will not promise you an income.\u201d"],
    ["8", "FAQ + buy", "Do I need a laptop? Followers? How do I get paid? \u2192 then one button, KES, M-Pesa."],
], [PW * 0.10, PW * 0.17, PW * 0.73]))
story.append(Spacer(1, 2 * mm))
story.append(note("Do not put a fake discount on it", [
    P("\u201cWas KSh 5,000, now KSh 1,499\u201d on a brand-new product is the single most "
      "recognisable signal of a scam course in this market. Launch price is fine; pretend "
      "history is not.", st_small)
]))
story.append(PageBreak())

# ---------------------------------------------------------------- 4. ads
hr("4 \u00b7 Advertising")
story += h1("Section 4", "The three creatives, scripted")
story.append(P("Shoot all three on your phone, vertical, 15\u201325 seconds, your own voice or "
               "on-screen text. No stock footage with a voiceover \u2014 it reads as an ad and "
               "gets skipped."))
story.append(Spacer(1, 1.5 * mm))

def ad_block(letter, name, angle, lines, note_txt):
    story.append(P(f"Creative {letter} \u2014 {name}", st_h3))
    story.append(P(f"<i>{angle}</i>", S("ang", fontSize=8.6, leading=12, textColor=MUTED,
                                        spaceAfter=3)))
    rows = [["Time", "On screen", "Say / text"]]
    rows += lines
    story.append(data_table(rows, [PW * 0.10, PW * 0.34, PW * 0.56]))
    story.append(Spacer(1, 1 * mm))
    story.append(P(note_txt, st_small))
    story.append(Spacer(1, 3.5 * mm))

ad_block("A", "The demonstration", "Works because it shows the skill instead of describing it.", [
    ["0\u20133s", "Raw long video playing", "\u201cThis is three hours of footage.\u201d"],
    ["3\u201310s", "Speed up, cut to vertical clips, add hooks", "\u201cEight clips in one evening \u2014 the trick is the first two seconds.\u201d"],
    ["10\u201318s", "Your page, clips going live", "\u201cBrands pay per thousand views for this.\u201d"],
    ["18\u201325s", "The workbook on screen", "\u201cThe whole process is in one workbook. Link below.\u201d"],
], "Best first test. It proves you can do the thing you are teaching.")
ad_block("B", "The honesty angle", "Works because everyone else in this market is shouting a number.", [
    ["0\u20134s", "You, straight to camera", "\u201cI am not going to tell you that you will make a million naira.\u201d"],
    ["4\u201312s", "Screen: three numbers, then the real maths", "\u201cMost beginners earn nothing in month one. Here is what 100,000 views is worth.\u201d"],
    ["12\u201321s", "Workbook pages", "\u201cThe workbook I wish I had: the numbers, the traps, the steps.\u201d"],
    ["21\u201325s", "Call to action", "\u201cKSh 1,499. Link in bio.\u201d"],
], "The most likely to convert in Kenya and Nigeria, where scam-fatigue is high. Also the safest with platform ad policy.")
ad_block("C", "The student angle", "Works for cold audiences who do not know what clipping is.", [
    ["0\u20133s", "Text on dark", "\u201cA skill you can learn on your phone in 30 days.\u201d"],
    ["3\u201311s", "Explain clipping, show a clip being made", "\u201cBrands have long videos. They pay people to cut them into shorts.\u201d"],
    ["11\u201320s", "What the workbook covers", "\u201cFinding campaigns, reading the rules, getting paid.\u201d"],
    ["20\u201325s", "Call to action", "\u201cStart today. KSh 1,499.\u201d"],
], "Good top-of-funnel. Expect cheaper clicks and fewer sales than A or B.")

story.append(PageBreak())

# ---------------------------------------------------------------- 5. campaign
hr("5 \u00b7 Campaign settings")
story.append(P("Campaign settings \u2014 the exact setup", st_h2))
story.append(data_table([
    ["Setting", "Value", "Why"],
    ["Platform", "Meta (Facebook + Instagram)", "TikTok needs $50/day; Meta runs at KSh 500/day"],
    ["Objective", "Sales if the pixel works, else Traffic", "Traffic is honest on a tiny budget"],
    ["Countries", "Kenya (all), Nigeria excluded initially", "Kenyan checkout is proven; NGN testing splits the data"],
    ["Age", "18\u201345", "Below 18 cannot contract; above 45 converts poorly on this offer"],
    ["Interests", "Broad first. If too broad, add: video editing, freelancing, side hustle, CapCut",
     "Narrow audiences starve a small budget"],
    ["Placements", "Automatic, but exclude Audience Network", "Audience Network burns small budgets on junk clicks"],
    ["Budget", "KSh 500/day per ad set, 6 days", "\u2248 \u20a640,000 total across the test"],
    ["Ad sets", "3, one per creative", "One variable: the creative"],
    ["Optimisation", "Link clicks", "Purchases will not get enough events to optimise"],
    ["Schedule", "Run 6 days, do not touch days 1\u20132", "Early edits reset learning and waste the budget"],
], [PW * 0.19, PW * 0.44, PW * 0.37]))
story.append(Spacer(1, 3 * mm))
story.append(P("How to read the results on day 3", st_h2))
story.append(data_table([
    ["If you see", "It means", "Do this"],
    ["Cost per click above KSh 40", "Creative is not landing", "Change the first 2 seconds, not the targeting"],
    ["Clicks but no sales", "The page or the price is the problem", "Fix the page before spending more"],
    ["Sales at any rate", "You have a product", "Double the budget on that creative only"],
    ["Almost no impressions", "Budget too low or audience too narrow", "Broaden to all Kenya, 18\u201355"],
    ["Lots of clicks, no checks to price", "Headline promises something the page does not deliver", "Rewrite section 3 of the page"],
], [PW * 0.30, PW * 0.32, PW * 0.38]))
story.append(Spacer(1, 2 * mm))
story.append(warn("Ad policy \u2014 the three things that get rejected", [
    P("<b>Income claims.</b> \u201cMake \u20a6500,000 a month\u201d will be rejected or restricted. "
      "Say what the product teaches, not what it earns.<br/>"
      "<b>Before/after money imagery.</b> Screenshots of bank alerts and dashboards are treated "
      "as financial-promotion claims.<br/>"
      "<b>Personal attributes.</b> \u201cAre you broke?\u201d \u2014 addressing the viewer\u2019s "
      "financial situation directly is a policy violation on Meta.", st_small)
]))
story.append(PageBreak())

# ---------------------------------------------------------------- 6. calendar
hr("6 \u00b7 30-day calendar")
story += h1("Section 6", "Thirty days, in order")
story.append(P("Dates assume a launch today. Shift everything if the build slips \u2014 but do "
               "not compress week one, because the checkout test is the thing that decides "
               "whether the rest is real."))
story.append(Spacer(1, 1.5 * mm))
story.append(data_table([
    ["Days", "Focus", "Concrete output", "Money out"],
    ["1\u20132", "Build", "Systeme.io funnel, sales page, Selar product at KSh 1,499", "\u20a60"],
    ["3", "Checkout test", "One real Kenyan completes a purchase end to end", "\u20a60 (refunded)"],
    ["4\u20135", "Content", "Three ad creatives shot and edited; six organic posts scheduled", "\u20a60"],
    ["6\u20137", "Warm launch", "WhatsApp, X, Instagram, LinkedIn: \u201cI built this, first 20 get KSh 999\u201d", "\u20a60"],
    ["8\u201310", "Outreach", "20 DMs/day to Kenyan creators, student pages, digital-skill accounts", "\u20a60"],
    ["11\u201312", "Partnerships", "Offer 30\u201340% affiliate commission to 5 Kenyan creators via Selar", "\u20a60"],
    ["13\u201314", "Review", "Sales so far, page conversion rate, which message got replies", "\u20a60"],
    ["15\u201320", "Paid test", "Meta, KSh 500/day, 3 creatives, Kenya only", "\u20a640,000"],
    ["21\u201322", "Read the data", "Kill losing creatives, keep the winner, fix the page", "\u20a60"],
    ["23\u201326", "Scale or stop", "If profitable: raise the winner to KSh 1,000/day for 4 days. If not: stop ads, go back to outreach", "\u20a60\u2013\u20a640,000"],
    ["27\u201328", "Testimonials", "Ask every buyer for one sentence and permission to use it", "\u20a60"],
    ["29\u201330", "Decide", "Keep, kill, or reposition. Write it down", "\u20a60"],
], [PW * 0.10, PW * 0.16, PW * 0.54, PW * 0.20]))
story.append(Spacer(1, 3 * mm))
story.append(note("The date you must not miss", [
    P("Day 3. If a real Kenyan cannot complete checkout, nothing else in this calendar matters. "
      "Everything before day 3 exists to make day 3 possible; everything after it depends on "
      "day 3 being true.", st_small)
]))
story.append(PageBreak())

# ---------------------------------------------------------------- 7. risks
hr("7 \u00b7 Stop rules")
story += h1("Section 7", "When to stop, and what to do instead")
story.append(P("Write these down before you start, because in the middle of a launch "
               "everything feels like it is about to work."))
story.append(Spacer(1, 1.5 * mm))
story.append(data_table([
    ["Trigger", "What it means", "Decision"],
    ["No sale after 40 direct outreach messages", "The offer or the price is wrong, not the traffic",
     "Change the price to KSh 999 and rewrite the headline"],
    ["No sale after KSh 20,000 of ads", "Cold traffic does not want this at this price",
     "Stop ads. Keep the organic channel."],
    ["Clicks but under 0.5% reaching checkout", "The page is failing before the price",
     "Rewrite the page, do not touch the ads"],
    ["Buyers asking for refunds", "The product does not match the promise",
     "Fix the product, stop selling until you have"],
    ["Days 1\u201310 and nothing built", "You are not launching, you are planning",
     "Cut everything except: sales page, Selar link, 10 DMs a day"],
], [PW * 0.26, PW * 0.38, PW * 0.36]))
story.append(Spacer(1, 3 * mm))
story.append(P("Checklist before you spend the first naira", st_h3))
story += bullets([
    "A real Kenyan has completed checkout with real money and been refunded.",
    "The sales page states the price in KES and says what the product is not.",
    "The workbook PDF is finished, readable on a phone, and has no placeholder text.",
    "Three creatives exist, each under 25 seconds, none containing an income claim.",
    "The product is yours \u2014 not compiled from someone else\u2019s tutorials.",
    "You know your stop rules and have written them down.",
], st_small)
story.append(Spacer(1, 5 * mm))
story.append(P("Launch Plan \u00b7 Edition 1.0 \u00b7 October 2026 \u00b7 Internal operating document, "
               "not for sale. Rates are indicative: \u20a61,340 = $1, KSh1 = \u20a610.35. "
               "Verify live rates, platform minimums and payment terms before committing money.",
               S("foot", fontSize=7.8, leading=11.4, textColor=MUTED)))
story.append(PageBreak())

hr("8 \u00b7 What it returns")
story += h1("Section 8", "What this realistically returns")
story.append(P("Five outcomes, from nothing to the number you actually want. The probability "
               "column is a judgement, not a forecast — but it is the judgement this plan is "
               "built on."))
story.append(data_table([
    ["Scenario", "Sales", "Gross (KSh)", "In naira", "Probability"],
    ["Nothing sells", "0", "0", "\u20a60", "Common for a first launch"],
    ["Slow validation", "3\u20135", "4,500\u20137,500", "\u20a647,000\u2013\u20a678,000", "Plausible"],
    ["Working product", "10\u201315", "15,000\u201322,500", "\u20a6155,000\u2013\u20a6233,000", "Good outcome"],
    ["Strong launch", "30\u201340", "45,000\u201360,000", "\u20a6466,000\u2013\u20a6621,000", "Needs an audience or partners"],
    ["\u20a62,000,000 target", "129", "193,000", "\u20a62,000,000", "Not without paid reach far beyond \u20a640,000"],
], [PW * 0.24, PW * 0.11, PW * 0.20, PW * 0.23, PW * 0.22]))
story.append(Spacer(1, 3 * mm))
story.append(caution("The honest framing", [
    P("Ten sales in 30 days would be a successful first launch, and it is worth roughly "
      "\u20a6155,000 \u2014 not \u20a62 million. The value of the month is not the revenue. It "
      "is that after it you will know whether you have a product people buy, which is a "
      "question you cannot answer by reading anything, including this.", st_small)
]))
doc.build(story)
print("wrote", OUT)
