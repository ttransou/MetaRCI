# comp-source-002

## Source

- Source type: synthetic OpenDocument Presentation
- File: `comp-source-002-generic-testbed.odp`
- Profile target: `composite`
- Intake ID: `comp-source-002`

## Purpose

This source is a bounded synthetic Composite portability testbed constructed to challenge composition semantics identified through `comp-source-001` in a different presentation format and packaging ecosystem.

The specimen intentionally mirrors the logical component mix of the PPTX baseline where practical so that differences in representation can be evaluated without introducing unnecessary subject-matter variation.

## Included Components

The presentation contains:

- five ordered slides;
- ordinary slide text;
- speaker notes;
- an embedded image;
- a presentation table;
- a chart with associated data;
- an embedded short video.

These components are intended to exercise Document-like, Media-like, and Structured Data-like structures within one coherent ODP parent source.

## Source Handling

The ODP should be preserved as the original synthetic test artifact.

Any extraction, unpacking, normalization, conversion, or derived inspection output should be documented separately rather than replacing or silently modifying the source file.

The specimen was produced from the bounded synthetic PPTX baseline and converted to ODP for portability testing. This derivation should remain explicit when interpreting similarities or differences between the two testbeds.

## Testbed Role

`comp-source-002` is the presentation-format portability challenge for Composite evaluation.

Its purpose is to test whether candidate composition semantics identified in `comp-source-001` remain useful across a different presentation standard, including:

- parent source identity;
- independently meaningful component identity;
- source-native ordering;
- containment;
- heterogeneous component structure;
- relationships among parent and components;
- parent-level versus component-level metadata scope;
- and the distinction between meaningful logical components and package implementation artifacts.

The specimen does not define the final Composite contract and does not imply that every internal ODP resource requires independent MetaRCI representation.

## Known Limitations

- The presentation is synthetic rather than a naturally occurring operational source.
- It was derived from the synthetic PPTX baseline rather than authored independently in ODP.
- Conversion may alter or normalize some implementation-specific presentation structures.
- Findings should therefore be interpreted as a portability challenge, not as fully independent evidence of ODP authoring behavior.
- A later independently authored or externally sourced ODP specimen may be useful if conversion provenance materially affects the questions under evaluation.
