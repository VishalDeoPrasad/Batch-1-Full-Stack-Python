class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def display_info(self):
        print(self.brand, self.color)


obj = Car("Toyota", "Blue")
obj.display_info()