class Employee:
  def __init__(self,name,salary):
    self.name=name
    self.salary = salary
  def __mul__(self,other):
    return self.salary * other.days
class Attendance:
  def __init__(self, name, days):
    self.name = name
    self.days = days
obj1 = Employee('Srinu',500.0)
obj2 = Attendance('Srinu',25)
print("Salary =",obj1*obj2)