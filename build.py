#!/usr/bin/env python3
"""Candidate A — Hard Gate Broadsheet for news-image-20261127.
Fresh renderer written in this session. Pillow only, no network, no clock,
no randomness. Draws a 1024x1024 cream broadsheet of Friday 27 Nov 2026.
Run: python3 build.py  -> writes entry.png + entry-300px.png in this dir.
"""
import hashlib
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
W = H = 1024
CREAM = (246, 242, 233)
NAVY = (30, 41, 59)
RED = (185, 28, 28)
INK = (28, 25, 23)
GREY = (90, 88, 80)
LIGHT = (232, 226, 210)
GOLD = (180, 130, 29)
GREEN = (22, 101, 52)
AMBER = (146, 90, 0)

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_IT = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


class Sheet:
    """Canvas wrapper that tracks every text box and fails on overflow."""

    def __init__(self):
        self.img = Image.new("RGB", (W, H), CREAM)
        self.d = ImageDraw.Draw(self.img)
        self.boxes = []

    def text(self, xy, s, f, fill=INK, anchor="la"):
        self.d.text(xy, s, font=f, fill=fill, anchor=anchor)
        w = self.d.textlength(s, font=f)
        h = f.size
        x, y = xy
        if anchor.startswith("m"):
            x -= w / 2
        elif anchor.startswith("r"):
            x -= w
        if "m" in anchor[1:]:
            y -= h / 2
        self.boxes.append((x, y, w, h, s))
        return w

    def wrap(self, s, f, maxw):
        words = s.split()
        lines, cur = [], ""
        for wd in words:
            trial = (cur + " " + wd).strip()
            if self.d.textlength(trial, font=f) <= maxw:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = wd
        if cur:
            lines.append(cur)
        return lines

    def para(self, x, y, s, f, maxw, fill=INK, leading=None, anchor="la"):
        lh = leading or int(f.size * 1.22)
        yy = y
        for ln in self.wrap(s, f, maxw):
            self.text((x, yy), ln, f, fill=fill, anchor=anchor)
            yy += lh
        return yy

    def check(self):
        bad = [b for b in self.boxes if b[0] < 0 or b[1] < 0
               or b[0] + b[2] > W or b[1] + b[3] > H]
        assert not bad, "text outside canvas: %r" % (bad[:3],)
        return len(self.boxes)


def badge(sheet, x, y, kind):
    """Status pill; returns its width."""
    col = {"CONFIRMED": GREEN, "CLAIM": AMBER, "REPORTED": GREY}[kind]
    f = font(SANS_B, 9)
    w = sheet.d.textlength(kind, font=f) + 10
    sheet.d.rounded_rectangle([x, y, x + w, y + 14], radius=7,
                              fill=col, outline=INK, width=1)
    sheet.d.text((x + 5, y + 2), kind, font=f, fill=(255, 255, 255))
    sheet.boxes.append((x, y, w, 14, kind))
    return w


NUMBERS = [
    ("800,000+", "WITHOUT POWER\nUS STORM"),
    ("77,000", "UK NET MIGRATION\nLOWEST SINCE 1997"),
    ("7,000", "TONNES OF DIESEL\nABOARD MED EMRE"),
    ("4.3%", "US Q3 GDP GROWTH\nREVISED UP"),
    ("2", "SPACEX SHARES\nPER US CHILD"),
    ("2", "ITALIANS KILLED\nKUWAIT STRIKE"),
]

HEROES = [
    dict(n=1, tag="MIDDLE EAST", badge="CLAIM",
         head="Drone strike kills two Italians in Kuwait",
         body="Italy and Kuwait blame Iran for a drone hit on an air-defence station. Tehran denies any role.",
         art="drone"),
    dict(n=2, tag="NORTH AMERICA", badge="CONFIRMED",
         head="Thanksgiving storm cuts power to 800,000+",
         body="Nor'easter floods the East Coast; the 100th Macy's parade is postponed for the first time.",
         art="storm"),
    dict(n=3, tag="TECH / SPACE", badge="CONFIRMED",
         head="Musk: two SpaceX shares for every US child",
         body="One share from SpaceX, one from Musk personally — a pledge worth about $18 billion.",
         art="rocket"),
]

