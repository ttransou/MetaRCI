# Document Profile

## Purpose

Current contract:

* The document profile exists as a structural profile named `document` in the profile YAML.

* It extends the base schema at version 0.1.0 and is currently a draft.

Current guidance:

* Use this profile for bounded textual or predominantly textual sources.

## Structural Characteristics

Current guidance:

* The source is treated as a primarily textual unit.

* Source identity, title, author, version, and intrinsic document organization are common concerns.

* Intrinsic document structure must be asserted by or observably grounded in the source artifact.

Deferred:

* Additional document-structure complexity beyond the current v0.1 subdivision model.

## Profile Emphasis

Current contract:

* Current executable emphasis is implemented through requirement-strengthening overrides for:
  * `reference.page_count`
  * `reference.stated_title`
  * `reference.stated_author`
* Current executable custom field support includes:
  * `reference.document_subdivisions`

Current guidance:

* Continue emphasizing document identity, authorship, source-grounded structure, versioning context, and relationships without adding domain-specific semantics.

* Treat intrinsic subdivision assertions as source-grounded only when headings, sections, clauses, or equivalent structure are directly present in or mechanically recoverable from the source.

* Treat analytical or imposed segmentation as Interpretive rather than intrinsic document structure.

## Profile Scope

The `document` profile models bounded textual or predominantly textual source artifacts and their intrinsic document-level structure.

Intrinsic structure must be asserted by or observably grounded in the source artifact. Examples include source-native parts, sections, chapters, clauses, appendices, and comparable structural divisions.

Analytical or imposed segmentation does not become document structure merely because it can be described structurally. Such segmentation belongs in the Interpretive tier.

The profile does not define domain semantics, document genre taxonomies, or the internal metadata of embedded media or structured-data components.

File format does not determine profile membership. PDF, Markdown, DOCX, plain text, XML, or other formats may all represent a document when the source itself is a bounded textual or predominantly textual artifact.

Source-native document structure belongs in the Reference tier. Interpretive or analyst-imposed segmentation belongs in the Interpretive tier.

## Rationale for Current Fields

Current contract:

* The profile currently relies on inherited base fields, three requirement overrides, and one reusable Reference-tier custom field.

* The document-specific custom field currently declared in YAML is `reference.document_subdivisions`.

* The v0.1 subdivision shape consists of:
  * `kind`
  * `label`
  * `source_locator`

Current guidance:

* The contract remains intentionally lightweight.

* Source-grounding discipline governs when `document_subdivisions` should be populated.

* `kind` and `label` describe source-native subdivision structure.

* `source_locator` provides a lightweight source-specific locator without requiring normalized locator semantics in v0.1.

Deferred:

* Explicit subdivision hierarchy.

* Parent/child references.

* Subdivision identifiers.

* Controlled subdivision vocabularies.

* Structured or normalized locator objects.

## Embedded Content

Current guidance:

* Embedded content should be separated conceptually into mechanically observable source facts and later judgments about significance.

* Reference metadata may record mechanically observable facts about embedded objects when those facts are directly present in or recoverable from the source.

* Mechanical detection of an embedded object does not establish that the object is significant, independently meaningful, or worthy of separate modeling.

* Significance, relevance, intended role, and similar judgments belong in Context or Interpretive metadata as appropriate.

* An embedded component should receive its own MetaRCI record only when an implementation or user determines that the component is independently meaningful.

* When separately modeled, the component should use the structural profile appropriate to that component and connect to the document through general MetaRCI relationship mechanisms.

Current guidance:

* The document profile does not define a dedicated `embedded_media_index`.

* The document profile should not classify every embedded object as media merely because it occurs inside a document.

* Tables, diagrams, images, charts, structured data, and other embedded objects may have different structural identities when modeled independently.

Deferred:

* Whether general MetaRCI relationships require a source-locator capability for identifying where a related component occurs within another source.

## Edition and Version Handling

Current guidance:

* Use `reference.stated_version` only for version or edition information directly stated by or mechanically recoverable from the source artifact.

* Do not populate `stated_version` solely from filenames, repository labels, external bibliographic information, or other contextual knowledge unless that value is also supported by the source itself.

* Externally established edition, publication, derivation, predecessor, successor, or revision history should be represented through Context fields such as `source_lineage` or `related_sources`, and through general MetaRCI relationships where appropriate.

* Analytical claims about differences, significance, or meaning across versions belong in the Interpretive tier.

Current guidance:

