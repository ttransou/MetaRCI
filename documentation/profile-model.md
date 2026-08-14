# MetaRCI Profile Model

## Core Structure

MetaRCI uses one structural chain:

Base schema -> Structural profile -> Record

Profiles are structural classes, not domain templates.

## Epistemic Rule

Tier placement is based on evidentiary basis, not tool, person, or workflow origin.

- Reference: source-native or mechanically recoverable claims
- Context: externally supplied or curated situating claims
- Interpretive: analytical, inferred, or evaluative claims

## v0.1 Primary Structural Profiles

The current primary v0.1 profiles are:

- document
- structured-data
- media
- composite

These profiles are peers in the v0.1 model.

## Profile Behavior in v0.1

- Profiles extend the base schema directly.
- Profiles may strengthen constraints and add profile-specific reusable fields.
- Profiles may not redefine base field structure through shallow overrides.
- Validation enforces exact version alignment between base, profile, and record.

## Testbed Role

Testbeds evaluate the model. They do not define the model by default.

A passing validator result confirms structural validity. It does not establish semantic truth, source authority, or interpretive correctness.

## Deferred Scope

Structured-Data-Relational is explicitly deferred beyond v0.1. It is not part of v0.1 completion claims for Structured Data.

## Extension Boundary

Implementation-specific policy, local vocabularies, and use-case rules belong in implementation extensions unless they are proven profile-reusable across evidence.