MINIS = [
    (4, "Gaza: Israel kills 9, Hamas weighs reply", "Deputy education minister among dead; 80 militants killed in a month, Netanyahu says.", "CONFIRMED"),
    (5, "UK net migration falls to 77,000", "Lowest since 1997 outside Covid; 738,000 arrived, 661,000 left in year to June.", "CONFIRMED"),
    (6, "Chess Game 3: 60-move draw", "Gukesh and Sindarov level at 1.5–1.5 in Geneva; rest day today, Game 4 Saturday.", "CONFIRMED"),
    (7, "Diesel tanker sinks off Ibiza", "Med Emre capsizes with up to 7,000 t aboard; one crew member dies.", "CONFIRMED"),
    (8, "Trump demands probe of 'fake' GDP", "Q3 growth revised up to 4.3% from 3.4%; president alleges pre-midterm manipulation.", "CONFIRMED"),
    (9, "Black Friday: sales seen +4.2%", "Holiday spending to top $1 trillion, NRF says; 82% of shoppers cut costs.", "CONFIRMED"),
    (10, "Depardieu to stand trial", "Paris court orders trial over alleged 2018 rape of actress Charlotte Arnould.", "CONFIRMED"),
    (11, "Zelensky: US 'too focused' on Mideast", "To BBC: Washington is not pushing Russia hard enough; Putin 'not a friend'.", "CONFIRMED"),
    (12, "Duterte ICC trial starts Monday", "Ex-Philippine leader, 81, faces 85 murder counts from his drug war, 2011–2018.", "CONFIRMED"),
    (13, "NZ: final election results today", "Official count due this afternoon; interim coalition held 67 of 131 seats.", "CONFIRMED"),
    (14, "Bangkok refinery blast injures 9", "Three critically hurt in explosion at Thai oil facility; toll disputed (7 vs 9).", "REPORTED"),
    (15, "India top court quashes release", "Supreme Court voids early release of ex-MP Anand Mohan.", "CONFIRMED"),
]

ALSO = [
    (16, "Europe stocks rally ~2% — DAX +2.08%, FTSE +1.75%"),
    (17, "Bank of Korea lifts rate 25bp to 3.25%"),
    (18, "Kenya: 2 wildlife officers guilty over missing fisherman"),
    (19, "Kenya schools: census shows facility gaps"),
    (20, "France far right tested by antisemitism claims"),
    (21, "Kim Jong Un vows permanent nuclear armament"),
    (22, "Spain: snap elections on Sunday — what's at stake"),
    (23, "Myanmar refuses parts of ICJ genocide ruling"),
    (24, "Cheaper HIV prevention jab reaches Africa"),
    (25, "UK train knifeman guilty of trying to murder 14"),
    (26, "Michigan State beats Arkansas 70–67 on Thanksgiving"),
    (27, "India–NZ 2nd Test starts in Christchurch today"),
    (28, "China's drones are reshaping Asia's militaries"),
    (29, "India GST cancellations go automatic from 1 Dec"),
    (30, "UK reservists contacted as threat level rises"),
    (31, "FIFA confirms cyberattack on personal data"),
    (32, "Brazil budget panel cuts $370m in spending"),
]

TICKS = [
    ("17:17", "Kuwait deaths\nconfirmed"),
    ("18:56", "Chess Game 3\ndraw reported"),
    ("20:58", "Kenya officers\nconvicted"),
    ("22:01", "Ibiza tanker\nreport"),
    ("22:33", "Kuwait update,\nIran denial"),
    ("00:02", "Europe roundup\npublished"),
    ("01:00", "EDITION\nCLOSED"),
]

# map pins: (num, lon, lat, dx, dy) label offset
PINS = [
    (1, 47, 29, 8, -6), (2, -74, 40, 8, -8), (3, -97, 26, 8, 4),
    (4, 34, 31, 8, 4), (5, -1, 52, 8, -8), (6, 6, 46, 8, -8),
    (7, 2, 39, 8, 6), (8, -77, 39, -22, -6), (9, -95, 37, -24, 8),
    (10, 2, 49, 8, -6), (11, 31, 50, 8, -6), (12, 121, 15, 8, -4),
    (13, 172, -41, -24, -4), (14, 100, 14, 8, -4), (15, 78, 21, 8, -4),
]

CONTINENTS = [
    # North America
    [(18, 62), (52, 78), (95, 84), (128, 66), (150, 58), (138, 44),
     (118, 34), (104, 26), (88, 30), (76, 42), (60, 52), (40, 58)],
    # South America
    [(88, 96), (112, 92), (132, 108), (142, 138), (128, 168), (108, 150),
     (96, 122)],
    # Europe
    [(158, 52), (178, 44), (196, 50), (200, 62), (186, 72), (166, 66)],
    # Africa
    [(162, 92), (186, 88), (206, 100), (212, 126), (196, 152), (180, 138),
     (168, 116)],
    # Asia
    [(204, 48), (240, 40), (282, 48), (296, 66), (276, 84), (252, 96),
     (232, 84), (214, 66)],
    # Australia
    [(262, 152), (288, 150), (292, 166), (268, 170), (258, 160)],
]


