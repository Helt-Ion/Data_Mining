@echo off

set VENV_DIR=%~dp0\venv
set SCRIPTS=%VENV_DIR%\Scripts

:: Enable jupyter
set PATH=%PATH%;%SCRIPTS%

:: Put your codes here

jupyter notebook password

@echo on
pause
