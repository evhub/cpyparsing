.PHONY: install
install:
	pip install --upgrade -e .

.PHONY: test
test:
	pytest --strict -s tests

.PHONY: clean
clean:
	rm -rf ./dist ./build
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
