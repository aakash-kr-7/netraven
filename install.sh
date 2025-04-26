#!/bin/bash

# Install script for NetRaven

echo "🐦 Setting up NetRaven..."

# Check if Python3 is installed
if ! command -v python3 &> /dev/null
then
    echo "❌ Python3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

# Check if venv module is available
if ! python3 -m venv --help &> /dev/null
then
    echo "❌ Python venv module is not available."
    echo "➡️  On Debian/Ubuntu, install it using: sudo apt install python3-venv"
    exit 1
fi

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
else
    echo "📦 Virtual environment already exists. Skipping creation."
fi

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "📜 Installing required Python packages..."
pip install -r requirements.txt

# Install NetRaven package locally
echo "🛠️  Installing NetRaven..."
pip install .

echo "✅ NetRaven installed successfully!"
echo ""
echo "➡️  Now you can run 'netraven_run' to start scanning your system logs!"
echo "🔎 Example: netraven_run"
