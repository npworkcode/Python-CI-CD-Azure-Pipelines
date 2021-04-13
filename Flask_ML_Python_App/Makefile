setup:
	py -3 -m venv ~/.avenv

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv -W ignore::DeprecationWarning --cov=app test*.py
	#python -m pytest --nbval notebook.ipynb


lint:
	#hadolint Dockerfile #uncomment to explore linting Dockerfiles
	pylint --disable=R,C,W1203 app.py

all: install lint test
