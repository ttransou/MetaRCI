# Composite Profile

## Purpose

Current contract:

* The composite profile exists as a structural profile named `composite`.
* It extends the base schema at version 0.1.0 and is currently draft.

Current guidance:

* Use this profile provisionally for logical source units composed of multiple independently meaningful components whose internal structures may differ.
* The current working definition is:

> **Composite represents the whole/part structure of a logical source whose independently meaningful components may use different MetaRCI structural profiles while remaining components of a single coherent parent source.**

* Composite should not be treated as another information structure in exactly the same sense as Document, Structured Data, or Media.
* Current evaluation should determine whether Composite remains a peer structural profile or is better represented as a separate composition mechanism.

## Structural Characteristics

Current guidance:

* Composite sources may involve:

  * parent/source identity;
  * component identity;
  * membership;
  * containment;
  * hierarchy;
  * ordering;
  * component roles;
  * relationships among components;
  * and metadata scope across parent and component records.
* Components may differ structurally while remaining parts of one coherent logical source.
* Internal file packaging should not be assumed to correspond directly to meaningful MetaRCI components.

Open question:

* What minimum structural signals distinguish meaningful logical composition from ordinary internal packaging or storage containment?

## Profile Emphasis

Current contract:

* The current YAML declares no overrides and no custom fields.
* Effective behavior currently remains the base schema with composite identity.

Current guidance:

* Emphasize whole/part identity and relationships without introducing a heavy package ontology.
* Preserve the structural identity of meaningful components rather than collapsing heterogeneous components into one generic Composite representation.
* Do not reproduce every internal resource of a package format merely because it is technically addressable.
* Candidate Composite structures should be introduced only when testbed evidence demonstrates recurring composition requirements that existing base relationships cannot represent cleanly.

## Profile Scope

Current guidance:

* Composite applies provisionally when one logical source contains multiple independently meaningful components whose identity, structure, or relationships matter to retrieval, provenance, governance, or interpretation.
* A source is not Composite merely because its physical file format is implemented as a container.
* Package resources that are technically distinct but not independently meaningful to the knowledge system do not necessarily require independent MetaRCI representation.
* Components may themselves be describable using Document, Structured Data, Media, or other applicable structural profiles.
* The parent source may retain its own MetaRCI identity and metadata independently of component records.

Examples of potentially meaningful components include:

* slide text;
* speaker notes;
* embedded images;
* embedded audio or video;
* tables;
* chart data;
* publication content documents;
* ordered resource sequences.

Examples of package resources that may not warrant independent MetaRCI treatment include:

* internal theme files;
* low-level relationship files;
* packaging metadata used only for file reconstruction;
* other implementation artifacts with no independent retrieval or interpretive role.

Open question:

* When does an internal component become independently meaningful enough to warrant its own MetaRCI representation?

## Composition Versus Packaging

Current guidance:

* Physical packaging and logical composition are distinct concerns.
* Formats such as PPTX, ODP, DOCX, XLSX, EPUB, and ZIP may internally contain multiple files or resources.
* Internal multiplicity alone does not establish Composite profile membership.
* The relevant question is whether those internal parts form meaningful components of one coherent logical source.
* Simple storage aggregation should not be treated as composition without evidence that the relationships among members are materially meaningful.

Boundary principle:

> A package is not Composite merely because it contains parts. Composition becomes relevant when those parts are meaningfully related as components of one logical source.

## Rationale for Current Fields

Current contract:

* The profile intentionally starts with no composite-specific field additions.
* Existing base fields such as `related_sources` and `relationships` can represent limited whole/part or member associations while composition semantics remain under evaluation.

Current guidance:

* This boundary-first approach allows Composite behavior to be explored without locking in one membership or containment model too early.
* Existing relationship mechanisms should be treated as provisional evidence tools rather than assumed to be the final composition contract.

## Epistemic Considerations

Current guidance:

* Composition should preserve the same Reference / Context / Interpretive distinction used elsewhere in MetaRCI.
* Parent-level and component-level metadata should remain distinguishable.
* The epistemic tier of a composition assertion depends on how that assertion is established.

### Reference-Level Composition

Current guidance:

* Mechanically recoverable parent/component structure may belong in Reference.
* Examples may include:

  * source-declared component identity;
  * package-declared ordering;
  * source-native containment;
  * mechanically recoverable parent-child relationships;
  * manifest membership;
  * and other structural relationships explicitly encoded by the source.
* A source-declared relationship should not be moved into Context merely because it concerns membership or containment.

Current design implication:

