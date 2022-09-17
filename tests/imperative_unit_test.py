# Unit tests

import sys
import unittest

# Use current path when importing packages
sys.path.append('.')

# Import testing packages
from tests.example_test_data import (example1_input, example2_input,
                                     example1_result, example2_result)
# Import Floyd Imperative function
from src.floyd_imperative import floyd_imperative_func


# Unit Tests
class FloydFunctionsTest(unittest.TestCase):
    """FloydFunctionsTest class inherits the unittest module"""

    def test_floyd_1(self):
        self.assertEqual(floyd_imperative_func(example1_input), example1_result,
                         "Invalid result")

    def test_floyd_2(self):
        self.assertEqual(floyd_imperative_func(example2_input), example2_result,
                         "Invalid result")


if __name__ == '__main__':
    # Run the unit tests
    unittest.main()
