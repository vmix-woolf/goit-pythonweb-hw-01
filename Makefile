# ===============================
#  Project: goit-pythonweb-hw-01
#  Purpose: Automation for checks and runs
# ===============================

PYTHON = poetry run python
POETRY = poetry run

# Run application
run:
	$(PYTHON) main.py

# Code style checks
check:
	$(POETRY) black --check .
	$(POETRY) isort --check-only .
	$(POETRY) ruff check .
	$(POETRY) mypy .

# Auto format code
format:
	$(POETRY) isort .
	$(POETRY) black .

# Lint only (Ruff + Mypy)
lint:
	$(POETRY) ruff check .
	$(POETRY) mypy .

# Run all tests
test:
	$(POETRY) pytest -q || true

# Run pre-commit hooks manually
precommit:
	$(POETRY) pre-commit run --all-files
