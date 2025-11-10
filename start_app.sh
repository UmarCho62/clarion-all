#!/bin/bash

# ADA Sales Navigator - Quick Start Script

echo "🎯 ADA Compliance Sales Navigator"
echo "=================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python found: $(python3 --version)"
echo ""

# Check if requirements are installed
echo "📦 Checking dependencies..."
if ! python3 -c "import streamlit" &> /dev/null; then
    echo "📥 Installing required packages..."
    pip3 install -r requirements.txt
    echo "✅ Dependencies installed!"
else
    echo "✅ Dependencies already installed"
fi

echo ""
echo "🚀 Starting Sales Navigator..."
echo ""
echo "The app will open in your browser at http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Run the Streamlit app
streamlit run sales_navigator_app.py