* The earlier assumption that a future member manifest would necessarily belong in Context should not be preserved without evidence.
* PPTX, ODP, EPUB, and comparable sources may demonstrate that some composition semantics are source-native Reference structure.

### Context-Level Composition

Current guidance:

* Externally supplied or curated assertions about component roles, publication context, ownership, intended use, or collection significance belong in Context.
* Context may also describe why particular components matter within an institutional, bibliographic, or operational setting.
* Parent-level context should not automatically be duplicated onto components without explicit inheritance guidance.

Open question:

* Which parent Context assertions, if any, may be inherited by components?

### Interpretive Composition

Current guidance:

* Analytical roles, inferred semantic connections, component significance, or relationships not established by the source belong in Interpretive.
* Interpretive relationships among components should remain explicit and attributable rather than being presented as mechanically established package structure.

Open question:

* How should source-declared structural relationships and analyst/model-derived semantic relationships coexist when they concern the same components?

## Parent and Component Metadata Scope

Current guidance:

* A Composite parent may have its own Reference, Context, and Interpretive metadata.
* Independently modeled components may also have their own R/C/I metadata.
* Metadata scope should remain explicit rather than assuming that parent metadata applies universally to children.
* Component-specific metadata may differ from or qualify parent-level metadata.

Open question:

* Which metadata belongs only to the parent?
* Which metadata belongs only to components?
* Which metadata may be inherited?
* Should inherited metadata be copied, referenced, or dynamically resolved?
* How should conflicts between parent-level and component-level assertions be represented?
* Should components always receive independent MetaRCI records, or only when their independent meaning warrants it?

Deferred:

* Formal inheritance behavior.
* Parent/component conflict-resolution semantics.
* Validator enforcement of inheritance or override rules.

## Relevant Design Questions

Open question:

* What makes a component independently meaningful?
* Does every meaningful component require its own MetaRCI record?
* Does the parent always receive its own R/C/I record?
* How should containment be represented?
* How should ordering be represented when order matters?
* How should component roles be represented?
* Can one component participate in more than one Composite source?
* Can Context be inherited from the parent?
* How should parent/component metadata conflicts be represented?
* Is composition strictly hierarchical, or must graph-like relationships be supported?
* How should extraction provenance distinguish an original embedded component from a component derived during parsing?
* Can and should a Composite source explicitly contain components validated under different structural profiles?
* Can existing base relationships represent composition adequately, or is a dedicated mechanism required?
* Should Composite remain a peer profile or become a composition layer/mechanism?

## Current Decisions Supported by YAML

Current contract:

* Status is draft.
* No composite-specific overrides are currently declared.
* No composite-specific custom fields are currently declared.

Current guidance:

* Existing `related_sources` and `relationships` may be used provisionally to represent parent/component or member relationships.
* This usage should not be interpreted as closure on the final composition model.

Proposed change:

* Introduce Composite custom fields only after recurring evidence demonstrates that existing base structures cannot represent required whole/part semantics clearly.

## Boundaries with Other Profiles

Current guidance:

* Do not use Composite solely because a source is packaged as a ZIP, folder, or other container.
* Prefer `document`, `structured-data`, or `media` when one primary information structure adequately represents the meaningful source unit.
* A DOCX containing incidental images does not necessarily require Composite treatment.
* An XLSX containing charts does not necessarily require Composite treatment.
* A presentation, publication, or comparable source may create Composite pressure when multiple internal components are independently meaningful and structurally heterogeneous.
* Composition and structural profile identity address different questions:

  * structural profiles describe the information structure of a source or component;
  * Composite describes how meaningful components participate in one coherent logical whole.

## Candidate Testbeds

Current guidance:

* Composite evaluation should use multiple source formats so that the architecture of one packaging standard does not define the model.
* Testbeds should expose meaningful component relationships rather than merely internal package complexity.

### Composite Testbed 1: PPTX

Proposed use:

* Initial composition specimen.
* Test one coherent presentation containing heterogeneous meaningful components such as:

  * slide text;
  * speaker notes;
  * embedded images;
  * tables;
  * charts with embedded structured data;
  * and embedded audiovisual media.
* Evaluate:

  * parent identity;
  * component identity;
  * ordering;
  * containment;
  * component roles;
  * heterogeneous structural treatment;
  * and parent/component metadata scope.

### Composite Testbed 2: ODP

Proposed use:

* Presentation-format portability challenge.
* Determine whether candidate composition semantics derived from PPTX remain valid in a different document/package ecosystem.
* Separate presentation-level composition concepts from Office Open XML implementation details.

### Composite Testbed 3: EPUB

Proposed use:

