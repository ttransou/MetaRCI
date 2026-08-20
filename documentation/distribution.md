## Distribution Contract

### Purpose

The MetaRCI distribution contract defines the minimum set of artifacts required to implement MetaRCI v0.1 outside the development repository.

The distribution should provide enough material for a consumer to:

- understand the MetaRCI contract;
- select an appropriate structural profile;
- construct a conforming record;
- validate that record;
- identify the MetaRCI and profile versions in use;
- integrate the validated record into a downstream system.

The distribution contract defines what must be available to consumers. It does not prescribe a single delivery mechanism.

MetaRCI may be distributed through a repository, release archive, package manager, embedded resources, or another implementation-specific channel, provided the required contract artifacts remain available and version-identifiable.

### Required v0.1 Distribution Artifacts

A MetaRCI v0.1 distribution should include the following normative or implementation-critical artifacts.

#### Base Schema

The distribution must include the current MetaRCI base schema.

The base schema defines:

- the three-tier record structure;
- shared fields;
- field types;
- nullability;
- common validation requirements;
- the extension points used by structural profiles.

The base schema is part of the executable MetaRCI contract and should be distributed in a machine-readable form.

#### Structural Profiles

The distribution must include the primary v0.1 structural profiles:

- `document`
- `structured-data`
- `media`
- `composite`

Each profile should remain identifiable by:

- profile name;
- profile version;
- compatible base-schema version;
- profile-specific overrides;
- profile-specific custom fields.

Only profiles that are part of the published MetaRCI release should be represented as supported distribution contracts.

Relational structured-data work is not part of the v0.1 distribution contract and should remain deferred.

#### Validation Tooling

The distribution should include a supported means of validating a MetaRCI record against:

1. the MetaRCI base schema; and
2. the selected structural profile.

The validation mechanism should enforce the structural contract without implying semantic truth or metadata authority.

A consumer should not be required to reconstruct MetaRCI validation behavior independently from prose documentation.

#### Version Metadata

The distribution must expose enough version information to determine:

- the MetaRCI release version;
- the base-schema version;
- the available profile versions;
- compatibility expectations among those artifacts.

Version information should be available in a form that can be inspected by both humans and programmatic consumers where practical.

#### Example Records

The distribution should include representative conforming records for the primary structural profiles.

Examples should demonstrate:

- expected record shape;
- use of Reference, Context, and Interpretive tiers;
- profile-specific structures;
- valid nullability and optional-field behavior;
- version and profile declarations.

Examples are implementation aids.

They do not define the MetaRCI contract independently of the schemas and profiles.

#### Implementation Documentation

The distribution should include sufficient implementation documentation to explain:

- the integration contract;
- profile selection;
- record construction;
- validation behavior;
- metadata scope and projection;
- provenance and linkage;
- version compatibility;
- the distinction between MetaRCI and downstream implementation behavior.

A consumer should not need to infer the integration model from testbed history or development notes.

### Normative Versus Supporting Material

Not every file in the MetaRCI development repository needs to be part of the reusable distribution.

The distribution should distinguish between artifacts required to implement the contract and artifacts retained primarily as supporting evidence or project history.

#### Normative or Implementation-Critical Material

This category includes artifacts such as:

- the base schema;
- released structural profiles;
- validation rules and supported validator behavior;
- version declarations;
- integration and implementation guidance required to consume the contract.

#### Supporting Material

This category may include:

- testbed reports;
- synthetic test sources;
- evaluation notes;
- research commentary;
- profile-development history;
- design discussions;
- deferred proposals;
- experimental records not intended as canonical examples.

Supporting material remains valuable for transparency and evidence, but a consumer should not be required to ingest or ship the full research history in order to implement MetaRCI.

### Distribution Independence

The MetaRCI contract should remain usable independently of a particular programming language or runtime.

A Python package may provide one convenient delivery mechanism, but the normative contract should remain accessible through portable artifacts such as YAML schemas and profiles.

This allows MetaRCI to be implemented by systems that:

- do not use Python;
- use their own validation infrastructure;
- embed MetaRCI resources into another application;
- consume the schemas through a service;
- manage metadata through an enterprise platform or other language ecosystem.

### Minimal Distribution Principle

The distribution should contain enough to implement MetaRCI correctly, but should not require consumers to adopt the entire development repository.

Conceptually:

```text
MetaRCI v0.1 distribution
├── base schema
├── released structural profiles
├── validation capability
├── version metadata
├── representative examples
└── implementation documentation
```

Research history, testbeds, and development artifacts may remain available separately without becoming runtime or implementation dependencies.

### Distribution Principle

Ship the contract and what is required to use it; do not make the development history a dependency.
