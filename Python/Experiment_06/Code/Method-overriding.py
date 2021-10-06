class A:
    def fun1(self):
        print('feature_1 of class A')
         
    def fun2(self):
        print('feature_2 of class A')
     
 
class B(A):
    # Modified function that is
    # already exist in class A
    def fun1(self):
        print('Modified feature_1 of class A by class B')   
         
    def fun3(self):
        print('feature_3 of class B')
         
# Create instance
obj = B()
     
# Call the override function
obj.fun1()
