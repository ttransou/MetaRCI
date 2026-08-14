# Structured-Data Profile

## Purpose

The Structured-Data profile covers sources whose meaning depends materially on explicit or recoverable data structure.

## v0.1 Contract

Executable contract in [profiles/structured-data.yaml](profiles/structured-data.yaml):

- Status: active
- Tier overrides: none
- Custom fields:
  - reference.source_fields
  - context.field_context
  - interpretive.field_interpretations

Field identity and locator properties currently supported:

- name
- position
- path
- local_id

## RCI Placement

- Reference: source-native field identity and mechanically recoverable structure.
- Context: externally supplied assertions about those fields.
- Interpretive: inferred assertions about those fields.

Tier placement follows evidentiary basis, not tool origin.

## v0.1 Evidence Summary

Current contract reflects completed structured-data evidence cycle:

1. Reference-level field identity needed first-class representation.
2. Context-level external assertions needed explicit association to Reference fields.
3. Interpretive field-level inferences needed explicit association to Reference fields.

The adopted cross-tier association pattern superseded earlier single-field hypotheses such as variable_definitions.

## Boundaries

- Validation enforces declared structure and types.
- Validation does not yet enforce full semantic sufficiency of locators.
- Guidance requiring enough identity for reliable association remains semantic guidance in v0.1.

## Deferred Beyond v0.1

- stricter locator-resolution checks against Reference entries
- richer domain/value/unit typing systems
- conflict handling across multiple external contextual sources
- cross-version field identity semantics

## Scope Clarification

In v0.1, Structured Data refers to the completed non-relational structured-data profile only.
Structured-Data-Relational is a separate deferred workstream and is not part of v0.1 closure.
