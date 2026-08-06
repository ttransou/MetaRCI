# MetaRCI Tier Notes

MetaRCI organizes metadata into three tiers according to how the metadata is obtained, curated, and used.

## Tier 1: Reference

Reference metadata records information that can be extracted or generated automatically from the source, file, or ingestion process with minimal human curation.

Examples include:

* filename;
* file format;
* checksum;
* file size;
* page count;
* stated title;
* stated author;
* creation or review dates;
* parser information;
* ingestion timestamp;
* extraction status.

Reference fields may remain `null` when a value is unavailable, inapplicable, or cannot be extracted reliably.

**Reference records the source.**

## Tier 2: Context

Context metadata situates the source within its broader corpus, domain, history, organization, relationships, or handling requirements.

These values may require:

* human curation;
* subject-matter expertise;
* an external catalog;
* a controlled vocabulary;
* a system of record;
* or organizational review.

Examples include:

* preferred and alternate titles;
* domain classifications;
* related sources;
* source lineage;
* organizational context;
* jurisdiction;
* intended audience;
* sensitivity;
* external identifiers.

**Context situates the source.**

## Tier 3: Interpretive

Interpretive metadata describes how a source or its contents are understood within a specific corpus, analytical model, or use case.

Fields in this tier are expected to vary significantly by domain.

Examples include:

* concepts;
* themes;
* analytical categories;
* entity roles;
* semantic relationships;
* corpus roles;
* interpretive notes;
* domain-specific extensions.

Interpretive metadata should be documented, attributable, and governed through appropriate annotation guidance or controlled vocabularies.

**Interpretation models the source.**

## Field Placement

A proposed field should generally be assigned according to the following questions:

1. Can the value be extracted or generated reliably from the source or ingestion process?
   Use the Reference Tier.

2. Does the value require external knowledge or curation to situate the source?
   Use the Context Tier.

3. Does the value express corpus-specific meaning, analysis, or relationships?
   Use the Interpretive Tier.

Fields should be included only when they materially support the implementation’s corpus, use case, retrieval behavior, governance, or evaluation needs.

