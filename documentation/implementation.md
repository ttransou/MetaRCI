# MetaRCI v0.1 Integration and Provisioning Strategy

## Purpose

The MetaRCI v0.1 profile and testbed work establishes the current metadata model and its primary structural contracts. The next phase defines how that model is implemented within and consumed by downstream systems without turning MetaRCI itself into a retrieval, orchestration, or application framework.

This phase focuses on the boundary between the MetaRCI contract and the systems that use it.

MetaRCI should remain framework-agnostic. SCARAG may serve as a reference implementation, but it must not become the normative definition of how MetaRCI is consumed.

The guiding boundary for this phase is:

> **MetaRCI defines and validates metadata records. It does not prescribe how downstream systems store, project, index, retrieve, or generate from those records.**

---

## Step 1 — Define the Integration Contract

**Status:** Active

Create `documentation/integration.md` to define how MetaRCI is implemented within and consumed by downstream systems without making those systems part of the MetaRCI model itself.

The integration contract should establish:

- what MetaRCI provides;
- what MetaRCI does not provide;
- the boundary between MetaRCI and a consuming pipeline or application;
- how a structural profile is selected;
- how Reference, Context, and Interpretive metadata are constructed;
- what MetaRCI validation guarantees and what it does not guarantee;
- the distinction between source-level, component-level, and downstream chunk- or index-level metadata;
- how selected MetaRCI metadata may be projected into downstream systems while preserving linkage to the authoritative record;
- how SCARAG may serve as a reference implementation without becoming normative;
- how a framework-neutral consumer can implement the same contract;
- version and compatibility expectations for records, profiles, and consumers.

The purpose of this step is to establish the implementation boundary before designing packaging, APIs, adapters, or pipeline-specific integrations.

---

## Step 2 — Define the Minimal v0.1 Distribution Contract

Determine what a reusable MetaRCI v0.1 distribution must contain.

Likely distribution elements include:

- the base schema;
- the four primary structural profiles;
- validation tooling;
- validation support resources;
- example records;
- version metadata;
- integration documentation.

This step should distinguish between material required to implement MetaRCI and material retained primarily as research, testbed, or development documentation.

No packaging mechanism should be treated as normative until the distribution contract is clear.

---

## Step 3 — Define the Minimal Programmatic API

Derive any Python-facing API from the integration contract rather than designing the API independently.

The initial API should answer only the needs established by the integration contract, such as:

- loading a MetaRCI profile;
- validating a record;
- exposing MetaRCI and profile version information;
- returning validation results programmatically;
- accessing schema and profile resources when appropriate.

The v0.1 API should remain deliberately small.

MetaRCI should not expose ingestion, parsing, chunking, embedding, retrieval, ranking, generation, or orchestration APIs.

---

## Step 4 — Package MetaRCI

Package MetaRCI according to the distribution and programmatic contracts established in the preceding steps.

Packaging should preserve multiple implementation paths where practical:

- direct use of YAML schemas and profiles;
- programmatic use through a lightweight Python package;
- repository/reference use for systems with their own implementation tooling.

Python packaging should support MetaRCI rather than redefine it as a Python-only model.

---

## Step 5 — Define Metadata Projection Guidance

Document how downstream systems may consume selected MetaRCI metadata without requiring every downstream object to reproduce a complete MetaRCI record.

The expected relationship is:

```text
Authoritative MetaRCI record
        ↓
selected metadata projection
        ↓
component / chunk / index metadata
```

Guidance should address:

- projection versus duplication;
- linkage and provenance back to the authoritative MetaRCI record;
- source-level and component-level scope;
- what metadata may be inherited;
- what metadata must not be assumed to inherit;
- how an implementation may select retrieval-relevant metadata.

This guidance should remain implementation-oriented and should not introduce another MetaRCI schema layer without evidence.

---

## Step 6 — Implement the SCARAG Reference Integration

Use SCARAG as the first concrete consumer of the MetaRCI integration contract.

A reference flow may resemble:

```text
source
→ extraction / curation
→ MetaRCI record construction
→ MetaRCI validation
→ SCARAG metadata projection
→ chunking / indexing / retrieval
```

