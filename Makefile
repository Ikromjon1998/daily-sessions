.PHONY: check fmt lint type test

check: fmt lint type test

fmt:
	ruff format .

lint:
	ruff check --fix .

type:
	mypy .

test:
	pytest
