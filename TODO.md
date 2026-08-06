# MetaRCI TODO

## Current Objective

Develop MetaRCI as a domain-agnostic, three-tier metadata model with:

* a stable base schema;
* a limited set of structural profiles;
* enforceable profile and record validation;
* clear extension boundaries;
* implementation testing without allowing individual use cases to define the model.

---

## Current Status

### Completed

* [x] Define the three MetaRCI tiers:

  * Reference
  * Context
  * Interpretive
* [x] Create the base schema.
* [x] Create an example profile.
* [x] Create an example metadata record.
* [x] Add YAML parsing and root validation.
* [x] Add base-schema, profile, and record document validation.
* [x] Add recursive field-definition validation.
* [x] Add recursive record-value validation.
* [x] Add nested object and object-list validation.
* [x] Add required-field and unknown-field validation.
* [x] Add exact base/profile version compatibility checks.
* [x] Add profile path and base-schema path validation.
* [x] Add aggregated error reporting by validation stage.
* [x] Add command-line file arguments.
* [x] Add automated tests.
* [x] Add GitHub Actions continuous integration.
* [x] Add `requirements.txt`.
* [x] Document validator behavior.
* [x] Define the initial structural profile model.
* [x] Restrict profile overrides in MetaRCI 0.1.
* [x] Prevent custom fields from shadowing base fields.

---

## Agent Working Rules

When working from this file, an agent should:

- complete one coherent task at a time;
- preserve the model-first design sequence;
- avoid introducing new profiles without structural justification;
- avoid domain-specific fields in core profiles;
- update tests and documentation when validator behavior changes;
- run `python validate.py` and the full test suite before marking work complete;
- avoid changing deferred items unless explicitly instructed;
- record unresolved architectural questions rather than silently deciding them;
- prefer full-file edits when YAML or Python structure is materially changed;
- keep commits scoped to coherent changes.

---

## Immediate Priorities

### 1. Add Profile-Constraint Tests

Add regression tests for the stricter MetaRCI 0.1 profile contract.

* [ ] Reject structural override of `type`.
* [ ] Reject structural override of `item_type`.
* [ ] Reject structural override of `properties`.
* [ ] Reject structural override of `item_properties`.
* [ ] Reject weakened field requirements.
* [ ] Reject weakened nullability.
* [ ] Reject expansion of base `allowed_values`.
* [ ] Reject introduction of `allowed_values` when the base field has none.
* [ ] Reject custom fields that duplicate base fields.
* [ ] Confirm valid strengthened requirements still pass.
* [ ] Confirm valid narrowed `allowed_values` still pass.

After adding the tests:

* [ ] Update the documented test count.
* [ ] Update the validation guide to describe the completed coverage.
* [ ] Confirm GitHub Actions passes.

---

### 2. Create the Four Structural Profiles

Create initial profile YAML files for:

* [ ] `profiles/document.yaml`
* [ ] `profiles/structured-data.yaml`
* [ ] `profiles/media.yaml`
* [ ] `profiles/composite.yaml`

Each profile should:

* extend the MetaRCI base schema;
* preserve all three tiers;
* use only permitted override attributes;
* add only structurally reusable custom fields;
* avoid domain-specific terminology;
* include a clear description and lifecycle status;
* validate successfully against at least one example record.

---

### 3. Review the Base Schema Against the Profile Set

Determine whether fields currently in the base schema are genuinely universal.

* [ ] Identify fields that belong in every profile.
* [ ] Identify fields that may belong only in one structural profile.
* [ ] Avoid moving fields prematurely without implementation evidence.
* [ ] Confirm the base remains a minimum shared contract.
* [ ] Confirm profiles specialize rather than redefine the base.

Questions to resolve:

* Are bibliographic fields too document-oriented for the base?
* Which technical source properties are universal enough to remain in Reference?
* Should generated-metadata provenance be represented in the base or introduced by profiles?
* Are collection membership relationships adequately represented by the current relationship model?
* Does `source_lineage` need a more structured representation?

---

### 4. Define Implementation Extensions

Create:

```text
documentation/extensions.md
```

The document should define how implementations may add local or domain-specific behavior without creating new structural profiles.

Topics to cover:

* [ ] namespaced custom fields;
* [ ] controlled vocabularies;
* [ ] authority files;
* [ ] local validation rules;
* [ ] organizational policy;
* [ ] corpus-specific metadata;
* [ ] sensitivity and access classifications;
* [ ] compatibility with structural profiles;
* [ ] separation between profile fields and implementation fields;
* [ ] extension versioning.

The extension mechanism should remain subordinate to:

```text
Base schema → Structural profile → Record
```

---

## Profile Development Questions

### Document

* [ ] What document-structure fields are genuinely reusable?
* [ ] Should section, page, chapter, and clause structures be represented directly?
* [ ] How should edition and version relationships be modeled?
* [ ] Which authorship and publication fields belong in the base versus the profile?

### Structured Data

