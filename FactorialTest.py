
import unittest
from factorial import Factorial

class FactorialTest(unittest.TestCase):

    def setUp(self):
        self.factorial = Factorial()

    def test_base_case(self):
        self.assertEqual(1, self.factorial(0))

    def test_non_base_case(self, i=5):
        self.assertEqual(self.factorial(i), i * self.factorial(i-1))

    def test_negative_input(self):
        try:
            self.factorial(-1)
            raise Exception("should not be here")
        except RecursionError: pass
