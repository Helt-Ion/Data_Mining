@echo off

set VENV_DIR=%~dp0\venv
set PYTHON="%VENV_DIR%\python"
set JUPYTER="%VENV_DIR%\Scripts\jupyter"

:: Put your codes here

%JUPYTER% notebook

@echo on
pause
