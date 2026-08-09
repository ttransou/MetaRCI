# Structured-Data Profile

## Purpose

Current contract:

* The structured-data profile exists as a structural profile named structured-data.
* It extends the base schema at version 0.1.0 and is currently draft.

Current guidance:

* Use this profile when source meaning depends substantially on explicit data structure.

## Structural Characteristics

Current guidance:

* Typical concerns include variables/columns, value domains, keys, granularity, and lineage.

Open question:

* Which of these concerns should become executable profile fields versus remain implementation guidance?

## Profile Emphasis

Current contract:

* The current YAML sets no tier overrides.
* The profile currently declares three structured-data custom fields:
  * `reference.source_fields`
  * `context.field_context`
  * `interpretive.field_interpretations`

Current guidance:

* Emphasize schema-aware interpretation rather than file format naming.

## Profile Scope

Current guidance:

* The `structured-data` profile models bounded sources whose meaning depends materially on explicit or recoverable data structure, including fields, variables, columns, records, and comparable schema-level organization.
* File format alone does not determine profile membership. A source belongs in the structured-data profile when its data structure is materially important to interpreting the source.
* Source-native or mechanically observable data structure belongs in the Reference tier.
* Externally supplied or curated semantic explanation about that structure belongs in the Context tier.
* Analytical characterization inferred from observed data belongs in the Interpretive tier.
* The structured-data profile should provide a first-class representation of source-native fields or variables rather than relying exclusively on narrative notes or relationships.

Current implementation status:

* Reusable field-level representation is implemented in the profile YAML contract.
* Cross-tier field association is implemented using lightweight locators that point back to `reference.source_fields`.
* Validator tests currently enforce declared property types and required object presence for these structures.

## Tier-Placement Principles

Current guidance:

* Tier placement follows the evidentiary basis of an assertion rather than the category of metadata or the tool, parser, model, or person that produced it.
* Metadata about the same logical field property may therefore belong in different tiers when supported by different kinds of evidence.

### Field or Variable Identity

Current guidance:

* Source-native field or variable identity belongs in Reference.
* The minimum defensible field identity consists of the source-provided field name and, where meaningful, its mechanically observable source order or position.
* Semantic properties of a field should be evaluated separately rather than assumed to belong to the same tier as field identity.

Current contract:

* Source-native field identity is represented through `reference.source_fields`.

### Value Type

Current guidance:

* A value type explicitly declared by or mechanically recoverable from the source belongs in Reference.
* A value type supplied by an external schema, data dictionary, or other contextual source belongs in Context.
* A value type inferred from observed values belongs in Interpretive.
* An inferred value type must not be represented as though it were source-declared.
* `value_type` therefore does not have a single inherent tier independent of its evidentiary basis.

Current design implication:

* A single monolithic Context-tier `variable_definitions` object may not adequately preserve the distinction between source-native, externally supplied, and inferred assertions.
* The final executable representation should preserve field identity across tiers without collapsing those epistemic distinctions.
- Validator behavior in v0.1 enforces the declared structure and property types of field-identity metadata but does not enforce full identity sufficiency across `name`, `position`, `path`, and `local_id`.
- The requirement that each field entry contain enough information to identify the field reliably remains profile guidance until a cross-property validation rule is implemented.

Deferred:

* The final executable representation of `value_type`.
* Strict validator enforcement that Context and Interpretive locators resolve to existing Reference entries.

### Unit

Current guidance:

- Unit metadata follows the evidentiary basis of the assertion rather than having a single inherent tier.
- A unit explicitly declared by or mechanically recoverable from the source belongs in Reference.
- A unit supplied by an external data dictionary, specification, or other contextual source belongs in Context.
- A unit inferred from naming conventions, observed values, or analyst judgment belongs in Interpretive.
- An inferred unit must not be represented as though it were source-declared.

Current design implication:

- The executable representation of unit metadata should preserve the distinction between source-native, externally supplied, and inferred assertions.
- Unit syntax, normalization, and controlled vocabularies are separate interoperability questions and are not settled by this tier-placement decision.

Deferred:

- Whether units should use free text, normalized codes, or a controlled standard.
- How unit assertions in different tiers should be associated with the same source-native field or variable.

### Value Domain

Current guidance:

