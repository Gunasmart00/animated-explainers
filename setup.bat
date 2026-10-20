@echo off
setlocal
cd /d "%~dp0"
title HowZit animated explainers - setup
echo ================================================
echo  HowZit animated explainers: one-time setup
echo ================================================
echo.

rem --- Python ---
set "PY="
where py >nul 2>nul && set "PY=py -3"
if not defined PY (
  where python >nul 2>nul && set "PY=python"
)
if not defined PY (
  echo Python was not found. Install Python 3.11 or newer from python.org
  echo ^(tick "Add python.exe to PATH"^), then double-click setup.bat again.
  pause
  exit /b 1
)
%PY% --version

rem --- ffmpeg ---
where ffmpeg >nul 2>nul
if not errorlevel 1 (
  echo ffmpeg: found
) else (
  if exist "%LOCALAPPDATA%\Microsoft\WinGet\Packages\Gyan.FFmpeg*" (
    echo ffmpeg: already installed by winget
  ) else (
    echo.
    echo Installing ffmpeg with winget. If it asks you to accept the terms, type Y and press Enter.
    winget install --id Gyan.FFmpeg -e
  )
)

rem --- Python environment and packages ---
if not exist ".venv\Scripts\python.exe" (
  echo.
  echo Creating the Python environment in .venv ...
  %PY% -m venv .venv
)
call ".venv\Scripts\activate.bat"
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
if errorlevel 1 (
  echo.
  echo Installing the Python packages failed. Check your internet connection and run setup.bat again.
  pause
  exit /b 1
)

rem --- Voice samples ---
echo.
echo ================================================
echo  Making voice samples (needs internet) ...
echo ================================================
python -m studio.voices
if exist voice-tests start "" voice-tests

rem --- Test render ---
echo.
echo ================================================
echo  Test render of the sample episode (draft, about a minute) ...
echo ================================================
python -m studio.build episodes\microwave-heating --draft
if exist "episodes\microwave-heating\output\microwave-heating_howzit_draft.mp4" start "" "episodes\microwave-heating\output\microwave-heating_howzit_draft.mp4"

echo.
echo Done. Listen to the voices in the voice-tests folder that just opened,
echo then tell Claude which one you like (or set it in presets\explainer.yaml).
echo The draft video is half size on purpose: it only checks voice and timing.
pause
