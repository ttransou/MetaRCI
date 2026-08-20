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

---

## Repository-to-Distribution Mapping

The v0.1 distribution should be derived from the development repository without reproducing the repository wholesale.

The distribution branch should contain only the artifacts required to implement, validate, understand, and version the MetaRCI contract, plus a minimal set of representative examples.

### Include in the Distribution

- base schema;
- released v0.1 structural profiles;
- supported validation tooling;
- version metadata;
- representative conforming examples;
- implementation/integration documentation;
- distribution documentation;
- license and essential project metadata;
- a concise README oriented toward implementers.

### Retain in the Main Repository as Supporting Evidence

- testbed source files;
- detailed testbed reports;
- exploratory evaluation notes;
- development chronology;
- profile-review working documents;
- research commentary;
- evidence used to justify schema/profile decisions;
- broader project documentation not required to implement MetaRCI.

These materials remain important to the transparency and research basis of MetaRCI, but they should not become implementation dependencies.

### Exclude From the v0.1 Distribution

- temporary files;
- obsolete agent instructions;
- experimental artifacts not part of the released contract;
- deferred profile work;
- Structured-Data-Relational implementation material;
- local development or environment artifacts;
- redundant examples used only during evaluation;
- internal notes that do not contribute to implementation.

### Distribution-Branch Principle

The distribution branch should be a curated projection of the MetaRCI repository, not a second development tree.

Changes to the MetaRCI model should originate in the main development workflow and be deliberately promoted into the distribution branch once they are part of a released contract.

The distribution branch should therefore answer:

> **What does an implementer actually need to use this version of MetaRCI?**

---

## Proposed Distribution Layout

The v0.1 distribution branch should present MetaRCI as a compact, implementation-oriented package rather than reproduce the structure of the development repository.

The layout should make the contract easy to locate, inspect, validate against, and integrate into another system.

A proposed distribution structure is:

```text
metarci/
├── README.md
├── LICENSE
├── VERSION
├── schemas/
│   └── metarci-base.yaml
├── profiles/
│   ├── document.yaml
│   ├── structured-data.yaml
│   ├── media.yaml
│   └── composite.yaml
├── examples/
│   ├── document-record.yaml
│   ├── structured-data-record.yaml
│   ├── media-record.yaml
│   └── composite-record.yaml
├── validation/
│   └── [supported validation tooling]
└── documentation/
    ├── implementation.md
    └── distribution.md
````

This structure is provisional. Final filenames and package organization may change when the distribution mechanism and programmatic API are defined.

### Root-Level Material

The distribution root should contain only essential release and orientation material.

#### `README.md`

The distribution README should be oriented toward implementers rather than toward the full research and development history of MetaRCI.

It should provide:

* a concise description of MetaRCI;
* the three-tier model;
* the four supported v0.1 structural profiles;
* basic implementation flow;
* validation instructions;
* links to the implementation and distribution documentation;
* version information;
* a pointer to the main MetaRCI repository for testbed evidence, research history, and broader documentation.

#### `LICENSE`

The applicable project license should travel with the distribution.

#### `VERSION`

The distribution should expose the MetaRCI release version in a simple, inspectable form.

The exact mechanism may later be replaced or supplemented by package metadata, but consumers should not need to infer the distribution version from repository history.

### `schemas/`

The `schemas/` directory should contain the released MetaRCI base schema required to construct and validate conforming records.

Only schemas that are part of the published distribution contract should be included.

Experimental or deferred schema work should remain in the development repository.

### `profiles/`

The `profiles/` directory should contain the released structural profiles associated with the distribution version.

For v0.1, these are:

* `document.yaml`
* `structured-data.yaml`
* `media.yaml`
* `composite.yaml`

Profile files should remain machine-readable and independently inspectable.

Deferred or experimental profiles should not be included.

### `examples/`

The `examples/` directory should contain a small set of representative conforming records.

The objective is to demonstrate the contract, not to reproduce the full testbed collection.

Each primary structural profile should have at least one concise example showing:

* profile declaration;
* Reference metadata;
* Context metadata;
* Interpretive metadata;
* profile-specific structures where applicable;
* valid use of optional and nullable values.

Examples should be maintained as validation-tested artifacts.

### `validation/`

The distribution should provide the supported validation capability required to check a MetaRCI record against the base schema and selected structural profile.

The exact organization of this directory should be determined when the programmatic and packaging contracts are defined.

The distribution should avoid requiring consumers to reconstruct validation behavior from documentation alone.

### `documentation/`

The distribution documentation should focus on implementation rather than research chronology.

At minimum, it should include:

* the MetaRCI integration contract;
* the distribution contract and implementation guidance necessary to understand the shipped artifacts.

Additional documentation should be included only where it materially helps a consumer implement the released contract.

Detailed testbed reports, exploratory notes, development history, and deferred design work should remain available from the main repository rather than being duplicated into the distribution.

### Separation From the Development Repository

The proposed distribution layout intentionally omits substantial parts of the development repository.

The absence of those materials does not make them unimportant.

The main repository remains the authoritative location for:

* testbed evidence;
* schema and profile development;
* research rationale;
* historical design decisions;
* deferred work;
* experimental artifacts;
* future-version development.

The distribution branch represents a released projection of that work for implementation purposes.

Conceptually:

```text
Main MetaRCI repository
        │
        ├── research
        ├── testbeds
        ├── development
        ├── evidence
        └── released contract
                 ↓
        curated distribution
                 ↓
             consumer
```

### Layout Principle

> **The distribution should make the MetaRCI contract easier to consume without creating a second place to design MetaRCI.**


