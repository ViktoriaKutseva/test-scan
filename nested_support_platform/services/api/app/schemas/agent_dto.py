"""agent_dto schema."""

from __future__ import annotations

from services.api.app.schemas.error_dto import ErrorDto

class AgentDto(dict):
    """Serializable support agent payload."""

    REQUIRED_FIELDS = ("id", "name")

    @classmethod
    def from_payload(cls, payload: dict) -> "AgentDto":
        missing = [field for field in cls.REQUIRED_FIELDS if not payload.get(field)]
        if missing:
            raise ValueError(ErrorDto.build(code="invalid_agent", message="Missing agent fields", details={"missing": missing})["message"])

        return cls(
            {
                "id": str(payload["id"]).strip(),
                "name": str(payload["name"]).strip(),
                "email": str(payload.get("email", "")).strip().lower(),
                "skills": sorted({str(skill).strip().lower() for skill in payload.get("skills", []) if str(skill).strip()}),
                "online": bool(payload.get("online", False)),
            }
        )
