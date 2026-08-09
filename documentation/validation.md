# MetaRCI Validation Guide

## Overview

MetaRCI includes a command-line validator that checks whether a base schema, structural profile, and metadata record conform to the framework’s rules.

The validator is implemented in:

```text
validate.py
```

It validates the relationship among three YAML document types:

```text
Base schema → Profile → Record
```

The base schema defines the shared metadata vocabulary and minimum validation contract.

A profile applies that contract to a structural source class. It may strengthen selected constraints, narrow existing controlled values, and add structurally necessary custom fields.

A record contains metadata values describing an actual source and must conform to the effective schema produced by the base schema and selected profile.

The validator performs structural, compatibility, and recursive value validation. It reports multiple errors within a safe validation stage rather than stopping after the first issue.

---

## Requirements

The validator requires:

* Python 3.10 or later;
* the dependencies listed in `requirements.txt`.

Install the dependencies from the repository root:

```bash
python -m pip install -r requirements.txt
```

---

## Default Validation

From the repository root, run:

```bash
python validate.py
```

Without command-line arguments, the validator uses the repository’s default example files:

```text
schemas/metarci-base.yaml
profiles/example-profile.yaml
examples/example-record.yaml
```

A successful run ends with:

```text
OK: Validation completed with no errors.
```

The validator also prints the resolved paths of the files it checked:

```text
Validated files:
  Base:    /path/to/MetaRCI/schemas/metarci-base.yaml
  Profile: /path/to/MetaRCI/profiles/example-profile.yaml
  Record:  /path/to/MetaRCI/examples/example-record.yaml
```

---

## Validating Other Files

The validator accepts optional command-line arguments for the base schema, profile, and record.

```bash
python validate.py \
  --base schemas/metarci-base.yaml \
  --profile profiles/example-profile.yaml \
  --record examples/example-record.yaml
```

A different profile and record may be supplied in the same way:

```bash
python validate.py \
  --base schemas/metarci-base.yaml \
  --profile profiles/document.yaml \
  --record examples/document-record.yaml
```

The available arguments are:

| Argument    | Purpose                                   |
| ----------- | ----------------------------------------- |
| `--base`    | Path to the MetaRCI base-schema YAML file |
| `--profile` | Path to the structural-profile YAML file  |
| `--record`  | Path to the metadata-record YAML file     |

Display command-line help with:

```bash
python validate.py --help
```

---

## Validation Model

MetaRCI validation occurs in stages.

The validator stops after a failed stage when later validation would depend on invalid or unavailable structures. Within a safe stage, it collects and reports all detected errors.

This avoids two common problems:

1. reporting only one error at a time;
2. producing misleading cascade errors after a foundational structure has already failed.

---

## Validation Stages

### 1. YAML Loading

The validator first confirms that all three files:

* exist;
* are readable;
* contain valid YAML;
* resolve to YAML mappings.

Malformed YAML or missing files cause immediate failure.

Example:

```text
ERROR: while parsing a block mapping
```

---

### 2. Root Validation

Each document must contain its expected root key:

| Document    | Required root     |
| ----------- | ----------------- |
| Base schema | `metarci`         |
| Profile     | `metarci_profile` |
| Record      | `metarci_record`  |

Example failure:

```text
VALIDATION FAILED: Root validation reported 1 error(s).
  1. Record is missing the 'metarci_record' root.
```

---

### 3. Document Validation

The validator checks the top-level structure of each document.

For the base schema, this includes:

* required metadata;
* valid lifecycle status;
* principles;
* tier declarations;
* tier field containers.

For the profile, this includes:

* required profile metadata;
* valid lifecycle status;
* implementation metadata;
* the declared base-schema path;
* profile override containers;
* custom-field containers.

For the record, this includes:

* required record metadata;
* the declared profile path;
* Reference, Context, and Interpretive tier mappings.

Example failure:

```text
VALIDATION FAILED: Document validation reported 1 error(s).
  1. Record tier 'context' must be a mapping.
```

---

