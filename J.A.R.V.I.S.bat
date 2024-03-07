@echo off
start cmd /c "wsl -- bash -c 'ollama run mistral'"
start cmd /c "cd /d "%~dp0" && %USERPROFILE%\AppData\Local\Programs\Python\Python311\python.exe "jarvis.py"