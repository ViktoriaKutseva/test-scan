"""create_ticket use case."""

from __future__ import annotations

from datetime import datetime, timezone
import uuid

from packages.domain.value_objects.priority import Priority
from packages.domain.value_objects.status import Status

def run(command: dict) -> dict:
    subject = " ".join(str(command.get("subject", "")).split())
    if not subject:
        raise ValueError("create_ticket requires a non-empty subject")

    ticket_id = str(command.get("id") or f"tkt_{uuid.uuid4().hex[:12]}")
    priority = Priority(str(command.get("priority", "medium")))
    status = Status(str(command.get("status", "new")))

    return {
        "use_case": "create_ticket",
        "ticket": {
            "id": ticket_id,
            "subject": subject,
            "description": str(command.get("description", "")).strip(),
            "customer_id": str(command.get("customer_id", "")).strip(),
            "priority": str(priority),
            "status": str(status),
            "created_at": datetime.now(timezone.utc).isoformat(),
        },
        "meta": {"source": str(command.get("source", "api")).strip().lower()},
    }
