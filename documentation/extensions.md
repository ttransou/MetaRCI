# MetaRCI Extensions

## Overview

MetaRCI extensions define how an implementation may add local, organizational, or domain-specific behavior without redefining the structural model.

The extension mechanism is intentionally subordinate to the core model:

```text
Base schema → Structural profile → Record
```

Extensions may add detail, policy, or implementation-specific metadata, but they must not silently change the structural contract established by the base schema or a selected profile.

---

## Purpose of Extensions

Extensions are appropriate when an implementation needs to record information that is:

* local to a corpus, organization, or workflow;
* governed by policy rather than source structure;
* specific to a controlled vocabulary, authority file, or local system of record;
* useful for access, review, or operational handling;
* not necessary to define the generic structural profile itself.

Examples include:

* a local handling classification;
* a project-specific review workflow;
* a corpus-specific subject label;
* a retention or access policy;
* a provenance note for local processing steps.

Extensions should remain additive. They should not replace a profile’s structural meaning or weaken the base-schema contract.

---

## Extension Boundaries

An extension must not:

* redefine a field’s base type;
* change a field from nullable to non-nullable in a way that conflicts with the selected profile;
* change a field’s structural shape through a profile-style override;
* introduce a new profile-level semantic meaning without a corresponding structural profile;
* duplicate a core MetaRCI field in a way that creates ambiguity.

If a proposed extension would materially alter the source structure or the required validation behavior for a profile, it should be treated as a model change rather than an implementation extension.

---

## Extension Patterns

### 1. Namespaced Custom Fields

Implementations may add fields under a namespaced prefix to distinguish local metadata from structural MetaRCI fields.

Example:

```yaml
context:
  local_policy:
    access_classification: restricted
```

The namespace should be explicit and stable so that consumers can distinguish implementation fields from core profile fields.

### 2. Controlled Vocabularies

An implementation may define local or organizational vocabularies for values such as review status, handling category, or trust level.

These values should be documented and versioned separately from the core MetaRCI model. A controlled vocabulary may be referenced by a field value without changing the base schema itself.

### 3. Authority Files

Authority files or local registries may support values such as:

* organizational owners;
* subject authorities;
* citation sources;
* review boards;
* access groups.

These resources belong in extensions when they are local to an implementation and do not change the core profile semantics.

### 4. Local Validation Rules

Implementations may apply additional validation rules for policy or workflow compliance.

Examples include:

* requiring a review note before a value is marked approved;
* constraining a local field to a controlled vocabulary;
* validating cross-field relationships for a specific corpus.

These rules should be documented as extension rules and should not be confused with the generic MetaRCI validator contract.

### 5. Organizational Policy

Operational metadata may reflect organizational policy, such as:

* handling restrictions;
* archival retention requirements;
* internal review status;
* legal or compliance annotations.

Such fields should be clearly marked as policy metadata rather than source-structure metadata.

### 6. Corpus-Specific Metadata

An implementation may need to record metadata that is meaningful only for a given corpus, such as:

* project identifiers;
* collection codes;
* internal labels;
* filing categories.

This is appropriate for extensions when the metadata does not require a new structural profile.

### 7. Sensitivity and Access Classifications

Sensitivity, access, and handling metadata may be important operationally, but they should remain distinct from the structural profile contract.

A profile may require that a sensitivity field exists, but the specific vocabulary or policy behind it may be defined by an implementation extension.

### 8. Compatibility With Structural Profiles

Extensions must remain compatible with the selected structural profile.

That means:

* they should not change the profile’s required field set in unexpected ways;
* they should not assume a different tier structure;
* they should not replace profile logic with implementation-only behavior.

### 9. Separation Between Profile Fields and Implementation Fields

A useful rule is:

* profile fields describe the source structure;
* extension fields describe an implementation’s local policy or workflow.

If a field is needed to describe a source’s intrinsic structure, it belongs in the profile or base schema. If it is only needed for a local process, it belongs in an extension.

### 10. Extension Versioning

Extensions should be versioned independently from the base schema and structural profiles.

A change to an extension should not automatically alter the meaning of an existing MetaRCI profile.

Suggested practice:

* version the extension document separately;
* document which core MetaRCI version it targets;
* note whether the extension is backward-compatible.

### 11. Extension Provenance

Every extension should record how it was introduced and by whom.

Useful provenance information may include:

* extension name;
* version;
* authoring organization;
* creation date;
* intended use;
* relationship to an authority file or policy document.

### 12. Conflicts Between Profile Rules and Extension Rules

When an extension rule conflicts with the structural profile contract, the profile contract takes precedence.

A local rule may not weaken the profile’s required fields or alter its structural semantics. If a conflict is unavoidable, the design should be revisited as a model change rather than silently made an extension rule.

---

## Recommended Extension Structure

An implementation extension may be documented as a small companion document or YAML mapping that clearly states:

```yaml
extension:
  name: local-policy-extension
  version: "0.1.0"
  targets:
    base_version: "0.1.0"
    profiles:
      - document
      - media
  fields:
    context:
      local_access_classification:
        type: string
        requirement: conditional
        nullable: true
        description: Local access classification for the implementation.
  validation_rules:
    - require review_note when access_classification is restricted
```

The structure should remain simple. The goal is to make the extension visible, reviewable, and separable from the core schema.

---

## Relationship to the Core Model

Extensions are a tool for implementation and governance, not a shortcut around the structural model.

They should remain subordinate to the core design sequence:

```text
Base schema → Structural profile → Record
```

A good extension:

* preserves the profile contract;
* adds local value without obscuring structural meaning;
* remains intelligible to downstream consumers;
* is versioned and documented;
* does not become a hidden source of profile drift.
