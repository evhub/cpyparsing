.PHONY: install
install:
	pip install --upgrade pip setuptools cython
	python ./constants.py
	pip install --upgrade -e .

.PHONY: install-2
install-2:
	pip2 install --upgrade pip setuptools cython
	python2 ./constants.py
	pip2 install --upgrade -e .

.PHONY: install-3
install-3:
	pip3 install --upgrade pip setuptools cython
	python3 ./constants.py
	pip3 install --upgrade -e .

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

.PHONY: upload
upload: install
	pip install --upgrade twine
	make upload-2
	make upload-3

.PHONY: upload-2
upload-2:
	python2 setup.py sdist bdist_wheel
	twine upload dist/*

.PHONY: upload-3
upload-3:
	python3 setup.py sdist bdist_wheel
	twine upload dist/*

.PHONY: test
test:
	python ./tests/cPyparsing_test.py

.PHONY: test-2
test-2:
	python2 ./tests/cPyparsing_test.py

.PHONY: test-3
test-3:
	python3 ./tests/cPyparsing_test.py

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
