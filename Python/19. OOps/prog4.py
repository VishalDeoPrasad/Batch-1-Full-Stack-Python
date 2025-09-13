class Car:
    def __init__(self):
        self.comp_name = "TATA"
        self.year = 2020
        self.model_name = "XUV"
        self.fuel_types = "EV"
        self.milage = 25
        self.no_of_doors = 5
        self.no_of_airBags = 2

    def travel(self):
        print("You can travel with the car!")

car1 = Car()
print(car1.comp_name)
print(car1.model_name)
car1.travel()

