"""Build the annotated Kratos pinout diagrams.

Reads the plain board artwork and writes a larger canvas with a pin table
callout beside each header, joined to the board by leader lines.

    py tools/generate-pinout.py

One entry in BOARDS describes each diagram. Connector boxes are the bounding
boxes of the header outlines in that board's source artwork, in its own pixel
coordinates. Everything else is shared, so all the diagrams look alike.
"""

import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
IMAGES = ROOT / "images" / "pinout"
HELPER = IMAGES / "helper.png"

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

NOTE_PAD = 20
NOTE_LINE_H = 40
CANVAS_BOTTOM_MARGIN = 54

HELPER_H = 480
HELPER_MARGIN = 50

MAIN_BOARD = {
    "source": IMAGES / "mainboard.png",
    "output": IMAGES / "mainboard-pinout.png",
    "title": "KRATOS MAIN BOARD",
    "strapline": "CONNECTOR PINOUT REFERENCE",
    "title_at": (1383, 108),
    "canvas": (2820, 1730),
    "origin": (120, 340),
    "mascot": True,
    "connectors": {
        "ADDON2": (513, 54, 593, 174),
        "ADDON1": (513, 187, 593, 307),
        "RGB1": (663, 351, 759, 431),
        "RGB2": (1824, 412, 1924, 497),
        "INPUT": (1930, 55, 2016, 152),
        "FRONT PANEL": (1940, 168, 2012, 494),
    },
    "pinouts": {
        "ADDON2": ("TOP TO BOTTOM", ["IO (SPARE)", "RING RGB", "GND", "5V"]),
        "ADDON1": ("TOP TO BOTTOM", ["IR / SDA", "BUZZER / SCL", "GND", "5V"]),
        "RGB1": ("LEFT TO RIGHT", ["5V", "RGB LEFT", "GND"]),
        "RGB2": ("LEFT TO RIGHT", ["5V", "RGB RIGHT", "GND"]),
        "INPUT": ("TOP TO BOTTOM", ["SCL", "SDA", "5V (NOT USED)"]),
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
    },
    # Where each callout sits on the canvas, and which edge of its header the
    # leader line points at. Boxes are placed clear of the board outline so no
    # leader has to cross the artwork.
    "layout": {
        "ADDON2": {"anchor": "top", "box": ("bottom_left", 413, 324), "from": "bottom_mid"},
        "INPUT": {"anchor": "top", "box": ("bottom_left", 1833, 324), "from": "bottom_mid"},
        "FRONT PANEL": {"anchor": "right", "box": ("mid_left", 2240, 671), "from": "left_mid"},
        "ADDON1": {"anchor": "bottom", "box": ("top_left", 60, 1260), "from": "top_mid"},
        "RGB1": {"anchor": "bottom", "box": ("top_left", 620, 1260), "from": "top_mid"},
        "RGB2": {"anchor": "bottom", "box": ("top_left", 1734, 1260), "from": "top_mid"},
    },
    "notes": [
        (
            "POWER",
            [
                "THE ESP32-S3 RUNS FROM A COMBINATION OF 5V, 5V STDBY AND USB-C.",
                "THE 5V PIN ON ADDON1 IS A COMBINATION OF 5V AND 5V STDBY.",
                "5V STDBY IS THE PAD ON THE BACK OF THE BOARD, USED TO KEEP KRATOS POWERED WITH THE CONSOLE OFF.",
                "THE 5V PIN ON INPUT IS LEFT UNCONNECTED IN THIS INSTALL. THE CONTROLLER PORTS SUPPLY THE 5V.",
            ],
            (1180, 1260),
        )
    ],
}

# Both controller boards use the same artwork geometry, mirrored: a 3-pin
# header in each top corner, a solder link beside each one, and the 5V ALT pad
# in the middle. Only which header is the input and which is the pass-through
# differs, so the two specs share this shape.
CONTROLLER_CONNECTORS = {
    "left_header": (223, 82, 305, 187),
    "right_header": (1746, 82, 1827, 184),
}
CONTROLLER_CANVAS = (2820, 1520)
CONTROLLER_ORIGIN = (380, 340)
# Two notes side by side, centred as a pair under the board.
CONTROLLER_NOTE_LEFT_AT = (780, 1180)
CONTROLLER_NOTE_RIGHT_AT = (1520, 1180)
LEFT_CORNER_BOX = ("bottom_left", 384, 324)
RIGHT_CORNER_BOX = ("bottom_left", 1906, 324)

