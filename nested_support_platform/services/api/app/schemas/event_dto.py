"""event_dto schema."""

from __future__ import annotations

from datetime import datetime, timezone

class EventDto(dict):
    """Serializable event payload for audit/event streams."""

    @classmethod
    def from_payload(cls, payload: dict) -> "EventDto":
        event_type = str(payload.get("type", "")).strip().lower()
        aggregate_id = str(payload.get("aggregate_id", "")).strip()
        if not event_type or not aggregate_id:
            raise ValueError("Event payload requires type and aggregate_id")

        occurred_at = payload.get("occurred_at")
        if not occurred_at:
            occurred_at = datetime.now(timezone.utc).isoformat()

        return cls(
            {
                "id": str(payload.get("id", "")).strip() or f"evt_{aggregate_id}_{event_type}",
                "type": event_type,
                "aggregate_id": aggregate_id,
                "occurred_at": str(occurred_at),
                "payload": dict(payload.get("payload", {})),
                "source": str(payload.get("source", "api")).strip().lower(),
            }
        )
