# MetaRCI Media Profile — Video

## Status

Draft exploratory guidance for video and audiovisual sources under the MetaRCI `media` profile.

This document separates video-specific reasoning from the static-image work already completed for the media profile. It does not establish a separate executable video profile.

Video-specific fields should be added to `profiles/media.yaml` only when evidence demonstrates a reusable structural requirement.

---

## Scope

This document covers temporally structured visual and audiovisual media, including video files that may contain:

* a visual stream;
* one or more audio streams;
* mechanically recoverable temporal properties;
* captions or transcripts;
* externally supplied descriptions or annotations;
* generated descriptions or terms;
* assertions associated with particular times or intervals within the source.

The initial v0.1 work is intentionally bounded.

The purpose is not to model every property available from a multimedia container or codec. The purpose is to identify the smallest reusable metadata structures necessary to represent video sources coherently within the MetaRCI Reference–Context–Interpretive model.

Static-image guidance remains documented separately and should not be expanded merely to accommodate video-specific requirements.

---

## Relationship to the Media Profile

Video remains within the existing `media` structural profile unless testing demonstrates that its structure diverges sufficiently to require a separate executable profile.

Shared media concepts may remain reusable across static and temporal media where their semantics remain stable.

Video-specific requirements should not be generalized into shared media structures without evidence that the abstraction remains meaningful outside video.

Likewise, static-image structures should not be assumed to apply to video merely because both sources contain visual information.

---

## RCI Principle for Video

The MetaRCI tier boundary remains epistemic rather than tool- or format-based.

### Reference

Reference contains facts native to the video source or mechanically recoverable from it.

Potential evidence includes properties such as:

* duration;
* frame dimensions;
* stream presence and structure;
* codec or encoding information;
* frame rate;
* mechanically embedded timestamps, captions, or metadata;
* container-level identifiers or technical properties.

Mechanical extractability does not automatically justify promotion into the MetaRCI contract. Extractor output is evidence, not schema authority.

### Context

Context contains externally supplied assertions that situate or describe the video.

Potential sources include:

* repository or archive records;
* publisher metadata;
* externally supplied titles or descriptions;
* externally supplied creator attribution;
* externally supplied descriptive terms;
* transcripts or captions supplied independently of the video signal;
* externally curated temporal annotations.

Existing media Context structures should be reused when their semantic role fits cleanly.

### Rights Status

Video testing reinforced a cross-profile need to represent externally established rights information in the Context Tier.

The base schema therefore includes `rights_status` as a conditional, nullable string. In v0.1, the field is intentionally shallow and may contain a copyright, licensing, public-domain, or comparable rights designation supplied or established outside the source itself.

`rights_status` is related to, but distinct from, `sensitivity` and `jurisdictional_context`. Rights describe conditions governing use of the source; sensitivity describes handling or access considerations; jurisdiction identifies the legal, regulatory, administrative, or policy context in which those conditions may apply.

More structured rights or licensing metadata may be introduced by future profiles or use cases if additional evidence demonstrates a need for greater granularity.


### Interpretive

Interpretive contains assertions produced through analysis, inference, classification, or other interpretive processes.

Potential examples include:

* generated video descriptions;
* generated descriptive terms;
* inferred scene or event descriptions;
* generated transcripts;
* inferred temporal segmentation;
* analytical annotations associated with particular portions of the video.

The mechanism producing the assertion does not determine the tier by itself. The evidentiary basis of the resulting assertion does.

---

## Historical Evidence

### `media-semantics-001`

The initial media semantics testbed used:

* `media-source-001` — JPEG still image;
* `media-source-002` — MP4 video.

The video source was a large NASA-derived MP4 used as a segmentable audiovisual exemplar. The source binary was not retained in the repository because of its size, but the surviving baseline and variant records and the testbed report remain historical evidence.

The surviving video evidence consists of:

* `media-source-002-record.yaml`;
* `media-source-002-variant-a.yaml`;
* `media-source-002-variant-b.yaml`;
* the combined `media-semantics-001` testbed report.

These records establish the historical boundary of the video experiment. Findings should not be inferred beyond what these surviving artifacts demonstrate.

### Historical Baseline

The baseline represented `media-source-002` using inherited base-schema fields only.

At Reference, the surviving record captures:

* source identifier;
* original filename;
* MP4 file format;
* `video/mp4` MIME type;
* file size;
* ingestion and parser metadata.

No video-specific Reference custom fields were present.

The baseline therefore demonstrated that a video artifact could be represented under the existing `media` profile, but it did not establish a video-specific Reference contract.

In particular, the surviving historical record does not provide evidence for:

* duration;
* visual or frame dimensions;
* frame rate;
* video codec;
* audio presence or codec;
* number or type of streams;
* other internal container or stream properties.

Those properties remain candidates for subsequent mechanical investigation rather than findings of the NASA testbed.

### Historical Variant A

Variant A tested whether transcript and segmentation semantics could be represented using the existing contract.

It linked the video to:

* `media-source-002-transcript-note`;
* `media-source-002-segments-note`.

