test:
	pytest --cov-report term-missing --cov=gtrending tests/ -vv
typecheck:
	mypy -p gtrending --ignore-missing-imports --warn-unreachable
typecheck-report:
	mypy -p gtrending --ignore-missing-imports --warn-unreachable --html-report mypy_report