* Structurally different composition challenge.
* Test:

  * publication-level identity;
  * multiple content documents;
  * supporting media;
  * manifest membership;
  * reading order;
  * component roles;
  * and parent/component metadata scope.
* Determine whether composition semantics remain reusable outside presentation formats.

## Example Applications

Current guidance:

* Presentation files with independently meaningful text, notes, images, tables, chart data, audiovisual media, and other meaningful components where present.
* Digital publications composed of multiple ordered content and media resources.
* Other coherent logical sources whose meaningful components require different structural treatment.

Boundary cases:

* Case packages, archival groupings, regulatory bundles, folders, and arbitrary ZIP collections may still be useful future tests, but should not define the initial Composite model.
* These aggregation cases may expose related membership requirements while differing from the composition behavior of a single coherent source artifact.

## Proposed Evaluation Sequence

Current guidance:

1. Treat the existing Composite profile as draft scaffolding rather than a settled peer-profile design.
2. Preserve Document, Structured Data, and Media as established structural baselines.
3. Inspect a bounded PPTX specimen without adding composition fields in advance.
4. Identify internal components that are independently meaningful at the MetaRCI level.
5. Determine whether existing structural profiles can adequately describe those components.
6. Record parent/component, containment, ordering, role, and relationship requirements that existing MetaRCI structures cannot represent cleanly.
7. Test recurring requirements against an ODP specimen.
8. Challenge recurring concepts with an EPUB specimen.
9. Promote only format-independent composition semantics supported across testbeds.
10. Decide from the evidence whether Composite should remain a structural profile, become a separate composition mechanism, or use another MetaRCI architectural pattern.

## Deferred

* `context.member_manifest` or any equivalent predefined membership structure.
* Formal expected-versus-present membership semantics.
* Formal component completeness state.
* Parent-to-component Context inheritance.
* Conflict-resolution behavior.
* Cross-profile membership enforcement.
* Graph-native composition.
* Profile inheritance.
* Validator referential-integrity checks for component relationships.
* Any assumption that Composite must remain a peer structural profile.

## Initial Checkpoint

Current contract:

* The Composite profile remains draft.
* No Composite-specific custom fields or tier overrides are implemented.
* Existing base relationships may be used provisionally for exploratory representation.

Current guidance:

* The earlier aggregation-centered closure hypothesis is reopened.
* The working definition now centers on coherent logical sources with independently meaningful components.
* PPTX should serve as the initial composition testbed, followed by ODP and EPUB as portability challenges.
* Do not introduce a membership schema until testbed evidence demonstrates recurring composition requirements.

## PPTX Evidence Checkpoint 1: Presentation-Level Membership and Ordering

Observed in `comp-source-001.pptx`:

* `presentation.xml` declares five slide identifiers in sequence.
* Those identifiers resolve through presentation relationships to:

  * `slides/slide1.xml`
  * `slides/slide2.xml`
  * `slides/slide3.xml`
  * `slides/slide4.xml`
  * `slides/slide5.xml`
* Slide membership is therefore explicitly declared by the source.
* Slide order is likewise explicitly declared by the source rather than inferred during extraction.

Current interpretation:

* The presentation acts as the parent logical source.
* The five slides are candidate meaningful components of that parent.
* Parent/component membership and slide ordering are mechanically recoverable and therefore constitute Reference-level composition evidence.
* Other package relationships observed at the same level, including slide masters, notes masters, themes, view properties, and table styles, should not automatically be treated as independently meaningful MetaRCI components.

Current schema implication:

* No Composite-specific field is justified by this evidence alone.
* This checkpoint confirms that PPTX can expose source-native membership and ordering, but further component-level inspection is required before determining whether existing base relationships are sufficient.

### PPTX Evidence Checkpoint 2: Embedded Image as a Meaningful Child Component

Observed in `comp-source-001.pptx`:

* `slide2.xml.rels` declares an image relationship:

  * `rId1` → `../media/image-2-1.png`
* `slide2.xml` explicitly embeds that relationship through:

  * `<a:blip r:embed="rId1">`
* The PNG is represented as a picture object within the slide while the underlying image resource remains separately stored within the PPTX package.
* The same slide also contains ordinary textual content.

Current interpretation:

* The image is not merely present somewhere in the physical package.
* Slide 2 explicitly incorporates the image as part of its source-declared content structure.
* This supports treating the image as a candidate independently meaningful Media-profile component of the slide.
* The slide therefore demonstrates heterogeneous meaningful content within one parent component.

Current schema implication:

