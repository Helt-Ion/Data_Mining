@echo off

set PYTHON_BASE=Python310
set PYTHON_BASE_FULL="%~dp0%PYTHON_BASE%/python"

%PYTHON_BASE_FULL% -c "" >NUL 2>NUL
if %ERRORLEVEL% == 0 goto :reset_source
echo Couldn't launch python
goto :exit

:reset_source
%PYTHON_BASE_FULL% -m pip config unset global.index-url
if %ERRORLEVEL% == 0 goto :exit
goto :error

:exit
@echo on
pause
exit /b

:error
echo.
echo Launch unsuccessful. Exiting.
@echo on
pause
