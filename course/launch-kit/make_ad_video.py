"""
Builds a TikTok ad video as a numbered PNG frame sequence.

No ffmpeg on this box, so we emit frames + a ready-to-run PowerShell command
that encodes them on the user's PC (where ffmpeg is already installed).

Video: 1080x1920, 30fps, 24 seconds, Creative A ("the arithmetic").
"""
import os, math
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
FPS = 30
OUT = "/home/user/Clipping-Finz/course/launch-kit/ad-frames"
os.makedirs(OUT, exist_ok=True)

BG      = (11, 13, 18)
BG2     = (18, 22, 31)
WHITE   = (255, 255, 255)
ORANGE  = (240, 135, 42)
TEAL    = (61, 220, 151)
MUTED   = (139, 149, 173)
DIM     = (93, 103, 121)
LIGHT   = (170, 180, 198)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def f(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= maxw:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_center(d, text, font, y, fill, maxw=900):
    for ln in wrap(d, text, font, maxw):
        w = d.textlength(ln, font=font)
        d.text(((W - w) / 2, y), ln, font=font, fill=fill)
        y += font.size * 1.25
    return y

SCENES = [
    (0.0, 3.0, "big", "100,000 views\nis worth $200."),
    (3.0, 8.0, "body", "That is the whole business.\nYou are paid per thousand views."),
    (8.0, 14.0, "list", "Four numbers decide\nwhat you actually get:\n\nrate  ·  minimum\ncap  ·  verification"),
    (14.0, 19.0, "body", "Most beginners learn none of them.\nThen they wonder why nothing pays."),
    (19.0, 24.0, "cta", "Clipping From Zero\n33-page workbook"),
]

TOTAL = int(SCENES[-1][1] * FPS)

def render(t):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # background circles
    d.ellipse([W - 260, -180, W + 320, 400], fill=BG2)
    d.ellipse([-220, H - 320, 220, H + 120], fill=(15, 20, 28))

    # top brand line
    d.text((80, 90), "CLIPPING FROM ZERO", font=f(FB, 26), fill=TEAL)
    d.text((80, 130), "A workbook, not a promise", font=f(FR, 24), fill=DIM)

    # progress bar (subtle, keeps the eye moving)
    prog = t / SCENES[-1][1]
    d.rectangle([0, H - 8, int(W * prog), H], fill=ORANGE)

    for start, end, kind, text in SCENES:
        if start <= t < end:
            local = (t - start) / (end - start)
            # fade-in over first 0.25s
            alpha = min(1.0, (t - start) / 0.25) if (t - start) < 0.25 else 1.0
            layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            ld = ImageDraw.Draw(layer)

            if kind == "big":
                lines = text.split("\n")
                y = 620
                fonts = [f(FB, 88), f(FB, 96)]
                for i, ln in enumerate(lines):
                    fo = fonts[min(i, len(fonts) - 1)]
                    col = WHITE if i == 0 else ORANGE
                    w = ld.textlength(ln, font=fo)
                    ld.text(((W - w) / 2, y), ln, font=fo, fill=col + (255,))
                    y += fo.size * 1.18
                # underline
                ld.rectangle([W / 2 - 110, y + 24, W / 2 + 110, y + 32], fill=ORANGE)

            elif kind == "body":
                lines = text.split("\n")
                y = 780
                for ln in lines:
                    fo = f(FR, 52)
                    w = ld.textlength(ln, font=fo)
                    ld.text(((W - w) / 2, y), ln, font=fo, fill=WHITE + (255,))
                    y += 74

            elif kind == "list":
                parts = text.split("\n")
                y = 700
                for i, ln in enumerate(parts):
                    if not ln.strip():
                        y += 30
                        continue
                    fo = f(FB, 56) if i == 0 else f(FB, 50)
                    col = WHITE if i == 0 else ORANGE
                    w = ld.textlength(ln, font=fo)
                    ld.text(((W - w) / 2, y), ln, font=fo, fill=col + (255,))
                    y += 78 if i == 0 else 68

            elif kind == "cta":
                lines = text.split("\n")
                y = 700
                w = ld.textlength(lines[0], font=f(FB, 76))
                ld.text(((W - w) / 2, y), lines[0], font=f(FB, 76), fill=WHITE + (255,))
                y += 96
                w = ld.textlength(lines[1], font=f(FR, 44))
                ld.text(((W - w) / 2, y), lines[1], font=f(FR, 44), fill=LIGHT + (255,))
                y += 120
                # CTA pill
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
    render(i / FPS).save(os.path.join(OUT, f"f{i:05d}.png"))

print("frames:", TOTAL, "->", OUT)
