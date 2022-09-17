# Use cProfile for testing imperative function

import cProfile
import sys

# Use current path when importing packages
sys.path.append('.')

# Import testing packages
from tests.example_test_data import (example1_input, example2_input,
                                     example1_result, example2_result)
# Import Floyd Imperative function
from src.floyd_imperative import floyd_imperative_func

# Performance Tests
cProfile.run("floyd_imperative_func(example1_input)")

cProfile.run("floyd_imperative_func(example2_input)")
