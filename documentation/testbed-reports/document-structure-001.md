# Testbed Report

## Header

* Testbed name: document-structure-001* Profile: document* Date: 2026-08-07* Author: GitHub Copilot* Source set summary: doc-source-001 (narrative baseline) and doc-source-002 (richly structured document)

### Playbook Alignment

This testbed was re-evaluated under the amended guidance in `documentation/testbeds.md`, including explicit source-grounding requirements.

A passing validator result is treated as evidence of structural validity only. Source fidelity, tier placement, and architectural suitability are evaluated separately.

---

## Questions Covered

* Should section/chapter/clause structures be represented directly in profile custom fields?
* How should documents with significant embedded media be represented when both document and media structure matter?
* How much edition/version relationship structure should be explicit versus relationship-based?

---

## Baseline Representation

* Record paths:

* `examples/doc-source-001-record.yaml`* `examples/doc-source-002-record.yaml`
* Why baseline reflects the current contract:
* both records use fields permitted by the current draft document profile;
* neither baseline requires an additional candidate structure to validate.
* Validator result:

* doc-source-001: pass* doc-source-002: pass

### Source-Grounding Quality

For doc-source-001:

* `stated_title` and `stated_author` are directly source-grounded.
* contextual and interpretive values are manually supplied for the testbed.
* ingestion timestamps, parser identifiers, analytical categories, and corpus-role labels include test scaffolding.

For doc-source-002:

* title, author, page count, file properties, and document structure can be mechanically inspected from the PDF using Poppler tooling.
* contextual and interpretive values remain separately curated or test-derived.

---

## Variant A

### Goal

Test whether the current relationship model can represent document-structure and embedded-object concerns without introducing additional profile fields.

### Representation

doc-source-001:

* uses a related representation and interpretive notes as an indirect way to discuss document structure;
* does not directly encode intrinsic source subdivisions.

doc-source-002:

* uses related-source and relationship patterns to point to an independently meaningful embedded component.

### Validator Result

* `examples/doc-source-001-variant-a.yaml`: pass
* `examples/doc-source-002-variant-a.yaml`: pass

### Strengths

* Fully executable under the current contract.
* Reuses the general relationship model.
* Provides a workable mechanism for linking independently meaningful source units.
* Avoids requiring the document profile to model the internal metadata of another profile.

### Weaknesses

* Relationship placeholders are not equivalent to intrinsic source-native subdivisions.
* Document subdivisions remain indirect and less machine-queryable.
* Relationship-only representation does not itself provide a stable inventory of document-native structure.
* Embedded-object location may require descriptive notes unless locator behavior is formalized elsewhere.

---

## Variant B

### Goal

Test candidate explicit representations while preserving source-grounding constraints.

### Representation

doc-source-001:

* does not assert invented chapter or section structure;
* keeps narrative segmentation in the Interpretive tier;
* treats opening, escalation, ending, and similar narrative divisions as interpretive segmentation rather than intrinsic document structure.

doc-source-002:

* tests `context.embedded_media_index` as an explicit embedded-object inventory.

### Validator Result

* `examples/doc-source-001-variant-b.yaml`: pass* `examples/doc-source-002-variant-b.yaml`: fail

* unknown field in Context tier: `embedded_media_index`

### Strengths

* Preserves the distinction between source-native structure and interpretive segmentation.
* Demonstrates that inability to exercise a question with one source is a valid testbed result.
* Tests a dedicated embedded-object representation without silently adding it to the document contract.

### Weaknesses

* doc-source-001 cannot legitimately exercise intrinsic document subdivision structure.
* `embedded_media_index` introduces a document-specific indexing mechanism that overlaps with existing relationship behavior.
* A dedicated embedded-media index also raises classification ambiguity for objects such as tables, diagrams, and extracted structured data.

---

## Evidence Summary by Question

### Question: Section / Chapter / Clause Representation

#### Observed Evidence

doc-source-001 does not provide reliable source-native chapter, section, or clause structure for this question. Interpretive narrative segmentation can be produced, but it is not equivalent to intrinsic document structure.

doc-source-002 provides mechanically recoverable source-native structure through the PDF Table of Contents and extracted textual headings.

Examples include:

* Executive Summary* Part 1: Foundational Information
* 1 Framing Risk
* 2 Audience
* 3 AI Risks and Trustworthiness
* 4 Effectiveness of the AI RMF
* Part 2: Core and Profiles
* 5 AI RMF Core
* 6 AI RMF Profiles
* Appendix A through Appendix D

Page references are also mechanically available for at least some subdivisions.

#### Representation Assessment

The current relationship model can point to a separate representation of document structure but does not directly model intrinsic subdivisions.

The document profile therefore retains `document_subdivisions` as a lightweight Reference-tier structure consisting of:

* `kind` — the source-grounded subdivision type;
* `label` — the human-readable subdivision label represented by the source;
* `source_locator` — an optional source-specific locator identifying the subdivision.

