@echo off

set VENV_DIR=%~dp0..\..\env\venv
set PYTHON="%VENV_DIR%\python"

:: Put your codes here

%PYTHON% -m src.data_read

@echo on
pause
