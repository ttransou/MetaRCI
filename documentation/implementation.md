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
