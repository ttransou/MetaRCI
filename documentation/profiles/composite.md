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
  * images;
  * tables;
  * charts and chart data;
  * and audiovisual media where practical.
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

* Presentation files with independently meaningful text, notes, media, tables, and chart data.
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
