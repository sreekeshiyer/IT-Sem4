class Grandfather: 
    def __init__(self, grandfathername): 
        self.grandfathername = grandfathername 
class Father(Grandfather): 
    def __init__(self, fathername, grandfathername): 
        self.fathername = fathername 
        Grandfather.__init__(self, grandfathername) 
class Son(Father): 
    def __init__(self,sonname, fathername, grandfathername): 
        self.sonname = sonname 
        Father.__init__(self, fathername, grandfathername) 
    def print_name(self): 
        print('Grandfather name :', self.grandfathername) 
        print("Father name :", self.fathername) 
        print("Son name :", self.sonname) 
s1 = Son('Prince', 'Rampal', 'Lal mani') 
print(s1.grandfathername) 
s1.print_name() 