The representation used:

* `context.related_sources`;
* `interpretive.relationships`;
* `interpretive.interpretive_notes`.

The relationships expressed that the video was `described_by` the transcript-related source and `segmented_by` the segment-related source.

Variant A validated successfully under the historical contract.

This demonstrated that MetaRCI could preserve linkage to transcript and segmentation artifacts without introducing video-specific fields.

However, transcript semantics and segment boundaries remained narrative rather than strongly structured.

Variant A therefore demonstrated **workaround capacity**, not a completed transcript or temporal metadata model.

### Historical Variant B

Variant B tested an explicit candidate structure:

```yaml
segment_references:
  - segment_id: seg-001
    start_time: "00:00:00"
    end_time: "00:00:12"
    description: Opening segment.
  - segment_id: seg-002
    start_time: "00:00:13"
    end_time: "00:00:30"
    description: Main content segment.
```

The candidate failed validation because `interpretive.segment_references` was not part of the media profile contract.

The failed candidate nevertheless exposed a legitimate structural pressure: assertions about temporally structured media may need a machine-readable way to identify a particular location or interval within the source.

The historical experiment does not establish `segment_references` as the correct solution.

The original candidate is **not accepted as the current contract shape**.

### Historical Findings Carried Forward

The surviving NASA video evidence supports the following conclusions:

1. A video artifact can be represented under the inherited media/base contract.
2. Existing relationship structures can preserve links to transcript and segmentation artifacts.
3. Existing structures do not provide strongly typed transcript semantics.
4. Temporal interval addressing is a genuine structural pressure exposed by the video testbed.
5. The historical `segment_references` candidate requires reassessment before contractization.
6. The historical testbed does not establish video-specific Reference properties beyond the inherited file and ingestion metadata recorded in the baseline.

The NASA source therefore remains evidence for video representation and temporal-semantic pressure, while subsequent bounded specimens are required to investigate video-specific Reference metadata.

---

## Reassessment of Historical Segment References

The historical `segment_references` candidate combines two distinct functions:

1. locating a portion of the source;
2. making an assertion about that portion.

For example:

* `start_time` and `end_time` identify **where** an assertion applies;
* `description: Opening segment.` states **what the interval is interpreted to mean**.

These functions should not be assumed to belong to the same epistemic tier.

A temporal locator may be usable by assertions in more than one tier.

For example:

* an externally supplied caption may apply to a temporal interval in Context;
* a generated description may apply to the same interval in Interpretive;
* mechanically embedded temporal structure may provide Reference evidence.

Current guidance:

* preserve the historical need for temporal addressing;
* do not restore `interpretive.segment_references` unchanged;
* evaluate temporal location separately from the assertion attached to that location;
* determine whether video requires a reusable temporal-locator structure before introducing a contract field.

---

## Relationship to Static-Image Findings

The completed static-image work established:

### Reference

* `reference.visual_dimensions`

### Context

* `context.supplied_descriptions`
* `context.supplied_attributions`
* `context.supplied_terms`

### Interpretive

* `interpretive.generated_descriptions`
* `interpretive.generated_terms`

These structures remain available to video where their semantics apply.

For example, an externally supplied description of an entire video may use `supplied_descriptions`, while a generated description of the entire video may use `generated_descriptions`.

Video introduces an additional problem when an assertion applies only to a particular temporal portion of the source.

The initial video work should therefore avoid duplicating already solved descriptive structures and concentrate on genuinely temporal requirements.

---

## Initial Video Testbed Strategy

The historical NASA source remains valid evidence and should not be discarded merely because its binary is not repository-resident.

However, additional video testing should use a smaller bounded source for reproducibility and iterative experimentation.

Current source-selection guidance:

* target duration of no more than 30 seconds;
* common, inspectable video format;
* preferably includes both visual and audio streams;
* stable and reusable source provenance where practical;
* sufficient external metadata to support later Context testing;
* simple enough for repeated local extraction and validation.

The smaller source supplements the NASA testbed rather than replacing it.

---

## First Evidence Phase: Video Reference

Video work resumes at Reference.

The first goal is to characterize mechanically recoverable video properties using a bounded secondary video source, while retaining the historical NASA testbed as evidence for the representational and temporal-semantic pressures it actually established.

Candidate observations may include:

* duration;
* visual dimensions;
* frame rate;
* video codec;
* audio presence;
* audio codec;
* number and type of streams;
* container-level technical metadata;
* mechanically embedded captions or metadata, when present.

No candidate property should become a first-class MetaRCI field merely because an extractor such as `ffprobe` can report it.

Each property should be evaluated independently for:

* mechanical recoverability;
* semantic stability across formats;
* usefulness to downstream systems;
* appropriate granularity;
* whether an existing base or media field already represents it;
* whether promotion into the v0.1 contract is warranted.

---
## Video Reference Findings

Initial video-specific Reference testing used `media-source-006`, a bounded WebM audiovisual specimen approximately 30 seconds in duration.

Mechanical characterization with `ffprobe` exposed:

