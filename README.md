
# Recursive Version Of Floyd’s Algorithm
### Mid-module assignment - Submitted to University of Liverpool
<img src="https://www.liverpool.ac.uk/logo-size-test/full-colour.svg" width="310px"/>

## Implements Floyd Warshall using recursion

## Install

Clone git repo:
```shell
git clone https://github.com/abrar-ah/floyd-recursive.git
```

Install required packages
```shell
pip install -r requirements.txt
```

## Usage

Type the following command to execute the program:
```shell
python test_recursive.py
```

### Unit Test

Unit test input and result of Floyd recursive function 
```shell
python -m unittest tests/imperative_unit_test.py
python -m unittest tests/recursive_unit_test.py
```

### Pefromance Test using cProfile

Unit test the example input and result of Floyd recursive function 
```shell
python -m cProfile tests/performance_test_recursive.py
```

Unit test the example input and result of Floyd imperative function 
```shell
python -m cProfile tests/performance_test_imperative.py
```