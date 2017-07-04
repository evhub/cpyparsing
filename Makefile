.PHONY: install
install:
	pip install --upgrade cython
	pip install --upgrade -e .

.PHONY: test
test:
	python ./tests/pyparsing_test.py

.PHONY: clean
clean:
	rm -rf ./dist ./build
	find . -name '*.c' -delete
	find . -name '*.py[cd]' -delete
	find . -name '__pycache__' -delete
