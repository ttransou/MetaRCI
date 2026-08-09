You are working in the MetaRCI repository.

Historical note: this instruction set was created for a pre-settlement re-evaluation pass. The current v0.1 document decision state is now reflected in the profile docs, matrix, and testbed report.

Your task is to re-evaluate the existing document testbed under the amended `documentation/testbeds.md` playbook.

Do not modify the base schema, document profile contract, validator, or tests unless explicitly instructed later.

## Scope

Review only the current document testbed materials:

* `documentation/testbeds.md`
* `documentation/testbed-report-template.md`
* `documentation/testbed-reports/` document report(s)
* `examples/doc-source-001-record.yaml`
* `examples/doc-source-001-variant-a.yaml`
* `examples/doc-source-001-variant-b.yaml`
* `examples/doc-source-002-record.yaml`
* existing doc-source-002 variants, if present
* `profiles/document.yaml`

The amended playbook is authoritative for this review.

## Primary Correction

The previous `doc-source-001` Variant B represented:

* opening
* middle
* ending
* narrative shift

as `document_subdivisions`.

These are interpretive narrative segments rather than clearly source-native document subdivisions.

Do not treat them as evidence for intrinsic document structure.

## Required Work

### 1. Preserve the baseline

Do not materially change the `doc-source-001` baseline unless a factual fixture error must be corrected.

### 2. Review Variant A

Keep Variant A as a test of whether the current relationship model can indirectly represent document-structure information.

Explicitly distinguish:

* a related representation of structure;
* intrinsic structure present in the source.

Do not claim that the relationship workaround directly represents source-native subdivisions if it does not.

### 3. Correct Variant B

Revise `doc-source-001-variant-b.yaml` so it does not invent source-native subdivisions.

If *The Yellow Wallpaper* source used in the testbed does not contain explicit sections, chapters, headings, or similar structural divisions:

* do not populate `document_subdivisions`;
* record that this source cannot legitimately exercise the intrinsic-subdivision question;
* keep any narrative segmentation in the Interpretive tier;
* make clear that interpretive segmentation is not equivalent to source structure.

A source that cannot exercise an open question is a valid testbed result.

### 4. Do not change executable contract in this review

Treat `reference.document_subdivisions` as a settled v0.1 document-profile decision. Use this review flow only to evaluate evidence quality and any future extension needs.

Do not modify:

* `profiles/document.yaml`
* `schemas/metarci-base.yaml`
* `validate.py`
* profile-specific tests

as part of this correction.

Do not remove or revise the current subdivision field definition as part of this bounded review.

### 5. Re-evaluate source grounding

For each relevant metadata value in the document testbed, classify it where useful as:

* directly source-grounded;
* externally curated/contextual;
* interpretively derived;
* test scaffolding.

Pay particular attention to:

* `stated_version`
* `source_lineage`
* subdivision-related values
* `intended_purpose`
* `analytical_categories`
* `corpus_role`

Do not treat test-scaffolding values as evidence about production metadata behavior.

### 6. Inspect doc-source-002 next

Use `doc-source-002` as the primary source for exercising intrinsic document subdivisions if it contains explicit source-native headings, sections, clauses, appendices, or other subdivisions.

Any candidate subdivision representation must use labels and locators grounded in the actual source.

Do not invent structural labels solely to exercise the field.

### 7. Update the document testbed report

Revise the report so that it clearly distinguishes:

* validator success;
* source-grounding quality;
* representational friction;
* architectural recommendation.

For the subdivision question, do not state that Context tier placement or contract promotion has been established unless the evidence actually supports it.

Use these outcome categories exactly:

* Current guidance
* Current contract
* Proposed change
* Deferred

## Deliverable

Before editing, summarize:

1. which files you intend to change;
2. which files you will inspect but not change;
3. any existing profile-contract change you discover that appears to have been made prematurely.

Then perform the bounded correction.

After editing:

* run `python validate.py`;
* run `python -m unittest discover -s tests -v`;
* report exact results;
* summarize what changed in the evidence interpretation;
* list any unresolved architectural questions separately.

Do not continue to structured-data, media, composite, profile-specific enforcement tests, or schema revision.
