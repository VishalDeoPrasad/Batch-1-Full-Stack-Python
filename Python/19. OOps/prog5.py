class Car:
    def __init__(self, name, year, model, fuel, mileage, doors, airbags):
        self.comp_name = name
        self.year = year
        self.model_name = model
        self.fuel_types = fuel
        self.mileage = mileage
        self.no_of_doors = doors
        self.no_of_airBags = airbags

    def travel(self):
        print("You can travel with the car!")

    def printAll(self):
        print(self.comp_name, self.year, self.model_name, self.fuel_types, 
              self.mileage, self.no_of_doors)

car1 = Car("Tata", 2022, "XUV", "EV", "23", 5, 2)
car1.travel()
car1.printAll()

