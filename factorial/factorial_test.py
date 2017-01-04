
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
        self.assertRaises(ValueError, self.factorial, -1)

    @unittest.skip("restoring correct behavior")
    def test_forced_failure(self):
        self.fail("Forced failure")
