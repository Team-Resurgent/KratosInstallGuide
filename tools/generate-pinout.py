"""Build the annotated Kratos Main Board pinout diagram.

Reads the plain board artwork and writes a larger canvas with a pin table
callout beside each header, joined to the board by leader lines.

    py tools/generate-pinout.py

Connector boxes below are the bounding boxes of the header outlines in the
source artwork, in its own pixel coordinates.
"""

import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "images" / "pinout" / "mainboard.png"
HELPER = ROOT / "images" / "pinout" / "helper.png"
OUTPUT = ROOT / "images" / "pinout" / "mainboard-pinout.png"

FONT_PATH = "C:/Windows/Fonts/bahnschrift.ttf"
FALLBACK_REGULAR = "C:/Windows/Fonts/arial.ttf"
FALLBACK_BOLD = "C:/Windows/Fonts/arialbd.ttf"

# Crossover is the squared-off face used for the labels on the board artwork,
# so the callout headers match it. It is usually a per-user install.
CROSSOVER_CANDIDATES = (
    Path(__file__).resolve().parent / "fonts" / "CROSSOVER.ttf",
    Path(os.environ.get("LOCALAPPDATA", "")) / "Microsoft/Windows/Fonts/CROSSOVER.ttf",
    Path("C:/Windows/Fonts/CROSSOVER.ttf"),
)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (110, 110, 110)
ROW_TINT = (243, 243, 243)

BOX_W = 520
HEADER_H = 68
SUBTITLE_H = 40
ROW_H = 48
NUM_COL_W = 76
BORDER = 4
ELBOW_GAP = 60

BOARD_X = 120
BOARD_Y = 340
CANVAS_W = 2820
CANVAS_H = 1610

HELPER_H = 480
HELPER_MARGIN = 50

CONNECTORS = {
    "ADDON2": (513, 54, 593, 174),
    "ADDON1": (513, 187, 593, 307),
    "RGB1": (663, 351, 759, 431),
    "RGB2": (1824, 412, 1924, 497),
    "INPUT": (1930, 55, 2016, 152),
    "FRONT PANEL": (1940, 168, 2012, 494),
}

PINOUTS = {
    "ADDON2": ("TOP TO BOTTOM", ["IO (SPARE)", "RING RGB", "GND", "5V (SECONDARY)"]),
    "ADDON1": ("TOP TO BOTTOM", ["IR / SDA", "BUZZER / SCL", "GND", "5V (PRIMARY)"]),
    "RGB1": ("LEFT TO RIGHT", ["5V (SECONDARY)", "RGB LEFT", "GND"]),
    "RGB2": ("LEFT TO RIGHT", ["5V (SECONDARY)", "RGB RIGHT", "GND"]),
    "INPUT": ("TOP TO BOTTOM", ["SCL", "SDA", "5V (PRIMARY)"]),
    "FRONT PANEL": (
        "TOP TO BOTTOM",
        [
            "NOT CONNECTED",
            "NOT CONNECTED",
            "NOT CONNECTED",
            "LED RED LEFT",
            "LED GREEN LEFT",
            "EJECT",
            "GND",
            "POWER",
            "GND",
        ],
    ),
}

# Where each callout sits on the canvas, and which edge of its header the
# leader line points at. Boxes are placed clear of the board outline so no
# leader has to cross the artwork.
POWER_NOTE = (
    "POWER",
    [
        "5V PRIMARY POWERS THE ESP32-S3 AND ADDON1.",
        "5V SECONDARY POWERS RGB1, RGB2 AND ADDON2.",
        "THE 5V STDBY PAD ON THE BACK OF THE BOARD IS AN ALTERNATIVE 5V PRIMARY FEED.",
    ],
)
NOTE_LEFT = 1237
NOTE_TOP = 1260
NOTE_PAD = 20
NOTE_LINE_H = 40

LAYOUT = {
    "ADDON2": {"anchor": "top", "box": ("bottom_left", 413, 324), "from": "bottom_mid"},
    "INPUT": {"anchor": "top", "box": ("bottom_left", 1833, 324), "from": "bottom_mid"},
    "FRONT PANEL": {"anchor": "right", "box": ("mid_left", 2240, 671), "from": "left_mid"},
    "ADDON1": {"anchor": "bottom", "box": ("top_left", 140, 1260), "from": "top_mid"},
    "RGB1": {"anchor": "bottom", "box": ("top_left", 700, 1260), "from": "top_mid"},
    "RGB2": {"anchor": "bottom", "box": ("top_left", 1734, 1260), "from": "top_mid"},
}


