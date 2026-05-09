"""report_rollup handler."""

from __future__ import annotations

def run(payload: dict) -> dict:
    return {"handler": "report_rollup", "payload": payload, "retry": True}
