file:
	python ./tests/test_str.py

unittest-file:
	python -m unittest -v tests/test_str.py

unittest-package:
	python -m unittest -v tests

unittest-module:
	python -m unittest -v tests.test_str

unittest-class:
	python -m unittest -v tests.test_str.TestStringMethods

unittest-test:
	python -m unittest -v tests.test_str.TestStringMethods.test_upper


unittest-file-without-discover:
	python -m unittest -v tests
	python -m unittest -v tests/
	python -m unittest -v tests/*


unittest-discover:
	python -m unittest discover -v tests/