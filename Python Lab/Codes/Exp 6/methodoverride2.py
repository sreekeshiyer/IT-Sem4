class Parent1():
    def show(self):
        print("Inside Parent1")
class Parent2():
    def display(self):
        print("Inside Parent2")
class Child(Parent1, Parent2):
    def show(self):
        print("Inside Child")
obj = Child()
obj.show()
obj.display()