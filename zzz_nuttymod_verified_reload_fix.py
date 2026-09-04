"""Bind the four-reload trigger to NuttyMod 1.4.2's settings namespace."""

from __future__ import annotations

import sys
from typing import Any, Callable


VERSION = "1.1.0"
REQUIRED_RELOADS = 4


def _find_runtime() -> dict[str, Any] | None:
    for module in tuple(sys.modules.values()):
        if module is None:
            continue
        manager_type = getattr(module, "AddonManager", None)
        namespace = getattr(getattr(manager_type, "reload", None), "__globals__", None)
        if (
            isinstance(namespace, dict)
            and "ADDONS_DIR" in namespace
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


def _advance(app: Any) -> tuple[int, bool]:
    count = int(getattr(app, "_nuttymod_verified_reload_count", 0)) + 1
    triggered = count >= REQUIRED_RELOADS
    setattr(app, "_nuttymod_verified_reload_count", 0 if triggered else count)
    return count, triggered


def _gate(app: Any, runtime: dict[str, Any]) -> str:
    pygame = runtime["_pygame"]()
    while True:
        width, height = app.screen.get_size()
        app.screen.fill((13, 48, 78))
        large = getattr(app, "large", pygame.font.SysFont("segoeui", 42, bold=True))
        small = getattr(app, "small", pygame.font.SysFont("segoeui", 18))
        tiny = getattr(app, "tiny", pygame.font.SysFont("segoeui", 14))
        heading = large.render("DEVELOPER MODE", True, (248, 252, 255))
        app.screen.blit(heading, heading.get_rect(center=(width // 2, height // 2 - 95)))
        prompt = small.render("Press ESC to enable Developer Mode", True, (92, 232, 184))
        app.screen.blit(prompt, prompt.get_rect(center=(width // 2, height // 2 - 25)))
        normal = tiny.render("Press ENTER to continue normally", True, (184, 232, 240))
        app.screen.blit(normal, normal.get_rect(center=(width // 2, height // 2 + 25)))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_ESCAPE:
                setattr(app, "_nuttymod_developer_mode", True)
                setattr(app, "_nuttymod_verified_reload_count", 0)
                notify = getattr(app, "notify", None)
                if callable(notify):
                    notify("Developer Mode enabled. Verify Add-ons & Mods four times.", 6)
                return "continue"
            if event.key in {pygame.K_RETURN, pygame.K_KP_ENTER}:
                return "continue"
        app.clock.tick(60)


def _install(runtime: dict[str, Any]) -> None:
    """Compatibility shim; the real button hook wraps _verification_screen."""
    runtime["_NUTTYMOD_VERIFIED_RELOAD_FIX"] = VERSION


def register(api: Any) -> None:
    runtime = _find_runtime()
    if runtime is not None:
        _install(runtime)
    api.about(
        name="NuttyMod Verified Reload Trigger",
        version=VERSION,
        author="NuttyMod Studios",
        description="Binds Developer Mode's fourth reload to the verified settings action.",
    )
