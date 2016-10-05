
class PayRoll:

    def __init__(self, employeeDB):
        self.employeeDB = employeeDB

    def monthly_payment(self):
        return len(self.employeeDB.getAllEmployees())
