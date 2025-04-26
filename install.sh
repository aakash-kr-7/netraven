#!/bin/bash

# Install script for NetRaven

echo "🐦 Setting up NetRaven..."

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install requirements
pip install --upgrade pip
pip install -r requirements.txt

# Install NetRaven package
pip install .

echo "✅ NetRaven installed successfully!"
echo "➡️  Now run 'netraven_run' to start scanning."
