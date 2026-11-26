"""Render a rotating view of the deterministic inner and outer balls."""

import argparse
from math import cos, log, pi, sin, sqrt, tau
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


BG = "#101c30"
TEXT = "#f6f8fc"
MUTED = "#c5d3ea"
TEAL = "#8be8df"
GOLD = "#ffd38f"


def project(point, yaw):
    x, y, z = point
    rx = x*cos(yaw) + z*sin(yaw)
    rz = z*cos(yaw) - x*sin(yaw)
    pitch = .28 + .12*sin(yaw)
    ry = y*cos(pitch) - rz*sin(pitch)
    depth = y*sin(pitch) + rz*cos(pitch)
    scale = 615/(4.2-depth)
    return 221 + scale*rx, 273 - scale*ry, depth


def wireframe(center, radius):
    for latitude in (-pi/3, -pi/6, 0, pi/6, pi/3):
        points = [
            (center+radius*cos(latitude)*cos(angle), radius*sin(latitude), radius*cos(latitude)*sin(angle))
            for angle in (tau*index/48 for index in range(49))
        ]
        yield from zip(points, points[1:])
    for meridian in (pi*index/6 for index in range(6)):
        points = [
            (center+radius*cos(angle)*cos(meridian), radius*sin(angle), radius*cos(angle)*sin(meridian))
            for angle in (tau*index/48 for index in range(49))
        ]
        yield from zip(points, points[1:])


def draw_frame(angle, fonts, geometry):
    title, label, value, body = fonts
    space = Image.new("RGB", (880, 580), BG)
    draw = ImageDraw.Draw(space)
    draw.text((27, 22), "Two balls bound the diameter", font=title, fill=TEXT)
    draw.line((28, 81, 852, 81), fill="#3c526f", width=2)

    lines = []
    for a, b, front, back in geometry:
        p, q = project(a, angle), project(b, angle)
        depth = (p[2]+q[2])/2
        lines.append((depth, p, q, front if depth>=0 else back))
    for depth, p, q, color in sorted(lines):
        draw.line((*p[:2], *q[:2]), fill=color, width=3 if depth>=0 else 2)

    gold_center = 1.5/sqrt(33+2*log(2)/3)
    for x, color in ((0, TEAL), (gold_center, GOLD)):
        px, py, _ = project((x,0,0), angle)
        draw.ellipse((px-7, py-7, px+7, py+7), fill=color, outline=BG, width=2)

    draw.rounded_rectangle((459, 104, 853, 444), radius=16, fill="#1a2b47")
    draw.text((480, 121), "n = 4, d = 1, L = 36", fill=TEXT, font=label)
    draw.text((480, 178), "Expected squared", fill=MUTED, font=body)
    draw.text((480, 214), "diameter", fill=MUTED, font=body)
    draw.line((480, 265, 829, 265), fill="#3c526f", width=2)
    draw.text((480, 292), "2–2 split", fill=TEXT, font=label)
    draw.text((829, 278), "≥120", fill=TEXT, font=value, anchor="ra")
    draw.text((480, 370), "1–3 split", fill=TEXT, font=label)
    draw.text((829, 356), "<104", fill=TEAL, font=value, anchor="ra")
    draw.ellipse((30,487,46,503), fill=TEAL)
    draw.text((61, 475), "Inner ball lies inside the confidence set.", font=body, fill=MUTED)
    draw.ellipse((30,536,46,552), fill=GOLD)
    draw.text((61, 524), "Outer ball uses the larger testing fold.", font=body, fill=MUTED)
    return space


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--regular-font", default="DejaVuSans.ttf")
    parser.add_argument("--bold-font", default="DejaVuSans-Bold.ttf")
    parser.add_argument("--output", type=Path, default=Path("visualization/cross-fit-balls.gif"))
    args = parser.parse_args()
    wide = sqrt(33+2*log(2)/3)
    inner = (sqrt(33)-1.5)/wide
    geometry = [
        (start, end, front, back)
        for center, radius, front, back in (
            (1.5/wide, 1, "#c89e67", "#705941"),
            (0, inner, "#6dbdb5", "#365e65"),
        )
        for start, end in wireframe(center, radius)
    ]
    fonts = tuple(
        ImageFont.truetype(font, size)
        for font, size in [(args.bold_font, 46), (args.bold_font, 34),
                           (args.bold_font, 55), (args.regular_font, 34)]
    )
    frames = [
        draw_frame(.50+tau*index/64, fonts, geometry).quantize(colors=120, method=2)
        for index in range(64)
    ]
    frames[0].save(args.output, save_all=True, append_images=frames[1:],
                   duration=92, loop=0, disposal=2, optimize=True)


if __name__ == "__main__":
    main()
