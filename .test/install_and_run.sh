#!/usr/bin/env bash
# From repo root: create venv, install stdgrimmsim, then run the test script.
set -e
cd "$(dirname "$0")/.."
TESTDIR=".test"
if [ ! -d "$TESTDIR/venv" ]; then
  echo "Creating venv in $TESTDIR/venv ..."
  python3 -m venv "$TESTDIR/venv"
fi
echo "Activating venv and installing stdgrimmsim (editable)..."
source "$TESTDIR/venv/bin/activate"
pip install -e . -q
echo "Running simulation test..."
python "$TESTDIR/run_simulation.py"
deactivate 2>/dev/null || true