* No Composite-specific field is justified by this evidence alone.
* The evidence strengthens the need to distinguish meaningful child components from implementation-only package resources.
* Any future composition mechanism may need to preserve a source-declared relationship between a parent component and an embedded image describable under the Media profile.

### PPTX Evidence Checkpoint 3: Speaker Notes as a Distinct Meaningful Component

Observed in `comp-source-001.pptx`:

* `slide2.xml.rels` declares:

  * `rId3` → `../notesSlides/notesSlide2.xml`
* `notesSlide2.xml` contains substantive authored text distinct from the visible slide body.
* The note content is explicitly associated with slide 2 through the source package relationship.

Current interpretation:

* Speaker notes are not merely presentation-format infrastructure when they contain substantive authored content.
* Slide 2 and its notes are mechanically related by the source while remaining distinct content-bearing components.
* A single slide can therefore participate in composition with multiple meaningful child components of different structural character.
* The distinct content of the notes also supports keeping parent/component metadata scope explicit rather than assuming that all slide-level metadata applies identically to associated notes.

Current schema implication:

* No Composite-specific field is justified by this evidence alone.
* The evidence supports continued evaluation of parent/component identity, source-native relationships, heterogeneous component treatment, and component-specific metadata scope.

### PPTX Evidence Checkpoint 4: Chart with Embedded Structured Data

Observed in `comp-source-001.pptx`:

* `slide4.xml.rels` declares:

  * `rId1` → `/ppt/charts/chart1.xml`
* The chart is therefore a separately addressable component explicitly related to slide 4.
* `chart1.xml.rels` declares:

  * `rId1` → `../embeddings/Microsoft_Excel_Worksheet1.xlsx`
* The chart therefore explicitly depends on a separately stored embedded Excel workbook.

Source-native relationship chain:

```text
presentation
  → slide 4
    → chart1.xml
      → Microsoft_Excel_Worksheet1.xlsx
```

Current interpretation:

* The chart is not merely a rendered visual object or flattened image.
* It is a distinct source component with an explicit dependency on separately stored structured data.
* The embedded workbook is structurally different from the surrounding slide and chart while remaining part of one coherent presentation source.
* This provides direct evidence that Composite may need to preserve relationships among meaningful components that are describable under different structural profiles.
* The relationship chain is mechanically recoverable and therefore constitutes Reference-level composition evidence.

Current schema implication:

* No Composite-specific field is justified by this evidence alone.
* The evidence strengthens the need to represent source-native parent/component relationships across heterogeneous structural types.
* Further evaluation should determine whether existing base `relationships` mechanisms can preserve this chain clearly enough without introducing a dedicated composition structure.

Additional confirmation:

* The embedded workbook contains native spreadsheet structures including `workbook.xml`, `sheet1.xml`, and `table1.xml`.
* This confirms that the chart’s backing component is not merely an opaque embedded file; it contains independently addressable structured-data elements.
* The PPTX therefore preserves a mechanically recoverable relationship from presentation content to a Structured Data-like child component.

### PPTX Evidence Checkpoint 5: Embedded Audiovisual Media

Observed in `comp-source-001.pptx`:

* `slide5.xml.rels` declares two relationships to the same embedded MP4:

  * `rId1` → `../media/media-5-1.mp4` with relationship type `video`;
  * `rId2` → `../media/media-5-1.mp4` with an Office media relationship type.
* The same relationship file also declares:

  * `rId3` → `../media/image-5-3.png`;
  * `rId5` → `../notesSlides/notesSlide5.xml`.
* `media-5-1.mp4` is present as a nonzero embedded media resource within the PPTX package.

Source-native relationship pattern:

```text
presentation
  → slide 5
    → media-5-1.mp4
    → image-5-3.png
    → notesSlide5.xml
```

Current interpretation:

* Slide 5 contains a true source-declared audiovisual media component rather than only a simulated or textual representation of video.
* The embedded MP4 is explicitly related to the slide through both video-specific and Office media relationships.
* A separate image resource is also associated with the slide and is consistent with a poster or preview representation for the media object.
* The slide therefore demonstrates another heterogeneous composition case in which Document-like slide content, Media-profile content, supporting image content, and speaker notes coexist within one coherent parent component.
* The media relationships are mechanically recoverable and therefore constitute Reference-level composition evidence.

Current schema implication:

* No Composite-specific field is justified by this evidence alone.
* The evidence strengthens the recurring pattern that meaningful child components may use different structural profiles while remaining explicitly related to one parent source.
* Any future composition mechanism should preserve source-declared media relationships without collapsing the embedded audiovisual object, its associated image, and the containing slide into one undifferentiated representation.

### PPTX Evidence Checkpoint 6: Native Tabular Structure

