@echo off
set PYTHON_PATH=C:\Users\Fernando\AppData\Local\Programs\Python\Python39
set PATH=%PYTHON_PATH%;%PYTHON_PATH%\Scripts;%PATH%

:: Check if Python is installed
%PYTHON_PATH%\python.exe --version
if %errorlevel% neq 0 (
    echo Python not found. Please install Python 3.9 or update the PYTHON_PATH variable.
    pause
    exit /b 1
)

echo Installing required libraries...
%PYTHON_PATH%\python.exe -m pip install --upgrade pip
%PYTHON_PATH%\python.exe -m pip install -r requirements.txt

:: Check if ffmpeg is installed
ffmpeg -version
if %errorlevel% neq 0 (
    echo FFmpeg not found. Please install FFmpeg and add it to your PATH.
    pause
    exit /b 1
)

echo All dependencies are installed.

pause
