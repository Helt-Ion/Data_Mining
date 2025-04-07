@echo off

set PYTHON_BASE=Python310
set PYTHON_BASE_FULL="%~dp0%PYTHON_BASE%/python"

echo Setting git proxy...

git config --global http.proxy "http://127.0.0.1:7890" >NUL 2>NUL

echo Setting pip proxy...

%PYTHON_BASE_FULL% -c "" >NUL 2>NUL
if %ERRORLEVEL% == 0 goto :reset_proxies
echo Couldn't launch python
goto :exit

:reset_proxies
%PYTHON_BASE_FULL% -m pip config set global.proxy http://127.0.0.1:7890 >NUL 2>NUL
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
