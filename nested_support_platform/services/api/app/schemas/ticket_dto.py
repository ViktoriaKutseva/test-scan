"""ticket_dto schema."""

from __future__ import annotations

class TicketDto(dict):
    """Serializable support ticket payload."""

    @classmethod
    def from_payload(cls, payload: dict) -> "TicketDto":
        ticket_id = str(payload.get("id", "")).strip()
        subject = " ".join(str(payload.get("subject", "")).split())
        if not ticket_id or not subject:
            raise ValueError("Ticket payload requires id and subject")

        priority = str(payload.get("priority", "medium")).strip().lower()
        status = str(payload.get("status", "new")).strip().lower()
        if priority not in {"low", "medium", "high", "urgent"}:
            raise ValueError("Ticket priority is invalid")
        if status not in {"new", "open", "pending", "resolved", "reopened", "closed"}:
            raise ValueError("Ticket status is invalid")

        sla_hours = {"low": 72, "medium": 24, "high": 8, "urgent": 2}[priority]

        return cls(
            {
                "id": ticket_id,
                "subject": subject,
                "description": str(payload.get("description", "")).strip(),
                "customer_id": str(payload.get("customer_id", "")).strip(),
                "assignee_id": str(payload.get("assignee_id", "")).strip() or None,
                "priority": priority,
                "status": status,
                "tags": sorted({str(tag).strip().lower() for tag in payload.get("tags", []) if str(tag).strip()}),
                "sla_target_hours": sla_hours,
            }
        )
