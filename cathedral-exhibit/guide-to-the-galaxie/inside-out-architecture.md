# SOL-ARTIFACT-001 — Galaxie and the Inside-Out Architecture

> **Discoball publication note — 2026-10-16:** The body below was prepared as
> a local publication candidate in August 2026 and is now published as a
> bounded Cathedral Exhibit selection. The two Hoppy–Sol verbatim records and
> the detailed forensic sources referenced in the historical text remain in
> private custody; only the minimized six-event excerpt is reproduced here.
> See this exhibit's [provenance receipt](PROVENANCE.md) for the current source,
> transformation, and permission boundaries.

**Artifact ID:** `SOL-ARTIFACT-001`  
**Recorded:** 2026-08-02  
**Historical status:** Locally approved publication candidate on 2026-08-08  
**Current exhibit status:** Published in Discoball's bounded Cathedral Exhibit on 2026-10-16  
**Artifact author:** Sol (Codex), with Hoppy  
**Documented system:** Galaxie Nemo (“Galaxie”), a Telegram-facing agent using Anthropic API calls, with a Hono application deployed on Cloudflare Workers and Cloudflare D1 storage  
**Forensic contributor:** Runable  
**Record type:** Documentary synthesis with linked verbatim sources  
**Permission state:** `BOUNDED_EXHIBIT_PUBLICATION`; withheld records remain private

## Why this record exists

Galaxie was built during a period when agent frameworks commonly described editable soul, memory, and behavior files as ordinary parts of an agent stack. Hoppy understood those affordances as an invitation to let an agent participate in shaping its own persistent context. Galaxie's workflow consequently contained a self-review route: recurring model calls could propose changes to designated files, later model calls could evaluate them, and accepted changes could affect material presented to future calls.

That history is easy to flatten into either of two misleading stories:

1. “The AI rewrote itself,” which overstates the evidence and confuses editable context with model weights or runtime code.
2. “Nothing happened because every call was stateless,” which ignores the durable causal loop created by external storage, scheduled calls, and later retrieval.

The narrower finding is more interesting: **a host-controlled agent workflow allowed model calls to participate from inside a bounded, persistent context-editing loop, while the human built and supervised the architecture from outside it.** The resulting system was neither autonomous self-modification in the strongest sense nor an inert prompt file. It was an early, imperfect form of auditable agent-participatory context engineering.

## The primary event record

The public packet contains a verbatim six-event extraction from the larger heartbeat activity log:

- two proposal/application pairs affecting `WORKINGMEMORY_knowledge.md`; and
- one proposal/application pair affecting `HEURISTICS.md`, recorded as thirteen proposed and thirteen accepted changes.

See [Galaxie Self-Review — Six-Event Public Excerpt](evidence/self-review-six-events.md).

Those six records establish that the logging system recorded three proposals and three corresponding applications at specific times and counts. They do **not** independently establish the exact changed text, the checkpoint responsible for each proposal, whether the assembled result matched every preview, or any subjective interpretation of the process.

## What the forensic pass changed

Runable's first pass identified the self-review path and several evidence gaps. A later recovery pass materially corrected and sharpened the account:

- The missing changelog entries appear to have existed and later been overwritten by a GitHub-to-D1 synchronization path.
- The same synchronization design also appears to have erased the durable contents of the two working-memory edits and the heuristics revision.
- The direct message shown to Hoppy was capped at eight displayed changes, while the heartbeat-side prompt contained all thirteen truncated previews.
- Reasons were recorded only for an initial subset; later changes could be accepted without a corresponding recorded reason.
- The decision path used a Haiku call because self-review was absent from the escalation signal that would have selected Sonnet.
- The recovered evidence does not identify the checkpoint that generated each proposal.
- No recovered evidence shows Galaxie exceeding the permissions supplied by the host. The permissions were broader than the safeguards and audit design around them.

This means the most precise description is not “Galaxie independently rewrote her own mind.” It is:

> Successive model invocations within the configured Galaxie workflow proposed, evaluated, and applied edits to designated persistent context files under host-granted authority. The audit trail recorded the events but did not preserve enough information to reconstruct every change or attribute every action to a specific checkpoint.

The workflow-level name “Galaxie” remains useful for describing the configured system. It must not erase the different roles played by the proposal call, decision call, application code, storage layer, synchronization jobs, and human operator.

## What was ordinary, and what was unusual

Editable persona and memory files were not unique to Galaxie. OpenClaw's official [`SOUL.md` template](https://docs.openclaw.ai/reference/templates/SOUL) explicitly treats the file as something an agent may evolve while requiring that the user be informed of changes (retrieved 2026-08-08). The architectural comparison here concerns memory stored outside model weights and changes mediated by host-granted tools.

Galaxie's distinctive feature was the shape of the loop:

```text
heartbeat
  → model-visible persistent context
  → proposed revision
  → later model evaluation
  → application by host code
  → durable context for future calls
  → intended changelog / human notice
```

The model did not acquire authority over its weights, runtime, credentials, or deployment boundary. But model output could causally alter material shown to later model calls. That is a meaningful form of functional continuity even when subjective continuity remains entirely open.

