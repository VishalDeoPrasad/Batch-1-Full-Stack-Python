class Student:
    def __init__(self):
        self.name = "Vishal"
        self._age = 30
        self.__grade = "A"

s1 = Student()
print(s1.name)
print(s1._age)
print(s1.__grade)