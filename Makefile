.PHONY: install
install:
	pip install --upgrade pip setuptools cython
	python ./constants.py
	pip install --upgrade -e .

.PHONY: clean
clean:
	rm -rf ./dist ./build
	find . -name '*.pyc' -delete
	find . -name '*.c' -delete
	find . -name '*.pyd' -delete
	find . -name '__pycache__' -delete

.PHONY: wipe
wipe: clean
	rm -rf *.egg-info

.PHONY: upload-sys
upload-sys: clean install
	pip install --upgrade twine
	python2 setup.py sdist bdist_wheel
	-twine upload dist/*
	python3 setup.py sdist bdist_wheel
	-twine upload dist/*

.PHONY: upload
upload:
	make upload-sys
	sh -c "make upload-sys"

.PHONY: test
test:
	python ./tests/cPyparsing_test.py

.PHONY: test-c
test-c:
	pushd ./tests
	make test-c
	popd

.PHONY: test-py
test-py:
	pushd ./tests
	make test-py
	popd

.PHONY: test-coconut-py
test-coconut-py:
	pushd ./tests
	make test-coconut-py
	popd

.PHONY: test-coconut-c
test-coconut-c:
	pushd ./tests
	make test-coconut-c
	popd
