def getGcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def getLcm(x, y):
    lcm = (x*y) // getGcd(x,y)
    return lcm

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("The L.C.M. is", getLcm(num1, num2))
