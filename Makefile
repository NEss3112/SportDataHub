.PHONY: test

test:
	PYTHONPATH=$(pwd)/sportdatahub pytest  tests 
