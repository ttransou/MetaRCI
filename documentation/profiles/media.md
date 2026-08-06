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

## Current Decisions Supported by YAML

Current contract:

* Status is draft.
* No profile-specific override behavior is declared.
* No media custom fields are currently declared.

## Unresolved Questions

Open question:

* How to represent machine-generated and human-curated descriptions without ambiguity.
* Whether to encode region/time segmentation in profile fields or extensions.

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
