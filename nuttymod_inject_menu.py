"""Recovered manifest entrypoint for the missing NuttyMod Inject Menu source.

The original optional installer UI was removed, but verification scripts still
load this exact path. This compatibility entrypoint satisfies the manifest API
without changing game files or installing payloads.
"""

from __future__ import annotations


def register(api):
    api.about(
        name="NuttyMod Inject Menu Compatibility",
        version="1.2.1-recovered",
        author="NuttyMod Studios",
        description=(
            "Recovered manifest entrypoint. NReplay provides its own replay, "
            "scene-import, and recovery menus."
        ),
    )
