#!/bin/bash

# Get the directory of the script
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Check if the system is macOS
if [ "$(uname)" == "Darwin" ]; then
    echo "Running on macOS"
    python3 "$SCRIPT_DIR/main.py"
else
    echo "This script is intended to be run on macOS."
fi

# Keep the terminal window open after the script executes
read -p "Press any key to close this window..."