* The document profile does not require a document-specific edition-history, revision-chain, or version-relationship custom field for v0.1.

* Existing Reference, Context, and relationship mechanisms are sufficient for the version and edition cases exercised by the current document testbed.

## Relevant Design Questions

Current contract decision:

* Intrinsic section/chapter/clause structures are represented through `reference.document_subdivisions`.

Current guidance:

* Version and edition information uses existing Reference, Context, and relationship mechanisms rather than a document-specific version structure.

* Significant embedded content does not require a document-specific indexing structure.

* Independently meaningful components may instead receive separate records and relationships.

Deferred:

* Whether later evidence requires more complex subdivision hierarchy or locator semantics.

Open question:

* Should any currently base-level document-skewed fields be reconsidered in a future base-schema review?

## Current Decisions Supported by YAML

Current contract:

* Status is draft.

* One reusable Reference-tier custom field is declared.

* `reference.document_subdivisions` uses the v0.1 minimum structure:
  * required `kind`
  * required `label`
  * conditional, nullable `source_locator`

* Only shallow allowed override behavior is used.

* Profile-version and base-version equality are required by validator behavior.

Current guidance:

* Do not extend the current subdivision shape unless recurring evidence demonstrates that the minimum v0.1 representation is insufficient.

## Boundaries with Other Profiles

Current guidance:

* Prefer structured-data when the source meaning is primarily schema-dependent.

* Prefer media when visual, audio, or audiovisual structure is primary.

* Prefer composite when the described unit is an aggregation of independently meaningful sources.

* An embedded object does not automatically change the structural profile of the containing document.

* An embedded object modeled independently should use the profile appropriate to its own source structure.

## Example Applications

Current guidance:

* Reports, policies, manuals, correspondence, articles, and similar textual artifacts.

Deferred:

* Domain-specific document specializations as separate structural profiles.

## Current Evidence Posture

Current contract decision:

* Intrinsic source-native document subdivisions belong in the Reference tier.

* The v0.1 `document_subdivisions` shape is limited to `kind`, `label`, and `source_locator`.

Current guidance:

* Document records should remain structurally lightweight and rely on inherited base fields plus the current requirement overrides for title, author, and `page_count`.

* Interpretive narrative segmentation should not be represented as intrinsic document subdivisions.

* Mechanical detection of embedded content establishes presence, not significance.

* When an embedded component becomes independently meaningful, use a separate MetaRCI record and general relationship modeling rather than a document-specific embedded-media index.

* Use `stated_version` only for source-stated or mechanically recoverable version information.

* Use Context and relationship mechanisms for externally established edition, publication, derivation, predecessor, successor, or revision history.

* Analytical comparison or significance across versions belongs in Interpretive metadata.

* No additional document-specific edition/version structure is required for v0.1.

Open question:

* Whether document-skewed base fields should be moved or re-scoped, pending formal base-schema review evidence.

Deferred:

* Additional subdivision hierarchy and locator semantics.

* Dedicated embedded-content indexing.

* Relationship-level source locators pending broader cross-profile evidence.

## Implementation Status

Current contract:

* No additional document-profile field is required for embedded content in v0.1.

* No additional document-profile field is required for edition/version handling in v0.1.

* `reference.document_subdivisions` is the current document-specific custom field.

* The canonical document example places `document_subdivisions` in the Reference tier.

* Document-subdivision regression tests validate the Reference-tier path and nested field requirements.

Current guidance:

* Keep `reference.document_subdivisions` lightweight and implementation-agnostic.

* Do not treat interpretive narrative segmentation as intrinsic source structure.

* Do not add `embedded_media_index` based on current evidence.

* Do not add a document-specific edition-history or revision-chain field based on current evidence.

* Add stricter subdivision semantics, embedded-content structure, or version-specific structure only after recurring evidence demonstrates a cross-implementation need.

Current note:

* The document profile YAML, canonical document record, and document-subdivision tests are aligned with the current v0.1 decisions.

* The current validator and unit-test suite pass after the Reference-tier subdivision change.

* Testbed evaluation should continue to distinguish mechanical source facts from contextual and interpretive enrichment.

* Field availability does not imply that every qualifying source must populate every conditional field.

If later evidence supports additional implementation changes, the implementation bundle should include:

* profile YAML update in `profiles/document.yaml`;* example update in `examples/document-record.yaml`;* positive/negative regression tests in `tests/test_validate.py`;* documentation updates in this file and `documentation/profile-question-matrix.md`.
