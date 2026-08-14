# MetaRCI Testbed Playbook

## Purpose

Testbeds are used to evaluate MetaRCI contracts. They do not define the model by default.

## Core Rules

- Preserve the base -> profile -> record contract sequence.
- Distinguish source-grounded, contextual, and interpretive assertions.
- Do not invent source structure to exercise candidate fields.
- Treat passing validation as structural legality, not semantic truth.

## Required Outputs Per Testbed

- baseline record that validates under the current contract
- one or more variants for the target question
- short report using the repository template
- explicit outcome label:
  - Current guidance
  - Current contract
  - Proposed change
  - Deferred

## Evidence Threshold for Contract Changes

Promote to Proposed change only when:

- the same structural need appears across independent source contexts
- current contract representations are materially insufficient
- the candidate shape is profile-reusable and not implementation-local

## v0.1 Scope Reminder

Primary v0.1 profiles are peers:

- document
- structured-data
- media
- composite

Structured-Data-Relational is deferred beyond v0.1 and should not be used as evidence for v0.1 contract closure.

## Validation Commands

- python validate.py --base <base> --profile <profile> --record <record>
- python -m unittest discover -s tests -p 'test_*.py' -v
