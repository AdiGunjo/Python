from abc import ABC, abstractmethod
 
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
 
    @abstractmethod
    def fuel_type(self):
        pass
 
    def summary(self):
        return f"{self.__class__.__name__}: {self.fuel_type()} | {self.start_engine()}"
 
 
class ElectricCar(Vehicle):
    def start_engine(self):
        return "Silent startup (motor engaged)"
 
    def fuel_type(self):
        return "Electric"
 
 
class DieselTruck(Vehicle):
    def start_engine(self):
        return "Engine cranks and roars to life"
 
    def fuel_type(self):
        return "Diesel"
 
 
for v in [ElectricCar(), DieselTruck()]:
    print(v.summary())
