"""search_dto schema."""

from __future__ import annotations

class SearchDto(dict):
    """Serializable search criteria payload with normalized options."""

    @classmethod
    def from_payload(cls, payload: dict) -> "SearchDto":
        query = " ".join(str(payload.get("query", "")).split())
        if not query:
            raise ValueError("Search query must not be empty")

        page = max(1, int(payload.get("page", 1)))
        page_size = min(100, max(1, int(payload.get("page_size", 25))))
        sort_by = str(payload.get("sort_by", "updated_at")).strip().lower()
        direction = str(payload.get("direction", "desc")).strip().lower()
        if direction not in {"asc", "desc"}:
            raise ValueError("Search direction must be 'asc' or 'desc'")

        return cls(
            {
                "query": query,
                "page": page,
                "page_size": page_size,
                "sort_by": sort_by,
                "direction": direction,
                "filters": dict(payload.get("filters", {})),
            }
        )
