# Testbed Report

## Header

* Testbed name: structured-data-schema-002
* Profile: structured-data
* Date: 2026-08-07
* Author: GitHub Copilot
* Source set summary: data-source-001 (USGS all_month.csv) and data-source-002 (ERDDAP CSV with units row)

## Questions Covered

* How should column or variable definitions be modeled in a reusable way?
* How should units, domains, and missing-value conventions be represented?
* How should inferred schema be distinguished from declared schema?

## Baseline Representation

* Record path: examples/data-source-001-record.yaml and examples/data-source-002-record.yaml
* Why baseline reflects current contract: both records use inherited base fields and relationship or note patterns only.
* Validator result: pass for both records.

## Variant A

* Goal: represent schema semantics using only current contract fields.
* Representation:
  * data-source-001: inferred schema notes in interpretive_notes and relationship pointers.
  * data-source-002: declared unit semantics represented in interpretive_notes and relationship pointers.
* Validator result:
  * examples/data-source-001-variant-a.yaml: pass
  * examples/data-source-002-variant-a.yaml: pass
* Strengths:
  * fully executable under current contract.
  * avoids profile changes while preserving useful context.
* Weaknesses:
  * variable-level semantics remain weakly structured.
  * declared versus inferred schema remains narrative rather than machine-checkable.

## Variant B (optional)

* Goal: evaluate an explicit reusable variable metadata shape.
* Representation:
  * both sources add context.variable_definitions with fields such as variable_name, value_type, unit, value_domain, missing_value_rule, and schema_source_type.
* Validator result:
  * examples/data-source-001-variant-b.yaml: fail
    * Unknown fields in context tier: variable_definitions
  * examples/data-source-002-variant-b.yaml: fail
    * Unknown fields in context tier: variable_definitions
* Strengths:
  * directly supports queryable variable metadata and declared versus inferred schema distinctions.
* Weaknesses:
  * not part of the current structured-data profile contract.

## Evidence Summary by Question

For question: variable-definition representation

* Observed ambiguity: current contract can describe variable semantics, but does not provide a typed reusable variable list.
* Tier-placement impact: candidate field naturally fits context tier.
* Reusability across sources: demonstrated across both a straightforward feed and a units-heavy CSV.
* Extension-only viability: viable short term, weaker long-term interoperability.
* Candidate closure outcome: Proposed change

For question: units, domains, and missing-value conventions

* Observed ambiguity: units and missing-value rules are representable narratively, not structurally.
* Tier-placement impact: context tier appears stable for candidate unit or domain metadata.
* Reusability across sources: yes, both source types use the same conceptual shape.
* Extension-only viability: workable interim approach.
* Candidate closure outcome: Proposed change

For question: inferred versus declared schema distinction

* Observed ambiguity: distinction is currently encoded only in notes, not enforceable structure.
* Tier-placement impact: candidate schema_source_type attribute fits context variable metadata.
* Reusability across sources: yes, inferred style appears in USGS feed and declared style appears in ERDDAP sample.
* Extension-only viability: possible but likely divergent across implementations.
* Candidate closure outcome: Proposed change

## Proposed Change Candidate (if any)

* Candidate field or rule: context.variable_definitions (list<object>)
* Profile location: profiles/structured-data.yaml custom_fields.context
* Why current contract is insufficient: cannot encode reusable machine-checkable variable semantics.
* Why extension-only is insufficient: inconsistent cross-implementation shapes are likely.
* Required implementation bundle:
  * profile YAML update
  * example record update
  * tests update
  * docs update

## Final Recommendation

* Keep open / close as guidance / propose contract change / defer:
  * keep boundary-first behavior as Current guidance for active use.
  * elevate variable_definitions candidate to Proposed change with this second source-backed evidence packet.
* Required next evidence step:
  * prototype context.variable_definitions in profile YAML with minimal item properties, then validate against both source variants and regression tests.
