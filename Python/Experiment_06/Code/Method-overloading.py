class Employee:
    def Hello_Emp(self,e_name=None):
        if e_name is not None:
            print("Hello "+e_name)
        else:
            print("Hello ")

emp1=Employee()
emp1.Hello_Emp()
emp1.Hello_Emp("Aamir")
