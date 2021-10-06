# create outer class
class Doctors:  
  def __init__(self):
     self.name = 'Doctor'
     self.den = self.Dentist()
     self.car = self.Cardiologist()
   
  def show(self):
    print('In outer class')
    print('Name:', self.name)
  
  # create a 1st Inner class
  class Dentist:
      def __init__(self):
         self.name = 'Dr. Savita'
         self.degree = 'BDS'
      def display(self):
         print('In inner class 1')
         print("Name:", self.name)
         print("Degree:", self.degree)
  
  # create a 2nd Inner class
  class Cardiologist:
      def __init__(self):
         self.name = 'Dr. Amit'
         self.degree = 'DM'
      def display(self):
         print('In inner class 2')
         print("Name:", self.name)
         print("Degree:", self.degree)
  
# create a object of outer class
outer = Doctors()
outer.show()
  
# create a object of 1st inner class
d1 = outer.den
  
# create a object of 2nd inner class
d2 = outer.car
print()
d1.display()
print()
d2.display()