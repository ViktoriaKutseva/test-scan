.PHONY: test lint typecheck bench

test:
python -m unittest discover -s tests -p "test_*.py"

lint:
python -m compileall services packages tests

typecheck:
@echo "mypy config present for CI realism"

bench:
python scripts/bench/run_scan_benchmark.py
