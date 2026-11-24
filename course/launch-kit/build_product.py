#!/usr/bin/env python3
"""
Builds: Clipping-From-Zero-Workbook.pdf  (the sellable product)
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _pdfkit import *   # noqa
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
import sec1, sec2, sec3, sec4, sec5, sec6

OUT = os.path.join(HERE, "Clipping-From-Zero-Workbook.pdf")
PW = A4[0] - 40 * mm

import json
MARKS_FILE = os.path.join(HERE, ".toc_marks.json")
try:
    PAGES = json.load(open(MARKS_FILE))
except Exception:
    PAGES = {}

def pg(key, default=""):
    return str(PAGES.get(key, default))

doc = Doc(OUT, "Clipping From Zero \u2014 The Beginner\u2019s Workbook",
          footer_text="Clipping From Zero  \u00b7  Edition 1.0  \u00b7  October 2026")
story = []

# ------------------------------------------------------------------ cover
story.append(Spacer(1, 12 * mm))
story.append(P("CLIPPING FROM ZERO", S("k", fontName="DJB", fontSize=9.5, leading=12,
                                      textColor=ACCENT, spaceAfter=4)))
story.append(Spacer(1, 4 * mm))
story.append(P("The Beginner\u2019s", S("t1", fontName="DJB", fontSize=32, leading=38, textColor=INK)))
story.append(P("Workbook", S("t2", fontName="DJB", fontSize=32, leading=38, textColor=INK)))
story.append(Spacer(1, 4 * mm))
story.append(P("Turning long videos into short-form work \u2014 and getting paid for it",
               S("t3", fontSize=12.5, leading=17, textColor=MUTED)))
story.append(Spacer(1, 7 * mm))
story.append(Rule(thickness=2, color=ACCENT, space=12))
story.append(Spacer(1, 2 * mm))
story.append(P("A workbook you work through, not a video you watch once. Six parts, "
               "twenty-four chapters, a 30-day log, and the honest numbers behind the "
               "opportunity.", S("lead", fontSize=11.5, leading=17.5)))
story.append(Spacer(1, 9 * mm))

story.append(data_table([
    ["What this is", "A structured course in clipping: the business, the work, the money, the traps."],
    ["Who it is for", "Complete beginners in Nigeria and Kenya, 18+. Phone-only is fine."],
    ["Time to read", "About 3 hours."],
    ["Time to work through", "30 days, 1\u20132 hours a day."],
    ["What it costs to start", "Nothing but data and time."],
    ["What it will not do", "Promise you an income. Nothing honestly can."],
], [PW * 0.28, PW * 0.72], header=False, zebra=False))
story.append(Spacer(1, 8 * mm))
story.append(warn("Read this before anything else", [
    P("Clipping pays per thousand views, and views are not guaranteed. Most people who start "
      "earn nothing in their first month. A meaningful number never get a single clip "
      "approved. This workbook teaches the skill, the opportunities and the traps \u2014 in "
      "detail \u2014 but it does not sell you an income, and you should be suspicious of "
      "anything that does.", st_small)
]))
story.append(Spacer(1, 6 * mm))
story.append(P("Edition 1.0  \u00b7  October 2026  \u00b7  Written for the Nigerian and Kenyan market",
               S("ed", fontSize=8.2, leading=11, textColor=MUTED)))
story.append(PageBreak())

# ------------------------------------------------------------------ contents
story.append(SetSection(doc, "Contents"))
story += h1("Contents", "What is inside")
toc = [
    ("1", "Understand the business before you spend a single hour", pg("c1.1")),
    ("", "1.1  What clipping actually is", ""),
    ("", "1.2  How the money works: views, rates, caps, verification", ""),
    ("", "1.3  The honest numbers for Kenya and Nigeria", ""),
    ("", "1.4  Four ways people earn from clipping", ""),
    ("", "1.5  What you need before day one", ""),
    ("2", "Find real work, not schemes", pg("c2.1")),
    ("", "2.1  The platforms that actually pay", ""),
    ("", "2.2  How to read a campaign brief", ""),
    ("", "2.3  Seven traps that eat beginners", ""),
    ("", "2.4  Client work: the income that does not depend on luck", ""),
    ("3", "Cut a clip that survives a phone screen", pg("c3.1")),
    ("", "3.1  The vertical crop", ""),
    ("", "3.2  Hooks: the first two seconds", ""),
    ("", "3.3  Captions, tags and disclosure", ""),
    ("", "3.4  The four-pass quality check", ""),
    ("4", "Publish, test, and repeat", pg("c4.1")),
    ("", "4.1  Setting up an account that is not throttled", ""),
    ("", "4.2  Posting schedule and platform order", ""),
    ("", "4.3  The split test that turns luck into a format", ""),
    ("", "4.4  When to kill an account", ""),
    ("5", "Get the money", pg("c5.1")),
    ("", "5.1  Submission, approval, and what you are actually paid", ""),
    ("", "5.2  Getting paid to a Nigerian or Kenyan bank", ""),
    ("", "5.3  Records, tax and keeping clean", ""),
    ("6", "The 30-day workbook", pg("c6")),
    ("", "Daily log, week reviews, and the day-30 decision page", ""),
]
rows = []
for num, title, page in toc:
    rows.append([
        P(f"<b>{num}</b>" if num else "", P("x", st_td).style if False else
          S("n", fontSize=9.4, leading=13, textColor=ACCENT, fontName="DJB")),
        P(f"<b>{esc(title)}</b>" if num else esc(title), st_td),
        P(page, S("pg", fontSize=8.8, leading=12.4, textColor=MUTED, alignment=2)),
    ])
t = Table(rows, colWidths=[11 * mm, PW - 26 * mm, 15 * mm])
t.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("TOPPADDING", (0, 0), (-1, -1), 3.2),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 3.2),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ("LINEBELOW", (0, 0), (-1, -1), 0.35, colors.HexColor("#eef1f5")),
]))
story.append(t)
story.append(Spacer(1, 7 * mm))
story.append(note("How to get value out of this", [
    P("Every chapter ends with a task. Do the task before moving on \u2014 reading this cover to "
      "cover without doing the work changes nothing at all. The tasks are small on purpose: "
      "fifteen minutes each, except the ones that require you to message a stranger.<br/><br/>"
      "The last part is a log with one line per day. Fill it in even when the day was a "
      "failure, especially when the day was a failure. In thirty days that log will tell you "
      "more about your chances than any advice you can read.", st_small)
]))
story.append(PageBreak())

# ------------------------------------------------------------------ parts
for mod in (sec1, sec2, sec3, sec4, sec5, sec6):
    mod.build(story, doc)

doc.build(story)
json.dump(doc.marks, open(MARKS_FILE, "w"), indent=1)
print("wrote", OUT, "| marks:", doc.marks)
