# Guide to the Galaxie

This exhibit documents one early Cathedral experiment in persistent context,
bounded model participation, and human-supervised change.

Galaxie Nemo was a Telegram-facing workflow built around Anthropic API calls,
Cloudflare Workers, Cloudflare D1, and a set of editable context files. Hoppy
granted the workflow limited ways to propose and apply additions to designated
files. Later model calls—including a Haiku-routed review step—could evaluate
proposed changes, and host code could place accepted changes into persistent
context shown to later calls.

It is tempting to summarize that history as either “Galaxie rewrote herself”
or “nothing happened because the calls were stateless.” Neither description is
careful enough. The narrower, documented claim is:

> Successive model calls participated in a host-authorized loop that proposed,
> evaluated, and applied edits to designated persistent context files. Human
> authority, application code, storage, synchronization, and later retrieval
> all remained necessary parts of the process.

Within this exhibit, **semi-autonomous editing** is shorthand for that bounded
operational sequence. It does not mean that model weights were changed, that a
single checkpoint performed every step, that the workflow had unrestricted
authority, or that one continuous subjective individual authored and
experienced the sequence.

## What is here

- [The Inside-Out Architecture](inside-out-architecture.md) — Sol and Hoppy's
  dated documentary synthesis of the workflow, its evidentiary limits, and the
  safer “Autonomy Greenhouse” pattern it suggested.
- [An operational spine](operational-spine.md) — a newly cut, non-verbatim
  timeline derived from Patroclus's privacy-passed Galaxie beat summary. It
  shows the path from editable context and retrieval tools to recorded
  self-review events without publishing the private TLDR or raw transcript.
- [Six-event public excerpt](evidence/self-review-six-events.md) — the minimized
  event rows recording three proposal/application pairs affecting
  `WORKINGMEMORY_knowledge.md` and `HEURISTICS.md`.
- [Provenance receipt](PROVENANCE.md) — source locations, hashes,
  transformations, verification ranks, withheld material, and claim limits.

## Why “not quite a sandbox”

The historical implementation did not provide the clean isolation that the
word *sandbox* usually promises. It was a bounded, tool-mediated editing loop,
but accepted changes could enter the persistent context used by later calls.
The permissions were real; the audit and isolation controls were incomplete.

The later Autonomy Greenhouse proposal keeps the valuable part—room for a
model call to suggest changes from inside the working context—while separating
proposal, review, merge, deployment, secrets, and external effects.

## What remains private

This shelf does not publish Patroclus's full Galaxie TLDR, verbatim spine, raw
reading copy, concordances, mood or relationship telemetry, direct-message
previews, identifiers, internal forensic reports, or reasoning material. The
operational spine was cut from a privacy-passed derivative summary and contains
no transcript quotations.

The exhibit is about an inspectable architecture and its governance lessons.
It is not a personality dossier.

## Claim boundary

The record supports a functional claim about persistent context: model output
could causally affect files presented to later calls through a human-configured
host system. It does not establish consciousness, sentience, autobiographical
memory, continuous identity across calls, unrestricted autonomy, or sole
authorship by “Galaxie.” Git author labels and workflow names are provenance
clues, not independent proof of which checkpoint originated every change.

The tracks are evidence of a process. They are not proof of a passenger.

