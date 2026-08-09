#!/usr/bin/env python3
"""Compatibility wrapper for the renamed image reference extractor."""

from pathlib import Path
import sys


# Ensure direct script execution can import sibling modules.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from image_reference_extract import main


if __name__ == "__main__":
    raise SystemExit(main())
