"""dedupe_service service."""

from __future__ import annotations

import hashlib
import json

from packages.domain.value_objects.idempotency_key import IdempotencyKey

class DedupeService:
    def __init__(self) -> None:
        self._seen_fingerprints: set[str] = set()

    @staticmethod
    def _fingerprint(payload: dict) -> str:
        canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(canonical.encode("utf-8")).hexdigest()

    def execute(self, payload: dict) -> dict:
        key = IdempotencyKey(str(payload.get("idempotency_key", "")))
        fingerprint = self._fingerprint(payload)
        already_seen = fingerprint in self._seen_fingerprints
        if not already_seen:
            self._seen_fingerprints.add(fingerprint)

        return {
            "ok": True,
            "idempotency_key": str(key),
            "is_duplicate": already_seen,
            "fingerprint": fingerprint,
            "payload": payload,
        }
