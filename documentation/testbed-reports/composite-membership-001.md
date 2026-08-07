# Testbed Report: Composite Membership Semantics 001

## Header

* Testbed name: composite-membership-001
* Profile: composite
* Date: 2026-08-07
* Author: repo working draft
* Source set summary: one baseline composite package record plus two modeled variants focused on expected versus present membership semantics.

## Questions Covered

From documentation/profiles/composite.md:

* How should expected versus present members be represented?
* How should member roles and ordering be expressed?
* How should completeness be represented when expected membership is unknown?
* Can and should a composite explicitly contain members validated under different structural profiles in a future contract?

## Baseline Representation

* Record path: examples/composite-record.yaml
* Why baseline reflects current contract:
  * Uses existing base fields only.
  * Uses related_sources plus interpretive.relationships for member linking.
  * Requires no composite custom fields.
* Validator result:
  * Passes under current contract when loaded with profiles/composite.yaml and schemas/metarci-base.yaml.

## Variant A

* Goal: represent expected and present members distinctly without changing contract.
* Representation:
  * Keep profile unchanged.
  * Use context.related_sources for present members only.
  * Encode expected-but-missing members as interpretive notes and relationships to planned identifiers.
* Validator result:
  * Expected to pass because only existing base fields are used.
* Strengths:
  * No profile or validator change required.
  * Preserves current contract and tooling.
* Weaknesses:
  * Completeness state remains implicit and harder to query.
  * Member role/order semantics are weakly structured.

## Variant B

* Goal: evaluate a candidate shape for explicit membership semantics.
* Representation:
  * Candidate field (proposal only, not implemented):
    * context.member_manifest: list<object>
    * child properties: member_id, member_profile, member_role, member_order, membership_status
  * membership_status would distinguish expected and present states.
* Validator result:
  * Not executable under current contract unless profile YAML adds this custom field.
* Strengths:
  * Clear expected-versus-present semantics.
  * Better queryability for roles/order and completeness.
* Weaknesses:
  * Requires profile custom field introduction and new tests.
  * Needs evidence that the shape is reusable across multiple composite implementations.

## Evidence Summary by Question

### 1) Expected versus present members

* Observed ambiguity:
  * Baseline model can express present members clearly.
  * Expected-but-missing members are only weakly representable without structured fields.
* Tier-placement impact:
  * Candidate field plausibly belongs in context.
* Reusability across sources:
  * Not yet established; needs at least one additional composite testbed.
* Extension-only viability:
  * Possible, but weak for cross-implementation reuse and interoperability.
* Candidate closure outcome:
  * Proposed change (pending additional evidence).

### 2) Member roles and ordering

* Observed ambiguity:
  * Roles/order can be described in notes but not strongly structured in baseline contract.
* Tier-placement impact:
  * Candidate role/order fields fit context-level collection metadata.
* Reusability across sources:
  * Plausible but not yet demonstrated by multiple implementations.
* Extension-only viability:
  * Possible but may fragment semantics by implementation.
* Candidate closure outcome:
  * Open question for now; could become Proposed change with second testbed.

### 3) Completeness when expected membership is unknown

* Observed ambiguity:
  * Baseline supports partial representation but no explicit completeness state.
* Tier-placement impact:
  * Completeness state likely context-level.
* Reusability across sources:
  * Unknown; requires partial-ingest scenarios in another composite testbed.
* Extension-only viability:
  * Viable short-term; weak for consistent cross-project interpretation.
* Candidate closure outcome:
  * Current guidance now, Proposed change candidate later.

### 4) Mixed-profile members in one composite

* Observed ambiguity:
  * Baseline already references document/media/structured-data members via relationships.
* Tier-placement impact:
  * No immediate tier change required.
* Reusability across sources:
  * Present in current example; still needs broader confirmation.
* Extension-only viability:
  * Not required for baseline practice.
* Candidate closure outcome:
  * Current guidance: allow in practice via relationships; defer formal constraints.

## Proposed Change Candidate (if any)

* Candidate field or rule:
  * context.member_manifest as list<object> with member_id, member_profile, member_role, member_order, membership_status.
* Profile location:
  * profiles/composite.yaml custom_fields.context
* Why current contract is insufficient:
  * Cannot encode expected-versus-present membership and completeness state in strongly queryable form.
* Why extension-only is insufficient:
  * Extension-only representation risks inconsistent semantics across implementations.
* Required implementation bundle:
  * profile YAML update
  * example record update
  * tests update for nested member-manifest validation
  * docs update in documentation/profiles/composite.md and documentation/profile-question-matrix.md

## Final Recommendation

* Keep open for now, with a proposal candidate documented.
* Required next evidence step:
  * Run a second composite testbed on a different package type (for example, archival series or regulatory filing bundle) and compare whether the same member_manifest shape is still minimal and reusable.
