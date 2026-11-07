@echo off
title VALIXIS 24/7 Agent Mesh
cd /d "%~dp0..\ai_agents"
echo Starting VALIXIS 24/7 Outbound & Inbound Autonomous Mesh...
python run_mesh_247.py
pause
