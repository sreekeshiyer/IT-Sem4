class MyClass:   
    x = 0 
    #parameterized constructor 
    def __init__(self, s): 
        self.x = s   
    def display(self):   
        return self.x  
obj = MyClass("Welcome") 
print(obj.display()) 