The purpose of the SCARAG integration is to demonstrate one implementation of MetaRCI, not to define MetaRCI through SCARAG-specific requirements.

Implementation pressure discovered through SCARAG should be recorded as evidence. It should not automatically produce changes to the MetaRCI contract.

---

## Step 7 — Create a Framework-Neutral Reference Example

Provide at least one minimal implementation example that is not SCARAG-specific.

The example should demonstrate how an arbitrary RAG, knowledge-management, knowledge-graph, or related system can:

- select an appropriate MetaRCI structural profile;
- construct a MetaRCI record;
- validate that record;
- retain the record as the authoritative metadata object;
- project selected metadata into downstream processing or retrieval structures.

This example should help substantiate MetaRCI's framework-agnostic design.

---

## Step 8 — Verify v0.1 Provisioning

Before treating v0.1 provisioning as complete, verify that a new consumer can determine:

- what MetaRCI artifacts to install, copy, or reference;
- which structural profile to use;
- how to construct a conforming record;
- how to validate that record;
- what validation does and does not establish;
- how the record may be consumed downstream;
- which responsibilities remain outside MetaRCI;
- which MetaRCI and profile versions are in use.

The provisioning phase is complete when the implementation path is understandable without requiring a consumer to infer MetaRCI architecture from the testbeds or from SCARAG.

---

## Phase Boundary

The v0.1 model-development work answers:

> **What is MetaRCI?**

The integration and provisioning phase answers:

> **How does another system use MetaRCI without becoming MetaRCI?**

The declared sequence above provides the working path for that phase. Later steps may be revised as evidence emerges from the integration contract and reference implementations.

For now, **Step 1 — Define the Integration Contract** is the active task.

---

## Integration Contract

### Purpose

This section defines the integration boundary between MetaRCI and the systems that implement or consume it.

MetaRCI is a framework-agnostic metadata model. It defines metadata structure through a base schema, structural profiles, records, and validation rules. It does not define the downstream systems that use those records.

The purpose of this integration contract is to establish how MetaRCI metadata may enter, move through, and be consumed by external pipelines while preserving the distinction between the MetaRCI model and implementation-specific behavior.

This contract applies to implementations using MetaRCI in systems such as:

- retrieval-augmented generation pipelines;
- knowledge-management systems;
- knowledge-graph workflows;
- document and media processing systems;
- search and indexing systems;
- other metadata-aware information pipelines.

SCARAG may serve as a reference implementation of this contract, but SCARAG does not define MetaRCI behavior.

### Integration Boundary

MetaRCI defines and validates metadata records.

It does not prescribe how downstream systems:

- parse or transform source content;
- chunk source material;
- create embeddings;
- store vectors or indexes;
- rank or retrieve content;
- generate responses;
- orchestrate models or agents;
- implement application-specific business logic.

A consuming system may use MetaRCI metadata as part of any of these processes, but those processes remain implementation concerns outside the MetaRCI contract.

The integration boundary can therefore be expressed as:

```text
External source and processing
        ↓
MetaRCI-compatible metadata construction
        ↓
MetaRCI validation
        ↓
Validated MetaRCI record
        ↓
Implementation-specific consumption
```

MetaRCI governs the structure and validation of the metadata record. The consuming system governs how that validated metadata is stored, projected, indexed, retrieved, or otherwise operationalized.

### Scope of This Contract

This integration contract defines:

- the responsibilities of MetaRCI;
- the responsibilities of consuming implementations;
- structural profile selection;
- MetaRCI record construction;
- validation responsibilities and limits;
- metadata scope across sources, components, and downstream units;
- projection of MetaRCI metadata into implementation-specific structures;
- provenance and linkage to authoritative MetaRCI records;
- version and compatibility expectations.

This integration contract does not define a required ingestion architecture, retrieval architecture, storage model, vector database, RAG framework, knowledge-graph platform, or programming language.

### MetaRCI Responsibilities

MetaRCI is responsible for defining the structure, scope, and validation requirements of metadata records that conform to the model.

Within the integration contract, MetaRCI provides:

- the base metadata schema;
- structural profiles for supported source types;
- the Reference, Context, and Interpretive tier model;
- field requirements, types, nullability, and permitted profile overrides;
- profile-specific structural fields where supported by evidence;
- record and profile version declarations;
- validation of records against the applicable base schema and structural profile;
- a consistent metadata contract that may be consumed by downstream systems.

A conforming MetaRCI record represents metadata according to the rules of the selected profile and the epistemic basis of each tier.

MetaRCI validation establishes structural conformance to that contract. It does not establish that every metadata value is factually correct, contextually authoritative, semantically complete, or appropriate for a particular retrieval use case.

### Implementation Responsibilities

The consuming implementation is responsible for determining how MetaRCI records are created, maintained, and operationalized within its own system.

Implementation responsibilities may include:

- selecting or developing parsers and extractors;
- mechanically recovering Reference metadata from source material;
- sourcing, verifying, normalizing, and maintaining Context metadata;
- producing or curating Interpretive metadata;
- selecting the appropriate MetaRCI structural profile for a source;
- constructing MetaRCI-compatible records;
- invoking MetaRCI validation at appropriate lifecycle points;
- deciding where authoritative MetaRCI records are stored;
- determining which metadata is projected into downstream components, chunks, indexes, graphs, or application structures;
- preserving provenance and linkage between projected metadata and the authoritative MetaRCI record;
- defining retrieval, ranking, generation, governance, and application-specific behavior.

An implementation may automate any of these activities where appropriate. Automation does not change the epistemic basis of a MetaRCI field or transfer responsibility for semantic or contextual authority to the MetaRCI validator.

### Responsibility Boundary

The distinction can be summarized as:

| Concern | MetaRCI | Consuming Implementation |
|---|---|---|
| Metadata grammar | Defines | Implements |
| Structural profiles | Defines | Selects and applies |
| Tier semantics | Defines | Populates according to evidence |
| Field requirements and types | Defines | Satisfies |
| Structural validation | Provides | Invokes and responds to |
| Metadata extraction | Does not prescribe | Implements |
| Context verification | Does not perform | Implements |
| Interpretive analysis | Does not perform | Implements |
| Storage | Does not prescribe | Implements |
| Metadata projection | Provides guidance only | Determines |
| Chunking and indexing | Does not prescribe | Implements |
| Retrieval and ranking | Does not prescribe | Implements |
| Generation | Does not prescribe | Implements |
| Semantic truth | Does not certify | Remains an implementation/governance concern |

### Profile Selection

A MetaRCI implementation must select the structural profile that best matches the organization and behavior of the source being described.

Profile selection is based on **source structure**, not subject domain, organizational function, or intended retrieval task.

The current v0.1 primary structural profiles are:

- `document`
- `structured-data`
- `media`
- `composite`

A source should use the profile whose structural assumptions most closely match the source itself.

#### Document

Use the `document` profile for sources whose primary structure is document-like and organized around textual or page-oriented content.

Examples may include:

- PDF documents;
- DOCX files;
- plain-text documents;
- reports;
- articles;
- policy documents;
- other primarily textual sources.

Document sources may contain internal subdivisions such as sections, chapters, or other source-native structural units.

#### Structured Data

Use the `structured-data` profile for sources whose primary information structure is tabular, field-based, record-oriented, or otherwise explicitly structured.

Examples may include:

- CSV files;
- spreadsheets;
- flat tabular datasets;
- other non-relational structured-data sources supported by the current profile.

Relational structured-data modeling is outside the v0.1 profile scope and is deferred to a later version.

#### Media

Use the `media` profile for sources whose primary content is visual, audiovisual, or otherwise media-oriented.

Examples may include:

- images;
- video;
- other supported media sources.

The presence of textual metadata, captions, transcripts, or embedded descriptive information does not by itself make a Media source a Document source.

#### Composite

Use the `composite` profile for a logical source whose independently meaningful components may require different structural treatment while remaining parts of one coherent parent source.

Examples may include:

- presentation files containing slides, notes, tables, charts, images, or audiovisual content;
- publication packages containing ordered document components and embedded media or structured content;
- other sources whose meaningful whole/part structure is intrinsic to the source.

Physical packaging alone does not make a source Composite.

