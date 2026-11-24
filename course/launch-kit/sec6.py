from _pdfkit import *   # noqa
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
PW = A4[0] - 40 * mm

def build(story, doc):
    story.append(PageBreak())
    story.append(Spacer(1, 40 * mm))
    story.append(P("PART SIX", S("p6d", fontName="DJB", fontSize=9, leading=12, textColor=ACCENT)))
    story.append(Spacer(1, 4 * mm))
    story.append(P("The 30-day<br/>workbook", S("p6t", fontName="DJB", fontSize=27, leading=33, textColor=INK)))
    story.append(Spacer(1, 7 * mm))
    story.append(Rule(thickness=1.4, color=ACCENT, space=12))
    story.append(P("Print these pages or fill them on your phone. One line a day. The point is "
                   "not neatness \u2014 it is that in thirty days you will have evidence about "
                   "your own work instead of a feeling about it.",
                   S("p6s", fontSize=11, leading=16.5)))
    story.append(PageBreak())

    story.append(SetSection(doc, "Part 6 \u00b7 The 30-day workbook"))
    story.append(Mark(doc, "c6"))
    story += h1("Weeks 1\u20132", "Log your first fourteen days")
    story.append(P("Day 1\u20135 are setup and warm-up. Days 6\u201314 are your first posting "
                   "block. Fill every line, including the zeros \u2014 especially the zeros.", st_small))
    story.append(Spacer(1, 2 * mm))

    rows = [["Day", "Clips posted", "Views at 24h", "Approved?", "What I noticed"]]
    for d in range(1, 15):
        label = f"{d}"
        if d <= 5:
            label = f"{d} (setup)"
        rows.append([P(label, st_td), "", "", "", ""])
    t = data_table(rows, [PW * 0.11, PW * 0.14, PW * 0.15, PW * 0.12, PW * 0.48])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 7.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7.5),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("LINEBELOW", (0, 0), (-1, -1), 0.5, RULE),
        ("LINEBELOW", (0, 0), (-1, 0), 0.9, INK),
    ]))
    story.append(t)
    story.append(Spacer(1, 4 * mm))
    story.append(P("End of week 1 \u2014 answer honestly", st_h3))
    story += bullets([
        "Did I post every day? If not, what was the actual reason?",
        "Which single clip did best, and what did its first two seconds look like?",
        "What did I abandon halfway through, and why?",
    ], st_small)
    story.append(PageBreak())

    story.append(Mark(doc, "c6b"))
    story += h1("Weeks 3\u20134", "Log the second half")
    story.append(P("By day 21 you should know your median views per clip. If you do not, you "
                   "have been posting without recording, which is the same as guessing.", st_small))
    story.append(Spacer(1, 2 * mm))
    rows = [["Day", "Clips posted", "Views at 24h", "Approved?", "What I noticed"]]
    for d in range(15, 31):
        rows.append([P(str(d), st_td), "", "", "", ""])
    t = data_table(rows, [PW * 0.11, PW * 0.14, PW * 0.15, PW * 0.12, PW * 0.48])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 6.2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6.2),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("LINEBELOW", (0, 0), (-1, -1), 0.5, RULE),
        ("LINEBELOW", (0, 0), (-1, 0), 0.9, INK),
    ]))
    story.append(t)
    story.append(PageBreak())

    story.append(Mark(doc, "c6c"))
    story += h1("Day 30 review", "The only page that decides what you do next")
    story.append(P("Fill this in with numbers, not impressions. It takes fifteen minutes and "
                   "it is the difference between a month of effort and a month of learning "
                   "something you can repeat."))
    story.append(Spacer(1, 2 * mm))
    rows = [
        ["Metric", "Number", "Notes"],
        ["Clips posted in total", "", ""],
        ["Campaign submissions approved", "", ""],
        ["Total views across all posts", "", ""],
        ["Median views per clip", "", ""],
        ["Best single clip", "", "What was different about the first two seconds?"],
        ["Campaign income received", "", "Actual money in, not accrued"],
        ["Client income received", "", ""],
        ["Total received", "", ""],
        ["Clips produced per hour", "", "Be honest \u2014 this sets your pricing"],
        ["Costs (data, ads, tools)", "", ""],
    ]
    t = data_table(rows, [PW * 0.34, PW * 0.17, PW * 0.49])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("LINEBELOW", (0, 0), (-1, -1), 0.5, RULE),
        ("LINEBELOW", (0, 0), (-1, 0), 0.9, INK),
    ]))
    story.append(t)
    story.append(Spacer(1, 4 * mm))
    story.append(P("Three questions", st_h3))
    story.append(P("<b>1.</b> What is the one thing that worked often enough to be repeatable?"))
    story.append(P("<b>2.</b> What did I spend money on, and would I spend it again?"))
    story.append(P("<b>3.</b> If I stopped today, what would I have that I could show someone? "
                   "(Clips, a page, a client list, a testimonial, a sample pack.)"))
    story.append(Spacer(1, 3 * mm))
    story.append(good("The honest conclusion", [
        P("If you have twenty-plus clips, a couple of approved submissions, and one client "
          "conversation, you have something rarer than a viral video: a repeatable process with "
          "evidence. If you have none of those, you also have something useful \u2014 a clear "
          "diagnosis of which of the six parts was never finished.", st_small)
    ]))
    story.append(PageBreak())

    # ------------------------------------------------ closing
    story.append(Spacer(1, 25 * mm))
    story.append(P("Before you close this", S("cl", fontName="DJB", fontSize=17, leading=23, textColor=INK)))
    story.append(Spacer(1, 4 * mm))
    story.append(P("Seven things worth remembering, in the order they will save you:", st_body))
    story.append(Spacer(1, 2 * mm))
    for i, t in enumerate([
        "Read the brief twice. Most rejections are reading failures.",
        "Post the moment it is ready, and submit the moment it is posted.",
        "Treat every payout as zero until it is in your account.",
        "Never buy views, and never fake a country.",
        "Median views matter more than any single viral clip.",
        "Client work does not depend on the algorithm. Ask for it from week two.",
        "Nobody who has real numbers needs to sell you a course about them.",
    ], 1):
        story.append(Paragraph(f'<b>{i}.</b>&nbsp;&nbsp;{t}', S(
            f"cl{i}", fontSize=10.4, leading=16.5, spaceAfter=7,
            leftIndent=14, firstLineIndent=-14)))
    story.append(Spacer(1, 12 * mm))
    story.append(Rule(thickness=1.2, color=ACCENT, space=10))
    story.append(P("Clipping From Zero \u00b7 Edition 1.0 \u00b7 October 2026",
                   S("cf", fontSize=8.4, leading=12, textColor=MUTED)))
    story.append(P("This workbook is an educational product. It does not guarantee income, and "
                   "nothing in it should be read as financial advice. Campaign rates, platform "
                   "rules and payment terms change; always check the live brief and the live "
                   "exchange rate before you commit time or money.",
                   S("cd", fontSize=8, leading=11.6, textColor=MUTED)))