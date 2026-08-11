# Structured-Data-Relational Profile

## Purpose

Current contract:

* The `structured-data-relational` profile exists as a structural profile named `structured-data-relational`.
* It extends the MetaRCI base schema directly at version 0.1.0.
* It is currently draft.
* The current profile declares no tier overrides or relational custom fields.

Current guidance:

* Use this profile when source meaning depends materially on **explicit relational structure**.
* `structured-data-relational` maintains its own profile contract and evidence path.
* Decisions established through the `structured-data` profile may be reused where their epistemic and structural logic remains applicable.
* Do not interpret similarities between `structured-data` and `structured-data-relational` as executable profile inheritance; current MetaRCI profile resolution does not support profile-to-profile inheritance.

## Structural Characteristics

Current guidance:

* Relational sources organize information through explicit structured objects and relationships among those objects.
* Typical structural concerns may include:

  * database or schema identity;
  * tables;
  * views;
  * columns;
  * declared data types;
  * nullability;
  * primary keys;
  * foreign keys;
  * uniqueness constraints;
  * other declared constraints;
  * and relationships among tables or comparable relational objects.
* Relational structure should be modeled according to what the source actually declares or exposes rather than reconstructed from assumed database conventions.

Open question:

* Which relational characteristics recur strongly enough across independent relational sources to become executable profile fields?

## Profile Emphasis

Current contract:

* The current YAML sets no tier overrides.
* The current YAML declares no relational custom fields.

Current guidance:

* Preserve the existing MetaRCI distinction between source-native structure, externally supplied semantic context, and analytical interpretation.
* Emphasize relational structure rather than SQL syntax or database-vendor implementation details.
* Avoid turning the profile into a general database-management-system ontology.
* Candidate fields should be promoted only when testbed evidence demonstrates reusable structural value across relational implementations.

## Profile Scope

Current guidance:

* The `structured-data-relational` profile models bounded sources whose meaning depends materially on explicit relational structure.
* Profile membership should depend on the structure preserved by the source, not merely on the fact that the source originated in a relational database management system.
* A flat export from a relational database may still be represented using `structured-data` when the exported source no longer preserves materially significant relational structure.
* A database schema, related table set, view structure, or comparable source that preserves keys, constraints, object identity, and relationships creates stronger pressure for `structured-data-relational`.
* Source-native or mechanically recoverable relational structure belongs in Reference.
* Externally supplied or curated explanation of relational structure belongs in Context.
* Analytical or inferred relational meaning belongs in Interpretive.

Open question:

* What is the minimum bounded source unit for this profile: a table, schema, database, view, query result, or another relationally coherent unit?

Deferred:

* Whether query results that retain relational lineage should use this profile or `structured-data`.
* Whether separately modeled tables, views, or schemas should receive independent MetaRCI records.

## Relationship to Structured Data

Current guidance:

* `structured-data-relational` addresses relationally structured sources whose schema relationships are materially important to representation or interpretation.
* It draws on decisions established through the `structured-data` profile where those decisions remain applicable.
* Shared concerns may include field identity, declared value types, externally supplied field semantics, and inferred field characteristics.
* Relational testing should introduce additional structure only where the existing Structured Data contract does not represent relational semantics adequately.
* The two profiles maintain separate executable contracts and evidence paths.

Current architecture note:

* `structured-data-relational.yaml` extends the MetaRCI base schema directly.
* It does not extend `structured-data.yaml`.
* Profile-to-profile inheritance remains outside the current executable contract.

## Tier-Placement Principles

Current guidance:

* Tier placement follows the evidentiary basis of an assertion rather than the database feature, extraction tool, parser, query engine, or analyst that produced it.
* Metadata about the same relational object or property may belong in different tiers when supported by different kinds of evidence.
* A database engine's ability to derive, infer, or expose a property does not by itself determine its epistemic tier.

### Relational Object Identity

Current guidance:

* Source-native names or identifiers for databases, schemas, tables, views, columns, constraints, or comparable relational objects belong in Reference when explicitly present or mechanically recoverable.
* Externally supplied aliases, business names, catalog descriptions, or semantic labels belong in Context.
* Analytical classifications of a relational object's role or meaning belong in Interpretive.

Open question:

* Whether relational objects require reusable local locator structures comparable to `reference.source_fields` in the existing Structured Data profile.

### Declared Data Type

Current guidance:

