# Media Profile

## Purpose

Current contract:

* The media profile exists as a structural profile named media.
* It extends the base schema at version 0.1.0 and is currently draft.

Current guidance:

* Use this profile for primarily visual, audio, audiovisual, or other non-textual source units.

## Structural Characteristics

Current guidance:

* Common concerns include technical source properties, rights context, descriptive interpretation, and relationships.

### Reference-Tier Media Properties

Current guidance:

* Media Reference metadata represents source-native or mechanically recoverable properties of the media object.
* Mechanical extractability alone does not require first-class representation; a property should also be reusable and structurally meaningful across implementations.
* Reference metadata should describe the technical structure of the media source without interpreting its semantic content.
* Properties derived from visual, auditory, or audiovisual analysis belong in Interpretive even when produced automatically by a model or analysis tool.

Current contract:

* The media profile defines `reference.visual_dimensions` as a conditional, nullable object.
* When `visual_dimensions` is present:

  * `width_pixels` is required, non-nullable, and integer.
  * `height_pixels` is required, non-nullable, and integer.

Current guidance:

* Pixel dimensions are sufficiently stable, reusable, and mechanically recoverable to warrant first-class Reference representation for raster visual media.
* Current testbed evidence supports consistent `width_pixels` and `height_pixels` extraction from JPEG, PNG, and TIFF sources.
* `visual_dimensions` should be used only when the source provides meaningful raster pixel dimensions.
* Extractor output may expose additional technical properties, but mechanical extractability alone does not justify promotion into the MetaRCI contract.

Current evidence:

* JPEG test source: 872 × 1024 pixels.
* PNG test source: 300 × 302 pixels.
* TIFF test source: 3072 × 1908 pixels.
* SVG test evidence does not map cleanly to raster pixel dimensions because SVG width and height are vector geometry attributes rather than necessarily pixel dimensions.

Deferred:

* SVG and other vector-native geometry, including width/height units, viewport, `viewBox`, and coordinate systems.
* Orientation and EXIF orientation handling.
* Resolution or density metadata such as DPI/PPI.
* Color space, bit depth, channel count, or similar technical properties.
* Format-specific encoding properties such as JPEG JFIF markers, PNG IHDR codes, and TIFF tag-level technical values.
* Codec and compression details.
* Video frame rate, duration, tracks, and stream structure.
* Audio-specific technical properties.
* Semantic visual properties such as objects, scenes, subjects, dominant colors, or OCR-derived content.

### Context-Tier Supplied Descriptions

Current guidance:

- Media Context metadata may include descriptive text supplied by an external source that situates, identifies, or explains the media object without being inferred from the media signal itself.
- Externally supplied descriptive text should remain distinguishable from machine-generated or analytically inferred descriptions, which belong in Interpretive.
- The source of a supplied description should be preserved explicitly so that the contextual assertion remains attributable.
- External descriptive metadata should be modeled by semantic role rather than by source-specific field names or catalog vocabularies.

Current decision:

- Externally supplied descriptive text is a reusable Context-tier concept for media.
- The media profile should represent this concept through `context.supplied_descriptions`.
- `supplied_descriptions` should support multiple entries because a media object may have more than one externally supplied description from different authoritative or contextual sources.
- Each entry should preserve both the descriptive text and the external source that supplied it.

Current evidence:

- `media-source-001` contains a mechanically recoverable embedded URI linking the JPEG to an external Library of Congress catalog record.
- The external LOC record supplies descriptive metadata that is not recoverable from the JPEG pixels themselves.
- The current base Context contract can preserve linkage and selected identifiers, but rich externally supplied descriptive text remains materially under-structured.
- This evidence demonstrates the need for a reusable Context structure without requiring LOC-specific field names or catalog semantics.

Proposed executable shape:

- `context.supplied_descriptions` as a conditional, nullable `list<object>`.
- Each item requires:
  - `text` as string, non-nullable.
  - `source_id` as string, non-nullable.
