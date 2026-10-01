#!/usr/bin/env python3

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def load_font(size: int, bold: bool = False):
    candidates = [
        "/System/Library/Fonts/HelveticaNeue.ttc",
        "/System/Library/Fonts/Helvetica.ttc",
    ]

    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue

    return ImageFont.load_default()


def scale_to_width(image: Image.Image, width: int) -> Image.Image:
    ratio = width / image.width
    height = round(image.height * ratio)

    return image.resize(
        (width, height),
        Image.Resampling.LANCZOS,
    )


def main():
    parser = argparse.ArgumentParser(
        description="Generate an annotated Figma/UAT design-review comparison."
    )

    parser.add_argument("--figma", required=True)
    parser.add_argument("--uat", required=True)
    parser.add_argument("--output", required=True)

    parser.add_argument("--finding-id", required=True)
    parser.add_argument("--property", required=True)
    parser.add_argument("--expected", required=True)
    parser.add_argument("--actual", required=True)
    parser.add_argument("--token")

    parser.add_argument(
        "--uat-crop",
        nargs=4,
        type=int,
        metavar=("LEFT", "TOP", "RIGHT", "BOTTOM"),
    )

    args = parser.parse_args()

    figma_path = Path(args.figma)
    uat_path = Path(args.uat)
    output_path = Path(args.output)

    figma = Image.open(figma_path).convert("RGB")
    uat = Image.open(uat_path).convert("RGB")

    if args.uat_crop:
        uat = uat.crop(tuple(args.uat_crop))

    column_width = 420

    figma = scale_to_width(figma, column_width)
    uat = scale_to_width(uat, column_width)

    margin = 32
    gutter = 32
    header_height = 52
    annotation_height = 150

    image_height = max(figma.height, uat.height)

    canvas_width = margin * 2 + column_width * 2 + gutter
    canvas_height = (
        margin
        + header_height
        + image_height
        + annotation_height
        + margin
    )

    canvas = Image.new(
        "RGB",
        (canvas_width, canvas_height),
        "white",
    )

    draw = ImageDraw.Draw(canvas)

    title_font = load_font(18)
    finding_font = load_font(17, bold=True)
    text_font = load_font(15)

    figma_x = margin
    uat_x = margin + column_width + gutter
    image_y = margin + header_height

    draw.text(
        (figma_x, margin),
        "FIGMA — Expected",
        fill="black",
        font=title_font,
    )

    draw.text(
        (uat_x, margin),
        "UAT — Actual",
        fill="black",
        font=title_font,
    )

    canvas.paste(figma, (figma_x, image_y))
    canvas.paste(uat, (uat_x, image_y))

    # Mark the UAT component itself.
    draw.rectangle(
        (
            uat_x,
            image_y,
            uat_x + uat.width - 1,
            image_y + uat.height - 1,
        ),
        outline="red",
        width=3,
    )

    marker_radius = 15
    marker_x = uat_x + uat.width - marker_radius - 8
    marker_y = image_y + marker_radius + 8

    draw.ellipse(
        (
            marker_x - marker_radius,
            marker_y - marker_radius,
            marker_x + marker_radius,
            marker_y + marker_radius,
        ),
        fill="red",
    )

    marker_text = args.finding_id

    marker_bbox = draw.textbbox(
        (0, 0),
        marker_text,
        font=text_font,
    )

    marker_width = marker_bbox[2] - marker_bbox[0]
    marker_height = marker_bbox[3] - marker_bbox[1]

    draw.text(
        (
            marker_x - marker_width / 2,
            marker_y - marker_height / 2 - 2,
        ),
        marker_text,
        fill="white",
        font=text_font,
    )

    annotation_y = image_y + image_height + 28

    draw.text(
        (margin, annotation_y),
        f"{args.finding_id} — {args.property}",
        fill="red",
        font=finding_font,
    )

    expected = f"Figma: {args.expected}"

    if args.token:
        expected += f" — {args.token}"

    draw.text(
        (margin, annotation_y + 34),
        expected,
        fill="black",
        font=text_font,
    )

    draw.text(
        (margin, annotation_y + 62),
        f"UAT: {args.actual}",
        fill="red",
        font=text_font,
    )

    draw.text(
        (margin, annotation_y + 90),
        "Confirmed difference",
        fill="red",
        font=text_font,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)

    canvas.save(output_path, "PNG")

    print(f"Generated: {output_path}")
    print(f"Dimensions: {canvas.width}x{canvas.height}")


if __name__ == "__main__":
    main()