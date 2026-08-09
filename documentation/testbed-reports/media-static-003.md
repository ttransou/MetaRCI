# Media Static-Image Testbed 003

## Purpose

Evaluate the MetaRCI `media` profile against static-image sources and determine a minimal v0.1 contract across Reference, Context, and Interpretive metadata.

## Scope

This report covers static visual media only.

Included evidence:

- JPEG
- PNG
- TIFF
- SVG as a vector-boundary case
- Library of Congress external metadata
- Wikimedia Commons external metadata
- generated-description and generated-term Interpretive fixtures

Audio and video are outside the scope of this report.

## Reference Findings

Static-image Reference testing established:

- `reference.visual_dimensions`
- `width_pixels`
- `height_pixels`

Raster dimensions were mechanically recoverable across JPEG, PNG, and TIFF.

SVG demonstrated that vector geometry should not be silently represented as raster pixel dimensions. Vector-specific geometry remains deferred.

Additional mechanically recoverable properties such as density, encoding details, component information, and embedded identifiers were observed but were not promoted into the v0.1 media contract without demonstrated need.

## Context Findings

External metadata from the Library of Congress was used as an initial exemplar, not as schema authority.

The following reusable Context structures were established:

- `context.supplied_descriptions`
- `context.supplied_attributions`
- `context.supplied_terms`

Each structure preserves the externally supplied assertion together with an identifier for the source supplying it.

Cross-source validation against Wikimedia Commons demonstrated that the same structures remain usable in a materially different metadata ecosystem:

- Commons `ImageDescription` mapped naturally to `supplied_descriptions`
- Commons `Artist` mapped naturally to `supplied_attributions`
- Commons categories mapped naturally to `supplied_terms`

No additional media-specific Context field was required by the second source ecosystem.

Sparse Context remains valid. MetaRCI does not require Context enrichment when no external descriptive source is available.

## Context Pressure Deferred

The following remain legitimate pressure areas but were not promoted into the v0.1 static-media contract:

- structured rights and licensing
- attribution-role granularity
- term vocabulary or type
- uncertain externally supplied date expressions
- collection membership
- richer provenance semantics

Some of these may ultimately belong in the base model rather than the media profile.

## Interpretive Findings

Static-image Interpretive testing established:

- `interpretive.generated_descriptions`
- `interpretive.generated_terms`

Generated descriptions use:

- required `text`
- required `generator`

Generated terms use:

- required `term`
- required `generator`

The generator records provenance of the Interpretive assertion. It does not establish correctness, confidence, authority, or review status.

Confidence scores, generator versions, timestamps, controlled vocabularies, review state, and related governance metadata remain deferred.

## RCI Boundary

Static-image testing reinforced the general MetaRCI rule that epistemic basis, rather than property name or producing tool, determines tier placement.

Examples:

- mechanically recoverable source metadata -> Reference
- externally supplied description or term -> Context
- model- or analyst-generated description or term -> Interpretive

The same logical descriptive concept may therefore appear in different tiers when its evidentiary basis differs.

## Validation

The executable media profile and regression suite validate:

- `reference.visual_dimensions`
- `context.supplied_descriptions`
- `context.supplied_attributions`
- `context.supplied_terms`
- `interpretive.generated_descriptions`
- `interpretive.generated_terms`

Static-image work closed with:

**85 tests passing.**

## v0.1 Static-Image Decision

Static-image support is provisionally complete for MetaRCI v0.1.

The current contract is intentionally minimal. It establishes useful structural and epistemic distinctions without attempting to encode every property exposed by image formats, external catalogs, or analytical systems.

Future evidence may extend the contract, but additional fields should be added only when reusable pressure is demonstrated.

## Next Testbed

The next media-profile work will reassess audiovisual source selection before video-specific schema decisions are made.

Initial video sources should be intentionally bounded, with a target duration of no more than 30 seconds, so that technical metadata, temporal structure, audio presence, external Context, and later Interpretive experiments can be evaluated incrementally.