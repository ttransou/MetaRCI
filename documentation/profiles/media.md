# Media Profile

## Purpose

Current contract:

* The media profile exists as a structural profile named media.
* It extends the base schema at version 0.1.0 and is currently draft.

Current guidance:

* Use this profile for primarily visual, audio, audiovisual, or other non-textual source units.

## Structural Characteristics

Current guidance:

* Common concerns include technical source properties, rights context, descriptive interpretation, and relationships.

Open question:

* Which media-specific concerns should be represented by profile custom fields in a future revision?

## Profile Emphasis

Current contract:

* The current YAML declares no overrides and no custom fields.
* Effective behavior is currently base-schema behavior plus profile identity.

Current guidance:

* Keep one initial media profile for image/audio/video unless structural divergence is demonstrated.

## Rationale for Current Fields

Current contract:

* The profile currently serves as a structural boundary without media-specific field additions.
* The example record validates using inherited base fields only.

Current guidance:

* Boundary-first design avoids premature commitment to one media annotation model.

## Relevant Design Questions

Open question:

* How should captions, transcripts, and accessibility descriptions be represented structurally?
* How should model-generated descriptions record provenance and review state?
* How should region/frame/time-segment references be represented?
* Which media properties belong in reference versus context/interpretive tiers?
* How to represent machine-generated and human-curated descriptions without ambiguity.
* Whether to encode region/time segmentation in profile fields or extensions.

## Current Decisions Supported by YAML

Current contract:

* Status is draft.
* No profile-specific override behavior is declared.
* No media custom fields are currently declared.

Proposed change:

* Add media custom fields only after a reusable cross-source pattern is demonstrated.

## Boundaries with Other Profiles

Current guidance:

* Prefer document when text structure is primary even if embedded media exists.
* Prefer structured-data when schema/table structure is primary.
* Prefer composite when the described source unit is a bundle containing multiple meaningful members.

## Example Applications

Current guidance:

* Photographs, diagrams, maps, recordings, videos, and scanned visual artifacts.

Deferred:

* Splitting media into separate image/audio/video structural profiles.

## Closure Candidate Pass (No Implementation)

Current guidance:

* Close as guidance now: keep a single media structural profile in 0.1 while image/audio/video differences remain mostly technical rather than structurally distinct.
* Close as guidance now: media records should continue to use inherited base fields and relationship metadata until reusable media-specific structures are proven across implementations.
* Close as guidance now: tier placement should default to reference for directly observed technical properties and context or interpretive tiers for curatorial or inferential assertions.

Open question:

* Keep open: standardized representation of captions, transcripts, accessibility descriptions, and model-generated description provenance in profile YAML.
* Keep open: standardized region/frame/time-segment representation in profile YAML.

## Recommended Code Change (Proposal Only)

Proposed change:

* Introduce one optional media custom field in profile YAML to capture reusable generated-description provenance, for example:
  * `interpretive.generated_descriptions` as `list<object>` with minimal child properties such as generator, generated_at, confidence, review_status, and text.

Current guidance:

* Do not implement yet.
* Implement only after at least two independent media testbeds require explicit generated-description provenance and cannot represent it clearly with current base fields and extensions.

If later approved, the implementation bundle should include:

* profile YAML update in `profiles/media.yaml`;
* example update in `examples/media-record.yaml`;
* positive/negative regression tests in `tests/test_validate.py` for nested generated-description validation;
* documentation updates in this file and `documentation/profile-question-matrix.md`.
