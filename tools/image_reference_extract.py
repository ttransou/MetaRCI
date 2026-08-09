#!/usr/bin/env python3
"""Tiny image reference extraction helper.

Parsers included:
- JPEG parser
- PNG parser
- TIFF parser
- SVG parser

This helper intentionally remains decoupled from MetaRCI record generation.
It extracts technical properties from file content and prints JSON.
"""

from __future__ import annotations

import argparse
import json
import re
import struct
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any


class ParseError(RuntimeError):
    """Raised when a file cannot be parsed as a supported image type."""


def _parse_jpeg(data: bytes) -> dict[str, Any]:
    if len(data) < 4 or data[:2] != b"\xff\xd8":
        raise ParseError("Not a JPEG SOI stream")

    out: dict[str, Any] = {"format": "jpeg", "parser": "jpeg"}
    comments: list[str] = []
    i = 2

    while i < len(data):
        if data[i] != 0xFF:
            i += 1
            continue

        while i < len(data) and data[i] == 0xFF:
            i += 1

        if i >= len(data):
            break

        marker = data[i]
        i += 1

        if marker in (0xD9, 0xDA):  # EOI or SOS
            break

        if i + 2 > len(data):
            break

        seglen = struct.unpack(">H", data[i : i + 2])[0]
        segstart = i + 2
        segend = segstart + seglen - 2

        if segend > len(data):
            raise ParseError("Corrupt JPEG segment length")

        seg = data[segstart:segend]

        if marker == 0xE0 and seg.startswith(b"JFIF\x00") and len(seg) >= 14:
            out["jfif_version"] = f"{seg[5]}.{seg[6]:02d}"
            out["density_units_code"] = seg[7]
            out["density_x"] = struct.unpack(">H", seg[8:10])[0]
            out["density_y"] = struct.unpack(">H", seg[10:12])[0]
            out["thumbnail_width"] = seg[12]
            out["thumbnail_height"] = seg[13]

        if marker in {
            0xC0,
            0xC1,
            0xC2,
            0xC3,
            0xC5,
            0xC6,
            0xC7,
            0xC9,
            0xCA,
            0xCB,
            0xCD,
            0xCE,
            0xCF,
        } and len(seg) >= 6:
            out["sample_precision_bits"] = seg[0]
            out["height_pixels"] = struct.unpack(">H", seg[1:3])[0]
            out["width_pixels"] = struct.unpack(">H", seg[3:5])[0]
            out["component_count"] = seg[5]
            out["sof_marker_hex"] = f"0x{marker:02X}"

        if marker == 0xFE:
            comments.append(seg.decode("latin-1", errors="replace"))

        i = segend

    if comments:
        out["comments"] = comments

    if "width_pixels" not in out or "height_pixels" not in out:
        raise ParseError("JPEG width/height were not found")

    return out


def _parse_png(data: bytes) -> dict[str, Any]:
    sig = b"\x89PNG\r\n\x1a\n"
    if len(data) < 33 or not data.startswith(sig):
        raise ParseError("Not a PNG signature")

    length = struct.unpack(">I", data[8:12])[0]
    chunk_type = data[12:16]
    if chunk_type != b"IHDR" or length < 13:
        raise ParseError("PNG IHDR chunk missing or invalid")

    ihdr = data[16:29]
    return {
        "format": "png",
        "parser": "png",
        "width_pixels": struct.unpack(">I", ihdr[0:4])[0],
        "height_pixels": struct.unpack(">I", ihdr[4:8])[0],
        "bit_depth": ihdr[8],
        "color_type_code": ihdr[9],
        "compression_method": ihdr[10],
        "filter_method": ihdr[11],
        "interlace_method": ihdr[12],
    }


