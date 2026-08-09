# Testbed Report

## Header

- Testbed name: structured-data-schema-003
- Profile: structured-data
- Date: 2026-08-09
- Author: repo working draft
- Source set summary: `iris.data` as the primary structured-data source and `iris.names` as an external descriptive/schema source.

## Question Covered

- Does externally supplied field-level schema information justify a reusable Context-tier field-association structure?
- Can Context assertions be associated with source-native field identity without duplicating the Reference field definition?
- Does positional field identity provide a sufficient anchor when the primary data artifact does not contain field names?

## Baseline Representation

- Primary record: `examples/data-source-003-record.yaml`
- Schema/documentation record: `examples/data-source-003-schema-record.yaml`
- Primary source: `testbed-sources/structured-data/data-source-003/iris.data`
- External contextual source: `testbed-sources/structured-data/data-source-003/iris.names`

Baseline behavior:

- `iris.data` establishes five source fields through positional identity.
- Field names and semantic descriptions are not imported into Reference because they are supplied by the external `iris.names` artifact.
- The baseline structured-data record validates under the current profile contract.

## Variant A

### Goal

Test a candidate Context-tier structure for assertions about fields whose identity is established in Reference but whose names and semantics are supplied by an external authoritative source.

### Representation

`examples/data-source-003-variant-a.yaml` adds candidate `context.field_context`.

Each field-context entry:

- identifies an existing Reference field using a lightweight `field` locator;
- identifies the external contextual source through `external_source_id`;
- records only assertions supported by `iris.names`;
- does not redefine the Reference field identity.

Example conceptual shape:

```yaml
field_context:
  - field:
      position: 1
    external_source_id: data-source-003-schema
    external_field_name: sepal length
    value_type: numeric
    unit: cm
```

### Validator Result

- `examples/data-source-003-variant-a.yaml`: pass

### Evidence Interpretation

`context.field_context` is now declared in `profiles/structured-data.yaml` and validates as part of the current v0.1 structured-data contract.

The source pair demonstrates a genuine Context-tier need:

- Reference can identify the field position from `iris.data`;
- external documentation supplies the field name and semantics;
- the two assertions require a stable association without collapsing the external information into Reference.

## Evidence Summary

### Positional Field Identity

`iris.data` does not provide field names in the primary data artifact.

The five fields can nevertheless be identified structurally by position.

This supports the current `reference.source_fields` contingency guidance that source-native position may serve as field identity when names are absent.

### External Field Name

`iris.names` supplies names for the positional fields.

Because those names are not asserted by `iris.data`, they should not be promoted into Reference metadata for the primary source.

They are contextual assertions about existing Reference fields.

### External Value Type

`iris.names` identifies the measurement attributes as numeric and the final field as the class attribute.

These assertions derive from the external descriptive source and therefore belong in Context for the primary structured-data record.

### External Unit

`iris.names` supplies centimeter units for the four measurement fields.

The units are externally supplied rather than asserted by `iris.data`, providing direct evidence for Context-tier unit metadata.

### External Value Domain

`iris.names` supplies the class values associated with the fifth field.

This provides direct evidence for a Context-tier externally declared value domain.

## Candidate Closure Outcome

**Current contract decision (v0.1)**

The evidence supports a reusable Context-tier field-association structure.

The candidate should:

- associate Context assertions with an existing `reference.source_fields` identity;
- use a lightweight field locator rather than duplicate the entire Reference field definition;
- preserve per-assertion provenance through an external source identifier;
- support externally supplied field names and semantic properties demonstrated by evidence.

The current candidate name is:

`context.field_context`

The minimum executable item shape is now implemented in `profiles/structured-data.yaml`.

## Next Step

Keep the current v0.1 field-association shape stable while gathering additional evidence for deferred items such as stricter locator-resolution semantics and cross-source conflict handling.

## Additional Evidence Snapshot (2026-08-09)

- Candidate record: `examples/data-source-001-variant-c.yaml`
- Primary source used for inference: `testbed-sources/structured-data/data-source-001/data-source-001.csv` (USGS all_month.csv snapshot)
- Purpose: test a candidate Interpretive-tier field-level inference structure grounded in observed source values.
- Candidate field: `interpretive.field_interpretations`
- Field locator strategy: lightweight locator back to `reference.source_fields` using `name` and `position`.
- Inferred assertions exercised:
  - `time` (position 1): inferred datetime-like string pattern from observed ISO-8601 UTC values.
  - `mag` (position 5): inferred numeric value type and variable observed precision.

Validator result:

- `examples/data-source-001-variant-c.yaml`: pass

Evidence interpretation:

- `interpretive.field_interpretations` is now declared in `profiles/structured-data.yaml` and validates under the current v0.1 contract.
- The field-level inference representation tested here moved from contract-boundary candidate to executable profile behavior.

Historical note:

- Earlier execution of this variant failed with unknown `field_interpretations` before profile declaration was added.
- That historical failure is preserved as prior boundary evidence, while current validator behavior confirms contract adoption.