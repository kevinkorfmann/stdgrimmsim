#!/usr/bin/env bash
# Run stdgrimmsim CLI (requires venv: run install_and_run.sh first, or have stdgrimmsim on PATH).
set -e
cd "$(dirname "$0")/.."
if [ -d ".test/venv" ]; then
  source .test/venv/bin/activate
fi
stdgrimmsim DagHyd -d InnsmouthDecline_1M27 -L 5000 -o .test/out.trees DeepOnes:4
echo "Wrote .test/out.trees"
python3 -c "import tskit; ts=tskit.load('.test/out.trees'); print('  Trees:', ts.num_trees, 'Sites:', ts.num_sites)"
rm -f .test/out.trees
