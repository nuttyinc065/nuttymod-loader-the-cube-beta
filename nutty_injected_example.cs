// NuttyMod C# manifest example. The existing runtime compiles/runs this file
// through csc or a temporary dotnet project and reads the final JSON line.
using System;

Console.WriteLine("{\"name\":\"Nutty Injected C#\",\"version\":\"1.0.0\",\"author\":\"NuttyMod Studios\",\"description\":\"C# payload installed through the NuttyMod Mods folder.\",\"shapes\":[{\"name\":\"C# Prism\",\"kind\":\"polygon\",\"sides\":6,\"size\":35,\"color\":[92,196,255],\"weight\":0.9}],\"events\":[{\"name\":\"Managed Surge\",\"duration\":7,\"wind\":420,\"gravity_scale\":0.55,\"spawn_count\":6,\"banner\":\"NuttyMod C# runner connected!\",\"color\":[92,196,255]}]}");
