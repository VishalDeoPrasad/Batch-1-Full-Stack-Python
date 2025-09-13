class College:
    college_name = "ABC College"
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks


s1 = College("Amit", 32, 98)
s2 = College("Vishal", 30, 99)

print(s1.name)
print(s2.name)
print(s1.college_name)
print(s2.college_name)

