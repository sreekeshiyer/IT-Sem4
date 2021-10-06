import math
 
a = int(input("Enter value of coefficient a: "))
b = int(input("Enter value of coefficient b: "))
c = int(input("Enter value of coefficient c: "))
if a==0:
    print("Invalid Quadratic Equation!")
else:
    dis = b * b - 4 * a * c  
    sqrt_val = math.sqrt(abs(dis))  
    if dis >= 0:  
        print("Real Roots are:")  
        print((-b + sqrt_val)/(2 * a))  
        print((-b - sqrt_val)/(2 * a))  
    else: 
        print("There are no real roots!")  
