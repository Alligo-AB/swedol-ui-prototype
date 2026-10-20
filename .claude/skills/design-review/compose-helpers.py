# Drawing helpers for design-review comparison images. Set SHOTS to the folder with the
# Figma exports and UAT screenshots, then write per-image sections using box/vbrace/panel/sheet/save.
from PIL import Image, ImageDraw, ImageFont
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SHOTS = os.path.expanduser('~/Desktop/design-review-shots')  # change per ticket
OUT = os.path.join(HERE, 'out')
os.makedirs(OUT, exist_ok=True)

RED = (217, 0, 0)
INK = (20, 20, 20)
MUTED = (90, 90, 90)
BG = (255, 255, 255)
FIG = (69, 94, 251)   # blue label for Figma
UAT = (217, 0, 0)     # red label for UAT


def font(size, bold=False):
    return ImageFont.truetype('/System/Library/Fonts/HelveticaNeue.ttc', size, index=1 if bold else 0)


def box(d, xy, label=None, color=RED, w=5, lab_pos='tl'):
    x0, y0, x1, y1 = xy
    d.rectangle(xy, outline=color, width=w)
    if label:
        f = font(34, True)
        tw = d.textlength(label, font=f)
        pad = 10
        if lab_pos == 'tl':
            lx, ly = x0, y0 - 52
        elif lab_pos == 'bl':
            lx, ly = x0, y1 + 8
        elif lab_pos == 'tr':
            lx, ly = x1 - tw - 2 * pad, y0 - 52
        elif lab_pos == 'r':
            lx, ly = x1 + 10, y0 + (y1 - y0) / 2 - 23
        else:  # br
            lx, ly = x1 - tw - 2 * pad, y1 + 8
        d.rectangle((lx, ly, lx + tw + 2 * pad, ly + 46), fill=color)
        d.text((lx + pad, ly + 5), label, font=f, fill=(255, 255, 255))


def vbrace(d, x, y0, y1, text, color=RED, left=False):
    d.line((x, y0, x, y1), fill=color, width=4)
    d.line((x - 12, y0, x + 12, y0), fill=color, width=4)
    d.line((x - 12, y1, x + 12, y1), fill=color, width=4)
    f = font(30, True)
    tx = x - 18 - d.textlength(text, font=f) if left else x + 18
    d.text((tx, (y0 + y1) / 2 - 18), text, font=f, fill=color)


def panel(img, title, color):
    """Add a title strip above an image."""
    f = font(40, True)
    strip = 70
    out = Image.new('RGB', (img.width, img.height + strip), BG)
    d = ImageDraw.Draw(out)
    d.rectangle((0, 0, 14, strip - 12), fill=color)
    d.text((28, 10), title, font=f, fill=INK)
    out.paste(img, (0, strip))
    return out


def sheet(header, sub, blocks, notes, width=None, gap=40):
    width = width or max(b.width for b in blocks)
    fh, fs, fn = font(52, True), font(32), font(32)
    # measure notes height
    lines = []
    tmp = ImageDraw.Draw(Image.new('RGB', (10, 10)))
    for tag, txt in notes:
        words, cur = txt.split(), ''
        wrapped = []
        for wd in words:
            t = (cur + ' ' + wd).strip()
            if tmp.textlength(t, font=fn) > width - 260:
                wrapped.append(cur)
                cur = wd
            else:
                cur = t
        wrapped.append(cur)
        lines.append((tag, wrapped))
    notes_h = sum(len(w) * 44 + 18 for _, w in lines) + 40
    total_h = 60 + 70 + 50 + sum(b.height + gap for b in blocks) + notes_h + 40
    out = Image.new('RGB', (width + 120, total_h), BG)
    d = ImageDraw.Draw(out)
    y = 50
    d.text((60, y), header, font=fh, fill=INK)
    y += 70
    d.text((60, y), sub, font=fs, fill=MUTED)
    y += 70
    for b in blocks:
        out.paste(b, (60, y))
        y += b.height + gap
    d.line((60, y, width + 60, y), fill=(220, 220, 220), width=2)
    y += 30
    ft = font(32, True)
    for tag, wrapped in lines:
        tw = d.textlength(tag, font=ft)
        d.rectangle((60, y, 60 + tw + 20, y + 44), fill=RED)
        d.text((70, y + 5), tag, font=ft, fill=(255, 255, 255))
        for i, ln in enumerate(wrapped):
            d.text((60 + 200, y + 5 + i * 44), ln, font=fn, fill=INK)
        y += len(wrapped) * 44 + 18
    return out


def save(img, name, max_w=1800):
    if img.width > max_w:
        img = img.resize((max_w, round(img.height * max_w / img.width)), Image.LANCZOS)
    p = os.path.join(OUT, name)
    img.save(p, optimize=True)
    print(p, img.size, os.path.getsize(p))
