# Document Profile

## Purpose

The Document profile covers bounded textual or predominantly textual sources while preserving strict Reference/Context/Interpretive separation.

## v0.1 Contract

Executable contract in [profiles/document.yaml](profiles/document.yaml):

- Status: active
- Requirement-strengthening overrides in Reference:
  - page_count: recommended
  - stated_title: recommended
  - stated_author: recommended
- Document-specific custom field:
  - reference.document_subdivisions

Subdivision shape:

- kind: required string
- label: required string
- source_locator: conditional, nullable string

## RCI Placement

- Reference: intrinsic source-native structure and source-stated metadata.
- Context: externally supplied situating metadata.
- Interpretive: analytical segmentation, significance, or commentary.

Interpretive segmentation must not be represented as intrinsic document structure.

## v0.1 Evidence Summary

Document evidence supported a deliberately minimal specialization:

- strengthen title/author/page_count requirements
- represent intrinsic subdivisions with a lightweight Reference structure

No additional document-specific Context or Interpretive field was required for v0.1.

## Boundaries

- Embedded objects do not automatically change the containing record to another profile.
- Independently meaningful embedded components may be modeled separately and linked through inherited relationship mechanisms.
- File format alone does not determine profile membership.

## Deferred Beyond v0.1

- deeper subdivision hierarchy
- normalized locator objects
- document-specific version-chain structures
- dedicated embedded-content indexing fields
