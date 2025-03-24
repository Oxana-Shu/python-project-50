install:
	uv sync

gendiff:
	uv run gendiff

build:
	uv build

lint:
	uv run ruff check

check: test lint

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml