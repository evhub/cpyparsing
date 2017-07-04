.PHONY: install
install:
	pip3 install --upgrade -e .

.PHONY: test
test: install
	python3 ./tests/pyparsing_test.py

.PHONY: clean
clean:
	rm -rf ./dist ./build
	find . -name '*.c' -delete
	find . -name '*.py[cd]' -delete
	find . -name '__pycache__' -delete
