# Testbed Report: Structured-Data Schema Semantics 001

## Header

* Testbed name: structured-data-schema-001
* Profile: structured-data
* Date: 2026-08-07
* Author: repo working draft
* Source set summary: one baseline structured-data record plus two modeled variants focused on variable-definition and inferred-versus-declared schema semantics.

## Executed Evidence

Command run:

* python -m unittest -v tests.test_validate.MetaRCIValidatorTests.test_structured_data_profile_and_record_pass tests.test_validate.MetaRCIValidatorTests.test_structured_data_profile_required_custom_field_is_enforced

Observed result:

* Ran 2 tests in 0.211s
* OK
* Baseline structured-data profile and record pass.
* Required profile custom-field enforcement behavior is confirmed by tests.

## Questions Covered

From documentation/profiles/structured-data.md:

* How should column or variable definitions be modeled in a reusable way?
* How should units, domains, and missing-value conventions be represented?
* Should schema definitions be nested in-record structures or separate related records?
* How should inferred schema be distinguished from declared schema?
* Whether to add reusable schema-description custom fields in reference/context/interpretive tiers.
* Whether additional validator checks are needed for structured-data-specific semantics.

## Baseline Representation

* Record path: examples/structured-data-record.yaml
* Why baseline reflects current contract:
  * Uses inherited base fields only.
  * Uses context and interpretive metadata plus relationship links.
  * Requires no structured-data custom fields.
* Validator result:
  * Valid under current contract when paired with profiles/structured-data.yaml.

## Variant A

* Goal: represent schema details without contract changes.
* Representation:
  * Keep profile unchanged.
  * Add schema and variable notes using interpretive.interpretive_notes and relationship links to schema sources.
  * Keep units and missing-value conventions in textual metadata.
* Validator result:
  * Expected to pass because only existing base fields are used.
* Strengths:
  * No profile or validator change required.
  * Fast and compatible with current tooling.
* Weaknesses:
  * Variable-level details are weakly structured and harder to query.
  * Inferred-versus-declared distinction is not machine-clear.

## Variant B

* Goal: evaluate a candidate reusable shape for variable metadata.
* Representation:
  * Candidate field (proposal only, not implemented):
    * context.variable_definitions: list<object>
    * child properties: variable_name, value_type, unit, value_domain, missing_value_rule, schema_source_type
  * schema_source_type would distinguish declared versus inferred schemas.
* Validator result:
  * Not executable under current contract unless profile YAML adds this custom field.
* Strengths:
  * Improves queryability and consistency for variable semantics.
  * Supports explicit declared-versus-inferred schema provenance.
* Weaknesses:
  * Requires profile custom field introduction and nested validation tests.
  * Needs proof of cross-implementation reuse.

## Evidence Summary by Question

### 1) Variable-definition representation

* Observed ambiguity:
  * Baseline can describe variable intent but not in a consistent structured shape.
* Tier-placement impact:
  * Candidate field plausibly belongs in context.
* Reusability across sources:
  * Plausible but unproven with only one testbed.
* Extension-only viability:
  * Viable short-term; weaker for interoperability.
* Candidate closure outcome:
  * Proposed change candidate pending second testbed.

### 2) Units, domains, and missing-value conventions

* Observed ambiguity:
  * Baseline supports narrative representation but not robust, queryable structure.
* Tier-placement impact:
  * Candidate metadata appears context-oriented.
* Reusability across sources:
  * Needs multi-dataset confirmation.
* Extension-only viability:
  * Reasonable interim path.
* Candidate closure outcome:
  * Current guidance now; Proposed change possible with more evidence.

### 3) Nested schema object vs separate related record

* Observed ambiguity:
  * Both approaches are possible under guidance; contract does not choose.
* Tier-placement impact:
  * No immediate base-tier conflict.
* Reusability across sources:
  * Unknown; must compare at least two implementations.
* Extension-only viability:
  * High, pending decision.
* Candidate closure outcome:
  * Keep open for now.

### 4) Inferred versus declared schema distinction

* Observed ambiguity:
  * Baseline cannot represent distinction as a first-class, machine-checkable structure.
* Tier-placement impact:
  * Candidate field attribute fits context semantics.
* Reusability across sources:
  * Likely broad but currently unproven.
* Extension-only viability:
  * Viable but may diverge across implementations.
* Candidate closure outcome:
  * Proposed change candidate pending additional evidence.

### 5) Additional validator checks for structured-data semantics

* Observed ambiguity:
  * No structured-data-specific semantic checks currently enforced.
* Tier-placement impact:
  * Not applicable.
* Reusability across sources:
  * Depends on selected contract shape.
* Extension-only viability:
  * N/A for core contract checks.
* Candidate closure outcome:
  * Deferred until profile field shape is settled.

## Proposed Change Candidate (if any)

* Candidate field or rule:
  * context.variable_definitions as list<object> with variable_name, value_type, unit, value_domain, missing_value_rule, schema_source_type.
* Profile location:
  * profiles/structured-data.yaml custom_fields.context
* Why current contract is insufficient:
  * Cannot capture variable-level semantics in a consistent, queryable, reusable structure.
* Why extension-only is insufficient:
  * Extension-only modeling risks divergent semantics between implementations.
* Required implementation bundle:
  * profile YAML update
  * example record update
  * tests update for nested variable-definition validation
  * docs update in documentation/profiles/structured-data.md and documentation/profile-question-matrix.md

## Final Recommendation

* Keep open for now, with proposal candidate documented.
* Required next evidence step:
  * run a second structured-data testbed on a different dataset style (for example, statistical table export) and verify whether the same variable_definitions shape remains minimal and reusable.
