
import unittest
from unittest.mock import Mock, call, patch, create_autospec

from payroll import PayRoll, Employee

class PayrollTest(unittest.TestCase):

    def setUp(self):

        self.employees = []

        self.employeeDB = Mock()
        self.bank_service = Mock()

        self.employeeDB.getAllEmployees.return_value=self.employees # stubbing

        self.payRoll = PayRoll(self.employeeDB, self.bank_service)

    def test_no_employees(self):
        self.assertEqual(0, self.payRoll.monthly_payment())

    def test_single_employee(self):
        self.employees.append(self._make_employee())
        self.assertEqual(1, self.payRoll.monthly_payment())

    def test_interaction_with_db_happened(self):
        _ = self.payRoll.monthly_payment()
        self.assertTrue(self.employeeDB.getAllEmployees.called)

    def test_only_one_interaction_with_db(self):
        _ = self.payRoll.monthly_payment()
        self.assertEqual(1, self.employeeDB.getAllEmployees.call_count)

    def test_employee_is_paid(self):
        self.employees.append(self._make_employee(identifier='id1', salary=1000))

        self.assertEqual(1, self.payRoll.monthly_payment())
        self.bank_service.make_payment.assert_called_once_with(employee_id='id1', salary=1000)

    def test_all_employees_are_paid(self):
        self.employees.append(self._make_employee(identifier='id1', salary=1000))
        self.employees.append(self._make_employee(identifier='id2', salary=2000))

        self.assertEqual(2, self.payRoll.monthly_payment())
        self.assertEqual(2, self.bank_service.make_payment.call_count)

        self.bank_service.make_payment.assert_any_call(employee_id='id1', salary=1000)
        self.bank_service.make_payment.assert_any_call(employee_id='id2', salary=2000)

    def test_interaction_order(self):
        
        self.employees.append(self._make_employee(identifier='id', salary=1000))

        self.assertEqual(1, self.payRoll.monthly_payment())

        happened = self.employeeDB.mock_calls + self.bank_service.mock_calls
        expected = [call.getAllEmployees(), call.make_payment(employee_id='id', salary=1000)]
        self.assertEqual(expected, happened)

    def test_employee_paid_is_updated_simple_patching(self): 

        employee = self._make_employee(identifier='id1', salary=1000)
        self.employees.append(employee)

        with patch.object(employee, 'paid') as paid:
            self.assertEqual(1, self.payRoll.monthly_payment())
            self.bank_service.make_payment.assert_called_once_with(employee_id='id1', salary=1000)
            paid.assert_called_once_with(True)
            self.assertFalse(employee.is_paid)
        
    def test_employee_paid_is_updated_wrapping_patching(self): 

        employee = self._make_employee(identifier='id1', salary=1000)
        self.employees.append(employee)

        with patch.object(employee, 'paid', wraps=employee.paid) as paid:
            self.assertEqual(1, self.payRoll.monthly_payment())
            self.bank_service.make_payment.assert_called_once_with(employee_id='id1', salary=1000)
            paid.assert_called_once_with(True)
            self.assertTrue(employee.is_paid)

    def _make_employee(self, identifier=None, salary=None):
        return Employee(identifier, salary)