# Pin 1 is the top pin on all four headers. The top-left corner header reads
# GND, RGB, 5V and the top-right one reads 5V, RGB, GND on both boards.
CORNER_PINS_LEFT = ("TOP TO BOTTOM", ["GND", "RGB", "5V"])
CORNER_PINS_RIGHT = ("TOP TO BOTTOM", ["5V", "RGB", "GND"])


def controller_board(side, input_header, supply_note, link_note):
    """Build a controller board spec. `input_header` is RGB1 or RGB2."""
    input_on_left = side == "RIGHT"
    return {
        "source": IMAGES / f"controller-{side.lower()}.png",
        "output": IMAGES / f"controller-{side.lower()}-pinout.png",
        "title": f"KRATOS {side} CONTROLLER BOARD",
        "title_size": 52,
        "strapline": "CONNECTOR PINOUT REFERENCE",
        "title_at": (1410, 108),
        "canvas": CONTROLLER_CANVAS,
        "origin": CONTROLLER_ORIGIN,
        "connectors": {
            input_header: CONTROLLER_CONNECTORS[
                "left_header" if input_on_left else "right_header"
            ],
            "OUT": CONTROLLER_CONNECTORS["right_header" if input_on_left else "left_header"],
        },
        "pinouts": {
            input_header: CORNER_PINS_LEFT if input_on_left else CORNER_PINS_RIGHT,
            "OUT": CORNER_PINS_RIGHT if input_on_left else CORNER_PINS_LEFT,
        },
        "layout": {
            input_header: {
                "anchor": "top",
                "box": LEFT_CORNER_BOX if input_on_left else RIGHT_CORNER_BOX,
                "from": "bottom_mid",
            },
            "OUT": {
                "anchor": "top",
                "box": RIGHT_CORNER_BOX if input_on_left else LEFT_CORNER_BOX,
                "from": "bottom_mid",
            },
        },
        "notes": [
            ("POWER", supply_note, CONTROLLER_NOTE_LEFT_AT),
            ("SOLDER LINKS", link_note, CONTROLLER_NOTE_RIGHT_AT),
        ],
    }


LEFT_BOARD = controller_board(
    "LEFT",
    "RGB1",
    ["THE LEFT BOARD HAS NO 5V SOURCE OF ITS OWN. IT RUNS ON THE 5V ARRIVING FROM THE RIGHT BOARD."],
    [
        "THERE IS ONE BESIDE EACH HEADER.",
        "BRIDGE THE LINK BESIDE RGB1 AND LEAVE THE ONE BESIDE OUT ALONE.",
    ],
)

RIGHT_BOARD = controller_board(
    "RIGHT",
    "RGB2",
    ["SOLDER THE 5V FEED FROM THE PORT 4 CONTROLLER PORT BOARD TO THE 5V ALT PAD."],
    [
        "THERE IS ONE BESIDE EACH HEADER.",
        "BRIDGE THE LINK BESIDE RGB2 AND LEAVE THE ONE BESIDE OUT ALONE.",
    ],
)

BOARDS = [MAIN_BOARD, LEFT_BOARD, RIGHT_BOARD]


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


def is_unused(pin):
    """Pins with nothing on them are greyed so the live ones stand out."""
    return pin == "NOT CONNECTED" or pin.endswith("(NOT USED)")


def box_height(pin_count):
    return HEADER_H + SUBTITLE_H + pin_count * ROW_H


