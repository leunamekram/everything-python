
# Pytest Tutorial from [Tutorials Point](https://www.tutorialspoint.com/pytest/pytest_introduction.htm)

## Unit Tests vs. Integration Tests
1. An integration test checks that components in your application operate with each other.
2. A unit test checks a small component in your application.

See [simple_test_sum.py](./sample-tests/simple_test_sum.py) for simple unit tests in python using built-in *assert()* function.

## Pytest Introduction
A python based testing framework used to write and execute test codes. Mainly used for API testing
though can be extended for more complex tests.

### Advantages of Pytest
* Can run multiple tests in parallel thus greatly reducing executime time of test suite.
* Has its own way of detecting test file and test functions automatically (if not mentioned explicitly).
* Allows skipping subset of tests  during execution.
* Allows to run subset of entire test suite
* Easy, free and open source.

### Installation and Help
Installing the latest version:
```
pip install pytest
```

Installing a specific version:
```
pip install pytest == 2.9.1
```

Displaying help section:
```
pytest -h
```

## Identifying Test Files and Test Functions
Files of the format **test_*.py** or **\*_test.py** in the current and subdirectories are automatically
identified by pytest as test files. Function names should start with **test** for them to be indentified
as test functions. See [test_square.py](./sample-tests/test_square.py).

### Running the test with Pytest:
This will execute all the tests in all the test files.
```
pytest
```

### Running the test with Pytest verbosely:
This will execute all the tests in all the test files.
```
pytest -v
```

### Running specific test files
This will execute all the tests in the *test_compare.py* test file.
```
pytest test_compare.py -v
```

### Running test functions with substring matching
This will execute all the tests with *great* string on test function name.
```
pytest -k great -v
```

### Grouping tests with markers
Below is the syntax for applying markers on tests.
```
@pytest.mark.<markername>
```

Running marked tests.
```
pytest -m <markername>
# Example
pytest -m others -v
```

## Pytest Fixtures
Fixtures are functions which will run before each test function to which it is applied. Thes are used to feed
some data to the test. A single fixture may be applid to multiple test functions. Functions are marked
as fixture through the following syntax.
```
@pytest.fixture
```

Test functions can use a fixture by mentioning the fixture name as an input parameter.
See [test_divisibility.py](./sample-tests/test_divisibility.py).

## Pytest Conftest.py
A fixture defined inside a test file cannot be used in another test file. This limitation can be solved
by adding test fixtures in a file called **conftest.py** which makes fixtures accessible across
multiple test files.

See [test_div_13.py](./sample-tests/test_div_13.py) which uses the test fixture from [conftest.py](./sample-tests/conftest.py).

## Pytest Parameterizing Tests
Parameterizing test (running test against multiple set of inputs) can be done with the following marker.
```
@pytest.mark.parametrize
```

See [test_multiplication.py](./sample-tests/test_multiplication.py).

## Pytest Xfail/Skip Tests, Stop Test Suite After N Test Failures
Pytest will execute xfailed test but it will not be considered as part of the failed or passed tests.
```
@pytest.mark.fail
```

Skipping a test means it will not be executed at all.
```
@pytest.mark.skip
```

Later when the tests becomes relevant, the markers can be removed.
See [test_compare_xfail_skip.py](./sample-tests/test_compare_xfail_skip.py).

The syntax for stopping test suite execution after N number of test fails is as follows.
```
pytest --maxfail=<N>
```

## Pytest - Run Tests in Parallel
Install pytest-xdist as follows.
```
pip install pytest-xdist
```

Now, we can run tests with N workers through the following syntax.
```
pytest -n <N>
```

## Test Execution Results in XML
```
pytest -v --junitxml="results.xml"
```

## Full Documentation
See [pytest.pdf](./docs/pytest.pdf) for full Pytest documentation.
