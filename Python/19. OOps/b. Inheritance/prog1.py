class anything:
    def __init__(self):
        self.name = "Labrador"

    def speak(self):
        print("Dog Can Speek!")

class Dog(anything):
    def printname(self):
        print(self.name)

d1 = Dog()
d1.printname()