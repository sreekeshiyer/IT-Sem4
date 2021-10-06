#definition of the class starts here  
class Person:  
    #initializing the variables  
    name = ""  
    age = 0  
      
    #defining constructor  
    def __init__(self, personName, personAge):  
        self.name = personName  
        self.age = personAge  
  
    #defining class methods  
    def showName(self):  
        print(self.name)  
  
    def showAge(self):  
        print(self.age)  
          
    #end of the class definition  
  
# Create an object of the class  
person1 = Person("Aamir", 20)  

#Create another object of the same class  
person2 = Person("Ansari", 102)

#call member methods of the objects
person1.showAge()  
person2.showName() 
