@echo off

set PYTHON_BASE=Python310
set PYTHON_BASE_FULL="%~dp0%PYTHON_BASE%/python"

echo Setting git proxy...

git config --global http.proxy "http://127.0.0.1:7890" >NUL 2>NUL

:exit
@echo on
pause
