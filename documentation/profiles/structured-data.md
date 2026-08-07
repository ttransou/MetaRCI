# Structured-Data Profile

## Purpose

Current contract:

* The structured-data profile exists as a structural profile named structured-data.
* It extends the base schema at version 0.1.0 and is currently draft.

Current guidance:

* Use this profile when source meaning depends substantially on explicit data structure.

## Structural Characteristics

Current guidance:

* Typical concerns include variables/columns, value domains, keys, granularity, and lineage.

Open question:

* Which of these concerns should become executable profile fields versus remain implementation guidance?

## Profile Emphasis

Current contract:

* The current YAML sets no overrides and no custom fields.
* Effective behavior is currently the base schema behavior.

Current guidance:

* Emphasize schema-aware interpretation rather than file format naming.

## Rationale for Current Fields

Current contract:

* The profile is intentionally boundary-first in 0.1.0: base fields only, no structured-data custom schema yet.
* The example record validates with inherited base fields and relationship/context metadata.

Current guidance:

* This preserves flexibility while evidence is gathered for reusable structured-data additions.

## Relevant Design Questions

Open question:

* How should column or variable definitions be modeled in a reusable way?
* How should units, domains, and missing-value conventions be represented?
* Should schema definitions be nested in-record structures or separate related records?
* How should inferred schema be distinguished from declared schema?
* Whether to add reusable schema-description custom fields in reference/context/interpretive tiers.
* Whether additional validator checks are needed for structured-data-specific semantics.

## Current Decisions Supported by YAML

Current contract:

* Status is draft.
* No profile-specific overrides are currently declared.
* No profile-specific custom fields are currently declared.

Proposed change:

* Introduce profile custom fields only after recurring cross-implementation evidence.

## Boundaries with Other Profiles

Current guidance:

* Prefer document when source is primarily narrative text.
* Prefer media when meaning is primarily visual/audio/spatial.
* Prefer composite when the unit is a package or aggregation of multiple sources.

## Example Applications

Current guidance:

* Tabular datasets, CSV exports, spreadsheet extracts, and machine-readable record sets.

Deferred:

* A heavy schema-language model in profile YAML.

## Closure Candidate Pass (No Implementation)

Current guidance:

* Close as guidance now: keep the structured-data profile boundary-first in 0.1 and continue using inherited base fields plus relationship metadata.
* Close as guidance now: represent schema-sensitive interpretation through context and interpretive metadata until reusable profile-level structures are demonstrated.
* Close as guidance now: prefer lightweight schema representation patterns over heavyweight schema-language embedding in the profile contract.

Open question:

* Keep open: standardized reusable representation for column or variable definitions in profile YAML.
* Keep open: standardized tier placement and structure for units, value domains, and missing-value conventions.
* Keep open: whether inferred-versus-declared schema distinction should be contractized in profile fields.

## Recommended Code Change (Proposal Only)

Proposed change:

* Introduce one optional structured-data custom field in profile YAML to capture reusable variable metadata, for example:
  * `context.variable_definitions` as `list<object>` with minimal child properties such as variable_name, value_type, unit, value_domain, and missing_value_rule.

Current guidance:

* Do not implement yet.
* Implement only after at least two independent structured-data testbeds require reusable variable/column representation that cannot be expressed clearly with current base fields and relationships.

If later approved, the implementation bundle should include:

* profile YAML update in `profiles/structured-data.yaml`;
* example update in `examples/structured-data-record.yaml`;
* positive/negative regression tests in `tests/test_validate.py` for nested variable-definition validation;
* documentation updates in this file and `documentation/profile-question-matrix.md`.