A ZIP archive, container format, or package containing multiple internal files should not automatically be assigned the Composite profile. The relevant question is whether the source itself expresses meaningful logical components and whole/part relationships.

### Profile Selection Principle

Profile selection should answer:

> **What structural model best represents this source as a source?**

It should not answer:

> **What is this source about?**

Domain, audience, organizational context, purpose, and similar concerns belong primarily to Context metadata rather than structural profile selection.

### Mixed Internal Structures

A source may contain internal structures that resemble another MetaRCI profile without changing the profile of the parent source.

For example:

- a Document may contain a table;
- a Media source may contain text or transcript material;
- a Composite presentation may contain an embedded image or structured table;
- a Composite publication may contain document-like chapters and embedded media.

The profile selected for the parent source governs the structural treatment of that parent. Meaningful components may be described or evaluated according to their own structure where an implementation requires that level of granularity.

The presence of heterogeneous internal content does not require the parent profile to absorb the internal schema of every component type.

### Implementation Responsibility

The consuming implementation is responsible for profile selection.

MetaRCI validation can determine whether a record conforms to a selected profile, but it does not determine whether the selected profile is semantically or structurally appropriate for the source.

Where profile selection is ambiguous, implementations should document the basis for the decision and prefer the simplest profile that adequately represents the source structure.

### Record Construction

After selecting the appropriate structural profile, the consuming implementation is responsible for constructing a MetaRCI-compatible record.

A MetaRCI record should be populated according to the epistemic basis of the available metadata rather than according to the mechanism used to obtain it.

#### Reference Metadata

Reference metadata should contain source-native, directly stated, or mechanically recoverable information with minimal interpretation.

Examples may include:

- filename and format;
- source identifiers;
- file dimensions or counts;
- stated titles or authors;
- source-native structural markers;
- checksums;
- ingestion timestamps;
- parser or extraction status;
- profile-specific Reference structures supported by the selected profile.

Reference metadata may be extracted automatically where appropriate.

Automated extraction does not remove the need to handle parser errors, ambiguous source structures, or missing values correctly.

#### Context Metadata

Context metadata should contain externally supplied or curated information used to situate the source within a broader corpus, domain, organizational environment, jurisdiction, audience, or operational setting.

Context may come from:

- external catalogs;
- systems of record;
- controlled vocabularies;
- organizational sources;
- bibliographic or administrative records;
- human curation;
- mechanically recoverable clues from supporting sources.

Mechanically recoverable Context values should still be verified, normalized, and aligned to the source and the implementation's retrieval or governance needs.

The fact that a Context value can be extracted automatically does not make it Reference metadata.

#### Interpretive Metadata

Interpretive metadata should contain analytical, inferred, generated, or evaluative information about the source.

Examples may include:

- concepts;
- themes;
- analytical categories;
- inferred relationships;
- interpretive notes;
- risk or relevance assessments;
- curated summaries or other analytical descriptions where supported by the base schema or selected profile.

Interpretive metadata may be produced by humans, automated systems, or a combination of both.

The production method does not determine tier placement. The epistemic character of the metadata does.

### Missing and Nullable Values

Implementations should preserve the distinction between:

- a value that is known;
- a value that is not present or not available;
- a value that is not applicable;
- a value that has not yet been curated or derived.

Where the MetaRCI contract permits null values, implementations should use nullability rather than inventing or inferring unsupported values solely to complete a record.

A conforming record does not need to maximize field population. It needs to represent available metadata accurately within the selected profile contract.

### Construction Principle

Record construction should follow:

> **Extract or observe → verify where required → place by epistemic basis → validate**

The objective is not to populate every possible field. The objective is to create a structurally conforming metadata record whose values have an appropriate and explainable basis.

### Validation Contract

MetaRCI validation determines whether a record conforms structurally to the applicable MetaRCI base schema and selected structural profile.

Validation is a contract check.

It evaluates whether the record satisfies requirements such as:

- required fields;
- permitted fields;
- field types;
- nullability rules;
- allowed values;
- nested object structure;
- list item structure;
- profile-specific requirements;
- permitted profile overrides;
- record and profile compatibility where enforced.

