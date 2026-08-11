# structured-relational-001

## Source

* Source: MySQL Sakila Sample Database
* Source URL: https://dev.mysql.com/doc/sakila/en/
    - https://dev.mysql.com/doc/index-other.html
* Profile target: `structured-data-relational`
* Intake ID: `structured-relational-001`

## Purpose

This source is used as the initial MetaRCI relational structured-data testbed.

The testbed is intended to evaluate how source-declared relational structure should be represented across the Reference, Context, and Interpretive tiers without assuming relational profile fields in advance.

Initial areas of interest include:

* database and schema structure;
* tables and views;
* columns and declared data types;
* nullability;
* primary keys;
* foreign keys;
* declared constraints;
* and relationships among relational objects.

## Retained Source Files

* `sakila-schema.sql`
* `sakila-data.sql`

Additional source artifacts may be retained later if they materially support the testbed.

## Source Handling

The retained files are preserved as source testbed artifacts.

Any normalization, extraction, transformation, or derived inspection output used during testing should be documented separately rather than silently altering the source files.

## Known Limitations

* Sakila is a sample database and should not be treated as representative of all relational database designs.
* MySQL-specific syntax and database features may appear in the schema.
* Vendor-specific features should not be promoted into the MetaRCI profile unless later evidence demonstrates reusable architectural value.
* Findings from this source should be challenged against an independent relational testbed before being treated as portable profile requirements.

## Testbed Role

`structured-relational-001` is the baseline relational specimen.

Its purpose is to expose candidate metadata pressure and architectural questions. It does not, by itself, define the `structured-data-relational` contract.

---

## Observation Notes

## Initial Schema Observations

First-pass inspection of `sakila-schema.sql` surfaced the following source-declared relational structures:

- explicit schema identity;
- independently named tables;
- declared column types;
- declared nullability;
- primary keys;
- named foreign-key constraints;
- explicit table/field references;
- foreign-key update/delete behavior;
- secondary indexes;
- defaults and automatic update behavior;
- vendor/version-specific schema features.

Initial reusable pressure appears strongest around:

- schema identity;
- table identity;
- column declarations;
- nullability;
- primary keys;
- foreign keys;
- relationship and constraint behavior.

Indexes, storage engine, character set, auto-increment behavior, spatial indexing, and version-conditional MySQL syntax remain observational only pending further evidence.

---

## Initial Relational Pressure

### Table Identity

Question:

Does a relational table require first-class Reference identity?

Test case:

`actor`

Existing Structured Data support:

- columns may be represented through `reference.source_fields`;
- field-level identity and metadata already have an established pattern.

Observed gap:

- there is no obvious first-class representation of the table that contains those fields;
- `actor` is explicitly source-declared and structurally meaningful.

Candidate pressure:

- relational sources may require a Reference-level representation for table identity.

No profile change is implied by this observation.

### Schema Versus Observed Data

The `actor` test case demonstrates a useful epistemic distinction between declared relational structure and observed record content.

The schema explicitly declares:

- `actor_id` as the primary key;
- column data types;
- nullability;
- automatic increment behavior;
- timestamp default/update behavior.

The data dump provides observed values for those fields but does not independently establish those declared constraints.

Observed properties such as uniqueness, completeness, recurring formats, or value ranges should therefore remain distinct from source-declared schema semantics.

### Foreign-Key Relationship Pressure

Test case:

`address.city_id` → `city.city_id`

Source declaration:

- constraint name: `fk_address_city`
- source table: `address`
- source field: `city_id`
- target table: `city`
- target field: `city_id`
- delete behavior: `RESTRICT`
- update behavior: `CASCADE`

Observed pressure:

- a relational relationship may have its own source-declared identity;
- the relationship connects specific source and target tables and fields;
- the relationship may include declared referential behavior in addition to the link itself.

Existing MetaRCI question:

- can the current base `relationships` structure preserve this information cleanly, or does relational data require a more specific Reference-level representation for declared foreign-key relationships?

No profile change is implied by this observation.