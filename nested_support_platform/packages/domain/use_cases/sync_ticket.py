"""sync_ticket use case."""

from __future__ import annotations

def run(command: dict) -> dict:
    current = dict(command.get("current", {}))
    incoming = dict(command.get("incoming", {}))
    if not current and not incoming:
        raise ValueError("sync_ticket requires current and/or incoming payload")

    merged = {**current, **incoming}
    merged["id"] = str(merged.get("id", "")).strip() or str(current.get("id") or incoming.get("id") or "")
    if not merged["id"]:
        raise ValueError("sync_ticket requires an id")

    changed_fields = sorted(
        {
            field
            for field in merged
            if current.get(field) != merged.get(field)
        }
    )

    return {
        "use_case": "sync_ticket",
        "ticket": merged,
        "changed_fields": changed_fields,
        "is_noop": not changed_fields,
    }