def draw_drone(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(58, 74, 96), outline=INK, width=2)
    d.ellipse([x + 8, y + 8, x + 44, y + 34], fill=(245, 197, 66), outline=INK, width=2)
    d.polygon([(x + 14, y + 21), (x + 38, y + 21), (x + 26, y + 44)], fill=(245, 197, 66), outline=INK)
    # drone quadcopter
    cx, cy = x + w - 62, y + 34
    d.rectangle([cx - 22, cy - 7, cx + 22, cy + 7], fill=(30, 41, 59), outline=INK, width=2)
    for sx in (-1, 1):
        d.ellipse([cx + sx * 30 - 9, cy - 20, cx + sx * 30 + 9, cy - 2], outline=INK, width=2)
        d.line([cx + sx * 22, cy, cx + sx * 30, cy - 10], fill=INK, width=2)
    d.line([cx, cy + 7, cx, cy + 26], fill=INK, width=2)
    # radar dish on a mast
    d.line([x + 40, y + h - 44, x + 40, y + h - 6], fill=INK, width=3)
    d.arc([x + 18, y + h - 52, x + 62, y + h - 30], 180, 360, fill=INK, width=3)
    d.line([x + 18, y + h - 41, x + 62, y + h - 41], fill=INK, width=2)
    d.rectangle([x + 30, y + h - 8, x + 50, y + h - 4], fill=(30, 41, 59), outline=INK, width=1)


def draw_storm(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(70, 88, 110), outline=INK, width=2)
    # cloud
    for cx, cy, r in [(x + 40, y + 26, 20), (x + 66, y + 18, 24), (x + 94, y + 28, 18)]:
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(226, 232, 240), outline=INK, width=2)
    # rain
    for i in range(7):
        rx = x + 16 + i * 14
        d.line([rx, y + 52, rx - 5, y + 70], fill=(190, 210, 230), width=2)
    # lightning
    d.polygon([(x + 120, y + 50), (x + 132, y + 50), (x + 124, y + 66),
               (x + 134, y + 66), (x + 116, y + 88), (x + 122, y + 68),
               (x + 114, y + 68)], fill=(245, 197, 66), outline=INK)
    # balloon
    bx, by = x + w - 78, y + 14
    d.ellipse([bx, by, bx + 56, by + 40], fill=(185, 28, 28), outline=INK, width=2)
    d.line([bx + 12, by + 40, bx + 20, by + 58], fill=INK, width=2)
    d.line([bx + 44, by + 40, bx + 36, by + 58], fill=INK, width=2)
    d.rectangle([bx + 16, by + 58, bx + 40, by + 68], fill=(180, 130, 29), outline=INK, width=2)


def draw_rocket(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(16, 24, 40), outline=INK, width=2)
    for sx, sy in [(x + 22, y + 16), (x + 60, y + 30), (x + 150, y + 14),
                   (x + 200, y + 44), (x + 250, y + 20)]:
        d.polygon([(sx, sy - 5), (sx + 2, sy), (sx, sy + 5), (sx - 2, sy)], fill=(255, 255, 255))
    # rocket
    rx, ry = x + w // 2 - 14, y + 10
    d.polygon([(rx + 14, ry), (rx + 26, ry + 22), (rx + 2, ry + 22)], fill=(185, 28, 28), outline=INK)
    d.rectangle([rx + 2, ry + 22, rx + 26, ry + 58], fill=(240, 240, 235), outline=INK, width=2)
    d.polygon([(rx + 2, ry + 44), (rx - 12, ry + 62), (rx + 2, ry + 58)], fill=(185, 28, 28), outline=INK)
    d.polygon([(rx + 26, ry + 44), (rx + 40, ry + 62), (rx + 26, ry + 58)], fill=(185, 28, 28), outline=INK)
    d.polygon([(rx + 10, ry + 58), (rx + 18, ry + 58), (rx + 22, ry + 76),
               (rx + 14, ry + 84), (rx + 6, ry + 76)], fill=(245, 197, 66), outline=INK)
    # coins: two shares
    for cx in (x + 26, x + w - 26):
        d.ellipse([cx - 13, y + h - 30, cx + 13, y + h - 4], fill=(245, 197, 66), outline=INK, width=2)
        d.text((cx, y + h - 28), "2", font=font(SANS_B, 14), fill=INK, anchor="ma")


