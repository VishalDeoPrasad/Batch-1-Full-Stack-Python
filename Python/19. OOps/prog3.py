class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("Person Can Run!")

obj2 = Person("Amit", 32)
print(obj2.name)
obj2.run()



