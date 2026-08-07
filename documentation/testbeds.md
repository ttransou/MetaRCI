# MetaRCI Testbed Playbook

## Purpose

This playbook defines how to run implementation testbeds that produce closure-quality evidence for open profile questions.

Current guidance:

* Testbeds evaluate the model.
* Testbeds do not define the model by themselves.

## Outcomes Required Per Testbed

Each testbed must produce:

* one baseline record that validates under the current profile contract;
* one or more variant records that stress open questions;
* a short evidence report using the template in documentation/testbed-report-template.md;
* explicit closure recommendations tagged as Current guidance, Current contract, Proposed change, or Deferred.

## Minimum Evidence Packet

For each open question exercised in a testbed, capture:

* question id and profile;
* scenario description;
* representation option A (current contract only);
* representation option B (candidate change, if applicable);
* validator result for each option;
* ambiguity notes;
* tier-placement rationale;
* portability notes across at least one additional source.

## Testbed Sequence

1. Select one profile and one open question cluster.
2. Build baseline record that passes with current YAML.
3. Build one or two controlled variants.
4. Run validation commands:
   * python validate.py
   * python -m unittest discover -s tests -v
5. Record findings using the report template.
6. Classify closure outcome:
   * Current guidance
   * Current contract
   * Proposed change
   * Deferred

## Closure Threshold

A question should be promoted to Proposed change only when:

* the same structural need appears in at least two independent implementations;
* the need cannot be represented clearly with current base fields and relationship patterns;
* the candidate shape is profile-reusable and not policy-local.

## Suggested Initial Testbeds

### Document

* Source set: one narrative document with embedded media and one without.
* Questions: document subdivisions, version relationships, embedded-media boundary.
* Source pack: documentation/testbed-sources/document-sources.md

### Structured Data

* Source set: one neutral CSV and one table-like export with units and missing-value conventions.
* Questions: variable definitions, units and domains, inferred versus declared schema.
* Source pack: documentation/testbed-sources/structured-data-sources.md

### Media

* Source set: one image set and one audio or video sample.
* Questions: generated-description provenance, captions or transcripts, region or segment references.
* Source pack: documentation/testbed-sources/media-sources.md

### Composite

* Source set: one package with complete membership and one with partial or unknown expected membership.
* Questions: expected versus present members, member roles and ordering, completeness semantics.
* Source pack: documentation/testbed-sources/composite-sources.md

## Decision Hygiene

* Do not modify base schema or profile YAML from one testbed result alone.
* Keep open questions open when evidence is incomplete.
* Record rejected alternatives and why.
* Sync any closure decision back to profile docs and the question matrix.