A successful validation result means that the record conforms to the current structural contract.

It does **not** mean that the metadata is necessarily correct, complete, authoritative, current, unbiased, or appropriate for every downstream use.

#### What Validation Establishes

MetaRCI validation may establish that:

- required structural elements are present;
- values use the expected data types;
- required nested properties are present;
- profile-specific structures conform to their declared grammar;
- unsupported fields or structural overrides are rejected where the contract prohibits them;
- the record can be consumed as a structurally conforming MetaRCI record.

#### What Validation Does Not Establish

MetaRCI validation does not independently establish:

- factual accuracy;
- semantic truth;
- contextual authority;
- provenance credibility;
- completeness of extraction;
- quality of human curation;
- quality of automated inference;
- appropriateness of a selected controlled vocabulary;
- correctness of profile selection;
- retrieval usefulness;
- ranking quality;
- governance adequacy;
- suitability for a particular downstream task.

These concerns remain the responsibility of the consuming implementation and its associated human, organizational, or technical governance processes.

#### Structural Conformance and Metadata Authority

A structurally valid value may still be wrong.

For example, a Context field may contain a syntactically valid domain assignment while still being poorly chosen, outdated, or inconsistent with organizational practice.

Likewise, an Interpretive field may contain structurally valid analytical metadata while still requiring review before it is trusted for a particular use case.

Validation should therefore be understood as:

> **Does this record satisfy the MetaRCI contract?**

rather than:

> **Is everything asserted by this record true?**

#### Validation in the Record Lifecycle

Implementations may invoke validation at multiple points in the metadata lifecycle, including:

- after initial Reference extraction;
- after Context curation;
- after Interpretive enrichment;
- before storing an authoritative record;
- before projecting metadata into downstream systems;
- after record updates or migrations;
- when validating records against a new compatible profile or MetaRCI version.

MetaRCI does not require a specific orchestration pattern for these checks.

The implementation determines when validation occurs according to its own ingestion, governance, update, and deployment processes.

#### Validation Failures

A validation failure indicates that the record does not currently satisfy the applicable structural contract.

Implementations should treat validation errors as contract violations to be resolved rather than as evidence that the underlying source or metadata is inherently invalid.

Resolution may require:

- correcting record structure;
- supplying a required value;
- using `null` where permitted;
- removing unsupported fields;
- correcting a field type;
- correcting the selected profile;
- correcting a profile or version reference;
- identifying an actual gap in the MetaRCI contract.

The last case should be distinguished carefully from an implementation-specific preference.

A new implementation requirement should not automatically result in expansion of the MetaRCI contract. Contract changes should be supported by reusable evidence beyond a single local implementation.


### Metadata Scope and Projection

A MetaRCI record describes metadata at the scope established by the selected profile and the source being represented.

That scope may be:

- the source as a whole;
- a meaningful component of a source;
- another independently addressable unit represented by a conforming MetaRCI record.

MetaRCI does not require every downstream object derived from that source to contain a complete copy of the authoritative record.

Instead, consuming implementations may project selected MetaRCI metadata into downstream structures according to operational need.

#### Authoritative Record

The authoritative MetaRCI record should remain the primary metadata representation for the source or component it describes.

Downstream systems may derive subsets of that metadata for purposes such as:

- chunk retrieval;
- filtering;
- ranking;
- indexing;
- graph construction;
- access control;
- corpus navigation;
- provenance display;
- generation support.

A projected subset does not become a replacement for the authoritative MetaRCI record merely because it is stored closer to the retrieval or application layer.

The relationship can be expressed as:

```text
Authoritative MetaRCI record
        ↓
selected metadata projection
        ↓
component / chunk / index / graph metadata
````

#### Source-Level Metadata

Source-level metadata describes the logical source represented by the MetaRCI record.

Examples may include:

* source identity;
* title;
* authorship;
* format;
* domain;
* intended audience;
* organizational context;
* sensitivity;
* interpretive concepts or themes.

A downstream implementation may project some of these values into derived units where doing so supports retrieval, filtering, governance, or provenance.

#### Component-Level Metadata

Where a source contains independently meaningful components, metadata may also be associated with those components.

A component should not automatically be assumed to inherit every value from its parent source.

Some metadata may reasonably apply across the whole source, while other metadata may be:

* specific to the parent;
* specific to the component;
* overridden at the component level;
* unknown at the component level;
* inappropriate to inherit.

Implementations should preserve the distinction between metadata that is explicitly asserted for a component and metadata that is propagated from a parent for operational convenience.

#### Chunk- and Index-Level Metadata

Chunks, vector records, search documents, graph nodes, or similar downstream units are implementation structures rather than MetaRCI record types unless they are explicitly modeled as such by an implementation.

A consuming system may attach selected MetaRCI metadata to these units.

For example, a retrieval chunk may carry:

* source identifier;
* source title;
* domain;
* section or component identifier;
* sensitivity level;
* selected provenance fields.

This does not require the chunk to reproduce the complete Reference, Context, and Interpretive tiers.

The metadata selected for projection should be determined by the downstream use case.

#### Projection Versus Duplication

Projection should be treated as a deliberate selection of metadata for downstream use rather than the automatic duplication of the entire MetaRCI record.

Implementations should consider:

* which fields materially support retrieval or filtering;
* which fields are needed for governance or access decisions;
* which fields are necessary to preserve provenance;
* which fields would create unnecessary storage or indexing overhead;
* whether projected values can become stale relative to the authoritative record.

Where projected metadata is persisted separately, implementations should maintain sufficient linkage to determine its source and, where relevant, its version.

#### Inheritance

MetaRCI does not assume universal inheritance of metadata from a parent source to its components or downstream units.

An implementation may define inheritance or propagation rules, but those rules are implementation behavior unless explicitly represented in the MetaRCI contract.

Inheritance decisions should distinguish between:

* metadata explicitly asserted for the child or component;
* metadata inherited from the parent;
* metadata copied for retrieval convenience;
* metadata derived specifically for the downstream unit.

This distinction is especially important for Context and Interpretive metadata, where parent-level meaning may not apply uniformly across all components.

### Projection Principle

> **Preserve the authoritative record; project only what the downstream system needs.**

Metadata projection should support retrieval and application behavior without collapsing the distinction between the MetaRCI source record and implementation-specific metadata structures.


### Validation Principle

> **Validation establishes structural conformance, not semantic truth.**

A MetaRCI record becomes trustworthy through the combination of structural validation, evidence quality, appropriate curation, provenance, and implementation-specific governance.


### Provenance and Linkage

MetaRCI records should remain traceable to the source or meaningful source component they describe.

When metadata is projected into downstream structures, consuming implementations should preserve sufficient linkage to identify the authoritative MetaRCI record from which that metadata originated.

MetaRCI does not prescribe a specific storage architecture for maintaining this linkage.

An implementation may use:

- source identifiers;
- record identifiers;
- component identifiers;
- profile and version references;
- database keys;
- document-store references;
- graph edges;
- index metadata;
- other stable implementation-specific identifiers.

The required mechanism may vary, but the relationship between authoritative metadata and projected metadata should remain recoverable.

#### Source Provenance

Reference metadata provides the primary source-grounded basis for identifying and tracing the described resource.

Depending on the profile and implementation, provenance-relevant information may include:

- source identifiers;
- original filenames;
- source paths or URLs;
- checksums;
- ingestion timestamps;
- parser or extraction information;
- version identifiers;
- source-native component identifiers;
- lineage information represented elsewhere in the MetaRCI record.

These values support traceability but do not, by themselves, establish the authority or quality of every metadata assertion associated with the source.

#### Metadata Provenance

The provenance of a metadata value is distinct from the provenance of the source itself.

For example:

- a Reference value may be mechanically recovered from the source;
- a Context value may come from an external catalog or organizational system;
- an Interpretive value may be produced through human analysis or automated inference.

Implementations should preserve this distinction where the origin or basis of a metadata assertion is operationally significant.

MetaRCI does not require every projected value to carry a complete provenance history. However, downstream use should not make it impossible to determine the authoritative record or evidentiary basis when that information is required for retrieval, governance, review, or audit.

#### Linkage to the Authoritative Record

Projected metadata should maintain sufficient linkage to support operations such as:

- retrieving the complete MetaRCI record;
- determining which source or component a downstream unit belongs to;
- checking whether projected metadata reflects the current authoritative record;
- reviewing provenance or contextual basis;
- updating or re-projecting metadata after the authoritative record changes;
- tracing retrieval or generated output back to the underlying source.

A downstream object may therefore contain a small linkage structure rather than a complete MetaRCI record.

Conceptually:

```text
Downstream object
    ├── projected MetaRCI metadata
    └── authoritative record reference
                    ↓
            MetaRCI record
                    ↓
                 source