The NIST source provides direct evidence that this minimum shape can represent intrinsic document structure such as parts, numbered sections, and appendices.

For v0.1, this shape is intentionally lightweight. The current evidence does not justify adding explicit hierarchy, subdivision identifiers, nesting, normalized locator objects, or a controlled subdivision vocabulary.

#### Tier-Placement Decision

Intrinsic source-native document structure belongs in the **Reference tier** because it describes structure asserted by or mechanically observable in the source artifact.

This includes structures such as:

* parts;
* chapters;
* sections;
* clauses;
* appendices;
* comparable source-native subdivisions.

Analyst-imposed or interpretive segmentation does not become document structure merely because it can be represented as sections. Such segmentation remains in the Interpretive tier.

Tier placement follows the nature and grounding of the metadata, not merely whether the value was entered by a parser or by a human curator.

#### Remaining Open Issues

The following are deferred rather than blockers for the v0.1 contract:

* whether later evidence requires explicit hierarchy or parent/child relationships among subdivisions;
* whether `source_locator` should eventually receive a normalized structure;
* whether a controlled vocabulary for `kind` would improve interoperability;
* whether Table-of-Contents evidence alone is sufficient for mechanical extraction or should be confirmed against body headings.

These questions do not prevent use of the current minimum shape.

#### Reusability Across Sources

* doc-source-001 does not supply qualifying intrinsic-structure evidence.
* doc-source-002 supplies direct source-native evidence for `kind`, `label`, and `source_locator`.
* the synthetic canonical document example demonstrates the intended shape but does not count as independent testbed evidence.

#### Closure Outcome

**Current contract decision**

`document_subdivisions` is retained in the document profile under the Reference tier with the following v0.1 minimum shape:

* required `kind` string;
* required `label` string;
* conditional, nullable `source_locator` string.

More complex hierarchy and locator structures are deferred until supported by additional evidence.

---

### Question: Document Versus Media / Composite Boundary

#### Observed Evidence

The document profile can represent an independently meaningful embedded object through existing related-source and relationship mechanisms.

A dedicated `embedded_media_index` is not required to express the basic boundary.

#### Tier-Placement Impact

* related-source pointers remain available in Context;
* relationships remain available in Interpretive;
* metadata intrinsic to the externalized object belongs to that object's own profile and record.

#### Profile-Boundary Finding

A dedicated document-specific media index risks requiring the document profile to classify objects that may instead be:

* media;
* structured data;
* another document;
* or another independently meaningful source unit.

The relationship model avoids that profile leakage.

A source locator associated with a relationship may be useful in future work, but this testbed does not establish a contract change for relationship locators.

#### Reusability Across Sources

The relationship pattern is structurally reusable whenever an embedded component becomes independently meaningful enough to receive its own MetaRCI record.

#### Closure Outcome

**Current guidance**

Mechanical detection of embedded content establishes presence, not significance.

The document profile does not require a dedicated `embedded_media_index` in v0.1.

When an implementation or user determines that an embedded component is independently meaningful, that component may receive its own MetaRCI record using the structurally appropriate profile and connect to the document through general MetaRCI relationship mechanisms.

Do not promote `embedded_media_index` from this evidence set.

---

### Question: Edition / Version Explicitness

#### Observed Evidence

Existing fields can express lightweight version and lineage information without introducing a document-specific version structure.

Relevant fields include:

* `reference.stated_version`
* `context.source_lineage`
* `context.related_sources`
* `interpretive.relationships`

#### Source-Grounding Constraint

`stated_version` should be used for version information actually stated by the source.

Edition or publication information known through external evidence should not be converted into a stated source fact merely for convenience. Such information may instead belong in contextual lineage or relationships.

#### Tier-Placement Impact

The existing Reference, Context, and relationship fields are sufficient for the cases exercised by this testbed.

#### Closure Outcome

**Current guidance**

Use `reference.stated_version` only for version or edition information directly stated by or mechanically recoverable from the source artifact.

Use Context and general relationship mechanisms for externally established edition, publication, derivation, predecessor, successor, or revision history.

Analytical claims about differences or significance across versions belong in Interpretive metadata.

No additional document-specific edition/version object is required for v0.1.

---

## Source-Grounding Classification Notes

### doc-source-001

#### Directly Source-Grounded

* `reference.stated_title`
* `reference.stated_author`
* Gutenberg source identifier, verified against the acquired source

#### Externally Curated or Contextual

* `context.domains`
* `context.categories`
* `context.intended_audiences`
* externally established source lineage or publication context

#### Interpretively Derived

* `interpretive.themes`
* `interpretive.concepts`
* narrative segmentation language
* interpretive relationship notes

#### Test Scaffolding

* test-specific `ingestion_timestamp`
* `parser_name` and `parser_version` when supplied only for fixture execution
* testbed `analytical_categories`
* testbed `corpus_role`* test-oriented `intended_purpose`

---

### doc-source-002

#### Directly Source-Grounded or Mechanically Extracted

