# Testbed Report

## Header

* Testbed name: media-semantics-001
* Profile: media
* Date: 2026-08-07
* Author: GitHub Copilot
* Source set summary: media-source-001 (JPEG still image) and media-source-002 (MP4 segmentable video)

## Questions Covered

* How should captions, transcripts, and accessibility descriptions be represented structurally?
* How should model-generated descriptions record provenance and review state?
* How should region/frame/time-segment references be represented?

## Baseline Representation

* Record path: examples/media-source-001-record.yaml and examples/media-source-002-record.yaml
* Why baseline reflects current contract: both sources are represented with inherited base fields only.
* Validator result: pass for both records.

## Variant A

* Goal: represent description provenance and segment semantics using only current contract fields.
* Representation:
  * media-source-001: descriptive provenance carried in interpretive notes and relationship pointers.
  * media-source-002: transcript and segment index represented through related sources and relationship notes.
* Validator result:
  * examples/media-source-001-variant-a.yaml: pass
  * examples/media-source-002-variant-a.yaml: pass
* Strengths:
  * fully executable under current media profile contract.
  * preserves compatibility while capturing essential interpretation context.
* Weaknesses:
  * generated description provenance and segments remain narrative, not strongly structured.

## Variant B (optional)

* Goal: evaluate explicit structured media metadata fields.
* Representation:
  * media-source-001 adds interpretive.generated_descriptions.
  * media-source-002 adds interpretive.segment_references.
* Validator result:
  * examples/media-source-001-variant-b.yaml: fail
    * Unknown fields in interpretive tier: generated_descriptions
  * examples/media-source-002-variant-b.yaml: fail
    * Unknown fields in interpretive tier: segment_references
* Strengths:
  * explicit and queryable structures for provenance and segmentation.
* Weaknesses:
  * candidate fields are not in the current media profile contract.

## Evidence Summary by Question

For question: captions and transcript representation

* Observed ambiguity: transcript and caption information can be represented, but only as untyped notes and relationships.
* Tier-placement impact: context and interpretive tiers can carry references, but not structured transcript semantics.
* Reusability across sources: demonstrated across image and video sources.
* Extension-only viability: viable short-term, less interoperable long-term.
* Candidate closure outcome: Proposed change

For question: generated description provenance and review state

* Observed ambiguity: provenance metadata is narrative rather than machine-checkable.
* Tier-placement impact: interpretive tier appears stable for generated description structures.
* Reusability across sources: yes, both still images and video can require generated description provenance.
* Extension-only viability: possible, but likely shape drift across implementations.
* Candidate closure outcome: Proposed change

For question: region/frame/time-segment representation

* Observed ambiguity: segment semantics currently depend on free-text notes.
* Tier-placement impact: interpretive tier candidate structure appears appropriate.
* Reusability across sources: demonstrated in segmentable video source; image region case remains to be tested.
* Extension-only viability: viable but weak for tooling interoperability.
* Candidate closure outcome: Proposed change

## Proposed Change Candidate (if any)

* Candidate field or rule:
  * interpretive.generated_descriptions (list<object>)
  * interpretive.segment_references (list<object>)
* Profile location: profiles/media.yaml custom_fields.interpretive
* Why current contract is insufficient: cannot represent provenance or segment structures in a consistent machine-checkable way.
* Why extension-only is insufficient: extension-only modeling risks incompatible annotation shapes across implementations.
* Required implementation bundle:
  * profile YAML update
  * example record update
  * tests update
  * docs update

## Final Recommendation

* Keep open / close as guidance / propose contract change / defer:
  * keep current boundary-first profile behavior for production use.
  * elevate generated_descriptions and segment_references candidates to Proposed change based on this two-source evidence packet.
* Required next evidence step:
  * add one image-region annotation source and verify whether segment_references should become a more general spatial or temporal reference model.
