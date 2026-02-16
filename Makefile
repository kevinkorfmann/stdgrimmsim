# stdgrimmsim — uv-based dev workflow
# Requires: uv (pip install uv or brew install uv)

.PHONY: install test test-cov quick-sim

install:
	uv sync --all-extras

test:
	uv run pytest -v tests

test-cov:
	uv run pytest -v tests --cov=stdgrimmsim --cov-report=term-missing

quick-sim:
	uv run python .test/run_simulation.py
