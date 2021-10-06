from abc import ABC, abstractmethod
class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass

class Triangle(Polygon):
    def noofsides(self):
        print("I have 3 sides")
 
class Quadrilateral(Polygon):
    def noofsides(self):
        print("I have 4 sides")

class Pentagon(Polygon):
    def noofsides(self):
        print("I have 5 sides")
 
class Hexagon(Polygon):
    def noofsides(self):
        print("I have 6 sides")

R1 = Triangle()
R1.noofsides()
R2 = Quadrilateral()
R2.noofsides()
R3 = Pentagon()
R3.noofsides()
R4 = Hexagon()
R4.noofsides()