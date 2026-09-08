"""Route the packaged game's runtime menu call through Dev confirmation."""

from __future__ import annotations

import sys
from typing import Any, Callable


VERSION = "1.0.0"


def _find_runtime() -> dict[str, Any] | None:
    for module in tuple(sys.modules.values()):
        if module is None:
            continue
        manager_type = getattr(module, "AddonManager", None)
        namespace = getattr(getattr(manager_type, "reload", None), "__globals__", None)
        if (
            isinstance(namespace, dict)
            and "_modified_main_menu" in namespace
            and "_GAME_MODULE" in namespace
        ):
            return namespace
    return None


def _closed_value(function: Callable[..., Any], name: str) -> Any | None:
    closure = getattr(function, "__closure__", None) or ()
    names = getattr(getattr(function, "__code__", None), "co_freevars", ())
    try:
        index = names.index(name)
    except ValueError:
        return None
    return closure[index].cell_contents if index < len(closure) else None


def _install(runtime: dict[str, Any]) -> bool:
    game_module = runtime.get("_GAME_MODULE")
    game_class = getattr(game_module, "GameApp", None)
    confirmation_menu = getattr(game_class, "main_menu", None)
    if game_class is None or not callable(confirmation_menu):
        return False
    if not getattr(confirmation_menu, "_nuttymod_dev_confirmation", False):
        return False

    runtime["_modified_main_menu"] = confirmation_menu
    game_class.main_menu = confirmation_menu

    normal_menu = _closed_value(confirmation_menu, "normal_menu")
    patch_namespace = getattr(normal_menu, "__globals__", None)
    if isinstance(patch_namespace, dict) and "_modified_main_menu" in patch_namespace:
        patch_namespace["_modified_main_menu"] = confirmation_menu

    run_method = getattr(game_class, "run", None)
    run_namespace = getattr(run_method, "__globals__", None)
    if isinstance(run_namespace, dict) and "_modified_main_menu" in run_namespace:
        run_namespace["_modified_main_menu"] = confirmation_menu

    runtime["_NUTTYMOD_LIVE_MENU_FIX"] = VERSION
    return True


def register(api: Any) -> None:
    runtime = _find_runtime()
    installed = _install(runtime) if runtime is not None else False
    api.about(
        name="NuttyMod Live Menu Fix",
        version=VERSION,
        author="NuttyMod Studios",
        description=(
            "Routes packaged-game menu calls through Developer confirmation."
            if installed
            else "Developer confirmation was not ready during this reload."
        ),
    )
