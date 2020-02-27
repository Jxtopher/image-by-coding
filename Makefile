

all:
	# python3 -m pipenv install
	python3 -m pipenv install black --dev
	python3 -m pipenv run black .
	python3 -m pipenv run flake8 .
	python3 -m pipenv run mypy --ignore-missing-imports .
	python3 -m pipenv run python3 ./tests.py

install:
	python3 -m pipenv install
	python3 -m pipenv install black --dev