# Composite Testbed Source Pack

## Goal

Prepare two composite source sets that test membership state, roles, and completeness semantics.

## Source Set A: Complete Membership Package

* intake id: comp-source-001
* profile target: composite
* purpose: baseline composite package with known members

Suggested files:

* comp-source-001/manifest.md
* comp-source-001/member-list.csv
* comp-source-001/source-bundle-note.md

Required characteristics:

* explicit member list with stable identifiers
* at least two member types (for example document and media)
* clear package-level purpose statement

Question coverage:

* mixed-profile membership handling
* role and ordering representation

## Source Set B: Partial or Unknown Membership Package

* intake id: comp-source-002
* profile target: composite
* purpose: stress expected-versus-present and completeness behavior

Suggested files:

* comp-source-002/manifest.md
* comp-source-002/member-list.csv
* comp-source-002/missing-members-note.md

Required characteristics:

* some expected members absent or uncertain
* at least one stated reason for incompleteness
* enough context to test completeness-state representation

Question coverage:

* expected versus present membership
* completeness when expectations are uncertain
* collection-level vs item-level interpretation boundaries

## Intake Completion Checklist

* source location recorded
* license/usage status recorded
* normalization steps recorded
* known limitations recorded
* baseline readiness set in documentation/testbed-source-intake.md