Observed in `comp-source-001.pptx`:

* `slide3.xml` contains a native DrawingML table object identified by:

  * `<a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/table">`
  * `<a:tbl>`
* The table declares:

  * an explicit table grid through `<a:tblGrid>`;
  * columns through `<a:gridCol>`;
  * rows through `<a:tr>`;
  * cells through `<a:tc>`;
  * and cell text through `<a:t>`.
* The table is therefore represented as source-native tabular structure rather than as visually aligned text boxes.

Current interpretation:

* Slide 3 contains a meaningful Structured Data-like component directly within the slide content.
* Unlike the chart case, the table does not depend on a separately embedded workbook for its basic row, column, and cell structure.
* PPTX therefore demonstrates more than one mechanism for structured content:

  * native table structure embedded directly in a slide;
  * chart content linked to separately stored structured data.
* These differences are mechanically recoverable from the source and constitute Reference-level composition evidence.

Current schema implication:

* No Composite-specific field is justified by this evidence alone.
* The evidence strengthens the need for any future composition mechanism to preserve meaningful structural differences among child components rather than representing all structured content identically.

### PPTX YAML Baseline Checkpoint

Observed in `comp-source-001-baseline.yaml`:

* The record validates successfully against:

  * `schemas/metarci-base.yaml`;
  * `profiles/composite.yaml`.
* The current Composite contract can therefore represent `comp-source-001.pptx` as a valid parent source record.
* The baseline intentionally leaves `context.related_sources` and `interpretive.relationships` empty rather than using those fields to encode mechanically recoverable PPTX composition relationships.

Current interpretation:

* Validation success demonstrates structural conformance of the parent record.
* Validation success does not demonstrate that the current contract can adequately represent source-declared slide membership, ordering, containment, or heterogeneous child relationships.
* Existing Context- and Interpretive-level relationship fields are not epistemically appropriate substitutes for composition relationships established mechanically by the source.

Current schema implication:

* The baseline is valid but compositionally incomplete.
* This creates concrete pressure for evaluating whether Reference requires a dedicated mechanism for source-native parent/component relationships.
* No schema change is proposed from the baseline alone; the next step is to test a candidate representation through a controlled variant.

### PPTX YAML Variant A Checkpoint: Minimal Reference-Level Components

Observed in `comp-source-001-variant-a.yaml`:

* Variant A copies the valid PPTX baseline record and introduces one experimental Reference-level field:

  * `components`
* The candidate structure represents the five source-declared slides as ordered child components of `comp-source-001`:

  * `slide-1`
  * `slide-2`
  * `slide-3`
  * `slide-4`
  * `slide-5`
* Each component records:

  * `component_id`;
  * `relationship_type: contains`;
  * and source-declared `order`.

Validator result:

* Validation fails because `reference.components` is not part of the current MetaRCI base schema or Composite profile contract.
* The failure is expected and is treated as evidence rather than as an implementation defect.

Current interpretation:

* The valid baseline demonstrates that the current contract can represent the PPTX parent source.
* Variant A demonstrates that the current contract cannot represent the simplest observed Reference-level composition requirement without introducing a new structure.
* The candidate `components` structure preserves mechanically recoverable membership and ordering in the Reference tier rather than relocating those facts into Context or Interpretive relationship fields.
* This is a narrower requirement than a general package manifest or full component ontology.

Current schema implication:

* `reference.components` is a candidate Composite-specific structure, not an accepted schema change.
* The current PPTX evidence supports testing a minimal component representation containing:

  * component identity;
  * relationship to the parent;
  * and order when source-declared.
* More complex semantics such as component profiles, inheritance, completeness, graph relationships, and role vocabularies should remain deferred until additional testbeds demonstrate recurring need.

Open question:

* Can this minimal Reference-level component structure also represent source-native composition clearly in ODP and EPUB, or is it specific to PPTX?
### Composite Reference Validation Checkpoint: Minimal Components Structure

Observed in `comp-source-001-variant-a.yaml`:

* Variant A introduced a candidate `reference.components` structure containing:

  * `component_id`;
  * `relationship_type`;
  * optional source-declared `order`.
* The initial Variant A validation failed because `reference.components` was not part of the current Composite profile contract.
* `profiles/composite.yaml` was then amended to introduce `reference.components` as a conditional custom field.
* After that profile amendment, `comp-source-001-variant-a.yaml` validated successfully.

Current interpretation:

