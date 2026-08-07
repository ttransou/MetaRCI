# Structured-Data Testbed Source Pack

## Goal

Prepare two structured-data source sets that stress variable semantics and schema provenance.

## Source Set A: Neutral Tabular Baseline

* intake id: data-source-001
* profile target: structured-data
* purpose: establish baseline structured-data behavior with simple columns

Suggested files:

* data-source-001/source.csv
* data-source-001/data-dictionary.md

Required characteristics:

* stable row/column shape
* plain value types (string, integer, float, date)
* minimal controlled-value usage

Question coverage:

* baseline variable/column modeling
* inferred versus declared schema distinction setup

## Source Set B: Units and Missing-Value Conventions

* intake id: data-source-002
* profile target: structured-data
* purpose: stress domains, units, and missing-value semantics

Suggested files:

* data-source-002/source.csv or source.tsv
* data-source-002/data-dictionary.md
* data-source-002/missing-value-conventions.md

Required characteristics:

* at least one numeric field with unit
* at least one enumerated or constrained value domain
* at least two missing-value codes or conventions

Question coverage:

* variable-definition structure
* unit and domain placement
* missing-value representation

## Intake Completion Checklist

* source location recorded
* license/usage status recorded
* normalization steps recorded
* known limitations recorded
* baseline readiness set in documentation/testbed-source-intake.md