- Value-domain metadata follows the evidentiary basis of the assertion rather than having a single inherent tier.
- A value domain explicitly declared by or mechanically recoverable from the source belongs in Reference.
- A value domain supplied by an external data dictionary, codebook, specification, or other contextual source belongs in Context.
- A value domain inferred from observed values belongs in Interpretive.
- Observed values must not be treated as a declared domain unless the source or an authoritative contextual source establishes that constraint.

Current design implication:

- The executable representation of value-domain metadata should preserve the distinction between declared constraints and values merely observed in the dataset.
- A set of observed values is not equivalent to an allowed-value set.
- Range, enumeration, code-list, and other domain forms may eventually require different structural representations.

Deferred:

- The minimum executable shape for value domains.
- Whether ranges, enumerations, code lists, and other domain types should share one representation or use distinct structures.
- How value-domain assertions in different tiers should be associated with the same source-native field or variable.

### Missing-Value Rule

Current guidance:

- Missing-value metadata follows the evidentiary basis of the assertion rather than having a single inherent tier.
- A missing-value convention explicitly declared by or mechanically recoverable from the source belongs in Reference.
- A missing-value convention supplied by an external data dictionary, codebook, specification, or other contextual source belongs in Context.
- A missing-value convention inferred from observed values or recurring patterns belongs in Interpretive.
- An observed sentinel value, blank pattern, or other absence pattern must not be represented as a declared missing-value rule without supporting evidence.

Current design implication:

- The presence of missing values and the rule governing how missing values are represented are distinct assertions.
- The executable representation should preserve the distinction between source-declared missing-value semantics and patterns inferred from the data.
- Missing-value representation may include sentinel values, null markers, blank values, or other source-specific conventions.

Deferred:

- The minimum executable shape for missing-value rules.
- Whether different missing-value mechanisms require distinct structural forms.
- How missing-value assertions in different tiers should be associated with the same source-native field or variable.

### Schema-Source Distinction

Current guidance:

- Do not introduce a general `schema_source_type` field solely to distinguish source-declared, externally supplied, and inferred schema assertions.
- MetaRCI tier placement already expresses the epistemic basis of an assertion:
  - source-declared or mechanically recoverable assertions belong in Reference;
  - externally supplied or curated assertions belong in Context;
  - inferred or analytically derived assertions belong in Interpretive.
- Adding a second declared-versus-inferred classification inside a single tier would duplicate the RCI model and could create contradictory provenance signals.

Current design implication:

- The executable structured-data model should preserve epistemic distinctions through tier placement rather than through a parallel `schema_source_type` flag.
- Schema provenance that is itself asserted by the source, such as a named schema language, schema version, or referenced schema artifact, is a separate metadata concern and may still require representation.

Deferred:

- Whether structured-data sources require explicit schema-provenance fields beyond the existing source-lineage and relationship mechanisms.
- How separately modeled schema artifacts should relate to structured-data records.

### Field Identity and Cross-Tier Association

Current guidance:

- Structured-data metadata requires a stable way to associate Reference, Context, and Interpretive assertions with the same source-native field or variable.
- MetaRCI should prefer source-native field identity when that identity is sufficiently stable and unambiguous within the source.
- A synthetic per-field identifier should not be required for every structured-data source solely to support cross-tier association.
- When source-native identity is ambiguous, duplicated, absent, nested, or otherwise insufficient, implementations should add the minimum additional disambiguation needed to identify the field reliably.

Recommended contingency order:

1. Use the source-native field name or equivalent identifier when it is unique and stable.
2. If the name alone is insufficient, combine it with a source-grounded locator such as position, ordinal, path, or equivalent structural information.
3. If source-native locators remain insufficient, use a local synthetic field identifier as an implementation-level association key.

Current design implication:

- Stable association is required; a universal synthetic identifier strategy is not.
- Synthetic identifiers used for disambiguation are implementation metadata and must not be represented as source-native facts unless the source itself provides the identifier.
- The association mechanism should remain local to the structured-data record unless later evidence demonstrates that individual fields require independent MetaRCI records.

Edge-case guidance:

- Duplicate field names should be disambiguated using source-grounded position, path, ordinal, or comparable structure where available.
- Unnamed fields may require position, path, or a local synthetic identifier.
- Nested structured data may require path-based identity rather than simple field names.
- Multi-row or hierarchical headers may require a composite source-native locator.
- Field order should not be used as an identity component when the source format does not assign meaningful or stable ordering.
- Renamed fields across source versions should not be assumed to represent the same field solely because their positions match.
- Fields created during ingestion or transformation should be distinguished from fields present in the original source.

Deferred:

- The exact executable shape for field locators or association keys.
- Whether MetaRCI should standardize a reusable field-locator object in a later profile revision.
- Whether cross-version field identity requires additional lineage or relationship semantics.

### Field Identity Sufficiency and Fallback

Current guidance:

- A structured-data field or variable must have enough source-grounded information to be distinguished reliably within the source.
- MetaRCI should not require one universally mandatory locator property for every field because structured-data sources vary in how field identity is expressed.
- Field identity may be established through a source-native name, position, ordinal, path, composite header, or comparable structural locator.
- The minimum sufficient identity depends on the source structure.
- A field name alone is sufficient only when that name is stable and unambiguous within the source.
- Position or ordinal may be used when source order is meaningful and stable.
- Path-based identity may be used for nested or hierarchical structured data.
- Multiple source-grounded properties may be combined when no single property is sufficient to disambiguate the field.

Recommended contingency order:

1. Use a source-native field name or equivalent identifier when it is unique and stable.
2. If the name alone is insufficient, combine it with source-grounded position, ordinal, path, or comparable structural information.
3. If no name is available, use another stable source-grounded locator such as position, ordinal, path, or equivalent structure.
4. If source-native identity remains insufficient, assign a local synthetic identifier as an implementation-level fallback.
5. If even a local synthetic identifier cannot be tied reliably to a stable source location, preserve the field as weakly identifiable rather than implying stronger identity than the source supports.

Current design implication:

- Stable field association is required, but a universal synthetic identifier is not.
- Synthetic identifiers are contingency mechanisms and should not be treated as source-native facts unless the source itself provides them.
- The executable field representation should permit flexible combinations of identity properties rather than requiring every field to provide the same locator set.
- Validator behavior may initially enforce the types of available identity properties without enforcing full cross-property identity sufficiency.
- Semantic identity constraints that exceed current validator capabilities may remain explicit profile guidance in v0.1 rather than forcing an artificially rigid schema.

Edge-case guidance:

- Duplicate field names should be disambiguated using position, ordinal, path, composite headers, or another source-grounded locator.
- Unnamed fields should use position, path, ordinal, or a local synthetic identifier where necessary.
- Nested JSON, XML, or comparable structures may require path-based identity.
- Multi-row or hierarchical headers may require composite field identity rather than a single flat name.
- Field position should not be treated as stable identity when the source format does not assign meaningful or persistent ordering.
- Renamed fields across source versions should not be assumed to represent the same logical field solely because their positions match.
- Fields created during ingestion, normalization, or transformation should be distinguished from fields present in the original source.
- Null, blank, NA, or other missing record-level values do not affect the identity of the field itself; field identity and record-level missingness are separate concerns.

Deferred:

- The exact executable combination of `name`, `position`, `ordinal`, `path`, and synthetic identifier properties.
- Whether MetaRCI should standardize a reusable field-locator object.
- Whether later validator versions should enforce an at-least-one identity-sufficient-property rule.
- Whether cross-version field identity requires additional lineage or relationship semantics.



## Rationale for Current Fields

Current contract:

* The profile now includes executable field-level structures across all three tiers.
* The canonical structured-data example validates with `reference.source_fields` under the current contract.

Current guidance:

* Keep the v0.1 minimum field-association shapes stable while gathering evidence for stricter locator-resolution semantics and advanced domain representations.

## Relevant Design Questions

Open question:

* How should column or variable definitions be modeled in a reusable way?
* How should units, domains, and missing-value conventions be represented?
* Should schema definitions be nested in-record structures or separate related records?
* How should inferred schema be distinguished from declared schema?
* Whether to add reusable schema-description custom fields in reference/context/interpretive tiers.
* Whether additional validator checks are needed for structured-data-specific semantics.

## Current Decisions Supported by YAML

Current contract:

- `reference.source_fields` is implemented as a conditional list of field-identity objects.
- Supported identity properties are `name`, `position`, `path`, and `local_id`.
- `context.field_context` is implemented as a conditional list of externally sourced field assertions.
- `interpretive.field_interpretations` is implemented as a conditional list of inferred field assertions.
- The validator enforces the declared types of these properties.

Current contract:

- No individual locator property is universally required.
- Identity sufficiency is currently a semantic profile rule rather than a validator-enforced cross-property constraint.

### Cross-Tier Field Association

Current guidance:

- Metadata about a structured-data field may originate from different epistemic bases and therefore may belong in different MetaRCI tiers.
- Cross-tier field metadata should attach to the source-field identity established in Reference rather than duplicate the full source-field definition in Context or Interpretive metadata.
- Reference remains the authoritative local description of source-native field identity.
- Context assertions about a field should point back to that Reference identity.
- Interpretive assertions about a field should also point back to that Reference identity.
- Cross-tier association should preserve the distinction between field identity and assertions made about that field.

Current design implication:

- `reference.source_fields` acts as the local anchor for field identity.
- Context and Interpretive structures should use lightweight field locators rather than restating complete field definitions.
- Field locators should reuse the same identity properties available to `reference.source_fields`:
  - `name`
  - `position`
  - `path`
  - `local_id`
- Locator properties should be populated only as needed to identify the intended source field reliably.
- A field locator does not create a new field identity; it refers back to an identity already established in Reference.
- Context and Interpretive field metadata should not silently redefine a Reference field by using conflicting identity information.

Recommended association pattern:

1. Establish the source-native field in `reference.source_fields`.
2. Use the minimum sufficient field locator when attaching Context metadata to that field.
3. Use the minimum sufficient field locator when attaching Interpretive metadata to that field.
4. Preserve the same identity-contingency rules used by `reference.source_fields` when names are duplicated, absent, nested, or otherwise insufficient.

Example conceptual pattern:

```yaml
reference:
  source_fields:
    - name: latitude
      position: 2

context:
  field_context:
    - field:
        name: latitude
        position: 2
      unit: degrees_north

interpretive:
  field_interpretations:
    - field:
        name: latitude
        position: 2
      value_type: float

```

The field object in Context or Interpretive is a locator to the Reference field, not a second definition of that field.

Edge-case guidance:

- When a field name is unique and stable, the name alone may be sufficient for cross-tier association.
- When a field name is duplicated or ambiguous, the locator should include additional source-grounded properties such as position, ordinal, path, or equivalent structure.
- When a local synthetic identifier is required for Reference identity, that same local_id may be used for cross-tier association.
- Nested and hierarchical sources may rely primarily on path-based association.
- Cross-tier assertions should not rely on field position when source ordering is not meaningful or stable.
- If an assertion cannot be associated reliably with a Reference field, that uncertainty should be preserved rather than resolved through invented identity.

Deferred:

- The exact executable shape of Context-tier field assertions.
- The exact executable shape of Interpretive-tier field assertions.
- Whether a reusable field-locator object should eventually be standardized across profile tiers.
- Whether validator logic should later verify that Context and Interpretive field locators resolve to an existing reference.source_fields entry.
- Whether cross-record or cross-version field association requires separate lineage or relationship semantics.

### Context-Tier Field Assertions

Current guidance:

- Context-tier field metadata represents externally supplied or curated assertions about a source field whose identity is established in Reference.
- `context.field_context` associates those assertions with an existing `reference.source_fields` entry through a lightweight field locator.
- A field-context entry should not redefine the source field; it should describe externally supplied metadata about that field.
- Each field-context entry should identify the external source supporting its assertions.
- One field-context entry should represent assertions supported by one `external_source_id` so that provenance remains unambiguous.

Current contract:

- `field` is the required locator back to the Reference field identity.
- `external_source_id` is required because Context assertions must remain attributable to the external source that supports them.
- The field locator may use the same identity properties supported by `reference.source_fields`:
  - `name`
  - `position`
  - `path`
  - `local_id`
- No single locator child is universally required in v0.1; the locator must contain enough information to identify the intended Reference field reliably.
- Context semantic properties should be populated only when supported by the identified external source.

Current semantic properties:

- `external_field_name`
- `value_type`
- `unit`
- `value_domain`
- `missing_value_rule`

Current evidence and adoption status:

- The `iris.data` / `iris.names` testbed demonstrates externally supplied field names, value types, units, and a value domain that cannot legitimately be represented as source-native Reference facts for `iris.data`.
- This evidence supported adoption of the current Context-tier field-association structure and superseded the earlier monolithic `context.variable_definitions` proposal.

Current executable shape:

- `context.field_context` is a conditional, nullable `list<object>`.
- Each item requires:
  - `field` as an object locator;
  - `external_source_id` as a non-nullable string.
- Semantic child properties are conditional and nullable unless later evidence justifies stronger requirements.

Edge-case guidance:

