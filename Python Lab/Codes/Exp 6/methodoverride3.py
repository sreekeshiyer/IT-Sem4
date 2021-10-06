class Parent(): 
    def display(self):
        print("Inside Parent") 
class Child(Parent):
    def show(self):
        print("Inside Child")
class GrandChild(Child):
    def show(self):
        print("Inside GrandChild")
g = GrandChild()   
g.show()
g.display()