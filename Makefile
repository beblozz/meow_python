intsall:
	uv sync

VD-games:
	uv run vd-main

build:
	uv build

package-install:
	uv tool install dist/*.whl
lint:
	uv run ruff check meow_python/
