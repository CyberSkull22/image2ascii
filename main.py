#!/usr/bin/env python3
"""Terminal Image to ASCII converter.

Usage examples:
  python main.py input.jpg
  python main.py input.jpg -w 160 -o ascii.txt
  python main.py input.jpg --charset " .:-=+*#%@" --invert
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

from PIL import Image

DEFAULT_CHARSET = "@%#*+=-:. "
DEFAULT_WIDTH = 120
MIN_WIDTH = 20
MAX_WIDTH = 600
HEIGHT_CORRECTION = 0.55


def clamp(value: int, low: int, high: int) -> int:
    return max(low, min(high, value))


def pixel_to_char(gray: int, charset: str) -> str:
    index = int((gray / 255) * (len(charset) - 1))
    return charset[index]


def image_to_ascii(
    image_path: Path,
    width: int,
    charset: str = DEFAULT_CHARSET,
    invert: bool = False,
) -> str:
    if not charset:
        raise ValueError("charset cannot be empty")

    width = clamp(width, MIN_WIDTH, MAX_WIDTH)
    chars = charset[::-1] if invert else charset

    with Image.open(image_path) as image:
        gray_image = image.convert("L")
        source_w, source_h = gray_image.size
        ratio = source_h / source_w
        output_h = max(1, int(ratio * width * HEIGHT_CORRECTION))
        resized = gray_image.resize((width, output_h))

        pixels: Iterable[int] = list(resized.getdata())
        lines: list[str] = []

        for row in range(output_h):
            start = row * width
            row_pixels = pixels[start : start + width]
            lines.append("".join(pixel_to_char(p, chars) for p in row_pixels))

        return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert an image file into ASCII art in your terminal."
    )
    parser.add_argument("input", type=Path, help="Path to source image (jpg, png, etc.)")
    parser.add_argument(
        "-w",
        "--width",
        type=int,
        default=DEFAULT_WIDTH,
        help=f"Output width in characters (default: {DEFAULT_WIDTH}, range: {MIN_WIDTH}-{MAX_WIDTH})",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Optional output .txt file path. If omitted, prints to terminal.",
    )
    parser.add_argument(
        "--charset",
        default=DEFAULT_CHARSET,
        help="Characters from dark to light (default: '@%%#*+=-:. ').",
    )
    parser.add_argument(
        "--invert",
        action="store_true",
        help="Invert brightness mapping (useful for dark terminal themes).",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if not args.input.exists() or not args.input.is_file():
        parser.error(f"Input image not found: {args.input}")

    if args.width < MIN_WIDTH or args.width > MAX_WIDTH:
        parser.error(f"Width must be between {MIN_WIDTH} and {MAX_WIDTH}.")

    try:
        ascii_art = image_to_ascii(
            image_path=args.input,
            width=args.width,
            charset=args.charset,
            invert=args.invert,
        )
    except Exception as exc:
        parser.error(f"Failed to convert image: {exc}")

    if args.output:
        args.output.write_text(ascii_art, encoding="utf-8")
        print(f"ASCII art saved to: {args.output}")
    else:
        print(ascii_art)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
