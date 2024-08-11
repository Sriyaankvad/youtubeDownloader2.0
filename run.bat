@echo off
:: Get the directory of the script
set SCRIPT_DIR=%~dp0

echo Running on Windows
python "%SCRIPT_DIR%main.py"

:: Keep the command prompt window open after the script executes
pause

