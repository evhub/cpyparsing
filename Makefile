.PHONY: full-test
full-test: install test

.PHONY: full-test-2
full-test-2: install test-2

.PHONY: full-test-3
full-test-3: install test-3

.PHONY: install
install: clean
	python -m pip install --upgrade pip setuptools wheel cython
	python ./constants.py
	python -m pip install --upgrade -e .

.PHONY: install-2
install-2: clean
	python2 -m pip install --upgrade pip setuptools wheel cython
	python2 ./constants.py
	python2 -m pip install --upgrade -e .

.PHONY: install-3
install-3: clean
	python3 -m pip install --upgrade pip setuptools wheel cython
	python3 ./constants.py
	python3 -m pip install --upgrade -e .

.PHONY: clean
clean: prepare
	rm -rf ./dist ./build
	-find . -name '*.pyc' -delete
	-find . -name '*.c' -delete
	-find . -name '*.so' -delete
	-find . -name '*.pyd' -delete
	-find . -name '__pycache__' -delete

.PHONY: prepare
prepare:
	-coconut --site-uninstall

.PHONY: wipe
wipe: clean
	-python -m pip uninstall cPyparsing
	-python3 -m pip uninstall cPyparsing
	-python2 -m pip uninstall cPyparsing
	rm -rf *.egg-info

.PHONY: build
build:
	python ./setup.py sdist bdist_wheel

.PHONY: upload-current
upload-current: install build
	pip install --upgrade twine
	twine upload dist/*

.PHONY: test
test: export COCONUT_PURE_PYTHON = TRUE
test:
	python ./tests/cPyparsing_test.py

.PHONY: test-2
test-2: export COCONUT_PURE_PYTHON = TRUE
test-2:
	python2 ./tests/cPyparsing_test.py

.PHONY: test-3
test-3: export COCONUT_PURE_PYTHON = TRUE
test-3:
	python3 ./tests/cPyparsing_test.py

.PHONY: test-c
test-c:
	pushd ./tests; make test-c; popd

.PHONY: test-py
test-py:
	pushd ./tests; make test-py; popd

.PHONY: test-coconut-py
test-coconut-py:
	pushd ./tests; make test-coconut-py; popd

.PHONY: test-coconut-c
test-coconut-c:
	pushd ./tests; make test-coconut-c; popd