````

#### Version-Aware Linkage

Where MetaRCI records or source metadata may change over time, implementations should consider preserving enough version information to distinguish between:

* the current authoritative record;
* an earlier MetaRCI record version;
* metadata projected from an earlier state of the record.

This is particularly important where projected metadata is stored in persistent indexes or retrieval systems that may not update automatically when the authoritative record changes.

MetaRCI does not prescribe a synchronization mechanism. The consuming implementation is responsible for deciding how changes to authoritative records propagate into downstream structures.

#### Provenance and Generated Output

Where projected MetaRCI metadata contributes to retrieval or generation, implementations may use record and source linkage to preserve traceability from generated output back to the evidence used to support it.

MetaRCI provides the metadata structure that can support such traceability, but it does not define citation generation, answer attribution, retrieval logging, or audit interfaces.

Those remain implementation concerns.

### Provenance Principle

> **Projection may reduce metadata, but it should not sever traceability.**

A downstream system should be able to use only the metadata it needs while retaining a recoverable path back to the authoritative MetaRCI record and underlying source.


### SCARAG as a Reference Implementation

SCARAG may serve as a reference implementation of the MetaRCI integration contract.

It is not the normative implementation of MetaRCI, and MetaRCI compatibility does not require a system to use SCARAG, reproduce SCARAG architecture, or adopt SCARAG-specific retrieval behavior.

The purpose of the reference implementation is to demonstrate that the MetaRCI contract can be operationalized within a real metadata-aware retrieval pipeline.

A SCARAG integration may demonstrate a flow such as:

```text
source
→ extraction / curation
→ MetaRCI record construction
→ MetaRCI validation
→ metadata projection
→ chunking / indexing
→ retrieval
````

In this relationship:

* MetaRCI defines the metadata contract;
* SCARAG implements that contract within its own pipeline;
* SCARAG determines how validated metadata is projected into retrieval structures;
* SCARAG-specific chunking, indexing, retrieval, ranking, evaluation, and generation behavior remain outside the MetaRCI contract.

#### Reference Implementation, Not Dependency

MetaRCI must remain usable without SCARAG.

A consuming implementation may use different:

* parsers;
* ingestion workflows;
* metadata stores;
* vector databases;
* chunking strategies;
* retrieval frameworks;
* knowledge-graph technologies;
* programming languages;
* orchestration systems.

Such differences do not affect MetaRCI conformance provided the implementation constructs and validates records according to the applicable MetaRCI contract.

SCARAG should therefore be understood as:

> **one implementation of MetaRCI, not the rule for implementing MetaRCI.**

#### Evidence From Reference Implementation

Implementation experience from SCARAG may provide useful evidence about:

* integration friction;
* metadata projection needs;
* provenance requirements;
* lifecycle behavior;
* retrieval utility;
* gaps or ambiguities in implementation guidance.

That evidence may inform future MetaRCI evaluation.

It should not automatically result in changes to the MetaRCI schema or profile contracts.

Any proposed MetaRCI change arising from SCARAG should be evaluated for broader applicability and reusable evidence beyond the needs of a single implementation.

### Framework-Neutral Consumption

The same integration contract should be usable by systems with no dependency on SCARAG.

A framework-neutral consumer should be able to:

1. identify the structure of the source;
2. select the appropriate MetaRCI profile;
3. construct Reference, Context, and Interpretive metadata as applicable;
4. validate the resulting MetaRCI record;
5. retain or store the authoritative record;
6. project selected metadata into its own operational structures;
7. preserve linkage between projected metadata, the MetaRCI record, and the underlying source.

Conceptually:

```text
Source
  ↓
