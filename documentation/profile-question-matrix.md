# Profile Question Decision Matrix

## Scope

This matrix tracks open architectural questions after v0.1 contract reconciliation.

The executable contract is defined by YAML profiles, validator behavior, examples, and tests.
Open questions are not authorization to change contracts without evidence.

## Current v0.1 Contract Closures

- document: minimal specialization with Reference-tier document_subdivisions and requirement strengthening for page_count, stated_title, stated_author
- structured-data: source_fields, field_context, field_interpretations
- media: Reference technical fields, Context supplied assertions, Interpretive generated assertions plus temporal_segments
- composite: Reference-tier components only

## Active Questions by Profile

### Document

- Should locator semantics for document_subdivisions be normalized beyond source_locator?
- Is additional hierarchy needed beyond the v0.1 minimal subdivision shape?

### Structured Data

- Should locator-resolution checks be enforced against existing Reference entries?
- Which field-level semantics should be typed more strictly without overfitting datasets?

### Media

- Which rights/licensing and attribution-role structures should move from guidance to contract?
- What minimum additional temporal/region structures are broadly reusable?

### Composite

- Is expected-versus-present membership worth a first-class field in a future version?
- Are completeness and role semantics reusable enough for contractization?

## Deferred Workstreams (Outside v0.1)

- Structured-Data-Relational contract development and closure
- Composite semantics beyond reference.components
- Rich governance metadata where only structural placeholders currently exist

## Evidence Rule

A proposed contract change requires recurring cross-source evidence and should not be justified by a single testbed or one profile's documentation volume.
