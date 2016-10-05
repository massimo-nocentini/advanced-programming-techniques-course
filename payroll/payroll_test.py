
import unittest

from payroll import PayRoll

class PayrollTest(unittest.TestCase):

    def setUp(self):
        self.employeeDB = None
        self.payRoll = PayRoll(self.employeeDB)

    def test_no_employees(self):
        self.assertEqual(0, self.payRoll.monthly_payment())
