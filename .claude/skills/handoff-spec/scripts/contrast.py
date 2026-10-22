#!/usr/bin/env python3
"""WCAG 2.2 AA contrast check for one text (or icon) color on one background.

Usage:
  python3 contrast.py <fg-hex> <bg-hex> --size <px> [--bold] [--opacity 0.6]
  python3 contrast.py <fg-hex> <bg-hex> --icon [--opacity 0.6]

Examples:
  python3 contrast.py #666666 #FFFFFF --size 14
  python3 contrast.py #222222 #FFFFFF --size 16 --opacity 0.6   (text in a group at 60% opacity)
  python3 contrast.py #FF4800 #FFFFFF --icon                   (icon or dot that carries meaning)
  python3 contrast.py #FFFFFF #FFFFFF --size 14 --opacity 0.6 --inner-bg #A8A8A8
      (text AND its own fill, both inside a 60% group, over a white page: e.g. an avatar letter)

Rules (WCAG 2.2 AA):
  text: 4.5:1, or 3:1 for large text (24px or more, or 18.66px or more and bold)
  --icon: 3:1 (non-text contrast, 1.4.11)
With --opacity, the color is blended over the background first.
With --inner-bg, the inner fill is also blended (same opacity) and becomes the background.
Prints one Markdown row: fg | bg | size | ratio | needs | result
"""
import sys


def expand(hex_color):
    h = hex_color.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        raise ValueError(f"not a 3 or 6 digit hex color: {hex_color}")
    return h


def luminance(hex_color):
    h = expand(hex_color)
    channels = []
    for i in (0, 2, 4):
        c = int(h[i:i + 2], 16) / 255
        channels.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    r, g, b = channels
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def blend(fg, bg, opacity):
    f, b = expand(fg), expand(bg)
    out = ""
    for i in (0, 2, 4):
        v = opacity * int(f[i:i + 2], 16) + (1 - opacity) * int(b[i:i + 2], 16)
        out += f"{round(v):02X}"
    return "#" + out


def ratio(fg, bg):
    a, b = luminance(fg), luminance(bg)
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


def take(args, flag, has_value=True):
    if flag not in args:
        return None
    i = args.index(flag)
    if has_value:
        value = args[i + 1]
        del args[i:i + 2]
        return value
    del args[i]
    return True


if __name__ == "__main__":
    args = sys.argv[1:]
    opacity = float(take(args, "--opacity") or 1)
    size = take(args, "--size")
    bold = bool(take(args, "--bold", has_value=False))
    icon = bool(take(args, "--icon", has_value=False))
    inner = take(args, "--inner-bg")
    if len(args) != 2 or not 0 < opacity <= 1 or (size is None and not icon):
        sys.exit(__doc__)
    fg, bg = args
    shown = fg
    if inner:
        page = bg
        bg = blend(inner, page, opacity)
        fg = blend(fg, page, opacity)
        shown = f"{args[0]} at {opacity:.0%} = {fg}"
        bg_shown = f"{inner} at {opacity:.0%} on {page} = {bg}"
    elif opacity < 1:
        fg = blend(fg, bg, opacity)
        shown = f"{args[0]} at {opacity:.0%} = {fg}"
    r = ratio(fg, bg)
    bg_shown = locals().get("bg_shown", bg)
    if icon:
        label, needs = "icon", 3.0
    else:
        px = float(size)
        large = px >= 24 or (bold and px >= 18.66)
        label = f"{px:g}px{' bold' if bold else ''}"
        needs = 3.0 if large else 4.5
    result = "pass" if r >= needs else "FAIL"
    print(f"| {shown} | {bg_shown} | {label} | {r:.2f}:1 | {needs:g}:1 | {result} |")
