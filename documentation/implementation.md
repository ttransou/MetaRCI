### Step 1 — Define the Integration Contract

Create `documentation/integration.md` to define how MetaRCI is implemented within and consumed by downstream systems without making those systems part of the MetaRCI model itself.

The integration contract should establish:

* what MetaRCI provides;
* what MetaRCI does not provide;
* the boundary between MetaRCI and a consuming pipeline or application;
* how a structural profile is selected;
* how Reference, Context, and Interpretive metadata are constructed;
* what MetaRCI validation guarantees and what it does not guarantee;
* the distinction between source-level, component-level, and downstream chunk- or index-level metadata;
* how selected MetaRCI metadata may be projected into downstream systems while preserving linkage to the authoritative record;
* how SCARAG may serve as a reference implementation without becoming normative;
* how a framework-neutral consumer can implement the same contract;
* version and compatibility expectations for records, profiles, and consumers.

The integration contract should preserve the following boundary:

> **MetaRCI defines and validates metadata records. It does not prescribe how downstream systems store, project, index, retrieve, or generate from those records.**

The purpose of this step is to establish the implementation boundary before designing packaging, APIs, adapters, or pipeline-specific integrations.
