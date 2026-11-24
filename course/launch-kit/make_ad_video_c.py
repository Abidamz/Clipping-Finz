"""
Creative C: "the December angle" - urgency without an income promise.

Targets people who need money now (festival season). The ad states plainly that
this will not produce December cash, then sells the thing it can honestly do:
get them competent by January.

1080x1920, 30fps, 30 seconds, silent (music added in the TikTok editor).
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

# (start, end, kind, lines)   kind: hook | truth | needs | gap | turn | cta
SCENES = [
    (0.0,  5.0,  "hook",
     ["Every December,", "everyone wants money."]),
    (5.0,  11.0, "truth",
     ["You cannot build", "a business in 7 days."]),
    (11.0, 17.0, "gap",
     ["So most people do", "the same three things.",
      "Borrow. Hustle. Regret."]),
    (17.0, 23.0, "turn",
     ["But you can learn how", "clipping actually pays", "by January."]),
    (23.0, 27.0, "needs",
     ["No followers.", "No camera.", "No permission."]),
    (27.0, 30.0, "cta",
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
            y = 640
            for i, ln in enumerate(lines):
                fo = f(FB, 70)
                col = WHITE if i == 0 else ORANGE
                w = ld.textlength(ln, font=fo)
                ld.text(((W - w) / 2, y), ln, font=fo, fill=col + (255,))
                y += 96
            ld.rectangle([W / 2 - 120, y + 16, W / 2 + 120, y + 24], fill=ORANGE)

        elif kind == "truth":
            y = 680
            for i, ln in enumerate(lines):
                fo = f(FB, 66)
                w = ld.textlength(ln, font=fo)
                ld.text(((W - w) / 2, y), ln, font=fo, fill=WHITE + (255,))
                y += 92

        elif kind == "gap":
            y = 620
            fo0 = f(FR, 54)
            w = ld.textlength(lines[0], font=fo0)
            ld.text(((W - w) / 2, y), lines[0], font=fo0, fill=LIGHT + (255,))
            y += 80
            w = ld.textlength(lines[1], font=fo0)
            ld.text(((W - w) / 2, y), lines[1], font=fo0, fill=LIGHT + (255,))
            y += 110
            # the three-word verdict, stacked
            for word in lines[2].rstrip(".").split(". "):
                fo = f(FB, 64)
                w = ld.textlength(word + ".", font=fo)
                ld.text(((W - w) / 2, y), word + ".", font=fo, fill=ORANGE + (255,))
                y += 92

        elif kind == "turn":
            y = 620
            styles = [(f(FR, 56), LIGHT), (f(FB, 62), TEAL), (f(FB, 66), ORANGE)]
            for i, ln in enumerate(lines):
                fo, col = styles[i]
                w = ld.textlength(ln, font=fo)
                ld.text(((W - w) / 2, y), ln, font=fo, fill=col + (255,))
                y += 100
            ld.rectangle([W / 2 - 110, y + 8, W / 2 + 110, y + 16], fill=TEAL)

        elif kind == "needs":
            y = 700
            fo = f(FB, 62)
            for ln in lines:
                w = ld.textlength(ln, font=fo)
                ld.text(((W - w) / 2, y), ln, font=fo, fill=WHITE + (255,))
                y += 104

        elif kind == "cta":
            y = 700
            fo = f(FB, 76)
            w = ld.textlength(lines[0], font=fo)
            ld.text(((W - w) / 2, y), lines[0], font=fo, fill=WHITE + (255,))
            y += 100
            fo2 = f(FR, 44)
            w = ld.textlength(lines[1], font=fo2)
            ld.text(((W - w) / 2, y), lines[1], font=fo2, fill=LIGHT + (255,))
            y += 116
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
    im.quantize(colors=64, method=Image.MEDIANCUT, dither=Image.NONE).save(
        os.path.join(OUT, f"f{i:05d}.png"), optimize=True)

print("frames:", TOTAL, "->", OUT)
