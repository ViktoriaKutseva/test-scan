"""feature_flags service."""

from __future__ import annotations

class FeatureFlags:
    def execute(self, payload: dict) -> dict:
        return {'ok': True, 'payload': payload}
