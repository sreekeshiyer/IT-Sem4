# create a Color class
class Color:
  # constructor 
  def __init__(self):
    # object attributes
    self.name = 'Green'
    self.lg = self.Lightgreen()
    
  def show(self):
    print("Name:", self.name)
    
  # create Lightgreen class
  class Lightgreen:
     def __init__(self):
        self.name = 'Light Green'
        self.code = '024avc'
    
     def display(self):
        print("Name:", self.name)
        print("Code:", self.code)
  
# create Color class object
outer = Color()
outer.show()
  
# create a Lightgreen inner class object
g = outer.lg
g.display()