# MetaRCI Profile Model

## Overview

MetaRCI profiles define how the base schema is specialized for different source structures while preserving one shared three-tier model.

Profiles are structural classifications, not domain templates.

## Position in the MetaRCI Model

Current contract:

```text
Base schema → Structural profile → Record
```

Current contract:

* The base schema defines shared fields and validation expectations.
* A structural profile may constrain or extend that shared model.
* A record must validate against the effective schema produced from base plus profile.

Current guidance:

* Domain, organizational, and corpus-specific behavior should be represented through implementation extensions, not through new structural profiles.

## Why Profiles Exist

Current guidance:

* Different source structures require different metadata behavior.
* Profiles allow controlled specialization without fragmenting the base model.
* Profiles keep the base schema stable and reusable across implementations.

## Structural Classification

Current contract:

* Profiles are identified by source structure and metadata behavior.
* Profiles are not keyed to subject domain.

Current guidance:

* Domain-specific terminology and local policy should stay out of core profile definitions unless structurally required across implementations.

## MetaRCI 0.1 Profile Set

Current contract:

```text
document
structured-data
media
composite
```

Current contract:

* Each profile exists as an executable YAML file under the profiles directory.
* Each profile currently declares draft status and base-version alignment to 0.1.0.

## Profile Selection

Current guidance:

```text
Primarily bounded textual artifact?        → document
Meaning depends on explicit data schema?   → structured-data
Primarily visual/audio/audiovisual source? → media
Aggregation of meaningful components?      → composite
```

Current guidance:

* File format alone should not determine profile choice.
* A container such as PDF or ZIP may still map to different structural profiles depending on what the source unit is.

## Profile Declaration

Current contract:

* A profile document uses the metarci_profile root.
* A record document uses the metarci_record root.
* The validator enforces exact profile/base version linkage for the loaded documents.

Current contract:

```text
profile.base_version == base.version
record.profile_version == profile.version
```

Current contract:

* The record profile path must match the loaded profile path during validation.

## Overrides and Custom Fields

Current contract:

* Profiles may define tier_overrides and custom_fields in reference, context, and interpretive tiers.
* Override targets must exist in the base schema.
* Custom fields must not shadow base fields.

Current contract:

* Permitted shallow override attributes are:

```text
requirement
nullable
description
allowed_values
```

Current contract:

* Structural attributes such as type, item_type, properties, and item_properties are not overridable in MetaRCI 0.1.
* Requirement weakening is invalid.
* Making a non-nullable base field nullable is invalid.
* allowed_values may be narrowed but not expanded beyond base declarations.

Current guidance:

* Custom fields should be added only when structurally reusable for a profile class.
* Implementation-only fields should be added through extensions.

## Inheritance Model

Current contract:

* Current executable profiles extend only the base schema.

Current guidance:

* Profile-to-profile inheritance is deferred in MetaRCI 0.1 to avoid conflict-resolution complexity.

Deferred:

* Multi-level profile inheritance.

## Effective-Schema Resolution

Current contract:

```text
1. Base fields
2. Profile overrides
3. Profile custom fields
```

Current contract:

* Resolution is deterministic and validated before record value checks run.

## Profile Constraints

Current contract:

* A profile cannot remove MetaRCI tiers.
* A profile cannot remove base fields through overrides.
* A profile cannot weaken base requirement/nullability constraints.
* A profile cannot structurally redefine base fields through shallow overrides.

Current guidance:

* Profile definitions should remain implementation-agnostic and avoid local policy coupling.

## Lifecycle

Current contract:

* Profiles declare lifecycle status using allowed base values.
* Current profile YAML files are all draft.

Current guidance:

* Lifecycle transitions should be tied to evidence from profile usage and validation outcomes.

## Versioning

Current contract:

* Profile version matching is exact in current validator behavior.

Current guidance:

* Profile version should change when overrides, custom fields, or validation obligations change.

Deferred:

* Semantic-version compatibility ranges for profile matching.

## Candidate-Profile Governance

Current guidance:

* A new profile proposal should include structural justification, reusable field rationale, and expected validation behavior.
* Convenience for one implementation is insufficient justification for a new profile.

Open question:

* What minimum evidence threshold should be required before adding a fifth structural profile?

## Relationship to Implementation Extensions

Current contract:

```text
Base schema → Structural profile → Record
```

Current contract:

* Extensions are subordinate to the structural contract and must not silently override it.

Current guidance:

* Keep implementation-specific vocabularies, policy rules, authority linkages, and local validation in extension documentation.
* See documentation/extensions.md for current extension guidance.

## Unresolved Architecture Items

Open question:

* Which profile-specific guidance should graduate into executable profile fields in a future revision?

Proposed change:

* Any proposal to move currently profile-specific concerns into the base schema requires explicit evidence review and human approval.

Deferred:

* Deep profile inheritance.
* Automatic profile selection.
* Model-enforced extension-schema validation.
