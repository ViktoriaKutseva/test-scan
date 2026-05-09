"""rebuild_embeddings handler."""

from __future__ import annotations

def run(payload: dict) -> dict:
    return {"handler": "rebuild_embeddings", "payload": payload, "retry": True}