Implementation-specific processing
  ↓
MetaRCI record
  ↓
MetaRCI validation
  ↓
Implementation-specific metadata projection
  ↓
RAG / KMS / KG / search / other downstream system
```

MetaRCI does not require the downstream system to share SCARAG's architecture or terminology.

The common requirement is the metadata contract, not the surrounding pipeline.

### Reference Implementation Principle

> **Reference implementations demonstrate the contract; they do not define it.**

### Version and Compatibility Expectations

MetaRCI records, profiles, and implementations should identify the version of the contract they use.

Version information allows a consuming system to determine which structural rules apply to a record and whether that record can be processed safely by the implementation.

#### MetaRCI Version

The MetaRCI version identifies the release of the overall model and its associated contract.

A release may include changes to:

- the base schema;
- structural profiles;
- validation behavior;
- documentation;
- integration guidance;
- packaging or programmatic interfaces.

Implementations should not assume that records created under different MetaRCI versions are automatically interchangeable.

#### Profile Version

Each structural profile may carry its own version in addition to the broader MetaRCI release version.

A record should identify the profile and profile version against which it was constructed and validated.

Conceptually:

```text
MetaRCI version
      ↓
profile + profile version
      ↓
record
````

The profile version identifies the structural contract applicable to that record.

#### Record Compatibility

A consuming implementation should be able to determine:

* which MetaRCI version the record targets;
* which structural profile the record uses;
* which version of that profile applies;
* whether the implementation supports that combination.

A record that validates successfully against one profile version should not be assumed to validate unchanged against a later profile version unless compatibility is explicitly preserved.

#### Compatible Changes

Changes may be treated as compatible where they do not invalidate existing conforming records or change the meaning of the existing contract.

Examples may include:

* documentation clarification;
* corrected examples;
* non-normative implementation guidance;
* additional validation diagnostics that do not change accepted structure;
* other changes that preserve existing schema and profile behavior.

Compatibility should be determined by actual contract behavior rather than by documentation labels alone.

#### Contract Changes

Changes that alter record structure or validation expectations may require a new compatible or incompatible contract version, depending on their effect.

Examples may include:

* introducing a new required field;
* changing a field type;
* changing nullability;
* removing an allowed value;
* changing a profile-specific structure;
* changing the permitted behavior of profile overrides;
* removing or renaming an existing field.

Such changes should be evaluated deliberately rather than introduced as incidental implementation fixes.

#### Consumer Behavior

A consuming implementation should define how it responds when it encounters an unsupported MetaRCI or profile version.

Possible behaviors may include:

* rejecting the record;
* routing the record for migration;
* invoking a compatible older validator;
* warning that the record uses an unsupported contract;
* applying an explicitly documented compatibility policy.

MetaRCI does not prescribe which operational response an implementation must use.

The implementation should not silently reinterpret an unsupported record as though it conformed to a different version.

#### Validation and Versioning

Validation should occur against the contract identified by the record and selected profile.

Where an implementation intentionally validates an older record against a newer contract, the result should be understood as a compatibility or migration check rather than proof that the record was originally authored under the newer version.

#### Downstream Projection and Versioning

Where MetaRCI metadata is projected into indexes, chunks, graphs, or other persistent downstream structures, implementations should consider retaining enough version information to determine which authoritative record and contract produced the projected metadata.

This is especially important when:

* authoritative records are updated;
* profiles change;
* indexes are rebuilt incrementally;
* projected metadata may persist longer than the source record state from which it was derived.

MetaRCI does not prescribe a synchronization or migration mechanism.

#### v0.1 Expectations

For MetaRCI v0.1, consumers should treat the current base schema and the primary structural profiles as the initial published contract:

* `document`
* `structured-data`
* `media`
* `composite`

Relational structured-data modeling is not part of the v0.1 contract and remains deferred to a later version.

The v0.1 integration contract should be treated as an initial implementation boundary rather than a guarantee that future releases will never introduce compatible or intentionally versioned changes.

### Versioning Principle

> **A MetaRCI record should identify the contract it conforms to, and a consumer should know whether it supports that contract.**

---

