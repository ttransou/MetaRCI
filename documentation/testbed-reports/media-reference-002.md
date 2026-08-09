# Testbed Report

## Header

* Testbed name: media-reference-002
* Profile: media
* Date: 2026-08-09
* Source set summary: comparative Reference-layer image test across JPEG, PNG, TIFF, and SVG.

## Questions Covered

* Are raster pixel dimensions reusable across common image formats?
* Does reference.visual_dimensions preserve the Reference-tier epistemic boundary?
* Which mechanically extracted technical properties recur across formats strongly enough to warrant current contract status?
* Does SVG/vector geometry map cleanly to the raster visual_dimensions model?

## Source Evidence

### media-source-001 — JPEG

* Source path: testbed-sources/media/media-source-001/media-source-001.jpg
* Extractor path: tools/image_reference_extract.py
* Parser selected by content dispatch: jpeg
* width_pixels: 872
* height_pixels: 1024
* Additional mechanically extracted JPEG/JFIF properties were observed (including jfif_version, density_units_code, density_x, density_y, component_count, and SOF marker details).
* Embedded JPEG comment URI was observed: http://hdl.loc.gov/loc.pnp/ppmsca.40464
* Those additional properties were not promoted into the MetaRCI contract.

Evidence snapshot:

```json
{
  "file_path": "testbed-sources/media/media-source-001/media-source-001.jpg",
  "format": "jpeg",
  "parser": "jpeg",
  "width_pixels": 872,
  "height_pixels": 1024,
  "comments": [
    "http://hdl.loc.gov/loc.pnp/ppmsca.40464"
  ]
}
```

### media-source-003 — PNG

* Source path: testbed-sources/media/media-source-003/Example_png.png
* Extractor path: tools/image_reference_extract.py
* Parser selected by content dispatch: png
* width_pixels: 300
* height_pixels: 302
* PNG-specific IHDR properties were observed (bit_depth, color_type_code, compression_method, filter_method, interlace_method).
* Those properties were not promoted into the MetaRCI contract.

Evidence snapshot:

```json
{
  "file_path": "testbed-sources/media/media-source-003/Example_png.png",
  "format": "png",
  "parser": "png",
  "width_pixels": 300,
  "height_pixels": 302,
  "bit_depth": 8,
  "color_type_code": 6,
  "compression_method": 0,
  "filter_method": 0,
  "interlace_method": 0
}
```

### media-source-004 — TIFF

* Source path: testbed-sources/media/media-source-004/The_Dam_at_the_Falls_(NYPL_b11708063-G91F021_024ZF).tiff
* Extractor path: tools/image_reference_extract.py
* Parser selected by content dispatch: tiff
* width_pixels: 3072
* height_pixels: 1908
* TIFF-specific technical/tag properties were observed (byte_order, bits_per_sample, compression_code, photometric_interpretation_code, samples_per_pixel).
* Those properties were not promoted into the MetaRCI contract.

Evidence snapshot:

```json
{
  "file_path": "testbed-sources/media/media-source-004/The_Dam_at_the_Falls_(NYPL_b11708063-G91F021_024ZF).tiff",
  "format": "tiff",
  "parser": "tiff",
  "width_pixels": 3072,
  "height_pixels": 1908,
  "byte_order": "little",
  "bits_per_sample": 8,
  "compression_code": 1,
  "photometric_interpretation_code": 2,
  "samples_per_pixel": 3
}
```

### media-source-005 — SVG

* Source path: testbed-sources/media/media-source-005/Exemplo.svg
* Extractor path: tools/image_reference_extract.py
* Parser selected by content dispatch: svg
* Mechanically extracted width: 172.0
* Mechanically extracted height: 178.0
* Raw SVG width and height attributes were also available (width_raw: "172", height_raw: "178").
* These values are vector geometry attributes and were not normalized into width_pixels / height_pixels.

Evidence snapshot:

```json
{
  "file_path": "testbed-sources/media/media-source-005/Exemplo.svg",
  "format": "svg",
  "parser": "svg",
  "width": 172.0,
  "height": 178.0,
  "width_raw": "172",
  "height_raw": "178"
}
```

## Cross-Source Evidence

* JPEG, PNG, and TIFF independently expose meaningful raster pixel width and height.
* This supports reference.visual_dimensions as a reusable raster-media structure rather than a JPEG-specific field.
* Format-specific encoding/header metadata varies substantially between JPEG, PNG, and TIFF.
* Mechanical extractability alone was therefore not treated as sufficient evidence for first-class MetaRCI representation.
* SVG demonstrates a structural boundary: vector width/height should not be coerced into raster pixel dimensions.

## Extractor Boundary

* image_reference_extract.py is evidence/extraction infrastructure.
* It uses content-based parser dispatch.
* Extractor output is not schema authority.
* Properties emitted by the helper do not automatically become MetaRCI Reference fields.
* The helper currently supports JPEG, PNG, TIFF, and SVG extraction paths.
* This report does not claim parser maturity or completeness beyond the demonstrated behavior on the listed testbed sources.

## Contract Outcome

Current contract:

* reference.visual_dimensions is a conditional, nullable object.
* width_pixels is required, non-nullable integer when visual_dimensions is present.
* height_pixels is required, non-nullable integer when visual_dimensions is present.

Current evidence:

* JPEG, PNG, and TIFF support this shape.
* Existing positive validation and negative regression coverage support the current executable contract.
* The full MetaRCI validator suite currently passes 65 tests.

## Closure

Current contract:

* raster visual_dimensions for JPEG/PNG/TIFF-style raster sources.

Current guidance:

* extractor output is evidence, not automatic schema.
* format-specific technical properties require independent evidence before promotion.

Deferred:

* SVG/vector geometry including width/height units, viewport, viewBox, and coordinate systems.
* additional raster technical properties such as density, color structure, bit depth, compression, orientation, EXIF, and format-specific header/tag data.
* video and audio Reference structure.

No new field is proposed in this report.

## Validation State

* Command: python -m unittest discover -s tests -v
* Ran 65 tests
* OK