- `source_id` identifies the external source supporting the supplied description.
- The description entry does not redefine or replace the related-source relationship; it preserves attribution at the individual descriptive-assertion level.

Boundary guidance:

- Text explicitly embedded in the media source itself remains Reference when mechanically recoverable.
- Text supplied by an external catalog, archive, CMS, DAM, repository, curator, or equivalent source belongs in Context when used as an externally supplied description.
- Text generated from analysis of the image, audio, or video signal belongs in Interpretive, even when generated automatically by a model or tool.
- A source-specific field such as a catalog `summary`, `caption`, or `description` may map to `supplied_descriptions` when its semantic role is externally supplied descriptive text.
- Source-specific vocabulary should not be promoted into the media profile solely because one implementation exposes it.

Deferred:

- Description type or subtype, such as caption, accessibility description, catalog summary, or editorial note.
- Language metadata.
- Description author or contributor identity beyond the supporting source.
- Description creation or modification dates.
- Review or approval state.
- Rights or licensing attached specifically to a description.
- Structured subject headings or controlled descriptive terms.
- Richer provenance linking when multiple upstream records contribute to one description.

### Context-Tier Supplied Attributions

Current guidance:

- Media Context metadata may include creator or contributor attribution supplied by an external source rather than mechanically recovered from the media object itself.
- Externally supplied attribution should remain distinguishable from source-native attribution metadata, which belongs in Reference when mechanically recoverable.
- Attribution inferred from analysis of the media signal belongs in Interpretive.
- Attribution should be modeled by its reusable semantic function rather than by source-specific field names or descriptive standards.

Current decision:

- Externally supplied attribution is a reusable Context-tier concept for media.
- The media profile should represent this concept through `context.supplied_attributions`.
- `supplied_attributions` should support multiple entries because a media object may have multiple attributed persons or organizations and may receive attribution from multiple external sources.
- Each entry should preserve both the attributed name and the external source supplying the attribution.

Current evidence:

- The external Library of Congress record associated with `media-source-001` explicitly supplies creator attribution for Robert Cornelius.
- That attribution is supplied by the external descriptive record rather than recovered from the JPEG itself.
- The current base Context contract does not provide a semantically precise structure for preserving externally supplied media attribution.
- The Library of Congress example demonstrates the general attribution pattern but does not define the MetaRCI vocabulary or schema.
- Comparable attribution assertions may originate from archival catalogs, museum systems, digital asset management systems, content management systems, bibliographic metadata, repository records, or descriptive standards such as Dublin Core.

Proposed executable shape:

- `context.supplied_attributions` as a conditional, nullable `list<object>`.
- Each item requires:
  - `name` as string, non-nullable.
  - `source_id` as string, non-nullable.
- `name` preserves the attributed person, organization, or other named agent as supplied by the external source.
- `source_id` identifies the external source supporting the attribution.
- The attribution entry does not normalize the supplied name into a canonical identity or authority record.

Boundary guidance:

- Creator or contributor information explicitly embedded in the media source and mechanically recoverable belongs in Reference.
- Creator or contributor attribution supplied by an external catalog, repository, CMS, DAM, archive, museum system, metadata record, or equivalent source belongs in Context.
- Attribution inferred from visual, audio, audiovisual, or other signal analysis belongs in Interpretive.
- Source-specific fields such as `creator`, `contributor`, `artist`, `photographer`, or equivalent labels may map to `supplied_attributions` when their semantic role is attribution supplied by an external source.
- MetaRCI should not translate a generic source attribution into a more specific role unless that role is explicitly supplied by the supporting source.
- Validation of the attribution structure establishes contractual legality; it does not establish the truth or authority of the attribution itself.

Deferred:

- Attribution role or relationship type, such as photographer, artist, illustrator, director, performer, or contributor.
- Canonical or normalized agent identifiers.
- Authority-file links or controlled-name identifiers.
- Distinction between persons and organizations.
- Attribution dates or periods.
- Attribution certainty or qualification.
- Source-specific creator/contributor vocabularies.
- Reconciliation of conflicting attributions from multiple external sources.

