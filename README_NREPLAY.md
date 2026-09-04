# NReplay Mod 1.0.2

NReplay is a Replay Mod-inspired implementation made specifically for **The
Cube Beta Fall Edition** and its NuttyMod 1.4.2 runtime. It does not copy or
run the Minecraft Replay Mod's Java code; it ports the familiar record,
timeline, recover, and scene workflow to the Cube's Python/Pygame state model.

## Install and open

The development install is already arranged for this Cube mods folder:

- `nreplay_mod.py` is the normal Python bootstrap.
- `nreplay/` contains the recorder, modified loader, menus, and module system.
- `nreplay.nuttymod` is the standard ZIP-compatible NuttyMod package.
- `nreplay.nmod` is the alias package supported by the modified loader.

After installing or upgrading, fully close and reopen the Cube once, then use
**Add-ons → Reload**. Enter the new **NReplay** landing menu. The
package and Python bootstraps are idempotent, so loading more than one package
form will not install duplicate game hooks.

## Controls

- **Record Next Run** arms automatic capture for the next simulation.
- **F8** starts or stops capture while a simulation is running.
- **F7** adds a marker to the recovery journal.
- **F9** opens Replay Studio after the current simulation exits.
- In playback: **Space** pauses, **Left/Right** seek, **Up/Down** change speed,
  **Home/End** jump, and **Esc** returns.

Recordings are stored under `nreplay_data/replays`. Capture first writes an
append-only file under `nreplay_data/recovery`; **Recover Recording** rebuilds
the newest journal and ignores a crash-torn final JSON line.

## Scenes and custom modules

NReplay imports both `.nscene` and the requested legacy/misspelled `.nsecne`
extension. A scene is UTF-8 JSON and can either embed frames or reference a
`.nreplay` file:

```json
{
  "format": "nreplay-scene",
  "format_version": 1,
  "name": "My Cut",
  "source": "session.nreplay",
  "modules": [
    {
      "id": "nreplay.cinematic-tint",
      "options": {"color": [80, 190, 255], "strength": 0.25}
    }
  ]
}
```

Custom module code lives only in `nreplay/modules/*.py`. A scene selects a
registered `MODULE_ID`; it cannot load an arbitrary path or embed executable
code. Modules are still Python code, so install modules only from creators you
trust. See `nreplay/modules/cinematic_tint.py` and the two files in `examples/`.

## Companion languages and tools

- `tools/Program.cs` builds as a .NET 8 validator/recovery utility.
- `tools/nreplay_scene.rb` converts JSON snapshots to `.nscene`.
- `tools/nreplay_tools.batch` provides build, test, and validate commands. A
  `.bat` launcher is included because Windows does not normally associate the
  custom `.batch` suffix with `cmd.exe`.

Run `tools\nreplay_tools.bat build` to rebuild packages and the C# utility, or
`tools\nreplay_tools.bat test` for Python tests.

## Format notes          

An `.nreplay` is a bounded ZIP container containing `manifest.json` and
`frames.ndjson`. The Python and C# readers reject traversal paths, encrypted
members, oversized archives, oversized frames, and unsupported format
versions. Replay capture records render-state snapshots; it does not inject
code into the game process or rewrite the game executable.
