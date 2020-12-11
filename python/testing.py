
#	For tests to function, working directory when calling script must be directory containing script, i.e: project top-level directory

#	Running all tests (from package directory)
#	pytest: run all tests
#>%		pytest
#	unittest: run all test
#>%		python -m unittest
#	unittest requires test files be in dir 'test/' and named 'test_*.py', and that there be an '__init__.py' in tests dir 

#	unittest: run all tests in directory '$tests' 
#>%		python -m unittest discover $tests

#	unittest-parallel (usage)
#>%		pip install unittest-parallel
#>%		unittest-parallel -t . -s tests

#	Tests may be run with
#>%		python -m tests.test
#python -m unittest discover -s tests
#python -m unittest -v tests.test-methods
#python -m unittest -v tests.test-cli

#	To run tests from arbitrary directory, specify location of project parent directory where tests should be performed
#>%		python -m unittest discover -s tests -t $path_src



