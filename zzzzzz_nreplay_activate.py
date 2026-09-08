"""Final NReplay activation pass after NuttyMod's existing menu fix mods."""

from __future__ import annotations

import importlib
from pathlib import Path
import sys


_MODS_DIR = Path(__file__).resolve().parent
if str(_MODS_DIR) not in sys.path:
    sys.path.insert(0, str(_MODS_DIR))

from nreplay import nreplay_loader as _cached_loader
from nreplay import recording as _cached_recording


# Add-ons Reload keeps normal Python packages in sys.modules. Reload the
# readable NReplay feature layer so fixes apply without requiring a game
# reinstall, then rebind the final menu chain selected by NuttyMod.
importlib.reload(_cached_recording)
_loader = importlib.reload(_cached_loader)
_loader.bootstrap()


def register(api):
    _loader.bootstrap()
    api.about(
        name="NReplay Runtime Activator",
        version="1.0.2",
        author="NReplay Project",
        description="Final menu binding and reload activation for NReplay.",
    )