* PPTX evidence supports a minimal Reference-level mechanism for preserving source-declared component membership and ordering.
* The successful validation demonstrates that this candidate structure can be incorporated into the Composite profile without disrupting the current base contract.
* The structure remains intentionally narrow and does not introduce component profiles, inheritance, roles, completeness states, graph semantics, or other higher-order composition behavior.
* The field is conditional because source-native composition may not be exposed uniformly across all Composite formats.

Current schema implication:

* `reference.components` is now structurally viable within the Composite profile.
* The current minimum item grammar is:

  * required `component_id`;
  * required `relationship_type`;
  * optional `order`.
* ODP and EPUB testbeds should be used to determine whether this grammar is sufficiently portable before additional Reference-level properties are introduced.

Current status:

* Candidate change validated against the PPTX testbed.
* Reference-tier Composite development remains open pending cross-format evaluation.

### Composite Context Validation Checkpoint: Existing Context Grammar

Observed in `comp-source-001-context-variant-a.yaml`:

* The PPTX Context variant uses the existing MetaRCI Context grammar without introducing Composite-specific Context fields.
* The record identifies `chart1` and `workbook1` through the existing `related_sources` field.
* The variant validates successfully against the base schema and current Composite profile.

Current interpretation:

* The existing Context tier can associate externally curated source relationships with the Composite parent record.
* Validation does not demonstrate that the parent Context record can express distinct curated roles or purposes for individual components.
* For example, the current parent-level grammar cannot distinguish a curated role such as:

  * chart → supporting evidence;
  * workbook → chart data source.
* These role statements are contextual assertions rather than mechanically recoverable Reference facts.

Current schema implication:

* No new Composite-specific Context field is justified by this evidence alone.
* Component-specific Context may be represented more cleanly through independently scoped component records rather than through an increasingly complex parent-level Composite structure.
* Parent-to-component Context inheritance should remain unresolved rather than assumed.
* Further testing should determine whether component-level Context records are sufficient before any Composite-specific Context schema is introduced.

Current status:

* Existing Context grammar validated successfully.
* No Composite-specific Context field proposed at this checkpoint.
* Context scope and inheritance remain open design questions.

## PPTX Testbed Closure

Current evidence:

* `comp-source-001.pptx` demonstrates a coherent parent presentation containing multiple independently meaningful and structurally heterogeneous components.
* Mechanically recoverable PPTX structure confirms:

  * parent-level slide membership;
  * source-declared slide ordering;
  * embedded image relationships;
  * distinct speaker-note relationships;
  * native tabular structure;
  * chart relationships to separately embedded structured data;
  * and embedded audiovisual media with associated supporting resources.
* The PPTX testbed also demonstrates that technically addressable package resources such as themes, layouts, and other implementation artifacts should not automatically be treated as meaningful MetaRCI components.

Reference result:

* The baseline Composite record validated but could not represent source-declared composition structure without epistemically misplacing those relationships.
* A minimal conditional `reference.components` structure was introduced with:

  * required `component_id`;
  * required `relationship_type`;
  * optional source-declared `order`.
* The PPTX Reference variant validates successfully with this structure.
* The PPTX evidence therefore supports `reference.components` as a viable candidate Composite-specific field.

Context result:

* The existing Context grammar validates successfully for the PPTX testbed.
* No Composite-specific Context field is currently justified.
* Component-specific Context appears more appropriately handled through independently scoped component metadata where needed.
* Parent-to-component Context inheritance remains unresolved and should not be assumed.

Interpretive result:

* The existing Interpretive relationship grammar validates successfully for analytical component relationships.
* No Composite-specific Interpretive field is currently justified.
* Source-declared composition and analytical component significance remain cleanly separable between Reference and Interpretive.

Current Composite implication:

* PPTX evidence supports a deliberately small Composite contract.
* The only Composite-specific schema addition currently supported by this testbed is the conditional Reference-level `components` structure.
* Context and Interpretive require no PPTX-driven custom fields at this stage.
* More complex composition semantics, including component profiles, inheritance, completeness, graph behavior, role vocabularies, and cross-profile enforcement, remain unsupported by current evidence and should stay deferred.

Closure status:

* `comp-source-001.pptx` is closed as the initial Composite PPTX testbed.
* PPTX findings should now be challenged against `comp-source-002.odp` before `reference.components` or any broader composition semantics are treated as portable Composite requirements.

### ODP Evidence Checkpoint 1: Presentation-Level Membership and Ordering

Observed in `comp-source-002.odp`:

* The main presentation structure is contained in `content.xml`.
* `content.xml` declares five `<draw:page>` elements in sequence:

  * `page1`
  * `page2`
  * `page3`
  * `page4`
  * `page5`
