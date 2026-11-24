"""
Creative B: "the beginner" - for people who know nothing about clipping.

Same silent motion-graphic format as Creative A, so it uses in-app TikTok music.
1080x1920, 30fps, 28 seconds.

Honesty guardrail: the brief implies "make money before December". The ad never
promises income - it frames December as a *timeline to learn*, and explicitly
says it is not enough time to get rich.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
FPS = 30
OUT = "/home/user/Clipping-Finz/course/launch-kit/ad-frames-b"
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

# (start, end, kind, payload)
SCENES = [
    (0.0,  4.0,  "hook",
     ["You have never clipped", "anything.", "", "That is fine.", "Here is the honest version."]),
    (4.0,  9.0,  "needs",
     ["You do not need", "followers. Or a camera.", "Or permission."]),
    (9.0,  15.0, "steps",
     ["1  Find a video", "2  Cut the best 30s", "3  Post it with a link"]),
    (15.0, 20.0, "trap",
     ["The part nobody says:", "some platforms pay nothing", "under 100,000 views."]),
    (20.0, 25.0, "timeline",
     ["There is no perfect week.",
      "Learning takes weeks, not talent.",
      "Enough to start.",
      "Not enough to get rich."]),
    (25.0, 28.0, "cta",
     ["Clipping From Zero", "33-page workbook"]),
]

TOTAL = int(SCENES[-1][1] * FPS)

def centered(d, text, font, y, fill):
    w = d.textlength(text, font=font)
    d.text(((W - w) / 2, y), text, font=font, fill=fill)

def render(t):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # background
    d.ellipse([W - 300, -220, W + 340, 420], fill=BG2)
    d.ellipse([-240, H - 360, 240, H + 140], fill=(15, 20, 28))

    # persistent brand mark
    d.text((80, 90), "CLIPPING FROM ZERO", font=f(FB, 26), fill=TEAL)
    d.text((80, 130), "A workbook, not a promise", font=f(FR, 24), fill=DIM)

    # progress
    prog = t / SCENES[-1][1]
    d.rectangle([0, H - 8, int(W * prog), H], fill=ORANGE)

    for start, end, kind, lines in SCENES:
        if not (start <= t < end):
            continue
        alpha = min(1.0, max(0.0, (t - start) / 0.3))
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ld = ImageDraw.Draw(layer)

        if kind == "hook":
            y = 600
            for i, ln in enumerate(lines):
                if not ln:
                    y += 26
                    continue
                fo = f(FB, 78)
                col = (WHITE if i < 2 else ORANGE)
                w = ld.textlength(ln, font=fo)
                ld.text(((W - w) / 2, y), ln, font=fo, fill=col + (255,))
                y += 96

        elif kind == "needs":
            fo = f(FB, 60)
            y = 720
            for i, ln in enumerate(lines):
                w = ld.textlength(ln, font=fo)
                col = ORANGE if i == 0 else WHITE
                ld.text(((W - w) / 2, y), ln, font=fo, fill=col + (255,))
                y += 98

        elif kind == "steps":
            # numbered card list
            y = 620
            for i, ln in enumerate(lines):
                # circle
                cx, cy = 250, y + 34
                ld.ellipse([cx - 34, cy - 34, cx + 34, cy + 34], outline=ORANGE + (255,), width=4)
                num = ln[0]
                nw = ld.textlength(num, font=f(FB, 38))
                ld.text((cx - nw / 2, cy - 24), num, font=f(FB, 38), fill=ORANGE + (255,))
                txt = ln[2:]
                ld.text((310, y + 8), txt, font=f(FB, 52), fill=WHITE + (255,))
                y += 130

        elif kind == "trap":
            fo = f(FR, 54)
            y = 720
            for i, ln in enumerate(lines):
                w = ld.textlength(ln, font=fo)
                col = LIGHT if i == 0 else WHITE
                ld.text(((W - w) / 2, y), ln, font=fo, fill=col + (255,))
                y += 86
            # underline the punch
            pw = 260
            ld.rectangle([W / 2 - pw / 2, y - 6, W / 2 + pw / 2, y + 2], fill=ORANGE)

        elif kind == "timeline":
            y = 620
            styles = [(f(FB, 62), WHITE), (f(FB, 50), TEAL),
                      (f(FR, 56), ORANGE), (f(FR, 56), LIGHT)]
            for i, ln in enumerate(lines):
                fo, col = styles[min(i, len(styles) - 1)]
                w = ld.textlength(ln, font=fo)
                ld.text(((W - w) / 2, y), ln, font=fo, fill=col + (255,))
                y += 104 if i < 1 else 96
            ld.rectangle([W / 2 - 130, y + 4, W / 2 + 130, y + 12], fill=ORANGE)

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
    im = render(i / FPS)
    # palette-compress inline so the repo stays small
    im.quantize(colors=64, method=Image.MEDIANCUT, dither=Image.NONE).save(
        os.path.join(OUT, f"f{i:05d}.png"), optimize=True)

print("frames:", TOTAL, "->", OUT)
