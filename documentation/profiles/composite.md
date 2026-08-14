# Composite Profile

## Purpose

The Composite profile models a logical source whose independently meaningful parts remain components of one coherent parent source.

Composite membership is structural, not domain-specific. Physical packaging alone does not make a source Composite.

## v0.1 Contract

Executable contract in [profiles/composite.yaml](profiles/composite.yaml):

- Status: active
- Tier overrides: none
- Composite-specific custom fields: Reference tier only

Reference custom field:

- reference.components: conditional, nullable list<object>
- component_id: required string
- relationship_type: required string
- order: optional integer

No Composite-specific Context custom fields are part of v0.1.
No Composite-specific Interpretive custom fields are part of v0.1.

## RCI Placement

- Reference: source-declared or mechanically recoverable whole/part structure (membership, containment, intrinsic order).
- Context: externally supplied situating claims about components, when present, using inherited base fields.
- Interpretive: analytical claims about significance or meaning of components, using inherited base fields.

## Evidence Summary

Composite v0.1 closure is supported by completed evidence across three source families:

1. PPTX established source-declared ordered component membership and heterogeneous meaningful parts.
2. ODP independently reproduced the same composition pattern without contract changes.
3. EPUB independently reproduced composition behavior in a non-presentation format.

Cross-testbed result: the same minimal Reference-level components structure was reusable without introducing Composite-specific Context or Interpretive fields.

## Scope Boundaries

- Do not treat internal package artifacts as components unless they are independently meaningful.
- Do not infer Composite membership from container format alone.
- Do not force every component into independent records unless implementation goals require it.
- Use inherited relationship mechanisms for analytical or contextual statements about components.

## Boundaries with Other Profiles

- document: bounded textual or predominantly textual source units
- structured-data: schema-dependent data sources
- media: visual/audio/audiovisual source units
- composite: whole/part structure across meaningful components

These four profiles are peers in v0.1.

## Deferred Beyond v0.1

The following remain deferred and are not part of the current Composite contract:

- expected-versus-present membership state fields
- completeness state fields
- component role taxonomies
- parent/component inheritance rules
- referential-integrity enforcement of component IDs across records

## Practical Guidance

- Keep component entries source-grounded and minimal.
- Add only evidence-supported component relationships in Reference.
- Keep Context and Interpretive assertions explicit and attributable through inherited fields.
- Treat testbeds as evaluation evidence, not as the definition of the model.
