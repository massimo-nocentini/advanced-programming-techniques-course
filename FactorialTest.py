
import unittest
from factorial import Factorial

class FactorialTest(unittest.TestCase):

#A testcase is created by subclassing unittest.TestCase. The three individual tests are defined with methods whose names start with the letters test. This naming convention informs the test runner about which methods represent tests.

#The crux of each test is a call to assertEqual() to check for an expected result; assertTrue() or assertFalse() to verify a condition; or assertRaises() to verify that a specific exception gets raised. These methods are used instead of the assert statement so the test runner can accumulate all test results and produce a report.

    def setUp(self):
        self.factorial = Factorial()

    def test_base_case(self):
        self.assertEqual(1, self.factorial(0))

    def test_non_base_case(self, i=5):
        self.assertEqual(self.factorial(i), i * self.factorial(i-1))

