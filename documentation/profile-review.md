# Profile Documentation Refactor Review

## Files Reviewed

* documentation/profile-model.md
* profiles/document.yaml
* profiles/structured-data.yaml
* profiles/media.yaml
* profiles/composite.yaml
* examples/document-record.yaml
* examples/structured-data-record.yaml
* examples/media-record.yaml
* examples/composite-record.yaml
* TODO.md

## Duplicated Content Removed

* Removed repeated profile-specific deep dives from the central model document.
* Removed repeated extension-boundary explanations and media generated-description discussion from the central model document.
* Removed repeated governance prose in places where one canonical statement is sufficient.

## Content Moved to Profile-Specific Files

* Moved document-specific structure and boundary guidance to documentation/profiles/document.md.
* Moved structured-data-specific schema/lineage guidance to documentation/profiles/structured-data.md.
* Moved media-specific descriptive and segmentation guidance to documentation/profiles/media.md.
* Moved composite-specific membership/completeness guidance to documentation/profiles/composite.md.

## Prose and YAML Inconsistencies Found

* Prior prose implied rich profile-specific field sets before they were contractized; current executable YAML now includes substantial custom-field sets for structured-data and media.
* Composite remains intentionally boundary-first with no profile-specific custom fields and no profile-specific overrides.
* Current executable document profile includes three requirement-strengthening overrides plus `reference.document_subdivisions`.

## Unsupported Architectural Claims Identified

* Claims that composite expected/present membership and completeness are structurally represented are not currently contract-enforced.

Current contract note:

* Generated-description provenance and generated terms are now contract-enforced in `profiles/media.yaml`.
* Structured-data field identity, contextual field assertions, and interpretive field assertions are now contract-enforced in `profiles/structured-data.yaml`.

## Unresolved Questions

* Which profile-specific guidance should become executable custom fields in 0.1.x or later?
* What evidence threshold is required for adding a new structural profile?
* How should composite completeness and member-role semantics be formalized, if at all?
* How should media region/time-segment semantics be represented without overfitting one implementation?

## Proposed Future Changes

* Promote guidance to profile YAML only after recurring cross-implementation evidence.
* Keep base-schema revision proposals separate and explicitly reviewed.
* Add profile-specific executable fields in small increments with validator and test updates.

## Base-Schema Integrity Confirmation

* Confirmed: schemas/metarci-base.yaml was not modified in this refactor.
