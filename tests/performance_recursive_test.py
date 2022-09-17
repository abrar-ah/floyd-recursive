# Use cProfile for testing recursive function

import cProfile
import sys

# Use current path when importing packages
sys.path.append('.')

# Import testing packages
from tests.example_test_data import (example1_input, example2_input,
                                 example1_result, example2_result)
# Import Floyd Recursive function
from src.floyd_recursive import floyd_recursive_func


# Performance Tests
cProfile.run("floyd_recursive_func(example1_input)")

cProfile.run("floyd_recursive_func(example2_input)")
