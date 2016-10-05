
import unittest
from unittest.mock import Mock

from payroll import PayRoll, Employee

class PayrollTest(unittest.TestCase):

    def setUp(self):

        self.employees = []
        self.employeeDB = Mock()

        self.employeeDB.getAllEmployees.return_value=self.employees # stubbing

        self.payRoll = PayRoll(self.employeeDB)

    def test_no_employees(self):
        self.assertEqual(0, self.payRoll.monthly_payment())

    def test_single_employee(self):
        self.employees.append(self._make_employee())
        self.assertEqual(1, self.payRoll.monthly_payment())


    def _make_employee(self):
        return Employee()
