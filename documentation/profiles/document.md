# Document Profile

## Purpose

Current contract:

* The document profile exists as a structural profile named document in the profile YAML.
* It extends the base schema at version 0.1.0 and is currently draft.

Current guidance:

* Use this profile for bounded textual or predominantly textual sources.

## Structural Characteristics

Current guidance:

* The source is treated as a primarily textual unit.
* Source identity, title, author, version, and document organization are common concerns.

Open question:

* Which document-structure elements should remain generic versus move to implementation extensions?

## Profile Emphasis

Current contract:

* Current executable emphasis is implemented through requirement-strengthening overrides for:
  * reference.page_count
  * reference.stated_title
  * reference.stated_author

Current guidance:

* Continue emphasizing document identity, authorship, versioning context, and relationships without adding domain-specific semantics.

## Rationale for Current Fields

Current contract:

* The profile currently relies on inherited base fields plus three requirement overrides.
* There are no document-specific custom fields in the YAML.
* The example record demonstrates this contract with base fields and no custom field usage.

Current guidance:

* The initial contract intentionally stays minimal while profile boundaries are tested across implementations.

## Relevant Design Questions

Open question:

* Should section/chapter/clause structures be represented directly in profile custom fields?
* How much edition/version relationship structure should be explicit versus relationship-based?
* How should documents with significant embedded media be represented when both document and media structure matter?
* Should any currently base-level document-skewed fields be reconsidered in a future base-schema review?

## Current Decisions Supported by YAML

Current contract:

* Status is draft.
* No custom fields are declared.
* Only shallow allowed override behavior is used.
* Profile-version and base-version equality are required by validator behavior.

Proposed change:

* Introduce additional document-structure profile fields only after recurring cross-implementation evidence.

## Boundaries with Other Profiles

Current guidance:

* Prefer structured-data when the source meaning is primarily schema-dependent.
* Prefer media when visual/audio structure is primary.
* Prefer composite when the described unit is an aggregation of independently meaningful sources.

## Example Applications

Current guidance:

* Reports, policies, manuals, correspondence, articles, and similar textual artifacts.

Deferred:

* Domain-specific document specializations as separate structural profiles.

## Closure Candidate Pass (No Implementation)

Current guidance:

* Close as guidance now: document records should remain structurally lightweight and rely on inherited base fields plus the current requirement overrides for title, author, and page_count.
* Close as guidance now: edition/version linkage should default to existing relationship modeling unless repeated ambiguity is demonstrated.
* Close as guidance now: when embedded media is materially primary, represent it as a separate media or composite record rather than forcing all structure into the document profile.

Open question:

* Keep open: section/chapter/clause representation in profile YAML, pending recurring cross-implementation evidence.
* Keep open: whether document-skewed base fields should be moved or re-scoped, pending formal base-schema review evidence.

## Recommended Code Change (Proposal Only)

Proposed change:

* Introduce one optional document custom field in profile YAML to capture reusable subdivision structure without domain language, for example:
  * `context.document_subdivisions` as `list<object>` with minimal child properties such as subdivision kind, label, and source locator.

Current guidance:

* Do not implement yet.
* Implement only after at least two independent document testbeds show recurring need that is not cleanly represented by current base fields and relationships.

If later approved, the implementation bundle should include:

* profile YAML update in `profiles/document.yaml`;
* example update in `examples/document-record.yaml`;
* positive/negative regression tests in `tests/test_validate.py` for nested subdivision validation;
* documentation updates in this file and `documentation/profile-question-matrix.md`.