def anchor_point(board, name):
    x0, y0, x1, y1 = board["connectors"][name]
    edge = board["layout"][name]["anchor"]
    if edge == "top":
        point = ((x0 + x1) // 2, y0)
    elif edge == "bottom":
        point = ((x0 + x1) // 2, y1)
    elif edge == "right":
        point = (x1, (y0 + y1) // 2)
    else:
        point = (x0, (y0 + y1) // 2)
    origin_x, origin_y = board["origin"]
    return point[0] + origin_x, point[1] + origin_y


def box_rect(board, name):
    height = box_height(len(board["pinouts"][name][1]))
    origin, x, y = board["layout"][name]["box"]
    if origin == "top_left":
        left, top = x, y
    elif origin == "bottom_left":
        left, top = x, y - height
    elif origin == "mid_left":
        left, top = x, y - height // 2
    else:
        raise ValueError(origin)
    return left, top, left + BOX_W, top + height


def leader_points(board, name, rect, end):
    """Route the leader orthogonally: out of the box, along, then into the header."""
    left, top, right, bottom = rect
    where = board["layout"][name]["from"]
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


def draw_callout(draw, board, name, fonts):
    direction, pins = board["pinouts"][name]
    left, top, right, bottom = box_rect(board, name)

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
            fill=GREY if is_unused(pin) else BLACK,
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


def note_layout(note, fonts):
    """Wrapped body text and the box it needs, so the canvas can be sized to fit."""
    _, paragraphs, (left, top) = note
    wrapped = [wrap_text(p, fonts["note"], BOX_W - NOTE_PAD * 2 - 12) for p in paragraphs]
    body_h = sum(len(p) * NOTE_LINE_H for p in wrapped) + (len(wrapped) - 1) * 14
    bottom = top + HEADER_H + NOTE_PAD * 2 + body_h
    return (left, top, left + BOX_W, bottom), wrapped


def draw_note(draw, note, fonts):
    title, _, _ = note
    (left, top, right, bottom), wrapped = note_layout(note, fonts)

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
        (canvas.width - HELPER_MARGIN - width, canvas.height - HELPER_MARGIN - HELPER_H),
    )


def build_fonts():
    """One set of fonts for every diagram, so the sheets match each other."""
    names = [name for board in BOARDS for name in board["pinouts"]]
    names += [note[0] for board in BOARDS for note in board.get("notes", ())]
    return {
        "strapline": load_font(34, "SemiLight"),
        "header": header_font(names, BOX_W - 60),
        "subtitle": load_font(24, "SemiLight"),
        "pin_num": load_font(32, "Bold"),
        "pin": load_font(34, "Regular"),
        "note": load_font(30, "Regular"),
    }


def render(board, fonts):
    art = Image.open(board["source"]).convert("RGBA")
    # The declared canvas is a minimum: note boxes grow with their text, so the
    # sheet grows with them rather than clipping.
    width, height = board["canvas"]
    for note in board.get("notes", ()):
        (_, _, _, note_bottom), _ = note_layout(note, fonts)
        height = max(height, note_bottom + CANVAS_BOTTOM_MARGIN)
    canvas = Image.new("RGB", (width, height), WHITE)
    canvas.paste(art, board["origin"], art)
    draw = ImageDraw.Draw(canvas)

    title_x, title_y = board["title_at"]
    title_font = load_font(board.get("title_size", 72), "Bold")
    draw.text((title_x, title_y), board["title"], font=title_font, fill=BLACK, anchor="mm")
    draw.text(
        (title_x, title_y + 60), board["strapline"], font=fonts["strapline"], fill=GREY, anchor="mm"
    )

    for name in board["pinouts"]:
        rect = box_rect(board, name)
        end = anchor_point(board, name)
        draw.line(leader_points(board, name, rect, end), fill=BLACK, width=3, joint="curve")
        draw.ellipse((end[0] - 9, end[1] - 9, end[0] + 9, end[1] + 9), fill=BLACK)
        draw_callout(draw, board, name, fonts)

    for note in board.get("notes", ()):
        draw_note(draw, note, fonts)
    if board.get("mascot"):
        paste_helper(canvas)

    # Line art with antialiasing needs only a handful of greys, so a palette
    # image keeps the file small without any visible loss.
    canvas.quantize(colors=64, method=Image.Quantize.MEDIANCUT).save(
        board["output"], optimize=True
    )
    print(f"wrote {board['output']} ({canvas.width}x{canvas.height})")


def main():
    fonts = build_fonts()
    for board in BOARDS:
        render(board, fonts)


if __name__ == "__main__":
    main()
