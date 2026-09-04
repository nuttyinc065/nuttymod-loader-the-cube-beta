"""Enable both conventional .cs and legacy .c# files in stable Mods."""

from __future__ import annotations

import sys
from typing import Any


def _runtime() -> dict[str, Any] | None:
    for module in tuple(sys.modules.values()):
        if module is None:
            continue
        manager_type = getattr(module, "AddonManager", None)
        namespace = getattr(getattr(manager_type, "reload", None), "__globals__", None)
        if isinstance(namespace, dict) and "SUPPORTED_MOD_SUFFIXES" in namespace:
            return namespace
    return None


def register(api: Any) -> None:
    runtime = _runtime()
    if runtime is not None:
        for key in (
            "SUPPORTED_MOD_SUFFIXES",
            "SUPPORTED_ADDON_SUFFIXES",
            "EXTRA_ADDON_SUFFIXES",
        ):
            runtime[key] = set(runtime.get(key, set())) | {".cs", ".c#"}
    api.about(
        name="NuttyMod C# Compatibility Bridge",
        version="1.0.0",
        author="NuttyMod Studios",
        description="Enables .cs and legacy .c# stable Mods through the existing C# runner.",
    )
