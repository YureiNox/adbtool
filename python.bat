@echo off


rem Check if Python is installed
where python >nul 2>&1
if %errorlevel% neq 0 (
    rem Python is not installed, so download the Python installer
    powershell -Command "(new-object System.Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.9.4/python-3.9.4-amd64.exe', 'python-3.9.4-amd64.exe')"

    rem Install Python
    python-3.9.4-amd64.exe /quiet InstallAllUsers=1 PrependPath=1

    rem Delete the Python installer
    del python-3.9.4-amd64.exe
)

rem Check if pip is installed
where pip >nul 2>&1
if %errorlevel% neq 0 (
    rem Pip is not installed, so download the get-pip.py script
    powershell -Command "(new-object System.Net.WebClient).DownloadFile('https://bootstrap.pypa.io/get-pip.py', 'get-pip.py')"

    rem Install pip
    python get-pip.py

    rem Delete the get-pip.py script
    del get-pip.py
)

