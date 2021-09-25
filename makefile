build:
	source venv/bin/activate
	python3 -m build

deploy:
	source venv/bin/activate
	python3 -m twine upload --repository pypi dist/*

clean:
	rm dist/*
	rm -r src/*egg*

prepare:
	python -m venv venv
	source venv/bin/activate
	pip3 install twine build
