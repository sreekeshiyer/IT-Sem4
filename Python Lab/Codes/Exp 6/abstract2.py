from abc import ABC, abstractmethod
class Vehicle(ABC):     
    @abstractmethod  
    def getNoOfWheels(Self):
        pass

class Bus(Vehicle):   
    def getNoOfWheels(self):
        return 6
class Auto(Vehicle):   
    def getNoOfWheels(self):
        return 3

b=Bus()
print(b.getNoOfWheels())
a=Auto()
print(a.getNoOfWheels())