### Context-Tier Supplied Terms

Current guidance:

- Media sources frequently arrive with limited or no contextual metadata beyond what can be recovered from the media object itself.
- The absence of externally supplied contextual terms is not, by itself, a metadata failure. It may accurately reflect the state in which the media source was acquired.
- When external descriptive terms are available, MetaRCI should preserve them without assuming that they belong to a controlled vocabulary, taxonomy, or formal classification system.
- Externally supplied terms should remain distinguishable from terms generated through analysis of the media signal.

Current decision:

- Externally supplied descriptive or classificatory terms are a reusable Context-tier concept for media.
- The media profile should represent this concept through `context.supplied_terms`.
- `supplied_terms` should support multiple entries because a media object may receive terms from multiple external sources.
- Each entry should preserve both the supplied term and the external source that supplied it.
- `supplied_terms` is conditional. A valid media record does not require externally supplied terms to exist.

Current evidence:

- The external Library of Congress record associated with `media-source-001` supplies subject and format headings describing and classifying the media object.
- These terms are supplied by the external descriptive record rather than mechanically recovered from the JPEG itself.
- Similar contextual terms may originate from archival catalogs, museum systems, digital asset management systems, content management systems, repository records, bibliographic metadata, manually curated keywords, tags, or controlled vocabularies.
- The Library of Congress example demonstrates the general externally supplied term pattern but does not define the MetaRCI vocabulary or schema.
- Media acquired outside curated repositories may contain little or no comparable contextual terminology.

Proposed executable shape:

- `context.supplied_terms` as a conditional, nullable `list<object>`.
- Each item requires:
  - `term` as string, non-nullable.
  - `source_id` as string, non-nullable.
- `term` preserves the descriptive or classificatory term supplied by the external source.
- `source_id` identifies the external source supporting the term.
- MetaRCI does not assume that individual terms are controlled, hierarchical, normalized, or mutually equivalent.

Boundary guidance:

- Terms explicitly embedded in the media source and mechanically recoverable remain Reference when represented as source-native metadata.
- Terms supplied by an external catalog, archive, CMS, DAM, repository, curator, metadata record, or equivalent source belong in Context.
- Labels, keywords, subjects, categories, or classifications generated from analysis of the media signal belong in Interpretive.
- Source-specific constructs such as subject headings, keywords, tags, categories, or format terms may map to `supplied_terms` when their semantic function is to provide externally supplied descriptive or classificatory terminology.
- A supplied term should be preserved as supplied rather than silently normalized into another vocabulary.
- The presence of no `supplied_terms` is valid and should not cause a media record to fail validation.

Sparse-Context guidance:

- Media records may legitimately contain substantially more Reference metadata than Context metadata.
- MetaRCI should not manufacture Context solely to make a media record appear descriptively complete.
- Where reliable external descriptive sources do not exist, Context fields may remain null or absent.
- Subsequent enrichment may add Context when externally grounded information becomes available.
- Machine-generated enrichment derived from the media signal remains Interpretive unless independently grounded in an external source.

Deferred:

- Vocabulary or scheme name.
- Vocabulary URI or authority identifier.
- Term identifiers or authority-file URIs.
- Distinction among subjects, keywords, tags, genres, forms, and categories.
- Hierarchical relationships among terms.
- Preferred versus alternate term forms.
- Language metadata.
- Term normalization or reconciliation across external vocabularies.
- Confidence or certainty.
- Conflict handling when external sources supply incompatible terminology.

### Cross-Source Context Validation

Current guidance:

- Media Context structures should be validated against materially different external metadata ecosystems before being treated as stable profile concepts.
- A single authoritative catalog may demonstrate a useful pattern, but it should not define the media profile vocabulary by itself.
- Cross-source testing should determine whether existing Context structures remain semantically usable without source-specific customization.

