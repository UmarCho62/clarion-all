@echo off
REM ADA Sales Navigator - Quick Start Script for Windows

echo.
echo 🎯 ADA Compliance Sales Navigator
echo ==================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

echo ✅ Python found
python --version
echo.

REM Check if requirements are installed
echo 📦 Checking dependencies...
python -c "import streamlit" >nul 2>&1
if errorlevel 1 (
    echo 📥 Installing required packages...
    pip install -r requirements.txt
    echo ✅ Dependencies installed!
) else (
    echo ✅ Dependencies already installed
)

echo.
echo 🚀 Starting Sales Navigator...
echo.
echo The app will open in your browser at http://localhost:8501
echo.
echo Press Ctrl+C to stop the server
echo.

REM Run the Streamlit app
streamlit run sales_navigator_app.py

