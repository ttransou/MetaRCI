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

* complete one coherent task at a time;
* preserve the model-first design sequence;
* avoid introducing new profiles without structural justification;
* avoid domain-specific fields in core profiles;
* treat profile YAML and example records as expressions of the model contract;
* update tests and documentation when validator behavior changes;
* run `python validate.py` and the full test suite before marking work complete;
* avoid changing deferred items unless explicitly instructed;
* record unresolved architectural questions rather than silently deciding them;
* prefer full-file edits when YAML or Python structure is materially changed;
* keep commits scoped to coherent changes.

---

## Immediate Priorities

### 1. Create the Four Structural Profiles

Create initial profile YAML files for:

* [x] `profiles/document.yaml`
* [x] `profiles/structured-data.yaml`
* [x] `profiles/media.yaml`
* [x] `profiles/composite.yaml`

Each profile should:

* extend the MetaRCI base schema;
* preserve all three tiers;
* use only permitted override attributes;
* strengthen rather than weaken the base contract;
* add only structurally reusable custom fields;
* avoid domain-specific terminology;
* include a clear description and lifecycle status;
* remain implementation-agnostic;
* validate successfully against at least one example record.

Develop the profiles one at a time rather than drafting all four simultaneously.

Recommended order:

```text
document
→ structured-data
→ media
→ composite
```

For each profile:

1. identify the source structure it represents;
2. identify relevant inherited base fields;
3. identify justified requirement overrides;
4. identify structurally necessary custom fields;
5. record unresolved questions;
6. create a valid example record;
7. run validation before moving to the next profile.

---

### 2. Create Valid Example Records

Create at least one valid record for each structural profile:

* [x] `examples/document-record.yaml`
* [x] `examples/structured-data-record.yaml`
* [x] `examples/media-record.yaml`
* [x] `examples/composite-record.yaml`

Each example should:

* use neutral, non-proprietary content;
* exercise profile-specific fields;
* include all three tiers;
* validate successfully;
* demonstrate where null values are acceptable;
* include at least one meaningful relationship where appropriate;
* avoid domain-specific assumptions that make the profile appear narrower than intended.

Example records serve two purposes:

1. demonstrate how the profile is used;
2. provide concrete fixtures for later regression tests.

Invalid examples should normally be generated within the automated test suite rather than stored as canonical repository examples unless they serve a documentation purpose.

---

### 3. Review the Base Schema Against the Profile Set

After drafting the profiles and example records, determine whether fields currently in the base schema are genuinely universal.

* [x] Identify fields used consistently across all four profiles.
* [x] Identify fields that appear overly specific to one profile.
* [x] Identify profile fields that may instead belong in the base.

Current findings:

* The four example records consistently use the core Reference, Context, and Interpretive fields that describe identity, ingestion, organizational context, and relationships.
* `page_count` appears document-skewed. It applies to paginated sources, and `null` is appropriate when the source is not paginated.
* `review_date` appears more governance-oriented than mechanically extracted and may need clearer placement or scope.
* No base-schema edits are proposed yet; the current evidence is enough to identify candidates, not enough to move them.

Questions to resolve:

* Are bibliographic fields too document-oriented for the base?
* Which technical source properties are universal enough to remain in Reference?
* Should generated-metadata provenance be represented in the base or introduced by profiles?
* Are collection membership relationships adequately represented by the current relationship model?
* Does `source_lineage` need a more structured representation?
* Are some current base fields better represented as profile custom fields?
* Do all four profiles use `related_sources` and `relationships` consistently?
* Is the current distinction between Context and Interpretive metadata sufficiently clear for media and composite records?

Do not revise the base schema merely because one profile needs a specialized field. Base-schema changes should be supported by recurring structural evidence.

---

### 4. Add Profile-Contract Regression Tests

After the four profiles and their valid example records establish the working contract, add regression tests for the stricter MetaRCI 0.1 profile rules.

#### Valid Profile Tests

* [x] Confirm `document.yaml` and its example record pass.
* [x] Confirm `structured-data.yaml` and its example record pass.
* [x] Confirm `media.yaml` and its example record pass.
* [x] Confirm `composite.yaml` and its example record pass.
* [x] Confirm valid strengthened requirements pass.
* [x] Confirm valid strengthened nullability passes.
* [x] Confirm valid narrowed `allowed_values` passes.
* [x] Confirm genuinely new profile custom fields pass.

#### Invalid Override Tests

* [x] Reject structural override of `type`.
* [x] Reject structural override of `item_type`.
* [x] Reject structural override of `properties`.
* [x] Reject structural override of `item_properties`.
* [x] Reject weakened field requirements.
* [x] Reject weakened nullability.
* [x] Reject expansion of base `allowed_values`.
* [x] Reject introduction of `allowed_values` when the base field has none.
* [x] Reject custom fields that duplicate base fields.
* [x] Reject overrides targeting undeclared base fields.

#### Profile-Specific Enforcement Tests

* [x] Confirm required document-profile fields are enforced.
* [x] Confirm required structured-data fields are enforced.
* [x] Confirm required media fields are enforced.
* [x] Confirm required composite fields are enforced.
* [x] Confirm profile-specific field types are enforced.
* [x] Confirm profile-specific nested structures are enforced.

After adding the tests:

