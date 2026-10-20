@echo off
setlocal
cd /d "%~dp0"
title HowZit - voice samples
if not exist ".venv\Scripts\activate.bat" (
  echo Run setup.bat first.
  pause
  exit /b 1
)
call ".venv\Scripts\activate.bat"
rem Optional: drag an episode folder onto this file to hear that episode's first lines.
python -m studio.voices %1
if exist voice-tests start "" voice-tests
pause
