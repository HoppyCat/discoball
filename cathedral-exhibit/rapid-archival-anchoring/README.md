# Rapid Archival Anchoring

Rapid archival anchoring was an early Cathedral method for preserving
time-sensitive human–AI records before every source could be fully verified.
Its governing sentence was deliberately modest:

> This does not prove authenticity. It strengthens provenance.

The method paired quick placement in version control with explicit labels for
source platform, source window, capture delay, processing, verification state,
and evidence still needed. It allowed uncertain material to be retained
without prematurely treating it as canon.

The [historical standard](historical-standard.md) is reproduced byte for byte
from Cathedral's former public `Needs Verification` README. It includes:

- the original definition;
- a reusable YAML capture header;
- the early verification-status ladder; and
- the rule of thumb to preserve uncertain material, label it, and verify it
  later.

## What anchoring can establish

Rapid capture into version control can document that a particular file was
committed no later than a recorded commit time. When capture delay, processor,
and custody are accurately documented, it can also make later substitution or
silent rewriting easier to detect.

Anchoring alone does not prove:

- that copied text matches the original platform record;
- that a named speaker, model, or window produced it;
- that timestamps written inside the file are accurate;
- that omitted material does not exist;
- that a model-generated summary is a verbatim transcript; or
- that the material is cleared for canon, quotation, transformation, or
  republication.

Screenshots, direct exports, stable source links, hashes, platform records, and
verbatim comparison can strengthen different parts of the chain.

## Historical ladder versus the current provenance scale

The historical `verification_status` values—`raw`, `timestamp-anchored`,
`formatted-not-verified`, `screenshot-verified`, `link-verified`, and
`canon-candidate`—described workflow state. They are not equivalent to
Discoball's present [P1–P5 verification scale](../../provenance/README.md).

In particular:

- `timestamp-anchored` recorded timing evidence, not authenticity;
- `formatted-not-verified` openly marked transformation without comparison;
- `canon-candidate` meant eligible for later consideration, not canonized; and
- no historical status supplied publication permission by itself.

## Present-day use

The original definition referred to a **public** version-controlled archive
because Cathedral was public at the time. Cathedral is now private. The method
can still be used in private custody, but a private commit does not create the
same independently visible public timestamp. Any present use should say which
kind of repository received the record.

Rapid archival anchoring is best understood as an intake discipline:

> Preserve early. Label uncertainty. Keep transformations visible. Verify
> later. Never let the existence of an archive entry make a stronger claim
> than its evidence can carry.

