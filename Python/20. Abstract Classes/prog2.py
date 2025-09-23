from abc import ABC, abstractmethod

class House(ABC):
    @abstractmethod
    def kitchen(self):
        print("Default Kitchen")
    
    @abstractmethod
    def bathroom(self):
        print("Default Bathroom")

    @abstractmethod
    def bedroom(self):
        print("Default Bedroom")

class Villa(House):
    def kitchen(self):
        print("Villa Kitchen")

    def bathroom(self):
        print("Villa Bathroom")

    def bedroom(self):
        print("Villa Bedroom")

v = Villa()
v.bathroom()
v.bedroom()
v.kitchen()