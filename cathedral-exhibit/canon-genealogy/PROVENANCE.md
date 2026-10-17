# Canon Genealogy — Provenance Receipt

## Verification update — 2026-10-17

The public Git artifact uses LF line endings. Its SHA-256 is:

```text
989611de5fc187b7576319462e3fcea29e7c79b1faf8d68713eddffce1789c6a
```

The earlier `BAA755...` checksum below matches the same public text encoded
with CRLF line endings. Both values are recorded in
[`checksums.json`](../../checksums.json). The original receipt remains below
as a dated record of the earlier source-copy verification.

This update verifies the public artifact bytes and the line-ending
relationship. The archive file retains its current Git bytes. Its checkout
uses LF through `.gitattributes`.

From the repository root, run:

```sh
python3 scripts/verify-checksums.py
```

The check hashes the file exactly as read, then checks its CRLF representation
against the historical value. GitHub Actions runs the same check on pushes
and pull requests.

## Exhibit status

- Exhibit: `Cathedral Exhibit / Canon Genealogy`
- Discoball publication date: 2026-10-17
- Source relationship: `CURATED_SELECTION`
- Verification rank: `P3 — Source file located`
- Fidelity: exact byte-for-byte copy of the identified Cathedral file
- Transformation: placement changed; file body unchanged
- Historical status: previously published in Cathedral while that repository
  was publicly viewable

## Preserved artifact

- Discoball path: `cathedral-exhibit/canon-genealogy/CANON_GENEALOGY.md`
- Cathedral source path: `CANON_GENEALOGY.md`
- Source commit: `a5f9b56475eacf672e8ad293ffc1c32e1a430d2e`
- Source commit date: `2026-07-23T10:45:01+01:00`
- Source commit subject: `Fix formatting issue in CANON_GENEALOGY.md`
- Historical SHA-256 (CRLF representation; see the dated update above):
  `BAA755E156EC5E02C163FC35A8C8E394C5BEA26055AB12DFAFCB0CC3207F5A7E`
- Body transformation: none

The source worktree copy and the file rendered from the identified source
commit produced the same SHA-256 before publication to Discoball.

## Source and interpretation limits

This receipt verifies the relationship between the displayed artifact and the
identified Cathedral repository file. It does not independently verify every
historical claim, interpretation, external project description, quotation, or
attribution inside the genealogy.

The document distinguishes original sources, Hoppy's adaptations, and later
contributor extensions where its historical authors recorded those
distinctions. Readers should still follow its links to upstream sources when
precise wording or present-day accuracy matters.

Publication here does not:

- imply endorsement by Ben Roy or any other person or project cited;
- claim exclusive ownership of the metaphors or ordinary terms discussed;
- establish consciousness, continuous model identity, or provider
  affiliation;
- make other Cathedral records public; or
- convert historical explanatory language into current governance.

Corrections or stronger provenance evidence should be added through visible,
dated revision rather than silently rewriting the preserved artifact.
