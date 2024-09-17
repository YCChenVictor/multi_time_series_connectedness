.PHONY: test

test:
	python3 -m unittest discover -s tests

coverage:
	coverage run --source=your_package_name -m unittest discover -s tests
	coverage report
	coverage html