def _parse_tiff(data: bytes) -> dict[str, Any]:
    if len(data) < 8:
        raise ParseError("TIFF header too short")

    byte_order = data[:2]
    if byte_order == b"II":
        endian = "<"
        byte_order_name = "little"
    elif byte_order == b"MM":
        endian = ">"
        byte_order_name = "big"
    else:
        raise ParseError("Not a TIFF byte-order header")

    magic = struct.unpack(endian + "H", data[2:4])[0]
    if magic != 42:
        raise ParseError("Not a TIFF magic number")

    ifd_offset = struct.unpack(endian + "I", data[4:8])[0]
    if ifd_offset + 2 > len(data):
        raise ParseError("Invalid TIFF IFD offset")

    entry_count = struct.unpack(endian + "H", data[ifd_offset : ifd_offset + 2])[0]
    pos = ifd_offset + 2

    type_sizes = {
        1: 1,   # BYTE
        2: 1,   # ASCII
        3: 2,   # SHORT
        4: 4,   # LONG
        5: 8,   # RATIONAL
        6: 1,   # SBYTE
        7: 1,   # UNDEFINED
        8: 2,   # SSHORT
        9: 4,   # SLONG
        10: 8,  # SRATIONAL
        11: 4,  # FLOAT
        12: 8,  # DOUBLE
    }

    tags: dict[int, tuple[int, int, int]] = {}
    for _ in range(entry_count):
        if pos + 12 > len(data):
            raise ParseError("Corrupt TIFF IFD entry")
        tag, typ, count, value_or_offset = struct.unpack(endian + "HHII", data[pos : pos + 12])
        tags[tag] = (typ, count, value_or_offset)
        pos += 12

    def _get_raw_value(typ: int, count: int, value_or_offset: int) -> bytes:
        size = type_sizes.get(typ)
        if size is None:
            return b""
        total = size * count
        if total <= 4:
            return struct.pack(endian + "I", value_or_offset)[:total]
        if value_or_offset + total > len(data):
            return b""
        return data[value_or_offset : value_or_offset + total]

    def _read_uint(typ: int, raw: bytes) -> int | None:
        if typ == 3 and len(raw) >= 2:
            return struct.unpack(endian + "H", raw[:2])[0]
        if typ == 4 and len(raw) >= 4:
            return struct.unpack(endian + "I", raw[:4])[0]
        return None

    width = None
    height = None
    bits_per_sample = None
    compression = None
    photometric = None
    samples_per_pixel = None

    if 256 in tags:  # ImageWidth
        typ, count, vo = tags[256]
        width = _read_uint(typ, _get_raw_value(typ, count, vo))
    if 257 in tags:  # ImageLength
        typ, count, vo = tags[257]
        height = _read_uint(typ, _get_raw_value(typ, count, vo))
    if 258 in tags:  # BitsPerSample
        typ, count, vo = tags[258]
        raw = _get_raw_value(typ, count, vo)
        if typ == 3 and len(raw) >= 2:
            bits_per_sample = struct.unpack(endian + "H", raw[:2])[0]
    if 259 in tags:  # Compression
        typ, count, vo = tags[259]
        compression = _read_uint(typ, _get_raw_value(typ, count, vo))
    if 262 in tags:  # PhotometricInterpretation
        typ, count, vo = tags[262]
        photometric = _read_uint(typ, _get_raw_value(typ, count, vo))
    if 277 in tags:  # SamplesPerPixel
        typ, count, vo = tags[277]
        samples_per_pixel = _read_uint(typ, _get_raw_value(typ, count, vo))

    if width is None or height is None:
        raise ParseError("TIFF width/height tags were not found")

    out: dict[str, Any] = {
        "format": "tiff",
        "parser": "tiff",
        "byte_order": byte_order_name,
        "width_pixels": width,
        "height_pixels": height,
    }
    if bits_per_sample is not None:
        out["bits_per_sample"] = bits_per_sample
    if compression is not None:
        out["compression_code"] = compression
    if photometric is not None:
        out["photometric_interpretation_code"] = photometric
    if samples_per_pixel is not None:
        out["samples_per_pixel"] = samples_per_pixel

    return out


def _parse_svg(data: bytes) -> dict[str, Any]:
    text = data.decode("utf-8", errors="replace").strip()
    if "<svg" not in text.lower():
        raise ParseError("Not an SVG document")

    try:
        root = ET.fromstring(text)
    except ET.ParseError as exc:
        raise ParseError(f"Invalid SVG XML: {exc}") from exc

    tag = root.tag.lower()
    if not (tag == "svg" or tag.endswith("}svg")):
        raise ParseError("SVG root element not found")

    width_raw = root.attrib.get("width")
    height_raw = root.attrib.get("height")
    view_box = root.attrib.get("viewBox")

    def _number_prefix(value: str | None) -> float | None:
        if not value:
            return None
        m = re.match(r"^\s*([+-]?\d+(?:\.\d+)?)", value)
        if not m:
            return None
        return float(m.group(1))

    width = _number_prefix(width_raw)
    height = _number_prefix(height_raw)

    out: dict[str, Any] = {"format": "svg", "parser": "svg"}
    if width is not None:
        out["width"] = width
        out["width_raw"] = width_raw
    if height is not None:
        out["height"] = height
        out["height_raw"] = height_raw
    if view_box is not None:
        out["viewBox"] = view_box

    if not out.get("width") and not out.get("height") and view_box is None:
        raise ParseError("SVG has no width/height/viewBox attributes")

    return out


def extract_image_properties(file_path: Path) -> dict[str, Any]:
    data = file_path.read_bytes()

    parsers = (_parse_jpeg, _parse_png, _parse_tiff, _parse_svg)
    errors: list[str] = []

    for parser in parsers:
        try:
            result = parser(data)
            result["file_path"] = str(file_path)
            return result
        except ParseError as exc:
            errors.append(str(exc))

    raise ParseError(
        "Unsupported or unrecognized image file. Parser attempts: "
        + " | ".join(errors)
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extract technical image properties from file content (JSON output)."
    )
    parser.add_argument("image_path", type=Path, help="Path to an image file")
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print JSON output",
    )
    args = parser.parse_args()

    props = extract_image_properties(args.image_path)

    if args.pretty:
        print(json.dumps(props, indent=2, sort_keys=True))
    else:
        print(json.dumps(props, sort_keys=True))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
