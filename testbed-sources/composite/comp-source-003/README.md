# comp-source-003

## Source

- Source type: synthetic EPUB publication
- File: `comp-source-003-generic-testbed.epub`
- Profile target: `composite`
- Intake ID: `comp-source-003`

## Purpose

This source is a bounded synthetic Composite testbed constructed to challenge composition semantics outside presentation formats.

The specimen is intended to test whether parent identity, resource membership, ordered reading sequence, heterogeneous components, and parent/component metadata scope remain useful across a publication-oriented container.

## Included Components

The EPUB contains:

- publication-level metadata;
- three XHTML content documents;
- an explicit package manifest;
- an explicit spine establishing reading order;
- a navigation document;
- an embedded SVG image;
- a table embedded within one content document;
- a shared stylesheet.

These components deliberately combine Document-like, Media-like, and Structured Data-like structures within one publication-level parent source.

## Source Handling

The EPUB should be preserved as the original synthetic test artifact.

Any unpacking, extraction, normalization, conversion, or derived inspection output should be documented separately rather than replacing or silently modifying the source file.

## Testbed Role

`comp-source-003` is the publication-oriented Composite challenge specimen.

Its purpose is to test:

- parent publication identity;
- explicit resource membership;
- reading order;
- component identity;
- heterogeneous component structure;
- meaningful versus package-only resources;
- parent-level versus component-level metadata scope;
- and portability of candidate composition semantics beyond presentation formats.

The specimen does not define the final Composite contract.

## Known Limitations

- The EPUB is synthetic rather than a naturally occurring publication.
- Component selection was intentionally designed to expose structural variety.
- The table is embedded within an XHTML content document rather than stored as an independent tabular resource.
- Findings should be interpreted together with PPTX and ODP evidence rather than as independent proof of a universal composition model.