### 4. Schema-Definition Validation

The validator checks the field definitions declared by the base schema and profile.

Each complete field definition must declare:

* a valid `type`;
* a valid `requirement`;
* a Boolean `nullable` value.

Supported field types are:

```text
string
integer
list
object
date
datetime
```

Supported requirement values are:

```text
required
recommended
conditional
optional
```

The validator also checks:

* list item types;
* nested object properties;
* object properties within lists;
* `allowed_values`;
* custom-field definitions;
* profile override targets;
* MetaRCI 0.1 override constraints.

---

## Profile Override Validation

MetaRCI 0.1 permits shallow, non-structural profile overrides.

Profiles may override only:

```text
requirement
nullable
description
allowed_values
```

Structural attributes are not overridable in version `0.1`, including:

```text
type
item_type
properties
item_properties
```

A profile must use a custom field or request a base-schema revision when a structural change is required.

### Requirement Strength

Profiles may strengthen a field requirement but may not weaken it.

The validator applies the following order:

```text
optional < conditional < recommended < required
```

Valid examples include:

```text
optional → recommended
optional → required
conditional → recommended
conditional → required
recommended → required
```

Invalid examples include:

```text
required → recommended
required → optional
recommended → conditional
recommended → optional
conditional → optional
```

Example failure:

```text
VALIDATION FAILED: Schema-definition validation reported 1 error(s).
  1. Override for 'reference.source_id' weakens requirement
     from 'required' to 'optional'. Profiles may strengthen
     requirements but may not weaken them.
```

### Nullability

Profiles may strengthen nullability by changing a nullable field to non-nullable.

Valid:

```text
nullable: true → nullable: false
```

Profiles may not weaken nullability by changing a non-nullable field to nullable.

Invalid:

```text
nullable: false → nullable: true
```

Example failure:

```text
VALIDATION FAILED: Schema-definition validation reported 1 error(s).
  1. Override for 'reference.source_id' changes a non-nullable
     base field to nullable.
```

### Allowed Values

Profiles may narrow an existing base `allowed_values` set.

For example, if the base permits:

```yaml
allowed_values:
  - success
  - partial
  - failed
  - skipped
```

a profile may narrow the set:

```yaml
allowed_values:
  - success
  - partial
```

A profile may not:

* introduce `allowed_values` when the base field has none;
* add values not declared by the base;
* expand the base vocabulary.

Example failure:

```text
VALIDATION FAILED: Schema-definition validation reported 1 error(s).
  1. Override for 'reference.extraction_status' expands the
     base allowed-values set with: 'complete'. Profiles may
     only narrow allowed_values.
```

### Descriptions

A profile may replace or refine a field description.

An override description must:

* be a string;
* not be empty.

### Structural Overrides

The following override is invalid:

```yaml
tier_overrides:
  reference:
    page_count:
      type: string
```

The validator reports unsupported override attributes:

```text
VALIDATION FAILED: Schema-definition validation reported 1 error(s).
  1. Unsupported override attributes for 'reference.page_count':
     type. MetaRCI 0.1 permits overrides only for:
     allowed_values, description, nullable, requirement.
```

---

## Custom-Field Validation

Profiles may add structurally necessary custom fields.

Custom fields must:

* belong to the Reference, Context, or Interpretive tier;
* use a supported MetaRCI field type;
* declare `requirement`;
* declare `nullable`;
* satisfy nested schema-definition rules;
* use a name not already declared by the base schema.

A custom field may not replace or shadow a base field.

The following is invalid:

```yaml
custom_fields:
  reference:
    source_id:
      type: string
      requirement: required
      nullable: false
```

Example failure:

```text
VALIDATION FAILED: Schema-definition validation reported 1 error(s).
  1. Custom fields in the reference tier duplicate fields
     declared by the base schema: source_id. Use tier_overrides
     to specialize an existing base field.
```

---

### 5. Version Compatibility

The profile declares the version of the base schema it extends:

```yaml
base_version: "0.1.0"
```

