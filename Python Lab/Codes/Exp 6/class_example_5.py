# create a outer class
class MyClass:  
  def __init__(self):
     # create a inner class object
     self.inner = self.Inner()
  def show(self):
     print('This is an outer class')
  
  # create a 1st inner class 
  class Inner:
    def __init__(self):
      # create a inner class of inner class object
      self.innerclassofinner = self.Innerclassofinner()
    def show(self):
      print('This is the inner class')
    
    # create a inner class of inner
    class Innerclassofinner:    
      def show(self):
         print()         
      def show(self):
         print('This is an inner class of inner class')
  
# create a outer class object 
outer = MyClass()
outer.show()
# create a inner class object 
obj1 = outer.inner
obj1.show()
# create a inner class of inner class object
obj2 = outer.inner.innerclassofinner
obj2.show()