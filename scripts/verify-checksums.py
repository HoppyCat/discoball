"""Verify the public Git bytes and their recorded CRLF representation."""

import hashlib
import json
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / "checksums.json").read_text(encoding="utf-8"))
failures = []

for entry in manifest["files"]:
    path = root / entry["path"]
    try:
        content = path.read_bytes()
    except OSError as error:
        failures.append(f"{entry['path']}: {error}")
        continue
    actual = hashlib.sha256(content).hexdigest()
    if actual != entry["sha256_lf"]:
        failures.append(
            f"{entry['path']}: expected Git LF SHA-256 {entry['sha256_lf']}, got {actual}"
        )
        continue
    crlf = content.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")
    historical = hashlib.sha256(crlf).hexdigest()
    if historical != entry["historical_sha256_crlf"]:
        failures.append(f"{entry['path']}: historical CRLF SHA-256 mismatch: {historical}")
        continue
    print(f"OK {entry['path']}: Git LF and historical CRLF checksums match")

if failures:
    print("\n".join(failures), file=sys.stderr)
    raise SystemExit(1)
