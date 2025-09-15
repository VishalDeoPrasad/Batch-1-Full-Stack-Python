class Employee:
    def __init__(self):
        self.name = "Ravi Gupta"
        self.__salary = 500000

    def get_salary(self):
        return self.__salary

emp1 = Employee()
print(emp1.name)
print(emp1.get_salary())
