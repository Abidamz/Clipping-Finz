"""
Creative C: "the festival" - seasonal (December) angle, honest.

Targets the festive-season money hunt WITHOUT promising income. The angle is
anti-hype: December floods the feed with "make money for the festival" claims,
and this ad is the one telling the truth about payout thresholds and delays.

This creative IS seasonal by design - it is meant to expire. Creative B stays
evergreen; run this alongside it during December only.
1080x1920, 30fps, 28s, silent (music added in TikTok).
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
FPS = 30
OUT = "/home/user/Clipping-Finz/course/launch-kit/ad-frames-c"
os.makedirs(OUT, exist_ok=True)

BG     = (11, 13, 18)
BG2    = (18, 22, 31)
WHITE  = (255, 255, 255)
ORANGE = (240, 135, 42)
TEAL   = (61, 220, 151)
DIM    = (93, 103, 121)
LIGHT  = (170, 180, 198)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def f(p, s):
    return ImageFont.truetype(p, s)

SCENES = [
    (0.0,  4.5,  "hook",
     ["Looking for money", "before the festival?"]),
    (4.5,  9.0,  "big",
     ["Then be careful", "what you buy this month."]),
    (9.0,  15.5, "lines",
     ["Nobody pays you for watching clips.",
      "You are paid per 1,000 views -",
      "once you clear the minimum."]),
    (15.5, 21.0, "punch",
     ["Most platforms also settle", "weeks after that."]),
    (21.0, 25.0, "turn",
     ["So this is not December money.",
      "It is January money."]),
    (25.0, 28.0, "cta",
     ["Clipping From Zero", "33-page workbook"]),
]

TOTAL = int(SCENES[-1][1] * FPS)

def render(t):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    d.ellipse([W - 300, -220, W + 340, 420], fill=BG2)
    d.ellipse([-240, H - 360, 240, H + 140], fill=(15, 20, 28))

    d.text((80, 90), "CLIPPING FROM ZERO", font=f(FB, 26), fill=TEAL)
    d.text((80, 130), "A workbook, not a promise", font=f(FR, 24), fill=DIM)

    prog = t / SCENES[-1][1]
    d.rectangle([0, H - 8, int(W * prog), H], fill=ORANGE)

    for start, end, kind, lines in SCENES:
        if not (start <= t < end):
            continue
        alpha = min(1.0, max(0.0, (t - start) / 0.3))
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ld = ImageDraw.Draw(layer)

        if kind == "hook":
            y = 660
            fo = f(FB, 84)
            for i, ln in enumerate(lines):
                col = WHITE if i == 0 else ORANGE
                w = ld.textlength(ln, font=fo)
                ld.text(((W - w) / 2, y), ln, font=fo, fill=col + (255,))
                y += 108
            ld.rectangle([W / 2 - 120, y + 20, W / 2 + 120, y + 28], fill=ORANGE)

        elif kind == "big":
            y = 720
            fo = f(FB, 64)
            for i, ln in enumerate(lines):
                col = WHITE if i == 0 else TEAL
                w = ld.textlength(ln, font=fo)
                ld.text(((W - w) / 2, y), ln, font=fo, fill=col + (255,))
                y += 108

        elif kind == "lines":
            y = 700
            for i, ln in enumerate(lines):
                fo = f(FR, 52)
                col = WHITE if i == 0 else LIGHT
                w = ld.textlength(ln, font=fo)
                ld.text(((W - w) / 2, y), ln, font=fo, fill=col + (255,))
                y += 88
            ld.rectangle([W / 2 - 260, y + 10, W / 2 + 260, y + 14], fill=(60, 68, 84))

        elif kind == "punch":
            y = 760
            fo = f(FB, 64)
            for i, ln in enumerate(lines):
                col = WHITE if i == 0 else ORANGE
                w = ld.textlength(ln, font=fo)
                ld.text(((W - w) / 2, y), ln, font=fo, fill=col + (255,))
                y += 100

        elif kind == "turn":
            y = 680
            for i, ln in enumerate(lines):
                fo = f(FB, 66) if i == 1 else f(FR, 52)
                col = LIGHT if i == 0 else TEAL
                w = ld.textlength(ln, font=fo)
                ld.text(((W - w) / 2, y), ln, font=fo, fill=col + (255,))
                y += 92 if i == 0 else 110
            ld.rectangle([W / 2 - 130, y, W / 2 + 130, y + 8], fill=TEAL)

        elif kind == "cta":
            y = 700
            fo = f(FB, 80)
            w = ld.textlength(lines[0], font=fo)
            ld.text(((W - w) / 2, y), lines[0], font=fo, fill=WHITE + (255,))
            y += 104
            fo2 = f(FR, 44)
            w = ld.textlength(lines[1], font=fo2)
            ld.text(((W - w) / 2, y), lines[1], font=fo2, fill=LIGHT + (255,))
            y += 120
            pw, ph = 520, 96
            x0 = (W - pw) / 2
            ld.rounded_rectangle([x0, y, x0 + pw, y + ph], radius=48, fill=ORANGE)
            label = "Link in bio"
            lw = ld.textlength(label, font=f(FB, 40))
            ld.text(((W - lw) / 2, y + 26), label, font=f(FB, 40), fill=(11, 13, 18, 255))

        if alpha < 1.0:
            a = layer.split()[3].point(lambda v: int(v * alpha))
            layer.putalpha(a)
        img.paste(layer, (0, 0), layer)

    return img

for i in range(TOTAL):
    render(i / FPS).quantize(colors=64, method=Image.MEDIANCUT, dither=Image.NONE).save(
        os.path.join(OUT, f"f{i:05d}.png"), optimize=True)

print("frames:", TOTAL, "->", OUT)
