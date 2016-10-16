
import unittest
from unittest.mock import Mock, call, patch, create_autospec

from payroll import PayRoll, Employee

from contextlib import contextmanager
from functools import partial

@contextmanager
def patch_object_wraps(target, attribute, *args, **kwds):

    if 'wraps' not in kwds:
        kwds['wraps'] = getattr(target, attribute, None)

    with patch.object(target, attribute, *args, **kwds) as patched: yield patched 


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

    def test_employee_paid_is_updated_wrapping_patching_refactored(self): 

        employee = self._make_employee(identifier='id1', salary=1000)
        self.employees.append(employee)

        with patch_object_wraps(employee, 'paid') as paid:
            self.assertEqual(1, self.payRoll.monthly_payment())
            self.bank_service.make_payment.assert_called_once_with(employee_id='id1', salary=1000)
            paid.assert_called_once_with(True)
            self.assertTrue(employee.is_paid)

    @unittest.expectedFailure
    def test_is_empty_on_spied_list(self):
        sequence = []
        with patch_object_wraps(sequence, '__len__', return_value=False) as length:
            self.assertEqual(False, len(sequence))
            self.assertRaises(AttributeError, sequence, len)

    @unittest.expectedFailure
    def test_getitem_on_patched_list(self):
        sequence = []
        with patch_object_wraps(sequence, '__getitem__') as getter:
            getter(0).return_value = 'foo'
            self.assertRaises(AttributeError, sequence, len)
        
    def test_employees_is_not_paid_when_bank_throws_exception(self):
            
        employee = self._make_employee(identifier='id1', salary=1000)
        self.employees.append(employee)
        self.bank_service.make_payment.side_effect = Exception("Raised by mocking `bank_service.make_payment` method")

        with patch_object_wraps(employee, 'paid') as paid:
            self.assertEqual(1, self.payRoll.monthly_payment())
            self.bank_service.make_payment.assert_called_once_with(employee_id='id1', salary=1000)
            paid.assert_called_once_with(False)
            self.assertFalse(employee.is_paid)
    
    def test_other_employees_are_paid_in_case_of_a_single_exception(self):
            
        employee1 = self._make_employee(identifier='id1', salary=1000)
        employee2 = self._make_employee(identifier='id2', salary=2000)
        self.employees.extend([employee1, employee2])

        self.bank_service.make_payment.side_effect = [Exception("Raised by mocking `bank_service.make_payment` method"), 
                                                      None]

        with    patch_object_wraps(employee1, 'paid') as employee1_paid, \
                patch_object_wraps(employee2, 'paid') as employee2_paid:
            self.assertEqual(2, self.payRoll.monthly_payment())
            self.assertEqual(2, self.bank_service.make_payment.call_count)
            employee1_paid.assert_called_once_with(False)
            employee2_paid.assert_called_once_with(True)

    def test_other_employees_are_paid_in_case_of_a_single_exception_alternative(self):
            
        employee1 = self._make_employee(identifier='id1', salary=1000)
        employee2 = self._make_employee(identifier='id2', salary=2000)
        self.employees.extend([employee1, employee2])

        def matcher(employee_id, salary):
            if (employee_id, salary) == ('id2', 2000): raise Exception("Mocking exception only for employee 2")  
            return None

        self.bank_service.make_payment.side_effect = matcher

        with    patch_object_wraps(employee1, 'paid') as employee1_paid, \
                patch_object_wraps(employee2, 'paid') as employee2_paid:
            self.assertEqual(2, self.payRoll.monthly_payment())
            self.assertEqual(2, self.bank_service.make_payment.call_count)
            employee1_paid.assert_called_once_with(True)
            employee2.paid.assert_called_once_with(False)

    # protected messages {{{
    def _make_employee(self, identifier=None, salary=None):
        return Employee(identifier, salary)
    # }}}




