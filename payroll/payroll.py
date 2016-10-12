

class PayRoll:

    def __init__(self, employeeDB, bank_service):
        self.employeeDB = employeeDB
        self.bank_service = bank_service

    def monthly_payment(self):
        employees = self.employeeDB.getAllEmployees()
        for e in employees:
            try:
                e.paid_by(self.bank_service)
                e.paid(True)
            except:
                print('exception when paying employee {}.'.format(e.identifier))
                e.paid(False)

        return len(employees)

class Employee: 
    
    def __init__(self, identifier, salary):
        self.identifier = identifier
        self.salary = salary
        self.is_paid = False

    def paid(self, state):
        self.is_paid = state

    def paid_by(self, bank_service):
        bank_service.make_payment(employee_id=self.identifier, salary=self.salary)