* Each page contains substantive slide content rather than acting only as a package placeholder.
* ODP therefore preserves slide membership and slide ordering directly within the source content structure.

Current interpretation:

* ODP represents presentation composition differently from PPTX, but exposes the same underlying Composite concepts.
* PPTX expresses ordered slide membership through presentation relationships and separate slide parts.
* ODP expresses ordered slide membership through sequential `draw:page` elements within `content.xml`.
* The implementation mechanism differs, but parent/component identity and intrinsic ordering remain mechanically recoverable.
* These facts therefore constitute Reference-level composition evidence.

Current schema implication:

* ODP independently supports the PPTX-derived `reference.components` concept.
* No ODP-specific field or relationship mechanism is justified by this evidence.
* The current minimal candidate grammar remains sufficient for this checkpoint:

  * `component_id`;
  * `relationship_type`;
  * optional source-declared `order`.
* This provides initial cross-format evidence that `reference.components` represents a composition concept rather than an Office Open XML implementation detail.

Current status:

* PPTX-derived component membership and ordering semantics survive the first ODP portability test.
* Further ODP component inspection is required before the Reference structure can be considered portable across the full testbed.

### ODP Evidence Checkpoint 2: Embedded Image as a Meaningful Child Component

Observed in `comp-source-002.odp`:

* Slide 2 (`draw:page draw:name="page2"`) contains a `draw:frame` identified as `Image 0`.
* Within that frame, `draw:image` explicitly references:

  * `Pictures/10000000000004B0000002D072EB7ADB.png`
* The relationship is expressed through source-native ODF attributes including:

  * `xlink:href`
  * `xlink:show="embed"`
  * `draw:mime-type="image/png"`
* The PNG therefore exists as a separately stored package resource that is explicitly embedded by the slide rather than merely co-located within the ODP package.

Current interpretation:

* ODP independently confirms that meaningful embedded media can be mechanically associated with a parent slide.
* The source mechanism differs from PPTX relationship files, but the underlying whole-part relationship is equivalent.
* The image remains a meaningful child component of the slide and presentation rather than a package resource inferred only from file proximity.
* This relationship is mechanically recoverable and therefore belongs at the Reference tier.

Current schema implication:

* The existing `reference.components` concept remains sufficient.
* No image-specific Composite field is justified.
* ODP provides cross-format evidence that meaningful child components may be identified through format-native relationship mechanisms without requiring those mechanisms to be represented directly in the MetaRCI contract.

Current status:

* Embedded-image composition survives the ODP portability test.
* This strengthens the case that `reference.components` models source composition rather than PPTX-specific packaging behavior.

ODP Evidence Checkpoint 3: Speaker Notes as Distinct Slide-Associated Content

Observed in comp-source-002.odp:

Slide 2 contains a presentation:notes element.
Within that notes structure, a dedicated draw:frame is marked with presentation:class="notes".
The speaker note text is stored separately inside its own draw:text-box.
The note is therefore structurally distinct from the visible slide body while remaining explicitly associated with the slide.

Current interpretation:

ODP preserves speaker notes as a meaningful source-native child structure rather than flattening them into ordinary slide text.
This independently confirms the PPTX finding that notes may have their own metadata scope while remaining components of the parent slide and presentation.
The association is mechanically recoverable and therefore constitutes Reference-level composition evidence.

Current schema implication:

No note-specific Composite field is justified.
The existing reference.components concept remains sufficient to represent the presence of meaningful child components without encoding ODP-specific presentation markup.
Component-specific metadata scope remains a separate concern from the parent-level composition relationship.

Current status:

Speaker-note composition survives the ODP portability test.
ODP and PPTX now independently support the same parent/component distinction for notes.

ODP Evidence Checkpoint 4: Native Table Structure

Observed in comp-source-002.odp:

Slide 3 contains a native <table:table> element within the presentation content.
The table includes source-native structural elements such as:
<table:table-column>;
<table:table-row>;
<table:table-cell>.
Cell values are represented within the table structure rather than only as visually positioned text.
The ODP therefore preserves the table as structured content rather than flattening it into an image or drawing approximation.

Current interpretation:

ODP independently confirms that structured tabular content may remain a meaningful child component inside a presentation source.
The implementation differs from PPTX DrawingML table markup, but the underlying Composite relationship is equivalent.
The table’s presence and internal structure are mechanically recoverable and therefore constitute Reference-level evidence.

Current schema implication:

No table-specific Composite field is justified.
The existing reference.components concept remains sufficient to represent the presence of a meaningful structured child component.
Structural treatment of the table itself may belong to the Structured Data profile if evaluated independently, while its membership within the presentation remains a Composite concern.

