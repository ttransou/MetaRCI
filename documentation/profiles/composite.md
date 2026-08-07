# Composite Profile

## Purpose

Current contract:

* The composite profile exists as a structural profile named composite.
* It extends the base schema at version 0.1.0 and is currently draft.

Current guidance:

* Use this profile for source units composed of multiple independently meaningful components.

## Structural Characteristics

Current guidance:

* Composite sources often involve membership, hierarchy, ordering, and collection-level context.

Open question:

* What minimum structural signals distinguish a composite from a simple storage container?

## Profile Emphasis

Current contract:

* The current YAML declares no overrides and no custom fields.
* Effective behavior currently remains the base schema with composite identity.

Current guidance:

* Emphasize collection-level identity and member relationships without introducing a heavy package ontology.

## Rationale for Current Fields

Current contract:

* The profile intentionally starts with no composite-specific field additions.
* The example record demonstrates a composite source via related_sources and interpretive relationships while staying within base fields.

Current guidance:

* This enables early composite use without locking in one membership schema too early.

## Relevant Design Questions

Open question:

* How should expected versus present members be represented?
* How should member roles and ordering be expressed?
* What context may be inherited from the composite record?
* How should collection-level and item-level metadata conflicts be handled?
* How should completeness be represented when expected membership is unknown?
* Should cross-profile membership constraints be formalized in profile YAML or remain descriptive guidance?
* Can and should a composite explicitly contain members validated under different structural profiles in a future contract?
* Should completeness and expected-membership state become first-class fields?

## Current Decisions Supported by YAML

Current contract:

* Status is draft.
* No composite-specific overrides are currently declared.
* No composite-specific custom fields are currently declared.

Current guidance:

* Composite members may be represented by related source links and relationship entries.

Proposed change:

* Introduce composite custom fields only with evidence across multiple implementations.

## Boundaries with Other Profiles

Current guidance:

* Do not use composite solely because a source is packaged as ZIP/folder.
* Prefer document, structured-data, or media when one primary source unit is being described.

## Example Applications

Current guidance:

* Case packages, archival groupings, regulatory bundles, and multimodal collections.

Deferred:

* A full graph-native composite membership model.

## Closure Candidate Pass (No Implementation)

Current guidance:

* Close as guidance now: treat composite as an aggregation profile only when the source unit has meaningful member relationships beyond simple storage.
* Close as guidance now: represent membership links with existing related_sources and relationship entries while the profile remains boundary-first.
* Close as guidance now: allow mixed-member structures in practice when modeled through relationships, while deferring formal cross-profile constraints.

Open question:

* Keep open: standardized representation for expected versus present members and completeness state in profile YAML.
* Keep open: standardized representation for member roles and ordering when these change interpretation.
* Keep open: whether inheritance and conflict-resolution behavior should remain guidance or become contractized checks.

## Recommended Code Change (Proposal Only)

Proposed change:

* Introduce one optional composite custom field in profile YAML to capture reusable membership state, for example:
  * `context.member_manifest` as `list<object>` with minimal child properties such as member_id, member_profile, member_role, member_order, and membership_status.

Current guidance:

* Do not implement yet.
* Implement only after at least two independent composite testbeds require explicit expected/present membership semantics that cannot be represented clearly with current related_sources and relationship usage.

If later approved, the implementation bundle should include:

* profile YAML update in `profiles/composite.yaml`;
* example update in `examples/composite-record.yaml`;
* positive/negative regression tests in `tests/test_validate.py` for nested member-manifest validation;
* documentation updates in this file and `documentation/profile-question-matrix.md`.
