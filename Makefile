.PHONY: test

test:
	python3 -m unittest discover -s tests

coverage:
	coverage run --source=src -m unittest discover -s tests
	coverage report
	coverage html
