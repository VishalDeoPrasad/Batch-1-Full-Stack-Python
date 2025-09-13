class Student:
    def __init__(self, name, age, marks=100):
        self.name = name
        self.age = age
        self.marks = marks

    def attend_class(self):
        print("Thanks for attending the session!")

    def show_grade(self):
        return "you have Good grade!"

obj = Student("Vishal", 30, 90)
print(obj.name)
print(obj.marks)
print(obj.show_grade())
