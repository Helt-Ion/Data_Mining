@echo off

set VENV_DIR=venv
set PYTHON="%~dp0%VENV_DIR%/python"

if exist %VENV_DIR%/ (
  %PYTHON% -c "" >NUL 2>NUL
  if %ERRORLEVEL% == 0 goto :export_env
  echo Couldn't launch python
  goto :error

  :export_env
  %PYTHON% -m pip freeze > requirements_freeze.txt
  if %ERRORLEVEL% == 0 goto :exit
  goto :error
)

echo venv does not exist, skipping.

:exit
@echo on
pause
exit /b

:error
echo.
echo Launch unsuccessful. Exiting.
@echo on
pause
