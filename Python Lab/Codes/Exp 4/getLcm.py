from getHcf import computeGCD

def compute_lcm(x, y):
    lcm = (x*y)//computeGCD(x,y)
    return lcm

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("LCM of",num1,"and",num2,"=", compute_lcm(num1, num2))