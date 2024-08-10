@echo off
set PYTHON_PATH=C:\Users\Fernando\AppData\Local\Programs\Python\Python39
set PATH=%PYTHON_PATH%;%PYTHON_PATH%\Scripts;%PATH%

echo Generating subtitles...
%PYTHON_PATH%\python.exe "generate_subtitles.py" "%~1"

pause
