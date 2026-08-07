# Testbed Report

## Header

* Testbed name: document-structure-001
* Profile: document
* Date: 2026-08-07
* Author: GitHub Copilot
* Source set summary: doc-source-001 (narrative baseline) and doc-source-002 (richly structured document)

## Questions Covered

* Should section/chapter/clause structures be represented directly in profile custom fields?
* How should documents with significant embedded media be represented when both document and media structure matter?
* How much edition/version relationship structure should be explicit versus relationship-based?

## Baseline Representation

* Record path: examples/doc-source-001-record.yaml and examples/doc-source-002-record.yaml
* Why baseline reflects current contract: both records use inherited base fields plus existing document overrides only.
* Validator result: pass for both records.

## Variant A

* Goal: represent subdivision and embedded-media boundary using only current contract fields.
* Representation:
  * doc-source-001: relationship and interpretive note placeholders for subdivisions.
  * doc-source-002: related source and relationship link to an externalized media component record id.
* Validator result:
  * examples/doc-source-001-variant-a.yaml: pass
  * examples/doc-source-002-variant-a.yaml: pass
* Strengths:
  * fully executable under current contract.
  * relies on reusable base relationship model.
* Weaknesses:
  * subdivision semantics are implicit and less machine-actionable.
  * embedded-media details are captured indirectly.

## Variant B (optional)

* Goal: test explicit structured fields for subdivisions and embedded-media index.
* Representation:
  * doc-source-001 adds context.document_subdivisions.
  * doc-source-002 adds context.embedded_media_index.
* Validator result:
  * examples/doc-source-001-variant-b.yaml: pass
  * examples/doc-source-002-variant-b.yaml: fail
    * Unknown fields in context tier: embedded_media_index
* Strengths:
  * more explicit and queryable candidate structures.
* Weaknesses:
  * embedded-media index shape remains outside the current document profile contract.

## Evidence Summary by Question

For question: section/chapter/clause representation

* Observed ambiguity: reduced for subdivision representation after adding explicit typed structure.
* Tier-placement impact: context tier supports a reusable subdivision list-object shape.
* Reusability across sources: demonstrated in both narrative and standards-style documents.
* Extension-only viability: no longer required for baseline subdivision representation.
* Candidate closure outcome: Proposed change (implemented in draft contract)

For question: document versus media/composite boundary

* Observed ambiguity: document-only modeling can represent boundary through relationships without schema changes.
* Tier-placement impact: relationship remains in interpretive; related-source pointers remain in context.
* Reusability across sources: yes, both sources can use this pattern.
* Extension-only viability: not required for baseline expression.
* Candidate closure outcome: Current guidance

For question: edition/version explicitness

* Observed ambiguity: stated_version plus source_lineage can express common version context.
* Tier-placement impact: reference and context fields are sufficient for this testbed.
* Reusability across sources: yes.
* Extension-only viability: not required for this evidence set.
* Candidate closure outcome: Current guidance

## Proposed Change Candidate (if any)

* Candidate field or rule: context.document_subdivisions (list<object>)
* Profile location: profiles/document.yaml custom_fields.context
* Why current contract is insufficient: no typed, reusable structure for subdivision indexing.
* Why extension-only is insufficient: extension-only approach reduces cross-implementation consistency.
* Required implementation bundle:
  * profile YAML update
  * example record update
  * tests update
  * docs update

## Final Recommendation

* Keep open / close as guidance / propose contract change / defer:
  * Subdivision structure moved to Proposed change and implemented in draft contract; keep monitoring for shape refinements across additional corpora.
  * Close embedded-media boundary as Current guidance (prefer relationship to media/composite when media is materially primary).
  * Close edition/version explicitness as Current guidance (use stated_version plus source_lineage/relationships).
* Required next evidence step:
  * run the same Variant A and B pattern on an additional independent document corpus outside the current two-source pair, then decide whether to keep, narrow, or extend document_subdivisions item properties.