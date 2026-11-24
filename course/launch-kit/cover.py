"""
Cover pages for both PDFs. Drawn as vectors on a full-bleed page.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, Color
from reportlab.platypus import Flowable

BG      = HexColor("#0b0d12")
BG2     = HexColor("#12161f")
BG3     = HexColor("#0f141c")
WHITE   = HexColor("#ffffff")
MUTED   = HexColor("#8b95ad")
DIM     = HexColor("#5d6779")
ORANGE  = HexColor("#f0872a")
TEAL    = HexColor("#3ddc97")
BLUE    = HexColor("#5b8cff")


def _brand(c, x, y, text, color, size=8.2, space=2.4):
    c.saveState()
    c.setFillColor(color)
    c.setFont("DJB", size)
    t = c.beginText()
    t.setTextOrigin(x, y)
    t.setCharSpace(space)
    t.textOut(text.upper())
    c.drawText(t)
    c.restoreState()


def _mark(c, x, y, s=54, color=ORANGE, lw=4.2):
    """Play triangle, outline only."""
    c.saveState()
    c.setStrokeColor(color)
    c.setLineWidth(lw)
    c.setLineJoin(1)
    c.setLineCap(1)
    p = c.beginPath()
    p.moveTo(x, y)
    p.lineTo(x, y + s)
    p.lineTo(x + s * 0.86, y + s * 0.5)
    p.close()
    c.drawPath(p, stroke=1, fill=0)
    c.restoreState()


def _wrap(c, text, font, size, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if c.stringWidth(t, font, size) <= maxw:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines


class FullCover(Flowable):
    """Full-bleed cover. The frame must be the whole page, padding 0."""
    def __init__(self, kind="workbook"):
        Flowable.__init__(self)
        self.kind = kind
        self._w, self._h = A4

    def wrap(self, aw, ah):
        return (self._w, self._h)

    def draw(self):
        if self.kind == "workbook":
            self._workbook(self.canv, self._w, self._h)
        else:
            self._plan(self.canv, self._w, self._h)

    # ------------------------------------------------------------------ workbook
    def _workbook(self, c, W, H):
        c.setFillColor(BG)
        c.rect(0, 0, W, H, stroke=0, fill=1)

        # background geometry
        c.setFillColor(BG2)
        c.circle(W * 0.97, H * 0.90, 168, stroke=0, fill=1)
        c.setFillColor(BG3)
        c.circle(W * 0.02, H * 0.20, 118, stroke=0, fill=1)

        L = 56          # left margin
        R = W - 56

        # top line
        _brand(c, L, H - 62, "Clipping From Zero", TEAL, 8.4, 2.6)
        _brand(c, R - 76, H - 62, "Edition 1.0", DIM, 8, 2.2)

        # title
        c.setFillColor(WHITE)
        c.setFont("DJB", 58)
        c.drawString(L, H - 232, "CLIPPING")
        c.setFillColor(ORANGE)
        c.drawString(L, H - 296, "FROM ZERO")

        # rule
        c.setStrokeColor(ORANGE)
        c.setLineWidth(3)
        c.line(L, H - 330, L + 92, H - 330)

        # subtitle
        c.setFillColor(HexColor("#aab4c6"))
        c.setFont("DJ", 12.5)
        y = H - 364
        for ln in _wrap(c, "The beginner\u2019s workbook for turning long videos "
                           "into short-form work \u2014 and getting paid for it.",
                        "DJ", 12.5, 320):
            c.drawString(L, y, ln)
            y -= 18

        # what is inside
        c.setFillColor(DIM)
        c.setFont("DJ", 9.6)
        y -= 16
        for item in ["6 parts  \u00b7  24 chapters  \u00b7  a 30-day log",
                     "The honest numbers  \u00b7  the traps  \u00b7  the work"]:
            c.drawString(L, y, item)
            y -= 15

        # mark
        _mark(c, R - 104, H - 436, 58, ORANGE, 4.4)

        # inside index
        ix = L
        iy = H - 612
        _brand(c, ix, iy, "Inside", DIM, 7.6, 2.6)
        parts = [
            ("01", "The business, honestly"),
            ("02", "Finding real work"),
            ("03", "Cutting for a phone"),
            ("04", "Publishing and testing"),
            ("05", "Getting paid"),
            ("06", "The 30-day log"),
        ]
        col_w = (R - L) / 2
        for i, (num, label) in enumerate(parts):
            col = i // 3
            row = i % 3
            x = ix + col * col_w
            yy = iy - 24 - row * 21
            c.setFillColor(ORANGE)
            c.setFont("DJB", 8.2)
            c.drawString(x, yy, num)
            c.setFillColor(HexColor("#9aa5b8"))
            c.setFont("DJ", 10)
            c.drawString(x + 22, yy, label)

        # bottom band
        c.setStrokeColor(HexColor("#232a38"))
        c.setLineWidth(0.8)
        c.line(L, 118, R, 118)

        c.setFillColor(HexColor("#c8d0de"))
        c.setFont("DJB", 9)
        c.drawString(L, 96, "For readers in Nigeria and Kenya")
        c.setFillColor(DIM)
        c.setFont("DJ", 9)
        c.drawRightString(R, 96, "October 2026")
        c.setFont("DJ", 8.2)
        c.drawString(L, 78, "18+  \u00b7  phone-only is fine  \u00b7  no income is promised or implied")

    # ------------------------------------------------------------------ plan
    def _plan(self, c, W, H):
        c.setFillColor(BG)
        c.rect(0, 0, W, H, stroke=0, fill=1)

        c.setFillColor(BG2)
        c.circle(W * 0.99, H * 0.14, 176, stroke=0, fill=1)
        c.setFillColor(BG3)
        c.circle(W * 0.04, H * 0.94, 104, stroke=0, fill=1)

        L, R = 56, W - 56

        _brand(c, L, H - 62, "Operating Pack", ORANGE, 8.4, 2.6)
        _brand(c, R - 128, H - 62, "Internal \u00b7 not for sale", DIM, 8, 2.2)

        c.setFillColor(WHITE)
        c.setFont("DJB", 46)
        c.drawString(L, H - 236, "Selling")
        c.drawString(L, H - 288, "Clipping")
        c.drawString(L, H - 340, "From Zero")

        c.setStrokeColor(ORANGE)
        c.setLineWidth(3)
        c.line(L, H - 368, L + 92, H - 368)

        c.setFillColor(HexColor("#aab4c6"))
        c.setFont("DJ", 13)
        y = H - 400
        for ln in _wrap(c, "A 30-day launch plan: Kenya first, Nigeria second.",
                        "DJ", 13, 340):
            c.drawString(L, y, ln)
            y -= 19

        c.setFillColor(DIM)
        c.setFont("DJ", 9.6)
        y -= 14
        for item in ["Budget reality  \u00b7  the funnel  \u00b7  three ad scripts",
                     "Systeme.io + Selar  \u00b7  stop rules"]:
            c.drawString(L, y, item)
            y -= 15

        # the key line, boxed
        bx, by, bw, bh = L, 170, W - 2 * L, 64
        c.setFillColor(HexColor("#1a1508"))
        c.setStrokeColor(HexColor("#d98800"))
        c.setLineWidth(0.9)
        c.roundRect(bx, by, bw, bh, 3, stroke=1, fill=1)
        c.setFillColor(HexColor("#d98800"))
        c.rect(bx, by, 2.6, bh, stroke=0, fill=1)
        c.setFillColor(HexColor("#e8d9bd"))
        c.setFont("DJ", 9.2)
        c.drawString(bx + 14, by + 42, "TikTok Ads needs $50/day. \u20a640,000 is about $30.")
        c.drawString(bx + 14, by + 26, "That is less than one day \u2014 not four weeks.")
        c.setFillColor(HexColor("#a89572"))
        c.setFont("DJ", 8)
        c.drawString(bx + 14, by + 12, "Section 1 shows what the same money buys instead.")

        c.setStrokeColor(HexColor("#232a38"))
        c.setLineWidth(0.8)
        c.line(L, 118, R, 118)
        c.setFillColor(HexColor("#c8d0de"))
        c.setFont("DJB", 9)
        c.drawString(L, 96, "Prepared for the Clipping From Zero launch")
        c.setFillColor(DIM)
        c.setFont("DJ", 9)
        c.drawRightString(R, 96, "October 2026")
