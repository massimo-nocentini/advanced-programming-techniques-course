
import unittest
from unittest.mock import Mock

from payroll import PayRoll, Employee

class PayrollTest(unittest.TestCase):

    def setUp(self):
        self.employeeDB = Mock()
        self.payRoll = PayRoll(self.employeeDB)

    def test_no_employees(self):
        self.employeeDB.getAllEmployees.return_value=[] # stubbing
        self.assertEqual(0, self.payRoll.monthly_payment())

    def test_single_employee(self):
        employees = [Employee()]
        self.employeeDB.getAllEmployees.return_value=employees # stubbing
        self.assertEqual(1, self.payRoll.monthly_payment())