* [ ] How should column or variable definitions be represented?
* [ ] How should units and value domains be modeled?
* [ ] How should keys, granularity, and missing-value conventions be represented?
* [ ] How should table-to-table and dataset-to-dataset relationships be modeled?
* [ ] Should schema definitions be nested objects or separate related records?

### Media

* [ ] Which technical properties are common across image, audio, and video?
* [ ] Should image, audio, and video remain one profile initially?
* [ ] How should captions, transcripts, and accessibility descriptions be represented?
* [ ] How should model-generated descriptions record provenance and review status?
* [ ] How should regions, frames, or time segments be identified?

### Composite

* [ ] What distinguishes a meaningful composite from a simple folder or archive?
* [ ] How should expected and present members be represented?
* [ ] How should member roles and ordering be expressed?
* [ ] What context may be inherited from a composite record?
* [ ] How should conflicts between collection-level and item-level metadata be handled?

---

## Validator Hardening

### Near-Term

* [ ] Add the remaining profile-constraint tests.
* [ ] Require non-empty descriptions for full field definitions.
* [ ] Detect duplicate values in `allowed_values`.
* [ ] Confirm that overridden `allowed_values` are type-compatible with the field.
* [ ] Confirm that base requirement values are valid before comparing strength.
* [ ] Improve diagnostics for empty profile overrides.
* [ ] Add tests for multiple simultaneous schema-definition errors.

### Later

* [ ] Add optional JSON diagnostic output.
* [ ] Add validation for multiple records in one command.
* [ ] Add directory-level record validation.
* [ ] Add semantic-version parsing.
* [ ] Consider warning-level diagnostics distinct from errors.
* [ ] Consider profile lifecycle enforcement.
* [ ] Consider validation of extension documents.
* [ ] Consider JSON Schema export.
* [ ] Consider packaging the validator as an installable CLI.

---

## Documentation

### Existing

* [x] `README.md`
* [x] `documentation/tier-notes.md`
* [x] `documentation/validation.md`
* [x] `documentation/profile-model.md`

### Planned

* [ ] `documentation/extensions.md`
* [ ] `documentation/profile-selection.md`
* [ ] `documentation/versioning.md`
* [ ] `documentation/governance.md`
* [ ] `documentation/implementation-guide.md`

Documentation should not duplicate detailed rules unnecessarily. Each document should have a clear purpose and link to related guidance.

---

## Examples and Test Records

Create at least one valid record for each structural profile.

* [ ] Document example record.
* [ ] Structured-data example record.
* [ ] Media example record.
* [ ] Composite example record.

Each example should:

* use neutral, non-proprietary content;
* exercise profile-specific fields;
* include all three tiers;
* validate successfully;
* demonstrate where null values are acceptable;
* include at least one meaningful relationship where appropriate.

Invalid examples should remain generated within the automated test suite rather than stored as canonical repository examples unless they serve a documentation purpose.

---

## Implementation Testbeds

Implementation testbeds may be used to evaluate MetaRCI without defining the framework.

Potential testbeds include:

* [ ] SCARAG Shakespeare branch for `document`;
* [ ] a tabular dataset for `structured-data`;
* [ ] an image or diagram collection for `media`;
* [ ] a corpus-level package for `composite`.

For each testbed, record:

* fields that map cleanly;
* fields that feel forced;
* missing structural concepts;
* ambiguous tier placement;
* validator limitations;
* extension needs;
* evidence for or against changes to the base model.

Changes to MetaRCI should be justified by recurring structural evidence, not by one implementation alone.

---

## Release Preparation

### Version 0.1.0

Before considering MetaRCI 0.1.0 ready:

* [ ] All four structural profiles exist.
* [ ] All four profiles validate.
* [ ] Each profile has at least one valid example record.
* [ ] Profile-constraint tests pass.
* [ ] CI passes on the default branch.
* [ ] Core documentation is internally consistent.
* [ ] Extension boundaries are documented.
* [ ] Base and profile versioning rules are documented.
* [ ] Known limitations are listed.
* [ ] Repository structure is reviewed.
* [ ] License is selected.
* [ ] Changelog is created.
* [ ] Release tag is created.

---

## Deferred Ideas

These ideas are intentionally deferred until there is evidence they are necessary.

* Profile-to-profile inheritance.
* Deep recursive profile overrides.
* Domain-specific core profiles.
* Remote schema resolution.
* Automated metadata extraction.
* Required use of language, vision, or multimodal models.
* General event or transaction modeling.
* Knowledge-graph serialization.
* Ontology alignment.
* Automatic profile selection.
* Record transformation between profile versions.

Deferral does not imply rejection. It preserves the scope of MetaRCI 0.1.

---

## Guiding Principle

MetaRCI should evolve from a stable model outward.

The intended sequence is:

```text
Model
→ Contract
→ Validation
→ Structural profiles
→ Extensions
→ Implementation testing
→ Revision from evidence
```

Implementation use cases may challenge the model, but they should not replace the model-first design process.
