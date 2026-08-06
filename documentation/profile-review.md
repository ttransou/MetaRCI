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

* Prior prose implied rich profile-specific field sets for structured-data, media, and composite; current profile YAML for these profiles declares no overrides and no custom fields.
* Prior prose implied some media/composite behaviors as if settled; current executable contract does not enforce those details.
* Current executable document profile includes only three requirement-strengthening overrides; prior prose read broader than executable constraints.

## Unsupported Architectural Claims Identified

* Claims that generated-description provenance is structurally supported in profile YAML are not currently contract-enforced.
* Claims that composite expected/present membership and completeness are structurally represented are not currently contract-enforced.
* Claims that structured-data schema modeling shape is settled are not currently contract-enforced.

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
