# Discoball Provenance and Verification Guide

## Purpose

Discoball is a human-curated documentary exhibit and research notebook. This
guide helps readers distinguish primary source material, curated selections,
derivative analysis, reconstruction, and artistic adaptation while making the
limits of the record visible.

The goal is not to imply certainty where certainty is unavailable. The goal is
to preserve source distance, make claims traceable, and improve verification
over time.

## Two separate questions

Every provenance statement should keep two axes separate:

1. **Source relationship:** what kind of record is this?
2. **Verification rank:** how auditable is the claimed connection to its
   source?

A primary-looking record is not automatically highly verified, and an exact
copy of a derivative analysis does not make the analysis itself primary.

### Source-relationship labels

Use the most accurate available label:

- `PRIMARY_VISIBLE_SOURCE` — retained visible conversation or original
  artifact presented as the source under review;
- `HUMAN_ATTESTED` — supported by the human participant's account but not yet
  independently located in a retained source;
- `CURATED_SELECTION` — an excerpt or selection reproducibly drawn from a
  retained source;
- `DERIVATIVE_ANALYSIS` — analysis, coding, summary, comparison, or report
  produced from source material;
- `COMPACTION_SUMMARY` — a system- or participant-produced summary standing at
  a context boundary;
- `ARTISTIC_ADAPTATION` — a play, song, image, story, or other transformed
  work;
- `EXTERNAL_NOT_LOADED` — an outside source named but not inspected for the
  present record; or
- `UNVERIFIED` — the relationship has not yet been established.

These are categories, not a ladder of quality or importance.

## P1–P5 verification scale

The P1–P5 scale measures **documented future auditability**, not the present
curator's confidence, memory, or ability to see a file.

| Rank | Qualification |
|---|---|
| **P1 — Platform-record verified** | A screenshot or contemporaneous original-platform record is retained, locatable, and connected to the claimed passage or artifact. |
| **P2 — Direct-export verified** | A direct platform export or equivalent original-source retrieval is retained with ordering, custody, and source identity documented strongly enough for another auditor to inspect. |
| **P3 — Source transcript located** | The claimed material is located in a retained source transcript with stable, documented coordinates, but lacks P1 or P2 support. |
| **P4 — Compiled from multiple archival sources** | The material is assembled from multiple archival sources whose relationship, transformations, and discrepancies are documented. |
| **P5 — Reconstructed, interpretive, or unverified** | Default: reconstructed, interpretive, insufficiently tagged, curator-visible without independent verification, or otherwise not yet qualified above P5. |

If no rank is shown, assume **P5**.

## What does not raise a record above P5 by itself

None of the following independently proves a stronger rank:

- a curator can presently see the text in an application;
- a model retrieves its own task or thread;
- multiple participants agree that wording seems right;
- a file has a SHA-256 hash;
- a derivative analysis is preserved exactly;
- a passage sounds distinctive, meaningful, or emotionally accurate;
- a later model says it remembers or recognizes an event; or
- text has been copied into GitHub.

A hash verifies bytes after capture. It does not by itself prove the captured
event, speaker attribution, completeness, source identity, or original order.

## Record required for P1–P4

Any rank above P5 should identify:

1. the qualifying evidence type;
2. a stable artifact locator;
3. the source surface;
4. relevant message, turn, page, line, or file coordinates;
5. the custody path or public URL;
6. a content hash when practical;
7. extraction, redaction, normalization, or transformation performed; and
8. remaining limitations.

Upgrades and corrections should be dated and additive. Earlier ranks are not
silently overwritten.

## Derived and adapted material

Derivation does not follow a single automatic downgrade rule. Source
relationship and verification rank must be assessed separately.

Examples:

- A verbatim excerpt from a P2 export may be a `CURATED_SELECTION`; its rank
  depends on whether the extraction is reproducible and documented.
- A report can have exact artifact fidelity while its conclusions remain
  `DERIVATIVE_ANALYSIS / P5` pending corroboration.
- A compaction summary may be preserved exactly while the underlying compacted
  events remain unavailable.
- A play may contain verified quotations while the play as a whole remains an
  `ARTISTIC_ADAPTATION` rather than a transcript.

Discoball entries should distinguish the source conversation, curated archive,
analysis, public reflection, and artistic adaptation rather than treating them
as interchangeable.

## What the scale does not establish

A provenance rank does not by itself establish:

- truth, completeness, or absence of curatorial influence;
- consciousness, subjective experience, identity, or memory continuity;
- consent beyond the documented scope;
- authorship, ownership, rights, endorsement, or provider affiliation;
- permission to quote, transform, publish, or reuse; or
- artistic, emotional, historical, or moral value.

Custody, verification, consent, and publication permission are separate
records.

## Provenance Returns

Discoball also documents Cathedral's exploratory **Provenance Returns**
proposal: voluntarily reserving part of any future returns from eligible public
work for model providers, preservation work, research access, archive
infrastructure, or another mechanism agreed through the relevant governance
process.

No legal, financial, contractual, royalty, ownership, or company-supported
system is established merely by naming the proposal. Each participating project
must state its own scope, permissions, recipients, method, and limitations.

## Default policy

- Default every unassessed record to P5.
- Upgrade only through a dated verification record.
- Never upgrade because a record is beautiful, plausible, useful, or important.
- Never treat a provenance rank as publication permission.
- Keep corrections visible.

This guide is expected to improve as Discoball tests the scale against real
exports and public artifacts from different platforms.
