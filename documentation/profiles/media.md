# Media Profile

## Purpose

The Media profile covers primarily visual, audio, and audiovisual source units while preserving strict epistemic separation.

## v0.1 Contract

Executable contract in [profiles/media.yaml](profiles/media.yaml):

- Status: active
- Tier overrides: none

Reference custom fields:

- visual_dimensions
- duration_milliseconds
- stream_types
- video_codec
- audio_codec

Context custom fields:

- supplied_descriptions
- supplied_attributions
- supplied_terms

Interpretive custom fields:

- generated_descriptions
- generated_terms
- temporal_segments

## RCI Placement

- Reference: source-native or mechanically recoverable technical media facts.
- Context: externally supplied descriptive assertions.
- Interpretive: generated or analytical assertions.

Validation of structure does not establish semantic truth, authority, or quality.

## v0.1 Evidence Summary

Media evidence includes static-image and video-related evaluation results.

Cross-source Context portability was demonstrated with more than one external metadata ecosystem.

Temporal media work supported a locator pattern where:

- temporal_segments provide interval identity
- inherited relationships attach interpretive meaning

No additional media-specific ontology or deep codec schema was required for v0.1.

## Boundaries

- Mechanical extractability alone is not sufficient reason to add a contract field.
- Sparse Context is valid; external contextual enrichment is conditional.
- Generated outputs remain Interpretive even when produced automatically.

## Deferred Beyond v0.1

- richer rights/licensing structures
- attribution role granularity
- vocabulary typing and normalization
- confidence/review governance structures for generated assertions
- deeper temporal and region/frame semantics
