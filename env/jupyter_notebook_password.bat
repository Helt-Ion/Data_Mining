@echo off

set VENV_DIR=%~dp0\venv
set PYTHON="%VENV_DIR%\python"

:: Put your codes here

%PYTHON% -m jupyter notebook password

@echo on
pause
