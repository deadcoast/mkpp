@echo off
echo.
echo ========================================
echo  milk++ Installation Script
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3.7+ from https://www.python.org/
    echo.
    pause
    exit /b 1
)

echo [1/3] Checking Python version...
python --version
echo.

echo [2/3] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)
echo.

echo [3/3] Installing mkpp command...
pip install -e .
if errorlevel 1 (
    echo [ERROR] Failed to install mkpp
    pause
    exit /b 1
)
echo.

echo ========================================
echo  Installation Complete!
echo ========================================
echo.
echo You can now use 'mkpp' from any directory!
echo.
echo Quick Start:
echo   - Run 'mkpp' to open interactive menu
echo   - Run 'mkpp dracula' to install Dracula theme
echo   - Run 'mkpp --help' for more options
echo.
echo Have fun with milk++! ^_^
echo.
pause