def render():
    s = Sheet()
    d = s.d
    mx = 24
    # --- micro bar ---
    s.text((mx, 10), "THE WORLD IN ONE IMAGE  •  MAKE.FUN NEWS-IMAGE-20261127",
           font(SANS_B, 12), fill=NAVY)
    s.text((W - mx, 10), "EDITION CLOSED 01:00 UTC", font(SANS_B, 12),
           fill=RED, anchor="ra")
    d.line([mx, 30, W - mx, 30], fill=INK, width=2)
    # --- masthead ---
    s.text((W // 2, 36), "FRIDAY 27 NOVEMBER 2026", font(SERIF, 58),
           fill=NAVY, anchor="ma")
    s.text((W // 2, 100), "The world in one image — 32 stories · 8 regions · every one first reported today",
           font(SERIF_IT, 17), fill=RED, anchor="ma")
    d.line([mx, 126, W - mx, 126], fill=RED, width=3)
    # --- numbers strip ---
    y0, y1 = 134, 198
    d.rectangle([mx, y0, W - mx, y1], fill=NAVY, outline=INK, width=2)
    bw = (W - 2 * mx) / 6
    for i, (num, lab) in enumerate(NUMBERS):
        x = mx + i * bw
        if i:
            d.line([x, y0 + 6, x, y1 - 6], fill=(120, 130, 150), width=1)
        s.text((x + bw / 2, y0 + 6), num, font(SANS_B, 30), fill=(255, 255, 255), anchor="ma")
        yy = y0 + 40
        for ln in lab.split("\n"):
            s.text((x + bw / 2, yy), ln, font(SANS_B, 10), fill=(200, 210, 225), anchor="ma")
            yy += 12
    # --- timeline ---
    s.text((mx, 206), "THE DAY IN UTC — OVERNIGHT INTO FRIDAY 27 NOV",
           font(SANS_B, 11), fill=NAVY)
    ty = 226
    d.line([mx, ty, W - mx, ty], fill=INK, width=2)
    tw = (W - 2 * mx) / 7
    for i, (t, lab) in enumerate(TICKS):
        cx = mx + i * tw + tw / 2
        d.ellipse([cx - 5, ty - 5, cx + 5, ty + 5], fill=RED, outline=INK, width=1)
        s.text((cx, ty + 8), t, font(SANS_B, 11), fill=NAVY, anchor="ma")
        yy = ty + 22
        for ln in lab.split("\n"):
            s.text((cx, yy), ln, font(SANS, 9), fill=GREY, anchor="ma")
            yy += 11
    # --- heroes ---
    hy, hh = 272, 172
    hw = (W - 2 * mx - 2 * 10) / 3
    arts = {"drone": draw_drone, "storm": draw_storm, "rocket": draw_rocket}
    for i, h in enumerate(HEROES):
        x = mx + i * (hw + 10)
        d.rectangle([x, hy, x + hw, hy + hh], fill=(255, 255, 255), outline=INK, width=2)
        arts[h["art"]](d, x + 2, hy + 2, hw - 4, 80)
        s.text((x + 8, hy + 88), h["tag"], font(SANS_B, 10), fill=RED)
        badge(s, x + hw - 78, hy + 86, h["badge"])
        s.para(x + 8, hy + 104, h["head"], font(SANS_B, 15), hw - 16, fill=NAVY, leading=17)
        s.para(x + 8, hy + 138, h["body"], font(SANS, 11), hw - 16, fill=INK, leading=13)
        s.text((x + hw - 22, hy + 6), str(h["n"]), font(SERIF, 26), fill=(255, 255, 255))
    # --- minis (status shown by the colour of the number cell) ---
    my = 452
    mw = (W - 2 * mx - 3 * 8) / 4
    mh, mg = 62, 8
    status_fill = {"CONFIRMED": GREEN, "CLAIM": AMBER, "REPORTED": GREY}
    for idx, (n, head, body, st) in enumerate(MINIS):
        r, c = divmod(idx, 4)
        x = mx + c * (mw + mg)
        y = my + r * (mh + mg)
        d.rectangle([x, y, x + mw, y + mh], fill=(255, 255, 255), outline=INK, width=1)
        d.rectangle([x, y, x + 30, y + mh], fill=status_fill[st], outline=INK, width=1)
        s.text((x + 15, y + 16), str(n), font(SERIF, 24), fill=(255, 255, 255), anchor="ma")
        s.para(x + 36, y + 5, head, font(SANS_B, 12), mw - 42, fill=NAVY, leading=14)
        s.para(x + 36, y + 33, body, font(SANS, 10), mw - 42, fill=INK, leading=12)
    # --- map + ALSO ---
    by = 662
    mapw, maph = 300, 196
    d.rectangle([mx, by, mx + mapw, by + maph], fill=(214, 228, 238), outline=INK, width=2)
    s.text((mx + 8, by + 4), "WHERE IT HAPPENED", font(SANS_B, 11), fill=NAVY)
    ox, oy = mx + 6, by + 26
    for poly in CONTINENTS:
        pts = [(ox + px * 0.92, oy + py * 0.92) for px, py in poly]
        d.polygon(pts, fill=(196, 214, 190), outline=INK)
    for (n, lon, lat, dx, dy) in PINS:
        px = ox + (lon + 170) / 360 * 276
        py = oy + (75 - lat) / 130 * 158
        d.ellipse([px - 4, py - 4, px + 4, py + 4], fill=RED, outline=INK, width=1)
        s.text((px + dx, py + dy), str(n), font(SANS_B, 10), fill=NAVY, anchor="la")
    ax = mx + mapw + 14
    s.text((ax, by), "ALSO ON FRIDAY 27 NOVEMBER 2026  —  16–32",
           font(SANS_B, 11), fill=NAVY)
    colw = (W - mx - ax - 2 * 10) / 3
    for i, (n, txt) in enumerate(ALSO):
        c = i // 6
        r = i % 6
        x = ax + c * (colw + 10)
        y = by + 20 + r * 30
        s.text((x, y), "%d." % n, font(SANS_B, 11), fill=RED)
        s.para(x + 20, y, txt, font(SANS, 10), colw - 20, fill=INK, leading=12)
    # --- DATE CHECK ---
    dy = 866
    d.rectangle([mx, dy, W - mx, dy + 78], fill=(255, 251, 235), outline=RED, width=2)
    s.text((mx + 10, dy + 6), "DATE CHECK — DELIBERATELY LEFT OUT (NOT 27 NOV)",
           font(SANS_B, 11), fill=RED)
    left = ["Huawei convicted 10/12 — 25 Nov", "CIA & ODNI cyberattack — 25 Nov",
            "Cairo tanker fire, 31 dead — 26 Nov"]
    right = ["Houthi refinery claim — 25 Nov", "F1 Qatar feud — 25 Nov report",
             "Colombia 76-hostage siege — 25 Nov"]
    for i, t in enumerate(left):
        s.text((mx + 10, dy + 24 + i * 14), "×  " + t, font(SANS, 10), fill=INK)
    for i, t in enumerate(right):
        s.text((mx + 500, dy + 24 + i * 14), "×  " + t, font(SANS, 10), fill=INK)
    # --- footer ---
    fy = 952
    d.line([mx, fy, W - mx, fy], fill=INK, width=1)
    s.text((mx, fy + 6), "LEGEND:  mini number cell green = CONFIRMED (2+ sources)  •  amber = CLAIM (disputed)  •  grey = REPORTED (single roundup)",
           font(SANS_B, 10), fill=NAVY)
    s.para(mx, fy + 22, "Sources: Reuters · BBC · CNN · NYT · Times · USA Today · Chess.com · ONS · BEA · Nairobi News · Mint · TOI. Disputed: Kuwait attribution denied by Iran; Bangkok toll 9 vs 7; NZ special-vote count differs by source. NOT YET: NZ final results, Chess Game 4 (Sat), Duterte plea (Mon), Macy's parade (Sat).",
           font(SANS, 10), W - 2 * mx, fill=GREY, leading=13)
    s.text((W // 2, fy + 52), "FRIDAY 27 NOVEMBER 2026 — THE WORLD IN ONE IMAGE",
           font(SANS_B, 10), fill=NAVY, anchor="ma")
    n = s.check()
    print("boxes tracked: %d" % n)
    return s.img


def main():
    img = render()
    img.save(os.path.join(HERE, "entry.png"))
    small = img.resize((300, 300), Image.LANCZOS)
    small.save(os.path.join(HERE, "entry-300px.png"))
    h = hashlib.sha256(open(os.path.join(HERE, "entry.png"), "rb").read()).hexdigest()
    print("entry.png sha256: %s" % h)
    print("bytes: %d" % os.path.getsize(os.path.join(HERE, "entry.png")))


if __name__ == "__main__":
    main()