Current decision:

- The current media Context structures should be tested against an external metadata source that differs materially from the Library of Congress catalog model.
- Wikimedia Commons is suitable as a second exemplar because its media metadata may originate from community-contributed descriptions, source inheritance, embedded metadata, structured statements, licensing data, categories, and external institutional records.
- The goal of this test is validation of portability, not expansion of the schema.

Current structures under test:

- `context.supplied_descriptions`
- `context.supplied_attributions`
- `context.supplied_terms`
- Existing base Context fields where there is a clear semantic fit.

Evaluation rule:

- Existing fields should be used only when their semantic role fits the external assertion cleanly.
- Source-specific Wikimedia Commons labels or metadata conventions should not be promoted into the MetaRCI media contract solely because they exist.
- Metadata that does not fit the current contract should be reported as contract pressure rather than forced into weak mappings.
- The preferred outcome is that no schema change is required.
- New media-specific Context fields should be considered only when a reusable semantic gap is demonstrated across independent source ecosystems.

Boundary guidance:

- Metadata mechanically recoverable from the media file remains Reference.
- Metadata supplied by the Wikimedia Commons page, structured record, uploader, linked source record, or other external descriptive source is Context-capable when explicitly asserted.
- Metadata inferred from the media signal remains Interpretive.
- The same logical property may appear in different RCI tiers depending on its evidentiary basis.

Success criterion:

- The current media Context contract is considered stronger if a Wikimedia Commons source can be represented cleanly using the existing structures without LOC-specific assumptions or new custom fields.

Cross-source result:

- Wikimedia Commons validation using `media-source-005` (`Exemplo.svg`) confirmed that the current media Context structures are portable beyond the initial Library of Congress exemplar.
- Commons `ImageDescription`, `Artist`, and category metadata map naturally to `supplied_descriptions`, `supplied_attributions`, and `supplied_terms` respectively.
- Existing base Context structures remain suitable for external identifiers and related-source linkage.
- No additional media-specific Context field was required by this second source ecosystem.
- Structured rights and licensing, attribution-role granularity, and term typing remain legitimate contract-pressure areas but are deferred pending broader evidence and consideration of whether they belong at the base-model rather than media-profile level.

### Interpretive-Tier Generated Descriptions

Current guidance:

- Descriptive text produced by analyzing the media signal is Interpretive metadata.
- A generated description must remain distinguishable from text mechanically recovered from the source and from description supplied by an external source.
- The epistemic basis of the description determines its tier, not the fact that all three may contain similar natural-language text.

Current decision:

- The media profile supports `interpretive.generated_descriptions` for descriptive text produced by a model, algorithm, analytical workflow, or other interpretive process.
- Multiple generated descriptions may be retained when different generators, workflows, or interpretations are relevant.
- Each generated description must identify both the descriptive assertion and the generator responsible for producing it.

Current shape:

```yaml
generated_descriptions:
  type: list
  item_type: object
  requirement: conditional
  nullable: true
  item_properties:
    text:
      type: string
      requirement: required
      nullable: false
    generator:
      type: string
      requirement: required
      nullable: false
```

Field guidance:

- `text` contains the generated descriptive assertion.
- `generator` identifies the model, tool, analytical process, or other mechanism responsible for producing the description.
- `generator` records provenance of the interpretation; it does not establish the correctness, authority, or quality of the generated text.

Tier boundary:

- Text explicitly present within the media source and mechanically recoverable from it belongs in Reference when represented as metadata.
- Descriptive text supplied by an external catalog, repository, CMS, DAM, curator, or comparable source belongs in Context.
- Descriptive text produced through analysis of the media signal belongs in Interpretive.

For example:

- embedded source caption -> Reference
- Wikimedia Commons or Library of Congress supplied description -> Context
- vision-model-generated image description -> Interpretive

Validation boundary:

