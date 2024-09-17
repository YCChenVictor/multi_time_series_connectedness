.PHONY: test

test:
	python3 -m unittest discover -s tests

coverage:
	coverage run --source=multi_time_series_connectedness -m unittest discover -s tests
	coverage report
	coverage html
