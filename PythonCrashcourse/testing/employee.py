class Employee():
    def __init__(self, first_name, last_name, annual_salary=0):
        self.firstname = first_name
        self.lastname = last_name
        self.annual_salary = annual_salary

    def give_raise(self,raise_amount=5000):
        self.raise_amount = raise_amount
        self.annual_salary = self.annual_salary + raise_amount

    def __str__(self): #print function will call __str__ for your object/class if you have
        # not define a print function.
        return self.firstname + ' ' + self.lastname + ' Annual salary:' + str(self.annual_salary)

new_employee = Employee('Hanwei','Li', 100000)

print(new_employee)
new_employee.give_raise(6000)
print(new_employee)
