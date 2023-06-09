install:
	pip install -r requirements.txt

lint:
	pylint hello.py

test:
	python -m pytest -vv test_hello.py

deploy:
	uvicorn app:app