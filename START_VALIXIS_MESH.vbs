Set WshShell = CreateObject("WScript.Shell")
strDir = "C:\Users\nagas\Documents\antigravity\resilient-heisenberg\ai_agents"
WshShell.CurrentDirectory = strDir
WshShell.Run "python run_mesh_247.py", 0, False
Set WshShell = Nothing