- Structural validation can confirm that a generated description contains the required `text` and `generator` values with the expected types.
- Validation does not establish whether the generated description is accurate, useful, unbiased, sufficiently specific, or faithful to the media source.
- Evaluation of generated descriptive content remains distinct from schema validation.

Deferred:

- generation timestamp
- model or generator version
- prompts or generation parameters
- confidence scores
- review status
- reviewer identity
- approval workflows
- language
- description type
- uncertainty representation
- relationships between multiple generated descriptions

### Interpretive-Tier Generated Terms

Current guidance:

- Discrete descriptive or classificatory terms produced through analysis of the media signal are Interpretive metadata.
- Generated terms must remain distinguishable from terms mechanically recovered from the source and from terms supplied by an external source.
- The epistemic basis of the term determines its tier, not the term value itself.

Current decision:

- The media profile supports `interpretive.generated_terms` for discrete terms produced by a model, algorithm, analytical workflow, or other interpretive process.
- Multiple generated terms may be retained when they represent separate analytical assertions about the media source.
- Each generated term must identify both the term itself and the generator responsible for producing it.

Current shape:

```yaml
generated_terms:
  type: list
  item_type: object
  requirement: conditional
  nullable: true
  item_properties:
    term:
      type: string
      requirement: required
      nullable: false
    generator:
      type: string
      requirement: required
      nullable: false
```

Field guidance:

- `term` contains the generated descriptive or classificatory assertion.
- `generator` identifies the model, tool, analytical process, or other mechanism responsible for producing the term.
- `generator` records provenance of the interpretation; it does not establish the correctness, authority, or usefulness of the generated term.
- Terms are preserved as produced unless a separate normalization process is explicitly represented elsewhere.

Tier boundary:

- A term explicitly embedded in the media source and mechanically recoverable from it belongs in Reference when represented as metadata.
- A term supplied by an external catalog, repository, CMS, DAM, curator, or comparable source belongs in Context.
- A term produced through analysis of the media signal belongs in Interpretive.

For example:

- embedded source keyword -> Reference
- Wikimedia Commons category or Library of Congress subject term -> Context
- vision-model-generated label such as `portrait` -> Interpretive

Relationship to generated descriptions:

- `generated_descriptions` represents generated natural-language descriptive text.
- `generated_terms` represents discrete generated labels, tags, concepts, or classificatory assertions.
- A system may produce either or both.
- A generated description should not be mechanically split into generated terms unless a separate analytical process actually performs that derivation.

Validation boundary:

- Structural validation can confirm that a generated term contains the required `term` and `generator` values with the expected types.
- Validation does not establish whether the generated term is accurate, relevant, sufficiently specific, normalized, or appropriate for retrieval.
- Evaluation of generated terms remains distinct from schema validation.

Deferred:

- confidence scores
- controlled vocabularies or schemes
- canonical term identifiers
- hierarchy
- term type or subtype
- language
- generation timestamp
- model or generator version
- review status
- reviewer identity
- normalization provenance
- deduplication or reconciliation across generators



## Profile Emphasis

Current contract:

* The current YAML declares no profile-specific overrides.
* The media profile currently defines `reference.visual_dimensions` as its first profile-specific custom field.
* Other media behavior remains inherited from the base schema unless explicitly declared by the profile.

Current guidance:

* Keep one initial media profile for image/audio/video unless structural divergence is demonstrated.

## Rationale for Current Fields

Current contract:

* The profile currently adds one media-specific Reference structure: `reference.visual_dimensions`.
* The field is conditional, so media records without meaningful raster pixel dimensions may continue to validate using inherited base fields.
* Current testbed evidence demonstrates the field across JPEG, PNG, and TIFF raster sources.

Current guidance:

* Boundary-first design avoids premature commitment to one media annotation model.
* The image Reference extraction helper is evidence infrastructure rather than schema authority; extracted technical properties are not automatically MetaRCI fields.

## Relevant Design Questions

Open question:

* How should captions, transcripts, and accessibility descriptions be represented structurally?
* How should model-generated descriptions record provenance and review state?
* How should region/frame/time-segment references be represented?
* Which additional mechanically recoverable media properties are reusable and structurally significant enough for first-class Reference representation?
* Which vector-native geometry properties, if any, should receive first-class Reference representation in a future revision?
* How to represent machine-generated and human-curated descriptions without ambiguity.
* Whether to encode region/time segmentation in profile fields or extensions.

## Current Decisions Supported by YAML

Current contract:

* Status is draft.
* No profile-specific override behavior is declared.
* `reference.visual_dimensions` is declared as a conditional, nullable object.
* `visual_dimensions.width_pixels` is required, non-nullable, and integer when the object is present.
* `visual_dimensions.height_pixels` is required, non-nullable, and integer when the object is present.

Current evidence:

* JPEG, PNG, and TIFF testbed sources validate the raster pixel-dimension model.
* Regression tests enforce required width and height properties and integer value types.
* The current validator suite passes 65 tests.

Current guidance:

* Add additional media custom fields only after a reusable cross-source pattern is demonstrated.
* Do not treat all properties emitted by the media Reference extraction helper as profile-contract fields.

## Boundaries with Other Profiles

Current guidance:

* Prefer document when text structure is primary even if embedded media exists.
* Prefer structured-data when schema/table structure is primary.
* Prefer composite when the described source unit is a bundle containing multiple meaningful members.

## Example Applications

Current guidance:

* Photographs, diagrams, maps, recordings, videos, and scanned visual artifacts.

Deferred:

* Splitting media into separate image/audio/video structural profiles.
* Normalized vector geometry for SVG and other vector-native formats.

## Closure Candidate Pass (No Implementation)

Current guidance:

* Close as guidance now: keep a single media structural profile in 0.1 while image/audio/video differences remain mostly technical rather than structurally distinct.
* Close as guidance now: media records should continue to use inherited base fields and relationship metadata except where reusable media-specific structures have been demonstrated and contractized.
* Close as guidance now: tier placement should default to Reference for source-native or mechanically recoverable technical properties, Context for externally supplied or curated situating assertions, and Interpretive for inferred or analytical assertions.
* Close as current contract: mechanically recoverable raster pixel dimensions are sufficiently reusable and structurally meaningful for first-class Reference representation through `reference.visual_dimensions`.
* Close as guidance now: JPEG, PNG, and TIFF provide sufficient cross-format evidence for the raster `visual_dimensions` contract in v0.1.
* Defer: SVG and other vector-native geometry should not be coerced into `width_pixels` and `height_pixels`; vector geometry remains a future enhancement.

Open question:

* Keep open: standardized representation of captions, transcripts, accessibility descriptions, and model-generated description provenance in profile YAML.
* Keep open: standardized region/frame/time-segment representation in profile YAML.
* Keep open: which additional technical media properties warrant first-class Reference representation beyond raster pixel dimensions.

## Recommended Code Change (Proposal Only)

Proposed change:

* Introduce one optional media custom field in profile YAML to capture reusable generated-description provenance, for example:

  * `interpretive.generated_descriptions` as `list<object>` with minimal child properties such as generator, generated_at, review_status, and text.

Current guidance:

* Do not implement `interpretive.generated_descriptions` yet.
* Implement generated-description provenance only after sufficient evidence demonstrates a reusable structure that cannot be represented clearly with current base fields and extensions.
* Defer confidence scoring until its semantics and source are sufficiently defined.
* Defer vector-native geometry representation until a reusable SVG/vector model is established.

If `interpretive.generated_descriptions` is later approved, its implementation bundle should include:

* profile YAML update in `profiles/media.yaml`;
* example update in `examples/media-record.yaml`;
* positive/negative regression tests in `tests/test_validate.py` for nested generated-description validation;
* documentation updates in this file and `documentation/profile-question-matrix.md`.