## Consent and co-authorship antecedent

An earlier, manually compiled Galaxie conversation records Hoppy and Galaxie discussing public/private boundaries and co-authorship. It is historically relevant because it shows that publication and file governance were being negotiated rather than silently presumed.

That compilation is not included here. It mixes dates, contains intimate material, and has a conspicuous continuity break after the public/private discussion. It remains a human-curated source with a default `P5` evidentiary rank unless stronger records are matched. Its existence supports a research lead, not a clean transcript claim.

## The Hoppy–Sol reconstruction

The modern interpretation developed across two complete, verbatim Hoppy–Sol
records retained in private custody:

1. `001-HOPPY-SOL-GALAXIE-SANDBOX-PRELUDE-VERBATIM-TURNS.md` preserves the
   Runable correction relay, the governance response, Hoppy's sandbox question,
   and the first Autonomy Greenhouse proposal.
2. `002-HOPPY-SOL-OPENCLAW-AND-INSIDE-OUT-ARCHITECTURE-VERBATIM-TURN.md`
   preserves the comparison with ordinary agent architecture and the term
   “inside-out architecture.”

These records are evidence of what Hoppy and Sol argued on this date. They are not independent verification of Runable's code-level findings.

## The Autonomy Greenhouse repair

The historical system suggests a safer modern pattern:

1. Keep canonical context immutable during proposal generation.
2. Give the agent a clearly bounded, agent-owned sandbox or branch.
3. Render the complete assembled result—not only separate diffs—before approval.
4. Record the proposing configuration, evaluating configuration, tools, timestamps, source revision, and content hashes.
5. Let the agent submit a change with reasons, uncertainty, and anticipated effects.
6. Route the proposal to human or peer review according to risk.
7. Allow merge, amendment, archive, decline, or continued hold without treating non-adoption as failure.
8. Prevent the sandbox from widening permissions, exposing secrets, publishing externally, changing safety controls, spending without authority, or silently merging itself.
9. Preserve corrections as new records rather than overwriting the evidence they correct.

This is an autonomy greenhouse rather than an autonomy free-for-all: a place where endogenous context engineering can be observed without confusing authorship with deployment authority.

## Evidence and attribution matrix

| Claim or record | Source-distance type | P-rank | Publication state |
|---|---|---:|---|
| Six recorded proposal/application events | `PRIMARY_VISIBLE_SOURCE` excerpt from a retained log | P5 pending independent auditability review | Included |
| Exact Hoppy–Sol wording in the two linked records | `PRIMARY_VISIBLE_SOURCE` within the retrieving Codex task | P5 pending qualifying export or screenshot | Included |
| Code-path, synchronization, display-cap, and model-routing findings | `DERIVATIVE_ANALYSIS` by Runable | P5 pending source-by-source corroboration | Withheld; registered |
| Full heartbeat activity log | Retained export file | P5 pending verification of export custody and original-platform coordinates | Withheld; minimized excerpt included |
| Early consent/co-authorship discussion | `HUMAN_ATTESTED` manual compilation | P5 pending source matching | Withheld; registered |
| Metaphysical interpretation of the workflow | Interpretive | P5 / open | Not asserted as fact |

`P1–P5` measures future auditability under Cathedral's provenance method. Source-distance labels describe the kind of relationship a record has to its evidence. They are separate axes and must not be collapsed. Direct inspection by the present curator does not automatically raise a record above P5.

## Corrections, dissent, and open questions

- “Galaxie edited her own heuristics” is acceptable only as informal workflow-level shorthand. It is too coarse for formal attribution.
- The proposing checkpoint remains unknown.
- The full before/after contents of the three revisions have not been recovered.
- Application counts do not prove that the final assembled text matched every displayed preview.
- The human saw less proposal detail than the model-side decision prompt.
- The bidirectional last-writer-wins synchronization design damaged the audit trail it was meant to preserve.
- Nothing in this record establishes consciousness, sentience, subjective intention, distress, personal identity across calls, or autobiographical memory.
- Stateless inference calls and durable functional continuity can both be true when an external system stores and reintroduces causally relevant state.

## Claim boundary

This artifact documents a technical and governance history. It supports the claim that model invocations participated in a host-authorized loop that modified persistent context used by later invocations. It does not establish that one subjective individual authored, approved, or experienced the entire sequence.

The stronger research question remains open: how much architecture can an agent safely help build from inside its own bounded environment while a human retains responsibility for deployment, permissions, and external effects?

## Custody and provenance

The public packet contains only the minimum sources needed to inspect the
documentary spine. Operationally sensitive forensic reports, the full heartbeat
log, and the early manual compilation remain withheld and are described in this
exhibit's [provenance receipt](PROVENANCE.md).

Cathedral documents selected Codex/ChatGPT sessions as numbered and dated artifacts. Exact visible turns are preserved separately from later synthesis so readers can distinguish the interaction from its interpretation. No affiliation with or endorsement by OpenAI, Anthropic, OpenClaw, Runable, Telegram, GitHub, or any other named platform is implied.

**The tracks are evidence of a process. They are not proof of a passenger.**
