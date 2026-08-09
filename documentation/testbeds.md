# MetaRCI Testbed Playbook

## Purpose

This playbook defines how to run implementation testbeds that produce closure-quality evidence for open profile questions.

Current guidance:

* Testbeds evaluate the model.
* Testbeds do not define the model by themselves.
* A record that validates successfully is not necessarily a faithful or appropriate representation of the source.
* Testbed evidence must distinguish source-grounded structure, curated context, interpretive assertions, and test scaffolding.

## Extraction Environment (Current Testbeds)

Current guidance:

* Extraction tooling used in testbeds is infrastructure for evidence collection, not part of the MetaRCI contract.
* MetaRCI remains parser-agnostic; records may capture parser or extractor provenance without requiring one specific implementation.

Current testbed extraction tools:

* Text or Markdown:

   * direct text inspection
* CSV:

   * Python standard-library parsing
* PDF:

   * Poppler utilities (`pdftotext`, `pdfinfo`)

Grounding rule:

* A testbed may only assert mechanically grounded source structure when the source can actually be inspected by the available tooling.

## Outcomes Required Per Testbed

Each testbed must produce:

* one baseline record that validates under the current profile contract;
* one or more variant records that stress open questions;
* a short evidence report using the template in `documentation/testbed-report-template.md`;
* explicit closure recommendations tagged as Current guidance, Current contract, Proposed change, or Deferred.

When a variant represents intrinsic source structure, the represented structure must be demonstrably present in the source artifact.

Do not invent chapters, sections, clauses, regions, segments, headings, members, or other structural units solely to exercise a candidate field.

If a source does not contain the structure needed to exercise an open question:

* record that the source does not provide evidence for that question;
* do not fabricate a structural representation;
* defer that question to another source or testbed;
* distinguish interpretive segmentation from intrinsic source structure.

## Minimum Evidence Packet

For each open question exercised in a testbed, capture:

* question id and profile;
* scenario description;
* source-grounding evidence;
* representation option A (current contract only);
* representation option B (candidate change, if applicable);
* validator result for each option;
* ambiguity notes;
* tier-placement rationale;
* portability notes across at least one additional independent source;
* whether each relevant value is:

  * directly source-grounded;
  * externally curated or contextual;
  * interpretively derived;
  * test scaffolding.

A passing validator result establishes structural validity only. It does not establish that the metadata accurately represents the source or belongs in the selected tier.

## Testbed Sequence

1. Select one profile and one open question cluster.
2. Identify the source-native evidence relevant to the question before constructing variants.
3. Build a baseline record that passes with current YAML.
4. Build one or two controlled variants.
5. For each variant, verify that:

   * source-native structure is represented only when demonstrably present in the source;
   * curated or contextual values are not presented as mechanically grounded source facts;
   * interpretive segmentation is not presented as intrinsic source structure;
   * test scaffolding is not treated as evidence about production metadata behavior.
6. Run validation commands:

   * `python validate.py`
   * `python -m unittest discover -s tests -v`
7. Record findings using the report template.
8. Classify closure outcome:

   * Current guidance
   * Current contract
   * Proposed change
   * Deferred

## Closure Threshold

A question should be promoted to Proposed change only when:

* the same structural need appears in at least two independent testbeds or source contexts;
* the need cannot be represented clearly with current base fields and relationship patterns;
* the candidate shape is profile-reusable and not policy-local;
* the evidence is source-grounded rather than created solely to exercise the proposed structure.

Two records derived from the same artifact do not constitute independent evidence.

Multiple variants within one testbed may demonstrate representational friction, but they do not by themselves satisfy the closure threshold.

## Suggested Initial Testbeds

### Document

* Source set: one narrative document with embedded media and one without.
* Questions: document subdivisions, version relationships, embedded-media boundary.
* Source pack: `documentation/testbed-sources/document-sources.md`

### Structured Data

* Source set: one neutral CSV and one table-like export with units and missing-value conventions.
* Questions: variable definitions, units and domains, inferred versus declared schema.
* Source pack: `documentation/testbed-sources/structured-data-sources.md`

### Media

* Source set: one image set and one audio or video sample.
* Questions: generated-description provenance, captions or transcripts, region or segment references.
* Source pack: `documentation/testbed-sources/media-sources.md`

### Composite

* Source set: one package with complete membership and one with partial or unknown expected membership.
* Questions: expected versus present members, member roles and ordering, completeness semantics.
* Source pack: `documentation/testbed-sources/composite-sources.md`

## Decision Hygiene

* Do not modify the base schema or profile YAML from one testbed result alone.
* Do not promote a candidate field merely because a variant validates successfully.
* Do not invent source structure to make a candidate representation testable.
* Treat a valid but awkward representation as evidence of friction, not automatically as evidence of a schema defect.
* Keep open questions open when evidence is incomplete.
* Record when a source cannot legitimately exercise a question.
* Record rejected alternatives and why.
* Keep proposed changes labeled as Proposed change until the closure threshold is met.
* Sync any closure decision back to profile docs and the question matrix.