def load_font(size, weight="Regular"):
    try:
        font = ImageFont.truetype(FONT_PATH, size)
        font.set_variation_by_name(weight)
        return font
    except Exception:
        path = FALLBACK_BOLD if weight in ("Bold", "SemiBold") else FALLBACK_REGULAR
        return ImageFont.truetype(path, size)


def crossover_path():
    for candidate in CROSSOVER_CANDIDATES:
        if candidate.is_file():
            return str(candidate)
    return None


def header_font(names, max_width, max_size=42):
    """Largest Crossover size at which every header name still fits its box."""
    path = crossover_path()
    if path is None:
        print("Crossover not found, falling back to Bahnschrift for headers")
        return load_font(max_size, "Bold")
    for size in range(max_size, 17, -1):
        font = ImageFont.truetype(path, size)
        if max(font.getlength(name) for name in names) <= max_width:
            return font
    return ImageFont.truetype(path, 18)


def draw_text_centred(draw, centre, text, font, fill):
    """Centre on the glyphs themselves.

    Pillow's "mm" anchor centres the font's full ascender-to-descender box, so
    all-caps text with no descenders ends up sitting high in its band.
    """
    x0, y0, x1, y1 = font.getbbox(text)
    cx, cy = centre
    draw.text(
        (cx - (x1 - x0) / 2 - x0, cy - (y1 - y0) / 2 - y0),
        text,
        font=font,
        fill=fill,
        anchor="la",
    )


def box_height(pin_count):
    return HEADER_H + SUBTITLE_H + pin_count * ROW_H


