@echo off
title Running Booster Script
:: Check for admin rights
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Running as Administrator
    python "%USERPROFILE%\Documents\booster.py"
    echo.
    echo Script completed. Press any key to exit.
) else (
    echo Requesting Administrative Privileges...
    powershell -Command "Start-Process cmd -ArgumentList '/c %~dp0%~nx0' -Verb RunAs"
)
pause >nul
