@echo off

set INSTALL_TORCH=False
set TORCH_INDEX_URL=
set TORCH_PACKAGE=
set TORCHVISION_PACKAGE=
set REQS_FILE=

set PYTHON_BASE=Python310
set PYTHON_BASE_FULL="%~dp0%PYTHON_BASE%/python"
set VENV_DIR=venv
set PYTHON="%~dp0%VENV_DIR%/python"

%PYTHON_BASE_FULL% -c "" >NUL 2>NUL
if %ERRORLEVEL% == 0 goto :create_venv
echo Couldn't launch python
goto :error

:create_venv
%PYTHON% -c "" >NUL 2>NUL
if %ERRORLEVEL% == 0 goto :build
echo Creating venv...
robocopy %PYTHON_BASE% %VENV_DIR% /E >NUL 2>NUL

%PYTHON% -c "" >NUL 2>NUL
if %ERRORLEVEL% == 0 goto :build
echo Couldn't launch python
goto :error

:build
%PYTHON% build.py
@echo on
pause
exit /b

:error
echo.
echo Launch unsuccessful. Exiting.
@echo on
pause