The record declares the version of the profile it uses:

```yaml
profile_version: "0.1.0"
```

The validator currently requires exact version matches.

It checks:

```text
profile.base_version == base.version
record.profile_version == profile.version
```

Example failure:

```text
VALIDATION FAILED: Version compatibility reported 1 error(s).
  1. Profile base_version does not match the loaded base-schema version.
     Expected '0.1.0', got '9.9.9'.
```

---

### 6. Effective Schema Resolution

After the base schema and profile have been validated, the validator resolves the effective schema for each tier.

The effective schema combines:

1. base-schema fields;
2. permitted profile overrides;
3. profile custom fields.

For a base field, a profile override changes only the explicitly supplied permitted attributes. All other attributes remain inherited from the base definition.

Custom fields are then added to the selected tier.

Schema resolution occurs only after override and custom-field constraints have passed validation.

---

### 7. Record-Structure Validation

The validator checks each record tier against the resolved schema.

It verifies that:

* all required fields are present;
* required fields are not null;
* all record fields are declared;
* no unknown fields have been introduced.

Example failure:

```text
VALIDATION FAILED: Record structure reported 1 error(s).
  1. Missing required fields in reference tier: source_id
```

Unknown fields also fail:

```text
VALIDATION FAILED: Record structure reported 1 error(s).
  1. Unknown fields in context tier: mystery_field
```

---

### 8. Recursive Record-Value Validation

The validator recursively checks record values against their resolved field definitions.

This includes:

* scalar value types;
* nullability;
* allowed values;
* list item types;
* nested object properties;
* required nested properties;
* unknown nested properties;
* object entries within lists.

For example, the following invalid value:

```yaml
page_count: twelve
```

fails because `page_count` is declared as an integer:

```text
Value 'reference.page_count' must be type 'integer',
but received 'str'.
```

Nested validation reports the complete path to the invalid value:

```text
context.sensitivity.categories[1]
```

or:

```text
interpretive.relationships[0].relationship_type
```

---

## Error Aggregation

The validator collects multiple errors within a safe validation stage.

For example, a record containing three independent value errors may produce:

```text
VALIDATION FAILED: Record-value validation reported 3 error(s).
  1. Value 'reference.page_count' must be type 'integer',
     but received 'str'.
  2. Value for 'reference.extraction_status' must be one of:
     'success', 'partial', 'failed', 'skipped'. Received 'complete'.
  3. Value 'context.alternate_titles[1]' must be type 'string',
     but received 'int'.
```

The validator does not continue into later stages when doing so would create misleading errors.

For example, it does not attempt record-value validation when the record tiers are not valid mappings.

---

## Exit Codes

The validator uses standard process exit codes.

| Exit code | Meaning                           |
| --------- | --------------------------------- |
| `0`       | Validation completed successfully |
| `1`       | Loading or validation failed      |

This allows the validator to be used in shell scripts, automated tests, and continuous-integration workflows.

Example:

```bash
python validate.py
echo $?
```

A successful validation prints:

```text
0
```

A failed validation prints:

```text
1
```

---

## Automated Tests

The validator includes an automated regression suite in:

```text
tests/test_validate.py
```

Run all tests from the repository root:

```bash
python -m unittest discover -s tests -v
```

The current suite tests:

* valid base, profile, and record files;
* invalid controlled values;
* incorrect scalar types;
* malformed list items;
* nested sensitivity fields;
* relationship objects;
* missing required fields;
* unknown record fields;
* malformed record tiers;
* base-schema version mismatches;
* profile-version mismatches;
* invalid schema field definitions;
* malformed nested schema definitions;
* invalid profile overrides;
* overrides targeting unknown fields;
* incorrect base-schema paths;
* incorrect profile paths;
* missing YAML roots;
* malformed YAML;
* aggregated value errors.

Additional tests should cover the MetaRCI 0.1 profile constraints:

