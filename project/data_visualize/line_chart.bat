@echo off

set VENV_DIR=%~dp0..\..\env\venv
set PYTHON="%VENV_DIR%\python"

:: Put your codes here

%PYTHON% -m src.line_chart

@echo on
pause
