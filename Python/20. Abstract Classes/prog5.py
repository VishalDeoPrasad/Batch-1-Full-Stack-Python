from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def max_speed(self):
        pass
    
    @abstractmethod
    def fuel_capacity(self):
        pass

class Car:
    def max_speed(self):
        print("Max Speed: 120 km/h")

    def fuel_capacity(self):
        print("Fuel Capacity: 25L")

class Bus:
    def max_speed(self):
        print("Max Speed: 140 km/h")

    def fuel_capacity(self):
        print("Fuel Capacity: 100L")

class Truck:
    def max_speed(self):
        print("Max Speed: 70 km/h")

    def fuel_capacity(self):
        print("Fuel Capacity: 50L")

car = Car()
car.max_speed()
car.fuel_capacity()
bus = Bus()
bus.max_speed()
bus.fuel_capacity()
truck = Truck()
truck.max_speed()
truck.fuel_capacity()
a

