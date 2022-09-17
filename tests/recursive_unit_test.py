# Unit tests

import sys
import unittest

# Use current path when importing packages
sys.path.append('.')

# Import testing packages
from tests.example_test_data import (example1_input, example2_input,
                                 example1_result, example2_result)
# Import Floyd Recursive function
from src.floyd_recursive import floyd_recursive_func


# Unit Tests
class FloydFunctionsTest(unittest.TestCase):
    """FloydFunctionsTest class inherits the unittest module"""

    def test_floyd_1(self):
        self.assertEqual(floyd_recursive_func(example1_input), example1_result,
                         "Invalid result")

    def test_floyd_2(self):
        self.assertEqual(floyd_recursive_func(example2_input), example2_result,
                         "Invalid result")


if __name__ == '__main__':
    # Run the unit tests
    unittest.main()
