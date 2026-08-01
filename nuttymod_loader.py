"""NuttyMod loader for The Cube Beta.

Run this file from the repository root. It discovers Python add-ons inside the
`addons` folder. Each add-on must expose `ADDON_INFO` and `run()`.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path
from types import ModuleType

ADDONS_DIR = Path(__file__).parent / "addons"


def load_addons() -> list[ModuleType]:
    addons: list[ModuleType] = []
    ADDONS_DIR.mkdir(exist_ok=True)

    for path in sorted(ADDONS_DIR.glob("*.py")):
        if path.name.startswith("_"):
            continue

        spec = importlib.util.spec_from_file_location(path.stem, path)
        if spec is None or spec.loader is None:
            print(f"Could not load {path.name}")
            continue

        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if not hasattr(module, "ADDON_INFO") or not callable(getattr(module, "run", None)):
            print(f"Skipped {path.name}: missing ADDON_INFO or run()")
            continue

        addons.append(module)

    return addons


def main() -> None:
    addons = load_addons()
    if not addons:
        print("No NuttyMod add-ons were found in the addons folder.")
        return

    print("NuttyMod Loader - The Cube Beta")
    print("================================")
    for index, addon in enumerate(addons, start=1):
        info = addon.ADDON_INFO
        print(f"{index}. {info.get('name', addon.__name__)} v{info.get('version', '?')}")
        print(f"   {info.get('description', '')}")

    while True:
        choice = input("Choose an add-on number, or Q to quit: ").strip().lower()
        if choice == "q":
            return
        try:
            selected = addons[int(choice) - 1]
        except (ValueError, IndexError):
            print("Invalid selection.")
            continue

        selected.run()
        return


if __name__ == "__main__":
    main()
