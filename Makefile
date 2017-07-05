.PHONY: install
install:
	pip install --upgrade cython
	python ./constants.py
	pip install --upgrade -e .

.PHONY: test
test:
	python ./tests/cPyparsing_test.py

.PHONY: clean
clean:
	rm -rf ./dist ./build
	find . -name '*.pyc' -delete
	find . -name '*.c' -delete
	find . -name '*.pyd' -delete
	find . -name '__pycache__' -delete
