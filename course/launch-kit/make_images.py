"""
Product images for the launch: a square listing image and a vertical promo image.
Same visual language as the PDF covers.
"""
import os
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FDIR = "/usr/share/fonts/truetype/dejavu"
pdfmetrics.registerFont(TTFont("DJ", os.path.join(FDIR, "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("DJB", os.path.join(FDIR, "DejaVuSans-Bold.ttf")))
from reportlab.lib.colors import HexColor

BG     = HexColor("#0b0d12")
BG2    = HexColor("#12161f")
BG3    = HexColor("#0f141c")
WHITE  = HexColor("#ffffff")
ORANGE = HexColor("#f0872a")
TEAL   = HexColor("#3ddc97")
DIM    = HexColor("#5d6779")
LIGHT  = HexColor("#aab4c6")

HERE = os.path.dirname(os.path.abspath(__file__))


def brand(c, x, y, text, color, size, space=2.6):
    c.saveState()
    c.setFillColor(color)
    c.setFont("DJB", size)
    t = c.beginText(); t.setTextOrigin(x, y); t.setCharSpace(space); t.textOut(text.upper())
    c.drawText(t)
    c.restoreState()


def mark(c, x, y, s, lw=9):
    c.saveState()
    c.setStrokeColor(ORANGE); c.setLineWidth(lw)
    c.setLineJoin(1); c.setLineCap(1)
    p = c.beginPath()
    p.moveTo(x, y); p.lineTo(x, y + s); p.lineTo(x + s * 0.86, y + s * 0.5); p.close()
    c.drawPath(p, stroke=1, fill=0)
    c.restoreState()


def square(path, W=1080, H=1080):
    path = path.replace(".png", ".pdf")
    c = canvas.Canvas(path, pagesize=(W, H))
    c.setFillColor(BG); c.rect(0, 0, W, H, stroke=0, fill=1)
    c.setFillColor(BG2); c.circle(W * 0.95, H * 0.88, 260, stroke=0, fill=1)
    c.setFillColor(BG3); c.circle(W * 0.04, H * 0.10, 180, stroke=0, fill=1)

    M = 86
    brand(c, M, H - 96, "Clipping From Zero", TEAL, 17)
    brand(c, W - M - 132, H - 96, "Workbook", DIM, 16)

    c.setFillColor(WHITE); c.setFont("DJB", 118)
    c.drawString(M, H - 300, "CLIPPING")
    c.setFillColor(ORANGE)
    c.drawString(M, H - 424, "FROM ZERO")

    c.setStrokeColor(ORANGE); c.setLineWidth(6)
    c.line(M, H - 470, M + 170, H - 470)

    c.setFillColor(LIGHT); c.setFont("DJ", 27)
    c.drawString(M, H - 528, "Turn long videos into short-form work")
    c.drawString(M, H - 566, "\u2014 and get paid for it.")

    mark(c, W - M - 150, H - 590, 112, 9)

    c.setStrokeColor(HexColor("#232a38")); c.setLineWidth(1.4)
    c.line(M, 178, W - M, 178)
    c.setFillColor(HexColor("#c8d0de")); c.setFont("DJB", 20)
    c.drawString(M, 140, "6 parts  \u00b7  24 chapters  \u00b7  30-day log")
    c.setFillColor(DIM); c.setFont("DJ", 18)
    c.drawString(M, 110, "Nigeria & Kenya  \u00b7  beginners  \u00b7  18+")
    c.drawRightString(W - M, 110, "October 2026")
    c.showPage(); c.save()


def story(path, W=1080, H=1920):
    path = path.replace(".png", ".pdf")
    c = canvas.Canvas(path, pagesize=(W, H))
    c.setFillColor(BG); c.rect(0, 0, W, H, stroke=0, fill=1)
    c.setFillColor(BG2); c.circle(W * 0.92, H * 0.80, 330, stroke=0, fill=1)
    c.setFillColor(BG3); c.circle(W * 0.06, H * 0.16, 240, stroke=0, fill=1)

    M = 90
    brand(c, M, H - 150, "Clipping From Zero", TEAL, 19)

    c.setFillColor(WHITE); c.setFont("DJB", 86)
    c.drawString(M, H - 400, "A skill you can")
    c.drawString(M, H - 494, "learn on your")
    c.setFillColor(ORANGE)
    c.drawString(M, H - 588, "phone in 30 days.")

    c.setStrokeColor(ORANGE); c.setLineWidth(7)
    c.line(M, H - 634, M + 190, H - 634)

    c.setFillColor(LIGHT); c.setFont("DJ", 30)
    body = ["Brands have long videos.", "They pay people to cut them",
            "into short clips.", "", "This is the workbook that", "teaches the whole process."]
    y = H - 710
    for ln in body:
        c.drawString(M, y, ln); y -= 46

    mark(c, M, H - 1250, 150, 10)

    c.setFillColor(HexColor("#232a38")); c.setLineWidth(1.4)
    c.line(M, 250, W - M, 250)
    c.setFillColor(WHITE); c.setFont("DJB", 40)
    c.drawString(M, 190, "Clipping From Zero")
    c.setFillColor(DIM); c.setFont("DJ", 26)
    c.drawString(M, 150, "Workbook  \u00b7  Nigeria & Kenya")
    c.showPage(); c.save()


if __name__ == "__main__":
    import pymupdf
    for name, fn in [("cover-square-1080", square), ("cover-story-1080x1920", story)]:
        pdf = os.path.join(HERE, name + ".pdf")
        fn(pdf)
        d = pymupdf.open(pdf)
        pix = d[0].get_pixmap(dpi=72)   # pdf is authored at final pixel size
        pix.save(os.path.join(HERE, name + ".png"))
        d.close()
        os.remove(pdf)
        print("wrote", name + ".png", pix.width, "x", pix.height)
