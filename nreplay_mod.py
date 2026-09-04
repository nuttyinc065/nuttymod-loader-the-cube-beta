"""NuttyMod entrypoint for NReplay.

This small bootstrap stays at ``addons/mods`` so the Cube's existing Python
mod scanner can find NReplay.  The implementation lives in the ``nreplay``
package and is also bundled into the .nmod/.nuttymod distributions.
"""

from __future__ import annotations

from pathlib import Path
import sys


_MODS_DIR = Path(__file__).resolve().parent
if str(_MODS_DIR) not in sys.path:
    sys.path.insert(0, str(_MODS_DIR))

from nreplay.nreplay_loader import bootstrap, register as _register


bootstrap()


def register(api):
    """Register NReplay with NuttyMod's manifest API."""
    return _register(api)
