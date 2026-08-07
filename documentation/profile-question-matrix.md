# Profile Question Decision Matrix

## Scope

This matrix defines how to close open profile-development questions using evidence.

Current contract:

* The executable contract is defined by the base schema, profile YAML files, validator behavior, and tests.
* Open questions are not authorization to change schemas.

Current guidance:

* Each question should be closed as either Current guidance, Current contract, or Proposed change.

## Evidence Types

Use one or more of the following evidence sources when closing a question:

* profile YAML definitions in profiles/
* example records in examples/
* validator behavior via `python validate.py`
* regression tests in tests/test_validate.py
* implementation testbed results and recurring cross-implementation patterns

## Closure Outcomes

* Current guidance: no executable change required
* Current contract: already reflected in YAML/validator/tests
* Proposed change: executable change required; record proposal before implementation
* Deferred: explicitly postponed pending evidence or scope decision

## Document Profile

| Open question | Primary evidence needed | Closure threshold | Likely closure outcome | Contract impact if changed |
|---|---|---|---|---|
| Which document-structure elements should remain generic versus move to implementation extensions? | Cross-implementation mapping of repeated fields and extension usage | Same field pattern appears in at least 2 distinct document implementations and is not policy-local | Current guidance or Proposed change | Profile YAML custom fields and tests |
| Should section/chapter/clause structures be represented directly in profile custom fields? | Examples showing repeated structural necessity across document sources | Need cannot be represented cleanly with current relationship model and base fields | Proposed change or Deferred | Profile custom field additions; validator/schema-definition tests |
| How much edition/version relationship structure should be explicit versus relationship-based? | Existing relationship usage in records and testbed records with revisions/translations | Relationship model shown insufficient for repeated cases | Current guidance or Proposed change | Profile docs only, or profile custom fields if upgraded |
| How should documents with significant embedded media be represented when both document and media structure matter? | Paired record experiments (document-only vs split document+media/composite) | One approach consistently preserves meaning with less ambiguity | Current guidance | Usually docs/tests only unless new fields introduced |
| Should any currently base-level document-skewed fields be reconsidered in a future base-schema review? | Base-field usage frequencies across all profile examples and testbeds | Field is repeatedly null/irrelevant outside one profile and better modeled as profile-specific | Proposed change | Base schema revision, profile/test updates, migration notes |

### Document Evidence Update (2026-08-07)

Evidence source:

* documentation/testbed-reports/document-structure-001.md

Observed execution results:

* Baseline pass: examples/doc-source-001-record.yaml
* Baseline pass: examples/doc-source-002-record.yaml
* Variant A pass: examples/doc-source-001-variant-a.yaml
* Variant A pass: examples/doc-source-002-variant-a.yaml
* Variant B pass: examples/doc-source-001-variant-b.yaml
* Variant B fail: examples/doc-source-002-variant-b.yaml (unknown context field embedded_media_index)

Evidence-based status deltas:

* Section/chapter/clause custom field question is now represented by a draft contract patch; keep evaluating shape stability across additional implementations.
* Embedded-media boundary question is now supported as Current guidance: represent materially primary media as related media/composite records using existing relationship patterns.
* Edition/version explicitness question is now supported as Current guidance: use stated_version plus source_lineage or relationships under the current contract.

Step 2 implementation update (2026-08-07):

* A draft contract patch now declares context.document_subdivisions in profiles/document.yaml.
* The document example now exercises this field in examples/document-record.yaml.
* Regression tests now verify required child-property and type enforcement in tests/test_validate.py.

## Structured-Data Profile

| Open question | Primary evidence needed | Closure threshold | Likely closure outcome | Contract impact if changed |
|---|---|---|---|---|
| Which concerns should become executable profile fields versus remain implementation guidance? | Inventory of repeated structured-data metadata needs across datasets | Repeated, structurally reusable need across at least 2 implementations | Proposed change or Current guidance | Profile YAML custom fields and tests |
| How should column or variable definitions be modeled in a reusable way? | Candidate field-shape comparison in example records | One shape supports multiple datasets without domain terms | Proposed change | Add custom nested fields and validation tests |
| How should units, domains, and missing-value conventions be represented? | Comparison of how often these are needed and where tier placement is stable | Stable tier placement and reusable structure emerge | Current guidance or Proposed change | Possibly profile fields plus validator tests |
| Should schema definitions be nested in-record structures or separate related records? | Side-by-side modeling in testbeds; query/retrieval ergonomics | One approach is clearly simpler and less ambiguous for repeated use | Current guidance | Docs only unless contractized |
| How should inferred schema be distinguished from declared schema? | Provenance examples with both inferred and source-declared schemas | Distinction needed to avoid interpretive ambiguity in repeated cases | Proposed change or Current guidance | Profile fields and provenance constraints if contractized |
| Whether to add reusable schema-description custom fields in reference/context/interpretive tiers | Tier placement analysis across examples | Clear, consistent tier placement across implementations | Proposed change | Profile YAML and tests |
| Whether additional validator checks are needed for structured-data-specific semantics | Test failures or ambiguity not caught by current validator | Demonstrable error class missed by current checks | Proposed change | Validator logic and new tests |

### Structured-Data Evidence Update (2026-08-07)

Evidence source:

* documentation/testbed-reports/structured-data-schema-002.md

Observed execution results:

* Baseline pass: examples/data-source-001-record.yaml
* Baseline pass: examples/data-source-002-record.yaml
* Variant A pass: examples/data-source-001-variant-a.yaml
* Variant A pass: examples/data-source-002-variant-a.yaml
* Variant B fail: examples/data-source-001-variant-b.yaml (unknown context field variable_definitions)
* Variant B fail: examples/data-source-002-variant-b.yaml (unknown context field variable_definitions)

Evidence-based status deltas:

* Variable-definition representation now has two-source evidence and is ready as a Proposed change candidate.
* Units, domain, and missing-value representation has two-source evidence and is ready as a Proposed change candidate.
* Inferred-versus-declared schema distinction has two-source evidence and is ready as a Proposed change candidate.

## Media Profile

| Open question | Primary evidence needed | Closure threshold | Likely closure outcome | Contract impact if changed |
|---|---|---|---|---|
| Which media-specific concerns should be represented by profile custom fields? | Repeated media metadata requirements across image/audio/video testbeds | Reusable concerns appear across media subtypes, not just one | Proposed change | Profile YAML custom fields and tests |
| How should captions, transcripts, and accessibility descriptions be represented structurally? | Multiple media examples with accessibility needs | Shared structure works for image/audio/video without overfitting | Proposed change or Current guidance | Profile fields and nested validation tests |
| How should model-generated descriptions record provenance and review state? | Cases with human and machine descriptions, audit/review workflow needs | Repeated need for explicit provenance to avoid ambiguity | Current guidance or Proposed change | Could require profile fields and validator checks |
| How should region/frame/time-segment references be represented? | Segment annotation examples across audio/video/image | A minimal shape captures segments consistently across subtypes | Proposed change or Deferred | Custom nested fields and structural tests |
| Which media properties belong in reference versus context/interpretive tiers? | Tier-placement consistency review across examples | Same tier choices hold across implementations | Current guidance | Docs only unless field moves are needed |
| How to represent machine-generated and human-curated descriptions without ambiguity | Comparison of representation patterns and reviewer outcomes | Ambiguity eliminated in repeated reviews | Current guidance or Proposed change | Possibly new fields and validation expectations |
| Whether to encode region/time segmentation in profile fields or extensions | Extension vs profile reuse analysis | Structural need is broad enough to justify core profile inclusion | Proposed change or Current guidance | Profile YAML changes if promoted |

### Media Evidence Update (2026-08-07)

Evidence source:

* documentation/testbed-reports/media-semantics-001.md

Observed execution results:

* Baseline pass: examples/media-source-001-record.yaml
* Baseline pass: examples/media-source-002-record.yaml
* Variant A pass: examples/media-source-001-variant-a.yaml
* Variant A pass: examples/media-source-002-variant-a.yaml
* Variant B fail: examples/media-source-001-variant-b.yaml (unknown interpretive field generated_descriptions)
* Variant B fail: examples/media-source-002-variant-b.yaml (unknown interpretive field segment_references)

Evidence-based status deltas:

* Generated-description provenance now has two-source evidence and is ready as a Proposed change candidate.
* Caption or transcript structure now has two-source evidence and is ready as a Proposed change candidate.
* Segment-reference representation has source-backed evidence and is ready as a Proposed change candidate.

## Composite Profile

| Open question | Primary evidence needed | Closure threshold | Likely closure outcome | Contract impact if changed |
|---|---|---|---|---|
| What minimum structural signals distinguish a composite from a simple storage container? | Classification trials on candidate bundles | Rule set reduces profile-selection ambiguity in repeated cases | Current guidance | Docs and profile-selection guidance |
| How should expected versus present members be represented? | Incomplete-package scenarios across testbeds | Representation handles unknown/missing members without false certainty | Proposed change or Current guidance | Potential new composite custom fields |
| How should member roles and ordering be expressed? | Cases where order/role changes interpretation | Lightweight structure works across composite use cases | Proposed change or Current guidance | Custom fields and nested validation tests |
| What context may be inherited from the composite record? | Conflict scenarios between collection and member records | Inheritance rule avoids silent override ambiguity | Current guidance | Docs and possibly validator warnings later |
| How should collection-level and item-level metadata conflicts be handled? | Conflict-handling playbook tested on examples | Consistent resolution policy across implementations | Current guidance or Proposed change | Docs, possibly validator checks in future |
| How should completeness be represented when expected membership is unknown? | Partial-ingest and unknown-membership scenarios | One model avoids implying certainty while remaining queryable | Proposed change or Current guidance | Potential custom fields |
| Should cross-profile membership constraints be formalized in profile YAML or remain descriptive guidance? | Composite sets containing document/media/structured-data members | Formal constraints add value over descriptive guidance | Proposed change or Deferred | Composite/profile-validation logic |
| Can and should a composite explicitly contain members validated under different structural profiles? | Multi-profile package testbeds | Cross-profile membership pattern is common and semantically useful | Current guidance or Proposed change | Could require relationship conventions or new fields |
| Should completeness and expected-membership state become first-class fields? | Evidence that relationship-only modeling is insufficient | Repeated inability to express completeness state clearly | Proposed change | Composite custom fields and tests |

## Operating Workflow

1. Capture candidate answers as Current guidance first when no executable change is required.
2. Promote to Current contract only when reflected in YAML/validator/tests.
3. For any Proposed change, create an explicit proposal note before editing schema/profile code.
4. Re-run validation and test suite after executable changes:
   * `python validate.py`
   * `python -m unittest discover -s tests -v`
5. Update profile docs and TODO status labels together to avoid contract/guidance drift.
