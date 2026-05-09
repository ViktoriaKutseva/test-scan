"""customer_dto schema."""

from __future__ import annotations

class CustomerDto(dict):
    """Serializable customer profile payload."""

    @classmethod
    def from_payload(cls, payload: dict) -> "CustomerDto":
        customer_id = str(payload.get("id", "")).strip()
        email = str(payload.get("email", "")).strip().lower()
        if not customer_id or not email:
            raise ValueError("Customer payload requires id and email")

        mrr = float(payload.get("monthly_recurring_revenue", 0))
        segment = "enterprise" if mrr >= 5000 else "standard"

        return cls(
            {
                "id": customer_id,
                "email": email,
                "name": str(payload.get("name", "")).strip(),
                "monthly_recurring_revenue": mrr,
                "segment": segment,
                "tags": sorted({str(tag).strip().lower() for tag in payload.get("tags", []) if str(tag).strip()}),
            }
        )
