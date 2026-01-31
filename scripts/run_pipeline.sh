#!/bin/bash

# Exit immediately if a command fails
set -e

# Move to project root directory
PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT_ROOT"

# Activate virtual environment if exists (optional)
# source venv/bin/activate

# Run the ETL pipeline
python -m pipeline.main
