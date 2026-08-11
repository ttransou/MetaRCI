# Composite Testbed Source Pack

## Goal

Prepare composite source sets that test whole/part structure, independently meaningful components, heterogeneous structural treatment, and parent/component metadata scope.

The testbeds should challenge the working Composite definition:

> **Composite represents the whole/part structure of a logical source whose independently meaningful components may use different MetaRCI structural profiles while remaining components of a single coherent parent source.**

The purpose of these source sets is to determine whether recurring composition semantics require a dedicated Composite profile, a separate composition mechanism, or another MetaRCI architectural pattern.

## Source Set A: Heterogeneous Presentation Baseline

* intake id: comp-source-001
* profile target: composite
* candidate source type: PPTX
* purpose: establish baseline composition behavior using one coherent presentation containing multiple independently meaningful component structures

Suggested source:

* a bounded `.pptx` presentation containing a deliberate mixture of:

  * slide text;
  * speaker notes;
  * images;
  * at least one table;
  * at least one chart with underlying data;
  * and audiovisual media if practical

Suggested files:

* comp-source-001/source.pptx
* comp-source-001/README.md

Required characteristics:

* multiple ordered slides
* meaningful slide-level text
* at least one independently meaningful Media component
* at least one Structured Data-like component
* explicit source-native ordering
* recoverable parent/component relationships
* enough internal variation to distinguish logical composition from incidental embedded content

Question coverage:

* parent source identity
* component identity
* source-native ordering
* containment
* component roles
* heterogeneous structural treatment
* Reference-level composition semantics
* parent-level versus component-level metadata
* threshold for independently meaningful component representation

## Source Set B: Presentation Portability Challenge

* intake id: comp-source-002
* profile target: composite
* candidate source type: ODP
* purpose: test whether composition semantics identified in the PPTX baseline remain reusable in a different presentation and packaging ecosystem

Suggested source:

* a bounded `.odp` presentation containing component types materially comparable to Source Set A

Suggested files:

* comp-source-002/source.odp
* comp-source-002/README.md

Required characteristics:

* multiple ordered slides
* meaningful text content
* embedded media or graphics
* table or chart content where practical
* recoverable parent/component relationships
* enough structural similarity to PPTX for comparison
* enough implementation difference to expose format-specific assumptions

Question coverage:

* portability of component identity
* portability of ordering and containment semantics
* reusable versus format-specific composition metadata
* parent/component metadata scope
* whether candidate Composite structures reflect presentation logic rather than Office Open XML packaging

## Source Set C: Publication Composition Challenge

* intake id: comp-source-003
* profile target: composite
* candidate source type: EPUB
* purpose: test whether composition semantics remain reusable outside presentation formats

Suggested source:

* a bounded `.epub` publication containing multiple content documents and supporting media

Suggested files:

* comp-source-003/source.epub
* comp-source-003/README.md

Required characteristics:

* publication-level parent identity
* multiple content documents
* explicit resource membership
* explicit reading order
* supporting images or other media
* enough internal structure to distinguish source-native composition from low-level package artifacts

Question coverage:

* parent/member identity outside presentation formats
* manifest membership
* ordered reading sequence
* component role
* parent/component metadata scope
* heterogeneous component handling
* distinction between meaningful logical components and package implementation resources
* portability of candidate composition semantics across source families

## Composition Boundary

The testbed set should not treat internal packaging complexity as sufficient evidence of Composite structure.

A source should create Composite pressure only when its internal components are independently meaningful to retrieval, provenance, governance, interpretation, or structural representation.

Examples of potentially meaningful components include:

* slide text;
* speaker notes;
* embedded images;
* embedded video;
* tables;
* chart data;
* publication content documents;
* ordered publication resources.

Examples of internal resources that should not automatically receive independent MetaRCI treatment include:

* theme files;
* package relationship files;
* internal reconstruction metadata;
* format-specific implementation artifacts with no independent knowledge-system role.

## Intake Completion Checklist

* source location recorded
* license/usage status recorded
* source format/version context recorded
* retained source artifact recorded
* normalization or extraction steps recorded
* meaningful component types identified
* package-only implementation artifacts distinguished from candidate logical components
* known limitations recorded
* baseline readiness set in `documentation/testbed-source-intake.md`