* A column type explicitly declared in the relational schema belongs in Reference.
* A type supplied by an external data dictionary, semantic model, or other contextual authority belongs in Context.
* A type inferred from observed values belongs in Interpretive.
* Inferred types must not be promoted into Reference merely because they were generated mechanically.

Current design implication:

* Existing Structured Data tier-placement rules for value type remain applicable where the same evidentiary distinctions exist.
* Relational testing should determine whether database-native type declarations require additional representation beyond the existing field-level model.

Deferred:

* Vendor-specific type systems and normalization across database engines.
* Whether relational profiles require a portable normalized type representation in addition to source-native declarations.

### Nullability

Current guidance:

* A nullable or non-nullable constraint explicitly declared by the relational schema belongs in Reference.
* An externally documented business requirement concerning nullability belongs in Context.
* A conclusion that a field appears always populated or always null based on observed records belongs in Interpretive.
* Observed completeness must not be treated as equivalent to a declared `NOT NULL` constraint.

Open question:

* Whether declared nullability should become a first-class relational field property or be represented through a more general constraint structure.

### Primary and Foreign Keys

Current guidance:

* Primary-key and foreign-key declarations recoverable from the source schema belong in Reference.
* External explanation of what those keys represent in the business, institutional, or domain context belongs in Context.
* Inferred key-like relationships that are not declared by the source belong in Interpretive.
* A high-cardinality or apparently unique column must not be represented as a declared primary key without supporting source evidence.
* A recurring value correspondence between two tables must not be represented as a declared foreign-key relationship unless the source establishes that relationship.

Current design implication:

* Relational testing should preserve the distinction between **declared structural relationships** and **inferred semantic or statistical relationships**.

Deferred:

* The minimum executable representation for primary keys.
* The minimum executable representation for foreign keys.
* Whether composite keys require a dedicated ordered field-reference structure.
* Referential-integrity validation beyond structural schema validation.

### Constraints

Current guidance:

* Source-declared uniqueness, check, referential, nullability, or comparable constraints belong in Reference.
* Policy or business rules supplied externally belong in Context even when they resemble database constraints.
* Patterns inferred from observed values belong in Interpretive unless the source establishes them as formal constraints.

Current design implication:

* A declared database constraint and an observed data regularity are epistemically different assertions.
* Relational profile design should avoid collapsing both into a generic `constraint` field without preserving their basis.

Deferred:

* Whether common constraint types warrant structured executable representations.
* How vendor-specific constraint mechanisms should be handled.
* Whether constraint expressions should be preserved verbatim, normalized, or both.

### Table Relationships

Current guidance:

* Relationships explicitly established by foreign keys or comparable source-native relational declarations belong in Reference.
* Externally supplied explanations of the meaning of those relationships belong in Context.
* Relationships inferred through analysis, naming patterns, value overlap, or domain interpretation belong in Interpretive.
* Structural database relationships should not automatically be treated as complete semantic descriptions of how entities relate in the domain.

Current design implication:

* Relational sources make the distinction between **structural relationship** and **semantic relationship** especially important.
* A foreign key can establish that one column references another without establishing the full business meaning of that relationship.

Deferred:

* Whether relational relationships should use profile-specific structures, the base `relationships` mechanism, or both.
* Cardinality representation.
* Join semantics beyond declared source structure.

### Database and Schema Context

Current guidance:

* Database-native catalog, schema, namespace, table, or view identity belongs in Reference when mechanically recoverable.
* Organizational interpretation of what a database or schema represents belongs in Context.
* Analytical grouping of tables into conceptual domains or inferred entities belongs in Interpretive.

Open question:

* Which levels of database or schema hierarchy are required for reliable local identity and cross-tier association?

## Cross-Tier Relational Association

Current guidance:

* Relational metadata will require stable association among source-native relational objects and assertions made about them in Context or Interpretive tiers.
* Existing Structured Data field-association principles should be reused where possible.
* Context and Interpretive metadata should point back to Reference-established relational identity rather than silently redefining tables, columns, keys, or relationships.
* Synthetic identifiers should be introduced only when source-native identities or locators are insufficient.

Open question:

* Whether the existing `source_fields` locator pattern can be reused cleanly for relational objects or whether tables, constraints, keys, and relationships require a broader relational locator model.

Deferred:

* Exact executable locator shapes.
* Validator enforcement that relational locators resolve to existing Reference objects.
* Cross-record or cross-version relational identity.

## Boundaries with Other Profiles

Current guidance:

* Prefer `structured-data` when the meaningful source structure can be represented adequately through fields, records, and comparable schema-level organization without requiring explicit relational semantics.
* Prefer `structured-data-relational` when keys, constraints, table or view identity, or relationships among structured objects are materially necessary to represent or interpret the source.
* Prefer `document` when the primary source meaning is narrative or document-oriented rather than record/schema-oriented.
* Prefer `media` when meaning is primarily visual, audio, spatial, or temporal.
* Composite sources may contain relational structured-data components, but composition and relational structure address different architectural concerns.

Boundary case:

* A CSV produced from a SQL query does not become relational solely because its upstream lineage involved a relational database.
* The exported CSV may be represented using `structured-data` while its relational origin is represented through provenance, lineage, or Context.
* A source that preserves table identities, keys, constraints, and relationships creates stronger pressure for `structured-data-relational`.

## Candidate Testbeds

Current guidance:

* Relational evaluation should use more than one source so that a single database product or schema design does not define the contract.
* Testbeds should be bounded enough to inspect manually while containing enough relational structure to exercise keys, constraints, relationships, and schema context.

### `structured-relational-001`

Candidate source:

* **MySQL Sakila**

Proposed use:

* Initial relational specimen.
* Test tables, columns, declared types, nullability, primary and foreign keys, constraints, views, and schema relationships.
* Distinguish reusable relational semantics from MySQL-specific database features.

### `structured-relational-002`

Candidate source:

* **Microsoft AdventureWorksLT**

Proposed use:

* Cross-source portability challenge from a different database ecosystem.
* Determine whether candidate structures derived from `structured-relational-001` remain reusable rather than reflecting one database implementation.

Later boundary case:

* A query result exported from a relational database may be used to test the distinction between relational source structure and relational source lineage.

## Proposed Evaluation Sequence

Current guidance:

1. Preserve the existing Structured Data contract as a source of prior decisions where applicable.
2. Inspect `structured-relational-001` without defining new relational fields in advance.
3. Record relational structure that the current MetaRCI contracts cannot represent cleanly.
4. Classify each candidate assertion by Reference, Context, or Interpretive basis.
5. Distinguish reusable relational semantics from database-engine-specific features.
6. Test recurring candidate structures against `structured-relational-002`.
7. Promote only reusable structural requirements into the relational profile contract.
8. Add validator behavior only after profile semantics have been supported by evidence.
9. Defer deeply technical DBMS properties unless retrieval, provenance, governance, interoperability, or downstream use demonstrates a need.

## Relevant Design Questions

Open question:

* What is the correct record boundary for relational sources?
* Should tables be modeled as nested structures or independently addressable source components?
* How should database, schema, table, view, column, key, and constraint identities relate?
* Which relational structures belong in Reference as first-class objects?
* Can existing Structured Data field locators support relational association without modification?
* How should composite primary and foreign keys be represented?
* How should declared cardinality or relationship constraints be represented, if at all?
* Should source-native table relationships use the base `relationships` structure or relational-specific structures?
* How should views differ from stored tables?
* How should query results be classified when relational lineage is known but relational structure is no longer present?
* Which vendor-specific database properties should remain outside the generic profile?
* Which relational properties materially support retrieval, provenance, governance, or downstream knowledge modeling?

Deferred:

* Profile inheritance between `structured-data` and `structured-data-relational`.
* Vendor-specific database ontology.
* Stored procedures, triggers, functions, execution plans, indexes, and performance-tuning metadata unless later evidence establishes a MetaRCI use case.
* Full SQL-language modeling.
* Automatic entity-relationship or ontology generation from database schema.
* Graph-specific transformations.
* Referential-integrity enforcement beyond the validator's approved structural scope.

## Example Applications

Current guidance:

* Relational database schemas.
* Bounded collections of related database tables.
* Database views where relational structure remains explicit.
* Database extracts that preserve sufficient schema and relationship information for relational interpretation.

Boundary cases:

* Flat query exports may remain `structured-data`.
* Vendor dumps or backup formats should not determine profile membership merely by file format.

## Initial Checkpoint

Current contract:

* `structured-data-relational` exists as a draft structural profile.
* The profile currently contains no relational custom fields or tier overrides.
* No relational testbed evidence has yet been promoted into executable contract.

Current guidance:

* Begin with source inspection rather than candidate-field implementation.
* Reuse mature Structured Data decisions only where their epistemic or structural logic remains applicable.
* Introduce relational-specific structure only where repeated testbed evidence demonstrates a need.
* Keep relational semantics portable and avoid coupling the profile to a particular SQL dialect or database engine.

