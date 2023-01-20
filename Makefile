test:
	python3 -m pytest --cov-report term-missing --cov=gtrending tests/ -vv --doctest-modules gtrending
doctest:
	cd docs
	sphinx-build -b doctest docs docs/_build
typecheck:
	python3 -m mypy -p gtrending --ignore-missing-imports --warn-unreachable --install-types --non-interactive
typecheck-report:
	python3 -m mypy -p gtrending --ignore-missing-imports --warn-unreachable --install-types --non-interactive --html-report mypy_report
fmt:
	python3 -m black .
fmt-check:
	python3 -m black . --check