Using `pdfinfo` and `pdftotext`, the source exposes:

* stated title;
* stated author;
* 48-page extent;
* PDF file properties;
* source-native headings;
* Table-of-Contents structure;
* page references associated with subdivisions.

The mechanical extraction pass also recovered file-level properties suitable for Reference metadata.

#### Externally Curated or Contextual

* domain and category assignments;
* audience characterization where not explicitly stated;
* contextual lineage assertions;
* related-source assignments;
* organizational interpretation beyond mechanically stated source metadata.

#### Interpretively Derived

* analytical categories;
* interpretive relationship notes;
* interpretive concepts and themes.

#### Test Scaffolding

* testbed-specific ingestion timestamps;
* fixture-specific parser identifiers where not recording the actual extraction tool;
* corpus-role labels used only to differentiate test variants;
* test-oriented intended-purpose values.

---

## Mechanical Extraction Evidence: doc-source-002

The PDF was inspected using Poppler utilities.

### `pdfinfo`

Mechanically available properties included:

* Title: Artificial Intelligence Risk Management Framework (AI RMF 1.0)
* Author: National Institute of Standards and Technology
* Pages: 48
* PDF version: 1.7
* File size: 1,946,127 bytes
* Creation date present in PDF metadata
* Modification date present in PDF metadata

### `pdftotext`

The extracted Table of Contents and textual content exposed source-native structural labels including:

* Executive Summary
* Part 1: Foundational Information
* 1 Framing Risk
* 2 Audience
* 3 AI Risks and Trustworthiness
* 4 Effectiveness of the AI RMF
* Part 2: Core and Profiles
* 5 AI RMF Core
* 6 AI RMF Profiles
* Appendix A
* Appendix B
* Appendix C
* Appendix D

Mechanically available locators include page references such as:

* Executive Summary → page 1
* Part 1: Foundational Information → page 4
* Part 2: Core and Profiles → page 20

This evidence establishes that intrinsic subdivision metadata can be mechanically grounded for at least one real document source.

---

## Document Subdivision Contract

### `document_subdivisions`

Current location:

```textprofiles/document.yamlcustom_fields.reference.document_subdivisions```

Current v0.1 shape:

```textlist[object]→ kind→ label→ source_locator```

### Evidence Supporting the Contract

doc-source-002 provides source-native examples for all three properties:

* subdivision kinds such as part, section, and appendix;
* human-readable labels represented directly by the source;
* source-specific locators based on page references.

This evidence supports both the inclusion of intrinsic document subdivisions in the document profile and the usefulness of the current minimum representation.

### v0.1 Design Decision

The v0.1 document profile uses a flat subdivision list containing:

* `kind`
* `label`
* `source_locator`

The profile does not currently require:

* subdivision identifiers;
* explicit nesting;
* parent/child references;
* hierarchy levels;
* controlled values for `kind`;
* structured locator objects.

These features are deferred because the current evidence does not demonstrate that their additional complexity is necessary.

### Current Status

**Current contract for v0.1.**

The minimum `document_subdivisions` shape is considered sufficient for the current document profile. Future testbeds may justify extensions or revisions, but those possibilities do not block the v0.1 document profile.

---

## Final Recommendation

### Document Subdivisions

**Current contract decision**

Retain:

```textcustom_fields.reference.document_subdivisions```

with the v0.1 minimum structure:

```textkindlabelsource_locator```

Intrinsic source-native document structure belongs in Reference.

Interpretive or analyst-imposed segmentation belongs in Interpretive.

Explicit hierarchy, locator normalization, subdivision identifiers, and controlled subdivision vocabularies are deferred until additional evidence demonstrates a need for them.

### Embedded Content Boundary

**Current guidance**

Mechanical detection of embedded content establishes presence, not significance.

The document profile does not require a dedicated embedded-content index in v0.1.

When an implementation or user determines that an embedded component is independently meaningful, represent it with its own MetaRCI record using the structurally appropriate profile and connect it to the document through general relationship mechanisms.

Do not add `embedded_media_index` based on the current evidence.

### Edition / Version Representation

**Current guidance**

Use `reference.stated_version` only for version or edition information directly stated by or mechanically recoverable from the source artifact.

Use Context and general relationship mechanisms for externally established edition, publication, derivation, predecessor, successor, or revision history.

Analytical comparison or significance across versions belongs in Interpretive metadata.

No additional document-specific version structure is required for v0.1.

## Implementation Status

The document-profile decisions exercised by this testbed are synchronized with the current v0.1 implementation:

* `document_subdivisions` is declared under the Reference tier;* the canonical document record uses the Reference-tier subdivision path;* document-subdivision regression tests validate the Reference-tier path and nested field requirements;* no dedicated embedded-content field is added;* no additional document-specific edition/version field is added.

The validator and unit-test suite pass after these changes.

The document profile is stable enough for the current v0.1 evidence set. Deferred questions remain available for future evidence review but do not block the current profile.
