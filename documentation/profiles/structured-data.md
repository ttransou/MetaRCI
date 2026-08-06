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

## Current Decisions Supported by YAML

Current contract:

* Status is draft.
* No profile-specific overrides are currently declared.
* No profile-specific custom fields are currently declared.

## Unresolved Questions

Open question:

* Whether to add reusable schema-description custom fields in reference/context/interpretive tiers.
* Whether additional validator checks are needed for structured-data-specific semantics.

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
