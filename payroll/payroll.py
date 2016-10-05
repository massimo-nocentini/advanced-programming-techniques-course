
class PayRoll:

    def __init__(self, employeeDB, bank_service):
        self.employeeDB = employeeDB
        self.bank_service = bank_service

    def monthly_payment(self):
        employees = self.employeeDB.getAllEmployees()
        if employees:
            e, *rest = employees
            e.paid_by(self.bank_service)
        return len(employees)

class Employee: 
    
    def __init__(self, identifier, salary):
        self.identifier = identifier
        self.salary = salary

    def paid_by(self, bank_service):
        bank_service.make_payment(employee_id=self.identifier, salary=self.salary)