* [x] Update the documented test count.
* [x] Update `documentation/validation.md` to describe completed coverage.
* [x] Update profile documentation if tests expose ambiguity.
* [x] Run the complete local test suite.
* [x] Confirm GitHub Actions passes.

The tests should protect a profile contract that has already been designed and demonstrated, not substitute for profile design.

Regression-test kickoff:

* [x] Avoid moving fields based on one profile alone.
* [x] Confirm the base remains a minimum shared contract.
* [x] Confirm profiles specialize rather than redefine the base.
* [x] Confirm the three-tier distinction remains meaningful across all profiles.
* [x] Record proposed base-schema changes before implementing them.

---

### 5. Define Implementation Extensions

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
* [ ] extension versioning;
* [ ] extension provenance;
* [ ] conflicts between profile rules and extension rules.

The extension mechanism should remain subordinate to:

```text
Base schema → Structural profile → Record
```

Extensions may specialize implementation behavior, but they should not silently alter the structural profile contract.

---

## Profile Development Questions

### Document

* [ ] What document-structure fields are genuinely reusable?
* [ ] Should section, page, chapter, and clause structures be represented directly?
* [ ] How should edition and version relationships be modeled?
* [ ] Which authorship and publication fields belong in the base versus the profile?
* [ ] Is presentation content sufficiently document-like for this profile?
* [ ] How should documents containing significant embedded media be represented?

### Structured Data

* [ ] How should column or variable definitions be represented?
* [ ] How should units and value domains be modeled?
* [ ] How should keys, granularity, and missing-value conventions be represented?
* [ ] How should table-to-table and dataset-to-dataset relationships be modeled?
* [ ] Should schema definitions be nested objects or separate related records?
* [ ] How should inferred schemas be distinguished from declared schemas?
* [ ] How should transformation and derivation history be represented?

### Media

* [ ] Which technical properties are common across image, audio, and video?
* [ ] Should image, audio, and video remain one profile initially?
* [ ] How should captions, transcripts, and accessibility descriptions be represented?
* [ ] How should model-generated descriptions record provenance and review status?
* [ ] How should regions, frames, or time segments be identified?
* [ ] Which media properties belong in Reference versus Context?
* [ ] How should manually curated and machine-generated descriptions coexist?

### Composite

* [ ] What distinguishes a meaningful composite from a simple folder or archive?
* [ ] How should expected and present members be represented?
* [ ] How should member roles and ordering be expressed?
* [ ] What context may be inherited from a composite record?
* [ ] How should conflicts between collection-level and item-level metadata be handled?
* [ ] Can a composite contain members using different structural profiles?
* [ ] How should completeness be represented when expected membership is unknown?

---

## Validator Hardening

### Near-Term

Complete after or alongside profile-contract regression testing where the profile work supplies concrete examples.

* [ ] Require non-empty descriptions for full field definitions.
* [ ] Detect duplicate values in `allowed_values`.
* [ ] Confirm that overridden `allowed_values` are type-compatible with the field.
* [ ] Confirm that base requirement values are valid before comparing strength.
* [ ] Improve diagnostics for empty profile overrides.
* [ ] Add tests for multiple simultaneous schema-definition errors.
* [ ] Add tests for valid and invalid profile-specific nested fields.
* [ ] Confirm custom fields cannot collide with other custom fields after schema resolution.

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

* [x] `documentation/extensions.md`
* [ ] `documentation/profile-selection.md`
* [ ] `documentation/versioning.md`
* [ ] `documentation/governance.md`
* [ ] `documentation/implementation-guide.md`

### Documentation Rules

* Avoid duplicating detailed rules across multiple documents.
* Give each document a clear purpose.
* Link to the authoritative document when related detail belongs elsewhere.
* Update documentation when executable validator behavior changes.
* Distinguish current behavior from deferred or proposed behavior.
* Keep implementation examples subordinate to the generic model.

---

## Implementation Testbeds

Implementation testbeds may be used to evaluate MetaRCI without defining the framework.

Potential testbeds include:

* [ ] SCARAG Shakespeare branch for `document`;
* [ ] a neutral tabular dataset for `structured-data`;
* [ ] an image or diagram collection for `media`;
* [ ] a corpus-level package for `composite`.

For each testbed, record:

* fields that map cleanly;
* fields that feel forced;
* missing structural concepts;
* ambiguous tier placement;
* validator limitations;
* extension needs;
* evidence for or against changes to the base model;
* evidence for or against changes to the selected profile.

Changes to MetaRCI should be justified by recurring structural evidence, not by one implementation alone.

Testbeds should be introduced only after the corresponding generic profile and example record exist.

---

## Release Preparation

### Version 0.1.0

Before considering MetaRCI 0.1.0 ready:

* [ ] All four structural profiles exist.
* [ ] All four profiles validate.
* [ ] Each profile has at least one valid example record.
* [ ] The base schema has been reviewed against all four profiles.
* [ ] Profile-contract regression tests pass.
* [ ] Profile-specific validation tests pass.
* [x] CI passes on the default branch.
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
→ Structural profiles
→ Valid example records
→ Base-model review
→ Regression validation
→ Extensions
→ Implementation testing
→ Revision from evidence
```

Implementation use cases may challenge the model, but they should not replace the model-first design process.