Current status:

Native-table composition survives the ODP portability test.
ODP and PPTX now independently support structured tabular content as a meaningful component within a coherent presentation source.

ODP Evidence Checkpoint 5: Native Chart as an Embedded Structured Object

Observed in comp-source-002.odp:

Slide 4 contains a draw:object reference to ./Object 1.
The embedded object has its own content.xml.
That object contains native chart structure, including chart-specific elements such as:
<chart:chart>;
<chart:plot-area>;
chart series and associated structured data elements.
A separate replacement/preview representation also exists, but the chart is not represented only as an image.

Current interpretation:

ODP preserves the chart as an independently structured embedded component rather than flattening it into a visual approximation.
The implementation differs from PPTX, where the chart and backing workbook were connected through OOXML relationship files, but the same Composite principle holds: the presentation contains a meaningful structured child whose internal representation can be inspected independently.
The existence and containment of the chart are mechanically recoverable and therefore constitute Reference-level composition evidence.

Current schema implication:

No chart-specific Composite field is justified.
The existing reference.components structure remains sufficient to represent the chart as a meaningful child component.
The chart’s internal structural treatment may be handled separately from its Composite membership.
ODP further supports the distinction between composition relationship and component-internal schema.

Current status:

Native-chart composition survives the ODP portability test.
ODP and PPTX now independently support meaningful embedded structured objects within a coherent presentation source.

ODP Evidence Checkpoint 6: Embedded Audiovisual Media

Observed in comp-source-002.odp:

Slide 5 contains a draw:frame identified as Media 0.
Within that frame, a draw:plugin explicitly references:
ppt/media/media-5-1.mp4
The plugin declares:
xlink:show="embed"
draw:mime-type="video/mp4"
The same frame also contains a separate preview image:
Pictures/MediaPreview1.png
The ODP therefore preserves both the actual temporal-media component and a distinct visual preview representation.

Current interpretation:

The MP4 is explicitly embedded as a source-native media component rather than inferred from package co-location.
The preview image is structurally separate from the actual audiovisual content.
ODP independently confirms the PPTX finding that temporal media can remain a meaningful child component of a presentation.
The containment relationship is mechanically recoverable and therefore constitutes Reference-level composition evidence.

Current schema implication:

No audiovisual-specific Composite field is justified.
The existing reference.components concept remains sufficient to represent the media as a meaningful child component.
The Media profile may govern the component’s own temporal-media metadata if evaluated independently, while Composite governs its membership within the parent presentation.

Current status:

Embedded audiovisual composition survives the ODP portability test.
PPTX and ODP now independently support ordered slides, embedded images, notes, native tables, structured chart objects, and temporal media as meaningful components of a coherent presentation source.

### ODP YAML Validation Checkpoint: Cross-Format Portability of `reference.components`

A Composite record for `comp-source-002.odp` was created using the existing `profiles/composite.yaml` contract without modification.

The ODP variant represented the five source-declared presentation pages through the existing Reference-level `components` structure:

* `page1`
* `page2`
* `page3`
* `page4`
* `page5`

Each component used:

* `component_id`;
* `relationship_type: contains`;
* source-declared `order`.

The record also retained existing base Context and Interpretive structures without introducing ODP-specific fields.

Validation result:

* `comp-source-002-variant-a.yaml` passed validation against:

  * `schemas/metarci-base.yaml`
  * `profiles/composite.yaml`
* No Composite profile changes were required.

Current interpretation:

* The `reference.components` structure introduced during PPTX evaluation is not dependent on OOXML-specific relationship mechanics.
* ODP exposes equivalent whole-part semantics through different native structures, including sequential `draw:page` elements and format-native embedded-object references.
* Different source formats may therefore supply different native component identifiers while remaining representable through the same MetaRCI composition contract.
* The successful ODP validation provides cross-format evidence that `reference.components` represents a reusable structural concept rather than a PPTX-specific accommodation.

Current schema implication:

* The existing minimal `reference.components` grammar remains sufficient:

  * required `component_id`;
  * required `relationship_type`;
  * optional `order`.
* No additional Reference fields are justified by the ODP testbed.
* No Composite-specific Context or Interpretive fields are justified by the ODP testbed.
* More specialized component semantics should remain within the relevant component profile or Interpretive layer rather than expanding the parent Composite contract prematurely.

Current status:

* ODP successfully validates the Composite composition model derived from PPTX.
* `reference.components` now has supporting evidence from two independently structured presentation formats.
* Further portability evaluation should focus on a structurally different Composite source rather than another presentation package.
