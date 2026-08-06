# MetaRCI Validation Guide

## Overview

MetaRCI includes a command-line validator that checks whether a base schema, implementation profile, and metadata record conform to the framework’s structural and validation rules.

The validator is implemented in:

```text
validate.py
```

It validates the relationship among three YAML document types:

```text
Base schema → Profile → Record
```

The base schema defines the available metadata fields and their rules. A profile selects, modifies, or extends those rules for a particular domain or corpus. A record contains metadata values that must conform to the resolved profile.

The validator performs both structural and value-level validation. It also reports multiple errors within a validation stage rather than stopping after the first issue.

---

## Requirements

The validator requires:

* Python 3.10 or later
* the dependencies listed in `requirements.txt`

Install PyYAML with:

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
  --profile profiles/humanities-profile.yaml \
  --record examples/hamlet-record.yaml
```

The available arguments are:

| Argument    | Purpose                                      |
| ----------- | -------------------------------------------- |
| `--base`    | Path to the MetaRCI base-schema YAML file    |
| `--profile` | Path to the implementation-profile YAML file |
| `--record`  | Path to the metadata-record YAML file        |

Display the command-line help with:

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
* profile override and custom-field containers.

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

Each field definition must declare:

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
* custom fields;
* profile overrides;
* override targets.

Example failure:

```text
VALIDATION FAILED: Schema-definition validation reported 1 error(s).
  1. Schema field 'reference.page_count' must declare one of
     ['date', 'datetime', 'integer', 'list', 'object', 'string']
     as its type. Received 'number'.
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

The resolved schema combines:

1. base-schema fields;
2. profile overrides;
3. profile custom fields.

For a base field, the profile may override selected attributes such as:

```yaml
requirement: recommended
```

Custom fields are then added to the selected tier.

This produces the field definitions used to validate the record.

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

Nested validation also reports the complete path to the invalid value:

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

The suite currently contains 22 tests.

The tests cover:

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

Each test creates temporary copies of the valid example files. The tests modify only those temporary copies and do not alter the repository’s canonical examples.

A successful test run ends with output similar to:

```text
----------------------------------------------------------------------
Ran 22 tests

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
3. installs PyYAML;
4. runs the validator against the example files;
5. runs the complete automated test suite.

The local commands executed by CI are:

```bash
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

The validator does not currently:

* validate multiple records in one command;
* produce JSON-formatted diagnostics;
* export JSON Schema;
* install as a packaged command-line application;
* resolve remote schema or profile references;
* apply semantic-version ranges;
* perform domain-specific factual validation.

These may be added in later versions without changing the fundamental validation model.

---

## Design Principle

The validator is intended to make MetaRCI metadata inspectable and enforceable.

A MetaRCI record should not merely contain metadata-shaped values. It should be possible to determine:

* where each field was declared;
* which profile rules apply;
* whether required context is present;
* whether values conform to their declared types;
* whether nested structures are complete;
* whether the record is compatible with the schema and profile versions it references.

The validator therefore treats metadata structure, provenance, context, and governance rules as testable parts of the framework rather than informal documentation.
