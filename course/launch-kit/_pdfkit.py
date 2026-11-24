"""
Clipping From Zero - PDF build engine.
Pure reportlab, DejaVu fonts (covers NGN/KES symbols), no external deps at runtime.
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, PageBreak, KeepTogether,
                                NextPageTemplate, Flowable)

# ---------------------------------------------------------------- fonts
FDIR = "/usr/share/fonts/truetype/dejavu"
pdfmetrics.registerFont(TTFont("DJ",   os.path.join(FDIR, "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("DJB",  os.path.join(FDIR, "DejaVuSans-Bold.ttf")))
pdfmetrics.registerFont(TTFont("DJM",  os.path.join(FDIR, "DejaVuSansMono.ttf")))
pdfmetrics.registerFont(TTFont("DJMB", os.path.join(FDIR, "DejaVuSansMono-Bold.ttf")))
pdfmetrics.registerFontFamily("DJ", normal="DJ", bold="DJB", italic="DJ", boldItalic="DJB")

# ---------------------------------------------------------------- palette
INK      = colors.HexColor("#12161f")
BODY     = colors.HexColor("#242a36")
MUTED    = colors.HexColor("#6b7484")
RULE     = colors.HexColor("#dfe3ea")
ACCENT   = colors.HexColor("#1f6feb")
ACCENT_D = colors.HexColor("#12407f")
WARN_BG  = colors.HexColor("#fff6e6")
WARN_BD  = colors.HexColor("#d98800")
BAD_BG   = colors.HexColor("#fdeeee")
BAD_BD   = colors.HexColor("#c0392b")
OK_BG    = colors.HexColor("#eaf6ef")
OK_BD    = colors.HexColor("#1a7f5a")
PANEL    = colors.HexColor("#f5f7fa")
WHITE    = colors.white

# ---------------------------------------------------------------- styles
def S(name, **kw):
    base = dict(fontName="DJ", fontSize=9.8, leading=14.5, textColor=BODY,
                spaceAfter=5, alignment=TA_LEFT)
    base.update(kw)
    return ParagraphStyle(name, **base)

st_h1      = S("h1", fontName="DJB", fontSize=21, leading=26, textColor=INK, spaceAfter=4)
st_kicker  = S("kicker", fontName="DJB", fontSize=8.5, leading=11, textColor=ACCENT,
               spaceAfter=3)
st_h2      = S("h2", fontName="DJB", fontSize=13, leading=17, textColor=INK,
               spaceBefore=9, spaceAfter=4)
st_h3      = S("h3", fontName="DJB", fontSize=10.2, leading=13.5, textColor=INK,
               spaceBefore=7, spaceAfter=3)
st_body    = S("body")
st_small   = S("small", fontSize=8.6, leading=12.4, textColor=MUTED)
st_caption = S("cap", fontSize=8.2, leading=11.5, textColor=MUTED, spaceBefore=2)
st_bullet  = S("bullet", leftIndent=11, firstLineIndent=-11, spaceAfter=4)
st_mono    = S("mono", fontName="DJM", fontSize=8.4, leading=12.6, textColor=INK)
st_quote   = S("quote", fontSize=10.5, leading=16, textColor=INK)
st_th      = S("th", fontName="DJB", fontSize=8.2, leading=11, textColor=MUTED)
st_td      = S("td", fontSize=8.8, leading=12.4)
st_tdb     = S("tdb", fontName="DJB", fontSize=8.8, leading=12.4, textColor=INK)

def P(t, s=st_body): return Paragraph(t, s)

def bullets(items, style=st_bullet, mark="\u2022"):
    return [Paragraph(f'{mark}&nbsp;&nbsp;{i}', style) for i in items]

def numbered(items):
    out = []
    for n, i in enumerate(items, 1):
        out.append(Paragraph(f'<b>{n}.</b>&nbsp;&nbsp;{i}',
                             S(f"num{n}", leftIndent=15, firstLineIndent=-15, spaceAfter=5)))
    return out

# ---------------------------------------------------------------- boxes
class Rule(Flowable):
    def __init__(self, width=None, thickness=0.7, color=RULE, space=6):
        Flowable.__init__(self); self.w = width; self.t = thickness
        self.c = color; self.space = space
    def wrap(self, aw, ah):
        self._w = self.w or aw
        return (self._w, self.t + self.space)
    def draw(self):
        self.canv.setStrokeColor(self.c); self.canv.setLineWidth(self.t)
        self.canv.line(0, self.space / 2, self._w, self.space / 2)

class Box(Flowable):
    """Coloured callout that wraps flowables."""
    def __init__(self, flows, bg=PANEL, border=None, pad=9, label=None,
                 label_color=None, width=None):
        Flowable.__init__(self)
        self.flows = flows; self.bg = bg; self.border = border
        self.pad = pad; self.label = label
        self.label_color = label_color or border or ACCENT
        self._w = width
    def wrap(self, aw, ah):
        self._w = self._w or aw
        inner = self._w - 2 * self.pad - (3 if self.border else 0)
        self._h = self.pad
        if self.label:
            self._h += 13
        self._heights = []
        for f in self.flows:
            w, h = f.wrap(inner, ah)
            self._heights.append(h)
            self._h += h
        self._h += self.pad
        return (self._w, self._h)
    def draw(self):
        c = self.canv
        x0, y0 = 0, 0
        h = self._h
        c.setFillColor(self.bg)
        c.setStrokeColor(self.border or self.bg)
        c.setLineWidth(0.8)
        c.roundRect(x0, y0, self._w, h, 3, stroke=1 if self.border else 0, fill=1)
        if self.border:
            c.setFillColor(self.border)
            c.rect(x0, y0, 2.6, h, stroke=0, fill=1)
        y = h - self.pad
        if self.label:
            c.setFillColor(self.label_color)
            c.setFont("DJB", 7.4)
            c.drawString(self.pad + 4, y - 8, self.label.upper())
            y -= 13
        inner_w = self._w - 2 * self.pad - 4
        for f, fh in zip(self.flows, self._heights):
            y -= fh
            f.drawOn(c, self.pad + 4, y)

def callout(title, paras, kind="note"):
    cfg = {"note": (PANEL, ACCENT),
           "warn": (WARN_BG, WARN_BD),
           "bad":  (BAD_BG, BAD_BD),
           "ok":   (OK_BG, OK_BD)}[kind]
    return Box(paras, bg=cfg[0], border=cfg[1], label=title)

def warn(t, ps): return callout(t, ps, "warn")
def caution(t, ps): return callout(t, ps, "bad")
def good(t, ps): return callout(t, ps, "ok")
def note(t, ps): return callout(t, ps, "note")

def data_table(rows, widths, header=True, zebra=True, align=None):
    data = []
    for r_i, row in enumerate(rows):
        out = []
        for c_i, cell in enumerate(row):
            if isinstance(cell, str):
                out.append(Paragraph(cell, st_th if (header and r_i == 0) else st_td))
            else:
                out.append(cell)
        data.append(out)
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0)
    cmds = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LINEBELOW", (0, 0), (-1, -1), 0.5, RULE),
    ]
    if header:
        cmds += [("LINEBELOW", (0, 0), (-1, 0), 0.9, INK),
                 ("BOTTOMPADDING", (0, 0), (-1, 0), 4)]
    if zebra:
        for i in range(1 if header else 0, len(data)):
            if (i % 2 == 0):
                cmds.append(("BACKGROUND", (0, i), (-1, i), colors.HexColor("#fafbfc")))
    t.setStyle(TableStyle(cmds))
    return t

# ---------------------------------------------------------------- doc template
class Doc(BaseDocTemplate):
    def __init__(self, path, title, footer_text="Launch Pack \u2014 Kenya & Nigeria, October 2026",
                 head_text="CLIPPING FROM ZERO", **kw):
        BaseDocTemplate.__init__(self, path, pagesize=A4,
                                 leftMargin=20 * mm, rightMargin=20 * mm,
                                 topMargin=19 * mm, bottomMargin=18 * mm,
                                 title=title, author="Nnamdi Abidamz",
                                 subject="Launching a digital product in Kenya and Nigeria",
                                 **kw)
        self.doc_title = title
        fw = self.width
        cover = Frame(self.leftMargin, self.bottomMargin, fw, self.height, id="cover",
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        body = Frame(self.leftMargin, self.bottomMargin, fw, self.height - 6 * mm, id="body",
                     leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([
            PageTemplate(id="cover", frames=[cover], onPage=self.cover_bg),
            PageTemplate(id="body", frames=[body], onPageEnd=self.decorate),
        ])
        self._section = ""
        self.footer_text = footer_text
        self.head_text = head_text
        self.marks = {}

    def cover_bg(self, c, d):
        pass

    def decorate(self, c, d):
        c.saveState()
        w, h = A4
        # header rule
        c.setStrokeColor(RULE); c.setLineWidth(0.6)
        c.line(self.leftMargin, h - 13 * mm, w - self.rightMargin, h - 13 * mm)
        c.setFont("DJ", 7.4); c.setFillColor(MUTED)
        c.drawString(self.leftMargin, h - 11.6 * mm, self.head_text)
        c.drawRightString(w - self.rightMargin, h - 11.6 * mm, self._section.upper())
        # footer
        c.setStrokeColor(RULE)
        c.line(self.leftMargin, 12 * mm, w - self.rightMargin, 12 * mm)
        c.setFont("DJ", 7.4); c.setFillColor(MUTED)
        c.drawString(self.leftMargin, 8.4 * mm, self.footer_text)
        c.drawRightString(w - self.rightMargin, 8.4 * mm, str(c.getPageNumber()))
        c.restoreState()

    def set_section(self, s):
        self._section = s


class Mark(Flowable):
    """Zero-height marker recording the page a chapter starts on."""
    def __init__(self, doc, name):
        Flowable.__init__(self); self.doc = doc; self.name = name
    def wrap(self, aw, ah):
        return (0, 0)
    def draw(self):
        self.doc.marks[self.name] = self.canv.getPageNumber()


class SetSection(Flowable):
    """Zero-height marker that sets the running header for the current page."""
    def __init__(self, doc, name):
        Flowable.__init__(self); self.doc = doc; self.name = name
    def wrap(self, aw, ah):
        return (0, 0)
    def draw(self):
        self.doc._section = self.name

# ---------------------------------------------------------------- cover
INK_BG = colors.HexColor("#0b0d12")
ACC_G  = colors.HexColor("#3ddc97")
ACC_B  = colors.HexColor("#5b8cff")

class CoverArt(Flowable):
    def __init__(self, title, sub, meta_lines, w, h):
        Flowable.__init__(self)
        self.title = title; self.sub = sub; self.meta = meta_lines
        self._w = w; self._h = h
    def wrap(self, aw, ah):
        return (self._w, self._h)
    def draw(self):
        c = self.canv
        w, h = self._w, self._h
        c.setFillColor(INK_BG)
        c.rect(0, 0, w, h + 40, stroke=0, fill=1)
        # accent geometry
        c.setFillColor(colors.HexColor("#12161f"))
        c.circle(w * 0.86, h * 0.80, 74, stroke=0, fill=1)
        c.setFillColor(colors.HexColor("#151a24"))
        c.circle(w * 0.10, h * 0.22, 58, stroke=0, fill=1)
        c.setStrokeColor(ACC_B); c.setLineWidth(1.1)
        c.line(0, h * 0.665, w, h * 0.665)
        c.setFillColor(ACC_G)
        c.setFont("DJB", 8.6)
        c.drawString(0, h * 0.685, "LAUNCH PACK  \u00b7  OCTOBER 2026")
        # title
        y = h * 0.60
        c.setFillColor(WHITE)
        sizes = [34, 30, 26, 22]
        lines = self.title
        for i, ln in enumerate(lines):
            c.setFont("DJB", sizes[min(i, len(sizes) - 1)])
            c.drawString(0, y, ln)
            y -= sizes[min(i, len(sizes) - 1)] * 1.16
        # subtitle
        y -= 6
        c.setFillColor(colors.HexColor("#9aa4b8"))
        c.setFont("DJ", 12.5)
        for ln in self.sub:
            c.drawString(0, y, ln)
            y -= 17
        # meta block bottom
        yy = 96
        c.setStrokeColor(colors.HexColor("#232a38")); c.setLineWidth(0.7)
        c.line(0, yy + 62, w, yy + 62)
        c.setFont("DJ", 8.2); c.setFillColor(colors.HexColor("#7c869c"))
        for ln in self.meta:
            c.drawString(0, yy + 48 - (self.meta.index(ln) * 13), ln)
        c.setFillColor(ACC_G)
        c.setFont("DJB", 7.8)
        c.drawString(0, yy - 8, "SELLABLE EDITION  \u00b7  V1.0")

# ---------------------------------------------------------------- helpers
def esc(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))

def h1(kicker, title):
    return [P(esc(kicker), st_kicker), P(esc(title), st_h1),
            Rule(thickness=1.6, color=ACCENT, space=9)]