* valid profile/record combinations for each structural profile;
* unsupported structural overrides;
* weakened requirements;
* weakened nullability;
* expanded `allowed_values`;
* newly introduced override vocabularies;
* custom fields that duplicate base fields;
* profile-specific required fields enforced through the effective schema;
* profile-specific field type enforcement for custom fields;
* profile-specific nested structure enforcement for custom object fields.
* structured-data `reference.source_fields` locator property types.
* structured-data `context.field_context` required field and external source attribution.
* structured-data `context.field_context` nested locator and list item types.
* structured-data `interpretive.field_interpretations` required field locator.
* structured-data `interpretive.field_interpretations` inferred-value and evidence-basis property types.

Each test creates temporary copies of the valid example files. The tests modify only those temporary copies and do not alter the repository’s canonical examples.

A successful test run ends with output similar to:

```text
----------------------------------------------------------------------
Ran 61 tests

OK
```

---

## Continuous Integration

MetaRCI uses GitHub Actions to run validation automatically.

The workflow is defined in:

```text
.github/workflows/validate.yaml
```

The workflow runs on:

* pushes;
* pull requests;
* manual workflow dispatch.

The workflow performs these steps:

1. checks out the repository;
2. configures Python;
3. installs dependencies from `requirements.txt`;
4. runs the validator against the example files;
5. runs the complete automated test suite.

The local commands executed by CI are:

```bash
python -m pip install -r requirements.txt
python validate.py
python -m unittest discover -s tests -v
```

A successful workflow confirms that:

* the canonical examples remain valid;
* all regression tests pass;
* recent changes have not broken the validator contract.

The workflow can also be started manually from the repository’s GitHub page:

```text
Actions → Validate MetaRCI → Run workflow
```

---

## Successful Validation Example

A successful run includes:

```text
OK: All YAML files parsed successfully.
OK: Expected MetaRCI roots are present.
OK: Base-schema document structure is valid.
OK: Base-schema metadata and lifecycle status are valid.
OK: Base-schema principles are valid.
OK: Reference, Context, and Interpretive tiers are present.
OK: Base-tier document structures are valid.
OK: Profile document structure is valid.
OK: Profile extends the loaded base schema.
OK: Profile implementation metadata is valid.
OK: Record document structure is valid.
OK: Record references the loaded profile.
OK: Record tiers are valid mappings.
OK: Base and profile schema definitions are valid.
OK: Profile overrides target declared base fields.
OK: Profile override constraints are satisfied.
OK: Profile overrides and custom fields were resolved.
OK: Profile base_version matches the base schema.
OK: Record profile_version matches the profile.
OK: Required fields are present across all tiers.
OK: Record fields are declared by the resolved profile.
OK: Record values passed recursive type validation.
OK: Declared allowed values are satisfied.
OK: Nested lists and objects match their schemas.
OK: Recursive record validation completed successfully.
OK: Validation completed with no errors.
```

---

## Current Scope

The validator currently supports validation of one base schema, one profile, and one record per command.

It uses exact version matching rather than semantic-version compatibility rules.

MetaRCI 0.1 profile overrides are intentionally shallow and non-structural.

The validator does not currently:

* validate multiple records in one command;
* produce JSON-formatted diagnostics;
* export JSON Schema;
* install as a packaged command-line application;
* resolve remote schema or profile references;
* apply semantic-version ranges;
* support profile-to-profile inheritance;
* deep-merge nested profile overrides;
* perform domain-specific factual validation.

These may be considered in later versions without changing the fundamental validation model.

---

## Design Principle

The validator is intended to make MetaRCI metadata inspectable and enforceable.

A MetaRCI record should not merely contain metadata-shaped values. It should be possible to determine:

* where each field was declared;
* which profile rules apply;
* whether a profile strengthens or weakens the base contract;
* whether custom fields preserve the shared vocabulary;
* whether required context is present;
* whether values conform to their declared types;
* whether nested structures are complete;
* whether the record is compatible with the schema and profile versions it references.

The validator therefore treats metadata structure, provenance, context, profile governance, and compatibility rules as testable parts of the framework rather than informal documentation.
