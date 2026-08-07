# Testbed Source Intake Plan

## Purpose

This file defines the minimum source material you should provide for each profile so testbed reports can produce closure-quality evidence.

Current guidance:

* Provide two independent source sets per profile when possible.
* Keep source material neutral, non-proprietary, and reproducible.

## Required Intake Fields Per Source Set

For each source set, record:

* source set id
* profile target
* source description
* source location or acquisition note
* license or usage status
* normalization performed
* expected question cluster coverage
* known limitations

## Profile Source Requirements

### Document

Minimum source sets:

* one narrative document with limited structure
* one document with embedded media or richer internal subdivision

Coverage goals:

* subdivision representation
* version and edition relationship behavior
* boundary between document and media/composite representation

### Structured Data

Minimum source sets:

* one neutral CSV-like tabular source
* one table-like export with units, value domains, or missing-value conventions

Coverage goals:

* variable-definition representation
* units and value-domain modeling
* inferred versus declared schema distinction

### Media

Minimum source sets:

* one still-image or diagram source set
* one audio or video source set

Coverage goals:

* captions or transcripts representation
* generated-description provenance and review metadata
* segment or region reference representation

### Composite

Minimum source sets:

* one package with complete known membership
* one package with partial or unknown expected membership

Coverage goals:

* expected versus present membership
* member roles and ordering
* completeness semantics
* mixed-profile member handling

## Source Intake Tracker

| Intake id | Profile | Source set summary | Ready for baseline | Ready for variants | Notes |
|---|---|---|---|---|---|
| doc-source-001 | document | TheYellowWallpaper.md | yes | no | |
| doc-source-002 | document | NIST AI Risk Management Framework 1.0.pdf | yes | no | |
| data-source-001 | structured-data | neutral tabular baseline; see documentation/testbed-sources/structured-data-sources.md | no | no | |
| data-source-002 | structured-data | units and missing-value conventions dataset; see documentation/testbed-sources/structured-data-sources.md | no | no | |
| media-source-001 | media | image or diagram collection baseline; see documentation/testbed-sources/media-sources.md | no | no | |
| media-source-002 | media | audio or video segmentable source; see documentation/testbed-sources/media-sources.md | no | no | |
| comp-source-001 | composite | complete-membership package; see documentation/testbed-sources/composite-sources.md | no | no | |
| comp-source-002 | composite | partial or unknown-membership package; see documentation/testbed-sources/composite-sources.md | no | no | |

## Readiness Gate

A profile is source-ready for closure work when:

* at least one baseline source set is marked ready for baseline;
* at least one second independent source set is marked ready for variants;
* the source sets cover at least one open-question cluster listed in the profile documentation.

## Next Action Template

When a source set is ready, immediately create:

* one baseline record draft;
* one variant record draft;
* one testbed report draft in documentation/testbed-reports.
