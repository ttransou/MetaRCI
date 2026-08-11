# Structured-Data-Relational Testbed Source Pack

## Goal

Prepare two relational structured-data source sets that stress declared schema structure, keys, constraints, and relationships across database objects.

## Source Set A: Relational Baseline

* intake id: structured-relational-001
* profile target: structured-data-relational
* candidate source: MySQL Sakila
* purpose: establish baseline relational behavior with explicit tables, columns, keys, constraints, and relationships

Suggested files:

* structured-relational-001/schema.sql
* structured-relational-001/data.sql
* structured-relational-001/README.md

Required characteristics:

* multiple related tables
* declared column types
* declared nullability
* primary keys
* foreign keys
* at least one reusable relationship across tables
* sufficient schema information to distinguish source-declared structure from inferred semantics

Question coverage:

* relational object identity
* table and column representation
* declared type placement
* nullability placement
* primary-key and foreign-key representation
* relationship representation
* database/schema context
* boundary between declared relational structure and interpreted semantic meaning

## Source Set B: Cross-Implementation Portability

* intake id: structured-relational-002
* profile target: structured-data-relational
* candidate source: Microsoft AdventureWorksLT
* purpose: test whether relational structures identified in the first source set remain reusable across a different database ecosystem

Suggested files:

* structured-relational-002/schema or creation scripts
* structured-relational-002/sample data or bounded extract
* structured-relational-002/README.md

Required characteristics:

* multiple related tables
* declared column types
* declared nullability
* primary and foreign keys
* constraints or comparable schema declarations
* relational structures materially comparable to Source Set A
* enough implementation difference to expose vendor-specific assumptions

Question coverage:

* portability of relational object modeling
* portability of key and constraint representation
* reusable versus vendor-specific schema metadata
* relational locator requirements
* cross-source consistency of tier placement
* whether candidate structures belong in the reusable profile contract

## Intake Completion Checklist

* source location recorded
* license/usage status recorded
* database/version context recorded
* normalization or extraction steps recorded
* retained source artifacts recorded
* vendor-specific features identified
* known limitations recorded
* baseline readiness set in documentation/testbed-source-intake.md

