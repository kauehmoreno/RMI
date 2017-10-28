

VENV = .venv
export VIRTUAL_ENV := $(abspath ${VENV})
export PATH := ${VIRTUAL_ENV}/bin:${PATH}

setup:
	@pip install -r requirements.txt

run:
	./manage.py runserver 0.0.0.0:8000