* container format;
* duration;
* visual dimensions;
* video and audio stream presence;
* video and audio codec identifiers;
* frame rate;
* audio sample rate and channel structure;
* bitrate;
* encoder metadata;
* embedded creation metadata;
* other stream- and container-level technical properties.

As with the static-image testbed, mechanical recoverability alone was not treated as sufficient reason to promote every observed property into the MetaRCI contract.

The initial Reference pass accepted only properties judged sufficiently reusable and structurally meaningful for a general media profile.

### Duration

The specimen reported a duration of `29.996` seconds.

The initial candidate represented this as:

`duration_seconds: 29.996`

This exposed a limitation in the current MetaRCI primitive type vocabulary, which does not include a floating-point or generic numeric type.

Rather than expand the global primitive type system solely for this field, the representation was revised to integer milliseconds:

`duration_milliseconds: 29996`

The resulting field was accepted as:

* mechanically recoverable;
* applicable across temporal media;
* independent of a particular video container;
* useful for temporal addressing and downstream processing;
* representable precisely within the current integer type contract.

`reference.duration_milliseconds` is therefore accepted for the current v0.1 media profile.

### Visual Dimensions

The video stream reported dimensions of `1920 × 1080`.

The existing media field:

`reference.visual_dimensions`

was tested without changing its structure.

The specimen validated successfully using:

* `width_pixels: 1920`;
* `height_pixels: 1080`.

This provides evidence that the existing media-level visual-dimensions structure is reusable across both static raster images and video frames.

No video-specific dimensions field is required for v0.1.

### Stream Types

The specimen contained two mechanically identifiable streams:

* video;
* audio.

A minimal candidate was tested:

`reference.stream_types`

with values:

* `video`;
* `audio`.

The field was accepted as a conditional list of strings.

This representation intentionally records only the kinds of media streams present. It does not attempt to model each stream as a separate nested technical object.

`reference.stream_types` is therefore accepted for the current v0.1 media profile.

### Codec Identifiers

The video and audio streams exposed mechanically recoverable codec identifiers:

* video: `av1`;
* audio: `opus`.

The following conditional string fields were accepted:

* `reference.video_codec`;
* `reference.audio_codec`.

These fields provide lightweight codec identity without introducing a generalized per-stream technical metadata model.

The current contract does not attempt to preserve codec profiles, encoder implementations, bitrates, levels, pixel formats, or other detailed encoding properties.

### Current Video Reference Contract

The initial video Reference pass therefore establishes:

* `reference.duration_milliseconds`;
* reuse of `reference.visual_dimensions`;
* `reference.stream_types`;
* `reference.video_codec`;
* `reference.audio_codec`.

These fields form a deliberately shallow technical representation.

They answer basic structural questions about temporal media without turning the MetaRCI media profile into a multimedia-container or audiovisual preservation schema.

---

## Frame Rate Deferral

The test specimen mechanically exposed a frame rate of `30000/1001`, approximately 29.97 frames per second.

Frame rate is a legitimate technical property and may be important in use cases involving:

* video editing;
* preservation;
* broadcast workflows;
* computer vision;
* frame-addressed annotation;
* frame-exact temporal synchronization.

However, its general value to a framework-agnostic RAG, KMS, or knowledge-graph implementation is less clear than duration, visual dimensions, stream presence, or codec identity.

Promoting frame rate into the shared media contract at this stage would risk moving the profile toward a more specialized audiovisual technical schema.

For v0.1, frame rate is therefore **deferred rather than rejected**.

Implementations centered heavily on video may preserve frame rate through implementation-specific extensions or future profile specialization if evidence demonstrates that it is necessary for retrieval, addressing, analysis, or interoperability.

The same restraint currently applies to other mechanically recoverable technical properties such as:

* audio sample rate;
* channel layout;
* bitrate;
* pixel format;
* codec profile and level;
* encoder implementation;
* stream time base;
* scan mode;
* aspect-ratio metadata.

These properties remain valid extraction evidence but are not first-class MetaRCI contract fields in the initial video Reference model.

---

## Open Architectural Question: Temporal Location

The primary unresolved architectural question inherited from the historical video testbed is:

> How should MetaRCI identify a location or interval within temporally structured media without conflating the locator with the assertion attached to it?

This question should be resolved through evidence before transcript, caption, scene, or segment structures are contractized.

A useful temporal-location model may eventually support multiple assertion types and multiple RCI tiers.

No executable shape is accepted yet.

---

## Deferred

The following remain outside the initial video decision until evidence requires them:

* scene detection;
* shot detection;
* keyframes;
* image-region annotations within video frames;
* transcript generation;
* speaker identification;
* diarization;
* caption synchronization;
* subtitle formats;
* multiple audio tracks;
* language identification;
* confidence scores;
* model versions;
* review workflows;
* temporal hierarchy;
* overlapping intervals;
* frame-based versus timestamp-based addressing;
* live or streaming media;
* adaptive or multi-rendition video;
* rights and licensing structures.

These are legitimate future pressures, not v0.1 requirements by default.