- Multiple external sources may describe the same Reference field through separate `field_context` entries.
- Conflicting external assertions should remain separately attributable rather than being silently merged.
- A Context field locator should follow the same identity-sufficiency and fallback rules established for `reference.source_fields`.
- If the external source cannot be identified reliably, the assertion should not be represented as fully sourced Context metadata.

Deferred:

- Validator enforcement that a `field` locator resolves to an existing `reference.source_fields` entry.
- Validator enforcement of full locator identity sufficiency.
- Conflict-resolution semantics when multiple external sources make incompatible assertions about the same field.
- More structured representations for complex value domains or missing-value rules.

### Interpretive-Tier Field Assertions

Current contract:

- Interpretive field metadata represents analytical or inferred assertions about a source field whose identity is established in Reference.
- `interpretive.field_interpretations` associates those assertions with an existing `reference.source_fields` entry through a lightweight field locator.
- A field-interpretation entry should not redefine the source field or present inferred properties as source-declared schema.
- Interpretive field assertions should preserve the basis and scope of the inference when practical.
- Observed characteristics should remain distinguishable from declared constraints, externally supplied semantics, or source-native structure.

Current contract:

- `field` is the required locator back to the Reference field identity.
- The field locator may use the same identity properties supported by `reference.source_fields`:
  - `name`
  - `position`
  - `path`
  - `local_id`
- No single locator child is universally required in v0.1; the locator must contain enough information to identify the intended Reference field reliably.
- `inferred_value_type` may be used for value-type characterization derived from observed source values rather than declared schema.
- `observed_characteristics` may record field-level patterns or properties observed during analysis without promoting those observations into declared schema rules.
- `inference_basis` should describe the evidence or analytical basis supporting the field-level interpretation.
- Interpretive assertions must not be represented as Reference or Context merely because they can be produced mechanically by a parser, profiler, model, or other tool.

Current evidence and adoption status:

- The `data-source-001` USGS testbed demonstrates field-level inferred value-type and observed-characteristic assertions for the `time` and `mag` fields.
- Those assertions are more precisely represented through a field-targeted Interpretive structure than through record-level `interpretive_notes` alone.
- The testbed demonstrated a recurring need to associate inferred metadata with a specific Reference field while preserving its Interpretive epistemic status, and the profile now implements this structure.

Current executable shape:

- `interpretive.field_interpretations` is a conditional, nullable `list<object>`.
- Each item requires:
  - `field` as an object locator.
- Candidate interpretive properties include:
  - `inferred_value_type`
  - `observed_characteristics`
  - `inference_basis`
- Semantic child properties remain conditional and nullable unless later evidence justifies stronger requirements.

Edge-case guidance:

- Multiple interpretations may target the same Reference field when they represent distinct analytical claims.
- Conflicting interpretations should remain explicit rather than being silently merged into one asserted field definition.
- Observed values, ranges, categories, formats, or patterns should not be represented as declared constraints without supporting source or contextual evidence.
- Inference derived from a sample or subset should preserve that limitation in `inference_basis` or equivalent interpretive documentation.
- If a field cannot be associated reliably with a Reference identity, the interpretation should preserve that uncertainty rather than inventing a stronger association.

Deferred:

- Validator enforcement that a `field` locator resolves to an existing `reference.source_fields` entry.
- Validator enforcement of full locator identity sufficiency.
- More structured representations for statistical distributions, observed ranges, inferred domains, or other analytical field characteristics.
- Confidence scoring or formal inference-method metadata.
- Cross-version interpretation lineage.


## Boundaries with Other Profiles

Current guidance:

* Prefer document when source is primarily narrative text.
* Prefer media when meaning is primarily visual/audio/spatial.
* Prefer composite when the unit is a package or aggregation of multiple sources.

## Example Applications

Current guidance:

* Tabular datasets, CSV exports, spreadsheet extracts, and machine-readable record sets.

Deferred:

* A heavy schema-language model in profile YAML.

## Current Checkpoint

Current contract:

* Structured-data profile v0.1 now has tested field-level representation across Reference, Context, and Interpretive tiers; 61 validator tests pass.
* Implemented field structures:
  * `reference.source_fields`
  * `context.field_context`
  * `interpretive.field_interpretations`
* Current full validator suite status: 61 tests pass.

Current guidance:

* Preserve the historical `variable_definitions` testbed results as superseded hypothesis evidence.
* Continue using source-grounded tier placement rules for value type, units, value domains, and missing-value assertions.
* Keep resolver-level semantics (for example, strict locator-resolution checks) as deferred until additional cross-source evidence and validator-scope decisions are approved.
