class Mother: 
    mothername = "" 
    def mother(self): 
        print(self.mothername) 
class Father: 
    fathername = "" 
    def father(self): 
        print(self.fathername) 
class Son(Mother, Father): 
    def parents(self): 
        print("Father :", self.fathername) 
        print("Mother :", self.mothername) 
s1 = Son() 
s1.fathername = "RAM" 
s1.mothername = "SITA" 
s1.parents() 