def anchor_point(name):
    x0, y0, x1, y1 = CONNECTORS[name]
    edge = LAYOUT[name]["anchor"]
    if edge == "top":
        point = ((x0 + x1) // 2, y0)
    elif edge == "bottom":
        point = ((x0 + x1) // 2, y1)
    elif edge == "right":
        point = (x1, (y0 + y1) // 2)
    else:
        point = (x0, (y0 + y1) // 2)
    return point[0] + BOARD_X, point[1] + BOARD_Y


def box_rect(name):
    height = box_height(len(PINOUTS[name][1]))
    origin, x, y = LAYOUT[name]["box"]
    if origin == "top_left":
        left, top = x, y
    elif origin == "bottom_left":
        left, top = x, y - height
    elif origin == "mid_left":
        left, top = x, y - height // 2
    else:
        raise ValueError(origin)
    return left, top, left + BOX_W, top + height


def leader_points(name, rect, end):
    """Route the leader orthogonally: out of the box, along, then into the header."""
    left, top, right, bottom = rect
    where = LAYOUT[name]["from"]
    mid_x = (left + right) // 2
    mid_y = (top + bottom) // 2

    if where == "bottom_mid":
        start = (mid_x, bottom)
        if start[0] == end[0]:
            return [start, end]
        elbow = bottom + ELBOW_GAP
        return [start, (start[0], elbow), (end[0], elbow), end]
    if where == "top_mid":
        start = (mid_x, top)
        if start[0] == end[0]:
            return [start, end]
        elbow = top - ELBOW_GAP
        return [start, (start[0], elbow), (end[0], elbow), end]
    if where == "left_mid":
        start = (left, mid_y)
        if start[1] == end[1]:
            return [start, end]
        elbow = left - ELBOW_GAP
        return [start, (elbow, start[1]), (elbow, end[1]), end]
    raise ValueError(where)


def draw_callout(draw, name, fonts):
    direction, pins = PINOUTS[name]
    left, top, right, bottom = box_rect(name)

    draw.rectangle((left, top, right, bottom), fill=WHITE, outline=BLACK, width=BORDER)
    draw.rectangle((left, top, right, top + HEADER_H), fill=BLACK)
    draw_text_centred(
        draw, ((left + right) // 2, top + HEADER_H // 2), name, fonts["header"], WHITE
    )

    subtitle_top = top + HEADER_H
    draw.text(
        ((left + right) // 2, subtitle_top + SUBTITLE_H // 2),
        f"PIN 1 FIRST, {direction}",
        font=fonts["subtitle"],
        fill=GREY,
        anchor="mm",
    )

    row_top = subtitle_top + SUBTITLE_H
    divider_x = left + NUM_COL_W
    draw.line((left + BORDER, row_top, right - BORDER, row_top), fill=BLACK, width=3)
    for index, pin in enumerate(pins):
        y = row_top + index * ROW_H
        if index % 2 == 1:
            draw.rectangle((left + BORDER, y, right - BORDER, y + ROW_H), fill=ROW_TINT)
        if index:
            draw.line((left + BORDER, y, right - BORDER, y), fill=(210, 210, 210), width=2)
        draw.text(
            (left + NUM_COL_W // 2, y + ROW_H // 2),
            str(index + 1),
            font=fonts["pin_num"],
            fill=BLACK,
            anchor="mm",
        )
        draw.text(
            (divider_x + 22, y + ROW_H // 2),
            pin,
            font=fonts["pin"],
            fill=GREY if pin == "NOT CONNECTED" else BLACK,
            anchor="lm",
        )

    draw.line((divider_x, row_top, divider_x, bottom - BORDER // 2), fill=BLACK, width=2)
    draw.rectangle((left, top, right, bottom), outline=BLACK, width=BORDER)


def wrap_text(text, font, max_width):
    lines = []
    line = ""
    for word in text.split():
        trial = f"{line} {word}".strip()
        if line and font.getlength(trial) > max_width:
            lines.append(line)
            line = word
        else:
            line = trial
    if line:
        lines.append(line)
    return lines


def draw_note(draw, fonts):
    title, paragraphs = POWER_NOTE
    left, top = NOTE_LEFT, NOTE_TOP
    right = left + BOX_W
    wrapped = [wrap_text(p, fonts["note"], BOX_W - NOTE_PAD * 2 - 12) for p in paragraphs]
    body_h = sum(len(p) * NOTE_LINE_H for p in wrapped) + (len(wrapped) - 1) * 14
    bottom = top + HEADER_H + NOTE_PAD * 2 + body_h

    draw.rectangle((left, top, right, bottom), fill=WHITE, outline=BLACK, width=BORDER)
    draw.rectangle((left, top, right, top + HEADER_H), fill=BLACK)
    draw_text_centred(
        draw, ((left + right) // 2, top + HEADER_H // 2), title, fonts["header"], WHITE
    )

    y = top + HEADER_H + NOTE_PAD
    for paragraph in wrapped:
        for line in paragraph:
            draw.text((left + NOTE_PAD, y), line, font=fonts["note"], fill=BLACK, anchor="la")
            y += NOTE_LINE_H
        y += 14
    draw.rectangle((left, top, right, bottom), outline=BLACK, width=BORDER)


def paste_helper(canvas):
    """Drop the manual's mascot into the empty bottom-right corner."""
    art = Image.open(HELPER).convert("L")
    width = round(art.width * HELPER_H / art.height)
    art = art.resize((width, HELPER_H), Image.LANCZOS)
    # The source art is small, so scaling up softens its outlines. Pulling the
    # midtones apart again restores a crisp edge without going fully jagged.
    art = art.point([0 if v < 100 else 255 if v > 180 else round((v - 100) * 255 / 80) for v in range(256)])
    canvas.paste(
        art.convert("RGB"),
        (CANVAS_W - HELPER_MARGIN - width, CANVAS_H - HELPER_MARGIN - HELPER_H),
    )


def main():
    board = Image.open(SOURCE).convert("RGBA")
    canvas = Image.new("RGB", (CANVAS_W, CANVAS_H), WHITE)
    canvas.paste(board, (BOARD_X, BOARD_Y), board)
    draw = ImageDraw.Draw(canvas)

    fonts = {
        "title": load_font(72, "Bold"),
        "strapline": load_font(34, "SemiLight"),
        "header": header_font(list(PINOUTS), BOX_W - 60),
        "subtitle": load_font(24, "SemiLight"),
        "pin_num": load_font(32, "Bold"),
        "pin": load_font(34, "Regular"),
    }

    draw.text((1383, 108), "KRATOS MAIN BOARD", font=fonts["title"], fill=BLACK, anchor="mm")
    draw.text((1383, 168), "CONNECTOR PINOUT REFERENCE", font=fonts["strapline"], fill=GREY, anchor="mm")

    for name in PINOUTS:
        rect = box_rect(name)
        end = anchor_point(name)
        draw.line(leader_points(name, rect, end), fill=BLACK, width=3, joint="curve")
        draw.ellipse((end[0] - 9, end[1] - 9, end[0] + 9, end[1] + 9), fill=BLACK)
        draw_callout(draw, name, fonts)

    paste_helper(canvas)

    # Line art with antialiasing needs only a handful of greys, so a palette
    # image keeps the file small without any visible loss.
    canvas.quantize(colors=64, method=Image.Quantize.MEDIANCUT).save(OUTPUT, optimize=True)
    print(f"wrote {OUTPUT} ({canvas.width}x{canvas.height})")


if __name__ == "__main__":
    main()
