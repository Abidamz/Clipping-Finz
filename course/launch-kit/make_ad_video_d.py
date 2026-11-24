"""
Creative D: "direct response" - hard CTA, high urgency, no income claims.

Refused the "I made $1,000 in 30 days" version: it is an earnings claim with no
substantiation, which breaches TikTok ad policy and the honesty rule for this
product. This version keeps the aggression and swaps the fake proof for real,
checkable numbers (published platform rates).

1080x1920, 30fps, 22 seconds, silent (music added in the TikTok editor).
Deliberately faster cuts than A/B/C - this is the direct-response slot.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
FPS = 30
OUT = "/home/user/Clipping-Finz/course/launch-kit/ad-frames-d"
os.makedirs(OUT, exist_ok=True)

BG     = (11, 13, 18)
BG2    = (18, 22, 31)
WHITE  = (255, 255, 255)
ORANGE = (240, 135, 42)
RED    = (238, 90, 80)
TEAL   = (61, 220, 151)
DIM    = (93, 103, 121)
LIGHT  = (170, 180, 198)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def f(p, s):
    return ImageFont.truetype(p, s)

SCENES = [
    (0.0,  2.5, "stop",    ["STOP SCROLLING."]),
    (2.5,  6.5, "honest",  ["This will not", "pay for December."]),
    (6.5,  11.0, "proof",  ["But these numbers", "are public:"]),
    (11.0, 15.0, "rates",  ["$1 - $2.50", "per 1,000 views"]),
    (15.0, 18.5, "what",   ["33 pages.", "Minimums. Caps.", "Verification."]),
    (18.5, 22.0, "cta",    ["KSh 1,499.", "Link in bio."]),
]

TOTAL = int(SCENES[-1][1] * FPS)

def render(t):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    d.ellipse([W - 300, -220, W + 340, 420], fill=BG2)
    d.ellipse([-240, H - 360, 240, H + 140], fill=(15, 20, 28))

    # brand mark is smaller here - direct response wants the message, not the brand
    d.text((80, 92), "CLIPPING FROM ZERO", font=f(FB, 24), fill=(70, 78, 94))
    prog = t / SCENES[-1][1]
    d.rectangle([0, H - 8, int(W * prog), H], fill=ORANGE)

    for start, end, kind, lines in SCENES:
        if not (start <= t < end):
            continue
        alpha = min(1.0, max(0.0, (t - start) / 0.2))
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ld = ImageDraw.Draw(layer)

        if kind == "stop":
            # punch-in scale over the short beat
            local = (t - start) / (end - start)
            scale = 1.0 + 0.06 * min(1.0, local * 2)
            fo = f(FB, int(92 * scale))
            txt = lines[0]
            w = ld.textlength(txt, font=fo)
            y = 820
            # bars above and below
            ld.rectangle([80, y - 44, W - 80, y - 32], fill=RED + (255,))
            ld.text(((W - w) / 2, y), txt, font=fo, fill=WHITE + (255,))
            ld.rectangle([80, y + 118, W - 80, y + 130], fill=RED + (255,))

        elif kind == "honest":
            y = 760
            for i, ln in enumerate(lines):
                fo = f(FB, 66)
                w = ld.textlength(ln, font=fo)
                col = RED if i == 1 else WHITE
                ld.text(((W - w) / 2, y), ln, font=fo, fill=col + (255,))
                y += 96

        elif kind == "proof":
            y = 780
            for i, ln in enumerate(lines):
                fo = f(FR, 54)
                w = ld.textlength(ln, font=fo)
                ld.text(((W - w) / 2, y), ln, font=fo, fill=LIGHT + (255,))
                y += 82

        elif kind == "rates":
            y = 700
            fo = f(FB, 80)
            w = ld.textlength(lines[0], font=fo)
            ld.text(((W - w) / 2, y), lines[0], font=fo, fill=TEAL + (255,))
            y += 122
            fo2 = f(FR, 50)
            w = ld.textlength(lines[1], font=fo2)
            ld.text(((W - w) / 2, y), lines[1], font=fo2, fill=WHITE + (255,))
            y += 86
            # source note - substantiation made visible
            fo3 = f(FR, 32)
            src = "published platform rates"
            w = ld.textlength(src, font=fo3)
            ld.text(((W - w) / 2, y), src, font=fo3, fill=DIM + (255,))

        elif kind == "what":
            y = 680
            for i, ln in enumerate(lines):
                fo = f(FB, 62) if i == 0 else f(FR, 54)
                w = ld.textlength(ln, font=fo)
                col = WHITE if i == 0 else LIGHT
                ld.text(((W - w) / 2, y), ln, font=fo, fill=col + (255,))
                y += 100

        elif kind == "cta":
            y = 700
            fo = f(FB, 84)
            w = ld.textlength(lines[0], font=fo)
            ld.text(((W - w) / 2, y), lines[0], font=fo, fill=WHITE + (255,))
            y += 130
            pw, ph = 560, 108
            x0 = (W - pw) / 2
            ld.rounded_rectangle([x0, y, x0 + pw, y + ph], radius=54, fill=ORANGE)
            label = lines[1]
            lw = ld.textlength(label, font=f(FB, 46))
            ld.text(((W - lw) / 2, y + 30), label, font=f(FB, 46), fill=(11, 13, 18, 255))

        if alpha < 1.0:
            a = layer.split()[3].point(lambda v: int(v * alpha))
            layer.putalpha(a)
        img.paste(layer, (0, 0), layer)

    return img

for i in range(TOTAL):
    im = render(i / FPS)
    im.quantize(colors=64, method=Image.MEDIANCUT, dither=Image.NONE).save(
        os.path.join(OUT, f"f{i:05d}.png"), optimize=True)

print("frames:", TOTAL, "->", OUT)
